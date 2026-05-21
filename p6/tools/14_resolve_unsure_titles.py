"""
14_resolve_unsure_titles.py
Re-screen the 402 UNSURE records using aggressive title-only patterns.
Cannot fetch abstracts in this environment; uses heuristics to classify
~30% as Y and ~1% as N from title text alone.

Outputs:
  results/unsure_resolved_Y_YYYYMMDD.csv  — 123 additional Y candidates
  results/unsure_resolved_N_YYYYMMDD.csv  — 2 additional exclusions
  results/unsure_still_YYYYMMDD.csv       — 276 still need abstract

After this script, run 08_dedup_against_existing.py on resolved_Y to
identify which are genuinely new vs duplicates of existing k=287 or
current 321 new_unique.

Usage:
  python3 14_resolve_unsure_titles.py
"""

import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

BASE   = Path("/home/user/PAPERS_IN_PHD_2026")
INDIR  = BASE / "p6/tools/results"
OUTDIR = BASE / "p6/tools/results"
TODAY  = date.today().strftime('%Y%m%d')

BATCH_TEMPLATE = INDIR / "batch_screening_template_20260518.txt"
CURRENT_321    = INDIR / "extraction_worklist_20260518.csv"
EXISTING_DB    = BASE / "p6/data/p6_study_database.csv"

OUT_Y     = OUTDIR / f"unsure_resolved_Y_{TODAY}.csv"
OUT_N     = OUTDIR / f"unsure_resolved_N_{TODAY}.csv"
OUT_STILL = OUTDIR / f"unsure_still_{TODAY}.csv"

# ── Screening patterns ────────────────────────────────────────────────────────

EXCL_PATTERNS = [
    r'qualitative|case study|case-study|grounded theory|content analysis',
    r'literature review|systematic review|bibliometric|meta-analy',
    r'health|hospital|medical|patient|clinical|nursing|pharmaceutical',
    r'consumer behav|purchase intent|buyer behav|buying behav',
    r'book review|editorial|corrigendum|erratum',
    r'country.level\s+analysis|national.level|macro.level\s+study',
    r'\bsurvey instrument\b|\bscale development\b|\bquestionnaire\b',
    r'language learn|education\s+system|academic\s+performance',
    r'sports?\s+performance|athlete|tournament',
]

# Strong INCLUDE signals from title alone
INCL_PATTERNS = [
    # Direct I→P language
    r'internationalization.{0,20}(?:performance|productivity|profitab|efficiency)',
    r'(?:performance|productivity|profitab|efficiency).{0,20}internationalization',
    r'export.{0,20}(?:performance|sales|intensity|ratio)',
    r'(?:performance|profitab).{0,20}export',
    r'fdi.{0,20}(?:performance|productivity|profitab)',
    r'(?:performance|productivity).{0,20}fdi',
    r'(?:outward|inward)\s+fdi\s+and\s+(?:firm|enterprise)',
    r'multinational.{0,20}performance',
    r'degree\s+of\s+internationalization',
    r'foreign\s+sales.{0,20}(?:performance|productivity)',
    r'international\s+diversification.{0,20}(?:performance|profitab)',
    # Explicit firm performance + internationalization context
    r'(?:firm|enterprise|sme|company)\s+(?:export|international|foreign)',
    r'(?:export|international|foreign).{0,15}(?:firm|enterprise|sme|company)',
    r'export\s+(?:performance|intensit|propensit|success|competitiven)',
    r'internationalization\s+(?:decision|strategy|process).{0,20}(?:performance|result|outcome)',
    r'(?:performance|productivity|profitab)\s+of\s+(?:export|international|foreign|multinational)',
    r'international\s+(?:business|trade|market).{0,20}(?:performance|profitab|efficiency)',
    # Moderators of I→P
    r'(?:technology|digital|innovation|r&d).{0,20}(?:export|international).{0,20}performance',
    r'institutional.{0,20}(?:export|international).{0,20}performance',
    r'(?:export|international)\s+performance.{0,20}(?:moderat|mediat)',
    # Common I→P measures
    r'\bfsts\b|\bfata\b|\bdoi\b.{0,20}(?:firm|performance)',
    r'total\s+factor\s+productivity.{0,20}(?:export|trade|international)',
    r'export\s+(?:diversification|orientation|market)',
    r'(?:competitiveness|survival).{0,20}(?:exporting|internationaliz)',
]


def excl_match(text: str) -> bool:
    return any(re.search(p, text, re.I) for p in EXCL_PATTERNS)


def incl_match(text: str) -> bool:
    return any(re.search(p, text, re.I) for p in INCL_PATTERNS)


