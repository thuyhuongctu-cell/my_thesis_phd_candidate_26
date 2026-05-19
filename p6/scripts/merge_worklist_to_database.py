#!/usr/bin/env python3
"""
merge_worklist_to_database.py
Merge fully-coded worklist records into p6_study_database.csv for MARA update.

Input:  extraction_worklist_v9_20260519.csv
        p6_study_database.csv (baseline k=237, K=287)
Output: p6_study_database_v2.csv (updated with WoS new records)

Code conversions:
  icrv: "1"→"I", "2"→"II", "3"→"III", "MX"→"MX", "FR"→"FR"
  dpl:  "1"→"PRE", "2"→"SPN", "3"→"FOL"
  cdai: inferred from icrv: I→"H", II→"M", III→"M", FR→"L", MX→"M"
"""
import csv
import re
from pathlib import Path
from difflib import SequenceMatcher

try:
    from rapidfuzz import fuzz
    def title_sim(a, b): return fuzz.token_sort_ratio(a.lower(), b.lower()) / 100.0
except ImportError:
    def title_sim(a, b): return SequenceMatcher(None, a.lower(), b.lower()).ratio()

WORKLIST = Path('/home/user/PAPERS_IN_PHD_2026/p6/tools/results/extraction_worklist_v9_20260519.csv')
EXISTING = Path('/home/user/PAPERS_IN_PHD_2026/p6/data/p6_study_database.csv')
OUTPUT   = Path('/home/user/PAPERS_IN_PHD_2026/p6/data/p6_study_database_v2.csv')

ICRV_MAP = {'1': 'I', '2': 'II', '3': 'III', 'MX': 'MX', 'FR': 'FR',
             'I': 'I', 'II': 'II', 'III': 'III'}
DPL_MAP  = {'1': 'PRE', '2': 'SPN', '3': 'FOL',
             'PRE': 'PRE', 'SPN': 'SPN', 'FOL': 'FOL'}
CDAI_FROM_ICRV = {'I': 'H', 'II': 'M', 'III': 'M', 'FR': 'L', 'MX': 'M'}

# fp_type codes valid for MARA
VALID_FP = {'ACC', 'LAB', 'MKT', 'MIX'}
# doi_type codes valid for MARA
VALID_DOI = {'FSTS', 'EXP', 'GEO', 'COMP', 'FDI', 'OTH'}

FULLTEXT_THRESHOLD = 0.88  # Fuzzy title dedup threshold


def normalize_doi(doi):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', doi.strip().lower())


def is_fully_complete(row):
    for f in ['r', 'n', 'icrv', 'dpl', 'doi_type', 'fp_type']:
        if not row.get(f, '').strip():
            return False
    return True


def is_excluded(row):
    return 'EXCLUDED' in row.get('extraction_status', '').upper()


def is_valid_for_mara(row):
    """Check if record passes MARA inclusion filter."""
    if is_excluded(row):
        return False, 'excluded'
    fp = row.get('fp_type', '').strip().upper()
    if fp not in VALID_FP:
        return False, f'fp_type={fp} not in {VALID_FP}'
    try:
        r = float(row['r'])
        n = int(float(row['n']))
        if n < 10:
            return False, f'n={n} < 10'
        if abs(r) > 0.999:
            return False, f'|r|={r} implausible'
    except Exception as e:
        return False, f'parse error: {e}'
    return True, 'ok'


def convert_worklist_row(row, new_study_id, new_effect_id):
    """Convert worklist row to database format."""
    icrv_raw = row.get('icrv', '').strip()
    icrv = ICRV_MAP.get(icrv_raw, icrv_raw)

    dpl_raw = row.get('dpl', '').strip()
    dpl = DPL_MAP.get(dpl_raw, dpl_raw)

    cdai = CDAI_FROM_ICRV.get(icrv, 'M')

    # Extract author surname(s) from authors field
    authors = row.get('authors', '').strip()
    if authors:
        parts = [a.strip() for a in re.split(r'[,;]', authors)]
        first_surname = parts[0].split()[-1] if parts[0].split() else parts[0]
        author_short = first_surname + (' et al.' if len(parts) > 2 else '')
    else:
        author_short = 'Unknown'

    doi_type = row.get('doi_type', '').strip().upper()
    if doi_type not in VALID_DOI:
        doi_type = 'COMP'  # fallback

    fp_type = row.get('fp_type', '').strip().upper()

    return {
        'study_id':     f'S{new_study_id}',
        'effect_id':    f'E{new_effect_id}',
        'author':       author_short,
        'year':         row.get('year', '').strip(),
        'r':            row.get('r', '').strip(),
        'n':            str(int(float(row.get('n', '0')))),
        'country':      '',
        'sample_start': '',
        'sample_end':   '',
        'icrv':         icrv,
        'cdai':         cdai,
        'dpl':          dpl,
        'doi_type':     doi_type,
        'fp_type':      fp_type,
        'include_flag': '1',
        'is_estimated': '0',
        'notes':        f'WoS-arm seq={row.get("seq","?")}; {row.get("notes","")[:100]}',
    }


