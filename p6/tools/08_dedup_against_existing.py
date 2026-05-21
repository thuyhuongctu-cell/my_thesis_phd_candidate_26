"""
08_dedup_against_existing.py
Deduplicate new L2-Y candidates against the existing k=237 database.

Match strategy (no DOIs in existing DB):
  1. Exact: last_author_token + year (e.g. "lall_1982")
  2. Fuzzy: last_author_token + year ± 1 (to catch year typos)
  3. Report: new_unique / already_in_DB / uncertain

Input : p6/tools/results/l2_deep_screened_20260518.csv  (l2_deep_flag==Y)
        p6/data/p6_study_database.csv  (existing k=237)
Output: p6/tools/results/new_candidates_deduped_YYYYMMDD.csv
"""

import csv, re
from datetime import date
from pathlib import Path

BASE   = Path("/home/user/PAPERS_IN_PHD_2026")
INPUT  = BASE / "p6/tools/results/l2_deep_screened_20260518.csv"
EXIST  = BASE / "p6/data/p6_study_database.csv"
OUTDIR = BASE / "p6/tools/results"
TODAY  = date.today().strftime('%Y%m%d')
OUTPUT = OUTDIR / f"new_candidates_deduped_{TODAY}.csv"


def last_token(author_str: str) -> str:
    """Extract first author's last name token for matching."""
    if not author_str:
        return ''
    # Format in new CSV: "Wang, Mengsha; Ni, Huiqiang" → "wang"
    # Format in existing DB: "Siddharthan & Lall" → "siddharthan"
    first = re.split(r'[;,&]', author_str)[0].strip()
    # Take last word of the first token (handles "Van den Berg" → "berg")
    tokens = first.split()
    if not tokens:
        return ''
    return re.sub(r'[^a-z]', '', tokens[-1].lower())


def make_key(last: str, year: str) -> str:
    return f"{last}_{year}"


# ── Load existing DB ──────────────────────────────────────────────────────────
with open(EXIST, newline='', encoding='utf-8') as f:
    existing = list(csv.DictReader(f))

existing_keys = set()
existing_years = {}  # last_token → set of years
for row in existing:
    last = last_token(row['author'])
    yr   = row['year'].strip()
    key  = make_key(last, yr)
    existing_keys.add(key)
    existing_years.setdefault(last, set()).add(yr)


# ── Load new Y records ────────────────────────────────────────────────────────
with open(INPUT, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames) + ['dedup_status', 'dedup_key']
    all_rows = list(reader)

new_y = [r for r in all_rows if r['l2_deep_flag'] == 'Y']
print(f"New Y candidates: {len(new_y)}")
print(f"Existing DB unique keys: {len(existing_keys)}")

results = []
stats = {'new_unique': 0, 'in_existing': 0, 'uncertain': 0}

for row in new_y:
    authors = row.get('authors', '') or ''
    year    = row.get('year', '').strip() or ''
    last    = last_token(authors)

    if not last or not year:
        status = 'uncertain-no-author-year'
        stats['uncertain'] += 1
    else:
        key = make_key(last, year)
        # Exact match
        if key in existing_keys:
            status = 'in_existing'
            stats['in_existing'] += 1
        else:
            # Near-year match (±1 for publication year discrepancies)
            years_for_author = existing_years.get(last, set())
            near = any(abs(int(y) - int(year)) <= 1
                       for y in years_for_author if y.isdigit() and year.isdigit())
            if near:
                status = 'uncertain-near-year-match'
                stats['uncertain'] += 1
            else:
                status = 'new_unique'
                stats['new_unique'] += 1

    row['dedup_status'] = status
    row['dedup_key']    = make_key(last, year) if last and year else ''
    results.append(row)

# ── Write output ──────────────────────────────────────────────────────────────
with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# ── Summary ───────────────────────────────────────────────────────────────────
print(f"\nDeduplication results for {len(new_y)} Y candidates:")
print(f"  new_unique:              {stats['new_unique']}")
print(f"  in_existing (exact):     {stats['in_existing']}")
print(f"  uncertain (near-match):  {stats['uncertain']}")
print(f"\nOutput: {OUTPUT}")

# Show in_existing examples
in_ex = [r for r in results if r['dedup_status'] == 'in_existing']
print(f"\nSample already-in-DB ({len(in_ex)} total):")
for r in in_ex[:10]:
    print(f"  key={r['dedup_key']} | {r['title'][:70]}")

# Show new unique examples by priority
new_high = [r for r in results if r['dedup_status']=='new_unique' and r['priority']=='High']
print(f"\nNew unique HIGH-priority studies: {len(new_high)}")
for r in new_high[:15]:
    print(f"  [{r['seq']}] {r['year']} | {r['title'][:75]}")
