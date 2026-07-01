#!/usr/bin/env python3
"""Busca Semantic Scholar Graph API bulk con cursor pagination y backoff.

Lee `<project_dir>/searches/semantic_scholar_query.txt`.
Escribe `<project_dir>/searches/raw_semantic_scholar.json`.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests
import yaml

API = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "title,abstract,authors,year,journal,externalIds,publicationTypes,referenceCount,citationCount"
USER_AGENT = "systematic-review-skill/1.0"


def backoff_get(url: str, params: dict, headers: dict, max_retries: int = 5) -> requests.Response:
    for attempt in range(max_retries):
        r = requests.get(url, params=params, headers=headers, timeout=60)
        if r.status_code == 200:
            return r
        if r.status_code == 429:
            delay = float(r.headers.get("retry-after", 60))
            print(f"[s2] 429 → esperando {delay}s (intento {attempt+1}/{max_retries})", file=sys.stderr)
            time.sleep(delay)
            continue
        if r.status_code >= 500:
            delay = 2 ** attempt
            time.sleep(delay)
            continue
        r.raise_for_status()
    raise RuntimeError(f"[s2] falló tras {max_retries} intentos")


def normalize(p: dict) -> dict:
    ext = p.get("externalIds") or {}
    return {
        "source": "semantic_scholar",
        "source_id": p.get("paperId", ""),
        "doi": ext.get("DOI", ""),
        "title": p.get("title") or "",
        "authors": [a.get("name", "") for a in (p.get("authors") or [])],
        "year": str(p.get("year") or ""),
        "journal": (p.get("journal") or {}).get("name", "") if p.get("journal") else "",
        "abstract": p.get("abstract") or "",
        "keywords": p.get("publicationTypes") or [],
        "url": f"https://www.semanticscholar.org/paper/{p.get('paperId','')}",
        "citation_count": p.get("citationCount", 0),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("project_dir")
    ap.add_argument("--max", type=int, default=10000)
    args = ap.parse_args()

    proj = Path(args.project_dir)
    query = (proj / "searches" / "semantic_scholar_query.txt").read_text(encoding="utf-8").strip()
    cfg = yaml.safe_load((proj / "project_config.yaml").read_text())
    api_key = (cfg.get("api_keys") or {}).get("semantic_scholar") or ""
    year_range = cfg.get("review", {}).get("time_window") or {}
    yr_start = year_range.get("start")
    yr_end = year_range.get("end")

    state_path = proj / "project_state.json"
    state = json.loads(state_path.read_text())
    cursor = state.get("search_cursors", {}).get("semantic_scholar")
    if cursor == "complete":
        print("[s2] ya completado", file=sys.stderr)
        return 0

    raw_path = proj / "searches" / "raw_semantic_scholar.json"
    records: list[dict] = json.loads(raw_path.read_text()) if raw_path.exists() else []

    params = {"query": query, "fields": FIELDS, "limit": 1000}
    if yr_start or yr_end:
        params["year"] = f"{yr_start or ''}-{yr_end or ''}"
    if cursor and cursor != "complete":
        params["token"] = cursor

    headers = {"User-Agent": USER_AGENT}
    if api_key:
        headers["x-api-key"] = api_key

    while True:
        r = backoff_get(API, params=params, headers=headers)
        body = r.json()
        data = body.get("data", []) or []
        records.extend(normalize(p) for p in data)
        raw_path.write_text(json.dumps(records, indent=2, ensure_ascii=False))

        token = body.get("token")
        state["search_cursors"]["semantic_scholar"] = token or "complete"
        state_path.write_text(json.dumps(state, indent=2))

        print(f"[s2] acumulado {len(records)} (token={token})", file=sys.stderr)
        if not token or len(records) >= args.max:
            break
        params["token"] = token
        time.sleep(1.0 if not api_key else 0.2)

    state["search_cursors"]["semantic_scholar"] = "complete"
    state.setdefault("counts", {})["identificados_semantic_scholar"] = len(records)
    state_path.write_text(json.dumps(state, indent=2))
    print(json.dumps({"ok": True, "count": len(records)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
