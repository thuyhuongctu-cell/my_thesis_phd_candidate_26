#!/usr/bin/env python3
"""P7 re-estimation reproducibility check (honesty gate before adding Japan).

Attempts to reproduce P7's ICRV turning-point gradient from the master pool
(data_wbes/p7/p7_pooled_clean.csv) using a quadratic FSTS model with within
country-year z-standardised labour productivity and country+year fixed effects.

PURPOSE: verify whether the published P7 turning points can be reproduced from
the available master data BEFORE attempting a "P7 + Japan" re-estimation. If the
baseline does not reproduce, we must NOT fabricate updated coefficients — the
exact P7 pipeline (PPP adjustment / sampling weights / control set / spec) is
required and only the authors' do-files can produce defensible numbers.

RESULT (2026-06-11): the reproduced gradient does NOT match published P7
(published TP Advanced-Innovation approx 28% rising to Emerging/SIDS approx 55%;
this script yields Advanced approx 79-84%, gradient direction inverted). Hence
P7's pipeline is not reproducible here; no updated P7 econometrics are reported.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

MASTER = "data_wbes/p7/p7_pooled_clean.csv"
DROP = ["Philippines_panel", "Nepal_panel", "Mongolia_panel",
        "Comoros", "Cyprus", "Turkey"]
GROUPS = ["Advanced_innovation", "Advanced_resource", "Upper_mid",
          "Lower_mid_transition", "Emerging", "SIDS_small"]


def ols_turning_point(d: pd.DataFrame, label: str) -> None:
    cols = [np.ones(len(d)), d["fsts"].values, d["fsts2"].values,
            d["firm_age"].values]
    names = ["const", "fsts", "fsts2", "firm_age"]
    for fe in ("country", "year"):
        if d[fe].nunique() > 1:
            du = pd.get_dummies(d[fe], prefix=fe, drop_first=True).astype(float)
            for c in du.columns:
                cols.append(du[c].values); names.append(c)
    X = np.column_stack(cols).astype(float)
    beta, *_ = np.linalg.lstsq(X, d["lp_z"].values.astype(float), rcond=None)
    b = dict(zip(names, beta))
    b1, b2 = b["fsts"], b["fsts2"]
    tp = -b1 / (2 * b2) if b2 else float("nan")
    shape = "inverted-U" if b2 < 0 else "U"
    print(f"  {label:22} N={len(d):6} | b1={b1:+.5f} b2={b2:+.6f} "
          f"| TP={tp:6.1f}% {shape}")


def main() -> None:
    df = pd.read_csv(MASTER, low_memory=False)
    a = df[~df["country"].isin(DROP)].dropna(
        subset=["icrv_label", "ln_labor_prod", "fsts_pct"]).copy()
    # remove currency artefact: z-standardise LP within country-year
    a["lp_z"] = a.groupby(["country", "year"])["ln_labor_prod"].transform(
        lambda x: (x - x.mean()) / x.std(ddof=0) if x.std(ddof=0) > 0 else 0.0)
    a = a.replace([np.inf, -np.inf], np.nan).dropna(subset=["lp_z"])
    a["fsts"] = a["fsts_pct"].astype(float)
    a["fsts2"] = a["fsts"] ** 2
    a["firm_age"] = a["firm_age"].fillna(a["firm_age"].median())
    print(f"analytic N (49-frame, LP+FSTS): {len(a):,} | "
          f"countries: {a['country'].nunique()}")
    print("\nReproduced turning points by ICRV group:")
    for g in GROUPS:
        ols_turning_point(a[a["icrv_label"] == g], g)
    print("\nPooled:")
    ols_turning_point(a, "POOLED-49")
    print("\nPublished P7 (thesis Ch4 §4.6): pooled TP(M5)=40.0%; gradient "
          "Advanced≈28% -> Emerging/SIDS≈55%.")
    print("=> Reproduction MISMATCH -> P7 pipeline not reproducible here; "
          "do NOT fabricate 'P7 + Japan' econometrics.")


if __name__ == "__main__":
    main()
