"""
10_select_reliability_subsample.py
Select a stratified random 20% subsample of Y records for inter-coder reliability.

NOT USED IN THE CURRENT STUDY: P6 is single-coder, so no inter-coder reliability
is reported (disclosed as a pre-registration deviation in the manuscript). This
is dormant tooling, retained only for the planned formal-search expansion IF a
second independent coder becomes available.

Stratification: DPL phase (1/2/3) × priority (High/Medium/Low)
Target: κ ≥ 0.70 for categorical fields, ICC ≥ 0.80 for r

Input : p6/tools/results/extraction_template_YYYYMMDD.csv  (most recent)
Output: p6/tools/results/reliability_subsample_YYYYMMDD.csv

Usage:
  python3 10_select_reliability_subsample.py
  python3 10_select_reliability_subsample.py --seed 42  # reproducible draw
  python3 10_select_reliability_subsample.py --pct 0.25 # 25% instead of 20%
"""

import csv
import random
import sys
from datetime import date
from pathlib import Path

BASE   = Path("/home/user/PAPERS_IN_PHD_2026")
INDIR  = BASE / "p6/tools/results"
OUTDIR = BASE / "p6/tools/results"
TODAY  = date.today().strftime('%Y%m%d')

# ── Args ─────────────────────────────────────────────────────────────────────
seed = 2026
pct  = 0.20
for i, arg in enumerate(sys.argv[1:], 1):
    if arg == '--seed' and i < len(sys.argv):
        seed = int(sys.argv[i + 1])
    if arg == '--pct' and i < len(sys.argv):
        pct = float(sys.argv[i + 1])

# ── Find most recent extraction template ─────────────────────────────────────
templates = sorted(INDIR.glob('extraction_template_*.csv'), reverse=True)
if not templates:
    sys.exit("ERROR: no extraction_template_*.csv found in results/")
INPUT  = templates[0]
OUTPUT = OUTDIR / f"reliability_subsample_{TODAY}.csv"
print(f"Using: {INPUT.name}")

# ── Load ─────────────────────────────────────────────────────────────────────
with open(INPUT, newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
    fieldnames = list(csv.DictReader(open(INPUT, newline='', encoding='utf-8')).fieldnames)

# ── Stratify by DPL × priority ───────────────────────────────────────────────
strata: dict[tuple, list] = {}
for row in rows:
    key = (row.get('dpl', '') or 'unk', row.get('priority', '') or 'unk')
    strata.setdefault(key, []).append(row)

random.seed(seed)
selected = []
for key, group in sorted(strata.items()):
    n = max(1, round(len(group) * pct))
    draw = random.sample(group, min(n, len(group)))
    selected.extend(draw)
    print(f"  Stratum DPL={key[0]} Prio={key[1]}: {len(group)} total → {len(draw)} selected")

# Add coder columns
fieldnames_out = list(fieldnames) + ['coder2_r', 'coder2_icrv', 'coder2_dpl',
                                      'coder2_doi_type', 'coder2_fp_type',
                                      'coder2_include', 'coder2_notes']
for row in selected:
    for col in ['coder2_r', 'coder2_icrv', 'coder2_dpl',
                'coder2_doi_type', 'coder2_fp_type', 'coder2_include', 'coder2_notes']:
        row[col] = ''

# ── Write ─────────────────────────────────────────────────────────────────────
with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames_out)
    writer.writeheader()
    writer.writerows(selected)

print(f"\nReliability subsample: {len(selected)}/{len(rows)} "
      f"({100*len(selected)//len(rows)}%) → {OUTPUT.name}")
print(f"Seed: {seed}  |  Target: κ≥0.70 categorical, ICC≥0.80 for r")
print("\nNext steps:")
print("  1. Coder 1 fills: r, icrv, dpl, doi_type, fp_type, is_estimated, include_flag")
print("  2. Coder 2 fills: coder2_* columns independently")
print("  3. Run: Rscript p6/tools/compute_reliability.R reliability_subsample_*.csv")
