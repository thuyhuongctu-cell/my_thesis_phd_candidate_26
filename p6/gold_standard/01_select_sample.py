#!/usr/bin/env python3
"""
01_select_sample.py — Stratified random sample selection for gold-standard
                      evaluation of the LLM-assisted extraction workflow.

Outputs:
  p6/gold_standard/gold_standard_sample.csv
    32 effect-rows selected by stratified random sampling on (icrv, dpl, doi_type).
    Stratification ensures coverage of:
      - ICRV regimes I/II/III/FR/MX (all 5 populated regimes)
      - DPL phases PRE/SPN/FOL (all 3)
      - DOI types FSTS/GEO/EXP/COMP (the 4 main; FDI and OTH have too few)

Sampling design rationale:
  - Target n=30-40 effect rows (effect_id is the unit) to balance statistical
    power for kappa estimation (typically n>=30 for stable kappa) against
    manual-extraction time (~30-60 min/paper for the human reviewer).
  - Within each stratum, simple random sampling with seed=42 for reproducibility.
  - Effect-rows (not study-rows) are sampled to reflect the actual extraction
    unit; multi-effect studies will appear once per sampled effect.

Usage:
  cd /path/to/MY_THESIS_PHD_CANDIDATE_26
  python3 p6/gold_standard/01_select_sample.py
"""
import csv, random
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC  = ROOT / 'p6' / 'data' / 'p6_study_database.csv'
OUT  = ROOT / 'p6' / 'gold_standard' / 'gold_standard_sample.csv'
SEED = 42

# Strata design: target counts per cell (sums to 32)
# Calibrated to reflect corpus composition while ensuring all regimes covered.
STRATA_TARGETS = {
    'I':   12,   # 139/288 ~ 48% of corpus -> 12/32 ~ 37% in sample (slightly under-rep to widen coverage)
    'II':   5,   # 25/288 ~ 9%  -> 5/32 ~ 16% (over-rep, small regime needs more)
    'III':  9,   # 91/288 ~ 32% -> 9/32 ~ 28%
    'FR':   3,   # 3/288 ~ 1%   -> ALL (census)
    'MX':   3,   # 30/288 ~ 10% -> 3/32 ~ 9%
}
# Total = 32 (32 effect-rows; expect ~28-30 unique studies after dedup)

def main():
    random.seed(SEED)

    with open(SRC, encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    # Bucket by icrv
    by_icrv = defaultdict(list)
    for r in rows:
        if r.get('include_flag', '').strip() not in ('', '0', 'false', 'False', 'FALSE'):
            by_icrv[r['icrv'].strip()].append(r)

    print(f"Source: {SRC.relative_to(ROOT)} ({len(rows)} effect-rows)")
    print(f"Strata available: {dict((k, len(v)) for k, v in by_icrv.items())}")

    sample = []
    for icrv, target in STRATA_TARGETS.items():
        pool = by_icrv.get(icrv, [])
        if len(pool) <= target:
            picked = pool                       # take all (e.g., FR with K=3)
            note = '(census: all available)'
        else:
            picked = random.sample(pool, target)
            note = f'(random sample of {target} from {len(pool)})'
        for p in picked:
            p['_sample_stratum'] = icrv
        sample.extend(picked)
        print(f"  ICRV={icrv:3s}: picked {len(picked):2d} {note}")

    print(f"\nTotal sampled effect-rows: {len(sample)}")
    print(f"Unique studies: {len(set(r['study_id'] for r in sample))}")

    # Distribution check
    dpl_dist = Counter(r['dpl'].strip() for r in sample)
    doi_dist = Counter(r['doi_type'].strip() for r in sample)
    fp_dist  = Counter(r['fp_type'].strip() for r in sample)
    print(f"\nResulting DPL distribution: {dict(dpl_dist)}")
    print(f"Resulting DOI distribution: {dict(doi_dist)}")
    print(f"Resulting FP  distribution: {dict(fp_dist)}")

    # Write sample to file with all original columns + stratum tag
    cols = list(sample[0].keys())
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(sample)
    print(f"\nWrote: {OUT.relative_to(ROOT)}")
    print(f"Sample seed: {SEED} (deterministic, re-runnable)")


if __name__ == '__main__':
    main()
