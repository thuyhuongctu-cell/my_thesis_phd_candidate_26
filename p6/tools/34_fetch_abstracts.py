#!/usr/bin/env python3
"""
34_fetch_abstracts.py — Fetch abstracts for UNSURE records from title-screening.

Strategy:
  1. DOI present → CrossRef Works API (doi.org/api)
  2. No DOI → OpenAlex title search
  
Input:  p6/tools/results/new_candidates_screened_YYYYMMDD.csv  (UNSURE rows)
Output: p6/tools/results/abstracts_YYYYMMDD.csv
"""

import csv
import json
import time
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import quote, urlencode
try:
    import requests
except ImportError:
    print("pip install requests", file=sys.stderr)
    sys.exit(1)

EMAIL = "huongp1323001@gstudent.ctu.edu.vn"
TODAY = datetime.now().strftime("%Y%m%d")

CROSSREF_WORKS = "https://api.crossref.org/works/{doi}"
OPENALEX_WORKS = "https://api.openalex.org/works"

HEADERS = {"User-Agent": f"P6MetaAnalysis/1.0 (mailto:{EMAIL})"}


def clean_abstract(text: str) -> str:
    if not text:
        return ""
    # Strip JATS XML tags
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:2000]  # cap at 2000 chars


def fetch_crossref_abstract(doi: str) -> str:
    url = CROSSREF_WORKS.format(doi=quote(doi.strip(), safe="/:"))
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json().get("message", {})
            abstract = data.get("abstract", "")
            return clean_abstract(abstract)
    except Exception:
        pass
    return ""


def fetch_openalex_abstract(title: str, year: str = "") -> str:
    params = {
        "filter": f"title.search:{title[:120]}",
        "select": "abstract_inverted_index,title",
        "per_page": 1,
        "mailto": EMAIL,
    }
    if year and year.isdigit():
        params["filter"] = params["filter"] + f",publication_year:{year}"
    try:
        r = requests.get(OPENALEX_WORKS, params=params, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            results = r.json().get("results", [])
            if results:
                inv = results[0].get("abstract_inverted_index")
                if inv:
                    # reconstruct from inverted index
                    tokens = {}
                    for word, positions in inv.items():
                        for pos in positions:
                            tokens[pos] = word
                    return clean_abstract(" ".join(v for _, v in sorted(tokens.items())))
    except Exception:
        pass
    return ""


def run(input_path: Path, output_path: Path, max_records: int = 0, delay: float = 0.2):
    # Load UNSURE rows
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)
        src_fieldnames = reader.fieldnames

    unsure = [r for r in all_rows if r.get("decision") == "UNSURE"]
    if max_records > 0:
        unsure = unsure[:max_records]

    print(f"UNSURE rows to process: {len(unsure)}", flush=True)

    out_fieldnames = list(src_fieldnames) + ["abstract", "abstract_source"]
    results = []
    doi_hits = title_hits = misses = 0

    for i, row in enumerate(unsure, 1):
        doi = row.get("doi", "").strip()
        abstract = ""
        source = ""

        if doi:
            abstract = fetch_crossref_abstract(doi)
            if abstract:
                source = "crossref"
                doi_hits += 1

        if not abstract:
            abstract = fetch_openalex_abstract(row.get("title", ""), row.get("year", ""))
            if abstract:
                source = "openalex"
                title_hits += 1
            else:
                misses += 1

        row["abstract"] = abstract
        row["abstract_source"] = source
        results.append(row)

        if i % 50 == 0 or i == len(unsure):
            print(f"  [{i}/{len(unsure)}] crossref={doi_hits} openalex={title_hits} miss={misses}", flush=True)

        time.sleep(delay)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=out_fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nDone. Output: {output_path}")
    print(f"  Total: {len(results)}  CrossRef: {doi_hits}  OpenAlex: {title_hits}  Miss: {misses}")
    coverage = round((doi_hits + title_hits) / max(len(results), 1) * 100, 1)
    print(f"  Abstract coverage: {coverage}%")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=f"p6/tools/results/new_candidates_screened_{TODAY}.csv")
    parser.add_argument("--output", default=f"p6/tools/results/abstracts_{TODAY}.csv")
    parser.add_argument("--max-records", type=int, default=0)
    parser.add_argument("--delay", type=float, default=0.25,
                        help="Seconds between API calls (default 0.25)")
    args = parser.parse_args()

    run(Path(args.input), Path(args.output), args.max_records, args.delay)
