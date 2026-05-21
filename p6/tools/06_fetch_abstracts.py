"""
06_fetch_abstracts.py
Fetch abstracts for UNSURE (and optionally Y) records via:
  1. Crossref API  (doi.org lookup — free, no auth)
  2. OpenAlex API  (DOI lookup → title fallback)

Input : p6/tools/results/l2_screened_20260518.csv
Output: p6/tools/results/abstracts_YYYYMMDD.csv
        p6/tools/results/l2_with_abstracts_YYYYMMDD.csv  (full file + abstract column)

Usage:
  python3 06_fetch_abstracts.py             # UNSURE only (default)
  python3 06_fetch_abstracts.py --all       # all 782 records
  python3 06_fetch_abstracts.py --limit 50  # first N records for testing
"""

import csv
import json
import time
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import date
from pathlib import Path

# ── Config ───────────────────────────────────────────────────────────────────
BASE_DIR   = Path("/home/user/PAPERS_IN_PHD_2026")
INPUT      = BASE_DIR / "p6/tools/results/l2_screened_20260518.csv"
OUTDIR     = BASE_DIR / "p6/tools/results"
TODAY      = date.today().strftime('%Y%m%d')
OUT_FULL   = OUTDIR / f"l2_with_abstracts_{TODAY}.csv"
OUT_CACHE  = OUTDIR / f"abstract_cache_{TODAY}.json"

DELAY      = 0.3   # seconds between API calls (polite rate)
MAX_TITLE_LEN = 120

# ── Helpers ──────────────────────────────────────────────────────────────────
def http_get(url: str, timeout: int = 10) -> dict | None:
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'P6-MetaAnalysis/1.0 (mailto:research@ctu.edu.vn)',
            'Accept': 'application/json'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception:
        return None


def crossref_abstract(doi: str) -> str:
    doi = doi.strip().lstrip('https://doi.org/').lstrip('http://dx.doi.org/')
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='/')}"
    data = http_get(url)
    if not data:
        return ''
    msg = data.get('message', {})
    abstract = msg.get('abstract', '') or ''
    # Strip JATS XML tags if present
    import re
    abstract = re.sub(r'<[^>]+>', ' ', abstract).strip()
    abstract = re.sub(r'\s+', ' ', abstract)
    return abstract


def openalex_abstract_by_doi(doi: str) -> str:
    doi_enc = urllib.parse.quote(doi.strip(), safe='/')
    url = f"https://api.openalex.org/works/doi:{doi_enc}"
    data = http_get(url)
    if not data:
        return ''
    return _openalex_reconstruct_abstract(data)


def openalex_abstract_by_title(title: str, year: str = '') -> str:
    q = urllib.parse.quote(title[:MAX_TITLE_LEN])
    url = f"https://api.openalex.org/works?search={q}&per_page=3"
    if year:
        url += f"&filter=publication_year:{year}"
    data = http_get(url)
    if not data:
        return ''
    results = data.get('results', [])
    if not results:
        return ''
    return _openalex_reconstruct_abstract(results[0])


def _openalex_reconstruct_abstract(work: dict) -> str:
    """Reconstruct abstract from OpenAlex inverted index."""
    inv = work.get('abstract_inverted_index') or {}
    if not inv:
        return ''
    # inv = {"word": [pos, pos, ...], ...}
    max_pos = max(p for positions in inv.values() for p in positions) + 1
    tokens = [''] * max_pos
    for word, positions in inv.items():
        for pos in positions:
            if pos < max_pos:
                tokens[pos] = word
    return ' '.join(t for t in tokens if t)


# ── Load cache ────────────────────────────────────────────────────────────────
cache: dict = {}
if OUT_CACHE.exists():
    with open(OUT_CACHE) as f:
        cache = json.load(f)
    print(f"Loaded {len(cache)} cached abstracts from {OUT_CACHE.name}")


def get_abstract(row: dict) -> tuple[str, str]:
    """Returns (abstract, source). Uses cache."""
    seq = row['seq']
    if seq in cache:
        return cache[seq]['abstract'], cache[seq]['source']

    doi = row.get('doi_enriched', '').strip()
    title = row.get('title', '').strip()
    year  = row.get('year', '').strip()

    abstract, source = '', ''

    # Try Crossref first (richer abstracts)
    if doi:
        abstract = crossref_abstract(doi)
        if abstract:
            source = 'crossref'
        time.sleep(DELAY)

    # Try OpenAlex by DOI
    if not abstract and doi:
        abstract = openalex_abstract_by_doi(doi)
        if abstract:
            source = 'openalex_doi'
        time.sleep(DELAY)

    # Try OpenAlex by title
    if not abstract and title:
        abstract = openalex_abstract_by_title(title, year)
        if abstract:
            source = 'openalex_title'
        time.sleep(DELAY)

    cache[seq] = {'abstract': abstract, 'source': source}
    return abstract, source


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    fetch_all = '--all' in sys.argv
    limit = None
    for i, arg in enumerate(sys.argv):
        if arg == '--limit' and i + 1 < len(sys.argv):
            limit = int(sys.argv[i + 1])

    with open(INPUT, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ['abstract', 'abstract_source']
        rows = list(reader)

    if fetch_all:
        targets = rows
        print(f"Fetching abstracts for ALL {len(targets)} records")
    else:
        targets = [r for r in rows if r['include_flag'] == 'UNSURE']
        print(f"Fetching abstracts for {len(targets)} UNSURE records")

    if limit:
        targets = targets[:limit]
        print(f"Limited to first {limit} records")

    # Build index for fast lookup
    row_by_seq = {r['seq']: r for r in rows}

    found = 0
    for i, row in enumerate(targets, 1):
        abstract, source = get_abstract(row)
        row_by_seq[row['seq']]['abstract'] = abstract
        row_by_seq[row['seq']]['abstract_source'] = source
        if abstract:
            found += 1
        if i % 50 == 0 or i == len(targets):
            print(f"  [{i}/{len(targets)}] abstracts found: {found}", flush=True)
            # Save cache periodically
            with open(OUT_CACHE, 'w') as f:
                json.dump(cache, f, ensure_ascii=False, indent=2)

    # Fill empty abstract/source for non-targeted rows
    for row in rows:
        if 'abstract' not in row:
            row['abstract'] = ''
            row['abstract_source'] = ''

    # Write output
    with open(OUT_FULL, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Save final cache
    with open(OUT_CACHE, 'w') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

    targeted = len(targets)
    print(f"\nDone. Abstracts fetched: {found}/{targeted} ({100*found//targeted if targeted else 0}%)")
    print(f"Output: {OUT_FULL}")
    print(f"Cache:  {OUT_CACHE}")


if __name__ == '__main__':
    main()
