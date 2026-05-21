#!/usr/bin/env python3
"""
06_wos_api_search.py — WoS Starter API v1 search for P6 meta-analysis.

Endpoint: https://api.clarivate.com/apis/wos-starter/v1/documents
Auth:     X-ApiKey header (Consumer Key from developer.clarivate.com)
Plans:    Free Trial = 50 req/day × 50 records/page = 2,500 records/day
          Institutional Member = 5,000 req/day

Usage:
  export WOS_API_KEY="your-consumer-key"
  python3 06_wos_api_search.py
  python3 06_wos_api_search.py --max 2000 --output results/wos_api.csv
"""

import argparse
import csv
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


BASE_URL    = "https://api.clarivate.com/apis/wos-starter/v1"
OUTPUT_DIR  = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WOS_API_KEY = os.environ.get("WOS_API_KEY", "")

# P6 query — WoS TS= syntax
DEFAULT_QUERY = (
    "TS=("
    "(internationalization OR internationalisation OR multinationality "
    "OR \"export intensity\" OR \"foreign sales\" OR FSTS) "
    "AND "
    "(\"firm performance\" OR \"financial performance\" OR productivity OR profitability) "
    "AND "
    "(firm OR enterprise OR company OR SME)"
    ") AND PY=(1977-2026) AND DT=Article AND LA=English"
)

COLUMNS   = ["source", "source_id", "authors", "year", "title", "journal", "doi", "abstract"]
PAGE_SIZE = 50   # Starter API max per page
RATE_WAIT = 1.1  # seconds between requests (1 req/sec limit)


# ---------------------------------------------------------------------------

def check_key():
    if not WOS_API_KEY:
        print("ERROR: WOS_API_KEY not set.", file=sys.stderr)
        print("  Get key at https://developer.clarivate.com/apis/wos-starter", file=sys.stderr)
        print("  Then: export WOS_API_KEY='your-consumer-key'", file=sys.stderr)
        sys.exit(1)


def headers() -> dict:
    return {"X-ApiKey": WOS_API_KEY, "Accept": "application/json"}


def search_page(query: str, page: int, limit: int) -> dict:
    """Fetch one page; handle rate limits with backoff."""
    for attempt in range(4):
        resp = requests.get(
            f"{BASE_URL}/documents",
            headers=headers(),
            params={"q": query, "db": "WOS", "limit": limit, "page": page},
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 401:
            sys.exit("ERROR: Invalid WOS_API_KEY (401 Unauthorized).")
        if resp.status_code == 403:
            sys.exit("ERROR: API key not approved or subscription inactive (403 Forbidden).")
        if resp.status_code == 429:
            wait = 60 * (attempt + 1)
            print(f"\nRate limit (429) — waiting {wait}s...", file=sys.stderr)
            time.sleep(wait)
            continue
        resp.raise_for_status()
    sys.exit("ERROR: Exceeded retry limit.")


def parse_hit(hit: dict) -> dict:
    # Authors
    author_list = hit.get("names", {}).get("authors", [])
    if isinstance(author_list, dict):
        author_list = [author_list]
    authors = "; ".join(
        a.get("displayName", a.get("wosStandard", ""))
        for a in author_list
    ).strip()

    # Source metadata
    source = hit.get("source", {})
    journal = source.get("sourceTitle", "").strip()
    year    = str(source.get("publishYear", "")).strip()

    # DOI — normalise
    doi = source.get("doi", "").strip().lower()
    doi = re.sub(r"^https?://doi\.org/", "", doi)

    # WoS UID → source_id
    uid = hit.get("uid", "")
    source_id = uid[4:] if uid.upper().startswith("WOS:") else uid

    # Abstract
    abstract = hit.get("abstract", "").strip()

    return {
        "source":    "wos",
        "source_id": source_id,
        "authors":   authors,
        "year":      year,
        "title":     hit.get("title", "").strip(),
        "journal":   journal,
        "doi":       doi,
        "abstract":  abstract,
    }


def write_csv(records: list[dict], path: Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(records)


# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="WoS Starter API search for P6 meta-analysis.")
    parser.add_argument("--query",  default=DEFAULT_QUERY)
    parser.add_argument("--max",    type=int, default=2500,
                        help="Max records (Free Trial: 2500/day, Institutional: 250000/day)")
    parser.add_argument("--output", default="")
    args = parser.parse_args()

    check_key()

    datestamp   = datetime.today().strftime("%Y%m%d")
    output_path = Path(args.output) if args.output else OUTPUT_DIR / f"wos_api_{datestamp}.csv"

    print(f"WoS Starter API — {datestamp}")
    print(f"Query: {args.query[:100]}...")

    # First page → get total count
    first_page = search_page(args.query, page=1, limit=PAGE_SIZE)
    meta  = first_page.get("metadata", {})
    total = int(meta.get("total", 0))
    print(f"Total results in WoS: {total:,}")

    limit = min(total, args.max)
    print(f"Retrieving: {limit:,} records")

    all_records = []

    # Parse first page
    for hit in first_page.get("hits", []):
        all_records.append(parse_hit(hit))
    print(f"  Page 1 → {len(all_records):,}/{limit:,}", end="\r")

    # Remaining pages
    page = 2
    while len(all_records) < limit:
        time.sleep(RATE_WAIT)
        data  = search_page(args.query, page=page, limit=PAGE_SIZE)
        hits  = data.get("hits", [])
        if not hits:
            break
        for hit in hits:
            if len(all_records) >= limit:
                break
            all_records.append(parse_hit(hit))
        print(f"  Page {page} → {len(all_records):,}/{limit:,}", end="\r")
        page += 1

    print(f"\nParsed {len(all_records):,} records total")
    n_doi = sum(1 for r in all_records if r["doi"])
    print(f"  With DOI    : {n_doi:,}")
    print(f"  Missing DOI : {len(all_records) - n_doi:,}")

    write_csv(all_records, output_path)
    print(f"Output: {output_path}")
    print(f"\nNext: python3 03_deduplicate_merge.py --inputs {output_path} --output results/merged_{datestamp}.csv")


if __name__ == "__main__":
    main()
