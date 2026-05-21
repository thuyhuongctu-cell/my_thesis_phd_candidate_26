#!/usr/bin/env python3
"""
56_apply_extraction_audit.py — Apply audit CSV from 55_extract_structured.py to tracker
Only updates rows where converted_r is currently empty (never overwrites manual work).
Only applies AUTO_HIGH rows by default; use --min-confidence AUTO_REVIEW to expand.

Usage:
  python3 56_apply_extraction_audit.py --input structured_extraction_20260521.csv
  python3 56_apply_extraction_audit.py --input structured_extraction_20260521.csv --min-confidence AUTO_REVIEW
"""
import csv, sys, argparse
from pathlib import Path

BASE = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'
RESULTS = BASE / 'p6/tools/results'

CONFIDENCE_RANK = {"AUTO_HIGH": 3, "AUTO_REVIEW": 2, "MANUAL_REQUIRED": 1, "BLOCKED_NO_PDF": 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Audit CSV filename (in p6/tools/results/)")
    ap.add_argument("--min-confidence", default="AUTO_HIGH",
                    choices=["AUTO_HIGH", "AUTO_REVIEW", "MANUAL_REQUIRED"])
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    audit_path = RESULTS / args.input if not Path(args.input).is_absolute() else Path(args.input)
    if not audit_path.exists():
        print(f"ERROR: {audit_path} not found")
        sys.exit(1)

    min_rank = CONFIDENCE_RANK[args.min_confidence]

    with open(audit_path, newline='', encoding='utf-8') as f:
        audit_rows = {r['seq'].strip(): r for r in csv.DictReader(f)}

    with open(TRACKER, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    updated = 0
    skipped_existing = 0
    skipped_confidence = 0

    for row in rows:
        seq = row['seq'].strip()
        if seq not in audit_rows:
            continue
        audit = audit_rows[seq]

        if CONFIDENCE_RANK.get(audit.get('review_status', ''), 0) < min_rank:
            skipped_confidence += 1
            continue

        if row.get('converted_r', '').strip():
            skipped_existing += 1
            continue  # never overwrite manual work

        # Apply extraction results
        field_map = {
            'r_doi_chieu → converted_r': ('r_doi_chieu', 'converted_r'),
            'n_mau → sample_size_n': ('n_mau', 'sample_size_n'),
            'loai_r → conversion_formula': ('loai_r', 'conversion_formula'),
            'r_bao_cao → reported_coefficient': ('r_bao_cao', 'reported_coefficient'),
            't_value → t_value': ('t_value', 't_value'),
            'p_value → p_value': ('p_value', 'p_value'),
        }

        any_applied = False
        for _, (src_col, dst_col) in field_map.items():
            if audit.get(src_col, '').strip() and dst_col in row:
                row[dst_col] = audit[src_col]
                any_applied = True

        if audit.get('r_doi_chieu', '').strip():
            row['ready_for_r'] = '1'

        if any_applied:
            updated += 1
            print(f"  seq={seq} | r={row.get('converted_r','')} | n={row.get('sample_size_n','')} | {audit.get('review_status','')}")

    if not args.dry_run:
        with open(TRACKER, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            w.writeheader()
            w.writerows(rows)
        print(f"\nApplied: {updated} | Skipped (existing): {skipped_existing} | Skipped (confidence): {skipped_confidence}")
    else:
        print(f"\nDRY RUN — would apply: {updated} | skip (existing): {skipped_existing} | skip (confidence): {skipped_confidence}")


if __name__ == "__main__":
    main()
