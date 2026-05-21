#!/usr/bin/env python3
"""
OpenAlex systematic search for P6 meta-analysis (I→P relationship).
PRISMA 2020 compliant: logs timestamps, query, result counts.

Usage:
    python3 openalex_prisma_search.py

Output:
    p6/tools/results/openalex_raw_YYYYMMDD.csv   — all retrieved records
    p6/tools/results/search_log.jsonl             — PRISMA-reproducibility log
"""

import requests
import csv
import json
import time
import datetime
import os
import sys
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────
EMAIL = "Thuyhuongctu@gmail.com"          # polite pool → higher rate limit
BASE_URL = "https://api.openalex.org/works"
OUTPUT_DIR = Path(__file__).parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TODAY = datetime.date.today().strftime("%Y%m%d")
CSV_FILE  = OUTPUT_DIR / f"openalex_raw_{TODAY}.csv"
LOG_FILE  = OUTPUT_DIR / "search_log.jsonl"

START_YEAR = 1977
END_YEAR   = 2026

# ── Search queries ────────────────────────────────────────────────────────────
# OpenAlex `search` searches title + abstract (no WoS-style TS= Boolean).
# Strategy: 4 overlapping queries → union → deduplicate by OpenAlex ID.
# This maximises recall while keeping individual queries precise enough.

QUERIES = [
    {
        "id": "Q1_main",
        "description": "Core: internationalization AND firm performance",
        "search": "internationalization firm performance",
    },
    {
        "id": "Q2_internationalisation",
        "description": "British spelling: internationalisation AND performance",
        "search": "internationalisation firm performance",
    },
    {
        "id": "Q3_export_intensity",
        "description": "Export intensity / FSTS / foreign sales AND performance",
        "search": "export intensity foreign sales performance productivity",
    },
    {
        "id": "Q4_multinationality",
        "description": "Multinationality / degree of internationalization AND performance",
        "search": "multinationality degree internationalization financial performance",
    },
    {
        "id": "Q5_geographic_diversification",
        "description": "Geographic / international diversification AND performance",
        "search": "geographic diversification international expansion firm performance",
    },
]

COMMON_FILTER = (
    f"type:article,"
    f"publication_year:{START_YEAR}-{END_YEAR},"
    f"language:en"
)

FIELDS = ",".join([
    "id", "doi", "title", "display_name",
    "authorships", "publication_year", "primary_location",
    "cited_by_count", "open_access",
])

# ── API helpers ───────────────────────────────────────────────────────────────

def get_page(search_term: str, cursor: str = "*", per_page: int = 200) -> dict:
    params = {
        "search":   search_term,
        "filter":   COMMON_FILTER,
        "per-page": per_page,
        "cursor":   cursor,
        "select":   FIELDS,
        "mailto":   EMAIL,
    }
    r = requests.get(BASE_URL, params=params, timeout=60)
    r.raise_for_status()
    return r.json()


def fetch_all(query_def: dict) -> list[dict]:
    """Paginate through all results for one query; return list of records."""
    records = []
    cursor = "*"
    page_n = 0
    total = None

    print(f"\n  [{query_def['id']}] {query_def['description']}")
    print(f"         search: '{query_def['search']}'")

    while True:
        page_n += 1
        try:
            data = get_page(query_def["search"], cursor)
        except requests.RequestException as e:
            print(f"  ⚠ Request error page {page_n}: {e}. Retrying in 5s…")
            time.sleep(5)
            data = get_page(query_def["search"], cursor)

        if total is None:
            total = data.get("meta", {}).get("count", 0)
            print(f"         total hits: {total:,}")

        results = data.get("results", [])
        if not results:
            break

        records.extend(results)
        print(f"         page {page_n}: {len(results)} records → cumulative {len(records):,}/{total:,}")

        next_cursor = data.get("meta", {}).get("next_cursor")
        if not next_cursor:
            break
        cursor = next_cursor
        time.sleep(0.5)   # polite delay

    return records, total


