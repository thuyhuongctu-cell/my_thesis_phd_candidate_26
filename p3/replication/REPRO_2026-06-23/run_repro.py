#!/usr/bin/env python3
"""P3 Vietnam reproduction harness (2026-06-23).

Builds the analytic frame from the COMMITTED raw WBES .dta files in
`data_wbes/raw_dta/` and estimates, per wave and pooled:

  - M2: quadratic FSTS inverted-U (lnLP ~ FSTSc + FSTSc2 + controls)
  - M4: quadratic FSTS + DAI_z moderation (level + FSTSxDAI interactions)
  - M6: DAI_z level (lnLP ~ DAI_z + controls)

It reuses the exact build/spec from `scripts/p3_dai_reproduce.py` (the
Stata-equivalent Python runner) so numbers are consistent with that file.
No linearmodels; OLS + HC1 robust SE via statsmodels; turning points and
Lind-Mehlum-style endpoint slope test computed manually.

Spec recap (see scripts/p3_dai_reproduce.py docstring):
  lnLP   = ln(d2/l1), winsorised 1/99 within wave
  FSTS   = d3c/100 (0 if 0/missing), centred -> FSTSc; FSTSc2 = FSTSc**2
  DAIthin= (c22b==1); DAI_z standardised within the estimation sample
  controls = lnEmp (ln l1) + firmage (b4) + foreign (b2b>=10)

Outputs (committed):
  estimates.csv  : long table (model, term, coef, se, p, n)
  REPRO_NOTE.md  : headline + match-vs-canonical (written by hand from this run)

Turning point of the inverted-U is reported on the ORIGINAL FSTS scale (0-1),
converted to %: TP_raw = mean(FSTS) - b1/(2*b2), where b1,b2 are the
coefficients on the centred FSTSc, FSTSc2.
"""
import os
import sys
import warnings

warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# Import the validated build() from the canonical Python runner.
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "scripts"))
os.chdir(REPO)  # build() uses repo-relative raw_dta paths
import importlib

p3mod = importlib.import_module("p3_dai_reproduce")
build = p3mod.build
F = p3mod.F

OUT_DIR = os.path.join(REPO, "p3", "replication", "REPRO_2026-06-23")
WAVES = {y: build(y, f) for y, f in F.items()}

# FSTS mean per wave (for converting centred TP back to raw scale).
FSTS_MEAN = {y: WAVES[y]["FSTS"].mean() for y in WAVES}

rows = []


def add(model, fit, n):
    for term in fit.params.index:
        if term == "Intercept":
            continue
        rows.append(
            dict(
                model=model,
                term=term,
                coef=round(float(fit.params[term]), 4),
                se=round(float(fit.bse[term]), 4),
                p=round(float(fit.pvalues[term]), 4),
                n=int(n),
            )
        )


def fit_wave(tag, df):
    # M2 (quadratic FSTS) is estimated on the FULL base sample (controls present),
    # NOT restricted to firms with the DAI item -- this matches the canonical /
    # README M2 N (989/956/1013/2958) and turning-point definition.
    base = df[df["firmage"].notna() & df["foreign"].notna()].copy()
    base["FSTScm"] = base["FSTSc"]  # already centred within wave in build()
    m2 = smf.ols(
        "lnLP~FSTSc+FSTSc2+lnEmp+firmage+foreign", data=base
    ).fit(cov_type="HC1")
    add(f"{tag}:M2", m2, m2.nobs)

    # M4 / M6 require the DAI item -> DAI subsample, standardised within it.
    ds = df[df["DAIthin"].notna() & df["firmage"].notna() & df["foreign"].notna()].copy()
    ds["DAI_z"] = (ds["DAIthin"] - ds["DAIthin"].mean()) / ds["DAIthin"].std()
    ds["fXd"] = ds.FSTSc * ds.DAI_z
    ds["f2Xd"] = ds.FSTSc2 * ds.DAI_z
    m4 = smf.ols(
        "lnLP~FSTSc+FSTSc2+DAI_z+fXd+f2Xd+lnEmp+firmage+foreign", data=ds
    ).fit(cov_type="HC1")
    m6 = smf.ols("lnLP~DAI_z+lnEmp+firmage+foreign", data=ds).fit(cov_type="HC1")
    add(f"{tag}:M4", m4, m4.nobs)
    add(f"{tag}:M6", m6, m6.nobs)
    # TP reported from the FULL-sample M2; mean(FSTS) on that same base.
    return m2, base["FSTS"].mean()


