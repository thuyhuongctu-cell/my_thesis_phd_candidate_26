#!/usr/bin/env python3
"""
58_merge_oa_manifests.py — Merge multiple Unpaywall/OA manifest CSVs into one

Usage:
  python3 p6/tools/58_merge_oa_manifests.py                     # auto-merge all oa_manifest_*.csv
  python3 p6/tools/58_merge_oa_manifests.py --out merged.csv    # specify output
  python3 p6/tools/58_merge_oa_manifests.py a.csv b.csv         # explicit inputs

Output: merged CSV with one row per seq (latest pdf_url wins if conflict).
Also prints stats: total, OA, with PDF URL.
"""
import csv, glob, sys, argparse
from pathlib import Path

RESULTS_DIR = Path(__file__).parent / 'results'


def load_manifest(path: str) -> list[dict]:
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def merge_manifests(paths: list[str]) -> tuple[list[dict], list[str]]:
    merged: dict[str, dict] = {}
    fieldnames: list[str] = []

    for p in paths:
        rows = load_manifest(p)
        if not rows:
            continue
        if not fieldnames:
            fieldnames = list(rows[0].keys())
        for row in rows:
            seq = row.get('seq', '').strip()
            if not seq:
                continue
            if seq not in merged:
                merged[seq] = row
            else:
                # Prefer row with a pdf_url
                existing_pdf = merged[seq].get('pdf_url', '').strip()
                new_pdf = row.get('pdf_url', '').strip()
                if not existing_pdf and new_pdf:
                    merged[seq] = row

    sorted_rows = sorted(merged.values(), key=lambda r: int(r.get('seq', 0)) if r.get('seq', '').isdigit() else 0)
    return sorted_rows, fieldnames


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('inputs', nargs='*', help='Manifest CSV files to merge')
    parser.add_argument('--out', default=None, help='Output path (default: oa_manifest_merged.csv in results/)')
    args = parser.parse_args()

    if args.inputs:
        paths = args.inputs
    else:
        paths = sorted(glob.glob(str(RESULTS_DIR / 'oa_manifest_*.csv')))
        if not paths:
            print("No oa_manifest_*.csv files found in results/")
            sys.exit(1)

    print(f"Merging {len(paths)} manifest(s):")
    for p in paths:
        rows = load_manifest(p)
        pdf = sum(1 for r in rows if r.get('pdf_url', '').strip())
        print(f"  {Path(p).name}: {len(rows)} rows, {pdf} with PDF URL")

    merged, fieldnames = merge_manifests(paths)

    out_path = Path(args.out) if args.out else RESULTS_DIR / 'oa_manifest_merged.csv'
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(merged)

    oa = sum(1 for r in merged if r.get('is_oa', '') in ('True', 'true', '1'))
    pdf = sum(1 for r in merged if r.get('pdf_url', '').strip())
    print(f"\nMerged output: {out_path}")
    print(f"  Total unique papers: {len(merged)}")
    print(f"  OA available: {oa}")
    print(f"  With PDF URL: {pdf} ({round(pdf/len(merged)*100,1) if merged else 0}%)")


if __name__ == '__main__':
    main()