def flatten_record(rec: dict, source_query: str) -> dict:
    """Extract flat CSV row from OpenAlex record."""
    # Authors
    authors = rec.get("authorships", [])
    author_names = "; ".join(
        a.get("author", {}).get("display_name", "") for a in authors[:5]
    )
    first_author = authors[0].get("author", {}).get("display_name", "") if authors else ""

    # Journal
    loc = rec.get("primary_location") or {}
    source = loc.get("source") or {}
    journal = source.get("display_name", "")

    # DOI
    doi = rec.get("doi", "") or ""
    if doi.startswith("https://doi.org/"):
        doi = doi[len("https://doi.org/"):]

    return {
        "openalex_id":      rec.get("id", ""),
        "doi":              doi,
        "title":            rec.get("display_name", ""),
        "first_author":     first_author,
        "all_authors":      author_names,
        "year":             rec.get("publication_year", ""),
        "journal":          journal,
        "cited_by_count":   rec.get("cited_by_count", 0),
        "is_oa":            rec.get("open_access", {}).get("is_oa", False),
        "oa_url":           rec.get("open_access", {}).get("oa_url", ""),
        "source_query":     source_query,
    }


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 72)
    print("P6 OpenAlex PRISMA Search — I→P Meta-Analysis")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Year range: {START_YEAR}–{END_YEAR} | Type: article | Language: en")
    print("=" * 72)

    all_records_by_id: dict[str, dict] = {}   # openalex_id → flattened row
    log_entries = []

    for qdef in QUERIES:
        t0 = time.time()
        raw_records, total_hits = fetch_all(qdef)
        elapsed = time.time() - t0

        new_count = 0
        for rec in raw_records:
            oid = rec.get("id", "")
            if oid and oid not in all_records_by_id:
                all_records_by_id[oid] = flatten_record(rec, qdef["id"])
                new_count += 1

        log_entries.append({
            "timestamp":     datetime.datetime.utcnow().isoformat() + "Z",
            "query_id":      qdef["id"],
            "description":   qdef["description"],
            "search_string": qdef["search"],
            "filter":        COMMON_FILTER,
            "total_hits":    total_hits,
            "retrieved":     len(raw_records),
            "new_unique":    new_count,
            "elapsed_s":     round(elapsed, 1),
        })

        print(f"  → {new_count:,} new unique records added (total pool: {len(all_records_by_id):,})")

    # ── Write CSV ─────────────────────────────────────────────────────────────
    print(f"\nWriting {len(all_records_by_id):,} unique records to {CSV_FILE}…")
    if all_records_by_id:
        fieldnames = list(next(iter(all_records_by_id.values())).keys())
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in sorted(all_records_by_id.values(), key=lambda r: int(r["year"]) if str(r["year"]).isdigit() else 0, reverse=True):
                writer.writerow(row)
        print(f"  ✅ CSV saved: {CSV_FILE}")

    # ── Write PRISMA log ──────────────────────────────────────────────────────
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        # Summary entry
        summary = {
            "timestamp":          datetime.datetime.utcnow().isoformat() + "Z",
            "event":              "search_session",
            "database":           "OpenAlex",
            "queries_run":        len(QUERIES),
            "total_unique_records": len(all_records_by_id),
            "year_range":         f"{START_YEAR}-{END_YEAR}",
            "filter":             COMMON_FILTER,
            "output_csv":         str(CSV_FILE),
            "individual_queries": log_entries,
        }
        f.write(json.dumps(summary, ensure_ascii=False) + "\n")
    print(f"  ✅ PRISMA log appended: {LOG_FILE}")

    # ── PRISMA summary ────────────────────────────────────────────────────────
    print("\n" + "=" * 72)
    print("PRISMA IDENTIFICATION — OpenAlex counts to enter in flow diagram:")
    print("=" * 72)
    for entry in log_entries:
        print(f"  {entry['query_id']:35s}  n = {entry['total_hits']:>7,}  ({entry['retrieved']:,} retrieved)")
    print(f"\n  {'TOTAL UNIQUE (after deduplication)':35s}  n = {len(all_records_by_id):>7,}")
    print("\n📋 Copy these numbers into:")
    print("   p6/p6_prisma_flow.md  — OpenAlex section (supplementary search)")
    print("   p6/p6_meta_manuscript_en.md  — §3.1 Information sources")
    print("=" * 72)


if __name__ == "__main__":
    main()