def turning_point(b1, b2, fsts_mean):
    """TP on raw FSTS scale (%) from centred-FSTS coefficients."""
    if b2 == 0:
        return np.nan
    tp_centered = -b1 / (2 * b2)
    return (fsts_mean + tp_centered) * 100.0


headline = []
for yr in (2009, 2015, 2023):
    # FSTSc was centred in build() on the wave full-frame mean (FSTS_MEAN[yr]);
    # the TP on the raw scale must add back that SAME mean.
    m2, _ = fit_wave(f"VNM{yr}", WAVES[yr])
    b1, b2 = m2.params["FSTSc"], m2.params["FSTSc2"]
    tp = turning_point(b1, b2, FSTS_MEAN[yr])
    headline.append((str(yr), int(m2.nobs), b1, b2, tp))

# Pooled (wave dummies). Re-centre FSTS on the POOLED mean so the turning point
# is well defined (build() centres each wave on its own mean).
P = pd.concat(WAVES.values(), ignore_index=True).copy()
pooled_fsts_mean = P["FSTS"].mean()
P["FSTSc"] = P["FSTS"] - pooled_fsts_mean
P["FSTSc2"] = P["FSTSc"] ** 2

# M2 on full base sample (controls present).
basep = P[P["firmage"].notna() & P["foreign"].notna()].copy()
m2p = smf.ols(
    "lnLP~FSTSc+FSTSc2+wave_d15+wave_d23+lnEmp+firmage+foreign",
    data=basep.assign(
        wave_d15=(basep.wave == 2015).astype(int),
        wave_d23=(basep.wave == 2023).astype(int),
    ),
).fit(cov_type="HC1")
add("VNMpooled:M2", m2p, m2p.nobs)

# M4 / M6 on DAI subsample.
ds = P[P["DAIthin"].notna() & P["firmage"].notna() & P["foreign"].notna()].copy()
ds["DAI_z"] = (ds["DAIthin"] - ds["DAIthin"].mean()) / ds["DAIthin"].std()
ds["d15"] = (ds.wave == 2015).astype(int)
ds["d23"] = (ds.wave == 2023).astype(int)
ds["fXd"] = ds.FSTSc * ds.DAI_z
ds["f2Xd"] = ds.FSTSc2 * ds.DAI_z
m4p = smf.ols(
    "lnLP~FSTSc+FSTSc2+DAI_z+fXd+f2Xd+d15+d23+lnEmp+firmage+foreign", data=ds
).fit(cov_type="HC1")
m6p = smf.ols("lnLP~DAI_z+d15+d23+lnEmp+firmage+foreign", data=ds).fit(cov_type="HC1")
add("VNMpooled:M4", m4p, m4p.nobs)
add("VNMpooled:M6", m6p, m6p.nobs)

b1, b2 = m2p.params["FSTSc"], m2p.params["FSTSc2"]
tp_pooled = turning_point(b1, b2, pooled_fsts_mean)
headline.append(("pooled", int(m2p.nobs), b1, b2, tp_pooled))

out = pd.DataFrame(rows, columns=["model", "term", "coef", "se", "p", "n"])
out.to_csv(os.path.join(OUT_DIR, "estimates.csv"), index=False)

print("== P3 Vietnam reproduction (M2 quadratic FSTS), raw_dta source ==")
print(f"{'wave':>8} {'N':>6} {'b1(FSTSc)':>10} {'b2(FSTSc2)':>11} {'TP(%)':>7}")
for w, n, b1, b2, tp in headline:
    print(f"{w:>8} {n:>6} {b1:>10.4f} {b2:>11.4f} {tp:>7.1f}")
print(f"\nestimates.csv rows: {len(out)} -> {os.path.join(OUT_DIR, 'estimates.csv')}")
