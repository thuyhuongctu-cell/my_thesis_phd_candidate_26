#!/usr/bin/env python3
"""
58_bulk_fill_r.py — Bulk-fill r values into tracker from a simple CSV input.

Input CSV must have at minimum: seq, r, n
Optional: conversion_formula, t_stat, p_value, beta, se, dv_type, iv_type, notes

Usage:
  python3 p6/tools/58_bulk_fill_r.py --input my_r_values.csv
  python3 p6/tools/58_bulk_fill_r.py --input my_r_values.csv --dry-run

Template (save as r_batch_input.csv):
  seq,r,n,conversion_formula,t_stat,p_value,beta,se,notes
  123,0.18,450,direct,,,,,Korean SMEs panel 2010-2020
  456,-0.09,1200,beta,-2.3,0.021,-0.09,0.04,ROA ~ FSTS OLS

Will NEVER overwrite existing non-empty converted_r values.
"""
import csv, math, sys, argparse
from pathlib import Path

BASE    = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'

def fisher_z(r: float) -> float:
    r = max(min(r, 0.9999), -0.9999)
    return 0.5 * math.log((1 + r) / (1 - r))

def variance_z(n: int) -> float:
    return 1.0 / max(n - 3, 1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',   required=True)
    parser.add_argument('--tracker', default=str(TRACKER))
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    with open(args.input) as f:
        inputs = {r['seq'].strip(): r for r in csv.DictReader(f)}
    print(f"Input rows: {len(inputs)}")

    with open(args.tracker) as f:
        rows = list(csv.DictReader(f))
        fieldnames = list(rows[0].keys())

    updated = 0
    skipped = 0
    for row in rows:
        seq = row.get('seq','').strip()
        if seq not in inputs:
            continue
        if row.get('converted_r','').strip():
            print(f"  SKIP seq={seq}: already has r={row['converted_r']}")
            skipped += 1
            continue

        inp = inputs[seq]
        try:
            r = float(inp.get('r','').strip())
        except (ValueError, TypeError):
            print(f"  SKIP seq={seq}: invalid r={inp.get('r')}")
            continue

        try:
            n = int(inp.get('n','').strip())
        except (ValueError, TypeError):
            n = None

        row['converted_r']        = str(round(r, 6))
        row['conversion_formula'] = inp.get('conversion_formula','').strip() or 'manual'
        row['ready_for_r']        = '1'
        if n:
            row['sample_size_n'] = str(n)
            row['fisher_z']      = str(round(fisher_z(r), 6))
            row['variance_z']    = str(round(variance_z(n), 8))
        if inp.get('t_stat','').strip():
            row['t_value'] = inp['t_stat'].strip()
        if inp.get('p_value','').strip():
            row['p_value'] = inp['p_value'].strip()
        if inp.get('beta','').strip():
            row['reported_coefficient'] = inp['beta'].strip()
        if inp.get('se','').strip():
            row['standard_error'] = inp['se'].strip()
        if inp.get('notes','').strip():
            existing = row.get('notes_for_extractor','')
            row['notes_for_extractor'] = (existing + ' | ' + inp['notes'].strip()).strip(' | ')
        if inp.get('dv_type','').strip():
            row['fp_type'] = inp['dv_type'].strip()

        updated += 1
        if args.dry_run:
            print(f"  [DRY] seq={seq}: r={r}, n={n}, formula={row['conversion_formula']}")

    if not args.dry_run:
        with open(args.tracker, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(rows)
        print(f"\nTracker updated: {args.tracker}")

    print(f"\nUpdated: {updated} | Skipped (existing r): {skipped}")

if __name__ == '__main__':
    main()
