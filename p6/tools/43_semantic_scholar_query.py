#!/usr/bin/env python3
"""
43_semantic_scholar_query.py — Fallback PDF lookup via Semantic Scholar API
Run via GitHub Actions (server blocks external APIs).

Queries S2 for papers where Unpaywall found no PDF URL.
S2 often indexes PDFs from arXiv, institutional repos, and author pages
that Unpaywall misses.

Input:  p6/tools/results/oa_manifest_20260520.csv     (Unpaywall output)
        p6/tools/results/extraction_queue_20260520.csv (for title/year)
Output: p6/tools/results/s2_manifest_YYYYMMDD.csv
        Also UPDATES oa_manifest with any new PDF links found

API: https://api.semanticscholar.org/graph/v1/paper/{doi}
     Fields: openAccessPdf, title, year, publicationTypes
     Rate: 100 req/5min unauthenticated → use 3s delay to stay safe
"""
import csv, sys, time, requests, argparse, re
from datetime import date
from pathlib import Path

S2_URL   = "https://api.semanticscholar.org/graph/v1/paper/{doi}"
S2_FIELDS = "openAccessPdf,title,year,externalIds"
DELAY    = 3.5   # seconds — 100 req/5min = 1 req/3s
DEFAULT_MANIFEST  = "p6/tools/results/oa_manifest_20260520.csv"
DEFAULT_QUEUE     = "p6/tools/results/extraction_queue_20260520.csv"
DEFAULT_OUTPUT    = f"p6/tools/results/s2_manifest_{date.today().strftime('%Y%m%d')}.csv"

HEADERS = {
    "User-Agent": "P6MetaAnalysis/1.0 (huongp1323001@gstudent.ctu.edu.vn; academic meta-analysis)"
}

OUT_COLS = ["seq", "doi", "title", "year", "s2_pdf_url", "s2_found", "error"]


def query_s2(doi: str) -> dict:
    try:
        r = requests.get(
            S2_URL.format(doi=doi.strip()),
            params={"fields": S2_FIELDS},
            headers=HEADERS,
            timeout=15
        )
        if r.status_code == 200:
            d = r.json()
            oa = d.get("openAccessPdf") or {}
            pdf_url = oa.get("url", "")
            return {"s2_pdf_url": pdf_url, "s2_found": "True" if pdf_url else "False", "error": ""}
        if r.status_code == 404:
            return {"s2_pdf_url": "", "s2_found": "False", "error": "not_found"}
        if r.status_code == 429:
            time.sleep(30)
            return {"s2_pdf_url": "", "s2_found": "False", "error": "rate_limited"}
        return {"s2_pdf_url": "", "s2_found": "False", "error": f"HTTP_{r.status_code}"}
    except Exception as e:
        return {"s2_pdf_url": "", "s2_found": "False", "error": str(e)[:60]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("--output",   default=DEFAULT_OUTPUT)
    parser.add_argument("--delay",    type=float, default=DELAY)
    parser.add_argument("--limit",    type=int, default=0,
                        help="Stop after N papers (0 = all). For testing.")
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    with open(args.manifest, newline="", encoding="utf-8") as f:
        manifest = list(csv.DictReader(f))
    manifest_cols = list(manifest[0].keys())
    manifest_by_seq = {r["seq"]: r for r in manifest}

    # Target: rows with no pdf_url and no repo_url (and have DOI)
    targets = [
        r for r in manifest
        if not r.get("pdf_url", "").strip()
        and not r.get("repo_url", "").strip()
        and r.get("doi", "").strip()
    ]

    if args.limit:
        targets = targets[:args.limit]
        print(f"[--limit] restricted to first {args.limit} targets", flush=True)

    print(f"Querying Semantic Scholar for {len(targets)} papers (no Unpaywall PDF)...", flush=True)
    print(f"Estimated time: {len(targets) * args.delay / 60:.1f} min", flush=True)

    results = []
    found = 0
    CHECKPOINT = 20  # save partial results every N papers

    def _save(partial_results):
        with open(args.output, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=OUT_COLS)
            w.writeheader()
            w.writerows(partial_results)

    for i, row in enumerate(targets, 1):
        doi = row["doi"].strip()
        s2 = query_s2(doi)

        entry = {
            "seq":       row["seq"],
            "doi":       doi,
            "title":     row.get("title", "")[:80],
            "year":      row.get("year", ""),
            "s2_pdf_url": s2["s2_pdf_url"],
            "s2_found":   s2["s2_found"],
            "error":      s2["error"],
        }
        results.append(entry)

        if s2["s2_pdf_url"]:
            found += 1
            if row["seq"] in manifest_by_seq:
                manifest_by_seq[row["seq"]]["pdf_url"]   = s2["s2_pdf_url"]
                manifest_by_seq[row["seq"]]["is_oa"]     = "True"
                manifest_by_seq[row["seq"]]["oa_status"] = (
                    manifest_by_seq[row["seq"]].get("oa_status", "") or "green"
                )

        if i % CHECKPOINT == 0:
            _save(results)
            print(f"  {i}/{len(targets)} | found: {found} | checkpoint saved", flush=True)
        elif i % 10 == 0:
            print(f"  {i}/{len(targets)} | S2 PDFs found: {found}", flush=True)

        time.sleep(args.delay)

    # Final write — S2 manifest
    _save(results)

    # Write updated OA manifest (with S2 PDFs merged in)
    with open(args.manifest, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=manifest_cols)
        w.writeheader()
        w.writerows(manifest)

    print(f"\n=== SEMANTIC SCHOLAR RESULTS ===")
    print(f"Queried:           {len(results)}")
    print(f"New PDF links:     {found}")
    errors = sum(1 for r in results if r["error"] and r["error"] != "not_found")
    print(f"Errors:            {errors}")
    not_found = sum(1 for r in results if r["error"] == "not_found")
    print(f"Not in S2:         {not_found}")
    print(f"S2 manifest:       {args.output}")
    print(f"Updated manifest:  {args.manifest}")


if __name__ == "__main__":
    main()
