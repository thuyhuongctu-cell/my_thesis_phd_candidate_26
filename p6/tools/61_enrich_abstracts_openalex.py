#!/usr/bin/env python3
"""
61_enrich_abstracts_openalex.py
Fetch abstracts from OpenAlex for all tracker_v2 papers (DOI + title fallback).
Output: p6/tools/results/abstracts_enriched.csv

Usage:
    python3 p6/tools/61_enrich_abstracts_openalex.py [--limit N] [--dry-run]

Rate limit: 10 req/s polite (no API key needed below 100k/day).
"""
import csv, time, urllib.request, urllib.parse, json, argparse, sys
from pathlib import Path
from datetime import datetime

TRACKER = Path("p6/tools/results/fulltext_to_extraction_tracker_v2.csv")
OUTPUT  = Path("p6/tools/results/abstracts_enriched.csv")
EMAIL   = "huongdt@vlute.edu.vn"
SLEEP   = 0.12   # ~8 req/s — polite
TIMEOUT = 20

def oa_by_doi(doi: str) -> dict | None:
    url = f"https://api.openalex.org/works/doi:{urllib.parse.quote(doi, safe='/')}?select=id,doi,title,abstract_inverted_index&mailto={EMAIL}"
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
            return json.load(r)
    except Exception:
        return None

def oa_by_title(title: str, year: str) -> dict | None:
    q = urllib.parse.quote(f'"{title[:80]}"')
    url = f"https://api.openalex.org/works?filter=publication_year:{year},title.search:{q}&select=id,doi,title,abstract_inverted_index&per-page=1&mailto={EMAIL}"
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
            data = json.load(r)
            results = data.get("results", [])
            return results[0] if results else None
    except Exception:
        return None

def invert_abstract(inv: dict | None) -> str:
    """Convert OpenAlex inverted index to plain text abstract."""
    if not inv:
        return ""
    word_pos = []
    for word, positions in inv.items():
        for pos in positions:
            word_pos.append((pos, word))
    word_pos.sort()
    return " ".join(w for _, w in word_pos)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Max papers to process (0=all)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rows = list(csv.DictReader(TRACKER.open()))
    total = len(rows)
    if args.limit:
        rows = rows[:args.limit]

    # Load already-enriched seqs to skip
    existing = {}
    if OUTPUT.exists():
        for r in csv.DictReader(OUTPUT.open()):
            existing[r["seq"]] = r

    out_fields = ["seq", "doi", "title", "year", "abstract", "oa_source", "oa_id"]
    need_header = not OUTPUT.exists()
    fout = OUTPUT.open("a", newline="", encoding="utf-8")
    writer = csv.DictWriter(fout, fieldnames=out_fields)
    if need_header:
        writer.writeheader()

    stats = {"doi_hit": 0, "title_hit": 0, "miss": 0, "skip": 0}

    for i, row in enumerate(rows):
        seq = row["seq"]
        if seq in existing:
            stats["skip"] += 1
            continue

        doi = row.get("doi", "").strip()
        title = row.get("title", "").strip()
        year  = row.get("year", "").strip()

        if args.dry_run:
            print(f"[{i+1}/{len(rows)}] {seq} | {title[:60]}")
            continue

        data = None
        source = ""

        if doi:
            data = oa_by_doi(doi)
            if data:
                source = "doi"
                stats["doi_hit"] += 1
            time.sleep(SLEEP)

        if not data and title:
            data = oa_by_title(title, year)
            if data:
                source = "title"
                stats["title_hit"] += 1
            time.sleep(SLEEP)

        if not data:
            stats["miss"] += 1

        abstract = ""
        oa_id = ""
        if data:
            abstract = invert_abstract(data.get("abstract_inverted_index"))
            oa_id = data.get("id", "")

        writer.writerow({
            "seq": seq, "doi": doi, "title": title, "year": year,
            "abstract": abstract, "oa_source": source, "oa_id": oa_id
        })

        if (i + 1) % 50 == 0:
            print(f"[{i+1}/{len(rows)}] doi_hit={stats['doi_hit']} title_hit={stats['title_hit']} miss={stats['miss']}", flush=True)

    fout.close()
    print(f"\nDone: {total} total in tracker")
    print(f"Processed: {len(rows) - stats['skip']} | skip={stats['skip']}")
    print(f"doi_hit={stats['doi_hit']} | title_hit={stats['title_hit']} | miss={stats['miss']}")
    print(f"Output: {OUTPUT}")

if __name__ == "__main__":
    main()
