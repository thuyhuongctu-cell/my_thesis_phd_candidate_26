#!/usr/bin/env python3
"""
07_enrich_doi_crossref.py — Enrich missing DOIs via CrossRef free API.

CrossRef polite API: https://api.crossref.org/works?query.title=...&query.author=...
No key needed; use mailto= header for polite pool (faster, higher rate limit).

Usage:
  python3 07_enrich_doi_crossref.py \
      --input  p6/tools/results/new_candidates_20260518.csv \
      --output p6/tools/results/new_candidates_doi_enriched.csv \
      --email  huongp1323001@gstudent.ctu.edu.vn
"""

import argparse
import csv
import sys
import time
from pathlib import Path
from urllib.parse import quote

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

CROSSREF_URL = "https://api.crossref.org/works"
RATE_WAIT    = 0.15   # ~6 req/sec, well within polite pool limit
SCORE_MIN    = 60.0   # CrossRef relevance score threshold (0–100+)


def clean(text: str) -> str:
    return (text or "").strip().lower()


def query_crossref(title: str, author: str, email: str) -> dict | None:
    """Return best CrossRef match or None if confidence too low."""
    first_author = author.split(";")[0].split(",")[0].strip()
    params = {
        "query.title":           title[:200],
        "query.author":          first_author[:60],
        "rows":                  3,
        "select":                "DOI,title,author,published,score",
        "mailto":                email,
    }
    try:
        resp = requests.get(CROSSREF_URL, params=params, timeout=15)
        if resp.status_code != 200:
            return None
        items = resp.json().get("message", {}).get("items", [])
        if not items:
            return None
        best = items[0]
        if best.get("score", 0) < SCORE_MIN:
            return None
        return best
    except Exception:
        return None


def title_similar(t1: str, t2: str) -> bool:
    """Rough title match: ≥70% words in common."""
    w1 = set(clean(t1).split())
    w2 = set(clean(t2).split())
    if not w1 or not w2:
        return False
    overlap = len(w1 & w2) / max(len(w1), len(w2))
    return overlap >= 0.70


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",   required=True)
    parser.add_argument("--output",  required=True)
    parser.add_argument("--email",   default="huongp1323001@gstudent.ctu.edu.vn")
    parser.add_argument("--max",     type=int, default=0,
                        help="Max records to enrich (0 = all)")
    args = parser.parse_args()

    in_path  = Path(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with open(in_path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    # Add doi_enriched column if not present
    if "doi_enriched" not in fieldnames:
        fieldnames = list(fieldnames) + ["doi_enriched", "doi_source"]

    limit       = args.max if args.max > 0 else len(rows)
    enriched    = 0
    already_had = 0
    failed      = 0

    for i, row in enumerate(rows[:limit]):
        existing_doi = (row.get("doi") or "").strip()
        if existing_doi:
            row["doi_enriched"] = existing_doi
            row["doi_source"]   = "wos"
            already_had += 1
            continue

        if i % 50 == 0:
            print(f"  Progress: {i}/{limit} | enriched: {enriched} | failed: {failed}",
                  end="\r")

        match = query_crossref(row.get("title", ""), row.get("authors", ""), args.email)
        time.sleep(RATE_WAIT)

        if match:
            cr_title = " ".join(match.get("title", [""]))
            if title_similar(row.get("title", ""), cr_title):
                row["doi_enriched"] = match["DOI"].lower()
                row["doi_source"]   = f"crossref_score={match['score']:.0f}"
                enriched += 1
            else:
                row["doi_enriched"] = ""
                row["doi_source"]   = "crossref_title_mismatch"
                failed += 1
        else:
            row["doi_enriched"] = ""
            row["doi_source"]   = "crossref_no_match"
            failed += 1

    print(f"\nDOI enrichment complete:")
    print(f"  Already had DOI : {already_had:,}")
    print(f"  Newly enriched  : {enriched:,}")
    print(f"  Not found       : {failed:,}")
    print(f"  Total processed : {min(limit, len(rows)):,} / {len(rows):,}")

    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Output: {out_path}")


if __name__ == "__main__":
    main()
