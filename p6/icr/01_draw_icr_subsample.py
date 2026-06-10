#!/usr/bin/env python3
"""Draw the 20% stratified ICR subsample for P6 dual-coding (k = 47 studies).

Deterministic (seed = 2026). Stratified by ICRV regime so every regime is
represented proportionally, matching the protocol in manuscript section 3.3.2
("two authors independently code a 20% stratified subsample, k = 47 studies").

Outputs (in p6/icr/):
  icr_subsample_master.csv        -- coder-1 (PI) codes = current database values
  icr_coding_sheet_coder2_BLANK.csv -- same rows, code columns EMPTY for coder 2

Coder 2 must fill the blank sheet from the source papers WITHOUT seeing the
master sheet. Then run 02_compute_icr.py.
"""
import pandas as pd
import numpy as np
from pathlib import Path

SEED = 2026
K_TARGET = 47
ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "p6" / "data" / "p6_study_database.csv"
OUT = ROOT / "p6" / "icr"

CODE_COLS = ["icrv", "dpl", "doi_type", "fp_type", "cdai"]
ID_COLS = ["study_id", "author", "year", "country", "sample_start", "sample_end"]


def main():
    df = pd.read_csv(DB)
    df = df[df.include_flag == 1]
    # one row per study (codes are study-level; take the first effect's codes)
    studies = df.sort_values("effect_id").groupby("study_id", as_index=False).first()
    n_studies = len(studies)

    rng = np.random.default_rng(SEED)
    # proportional allocation by ICRV regime, largest-remainder rounding to hit K_TARGET
    counts = studies.icrv.value_counts()
    exact = counts / counts.sum() * K_TARGET
    alloc = exact.astype(int)
    remainder = (exact - alloc).sort_values(ascending=False)
    for regime in remainder.index[: K_TARGET - alloc.sum()]:
        alloc[regime] += 1
    assert alloc.sum() == K_TARGET, alloc

    picks = []
    for regime, k in alloc.items():
        pool = studies[studies.icrv == regime]
        picks.append(pool.sample(n=k, random_state=rng.integers(0, 2**31)))
    sample = pd.concat(picks).sort_values("study_id")
    sample["year"] = sample["year"].astype("Int64")

    master = sample[ID_COLS + CODE_COLS].copy()
    master.to_csv(OUT / "icr_subsample_master.csv", index=False)

    blank = sample[ID_COLS].copy()
    for c in CODE_COLS:
        blank[c] = ""
    blank.to_csv(OUT / "icr_coding_sheet_coder2_BLANK.csv", index=False)

    print(f"Total included studies: {n_studies}")
    print(f"Subsample drawn: k = {len(sample)} (target {K_TARGET}, seed {SEED})")
    print("Allocation by ICRV regime:")
    print(alloc.to_string())
    print(f"\nWrote: {OUT/'icr_subsample_master.csv'}")
    print(f"Wrote: {OUT/'icr_coding_sheet_coder2_BLANK.csv'}")


if __name__ == "__main__":
    main()
