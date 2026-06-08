#!/usr/bin/env python3
"""
P9' India — Robustness checks for §4.6

4 specifications run on M2 (FSTS + FSTS² + controls) across all 3 waves:
(R1) Manufacturing-only sub-sample (ISIC 10-33)
(R2) Trimmed FSTS (drop FSTS > 0.95 — extreme exporters)
(R3) Size sub-sample — SMEs only (employees < 100) vs Large (>= 100)
(R4) Alternative DV — log(sales per worker) NORMALISED differently (raw labour productivity)

Outputs:
- p9_india_robustness.csv  (all 4 specs × 3 waves × M2 coefficients)
- console summary
"""

from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.api as sm

# Re-use functions from main pipeline
sys.path.insert(0, str(Path(__file__).parent))
from run_pipeline import build_wave, ols_hc1, ols_cluster, lind_mehlum, turning_point, paternoster_z

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data_wbes" / "raw_dta"
OUT_RES = ROOT / "p9_india" / "replication" / "results"

CONTROLS = ["lnEmp", "firmage", "foreigndummy"]


def get_isic2(path: Path) -> tuple[pd.Series, str]:
    """Extract ISIC 2-digit sector code from raw WBES file.

    Returns (isic2_series, manufacturing_range_label).
    - 2014 PICS3 uses a4a (ISIC Rev 3.1, 2-digit, mfg = 15-37)
    - 2022/2025 BREADY uses d1a2_v4 (ISIC Rev 4, 4-digit, mfg first-2-digit = 10-33)
    """
    df, _ = pyreadstat.read_dta(path)
    if "d1a2_v4" in df.columns:
        raw = pd.to_numeric(df["d1a2_v4"], errors="coerce")
        # 4-digit Rev 4 → take first 2 digits
        isic2 = np.floor(raw / 100.0)
        return isic2, "rev4_2digit"
    elif "a4a" in df.columns:
        raw = pd.to_numeric(df["a4a"], errors="coerce")
        # Already 2-digit Rev 3.1
        return np.floor(raw), "rev3_2digit"
    else:
        return pd.Series([np.nan] * len(df)), "missing"


def mfg_mask(isic2: pd.Series, rev_label: str) -> pd.Series:
    """Return boolean mask for manufacturing firms (ISIC harmonised)."""
    if rev_label == "rev3_2digit":
        # ISIC Rev 3.1 manufacturing = 15-37
        return (isic2 >= 15) & (isic2 <= 37)
    elif rev_label == "rev4_2digit":
        # ISIC Rev 4 manufacturing = 10-33
        return (isic2 >= 10) & (isic2 <= 33)
    return pd.Series([False] * len(isic2))


def run_spec(name: str, df: pd.DataFrame, wave: int) -> dict:
    """Estimate M2 on filtered df; return key statistics."""
    if df["sample_base"].sum() < 100:
        return {"spec": name, "wave": wave, "N": int(df["sample_base"].sum()),
                "status": "too_few_obs"}
    d = df[df["sample_base"]].copy()
    n_clusters = d["state"].nunique() if "state" in d.columns else np.nan

    M2 = ols_hc1(d["lnLP"], d[["FSTS", "FSTSsq"] + CONTROLS])
    ut = lind_mehlum(M2, "FSTS", "FSTSsq", d["FSTS"].min(), d["FSTS"].max())
    tp = turning_point(M2, "FSTS", "FSTSsq")

    M2c = ols_cluster(d["lnLP"], d[["FSTS", "FSTSsq"] + CONTROLS], d["state"]) if "state" in d.columns else M2

    return {
        "spec": name, "wave": wave, "N": int(M2.nobs), "clusters": n_clusters,
        "b_FSTS": M2.params["FSTS"], "se_FSTS_HC1": M2.bse["FSTS"], "p_FSTS_HC1": M2.pvalues["FSTS"],
        "se_FSTS_cluster": M2c.bse["FSTS"], "p_FSTS_cluster": M2c.pvalues["FSTS"],
        "b_FSTSsq": M2.params["FSTSsq"], "se_FSTSsq_HC1": M2.bse["FSTSsq"], "p_FSTSsq_HC1": M2.pvalues["FSTSsq"],
        "se_FSTSsq_cluster": M2c.bse["FSTSsq"], "p_FSTSsq_cluster": M2c.pvalues["FSTSsq"],
        "tp_pct": tp["tp"] * 100, "tp_ci_low_pct": tp["ci_low"] * 100, "tp_ci_high_pct": tp["ci_high"] * 100,
        "lm_inverted_U": ut["inverted_U_supported"], "lm_p_joint": ut["p_joint"],
        "r2_adj": M2.rsquared_adj,
    }


