#!/usr/bin/env python3
"""Compute inter-coder reliability for P6 after dual-coding is complete.

Usage:
    python3 p6/icr/02_compute_icr.py

Reads:
    p6/icr/icr_subsample_master.csv          (coder 1 = PI codes)
    p6/icr/icr_coding_sheet_coder2_FILLED.csv (coder 2's completed sheet)

Reports, per the protocol in manuscript section 3.3.2:
  - Cohen's kappa (unweighted) for categorical variables:
      icrv (5 regimes), dpl (3 phases), doi_type, fp_type
  - For cdai: the database stores an ordinal H/M/L code, so this script
    reports BOTH unweighted and linear-weighted kappa. If the authors later
    add a continuous 0-1 cDAI column, ICC(2,1) is computed for it instead.

Refuses to run on an incomplete coder-2 sheet (any blank code cell), so no
reliability statistic can be produced from partial or fabricated data.
"""
import sys
import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).resolve().parent
MASTER = OUT / "icr_subsample_master.csv"
CODER2 = OUT / "icr_coding_sheet_coder2_FILLED.csv"

CAT_COLS = ["icrv", "dpl", "doi_type", "fp_type"]
ORDINAL_MAP = {"L": 0, "M": 1, "H": 2}


def cohens_kappa(a, b, weights=None):
    cats = sorted(set(a) | set(b))
    idx = {c: i for i, c in enumerate(cats)}
    k = len(cats)
    M = np.zeros((k, k))
    for x, y in zip(a, b):
        M[idx[x], idx[y]] += 1
    n = M.sum()
    if weights == "linear":
        W = np.abs(np.subtract.outer(np.arange(k), np.arange(k))) / (k - 1)
    else:
        W = 1 - np.eye(k)
    row = M.sum(1) / n
    col = M.sum(0) / n
    E = np.outer(row, col)
    po = 1 - (W * M / n).sum()
    pe = 1 - (W * E).sum()
    return (po - pe) / (1 - pe) if pe < 1 else np.nan


def icc_2_1(x, y):
    """Two-way random effects, absolute agreement, single rater: ICC(2,1)."""
    data = np.column_stack([x, y]).astype(float)
    n, k = data.shape
    grand = data.mean()
    row_m = data.mean(1)
    col_m = data.mean(0)
    ss_rows = k * ((row_m - grand) ** 2).sum()
    ss_cols = n * ((col_m - grand) ** 2).sum()
    ss_total = ((data - grand) ** 2).sum()
    ss_err = ss_total - ss_rows - ss_cols
    ms_r = ss_rows / (n - 1)
    ms_c = ss_cols / (k - 1)
    ms_e = ss_err / ((n - 1) * (k - 1))
    return (ms_r - ms_e) / (ms_r + (k - 1) * ms_e + k * (ms_c - ms_e) / n)


def main():
    if not CODER2.exists():
        sys.exit(
            f"ERROR: {CODER2.name} not found.\n"
            "Coder 2 must complete icr_coding_sheet_coder2_BLANK.csv from the "
            "source papers (blind to the master sheet), save it as "
            "icr_coding_sheet_coder2_FILLED.csv, then re-run this script.\n"
            "This script will NOT produce statistics without real second-coder data."
        )
    m = pd.read_csv(MASTER, dtype=str)
    c2 = pd.read_csv(CODER2, dtype=str)

    merged = m.merge(c2, on="study_id", suffixes=("_c1", "_c2"))
    if len(merged) != len(m):
        sys.exit(f"ERROR: study_id mismatch (master {len(m)}, merged {len(merged)}).")

    code_cols = CAT_COLS + ["cdai"]
    blanks = {
        c: merged[f"{c}_c2"].isna().sum() + (merged[f"{c}_c2"].str.strip() == "").sum()
        for c in code_cols
    }
    if any(v > 0 for v in blanks.values()):
        sys.exit(f"ERROR: coder-2 sheet has blank cells: {blanks}. Complete all rows first.")

    print(f"k = {len(merged)} studies dual-coded\n")
    print(f"{'Variable':<22}{'Statistic':<28}{'Value':>8}   Threshold")
    print("-" * 70)
    for c in CAT_COLS:
        kap = cohens_kappa(merged[f"{c}_c1"], merged[f"{c}_c2"])
        flag = "OK" if kap >= 0.70 else "BELOW"
        print(f"{c:<22}{'Cohen kappa (unweighted)':<28}{kap:>8.3f}   >=0.70 {flag}")

    c1, c2v = merged["cdai_c1"], merged["cdai_c2"]
    if set(c1) | set(c2v) <= set(ORDINAL_MAP):
        kap_u = cohens_kappa(c1, c2v)
        kap_w = cohens_kappa(
            c1.map(lambda v: "LMH"[ORDINAL_MAP[v]]), c2v.map(lambda v: "LMH"[ORDINAL_MAP[v]]),
            weights="linear",
        )
        print(f"{'cdai (H/M/L ordinal)':<22}{'Cohen kappa (unweighted)':<28}{kap_u:>8.3f}   >=0.70")
        print(f"{'cdai (H/M/L ordinal)':<22}{'Cohen kappa (linear wt)':<28}{kap_w:>8.3f}   >=0.70")
        print(
            "\nNOTE: database cdai is ordinal H/M/L, not continuous 0-1; the manuscript "
            "Table 3.1 row 'cDAI score / ICC(2,1)' should be reconciled by the authors "
            "(either supply continuous scores or relabel the row as weighted kappa)."
        )
    else:
        icc = icc_2_1(c1.astype(float), c2v.astype(float))
        print(f"{'cdai (continuous)':<22}{'ICC(2,1)':<28}{icc:>8.3f}   >=0.80")

    print("\nDisagreement rows (resolve by discussion, then record in notes):")
    for c in code_cols:
        d = merged[merged[f"{c}_c1"] != merged[f"{c}_c2"]]
        if len(d):
            print(f"  {c}: {', '.join(d.study_id.tolist())}")


if __name__ == "__main__":
    main()
