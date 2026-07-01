#!/usr/bin/env python3
"""Busca PubMed vía E-utilities con paginación y backoff exponencial.

Lee `<project_dir>/searches/pubmed_query.txt` y escribe
`<project_dir>/searches/raw_pubmed.json` con normalización al schema común.

Persiste cursor en `<project_dir>/project_state.json` para reanudación.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests
import yaml

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
RETMAX = 200
USER_AGENT = "systematic-review-skill/1.0 (Claude Code)"


def backoff_get(url: str, params: dict, max_retries: int = 5, base_delay: float = 1.0) -> requests.Response:
    for attempt in range(max_retries):
        r = requests.get(url, params=params, headers={"User-Agent": USER_AGENT}, timeout=60)
        if r.status_code == 200:
            return r
        if r.status_code == 429 or r.status_code >= 500:
            delay = base_delay * (2 ** attempt)
            print(f"[pubmed] {r.status_code} → esperando {delay}s (intento {attempt+1}/{max_retries})", file=sys.stderr)
            time.sleep(delay)
            continue
        r.raise_for_status()
    raise RuntimeError(f"[pubmed] falló tras {max_retries} intentos: {r.status_code}")


def esearch(query: str, retstart: int, retmax: int, api_key: str | None, email: str | None) -> dict:
    params = {
        "db": "pubmed",
        "term": query,
        "retstart": retstart,
        "retmax": retmax,
        "retmode": "json",
        "tool": "systematic-review-skill",
    }
    if email:
        params["email"] = email
    if api_key:
        params["api_key"] = api_key
    return backoff_get(f"{EUTILS}/esearch.fcgi", params).json()["esearchresult"]


def efetch(pmids: list[str], api_key: str | None, email: str | None) -> str:
    if not pmids:
        return ""
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "rettype": "abstract",
        "retmode": "xml",
        "tool": "systematic-review-skill",
    }
    if email:
        params["email"] = email
    if api_key:
        params["api_key"] = api_key
    return backoff_get(f"{EUTILS}/efetch.fcgi", params).text


def parse_efetch_xml(xml_text: str) -> list[dict]:
    """Parser ligero del XML de PubMed sin dependencia externa fuerte."""
    from xml.etree import ElementTree as ET
    out = []
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"[pubmed] XML parse error: {e}", file=sys.stderr)
        return []
    for art in root.findall(".//PubmedArticle"):
        pmid_el = art.find(".//PMID")
        pmid = pmid_el.text if pmid_el is not None else ""

        title_el = art.find(".//ArticleTitle")
        title = "".join(title_el.itertext()).strip() if title_el is not None else ""

        abstract_parts = [
            ("".join(a.itertext())).strip()
            for a in art.findall(".//Abstract/AbstractText")
        ]
        abstract = " ".join(p for p in abstract_parts if p)

        authors = []
        for a in art.findall(".//Author"):
            ln = a.find("LastName")
            fn = a.find("ForeName")
            if ln is not None:
                name = (fn.text + " " if fn is not None and fn.text else "") + (ln.text or "")
                authors.append(name.strip())

        year_el = art.find(".//PubDate/Year")
        if year_el is None:
            year_el = art.find(".//PubDate/MedlineDate")
        year = year_el.text[:4] if year_el is not None and year_el.text else ""

        journal_el = art.find(".//Journal/Title")
        journal = journal_el.text if journal_el is not None else ""

        doi = ""
        for aid in art.findall(".//ArticleId"):
            if aid.get("IdType") == "doi" and aid.text:
                doi = aid.text.strip()
                break

        kw = [k.text for k in art.findall(".//Keyword") if k.text]

        out.append({
            "source": "pubmed",
            "source_id": pmid,
            "doi": doi,
            "title": title,
            "authors": authors,
            "year": year,
            "journal": journal,
            "abstract": abstract,
            "keywords": kw,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
        })
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    p.add_argument("--max", type=int, default=10000)
    args = p.parse_args()

    proj = Path(args.project_dir)
    query = (proj / "searches" / "pubmed_query.txt").read_text(encoding="utf-8").strip()
    if not query:
        print("[pubmed] query vacío", file=sys.stderr)
        return 1

    cfg = yaml.safe_load((proj / "project_config.yaml").read_text())
    api_key = (cfg.get("api_keys") or {}).get("ncbi_api_key") or None
    email = (cfg.get("api_keys") or {}).get("ncbi_email") or None

    state_path = proj / "project_state.json"
    state = json.loads(state_path.read_text())
    cursor = state.get("search_cursors", {}).get("pubmed", 0)
    if cursor == "complete":
        print("[pubmed] ya completado", file=sys.stderr)
        return 0

    raw_path = proj / "searches" / "raw_pubmed.json"
    records: list[dict] = json.loads(raw_path.read_text()) if raw_path.exists() else []

    # esearch inicial para saber total
    head = esearch(query, retstart=int(cursor), retmax=RETMAX, api_key=api_key, email=email)
    total = min(int(head["count"]), args.max)
    print(f"[pubmed] total hits: {head['count']} (cap: {args.max})", file=sys.stderr)

    while int(cursor) < total:
        retstart = int(cursor)
        sr = esearch(query, retstart=retstart, retmax=RETMAX, api_key=api_key, email=email)
        ids = sr.get("idlist", [])
        if not ids:
            break
        # delay para respetar 3 req/s sin api key, 10 con key
        time.sleep(0.34 if not api_key else 0.11)
        xml = efetch(ids, api_key=api_key, email=email)
        batch = parse_efetch_xml(xml)
        records.extend(batch)

        # persiste batch a batch
        raw_path.write_text(json.dumps(records, indent=2, ensure_ascii=False))
        cursor = retstart + len(ids)
        state["search_cursors"]["pubmed"] = cursor
        state_path.write_text(json.dumps(state, indent=2))
        print(f"[pubmed] avanzado a {cursor}/{total}", file=sys.stderr)
        time.sleep(0.34 if not api_key else 0.11)

    state["search_cursors"]["pubmed"] = "complete"
    state.setdefault("counts", {})["identificados_pubmed"] = len(records)
    state_path.write_text(json.dumps(state, indent=2))
    print(json.dumps({"ok": True, "count": len(records)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
