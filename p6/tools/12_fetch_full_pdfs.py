#!/usr/bin/env python3
"""
Fetch legally available full-text PDFs for a meta-analysis extraction sheet.
Sources: OpenAlex, Unpaywall, Crossref metadata links, and DOI landing pages.

Usage:
  python fetch_full_pdfs.py --input master_extraction_20260518_autocoded.xlsx --email your_email@example.com

Outputs:
  - pdfs/*.pdf
  - pdf_fetch_log.csv
  - master_extraction_with_pdf_status.xlsx
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import quote, urlparse

import pandas as pd
import requests


DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
PDF_MAGIC = b"%PDF"


@dataclass
class CandidateURL:
    doi: str
    title: str
    source: str
    url: str
    evidence: str
    is_oa: Optional[bool] = None
    license: Optional[str] = None
    version: Optional[str] = None


@dataclass
class FetchResult:
    row_index: int
    study_id: str
    title: str
    doi: str
    status: str
    pdf_path: str
    best_pdf_url: str
    source: str
    evidence: str
    is_oa: str
    license: str
    version: str
    http_status: str
    notes: str


def normalize_doi(value: Any) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    if not text or text.lower() in {"nan", "none", "nr"}:
        return ""
    text = text.replace("https://doi.org/", "").replace("http://dx.doi.org/", "").replace("doi:", "")
    match = DOI_RE.search(text)
    return match.group(0).rstrip(".,;)").lower() if match else ""


def safe_filename(study_id: str, doi: str, title: str) -> str:
    base = study_id or doi or title[:80] or "paper"
    base = re.sub(r"[^A-Za-z0-9._-]+", "_", base).strip("_")[:120]
    digest = hashlib.md5((doi or title).encode("utf-8", errors="ignore")).hexdigest()[:8]
    return f"{base}_{digest}.pdf"


def request_json(session: requests.Session, url: str, headers: Dict[str, str], timeout: int = 30) -> Tuple[int, Optional[Dict[str, Any]]]:
    try:
        r = session.get(url, headers=headers, timeout=timeout)
        if r.status_code == 200:
            return r.status_code, r.json()
        return r.status_code, None
    except Exception:
        return 0, None


def from_openalex(session: requests.Session, doi: str, title: str, headers: Dict[str, str]) -> List[CandidateURL]:
    candidates: List[CandidateURL] = []
    if not doi:
        return candidates
    url = f"https://api.openalex.org/works/https://doi.org/{quote(doi, safe='') }"
    status, data = request_json(session, url, headers)
    if not data:
        return candidates

    oa = data.get("open_access") or {}
    primary = data.get("primary_location") or {}
    best = data.get("best_oa_location") or {}
    locations = data.get("locations") or []

    for label, loc in [("best_oa_location", best), ("primary_location", primary)]:
        if isinstance(loc, dict):
            pdf_url = loc.get("pdf_url")
            landing_url = loc.get("landing_page_url")
            if pdf_url:
                candidates.append(CandidateURL(doi, title, "OpenAlex", pdf_url, label, oa.get("is_oa"), loc.get("license"), loc.get("version")))
            elif landing_url and ".pdf" in landing_url.lower():
                candidates.append(CandidateURL(doi, title, "OpenAlex", landing_url, f"{label}:landing_page_url_pdf", oa.get("is_oa"), loc.get("license"), loc.get("version")))

    for loc in locations:
        if not isinstance(loc, dict):
            continue
        pdf_url = loc.get("pdf_url")
        if pdf_url:
            candidates.append(CandidateURL(doi, title, "OpenAlex", pdf_url, "locations.pdf_url", oa.get("is_oa"), loc.get("license"), loc.get("version")))
    return candidates


def from_unpaywall(session: requests.Session, doi: str, title: str, email: str, headers: Dict[str, str]) -> List[CandidateURL]:
    candidates: List[CandidateURL] = []
    if not doi or not email:
        return candidates
    url = f"https://api.unpaywall.org/v2/{quote(doi, safe='')}?email={quote(email)}"
    status, data = request_json(session, url, headers)
    if not data:
        return candidates

    best = data.get("best_oa_location") or {}
    oa_locations = data.get("oa_locations") or []
    for label, loc in [("best_oa_location", best), *[("oa_locations", x) for x in oa_locations]]:
        if not isinstance(loc, dict):
            continue
        pdf_url = loc.get("url_for_pdf")
        landing = loc.get("url")
        if pdf_url:
            candidates.append(CandidateURL(doi, title, "Unpaywall", pdf_url, label, data.get("is_oa"), loc.get("license"), loc.get("version")))
        elif landing and ".pdf" in landing.lower():
            candidates.append(CandidateURL(doi, title, "Unpaywall", landing, f"{label}:url_pdf", data.get("is_oa"), loc.get("license"), loc.get("version")))
    return candidates


def from_crossref(session: requests.Session, doi: str, title: str, headers: Dict[str, str]) -> List[CandidateURL]:
    candidates: List[CandidateURL] = []
    if not doi:
        return candidates
    url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
    status, data = request_json(session, url, headers)
    if not data:
        return candidates
    msg = data.get("message", {})
    for link in msg.get("link", []) or []:
        if not isinstance(link, dict):
            continue
        content_type = str(link.get("content-type", "")).lower()
        candidate_url = link.get("URL") or link.get("url")
        if candidate_url and ("pdf" in content_type or ".pdf" in candidate_url.lower()):
            candidates.append(CandidateURL(doi, title, "Crossref", candidate_url, f"link:{content_type}", None, None, None))
    return candidates


def looks_like_pdf(response: requests.Response, content: bytes) -> bool:
    content_type = response.headers.get("Content-Type", "").lower()
    return content.startswith(PDF_MAGIC) or "application/pdf" in content_type or response.url.lower().split("?")[0].endswith(".pdf")


def download_pdf(session: requests.Session, candidate: CandidateURL, out_path: Path, headers: Dict[str, str], min_bytes: int = 5000) -> Tuple[bool, str, str]:
    try:
        with session.get(candidate.url, headers=headers, timeout=60, stream=True, allow_redirects=True) as r:
            status = str(r.status_code)
            if r.status_code != 200:
                return False, status, f"HTTP {status}"
            first = next(r.iter_content(chunk_size=8192), b"")
            if not looks_like_pdf(r, first):
                return False, status, f"not_pdf content-type={r.headers.get('Content-Type', '')} final_url={r.url}"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            size = 0
            with out_path.open("wb") as f:
                f.write(first)
                size += len(first)
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        size += len(chunk)
            if size < min_bytes:
                out_path.unlink(missing_ok=True)
                return False, status, f"too_small {size} bytes"
            return True, status, f"downloaded {size} bytes"
    except Exception as e:
        return False, "0", repr(e)


def pick_doi_column(df: pd.DataFrame) -> Optional[str]:
    for c in df.columns:
        if str(c).strip().lower() in {"doi", "dois"}:
            return c
    for c in df.columns:
        if "doi" in str(c).lower():
            return c
    return None


def pick_title_column(df: pd.DataFrame) -> Optional[str]:
    for name in ["title", "article_title", "paper_title", "study_title"]:
        for c in df.columns:
            if str(c).strip().lower() == name:
                return c
    for c in df.columns:
        if "title" in str(c).lower():
            return c
    return None


def pick_id_column(df: pd.DataFrame) -> Optional[str]:
    for name in ["study_id", "id", "paper_id", "record_id"]:
        for c in df.columns:
            if str(c).strip().lower() == name:
                return c
    return None


def dedupe_candidates(candidates: Iterable[CandidateURL]) -> List[CandidateURL]:
    seen = set()
    out = []
    for c in candidates:
        key = c.url.strip()
        if key and key not in seen:
            seen.add(key)
            out.append(c)
    # Prefer OA, publishedVersion, and URLs that visibly end with PDF.
    def score(c: CandidateURL) -> Tuple[int, int, int]:
        return (1 if c.is_oa else 0, 1 if str(c.version).lower() == "publishedversion" else 0, 1 if ".pdf" in c.url.lower() else 0)
    return sorted(out, key=score, reverse=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Input .xlsx or .csv extraction file")
    ap.add_argument("--email", required=True, help="Your email for polite API use and Unpaywall")
    ap.add_argument("--outdir", default="pdfs", help="PDF output folder")
    ap.add_argument("--delay", type=float, default=1.0, help="Delay between records in seconds")
    ap.add_argument("--max", type=int, default=0, help="Limit number of rows for testing; 0 = all")
    ap.add_argument("--skip-existing", action="store_true", help="Skip rows when target PDF exists")
    args = ap.parse_args()

    in_path = Path(args.input)
    if in_path.suffix.lower() in {".xlsx", ".xls"}:
        df = pd.read_excel(in_path)
    else:
        df = pd.read_csv(in_path)

    doi_col = pick_doi_column(df)
    title_col = pick_title_column(df)
    id_col = pick_id_column(df)
    if not doi_col:
        raise ValueError("No DOI column found. Rename your DOI column to 'DOI'.")

    headers = {
        "User-Agent": f"MetaAnalysisPDFPipeline/1.0 (mailto:{args.email})",
        "Accept": "application/pdf,application/json,text/html;q=0.9,*/*;q=0.8",
    }
    session = requests.Session()
    results: List[FetchResult] = []
    outdir = Path(args.outdir)

    rows = df.iterrows()
    if args.max and args.max > 0:
        rows = list(rows)[: args.max]

    for i, row in rows:
        doi = normalize_doi(row.get(doi_col, ""))
        title = str(row.get(title_col, "") if title_col else "").strip()
        study_id = str(row.get(id_col, "") if id_col else f"row_{i+1}").strip()
        if not doi:
            results.append(FetchResult(i, study_id, title, "", "no_doi", "", "", "", "", "", "", "", "", "No DOI available"))
            continue

        filename = safe_filename(study_id, doi, title)
        out_path = outdir / filename
        if args.skip_existing and out_path.exists():
            results.append(FetchResult(i, study_id, title, doi, "existing", str(out_path), "", "", "", "", "", "", "", "Existing PDF skipped"))
            continue

        candidates = []
        candidates += from_openalex(session, doi, title, headers)
        candidates += from_unpaywall(session, doi, title, args.email, headers)
        candidates += from_crossref(session, doi, title, headers)
        candidates = dedupe_candidates(candidates)

        if not candidates:
            results.append(FetchResult(i, study_id, title, doi, "no_pdf_url_found", "", "", "", "", "", "", "", "", "No OA/direct PDF URL found"))
            time.sleep(args.delay)
            continue

        success = False
        last_status = ""
        notes = []
        chosen = candidates[0]
        for cand in candidates:
            ok, http_status, note = download_pdf(session, cand, out_path, headers)
            last_status = http_status
            notes.append(f"{cand.source}:{note}")
            if ok:
                chosen = cand
                success = True
                break

        results.append(FetchResult(
            i, study_id, title, doi,
            "downloaded" if success else "pdf_url_failed",
            str(out_path) if success else "",
            chosen.url,
            chosen.source,
            chosen.evidence,
            str(chosen.is_oa or ""),
            str(chosen.license or ""),
            str(chosen.version or ""),
            last_status,
            " | ".join(notes)[:1000],
        ))
        print(f"[{i+1}/{len(df)}] {doi} -> {results[-1].status} via {results[-1].source}")
        time.sleep(args.delay)

    log = pd.DataFrame([asdict(r) for r in results])
    log.to_csv("pdf_fetch_log.csv", index=False, encoding="utf-8-sig")

    # Merge status back to workbook by original row index.
    df_out = df.copy()
    merge_cols = ["status", "pdf_path", "best_pdf_url", "source", "evidence", "is_oa", "license", "version", "notes"]
    for c in merge_cols:
        df_out[f"pdf_{c}"] = ""
    for r in results:
        for c in merge_cols:
            df_out.loc[r.row_index, f"pdf_{c}"] = getattr(r, c)

    with pd.ExcelWriter("master_extraction_with_pdf_status.xlsx", engine="openpyxl") as writer:
        df_out.to_excel(writer, index=False, sheet_name="Extraction_PDF_Status")
        log.to_excel(writer, index=False, sheet_name="PDF_Fetch_Log")

    print("\nDone.")
    print("Downloaded:", int((log["status"] == "downloaded").sum()))
    print("No DOI:", int((log["status"] == "no_doi").sum()))
    print("No PDF URL:", int((log["status"] == "no_pdf_url_found").sum()))
    print("Failed URL:", int((log["status"] == "pdf_url_failed").sum()))
    print("Outputs: pdfs/, pdf_fetch_log.csv, master_extraction_with_pdf_status.xlsx")


if __name__ == "__main__":
    main()
