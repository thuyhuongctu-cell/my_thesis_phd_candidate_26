#!/usr/bin/env python3
"""
P7 Model Runner — OLS H1–H5 + 3-way interaction (H7-P7).

Reads p7_pooled_clean.csv, runs hierarchical OLS models with HC1 robust SEs,
Lind-Mehlum tests, and exports results tables + coefficients CSV.

Usage:
  python3 02_run_p7_models.py [--data PATH] [--out-dir PATH] [--min-n INT]
"""
import argparse
import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------------
# Lind–Mehlum (2010) concavity test
# ---------------------------------------------------------------------------
def lind_mehlum_test(model, x_name: str, x2_name: str) -> dict:
    """
    Test for inverted-U using Lind–Mehlum (2010) joint significance test.
    H0: not an inverted-U (i.e., either monotone or U-shaped).
    Returns dict with turning point (TP), p-value, and interpretation.
    """
    try:
        b1 = model.params[x_name]
        b2 = model.params[x2_name]
        if b2 >= 0:
            return {"tp": np.nan, "b1": b1, "b2": b2,
                    "lm_p": 1.0, "shape": "U or linear (b2>=0)"}
        tp = -b1 / (2 * b2)
        # Fieller-method CI for TP via delta method
        cov = model.cov_params()
        var_b1 = cov.loc[x_name, x_name]
        var_b2 = cov.loc[x2_name, x2_name]
        cov_b1b2 = cov.loc[x_name, x2_name]
        var_tp = (var_b1 / (2 * b2) ** 2 +
                  b1 ** 2 * var_b2 / (2 * b2) ** 4 -
                  b1 * cov_b1b2 / (2 * b2) ** 3)
        se_tp = np.sqrt(var_tp) if var_tp > 0 else np.nan

        # Joint test: slope at left > 0 AND slope at right < 0
        # Simplified: use t-test on b2 < 0 (necessary condition)
        t_b2 = b2 / model.bse[x2_name]
        p_b2_neg = stats.t.cdf(t_b2, df=model.df_resid)  # one-sided p(b2<0)
        t_b1 = b1 / model.bse[x_name]
        p_b1_pos = 1 - stats.t.cdf(-t_b1, df=model.df_resid)  # one-sided p(b1>0)
        lm_p = max(p_b2_neg, 1 - p_b1_pos)  # conservative joint p

        return {
            "tp": round(tp * 100, 1) if 0 < tp < 1 else round(tp, 3),
            "tp_raw": tp,
            "tp_se": round(se_tp * 100, 2) if se_tp else np.nan,
            "b1": round(b1, 4), "b2": round(b2, 4),
            "lm_p": round(lm_p, 4),
            "shape": "inverted-U" if (b2 < 0 and lm_p < 0.10) else "not confirmed",
        }
    except Exception as e:
        return {"tp": np.nan, "lm_p": np.nan, "shape": f"error: {e}"}


def run_ols_hc1(formula: str, data: pd.DataFrame) -> sm.regression.linear_model.RegressionResultsWrapper:
    try:
        model = smf.ols(formula, data=data).fit(cov_type="HC1")
        return model
    except Exception as e:
        raise RuntimeError(f"OLS failed on formula: {formula}\nError: {e}")