# ── Parse batch template ──────────────────────────────────────────────────────
with open(BATCH_TEMPLATE, 'r', encoding='utf-8') as f:
    content = f.read()

records = []
for block in content.split('---\n'):
    block = block.strip()
    if not block or block.startswith('#'):
        continue
    rec = {}
    for line in block.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            rec[key.strip().lower()] = val.strip()
    if 'id' in rec and 'title' in rec:
        records.append(rec)

print(f"Parsed {len(records)} UNSURE records from batch template")

# ── Build dedup keys from current 321 and existing k=287 ─────────────────────
existing_keys = set()

# From extraction worklist (321 new_unique)
with open(CURRENT_321, newline='', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        doi = str(row.get('doi', '') or '').strip().lower().lstrip('https://doi.org/').lstrip('http://dx.doi.org/')
        if doi and doi not in ('', 'none', 'nr', 'nr - full-text needed'):
            existing_keys.add(doi)
        # Also add title-year key
        title = str(row.get('title', '') or '').lower().strip()[:50]
        year  = str(row.get('year', '') or '').strip()
        if title and year:
            existing_keys.add(f"{title}|{year}")

# From existing k=287 database
with open(EXISTING_DB, newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        study_id = row.get('study_id', '').strip()
        if study_id:
            # Author + year key
            author = str(row.get('author', '')).split(',')[0].strip().lower()[:20]
            year   = str(row.get('year', '')).strip()
            if author and year:
                existing_keys.add(f"{author}|{year}")

print(f"Dedup keys loaded: {len(existing_keys)} existing records")

# ── Screen and classify ───────────────────────────────────────────────────────
y_recs, n_recs, still_recs = [], [], []
stats = Counter()

for rec in records:
    title   = rec.get('title', '')
    journal = rec.get('journal', '')
    text    = f"{title} {journal}".lower()
    year    = rec.get('year', '')
    doi     = rec.get('doi', '').strip().lower()

    is_excl = excl_match(text)
    is_incl = incl_match(text)

    # Check if already in extraction list (duplicate)
    already_exists = False
    if doi and doi not in ('', '[fetch required]'):
        clean_doi = doi.replace('https://doi.org/', '').replace('http://dx.doi.org/', '').strip()
        if clean_doi in existing_keys:
            already_exists = True
    title_key = f"{title.lower()[:50]}|{year}"
    if title_key in existing_keys:
        already_exists = True

    if already_exists:
        stats['already_in_321_or_k287'] += 1
        continue   # skip — already captured

    if is_excl and not is_incl:
        rec['screen_decision'] = 'N'
        rec['screen_reason'] = 'title_exclusion_pattern'
        n_recs.append(rec)
        stats['N_new'] += 1
    elif is_incl and not is_excl:
        rec['screen_decision'] = 'Y'
        rec['screen_reason'] = 'title_inclusion_pattern'
        y_recs.append(rec)
        stats['Y_new'] += 1
    else:
        rec['screen_decision'] = 'UNSURE'
        rec['screen_reason'] = 'title_ambiguous_needs_abstract'
        still_recs.append(rec)
        stats['still_UNSURE'] += 1

print(f"\nClassification results:")
print(f"  Already in 321/k287:  {stats['already_in_321_or_k287']}")
print(f"  New Y candidates:     {stats['Y_new']}")
print(f"  New N exclusions:     {stats['N_new']}")
print(f"  Still UNSURE:         {stats['still_UNSURE']}")

# ── Write outputs ──────────────────────────────────────────────────────────────
FIELDS = ['id', 'title', 'authors', 'year', 'journal', 'doi',
          'screen_decision', 'screen_reason']

for out_path, recs in [(OUT_Y, y_recs), (OUT_N, n_recs), (OUT_STILL, still_recs)]:
    with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction='ignore')
        w.writeheader()
        w.writerows(recs)
    print(f"  → {out_path.name}: {len(recs)} records")

print(f"\nUpdated PRISMA flow:")
print(f"  Records identified:     2,180")
print(f"  After internal dedup:   2,179")
print(f"  L1 pre-screen:          782")
print(f"  L2 initial Y:           345")
print(f"  UNSURE resolved Y:      +{stats['Y_new']}")
print(f"  Total L2 Y:             {345 + stats['Y_new']}")
print(f"  Current 321 new_unique: 321 (after dedup vs k=287)")
print(f"  Potential additions:    ~{stats['Y_new']} (need dedup + full-text verification)")
print(f"  Still need abstract:    {stats['still_UNSURE']}")
print(f"\nNext step: manually verify {stats['Y_new']} new Y candidates")
print(f"  then run 08_dedup_against_existing.py on unsure_resolved_Y_{TODAY}.csv")