def main():
    # Load existing database
    with open(EXISTING, encoding='utf-8') as f:
        existing = list(csv.DictReader(f))
    fieldnames = list(existing[0].keys())

    # Build lookup sets
    existing_dois = set()
    for r in existing:
        doi = r.get('doi', '').strip()
        if doi:
            existing_dois.add(normalize_doi(doi))

    existing_titles_years = [(r.get('title', '').strip().lower(), str(r.get('year', ''))) for r in existing]

    # Load worklist
    with open(WORKLIST, encoding='utf-8') as f:
        worklist = list(csv.DictReader(f))

    # Filter fully-complete, non-excluded, valid for MARA
    candidates = []
    skip_incomplete = 0
    skip_excluded = 0
    skip_invalid = 0

    for row in worklist:
        if is_excluded(row):
            skip_excluded += 1
            continue
        if not is_fully_complete(row):
            skip_incomplete += 1
            continue
        ok, reason = is_valid_for_mara(row)
        if not ok:
            skip_invalid += 1
            continue
        candidates.append(row)

    print(f"Worklist total:      {len(worklist)}")
    print(f"  Skip excluded:     {skip_excluded}")
    print(f"  Skip incomplete:   {skip_incomplete}")
    print(f"  Skip invalid type: {skip_invalid}")
    print(f"  Candidates:        {len(candidates)}")

    # Deduplicate against existing
    max_study_id = max(int(r['study_id'].replace('S', '')) for r in existing)
    max_effect_id = max(int(r['effect_id'].replace('E', '')) if r['effect_id'].startswith('E')
                        else int(r['effect_id']) for r in existing)

    new_study_id = max_study_id + 1
    new_effect_id = max_effect_id + 1

    accepted = []
    dup_doi = 0
    dup_title = 0

    for row in candidates:
        # DOI check
        row_doi = normalize_doi(row.get('doi', '').strip())
        if row_doi and row_doi in existing_dois:
            dup_doi += 1
            continue

        # Title fuzzy check
        row_title = row.get('title', '').strip().lower()
        row_year = str(row.get('year', '')).strip()
        is_dup = False
        for ex_title, ex_year in existing_titles_years:
            if ex_year == row_year and title_sim(row_title, ex_title) >= FULLTEXT_THRESHOLD:
                is_dup = True
                break
        if is_dup:
            dup_title += 1
            continue

        # Convert and accept
        db_row = convert_worklist_row(row, new_study_id, new_effect_id)
        accepted.append(db_row)
        # Add to lookup to prevent within-batch dups
        existing_titles_years.append((row_title, row_year))
        if row_doi:
            existing_dois.add(row_doi)
        new_study_id += 1
        new_effect_id += 1

    print(f"\nDeduplication:")
    print(f"  Duplicates (DOI):   {dup_doi}")
    print(f"  Duplicates (title): {dup_title}")
    print(f"  Accepted new:       {len(accepted)}")

    # Build merged dataset
    # Mark existing rows
    for r in existing:
        r.setdefault('include_flag', '1')

    all_rows = existing + accepted
    print(f"\nMerged database: k={len(all_rows)} total effect rows")
    print(f"  Baseline:  K={len(existing)} from k=237 studies")
    print(f"  New (WoS): K={len(accepted)} new effect rows")

    # Write output
    with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"\nSaved: {OUTPUT}")

    # Summary stats
    from collections import Counter
    icrv_all = Counter(r['icrv'] for r in all_rows if r.get('include_flag') == '1')
    dpl_all = Counter(r['dpl'] for r in all_rows if r.get('include_flag') == '1')
    print(f"\nICRV distribution: {dict(icrv_all)}")
    print(f"DPL distribution: {dict(dpl_all)}")


if __name__ == '__main__':
    main()
