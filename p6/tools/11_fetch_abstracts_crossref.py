#!/usr/bin/env python3
"""
11_fetch_abstracts_crossref.py
Fetch abstracts for worklist records via CrossRef API (free, no key required).
Falls back to Semantic Scholar API for records without CrossRef abstract.

Usage:
    python3 p6/tools/11_fetch_abstracts_crossref.py \
        --input  p6/tools/results/extraction_worklist_v9_20260519.csv \
        --output p6/tools/results/worklist_with_abstracts_YYYYMMDD.csv \
        [--limit 100]   # process only first N records with DOIs
"""

import csv
import json
import time
import urllib.request
import urllib.error
import urllib.parse
import argparse
import sys
from datetime import datetime
from pathlib import Path

CROSSREF_API   = "https://api.crossref.org/works/{doi}"
SEMANTICSCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=abstract,title,year"
CACHE_FILE     = Path("p6/tools/results/abstract_cache_crossref.json")
POLITE_EMAIL   = "huongp1323001@gstudent.ctu.edu.vn"   # CrossRef polite pool


def load_cache():
    if CACHE_FILE.exists():
        with open(CACHE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def fetch_crossref(doi, cache):
    key = "cr:" + doi.lower()
    if key in cache:
        return cache[key]

    url = CROSSREF_API.format(doi=urllib.parse.quote(doi, safe=""))
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "P6MetaAnalysis/1.0 (mailto:%s)" % POLITE_EMAIL}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        msg = data.get("message", {})
        abstract = msg.get("abstract", "")
        # CrossRef wraps abstracts in <jats:p> tags sometimes
        if abstract:
            abstract = abstract.replace("<jats:p>", "").replace("</jats:p>", " ").strip()
        cache[key] = abstract
        return abstract
    except Exception:
        cache[key] = ""
        return ""


def fetch_semanticscholar(doi, cache):
    key = "ss:" + doi.lower()
    if key in cache:
        return cache[key]

    url = SEMANTICSCHOLAR_API.format(doi=urllib.parse.quote(doi, safe=""))
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "P6MetaAnalysis/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        abstract = data.get("abstract") or ""
        cache[key] = abstract
        return abstract
    except Exception:
        cache[key] = ""
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input",  required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--limit",  type=int, default=None,
                    help="Max number of DOI records to fetch (default: all)")
    ap.add_argument("--delay",  type=float, default=0.5,
                    help="Seconds between API calls (default: 0.5)")
    args = ap.parse_args()

    cache = load_cache()

    with open(args.input, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = list(rows[0].keys()) if rows else []
    if "abstract" not in fieldnames:
        fieldnames.append("abstract")

    fetched = skipped = already = errors = 0
    limit_count = 0

    for row in rows:
        doi = row.get("doi", "").strip()
        existing_abstract = row.get("abstract", "").strip()

        if not doi:
            skipped += 1
            continue
        if existing_abstract and len(existing_abstract) > 30:
            already += 1
            continue
        if args.limit and limit_count >= args.limit:
            break

        # Try CrossRef first
        abstract = fetch_crossref(doi, cache)
        time.sleep(args.delay)

        # Fallback to Semantic Scholar
        if not abstract:
            abstract = fetch_semanticscholar(doi, cache)
            time.sleep(args.delay)

        row["abstract"] = abstract
        if abstract:
            fetched += 1
            print("[%d] OK  doi=%s  chars=%d" % (int(row.get("seq", 0)), doi[:50], len(abstract)))
        else:
            errors += 1
            print("[%d] ---  doi=%s  (no abstract)" % (int(row.get("seq", 0)), doi[:50]))

        limit_count += 1

        # Save cache every 20 records
        if (fetched + errors) % 20 == 0:
            save_cache(cache)

    save_cache(cache)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\n=== Summary ===")
    print("Fetched abstracts : %d" % fetched)
    print("Already had       : %d" % already)
    print("No DOI / skipped  : %d" % skipped)
    print("No abstract found : %d" % errors)
    print("Output            : %s" % out_path)


if __name__ == "__main__":
    main()
