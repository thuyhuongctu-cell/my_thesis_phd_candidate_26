#!/usr/bin/env python3
"""
06_wos_api_search.py — Automated WoS search via Clarivate Starter API (free tier).

HOW TO GET YOUR API KEY (free):
  1. Go to https://developer.clarivate.com/
  2. Sign up → create an App → select "Web of Science Starter API"
  3. Free tier: 500 queries/week, 1 request/second, 10 records/page
  4. Set environment variable:  export WOS_API_KEY="your-key-here"

Free tier is sufficient for a P6 meta-analysis search (~200–500 results expected).

Usage:
  export WOS_API_KEY="abc123..."
  python3 06_wos_api_search.py
  python3 06_wos_api_search.py --query "TS=(internationalization AND performance)" --max 500
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
# Configuration
# ---------------------------------------------------------------------------

WOS_API_KEY = os.environ.get("WOS_API_KEY", "")  # set via env or paste here
BASE_URL = "https://api.clarivate.com/api/wos"
OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# P6 meta-analysis search query (WoS TS= syntax)
DEFAULT_QUERY = (
    "TS=("
    "(internationalization OR internationalisation OR multinationality OR "
    "\"export intensity\" OR \"foreign sales\" OR FSTS) "
    "AND "
    "(\"firm performance\" OR \"financial performance\" OR productivity OR profitability) "
    "AND "
    "(firm OR enterprise OR company OR SME)"
    ") AND PY=(1977-2026) AND DT=Article AND LA=English"
)

COLUMNS = ["source", "source_id", "authors", "year", "title", "journal", "doi", "abstract"]

PAGE_SIZE = 10  # Starter API limit is 10 records per request


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def check_api_key():
    if not WOS_API_KEY:
        print("ERROR: WOS_API_KEY not set.", file=sys.stderr)
        print("  Get a free key at https://developer.clarivate.com/", file=sys.stderr)
        print("  Then: export WOS_API_KEY='your-key'", file=sys.stderr)
        sys.exit(1)


def get_headers() -> dict:
    return {
        "X-ApiKey": WOS_API_KEY,
        "Accept": "application/json",
        "Content-Type": "application/json",
    }


def search_query(query: str) -> tuple[str, int]:
    """Submit a new search and return (query_id, record_count)."""
    resp = requests.get(
        f"{BASE_URL}",
        headers=get_headers(),
        params={"databaseId": "WOS", "usrQuery": query, "count": 1, "firstRecord": 1},
        timeout=30,
    )
    if resp.status_code == 401:
        sys.exit("ERROR: Invalid WOS_API_KEY.")
    if resp.status_code == 429:
        print("Rate limit — waiting 60s...", file=sys.stderr)
        time.sleep(60)
        return search_query(query)
    resp.raise_for_status()
    data = resp.json()
    query_id = data.get("QueryResult", {}).get("QueryID", "")
    total = int(data.get("QueryResult", {}).get("RecordsFound", 0))
    return query_id, total


def fetch_records(query_id: str, first: int, count: int) -> list[dict]:
    resp = requests.get(
        f"{BASE_URL}/query/{query_id}",
        headers=get_headers(),
        params={"firstRecord": first, "count": count},
        timeout=30,
    )
    if resp.status_code == 429:
        print("Rate limit — waiting 60s...", file=sys.stderr)
        time.sleep(60)
        return fetch_records(query_id, first, count)
    resp.raise_for_status()
    data = resp.json()
    return data.get("Records", {}).get("records", {}).get("REC", [])


def parse_record(rec: dict) -> dict:
    static = rec.get("static_data", {})
    summary = static.get("summary", {})

    # Title
    titles = summary.get("titles", {}).get("title", [])
    title = ""
    for t in titles:
        if t.get("type") == "item":
            title = t.get("content", "")
            break

    # Authors
    names_block = summary.get("names", {}).get("name", [])
    if isinstance(names_block, dict):
        names_block = [names_block]
    authors = "; ".join(
        n.get("display_name", n.get("full_name", ""))
        for n in names_block
        if n.get("role") == "author"
    )

    # Year
    pub_info = summary.get("pub_info", {})
    year = str(pub_info.get("pubyear", ""))

    # Journal
    source_title = ""
    for t in titles:
        if t.get("type") == "source":
            source_title = t.get("content", "")
            break

    # DOI
    identifiers = rec.get("dynamic_data", {}).get("cluster_related", {}).get("identifiers", {})
    id_list = identifiers.get("identifier", [])
    if isinstance(id_list, dict):
        id_list = [id_list]
    doi = ""
    for ident in id_list:
        if ident.get("type", "").lower() == "doi":
            doi = ident.get("value", "").lower().strip()
            doi = re.sub(r"^https?://doi\.org/", "", doi)
            break

    # WoS accession number
    uid = rec.get("UID", "")
    source_id = uid.replace("WOS:", "") if uid.startswith("WOS:") else uid

    # Abstract
    abstract_block = static.get("fullrecord_metadata", {}).get("abstracts", {}).get("abstract", {})
    if isinstance(abstract_block, list):
        abstract_block = abstract_block[0] if abstract_block else {}
    abstract_text = abstract_block.get("abstract_text", {})
    if isinstance(abstract_text, dict):
        para = abstract_text.get("p", "")
        abstract = para if isinstance(para, str) else " ".join(para)
    else:
        abstract = ""

    return {
        "source": "wos",
        "source_id": source_id,
        "authors": authors,
        "year": year,
        "title": title,
        "journal": source_title,
        "doi": doi,
        "abstract": abstract,
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
    parser = argparse.ArgumentParser(description="Search WoS Starter API for P6 meta-analysis.")
    parser.add_argument("--query", default=DEFAULT_QUERY, help="WoS query string (TS= syntax)")
    parser.add_argument("--max", type=int, default=500, help="Max records (default 500; free tier: 500/week)")
    parser.add_argument("--output", default="", help="Output CSV path")
    args = parser.parse_args()

    check_api_key()

    datestamp = datetime.today().strftime("%Y%m%d")
    output_path = Path(args.output) if args.output else OUTPUT_DIR / f"wos_api_{datestamp}.csv"

    print(f"WoS Starter API search — {datestamp}")
    print(f"Query: {args.query[:120]}...")

    query_id, total = search_query(args.query)
    print(f"Total results: {total}")

    limit = min(total, args.max)
    print(f"Retrieving: {limit} records (free tier: 500/week)")

    records = []
    for first in range(1, limit + 1, PAGE_SIZE):
        batch = min(PAGE_SIZE, limit - first + 1)
        recs = fetch_records(query_id, first, batch)
        for r in recs:
            records.append(parse_record(r))
        print(f"  Retrieved {min(first + batch - 1, limit)}/{limit}", end="\r")
        time.sleep(1.0)  # Starter API: 1 req/second

    print(f"\nParsed {len(records)} records")
    n_doi = sum(1 for r in records if r["doi"])
    print(f"  With DOI       : {n_doi}")
    print(f"  Missing DOI    : {len(records) - n_doi}")

    write_csv(records, output_path)
    print(f"Output written   : {output_path}")
    print(f"\nNext step: python3 03_deduplicate_merge.py --inputs {output_path} [other_csvs...]")


if __name__ == "__main__":
    main()
