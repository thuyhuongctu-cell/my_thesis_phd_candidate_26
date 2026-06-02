#!/usr/bin/env python3
"""
P9' India — Python port of Stata pipeline (01_build_india.do + 02_run_models.do)

Builds analytic samples from WBES India 2014, 2022, 2025 and estimates:
- M0..M4 per wave (OLS with HC1 robust SE)
- Lind-Mehlum U-test for inverted-U
- Delta-method turning-point CI
- Paternoster cross-wave z-test (2014 vs 2025)
- 3-wave pooled robustness with trend

Outputs (all CSV):
- p9_india/replication/results/p9_india_descriptives.csv
- p9_india/replication/results/p9_india_coefs_main_models.csv
- p9_india/replication/results/p9_india_moderators.csv
- p9_india/replication/results/p9_india_turning_points.csv
- p9_india/replication/results/p9_india_paternoster.csv
- p9_india/replication/results/p9_india_3wave_pooled.csv
- p9_india/replication/results/p9_india_uTest.csv

Run: python3 p9_india/replication/run_pipeline.py
"""

from __future__ import annotations

import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.api as sm
from scipy import stats

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data_wbes" / "raw_dta"
OUT_DATA = ROOT / "p9_india" / "replication" / "data"
OUT_RES = ROOT / "p9_india" / "replication" / "results"
OUT_DATA.mkdir(parents=True, exist_ok=True)
OUT_RES.mkdir(parents=True, exist_ok=True)

CONTROLS = ["lnEmp", "firmage", "foreigndummy"]


# ============================================================
# WAVE BUILD
# ============================================================
def build_wave(path: Path, wave_year: int) -> pd.DataFrame:
    """Replicate Stata build_india_wave for one wave."""
    df, _ = pyreadstat.read_dta(path)
    cols = set(df.columns)

    # State cluster (Sampling Region a2) — for cluster-robust SE
    state = df["a2"] if "a2" in cols else pd.Series([np.nan] * len(df))

    # Sales: prefer d2 (PICS3/BEE); fallback to n3 (BREADY)
    sales = df["d2"] if "d2" in cols else df["n3"]
    workers = df["l1"]
    lnLP = np.log(sales / workers)
    lnLP = lnLP.where((sales > 0) & (workers > 0))

    # Export intensity: recode negative codes to NaN
    d3b = df["d3b"].where(df["d3b"] >= 0)
    d3c = df["d3c"].where(df["d3c"] >= 0)
    FSTS = (d3b + d3c) / 100.0
    FSTS = FSTS.where((FSTS >= 0) & (FSTS <= 1))
    FSTS = FSTS.where(~((d3b == 0) & (d3c == 0)) | True, 0.0)
    # Replace 0+0 with 0 (already 0 by arithmetic; keep explicit)
    FSTS = FSTS.fillna(((d3b == 0) & (d3c == 0)).map({True: 0.0, False: np.nan}))
    FSTSsq = FSTS ** 2

    # TCI: 4 binary items, require ≥3 non-missing
    def binitem(col):
        if col in cols:
            return (df[col] == 1).where(df[col].notna()).astype("Float64")
        return pd.Series([pd.NA] * len(df), dtype="Float64")

    tci_items = pd.DataFrame({
        "cert": binitem("b8"),
        "tech": binitem("e6"),
        "inno": binitem("h1"),
        "rd": binitem("h8"),
    })
    n_tci = tci_items.notna().sum(axis=1)
    TCI_raw = tci_items.mean(axis=1).where(n_tci >= 3)
    mu, sd = TCI_raw.mean(), TCI_raw.std(ddof=1)
    TCI_full = (TCI_raw - mu) / sd if sd > 0 else pd.Series(np.nan, index=df.index)

    # DAI Tier-1
    DAI_core = (df["c22b"] == 1).where(df["c22b"].notna()).astype("Float64") if "c22b" in cols else pd.Series([pd.NA] * len(df), dtype="Float64")

    # DAI Tier-2 (BREADY only)
    if "k33" in cols:
        k33 = df["k33"].where(df["k33"] >= 0)
        DAI_epay = k33 / 100.0
    else:
        DAI_epay = pd.Series([np.nan] * len(df))

    # Controls
    lnEmp = np.log(workers).where(workers > 0)
    firmage = (wave_year - df["b5"]).where(df["b5"].notna())
    # data-quality cap: drop encoded errors (firmage <= 0 or > 150)
    firmage = firmage.where((firmage > 0) & (firmage <= 150))
    foreigndummy = (df["b2b"] >= 10).where(df["b2b"].notna()).astype("Float64")

    out = pd.DataFrame({
        "wave": wave_year,
        "state": state,
        "lnLP": lnLP,
        "FSTS": FSTS,
        "FSTSsq": FSTSsq,
        "TCI_full": TCI_full,
        "DAI_core": DAI_core.astype("float64") if hasattr(DAI_core, "astype") else DAI_core,
        "DAI_epay": DAI_epay,
        "lnEmp": lnEmp,
        "firmage": firmage,
        "foreigndummy": foreigndummy.astype("float64"),
    })

    # Force all numeric columns to float64 (statsmodels chokes on nullable Float64)
    for c in ["lnLP", "FSTS", "FSTSsq", "TCI_full", "DAI_core", "DAI_epay",
              "lnEmp", "firmage", "foreigndummy"]:
        out[c] = pd.to_numeric(out[c], errors="coerce").astype("float64")

    out["sample_base"] = out[["lnLP", "FSTS", "lnEmp", "firmage", "foreigndummy"]].notna().all(axis=1)
    out["sample_full"] = out["sample_base"] & out[["TCI_full", "DAI_core"]].notna().all(axis=1)

    return out


