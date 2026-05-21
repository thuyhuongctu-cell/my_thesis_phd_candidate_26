#!/usr/bin/env python3
"""
53_apply_s2_auto_screen.py
Apply auto-screen decisions from 50_fetch_s2_abstracts_unsure.py output
to the main tracker. Only updates auto-N decisions (conservative: keeps 
UNSURE_L2 as UNSURE for manual review).

Input:  s2_auto_screen_YYYYMMDD.csv  (from script 50)
        fulltext_to_extraction_tracker_v3.csv
Output: UPDATES tracker (N decisions only — safe, conservative)
        Prints count of changes

Usage:
  python3 53_apply_s2_auto_screen.py [--date YYYYMMDD]  # default=today
"""
import csv, sys, argparse
from datetime import date
from pathlib import Path
from collections import Counter

TODAY = date.today().strftime('%Y%m%d')
BASE  = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'

def main(screen_date: str):
    screen_file = BASE / f'p6/tools/results/s2_auto_screen_{screen_date}.csv'
    if not screen_file.exists():
        print(f'ERROR: {screen_file} not found. Run 50_fetch_s2_abstracts_unsure.py first.')
        sys.exit(1)

    # Load auto-screen decisions
    with open(screen_file, newline='', encoding='utf-8') as f:
        screen_rows = {r['seq'].strip(): r for r in csv.DictReader(f)}

    print(f'Loaded {len(screen_rows)} auto-screen decisions from {screen_file.name}')
    dist = Counter(r['auto_decision'] for r in screen_rows.values())
    print(f'Distribution: {dict(dist)}')

    # Load tracker
    with open(TRACKER, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    updated_n = 0
    updated_unsure_l2 = 0

    for row in rows:
        seq = row['seq'].strip()
        if seq not in screen_rows:
            continue
        if row.get('fulltext_screening_decision','').strip() != 'UNSURE':
            continue  # only update UNSURE papers

        decision = screen_rows[seq]['auto_decision']
        reason   = screen_rows[seq]['auto_reason']

        if decision == 'N':
            row['fulltext_screening_decision'] = 'N'
            row['fulltext_screening_reason'] = reason
            updated_n += 1
        elif decision == 'UNSURE_L2':
            row['fulltext_screening_decision'] = 'UNSURE_L2'
            row['fulltext_screening_reason'] = reason
            updated_unsure_l2 += 1
        # Leave other UNSURE as-is

    # Write back
    with open(TRACKER, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)

    print(f'\nApplied: {updated_n} auto-N, {updated_unsure_l2} flagged UNSURE_L2')
    
    # Final counts
    final_dist = Counter(r.get('fulltext_screening_decision','').strip() for r in rows)
    print('Final tracker distribution:', dict(sorted(final_dist.items())))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--date', default=TODAY)
    args = p.parse_args()
    main(args.date)