def format_results(models: dict, lm_tests: dict = None) -> pd.DataFrame:
    """Assemble coefficient table across models."""
    rows = []
    for mname, res in models.items():
        for param in res.params.index:
            rows.append({
                "model": mname, "term": param,
                "b": round(res.params[param], 4),
                "se": round(res.bse[param], 4),
                "t": round(res.tvalues[param], 3),
                "p": round(res.pvalues[param], 4),
                "sig": ("***" if res.pvalues[param] < 0.001 else
                        "**" if res.pvalues[param] < 0.01 else
                        "*" if res.pvalues[param] < 0.05 else
                        "†" if res.pvalues[param] < 0.10 else ""),
                "n": int(res.nobs),
                "r2": round(res.rsquared, 4),
                "adj_r2": round(res.rsquared_adj, 4),
            })
    df = pd.DataFrame(rows)
    if lm_tests:
        lm_df = pd.DataFrame([{"model": k, **v} for k, v in lm_tests.items()])
        df = df.merge(lm_df, on="model", how="left")
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data_wbes/p7/p7_pooled_clean.csv")
    parser.add_argument("--out-dir", default="p7/replication/results")
    parser.add_argument("--min-n", type=int, default=50,
                        help="Min obs per country-year to include")
    parser.add_argument("--subsample", default=None,
                        help="Filter: e.g. 'region==\"Southeast Asia\"'")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.parent
    data_path = repo_root / args.data
    out_dir = repo_root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading {data_path}")
    df = pd.read_csv(data_path)
    print(f"  Raw rows: {len(df):,}")

    # Scope: Asia-Pacific defined by the World Bank's operational regions —
    # East Asia & Pacific (EAP) + South Asia (SAR) + the West-Asian part of
    # Middle East, North Africa, Afghanistan & Pakistan (MENAAP). Economies the
    # World Bank files under Europe & Central Asia (ECA) or Sub-Saharan Africa
    # (AFR) are outside this frame and dropped, even where they appear in the
    # harmonised WBES pool. ECA: Turkey, Azerbaijan, Armenia, Georgia, Cyprus,
    # Kazakhstan, Kyrgyz Rep., Tajikistan, Turkmenistan, Uzbekistan. AFR: Comoros.
    out_of_scope = {
        "Turkey", "Azerbaijan", "Armenia", "Georgia", "Cyprus",
        "Kazakhstan", "KyrgyzRepublic", "Tajikistan", "Turkmenistan", "Uzbekistan",
        "Comoros",
    }
    n_before = len(df)
    df = df[~df["country"].isin(out_of_scope)].copy()
    print(f"  Dropped out-of-scope economies {sorted(out_of_scope)}: "
          f"-{n_before - len(df):,} rows -> {len(df):,} rows")
    print(f"  Countries: {df['country'].nunique()}")
    print(f"  Country-years: {df.groupby(['country','year']).ngroups}")

    # Optional subsample filter
    if args.subsample:
        df = df.query(args.subsample)
        print(f"  After filter '{args.subsample}': {len(df):,} rows")

    # ---------- Data preparation ----------
    # Drop country-years with fewer than min-n complete observations
    cy_n = df.groupby(["country", "year"])[
        ["ln_labor_prod", "fsts", "tci_z", "dai_z"]
    ].apply(lambda x: x.dropna().shape[0])
    valid_cy = cy_n[cy_n >= args.min_n].reset_index()[["country", "year"]]
    df = df.merge(valid_cy, on=["country", "year"])
    print(f"  After min-N={args.min_n} filter: {len(df):,} rows, "
          f"{df['country'].nunique()} countries")

    # Create analytical variables
    df = df.copy()
    df["fsts_c"] = df["fsts"] - df.groupby(["country", "year"])["fsts"].transform("mean")
    df["fsts_c2"] = df["fsts_c"] ** 2
    df["fsts_raw"] = df["fsts"]
    df["fsts_c_x_tci"] = df["fsts_c"] * df["tci_z"]
    df["fsts_c2_x_tci"] = df["fsts_c2"] * df["tci_z"]
    df["fsts_c_x_dai"] = df["fsts_c"] * df["dai_z"]
    df["fsts_c2_x_dai"] = df["fsts_c2"] * df["dai_z"]
    df["fsts_c_x_mgr"] = df["fsts_c"] * df["mgr_experience"]
    df["fsts_c_x_female"] = df["fsts_c"] * df["mgr_female"]

    # ICRV regime dummies (Group 3=reference=Upper_mid)
    df["icrv_g1"] = (df["icrv_group"] == 1).astype(float)
    df["icrv_g2"] = (df["icrv_group"] == 2).astype(float)
    df["icrv_g4"] = (df["icrv_group"] == 4).astype(float)
    df["icrv_g5"] = (df["icrv_group"] == 5).astype(float)
    df["icrv_g6"] = (df["icrv_group"] == 6).astype(float)
    df["fsts_c_x_icrv"] = df["fsts_c"] * df["icrv_group"]
    df["fsts_c2_x_icrv"] = df["fsts_c2"] * df["icrv_group"]

    # 3-way interaction: DAI × ICRV × mgr_experience
    df["dai_x_icrv"] = df["dai_z"] * df["icrv_group"]
    df["fsts_c_x_dai_x_icrv"] = df["fsts_c"] * df["dai_z"] * df["icrv_group"]
    df["fsts_c_x_dai_x_mgr"] = df["fsts_c"] * df["dai_z"] * df["mgr_experience"]

    # Country-year FE string for R-style formula
    df["cy_fe"] = df["country"].astype(str) + "_" + df["year"].astype(str)

    # Analytical sample: require all focal variables
    focal_vars = ["ln_labor_prod", "fsts_c", "fsts_c2", "tci_z", "dai_z",
                  "mgr_experience", "mgr_female", "female_owner", "firm_age",
                  "ln_size", "foreign_own_pct"]
    analytic = df.dropna(subset=["ln_labor_prod", "fsts_c"]).copy()
    print(f"\n  Analytic sample (y+fsts complete): {len(analytic):,}")
    print(f"  With TCI: {analytic['tci_z'].notna().sum():,}")
    print(f"  With DAI: {analytic['dai_z'].notna().sum():,}")
    print(f"  With mgr_exp: {analytic['mgr_experience'].notna().sum():,}")

    # Full sample with all focal vars
    full_analytic = analytic.dropna(
        subset=["tci_z", "dai_z", "mgr_experience", "mgr_female"]
    )
    print(f"  Full analytic (all focal): {len(full_analytic):,}")

    # Build controls dynamically from columns that are actually present + have data
    optional_controls = ["female_owner", "foreign_own_pct", "firm_age", "ln_size"]
    available_controls = [
        c for c in optional_controls
        if c in df.columns and df[c].notna().sum() > 100
    ]
    controls_base = " + ".join(available_controls) if available_controls else "1"
    print(f"  Controls used: {controls_base}")

    # Rebuild full_analytic using only available focal vars
    full_focal_vars = ["tci_z", "dai_z", "mgr_experience"]
    available_focal = [v for v in full_focal_vars if v in df.columns and df[v].notna().sum() > 10]
    if "mgr_female" in df.columns and df["mgr_female"].notna().sum() > 10:
        available_focal.append("mgr_female")
    full_analytic = analytic.dropna(subset=available_focal)
    print(f"  Full analytic (revised, focal={available_focal}): {len(full_analytic):,}")

    # ---------- Model hierarchy ----------
    models = {}
    lm_tests = {}

    # M0 — intercept only
    models["M0"] = run_ols_hc1("ln_labor_prod ~ 1", analytic)

    # M1 — linear FSTS
    models["M1"] = run_ols_hc1("ln_labor_prod ~ fsts_c", analytic)

    # M2 — quadratic FSTS (H1: inverted-U)
    models["M2"] = run_ols_hc1("ln_labor_prod ~ fsts_c + fsts_c2", analytic)
    lm_tests["M2"] = lind_mehlum_test(models["M2"], "fsts_c", "fsts_c2")

    # M3 — M2 + controls
    sub3 = analytic.dropna(subset=[c for c in available_controls if c in analytic.columns])
    sub3 = sub3 if len(sub3) > 50 else analytic
    models["M3"] = run_ols_hc1(
        f"ln_labor_prod ~ fsts_c + fsts_c2 + {controls_base}", sub3
    )
    lm_tests["M3"] = lind_mehlum_test(models["M3"], "fsts_c", "fsts_c2")

    # M5 — M3 + country-year FE
    sub5 = sub3.copy()
    sub5 = sub5[sub5.groupby("cy_fe")["cy_fe"].transform("count") > 1]
    if len(sub5) > 100:
        try:
            models["M5"] = run_ols_hc1(
                f"ln_labor_prod ~ fsts_c + fsts_c2 + {controls_base} + C(cy_fe)",
                sub5
            )
            lm_tests["M5"] = lind_mehlum_test(models["M5"], "fsts_c", "fsts_c2")
        except Exception as e:
            print(f"  M5 failed: {e}")

    # M6 — M3 + TCI direct (H2 direct effect)
    sub6 = analytic.dropna(subset=["tci_z"] + [c for c in available_controls if c in analytic.columns])
    if len(sub6) > 50:
        models["M6"] = run_ols_hc1(
            f"ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + {controls_base}", sub6
        )
        lm_tests["M6"] = lind_mehlum_test(models["M6"], "fsts_c", "fsts_c2")

    # M7 — M6 + TCI moderation (H2 moderation)
    sub7 = sub6.copy()
    if len(sub7) > 50:
        models["M7"] = run_ols_hc1(
            f"ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + "
            f"fsts_c_x_tci + fsts_c2_x_tci + {controls_base}", sub7
        )
        lm_tests["M7"] = lind_mehlum_test(models["M7"], "fsts_c", "fsts_c2")
        # Joint F for TCI moderation
        try:
            r = models["M7"].f_test("fsts_c_x_tci = 0, fsts_c2_x_tci = 0")
            lm_tests["M7"]["tci_mod_joint_F"] = round(float(r.fvalue), 4)
            lm_tests["M7"]["tci_mod_joint_p"] = round(float(r.pvalue), 4)
        except Exception:
            pass

    # M8 — M7 + DAI direct + DAI moderation (H3/H4)
    sub8 = analytic.dropna(subset=["tci_z", "dai_z"] + [c for c in available_controls if c in analytic.columns])
    if len(sub8) > 50:
        models["M8"] = run_ols_hc1(
            f"ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + "
            f"fsts_c_x_tci + fsts_c2_x_tci + dai_z + "
            f"fsts_c_x_dai + fsts_c2_x_dai + {controls_base}", sub8
        )
        lm_tests["M8"] = lind_mehlum_test(models["M8"], "fsts_c", "fsts_c2")
        try:
            r = models["M8"].f_test("fsts_c_x_dai = 0, fsts_c2_x_dai = 0")
            lm_tests["M8"]["dai_mod_joint_F"] = round(float(r.fvalue), 4)
            lm_tests["M8"]["dai_mod_joint_p"] = round(float(r.pvalue), 4)
        except Exception:
            pass

    # M9 — Top manager moderation (H4)
    mgr_vars = ["mgr_experience"]
    if "mgr_female" in df.columns and df["mgr_female"].notna().sum() > 10:
        mgr_vars.append("mgr_female")
    mgr_formula_terms = "mgr_experience + fsts_c_x_mgr"
    if "mgr_female" in mgr_vars:
        mgr_formula_terms += " + mgr_female"
    sub9 = analytic.dropna(subset=["tci_z", "dai_z"] + mgr_vars +
                            [c for c in available_controls if c in analytic.columns])
    if len(sub9) > 50:
        models["M9"] = run_ols_hc1(
            f"ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + "
            f"fsts_c_x_tci + fsts_c2_x_tci + dai_z + "
            f"fsts_c_x_dai + fsts_c2_x_dai + "
            f"{mgr_formula_terms} + {controls_base}", sub9
        )
        lm_tests["M9"] = lind_mehlum_test(models["M9"], "fsts_c", "fsts_c2")

    # M10 — ICRV institutional moderation (H5)
    sub10 = analytic.dropna(subset=["icrv_group", "tci_z", "dai_z"] +
                             [c for c in available_controls if c in analytic.columns])
    if len(sub10) > 50 and sub10["icrv_group"].nunique() > 1:
        models["M10"] = run_ols_hc1(
            f"ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z + "
            f"icrv_group + fsts_c_x_icrv + fsts_c2_x_icrv + "
            f"{controls_base}", sub10
        )
        lm_tests["M10"] = lind_mehlum_test(models["M10"], "fsts_c", "fsts_c2")

    # M11 — Full 3-way: DAI × ICRV × mgr_experience (H7-P7)
    sub11 = analytic.dropna(subset=["icrv_group", "tci_z", "dai_z",
                                     "mgr_experience"] +
                             [c for c in available_controls if c in analytic.columns])
    if len(sub11) > 50 and sub11["icrv_group"].nunique() > 1:
        try:
            m11_mgr = "mgr_experience + fsts_c_x_mgr"
            if "mgr_female" in df.columns and df["mgr_female"].notna().sum() > 10:
                m11_mgr += " + mgr_female"
            models["M11"] = run_ols_hc1(
                f"ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z + "
                f"icrv_group + fsts_c_x_icrv + "
                f"fsts_c_x_dai + dai_x_icrv + "
                f"fsts_c_x_dai_x_icrv + "
                f"{m11_mgr} + {controls_base}", sub11
            )
            lm_tests["M11"] = lind_mehlum_test(models["M11"], "fsts_c", "fsts_c2")
        except Exception as e:
            print(f"  M11 failed: {e}")

    # ---------- Export results ----------
    coef_df = format_results(models, lm_tests)
    coef_path = out_dir / "p7_coefs_all_models.csv"
    coef_df.to_csv(coef_path, index=False)
    print(f"\nSaved {coef_path}")

    # Summary table (focal terms only)
    focal_terms = ["Intercept", "fsts_c", "fsts_c2", "tci_z", "dai_z",
                   "fsts_c_x_tci", "fsts_c2_x_tci",
                   "fsts_c_x_dai", "fsts_c2_x_dai",
                   "mgr_experience", "mgr_female",
                   "icrv_group", "fsts_c_x_icrv",
                   "fsts_c_x_dai_x_icrv"]
    summary = coef_df[coef_df["term"].isin(focal_terms)].copy()
    summary_path = out_dir / "p7_summary_focal.csv"
    summary.to_csv(summary_path, index=False)
    print(f"Saved {summary_path}")

    # Model fit table
    fit_rows = []
    for mname, res in models.items():
        lm = lm_tests.get(mname, {})
        fit_rows.append({
            "model": mname, "n": int(res.nobs),
            "r2": round(res.rsquared, 4),
            "adj_r2": round(res.rsquared_adj, 4),
            "aic": round(res.aic, 2),
            "turning_point_pct": lm.get("tp", np.nan),
            "lm_p": lm.get("lm_p", np.nan),
            "shape": lm.get("shape", ""),
            "tci_mod_joint_p": lm.get("tci_mod_joint_p", np.nan),
            "dai_mod_joint_p": lm.get("dai_mod_joint_p", np.nan),
        })
    fit_df = pd.DataFrame(fit_rows)
    fit_path = out_dir / "p7_model_fit.csv"
    fit_df.to_csv(fit_path, index=False)
    print(f"Saved {fit_path}")

    # JSON audit
    audit = {
        "n_total": int(len(analytic)),
        "n_countries": int(analytic["country"].nunique()),
        "n_country_years": int(analytic.groupby(["country", "year"]).ngroups),
        "countries": sorted(analytic["country"].unique().tolist()),
        "models_run": list(models.keys()),
    }
    audit_path = out_dir / "p7_audit.json"
    with open(audit_path, "w") as f:
        json.dump(audit, f, indent=2, default=str)

    # Console summary
    print("\n=== MODEL FIT SUMMARY ===")
    print(fit_df[["model", "n", "adj_r2", "turning_point_pct",
                   "lm_p", "shape"]].to_string(index=False))

    print("\n=== KEY FOCAL COEFFICIENTS ===")
    for mname in ["M2", "M7", "M8", "M10"]:
        if mname not in models:
            continue
        res = models[mname]
        print(f"\n--- {mname} (N={int(res.nobs)}, AdjR²={res.rsquared_adj:.3f}) ---")
        for term in focal_terms:
            if term in res.params.index:
                b = res.params[term]
                p = res.pvalues[term]
                sig = ("***" if p < 0.001 else "**" if p < 0.01 else
                       "*" if p < 0.05 else "†" if p < 0.10 else "")
                print(f"  {term:35s}  b={b:+.4f}  p={p:.4f} {sig}")


if __name__ == "__main__":
    main()