# ============================================================
# ESTIMATION HELPERS
# ============================================================
def ols_hc1(y: pd.Series, X: pd.DataFrame) -> sm.regression.linear_model.RegressionResultsWrapper:
    X_const = sm.add_constant(X, has_constant="add")
    return sm.OLS(y, X_const, missing="drop").fit(cov_type="HC1")


def ols_cluster(y: pd.Series, X: pd.DataFrame, groups: pd.Series) -> sm.regression.linear_model.RegressionResultsWrapper:
    """OLS with cluster-robust SE on `groups` (e.g., state)."""
    X_const = sm.add_constant(X, has_constant="add")
    common = X_const.index.intersection(y.index).intersection(groups.index)
    common = common[y.loc[common].notna() & X_const.loc[common].notna().all(axis=1) & groups.loc[common].notna()]
    return sm.OLS(y.loc[common], X_const.loc[common]).fit(
        cov_type="cluster", cov_kwds={"groups": groups.loc[common].astype(int)}
    )


def lind_mehlum(res, x_name: str, x2_name: str, x_min: float, x_max: float) -> dict:
    """Lind & Mehlum (2010) U-test for inverted-U."""
    b1 = res.params[x_name]
    b2 = res.params[x2_name]
    cov = res.cov_params()
    var_b1 = cov.loc[x_name, x_name]
    var_b2 = cov.loc[x2_name, x2_name]
    cov_b1b2 = cov.loc[x_name, x2_name]

    slope_low = b1 + 2 * b2 * x_min
    slope_high = b1 + 2 * b2 * x_max

    var_low = var_b1 + 4 * x_min ** 2 * var_b2 + 4 * x_min * cov_b1b2
    var_high = var_b1 + 4 * x_max ** 2 * var_b2 + 4 * x_max * cov_b1b2

    t_low = slope_low / np.sqrt(var_low) if var_low > 0 else np.nan
    t_high = slope_high / np.sqrt(var_high) if var_high > 0 else np.nan

    p_low = 1 - stats.norm.cdf(t_low)
    p_high = stats.norm.cdf(t_high)

    inv_u = (b2 < 0) and (slope_low > 0) and (slope_high < 0)
    p_joint = max(p_low, p_high)

    return {
        "b1": b1, "b2": b2,
        "slope_at_min": slope_low, "slope_at_max": slope_high,
        "t_low": t_low, "t_high": t_high,
        "p_low": p_low, "p_high": p_high,
        "p_joint": p_joint,
        "inverted_U_supported": bool(inv_u and p_joint < 0.05),
    }


def turning_point(res, x_name: str, x2_name: str) -> dict:
    """Delta-method turning point + 95% CI."""
    b1 = res.params[x_name]
    b2 = res.params[x2_name]
    cov = res.cov_params()
    var_b1 = cov.loc[x_name, x_name]
    var_b2 = cov.loc[x2_name, x2_name]
    cov_b1b2 = cov.loc[x_name, x2_name]

    tp = -b1 / (2 * b2) if b2 != 0 else np.nan
    # ∂tp/∂b1 = -1/(2*b2); ∂tp/∂b2 = b1/(2*b2^2)
    dtp_db1 = -1.0 / (2.0 * b2)
    dtp_db2 = b1 / (2.0 * b2 ** 2)
    var_tp = (dtp_db1 ** 2) * var_b1 + (dtp_db2 ** 2) * var_b2 + 2 * dtp_db1 * dtp_db2 * cov_b1b2
    se_tp = np.sqrt(var_tp) if var_tp > 0 else np.nan
    return {
        "tp": tp, "se": se_tp,
        "ci_low": tp - 1.96 * se_tp,
        "ci_high": tp + 1.96 * se_tp,
    }


