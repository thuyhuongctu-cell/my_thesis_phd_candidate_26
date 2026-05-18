#!/usr/bin/env python3
"""
09_select_reliability_subsample.py — Select 20% stratified reliability subsample.

Input:  L2 extraction template (after coding is complete, include_flag filled)
Output: reliability_subsample.csv — ~20% stratified by DPL phase and ICRV regime

Usage:
    python3 09_select_reliability_subsample.py \
        --input  p6/tools/results/l2_extraction_template.csv \
        --output p6/tools/results/reliability_subsample.csv \
        --seed   42
"""

import argparse
import csv
import random
import sys
from pathlib import Path
from collections import defaultdict


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--input",  required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--seed",   type=int, default=42)
    p.add_argument("--pct",    type=float, default=0.20, help="Fraction to sample (default 0.20)")
    return p.parse_args()


def main():
    args = parse_args()
    src = Path(args.input)
    dst = Path(args.output)
    dst.parent.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(open(src, encoding="utf-8")))

    # Only sample from INCLUDE studies
    included = [r for r in rows if r.get("include_flag", "").strip().upper() == "Y"]
    if not included:
        print("No included studies (include_flag == Y) found. Run after L2 screening.", file=sys.stderr)
        sys.exit(1)

    # Stratify by DPL x ICRV
    strata = defaultdict(list)
    for r in included:
        dpl  = r.get("dpl", "").strip() or "unknown"
        icrv = r.get("icrv", "").strip() or "unknown"
        strata[(dpl, icrv)].append(r)

    random.seed(args.seed)
    sample = []
    for key, group in strata.items():
        n_take = max(1, round(len(group) * args.pct))
        n_take = min(n_take, len(group))
        sample.extend(random.sample(group, n_take))

    # Deduplicate (in case rounding adds duplicates)
    seen = set()
    unique_sample = []
    for r in sample:
        uid = r.get("title", "") + r.get("year", "")
        if uid not in seen:
            seen.add(uid)
            unique_sample.append(r)

    # Add coder columns
    for r in unique_sample:
        r["coder1_include_flag"] = r.get("include_flag", "")
        r["coder1_icrv"]         = r.get("icrv", "")
        r["coder1_dpl"]          = r.get("dpl", "")
        r["coder1_r"]            = r.get("r", "")
        r["coder1_n"]            = r.get("n", "")
        r["coder2_include_flag"] = ""
        r["coder2_icrv"]         = ""
        r["coder2_dpl"]          = ""
        r["coder2_r"]            = ""
        r["coder2_n"]            = ""
        r["agreement_flag"]      = ""  # Y/N — to be filled after double-coding

    fieldnames = list(unique_sample[0].keys())
    with open(dst, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_sample)

    total_pct = len(unique_sample) / len(included) * 100
    print(f"Included studies   : {len(included)}")
    print(f"Sample size        : {len(unique_sample)} ({total_pct:.1f}%)")
    print(f"Strata covered     : {len(strata)}")
    print(f"Output             : {dst}")
    print()
    print("Next steps:")
    print("  1. Share reliability_subsample.csv with Coder 2")
    print("  2. Each coder fills coder1_* / coder2_* columns INDEPENDENTLY")
    print("  3. Run compute_reliability.R to compute ICC and kappa")


if __name__ == "__main__":
    main()
