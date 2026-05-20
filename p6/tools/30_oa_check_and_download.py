#!/usr/bin/env python3
"""
30_oa_check_and_download.py
Check Open Access availability for worklist DOIs via Unpaywall + OpenAlex APIs,
then download freely available PDFs.

Usage:
  python3 30_oa_check_and_download.py \
      --input  p6/tools/results/extraction_worklist_v11_20260519.csv \
      --output p6/tools/results/oa_check_20260519.csv \
      --pdfs   p6/tools/pdfs/ \
      --email  seranguyenct@gmail.com
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import os
import time
from pathlib import Path
from typing import Optional

import requests

EMAIL = "seranguyenct@gmail.com"
DELAY = 0.5          # seconds between API calls — polite rate
TIMEOUT = 20         # per-request timeout
PDF_MAGIC = b"%PDF"

HEADERS = {"User-Agent": f"P6-meta-analysis-extraction/1.0 (mailto:{EMAIL})"}


# ── Unpaywall ────────────────────────────────────────────────────────────────

def _unpaywall(doi: str) -> dict:
    url = f"https://api.unpaywall.org/v2/{doi}?email={EMAIL}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return {}


def _best_oa_url_unpaywall(data: dict) -> tuple[str, str, str]:
    """Return (pdf_url, host_type, license) from Unpaywall response."""
    best = data.get("best_oa_location") or {}
    url = best.get("url_for_pdf") or best.get("url") or ""
    host = best.get("host_type", "")
    lic  = best.get("license") or data.get("oa_status", "")
    # Also check locations list
    if not url:
        for loc in data.get("oa_locations", []):
            if loc.get("url_for_pdf"):
                url = loc["url_for_pdf"]
                host = loc.get("host_type", "")
                lic  = loc.get("license", "")
                break
    return url, host, lic


# ── OpenAlex ─────────────────────────────────────────────────────────────────

def _openalex(doi: str) -> dict:
    encoded = requests.utils.quote(doi, safe="")
    url = f"https://api.openalex.org/works/https://doi.org/{encoded}?mailto={EMAIL}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return {}


def _best_oa_url_openalex(data: dict) -> tuple[str, str]:
    """Return (pdf_url, oa_status) from OpenAlex response."""
    oa = data.get("open_access", {})
    pdf_url = oa.get("oa_url") or ""
    status  = oa.get("oa_status", "")
    # Check primary_location
    for loc in ([data.get("primary_location")] + data.get("locations", [])):
        if not loc:
            continue
        if loc.get("pdf_url"):
            pdf_url = loc["pdf_url"]
            break
    return pdf_url, status


# ── PDF download ─────────────────────────────────────────────────────────────

def _download_pdf(url: str, dest: Path) -> bool:
    if dest.exists():
        return True
    try:
        r = requests.get(url, headers=HEADERS, timeout=60, stream=True)
        if r.status_code != 200:
            return False
        # Check content type
        ct = r.headers.get("content-type", "")
        data = r.content
        if PDF_MAGIC not in data[:16]:
            return False
        dest.write_bytes(data)
        return True
    except Exception:
        return False


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    global EMAIL
    ap = argparse.ArgumentParser()
    ap.add_argument("--input",  default="p6/tools/results/fulltext_to_extraction_tracker_v2.csv")
    ap.add_argument("--output", default="p6/tools/results/oa_check_20260519.csv")
    ap.add_argument("--pdfs",   default="p6/tools/pdfs/")
    ap.add_argument("--email",  default=EMAIL)
    ap.add_argument("--no-download", action="store_true", help="Check OA only, skip PDF downloads")
    ap.add_argument("--limit",  type=int, default=0, help="Process only first N DOIs (0=all)")
    args = ap.parse_args()

    EMAIL = args.email

    pdf_dir = Path(args.pdfs)
    pdf_dir.mkdir(parents=True, exist_ok=True)

    # Load worklist
    with open(args.input, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    doi_rows = [r for r in rows if r.get("doi", "").strip()]
    if args.limit:
        doi_rows = doi_rows[:args.limit]

    print(f"Checking {len(doi_rows)} papers with DOI (out of {len(rows)} total)…")

    results = []
    oa_count = 0
    dl_ok = 0
    dl_fail = 0

    for i, row in enumerate(doi_rows, 1):
        doi   = row["doi"].strip()
        seq   = row.get("seq", str(i))
        title = row.get("title", "")[:60]

        # 1) Try Unpaywall
        time.sleep(DELAY)
        udata = _unpaywall(doi)
        u_pdf, u_host, u_lic = _best_oa_url_unpaywall(udata) if udata else ("", "", "")
        u_is_oa = udata.get("is_oa", False) if udata else False

        # 2) Try OpenAlex (only if Unpaywall has no PDF)
        oa_pdf = u_pdf
        oa_status = u_lic or ("oa" if u_is_oa else "closed")
        if not oa_pdf:
            time.sleep(DELAY)
            adata = _openalex(doi)
            oa_pdf, oa_status = _best_oa_url_openalex(adata) if adata else ("", "")

        is_oa = bool(oa_pdf) or u_is_oa
        if is_oa:
            oa_count += 1

        # 3) Download PDF if available
        pdf_path = ""
        dl_status = "NO_OA"
        if oa_pdf and not args.no_download:
            safe = hashlib.md5(doi.encode()).hexdigest()[:12]
            dest = pdf_dir / f"{seq}_{safe}.pdf"
            ok = _download_pdf(oa_pdf, dest)
            if ok:
                dl_status = "DOWNLOADED"
                pdf_path  = str(dest)
                dl_ok += 1
            else:
                dl_status = "DOWNLOAD_FAILED"
                dl_fail += 1
        elif oa_pdf and args.no_download:
            dl_status = "OA_URL_FOUND"

        results.append({
            "seq":        seq,
            "doi":        doi,
            "title":      row.get("title", ""),
            "journal":    row.get("journal", ""),
            "year":       row.get("year", ""),
            "is_oa":      "Y" if is_oa else "N",
            "oa_url":     oa_pdf,
            "oa_status":  oa_status,
            "host_type":  u_host,
            "dl_status":  dl_status,
            "pdf_path":   pdf_path,
        })

        if i % 50 == 0 or i == len(doi_rows):
            pct = i / len(doi_rows) * 100
            print(f"  [{i}/{len(doi_rows)} {pct:.0f}%] OA so far: {oa_count}  "
                  f"Downloaded: {dl_ok}  Failed: {dl_fail}")

    # Write results
    out_path = Path(args.output)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        w.writeheader()
        w.writerows(results)

    # Summary
    print(f"\n{'='*55}")
    print(f"RESULTS — {len(doi_rows)} papers with DOI checked")
    print(f"  Open Access found : {oa_count} / {len(doi_rows)} ({oa_count/len(doi_rows)*100:.1f}%)")
    if not args.no_download:
        print(f"  PDFs downloaded   : {dl_ok}")
        print(f"  Download failed   : {dl_fail}")
        print(f"  No OA found       : {len(doi_rows) - oa_count}")
    print(f"  Output CSV        : {out_path}")
    print(f"  PDFs folder       : {pdf_dir} ({dl_ok} files)")
    print(f"{'='*55}")

    # Papers WITHOUT DOI
    no_doi = len(rows) - len([r for r in rows if r.get("doi", "").strip()])
    print(f"\nRemaining {no_doi} papers without DOI → need manual Google Scholar / ResearchGate lookup")


if __name__ == "__main__":
    main()