def paternoster_z(b1, se1, b2, se2) -> tuple[float, float]:
    z = (b2 - b1) / np.sqrt(se1 ** 2 + se2 ** 2)
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p


def coef_row(res, name: str, label: str) -> dict:
    """Extract (coef, se, t, p, ci_low, ci_high) for one term."""
    if name not in res.params.index:
        return None
    b = res.params[name]
    se = res.bse[name]
    t = res.tvalues[name]
    p = res.pvalues[name]
    ci = res.conf_int().loc[name]
    return {"term": label, "coef": b, "se": se, "t": t, "p": p,
            "ci_low": ci[0], "ci_high": ci[1]}


# ============================================================
# MAIN PIPELINE
# ============================================================
def run_wave(wave_year: int, raw_file: Path) -> tuple[pd.DataFrame, dict]:
    """Build + estimate one wave; return (analytic_df, results_dict)."""
    print(f"\n{'=' * 70}\n  INDIA {wave_year} WAVE\n{'=' * 70}")
    df = build_wave(raw_file, wave_year)
    df_base = df[df["sample_base"]].copy()
    df_full = df[df["sample_full"]].copy()

    print(f"  N raw:           {len(df):>6,}")
    print(f"  N sample_base:   {len(df_base):>6,}")
    print(f"  N sample_full:   {len(df_full):>6,}")

    # M0..M2 (sample_base)
    M0 = ols_hc1(df_base["lnLP"], df_base[CONTROLS])
    M1 = ols_hc1(df_base["lnLP"], df_base[["FSTS"] + CONTROLS])
    M2 = ols_hc1(df_base["lnLP"], df_base[["FSTS", "FSTSsq"] + CONTROLS])

    # M2 with state-cluster SE (Cameron-Gelbach-Miller 2008 robust to within-state correlation)
    M2_cluster = ols_cluster(df_base["lnLP"], df_base[["FSTS", "FSTSsq"] + CONTROLS], df_base["state"])
    n_clusters = df_base["state"].nunique()

    # Lind-Mehlum U-test
    ut = lind_mehlum(M2, "FSTS", "FSTSsq", df_base["FSTS"].min(), df_base["FSTS"].max())
    tp = turning_point(M2, "FSTS", "FSTSsq")

    print(f"\n  M2 main: lnLP = α + β1·FSTS + β2·FSTS² + controls")
    print(f"    β1 (FSTS)   = {M2.params['FSTS']:>+8.4f} (SE_HC1 {M2.bse['FSTS']:.4f}, p={M2.pvalues['FSTS']:.4f}) | SE_cluster = {M2_cluster.bse['FSTS']:.4f} (p={M2_cluster.pvalues['FSTS']:.4f})")
    print(f"    β2 (FSTSsq) = {M2.params['FSTSsq']:>+8.4f} (SE_HC1 {M2.bse['FSTSsq']:.4f}, p={M2.pvalues['FSTSsq']:.4f}) | SE_cluster = {M2_cluster.bse['FSTSsq']:.4f} (p={M2_cluster.pvalues['FSTSsq']:.4f})")
    print(f"    R²(adj)     = {M2.rsquared_adj:.4f}    N = {int(M2.nobs):,}    Clusters = {n_clusters}")
    print(f"\n  Lind-Mehlum U-test (FSTS range [{df_base['FSTS'].min():.2f}, {df_base['FSTS'].max():.2f}]):")
    print(f"    Slope at FSTS_min = {ut['slope_at_min']:>+8.4f}  (p={ut['p_low']:.4f})")
    print(f"    Slope at FSTS_max = {ut['slope_at_max']:>+8.4f}  (p={ut['p_high']:.4f})")
    print(f"    Inverted-U supported: {ut['inverted_U_supported']}  (joint p={ut['p_joint']:.4f})")

    print(f"\n  Turning point (delta method):")
    if not np.isnan(tp["tp"]):
        print(f"    TP = {tp['tp']*100:>+6.2f}%   95% CI [{tp['ci_low']*100:+6.2f}%, {tp['ci_high']*100:+6.2f}%]")
    else:
        print(f"    TP undefined (β2 = 0 or not estimable)")

    # M3: TCI moderation (sample_full)
    M3 = None
    if len(df_full) > 50:
        Xm3 = df_full[["FSTS", "FSTSsq", "TCI_full"] + CONTROLS].copy()
        Xm3["FSTS_x_TCI"] = df_full["FSTS"] * df_full["TCI_full"]
        Xm3["FSTSsq_x_TCI"] = df_full["FSTSsq"] * df_full["TCI_full"]
        M3 = ols_hc1(df_full["lnLP"], Xm3)

    # M4: DAI Tier-1 moderation (sample_full)
    M4 = None
    if len(df_full) > 50:
        Xm4 = df_full[["FSTS", "FSTSsq", "DAI_core"] + CONTROLS].copy()
        Xm4["FSTS_x_DAI"] = df_full["FSTS"] * df_full["DAI_core"]
        Xm4["FSTSsq_x_DAI"] = df_full["FSTSsq"] * df_full["DAI_core"]
        M4 = ols_hc1(df_full["lnLP"], Xm4)

    # M4b: DAI Tier-2 (e-payment, 2025-only)
    M4b = None
    if df_full["DAI_epay"].notna().sum() > 50:
        df_t2 = df_full[df_full["DAI_epay"].notna()].copy()
        Xm4b = df_t2[["FSTS", "FSTSsq", "DAI_epay"] + CONTROLS].copy()
        Xm4b["FSTS_x_DAIepay"] = df_t2["FSTS"] * df_t2["DAI_epay"]
        Xm4b["FSTSsq_x_DAIepay"] = df_t2["FSTSsq"] * df_t2["DAI_epay"]
        M4b = ols_hc1(df_t2["lnLP"], Xm4b)
        print(f"\n  M4b DAI Tier-2 (UPI e-payment) — N = {int(M4b.nobs):,}")
        print(f"    FSTS×DAI_epay   = {M4b.params['FSTS_x_DAIepay']:>+8.4f} (p={M4b.pvalues['FSTS_x_DAIepay']:.4f})")
        print(f"    FSTSsq×DAI_epay = {M4b.params['FSTSsq_x_DAIepay']:>+8.4f} (p={M4b.pvalues['FSTSsq_x_DAIepay']:.4f})")

    return df, {
        "M0": M0, "M1": M1, "M2": M2, "M2_cluster": M2_cluster,
        "M3": M3, "M4": M4, "M4b": M4b,
        "utest": ut, "tp": tp, "n_base": len(df_base), "n_full": len(df_full),
        "n_clusters": n_clusters,
    }


