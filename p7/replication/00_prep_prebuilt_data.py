#!/usr/bin/env python3
"""
Convert pooled_wbes_6waves.csv (Class-AI-Agent format) → P7-compatible format.

Column mapping:
  export_pct / 100   → fsts
  TCI_full (0-1)     → z-score → tci_z   [5-component: cert+tech+innov+process+rd]
  DAI_rich (0-1)     → z-score → dai_z   [3-component: web+epay+epay_supp]
  manager_exp (1-4)  → mgr_experience (ordinal)
  foreign_own        → foreign_own_pct
  country (3-char)   → mapped + icrv_group assigned

Usage:
  python3 00_prep_prebuilt_data.py [--input PATH] [--out PATH]
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

COUNTRY_MAP = {
    "VNM": "Vietnam",
    "CHN": "China",
    "SGP": "Singapore",
}

ICRV_MAP = {
    "Vietnam": 4,
    "China": 3,
    "Singapore": 1,
}

ICRV_LABEL = {
    1: "Advanced_innovation",
    3: "Upper_mid",
    4: "Lower_mid_transition",
}


def zscore(s: pd.Series) -> pd.Series:
    mu, sd = s.mean(), s.std()
    return (s - mu) / sd if sd > 0 else s - mu


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data_wbes/analysis/pooled_wbes_6waves.csv",
    )
    parser.add_argument(
        "--out",
        default="data_wbes/p7/p7_pooled_rich.csv",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.parent
    src = repo_root / args.input
    dst = repo_root / args.out
    dst.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(src)
    print(f"Loaded {src}: {df.shape[0]:,} rows, {df.shape[1]} cols")

    out = pd.DataFrame()

    # Country / metadata
    out["country"] = df["country"].map(COUNTRY_MAP).fillna(df["country"])
    out["year"] = df["year"]
    out["icrv_group"] = out["country"].map(ICRV_MAP)
    out["icrv_label"] = out["icrv_group"].map(ICRV_LABEL)
    out["cy_fe"] = out["country"] + "_" + out["year"].astype(str)

    # Outcome
    out["ln_labor_prod"] = df["ln_labor_prod"]
    out["ln_size"] = df["ln_empl"]

    # FSTS — export intensity (0–1)
    out["fsts"] = df["export_pct"] / 100
    out["exporter"] = df["exporter"]

    # TCI — standardize TCI_full (5 components)
    out["tci_full_raw"] = df["TCI_full"]
    out["tci_thin_raw"] = df["TCI_thin"]
    out["tci_z"] = zscore(df["TCI_full"])       # primary composite for models
    out["tci_thin_z"] = zscore(df["TCI_thin"])  # sensitivity

    # DAI — standardize DAI_rich (3 components)
    out["dai_rich_raw"] = df["DAI_rich"]
    out["dai_thin_raw"] = df["DAI_thin"]
    out["dai_z"] = zscore(df["DAI_rich"])       # primary composite
    out["dai_thin_z"] = zscore(df["DAI_thin"])  # sensitivity

    # Top manager
    out["mgr_experience"] = df["manager_exp"]   # ordinal 1-4
    out["mgr_female"] = np.nan                  # not in this file

    # Controls
    out["firm_age"] = df["firm_age"]
    out["foreign_own_pct"] = df["foreign_own"]
    out["female_owner"] = np.nan               # not in this file

    dst.write_text("")  # ensure parent exists
    out.to_csv(dst, index=False)
    print(f"Saved {dst}: {len(out):,} rows, {len(out.columns)} cols")

    # Summary
    print("\n=== COUNTRY-YEAR COVERAGE ===")
    print(out.groupby(["country", "year"]).size().to_string())
    print("\n=== VARIABLE STATS ===")
    print(out[["ln_labor_prod", "fsts", "tci_z", "dai_z", "mgr_experience"]].describe().round(3))


if __name__ == "__main__":
    main()
