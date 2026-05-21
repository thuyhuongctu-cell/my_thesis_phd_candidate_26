#!/usr/bin/env python3
"""
39_query_unpaywall.py — Query Unpaywall for OA status + PDF links
Run via GitHub Actions (server blocks external APIs).

Input:  p6/tools/results/extraction_queue_YYYYMMDD.csv
Output: p6/tools/results/oa_manifest_YYYYMMDD.csv

Columns out: seq, doi, title, year, is_oa, oa_status, pdf_url, repo_url, version, license
"""
import csv, sys, time, requests, argparse
from datetime import date
from pathlib import Path

EMAIL = "huongp1323001@gstudent.ctu.edu.vn"
UNPAYWALL_URL = "https://api.unpaywall.org/v2/{doi}"
DEFAULT_INPUT  = f"p6/tools/results/extraction_queue_20260520.csv"
DEFAULT_OUTPUT = f"p6/tools/results/oa_manifest_{date.today().strftime('%Y%m%d')}.csv"
DELAY = 0.15   # ~6 req/s — well within 100k/day limit

OUT_COLS = [
    "seq", "extraction_priority", "doi", "title", "year", "journal",
    "is_oa", "oa_status", "pdf_url", "repo_url", "version",
    "license", "host_type", "error"
]


def query_unpaywall(doi: str) -> dict:
    try:
        r = requests.get(
            UNPAYWALL_URL.format(doi=doi.strip()),
            params={"email": EMAIL},
            timeout=15
        )
        if r.status_code == 200:
            d = r.json()
            best = d.get("best_oa_location") or {}
            return {
                "is_oa":     str(d.get("is_oa", False)),
                "oa_status": d.get("oa_status", "unknown"),
                "pdf_url":   best.get("url_for_pdf") or "",
                "repo_url":  best.get("url") or "",
                "version":   best.get("version") or "",
                "license":   best.get("license") or "",
                "host_type": best.get("host_type") or "",
                "error":     "",
            }
        return {"is_oa": "", "oa_status": "", "pdf_url": "", "repo_url": "",
                "version": "", "license": "", "host_type": "",
                "error": f"HTTP {r.status_code}"}
    except Exception as e:
        return {"is_oa": "", "oa_status": "", "pdf_url": "", "repo_url": "",
                "version": "", "license": "", "host_type": "", "error": str(e)[:80]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",  default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--priority", default="1_DOI_FIRST",
                        help="Filter by extraction_priority (default: 1_DOI_FIRST). Use 'all' for all.")
    parser.add_argument("--delay",  type=float, default=DELAY)
    args = parser.parse_args()

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    with open(args.input, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if args.priority != "all":
        rows = [r for r in rows if r.get("extraction_priority", "") == args.priority]

    rows = [r for r in rows if r.get("doi", "").strip()]

    print(f"Querying Unpaywall for {len(rows)} DOIs (priority={args.priority})...", flush=True)

    results = []
    oa_count = 0
    pdf_count = 0

    for i, row in enumerate(rows, 1):
        doi = row["doi"].strip()
        ua = query_unpaywall(doi)
        out = {
            "seq":                row.get("seq", ""),
            "extraction_priority": row.get("extraction_priority", ""),
            "doi":                doi,
            "title":              row.get("title", ""),
            "year":               row.get("year", ""),
            "journal":            row.get("journal", ""),
        }
        out.update(ua)
        results.append(out)

        if ua["is_oa"] == "True":
            oa_count += 1
        if ua["pdf_url"]:
            pdf_count += 1

        if i % 50 == 0:
            print(f"  {i}/{len(rows)} done | OA so far: {oa_count} | PDF links: {pdf_count}", flush=True)

        time.sleep(args.delay)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS)
        w.writeheader()
        w.writerows(results)

    print(f"\n=== UNPAYWALL RESULTS ===")
    print(f"Total queried:    {len(results)}")
    print(f"OA (any version): {oa_count} ({100*oa_count/max(1,len(results)):.1f}%)")
    print(f"Direct PDF link:  {pdf_count} ({100*pdf_count/max(1,len(results)):.1f}%)")
    errors = sum(1 for r in results if r["error"])
    print(f"Errors:           {errors}")
    print(f"Output:           {args.output}")

    # OA status breakdown
    from collections import Counter
    statuses = Counter(r["oa_status"] for r in results if r["oa_status"])
    print("\nOA status breakdown:")
    for s, c in statuses.most_common():
        print(f"  {s:12s} {c:4d}  ({100*c/len(results):.1f}%)")


if __name__ == "__main__":
    main()
