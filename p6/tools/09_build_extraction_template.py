"""
09_build_extraction_template.py
Build a clean effect-size extraction template for the 321 new_unique studies
identified after deduplication against the existing k=237 database.

Input : p6/tools/results/new_candidates_deduped_20260518.csv
Output: p6/tools/results/extraction_template_YYYYMMDD.csv

Columns in output:
  Identification : seq, study_id, effect_id, authors, year, title, journal, doi
  Context        : priority, l2_deep_reason, dedup_key
  Sample         : country, sample_start, sample_end, n
  Effect sizes   : r, r_quadratic, turning_point, beta, t_value, f_value, df
  Moderators     : icrv, cdai, cdai_source, dpl
  Coding flags   : doi_type, fp_type, is_estimated, is_partial, is_panel,
                   endogeneity_corrected, extraction_status, coder, notes

Pre-filled from pre-screening where possible:
  icrv  ← prescreen_icrv  (if available)
  cdai  ← cdai (if already set)
  dpl   ← inferred from sample_end year range
  doi_type ← prescreen_doi_type
  fp_type  ← prescreen_fp_type
"""

import csv
import re
from datetime import date
from pathlib import Path

BASE   = Path("/home/user/PAPERS_IN_PHD_2026")
INPUT  = BASE / "p6/tools/results/new_candidates_deduped_20260518.csv"
OUTDIR = BASE / "p6/tools/results"
TODAY  = date.today().strftime('%Y%m%d')
OUTPUT = OUTDIR / f"extraction_template_{TODAY}.csv"

PRIORITY_ORDER = {'High': 0, 'Medium': 1, 'Low': 2, '': 3}

OUTPUT_FIELDS = [
    # ── Identification ────────────────────────────────────────────────────
    'seq', 'study_id', 'effect_id',
    'authors', 'year', 'title', 'journal', 'doi',
    # ── Screening context ─────────────────────────────────────────────────
    'priority', 'l2_deep_reason', 'dedup_key',
    # ── Sample descriptors ────────────────────────────────────────────────
    'country', 'sample_start', 'sample_end', 'n',
    # ── Primary effect size (fill one of r / beta / t_value / f_value) ───
    'r',            # Pearson r (preferred)
    'r_quadratic',  # quadratic term r (if nonlinear model)
    'turning_point',# TP* in % FSTS (if reported)
    'beta',         # standardized β (if r not available)
    't_value',      # t-statistic (if β/r not reported directly)
    'f_value',      # F-statistic (df1=1, for conversion to r)
    'df',           # denominator df for t/F conversion
    # ── Moderator coding ──────────────────────────────────────────────────
    'icrv',         # 1–6: Advanced(1) → SIDS/Frontier(6)
    'cdai',         # World Bank DAI 0–1 (country-level)
    'cdai_source',  # year of DAI observation used
    'dpl',          # Digital Platform Lifecycle: 1=pre-2000, 2=2000-09, 3=2010+
    # ── Study design flags ────────────────────────────────────────────────
    'doi_type',         # FSTS/EI/entropy/count/binary/other
    'fp_type',          # ROA/ROE/Tobin/ROS/Sales_growth/LP/composite/other
    'is_estimated',     # 1 if r converted from β/t/F, 0 if reported directly
    'is_partial',       # 1 if partial correlation (controls included)
    'is_panel',         # 1 if panel data, 0 if cross-sectional
    'endogeneity_corrected',  # 1 if IV/2SLS/GMM/Heckman used
    # ── Workflow ──────────────────────────────────────────────────────────
    'extraction_status',  # blank / in_progress / done / cannot_access
    'coder',              # initials of person extracting
    'notes',
]


def infer_dpl(year_str: str) -> str:
    """Infer DPL phase from sample_end or publication year."""
    try:
        yr = int(year_str.strip())
        if yr < 2000:
            return '1'
        elif yr <= 2009:
            return '2'
        else:
            return '3'
    except (ValueError, AttributeError):
        return ''


def build_study_id(authors: str, year: str) -> str:
    """Generate candidate study_id in author_year format."""
    if not authors or not year:
        return ''
    first = re.split(r'[;,&]', authors)[0].strip()
    last = first.split()[-1] if first.split() else ''
    last = re.sub(r'[^a-zA-Z]', '', last).lower()
    return f"{last}_{year.strip()}" if last else ''


