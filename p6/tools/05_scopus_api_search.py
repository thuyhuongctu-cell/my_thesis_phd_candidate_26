#!/usr/bin/env python3
"""
05_scopus_api_search.py — Automated Scopus search via Elsevier API.

HOW TO GET YOUR API KEY (free for institutional users):
  1. Go to https://dev.elsevier.com/
  2. Click "I want an API key" → register with your university email
  3. Select "Academic Research" → your key appears on dashboard
  4. Set environment variable:  export SCOPUS_API_KEY="your-key-here"
  OR edit SCOPUS_API_KEY below (not recommended for shared environments).

Can Tho University (ctu.edu.vn) qualifies for institutional access.
Key is usually provisioned within 24 hours.

Usage:
  export SCOPUS_API_KEY="abc123..."
  python3 05_scopus_api_search.py
  python3 05_scopus_api_search.py --query "TITLE-ABS-KEY(internationalization AND performance)" --max 500
"""

import argparse
import csv
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Install requests: pip install requests")


# ---------------------------------------------------------------------------
# Configuration — edit SCOPUS_API_KEY or set as environment variable
# ---------------------------------------------------------------------------

SCOPUS_API_KEY = os.environ.get("SCOPUS_API_KEY", "")  # set via env or paste here
BASE_URL = "https://api.elsevier.com/content/search/scopus"
OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Default query for P6 meta-analysis (internationalization → firm performance)
DEFAULT_QUERY = (
    "TITLE-ABS-KEY("
    "(internationalization OR internationalisation OR multinationality OR "
    "\"export intensity\" OR FSTS OR \"foreign sales\") "
    "AND "
    "(\"firm performance\" OR \"financial performance\" OR productivity OR profitability OR ROA OR ROE) "
    "AND "
    "(enterprise OR firm OR company OR SME OR \"small and medium\")"
    ") AND PUBYEAR > 1976 AND DOCTYPE(ar) AND LANGUAGE(English)"
)

COLUMNS = ["source", "source_id", "authors", "year", "title", "journal", "doi", "abstract"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def check_api_key():
    if not SCOPUS_API_KEY:
        print("ERROR: SCOPUS_API_KEY not set.", file=sys.stderr)
        print("  Get a free key at https://dev.elsevier.com/ using your CTU email.", file=sys.stderr)
        print("  Then: export SCOPUS_API_KEY='your-key'", file=sys.stderr)
        sys.exit(1)


def fetch_page(query: str, start: int, count: int = 25) -> dict:
    headers = {
        "X-ELS-APIKey": SCOPUS_API_KEY,
        "Accept": "application/json",
    }
    params = {
        "query": query,
        "start": start,
        "count": count,
        "field": "dc:identifier,dc:title,dc:creator,prism:publicationName,"
                 "prism:coverDate,prism:doi,dc:description,eid",
    }
    resp = requests.get(BASE_URL, headers=headers, params=params, timeout=30)
    if resp.status_code == 401:
        sys.exit("ERROR: Invalid or expired API key. Check SCOPUS_API_KEY.")
    if resp.status_code == 429:
        print("Rate limit hit — waiting 10s...", file=sys.stderr)
        time.sleep(10)
        return fetch_page(query, start, count)
    resp.raise_for_status()
    return resp.json()


def parse_entry(entry: dict) -> dict:
    doi = entry.get("prism:doi", "").strip().lower()
    doi = re.sub(r"^https?://doi\.org/", "", doi)
    date = entry.get("prism:coverDate", "")
    year = date[:4] if date else ""
    creator = entry.get("dc:creator", "")
    return {
        "source": "scopus",
        "source_id": entry.get("eid", entry.get("dc:identifier", "")),
        "authors": creator,
        "year": year,
        "title": entry.get("dc:title", "").strip(),
        "journal": entry.get("prism:publicationName", "").strip(),
        "doi": doi,
        "abstract": entry.get("dc:description", "").strip(),
    }


def write_csv(records: list[dict], path: Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(records)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Search Scopus API for P6 meta-analysis.")
    parser.add_argument("--query", default=DEFAULT_QUERY, help="Scopus query string")
    parser.add_argument("--max", type=int, default=2000, help="Max records to retrieve (default 2000)")
    parser.add_argument("--output", default="", help="Output CSV path")
    args = parser.parse_args()

    check_api_key()

    datestamp = datetime.today().strftime("%Y%m%d")
    output_path = Path(args.output) if args.output else OUTPUT_DIR / f"scopus_api_{datestamp}.csv"

    print(f"Scopus API search — {datestamp}")
    print(f"Query: {args.query[:120]}...")

    # First request to get total count
    data = fetch_page(args.query, start=0, count=1)
    total = int(data.get("search-results", {}).get("opensearch:totalResults", 0))
    print(f"Total results: {total}")

    limit = min(total, args.max)
    print(f"Retrieving: {limit} records")

    records = []
    page_size = 25
    for start in range(0, limit, page_size):
        batch = min(page_size, limit - start)
        data = fetch_page(args.query, start=start, count=batch)
        entries = data.get("search-results", {}).get("entry", [])
        for entry in entries:
            records.append(parse_entry(entry))
        print(f"  Retrieved {min(start + batch, limit)}/{limit}", end="\r")
        time.sleep(0.1)  # polite pacing

    print(f"\nParsed {len(records)} records")
    n_doi = sum(1 for r in records if r["doi"])
    print(f"  With DOI       : {n_doi}")
    print(f"  Missing DOI    : {len(records) - n_doi}")

    write_csv(records, output_path)
    print(f"Output written   : {output_path}")
    print(f"\nNext step: python3 03_deduplicate_merge.py --inputs {output_path} [other_csvs...]")


if __name__ == "__main__":
    main()