def main():
    waves = {
        2014: RAW / "India-2014-full-data.dta",
        2022: RAW / "India-2022-full-data.dta",
        2025: RAW / "India-2025-full-data.dta",
    }

    # Build analytic + attach ISIC2 + manufacturing mask for each wave
    dfs = {}
    isic_revs = {}
    for y, raw in waves.items():
        df = build_wave(raw, y)
        isic2, rev = get_isic2(raw)
        df["isic2"] = isic2.values
        df["is_mfg"] = mfg_mask(isic2, rev).values
        dfs[y] = df
        isic_revs[y] = rev
        n_mfg = df["is_mfg"].sum()
        print(f"  {y} ISIC {rev}: {n_mfg:,} manufacturing firms / {len(df):,} total")

    results = []

    print("=" * 80)
    print("  ROBUSTNESS CHECKS — 4 specifications × 3 waves")
    print("=" * 80)

    for y in (2014, 2022, 2025):
        df = dfs[y]
        print(f"\n--- Wave {y} ---")

        # BASELINE (full sample) for reference
        res = run_spec("baseline", df, y)
        results.append(res)
        print(f"  baseline       N={res['N']:>5}  β2={res['b_FSTSsq']:>+7.3f} (HC1 p={res['p_FSTSsq_HC1']:.4f})  TP={res['tp_pct']:>+7.1f}%  inverted-U={res['lm_inverted_U']}")

        # R1: Manufacturing only (ISIC harmonised: Rev 3.1 [15-37] or Rev 4 [10-33])
        df_mfg = df[df["is_mfg"]].copy()
        res = run_spec("R1_manufacturing_only", df_mfg, y)
        results.append(res)
        print(f"  R1 mfg-only    N={res['N']:>5}  β2={res['b_FSTSsq']:>+7.3f} (HC1 p={res['p_FSTSsq_HC1']:.4f})  TP={res['tp_pct']:>+7.1f}%  inverted-U={res['lm_inverted_U']}")

        # R2: Trimmed FSTS (drop FSTS > 0.95)
        df_trim = df[(df["FSTS"].isna()) | (df["FSTS"] <= 0.95)].copy()
        res = run_spec("R2_trimmed_FSTS_le095", df_trim, y)
        results.append(res)
        print(f"  R2 trim<=.95   N={res['N']:>5}  β2={res['b_FSTSsq']:>+7.3f} (HC1 p={res['p_FSTSsq_HC1']:.4f})  TP={res['tp_pct']:>+7.1f}%  inverted-U={res['lm_inverted_U']}")

        # R3a: SME only (employees < 100 → lnEmp < ln(100) = 4.605)
        df_sme = df[df["lnEmp"] < np.log(100)].copy()
        res = run_spec("R3a_SME_emp_lt100", df_sme, y)
        results.append(res)
        print(f"  R3a SME<100    N={res['N']:>5}  β2={res['b_FSTSsq']:>+7.3f} (HC1 p={res['p_FSTSsq_HC1']:.4f})  TP={res['tp_pct']:>+7.1f}%  inverted-U={res['lm_inverted_U']}")

        # R3b: Large only (employees >= 100)
        df_lg = df[df["lnEmp"] >= np.log(100)].copy()
        res = run_spec("R3b_Large_emp_ge100", df_lg, y)
        results.append(res)
        print(f"  R3b Large>=100 N={res['N']:>5}  β2={res['b_FSTSsq']:>+7.3f} (HC1 p={res['p_FSTSsq_HC1']:.4f})  TP={res['tp_pct']:>+7.1f}%  inverted-U={res['lm_inverted_U']}")

        # R4: Alternative DV — LP in levels (not log)
        df_r4 = df.copy()
        df_r4["lnLP_raw"] = np.exp(df_r4["lnLP"])  # back-transform to levels (= sales/worker)
        d = df_r4[df_r4["sample_base"]].copy()
        n_clusters = d["state"].nunique() if "state" in d.columns else np.nan
        # Standardise levels DV to avoid huge coefficient scale
        d["LP_std"] = (d["lnLP_raw"] - d["lnLP_raw"].mean()) / d["lnLP_raw"].std(ddof=1)
        M2_r4 = ols_hc1(d["LP_std"], d[["FSTS", "FSTSsq"] + CONTROLS])
        ut_r4 = lind_mehlum(M2_r4, "FSTS", "FSTSsq", d["FSTS"].min(), d["FSTS"].max())
        tp_r4 = turning_point(M2_r4, "FSTS", "FSTSsq")
        res = {
            "spec": "R4_DV_levels_std", "wave": y, "N": int(M2_r4.nobs), "clusters": n_clusters,
            "b_FSTS": M2_r4.params["FSTS"], "se_FSTS_HC1": M2_r4.bse["FSTS"], "p_FSTS_HC1": M2_r4.pvalues["FSTS"],
            "se_FSTS_cluster": np.nan, "p_FSTS_cluster": np.nan,
            "b_FSTSsq": M2_r4.params["FSTSsq"], "se_FSTSsq_HC1": M2_r4.bse["FSTSsq"], "p_FSTSsq_HC1": M2_r4.pvalues["FSTSsq"],
            "se_FSTSsq_cluster": np.nan, "p_FSTSsq_cluster": np.nan,
            "tp_pct": tp_r4["tp"] * 100, "tp_ci_low_pct": tp_r4["ci_low"] * 100, "tp_ci_high_pct": tp_r4["ci_high"] * 100,
            "lm_inverted_U": ut_r4["inverted_U_supported"], "lm_p_joint": ut_r4["p_joint"],
            "r2_adj": M2_r4.rsquared_adj,
        }
        results.append(res)
        print(f"  R4 LP-std-lvl  N={res['N']:>5}  β2={res['b_FSTSsq']:>+7.3f} (HC1 p={res['p_FSTSsq_HC1']:.4f})  TP={res['tp_pct']:>+7.1f}%  inverted-U={res['lm_inverted_U']}")

    df_out = pd.DataFrame(results)
    df_out.to_csv(OUT_RES / "p9_india_robustness.csv", index=False)
    print(f"\n  ✓ Robustness results → {OUT_RES / 'p9_india_robustness.csv'}")

    # Cross-wave Paternoster on Manufacturing-only sub-sample (R1)
    print("\n" + "=" * 80)
    print("  CROSS-WAVE PATERNOSTER on R1 (manufacturing-only) — 2014 vs 2025")
    print("=" * 80)
    r1_14 = next(r for r in results if r["spec"] == "R1_manufacturing_only" and r["wave"] == 2014)
    r1_25 = next(r for r in results if r["spec"] == "R1_manufacturing_only" and r["wave"] == 2025)
    z1, p1 = paternoster_z(r1_14["b_FSTS"], r1_14["se_FSTS_HC1"], r1_25["b_FSTS"], r1_25["se_FSTS_HC1"])
    z2, p2 = paternoster_z(r1_14["b_FSTSsq"], r1_14["se_FSTSsq_HC1"], r1_25["b_FSTSsq"], r1_25["se_FSTSsq_HC1"])
    print(f"  FSTS    (mfg-only, HC1): z = {z1:>+6.3f}, p = {p1:.4f}")
    print(f"  FSTSsq  (mfg-only, HC1): z = {z2:>+6.3f}, p = {p2:.4f}")


if __name__ == "__main__":
    main()