with open(INPUT, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

# Filter to new_unique only
unique = [r for r in rows if r['dedup_status'] == 'new_unique']
print(f"Total new_unique: {len(unique)}")

# Sort: High → Medium → Low, then by year desc, then seq
unique.sort(key=lambda r: (
    PRIORITY_ORDER.get(r.get('priority', ''), 3),
    -int(r.get('year', '0') or '0'),
    int(r.get('seq', '9999') or '9999'),
))

out_rows = []
for i, row in enumerate(unique, 1):
    year = row.get('year', '').strip()

    # Seed study_id / effect_id (researcher will finalize)
    sid = row.get('study_id', '').strip() or build_study_id(row.get('authors', ''), year)
    eid = row.get('effect_id', '').strip() or f"{sid}_e1"

    # Seed moderators from pre-screening when available
    icrv     = row.get('prescreen_icrv', '').strip() or row.get('icrv', '').strip()
    cdai     = row.get('cdai', '').strip()
    cdai_src = row.get('cdai_source', '').strip()
    dpl      = row.get('dpl', '').strip() or infer_dpl(year)
    doi_type = row.get('prescreen_doi_type', '').strip() or row.get('doi_type', '').strip()
    fp_type  = row.get('prescreen_fp_type', '').strip() or row.get('fp_type', '').strip()

    out = {
        'seq':          row.get('seq', str(i)),
        'study_id':     sid,
        'effect_id':    eid,
        'authors':      row.get('authors', ''),
        'year':         year,
        'title':        row.get('title', ''),
        'journal':      row.get('journal', ''),
        'doi':          row.get('doi_enriched', ''),
        'priority':     row.get('priority', ''),
        'l2_deep_reason': row.get('l2_deep_reason', ''),
        'dedup_key':    row.get('dedup_key', ''),
        'country':      row.get('country', ''),
        'sample_start': row.get('sample_start', ''),
        'sample_end':   row.get('sample_end', ''),
        'n':            row.get('n', ''),
        'r':            row.get('r', ''),
        'r_quadratic':  row.get('r_quadratic', ''),
        'turning_point':row.get('turning_point', ''),
        'beta':         '',
        't_value':      '',
        'f_value':      '',
        'df':           '',
        'icrv':         icrv,
        'cdai':         cdai,
        'cdai_source':  cdai_src,
        'dpl':          dpl,
        'doi_type':     doi_type,
        'fp_type':      fp_type,
        'is_estimated':    row.get('is_estimated', ''),
        'is_partial':      row.get('is_partial', ''),
        'is_panel':        row.get('is_panel', ''),
        'endogeneity_corrected': row.get('endogeneity_corrected', ''),
        'extraction_status': '',
        'coder':         '',
        'notes':         row.get('notes', ''),
    }
    out_rows.append(out)

with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDS)
    writer.writeheader()
    writer.writerows(out_rows)

# ── Summary ───────────────────────────────────────────────────────────────────
prio_counts = {}
dpl_counts  = {}
for r in out_rows:
    prio_counts[r['priority']] = prio_counts.get(r['priority'], 0) + 1
    dpl_counts[r['dpl']]       = dpl_counts.get(r['dpl'], 0) + 1

doi_pre = sum(1 for r in out_rows if r['doi'])
icrv_pre = sum(1 for r in out_rows if r['icrv'])

print(f"\nExtraction template: {OUTPUT}")
print(f"Total rows: {len(out_rows)}")
print()
print("Priority distribution:")
for k in ['High', 'Medium', 'Low', '']:
    if prio_counts.get(k):
        print(f"  {k or 'unset'}: {prio_counts[k]}")
print()
print("DPL phase pre-filled:")
for k in ['1', '2', '3', '']:
    if dpl_counts.get(k):
        label = {'1': 'pre-2000', '2': '2000-2009', '3': '2010+'}.get(k, 'unknown')
        print(f"  Phase {k} ({label}): {dpl_counts[k]}")
print()
print(f"DOI pre-filled:  {doi_pre}/{len(out_rows)} ({100*doi_pre//len(out_rows)}%)")
print(f"ICRV pre-filled: {icrv_pre}/{len(out_rows)}")

# Show High-priority sample
high = [r for r in out_rows if r['priority'] == 'High']
print(f"\nHigh-priority studies ({len(high)}) — first 10:")
for r in high[:10]:
    print(f"  [{r['seq']:>4}] {r['year']} DPL={r['dpl']} ICRV={r['icrv'] or '?'} | {r['title'][:65]}")
