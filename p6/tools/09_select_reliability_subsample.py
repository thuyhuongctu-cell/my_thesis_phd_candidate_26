#!/usr/bin/env python3
"""
09_select_reliability_subsample.py — Select 20% stratified reliability subsample.

Input:  fulltext_to_extraction_tracker_v3.csv (after ready_for_r=1 rows exist)
Output: reliability_subsample_YYYYMMDD.csv — stratified by DPL x ICRV

Usage:
    python3 p6/tools/09_select_reliability_subsample.py
    python3 p6/tools/09_select_reliability_subsample.py --pct 0.20 --min-n 20
    python3 p6/tools/09_select_reliability_subsample.py --seed 42 --dry-run
"""

import argparse, csv, random, math, sys
from pathlib import Path
from datetime import date
from collections import defaultdict, Counter

DEFAULT_TRACKER = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
DEFAULT_OUTPUT  = f"p6/tools/results/reliability_subsample_{date.today().strftime('%Y%m%d')}.csv"


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--tracker", default=DEFAULT_TRACKER)
    p.add_argument("--output",  default=DEFAULT_OUTPUT)
    p.add_argument("--seed",    type=int,   default=42)
    p.add_argument("--pct",     type=float, default=0.20, help="Fraction to sample (default 0.20)")
    p.add_argument("--min-n",   type=int,   default=20,   help="Minimum subsample size (default 20)")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def main():
    args = parse_args()
    random.seed(args.seed)

    with open(args.tracker, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())

    # Only sample from fully extracted papers
    ready = [r for r in rows if r.get("ready_for_r", "").strip() == "1"]
    if not ready:
        print("ERROR: No ready_for_r=1 rows found.", file=sys.stderr)
        print("       Complete manual extraction and set ready_for_r=1 first.", file=sys.stderr)
        sys.exit(1)

    # Stratify by DPL x ICRV
    strata = defaultdict(list)
    for r in ready:
        dpl  = r.get("dpl", "").strip() or "?"
        icrv_raw = r.get("icrv", "").strip() or "?"
        icrv_g = icrv_raw if icrv_raw in ("1", "2", "3", "0") else "4+"
        strata[(dpl, icrv_g)].append(r)

    sample = []
    for (dpl, icrv_g), group in strata.items():
        n_take = max(1, math.ceil(len(group) * args.pct))
        n_take = min(n_take, len(group))
        sample.extend(random.sample(group, n_take))

    # Top-up to min_n if needed
    selected_seqs = {r["seq"] for r in sample}
    remaining = [r for r in ready if r["seq"] not in selected_seqs]
    if len(sample) < args.min_n and remaining:
        topup = random.sample(remaining, min(args.min_n - len(sample), len(remaining)))
        sample.extend(topup)

    print(f"ready_for_r=1 rows: {len(ready)}")
    print(f"Subsample selected: {len(sample)} ({len(sample)/len(ready):.0%})")
    print("Strata breakdown (DPL, ICRV):")
    for (dpl, icrv_g), n in sorted(Counter(
            (r.get("dpl","?"), r.get("icrv","?") or "?") for r in sample
    ).items()):
        print(f"  DPL={dpl}, ICRV={icrv_g}: {n}")

    if args.dry_run:
        print("\n[DRY RUN] No file written.")
        return

    # Add coder comparison columns (coder1 = current extraction, coder2 = blank)
    extended = fieldnames + ["coder1_icrv", "coder1_r", "coder1_n",
                             "coder2_icrv", "coder2_r", "coder2_n", "agreement_flag"]
    out_rows = []
    for r in sample:
        out = dict(r)
        out["coder1_icrv"]    = r.get("icrv", "")
        out["coder1_r"]       = r.get("converted_r", "")
        out["coder1_n"]       = r.get("sample_size_n", "")
        out["coder2_icrv"]    = ""
        out["coder2_r"]       = ""
        out["coder2_n"]       = ""
        out["agreement_flag"] = ""
        out_rows.append(out)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=extended, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"\nOutput: {args.output}")
    print(f"\nNext steps:")
    print(f"  1. Give subsample to Coder 2 (strip coder1_* columns before sharing)")
    print(f"  2. Both code INDEPENDENTLY: icrv, dpl, fp_type, converted_r, sample_size_n")
    print(f"  3. Merge and compute: Rscript p6/tools/compute_reliability.R")
    print(f"  4. Targets: κ ≥ 0.70 (categorical), ICC ≥ 0.80 (continuous)")


if __name__ == "__main__":
    main()