def main():
    print("=" * 70)
    print("  P9' INDIA — 3-wave WBES analysis pipeline (Python port)")
    print("=" * 70)

    waves = {
        2014: RAW / "India-2014-full-data.dta",
        2022: RAW / "India-2022-full-data.dta",
        2025: RAW / "India-2025-full-data.dta",
    }
    dfs = {}
    res = {}
    for y, p in waves.items():
        df, r = run_wave(y, p)
        dfs[y] = df
        res[y] = r
        df.to_csv(OUT_DATA / f"india_{y}_analytic.csv", index=False)

    # ----------------- Pooled 3-wave -----------------
    pooled = pd.concat([
        dfs[2014].assign(wave_2022=0, wave_2025=0),
        dfs[2022].assign(wave_2022=1, wave_2025=0),
        dfs[2025].assign(wave_2022=0, wave_2025=1),
    ], ignore_index=True)
    pooled["trend"] = pooled["wave"] - 2014
    pooled["trend2"] = pooled["trend"] ** 2
    pooled.to_csv(OUT_DATA / "india_pooled_analytic.csv", index=False)

    # ----------------- 2-wave pooled (2014 vs 2025) Paternoster z -----------------
    print(f"\n{'=' * 70}\n  CROSS-WAVE COMPARISON (2014 vs 2025, primary 11-year window)\n{'=' * 70}")
    z_FSTS, p_FSTS = paternoster_z(
        res[2014]["M2"].params["FSTS"], res[2014]["M2"].bse["FSTS"],
        res[2025]["M2"].params["FSTS"], res[2025]["M2"].bse["FSTS"],
    )
    z_FSTS2, p_FSTS2 = paternoster_z(
        res[2014]["M2"].params["FSTSsq"], res[2014]["M2"].bse["FSTSsq"],
        res[2025]["M2"].params["FSTSsq"], res[2025]["M2"].bse["FSTSsq"],
    )
    print(f"  Paternoster z (FSTS    2014→2025): z = {z_FSTS:>+6.3f}, p = {p_FSTS:.4f}")
    print(f"  Paternoster z (FSTSsq  2014→2025): z = {z_FSTS2:>+6.3f}, p = {p_FSTS2:.4f}")

    if p_FSTS > 0.05 and p_FSTS2 > 0.05:
        print(f"  → H2b (durability) SUPPORTED: cannot reject coefficient equality across waves")
    else:
        print(f"  → H2a (shift) SUPPORTED on at least one coefficient")

    # 3-wave pooled with trend
    p_base = pooled[pooled["sample_base"]].copy()
    Xtrend = p_base[["FSTS", "FSTSsq", "trend"] + CONTROLS].copy()
    Xtrend["FSTS_x_trend"] = p_base["FSTS"] * p_base["trend"]
    Xtrend["FSTSsq_x_trend"] = p_base["FSTSsq"] * p_base["trend"]
    M_trend = ols_hc1(p_base["lnLP"], Xtrend)

    Xdummy = p_base[["FSTS", "FSTSsq", "wave_2022", "wave_2025"] + CONTROLS].copy()
    Xdummy["FSTS_x_2022"] = p_base["FSTS"] * p_base["wave_2022"]
    Xdummy["FSTS_x_2025"] = p_base["FSTS"] * p_base["wave_2025"]
    Xdummy["FSTSsq_x_2022"] = p_base["FSTSsq"] * p_base["wave_2022"]
    Xdummy["FSTSsq_x_2025"] = p_base["FSTSsq"] * p_base["wave_2025"]
    M_dummy = ols_hc1(p_base["lnLP"], Xdummy)

    print(f"\n  3-wave pooled with wave dummies (N = {int(M_dummy.nobs):,}):")
    for term in ["FSTS_x_2022", "FSTS_x_2025", "FSTSsq_x_2022", "FSTSsq_x_2025"]:
        b, p = M_dummy.params[term], M_dummy.pvalues[term]
        print(f"    {term:<20} = {b:>+8.4f}  (p={p:.4f})")

    # ----------------- WRITE RESULTS -----------------
    # Turning points
    tp_rows = []
    for y in (2014, 2022, 2025):
        t = res[y]["tp"]
        tp_rows.append({"wave": y, "tp_pct": t["tp"] * 100, "se_pct": t["se"] * 100,
                        "ci_low_pct": t["ci_low"] * 100, "ci_high_pct": t["ci_high"] * 100})
    pd.DataFrame(tp_rows).to_csv(OUT_RES / "p9_india_turning_points.csv", index=False)

    # Paternoster — HC1 SE
    pd.DataFrame([
        {"term": "FSTS",   "b_2014": res[2014]["M2"].params["FSTS"],   "se_2014": res[2014]["M2"].bse["FSTS"],
         "b_2025": res[2025]["M2"].params["FSTS"],   "se_2025": res[2025]["M2"].bse["FSTS"],   "z_pat": z_FSTS,  "p_pat": p_FSTS},
        {"term": "FSTSsq", "b_2014": res[2014]["M2"].params["FSTSsq"], "se_2014": res[2014]["M2"].bse["FSTSsq"],
         "b_2025": res[2025]["M2"].params["FSTSsq"], "se_2025": res[2025]["M2"].bse["FSTSsq"], "z_pat": z_FSTS2, "p_pat": p_FSTS2},
    ]).to_csv(OUT_RES / "p9_india_paternoster.csv", index=False)

    # Paternoster — cluster-robust SE (Cameron-Gelbach-Miller 2008)
    z_FSTS_cl, p_FSTS_cl = paternoster_z(
        res[2014]["M2_cluster"].params["FSTS"], res[2014]["M2_cluster"].bse["FSTS"],
        res[2025]["M2_cluster"].params["FSTS"], res[2025]["M2_cluster"].bse["FSTS"],
    )
    z_FSTS2_cl, p_FSTS2_cl = paternoster_z(
        res[2014]["M2_cluster"].params["FSTSsq"], res[2014]["M2_cluster"].bse["FSTSsq"],
        res[2025]["M2_cluster"].params["FSTSsq"], res[2025]["M2_cluster"].bse["FSTSsq"],
    )
    pd.DataFrame([
        {"term": "FSTS",   "b_2014": res[2014]["M2_cluster"].params["FSTS"],   "se_2014": res[2014]["M2_cluster"].bse["FSTS"],
         "b_2025": res[2025]["M2_cluster"].params["FSTS"],   "se_2025": res[2025]["M2_cluster"].bse["FSTS"],   "z_pat": z_FSTS_cl,  "p_pat": p_FSTS_cl,
         "n_clusters_2014": res[2014]["n_clusters"], "n_clusters_2025": res[2025]["n_clusters"]},
        {"term": "FSTSsq", "b_2014": res[2014]["M2_cluster"].params["FSTSsq"], "se_2014": res[2014]["M2_cluster"].bse["FSTSsq"],
         "b_2025": res[2025]["M2_cluster"].params["FSTSsq"], "se_2025": res[2025]["M2_cluster"].bse["FSTSsq"], "z_pat": z_FSTS2_cl, "p_pat": p_FSTS2_cl,
         "n_clusters_2014": res[2014]["n_clusters"], "n_clusters_2025": res[2025]["n_clusters"]},
    ]).to_csv(OUT_RES / "p9_india_paternoster_cluster.csv", index=False)

    print(f"\n  Paternoster z (CLUSTER-ROBUST, state-level, ~24 clusters):")
    print(f"    FSTS    z_cluster = {z_FSTS_cl:>+6.3f}, p = {p_FSTS_cl:.4f}")
    print(f"    FSTSsq  z_cluster = {z_FSTS2_cl:>+6.3f}, p = {p_FSTS2_cl:.4f}")

    # U-test
    pd.DataFrame([
        {"wave": y, **res[y]["utest"]} for y in (2014, 2022, 2025)
    ]).to_csv(OUT_RES / "p9_india_uTest.csv", index=False)

    # Main M2 coefficients across waves
    main_rows = []
    for y in (2014, 2022, 2025):
        m = res[y]["M2"]
        for term in ["FSTS", "FSTSsq"] + CONTROLS + ["const"]:
            if term in m.params.index:
                main_rows.append({
                    "wave": y, "model": "M2", "term": term,
                    "coef": m.params[term], "se": m.bse[term],
                    "p": m.pvalues[term], "n": int(m.nobs),
                    "r2_adj": m.rsquared_adj,
                })
    pd.DataFrame(main_rows).to_csv(OUT_RES / "p9_india_coefs_main_models.csv", index=False)

    # Moderators (M3 TCI, M4 DAI Tier-1, M4b DAI Tier-2)
    mod_rows = []
    for y in (2014, 2022, 2025):
        for label, m in [("M3_TCI", res[y].get("M3")), ("M4_DAI_tier1", res[y].get("M4")), ("M4b_DAI_tier2", res[y].get("M4b"))]:
            if m is None:
                continue
            for term in m.params.index:
                if term == "const":
                    continue
                mod_rows.append({
                    "wave": y, "model": label, "term": term,
                    "coef": m.params[term], "se": m.bse[term],
                    "p": m.pvalues[term], "n": int(m.nobs),
                    "r2_adj": m.rsquared_adj,
                })
    pd.DataFrame(mod_rows).to_csv(OUT_RES / "p9_india_moderators.csv", index=False)

    # 3-wave pooled
    pool_rows = []
    for label, m in [("trend", M_trend), ("dummy", M_dummy)]:
        for term in m.params.index:
            pool_rows.append({
                "model": label, "term": term,
                "coef": m.params[term], "se": m.bse[term],
                "p": m.pvalues[term], "n": int(m.nobs),
                "r2_adj": m.rsquared_adj,
            })
    pd.DataFrame(pool_rows).to_csv(OUT_RES / "p9_india_3wave_pooled.csv", index=False)

    # Descriptives
    desc_rows = []
    for y in (2014, 2022, 2025):
        d = dfs[y][dfs[y]["sample_base"]]
        for v in ["lnLP", "FSTS", "FSTSsq", "TCI_full", "DAI_core", "DAI_epay", "lnEmp", "firmage", "foreigndummy"]:
            s = d[v].dropna()
            desc_rows.append({
                "wave": y, "var": v, "n": len(s),
                "mean": s.mean(), "sd": s.std(ddof=1),
                "min": s.min(), "max": s.max(),
            })
    pd.DataFrame(desc_rows).to_csv(OUT_RES / "p9_india_descriptives.csv", index=False)

    print(f"\n{'=' * 70}\n  ✓ All result CSVs written to {OUT_RES.relative_to(ROOT)}/\n{'=' * 70}")


if __name__ == "__main__":
    main()
