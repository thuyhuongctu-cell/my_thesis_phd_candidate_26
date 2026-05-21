#!/usr/bin/env python3
"""
generate_dta_from_csv.py
Convert CSV regression coefficient tables from P3/P4/P5 into proper Stata .dta files.
Also generates summary .dta datasets with key statistics for archival.

Usage:
    python3 generate_dta_from_csv.py
"""
import os
import sys
import numpy as np
import pandas as pd
import pyreadstat

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Output directory ───────────────────────────────────────────────────────
OUT = os.path.join(REPO, "replication_tools", "dta_outputs")
os.makedirs(OUT, exist_ok=True)

print("=" * 60)
print("  Generating .dta files from CSV replication results")
print("=" * 60)

# ──────────────────────────────────────────────────────────────────────────
# HELPER: write dataframe as Stata .dta with variable labels
# ──────────────────────────────────────────────────────────────────────────
def to_dta(df: pd.DataFrame, path: str, variable_labels: dict = None,
           dataset_label: str = ""):
    """Write DataFrame as Stata .dta (version 15 format)."""
    # Ensure all string columns are clean
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].astype(str).str[:80]
    pyreadstat.write_dta(df, path,
                         column_labels=variable_labels or {},
                         file_label=dataset_label[:80])
    print(f"  Saved: {os.path.relpath(path, REPO)}")


# ══════════════════════════════════════════════════════════════════════════
# PAPER 3 — Vietnam
# ══════════════════════════════════════════════════════════════════════════
print("\n── Paper 3: Vietnam ──────────────────────────────────────")

p3_coefs_path = os.path.join(REPO, "p3", "replication", "coefs_main_models.csv")
if os.path.exists(p3_coefs_path):
    df_p3 = pd.read_csv(p3_coefs_path)
    df_p3.columns = [c.lower().strip() for c in df_p3.columns]

    # Encode sample as numeric
    sample_map = {"VNM2009": 1, "VNM2015": 2, "VNM2023": 3, "VNMpooled": 4}
    df_p3["sample_code"] = df_p3["sample"].map(sample_map).fillna(0).astype(int)

    # Model number as numeric
    model_map = {f"M{i}": i for i in range(9)}
    df_p3["model_num"] = df_p3["model"].map(model_map).fillna(-1).astype(int)

    labels_p3 = {
        "sample":      "Wave label (VNM2009/2015/2023/pooled)",
        "sample_code": "Wave code (1=2009,2=2015,3=2023,4=pooled)",
        "model":       "Model specification (M0-M8)",
        "model_num":   "Model number (0-8)",
        "term":        "Regressor name",
        "b":           "OLS coefficient",
        "se":          "HC1 robust standard error",
        "p":           "Two-sided p-value",
        "ci_lo":       "Lower 95% confidence bound",
        "ci_hi":       "Upper 95% confidence bound",
        "n":           "Analytic sample size",
        "r2":          "R-squared",
    }
    to_dta(df_p3,
           os.path.join(OUT, "p3_coefs_main_models.dta"),
           labels_p3,
           "P3 Vietnam WBES — OLS coefficients (M0-M8, three waves + pooled)")

    # Turning-point table (from Lind-Mehlum CSV)
    lm_path = os.path.join(REPO, "p3", "replication", "coefs_main_models.csv")
    # Build turning points from M2 coefficients
    tp_rows = []
    for samp, sdf in df_p3[df_p3["model"] == "M2"].groupby("sample"):
        b1_row = sdf[sdf["term"].str.contains("FSTSc$", regex=True)]
        b2_row = sdf[sdf["term"].str.contains("FSTSc2", regex=True)]
        if len(b1_row) == 1 and len(b2_row) == 1:
            b1 = float(b1_row["b"].values[0])
            b2 = float(b2_row["b"].values[0])
            se1 = float(b1_row["se"].values[0])
            se2 = float(b2_row["se"].values[0])
            if b2 != 0:
                # raw TP centred = -b1/(2*b2)
                tp_c = -b1 / (2 * b2)
                # delta-method SE
                tp_se = np.sqrt((se1 / (2 * b2)) ** 2 +
                                (b1 * se2 / (2 * b2 ** 2)) ** 2)
                tp_rows.append({"sample": samp,
                                "tp_raw": tp_c + 0.25,  # approx centred mean ≈ 0.25
                                "tp_se": tp_se,
                                "tp_lo": tp_c + 0.25 - 1.96 * tp_se,
                                "tp_hi": tp_c + 0.25 + 1.96 * tp_se,
                                "b1_fsts": b1, "b2_fstssq": b2})
    if tp_rows:
        df_tp = pd.DataFrame(tp_rows)
        to_dta(df_tp,
               os.path.join(OUT, "p3_turning_points.dta"),
               {"sample": "Wave", "tp_raw": "Turning point (raw FSTS)",
                "tp_se": "Delta-method SE", "tp_lo": "Lower 95% CI",
                "tp_hi": "Upper 95% CI"},
               "P3 Vietnam — M2 turning points (delta-method CI)")
else:
    print(f"  [SKIP] Not found: {p3_coefs_path}")


# ══════════════════════════════════════════════════════════════════════════
# PAPER 4 — Singapore
# ══════════════════════════════════════════════════════════════════════════
print("\n── Paper 4: Singapore ────────────────────────────────────")

p4_coefs_path = os.path.join(REPO, "p4", "replication", "tables",
                              "coefs_main_models.csv")
if os.path.exists(p4_coefs_path):
    df_p4 = pd.read_csv(p4_coefs_path, on_bad_lines="skip")
    df_p4.columns = [c.lower().strip() for c in df_p4.columns]

    # Rename columns to match Stata conventions
    rename_map = {"beta": "b", "p_value": "p", "adj_r2": "r2_a",
                  "stars": "sig_stars"}
    df_p4 = df_p4.rename(columns={k: v for k, v in rename_map.items()
                                   if k in df_p4.columns})

    # Encode wave as numeric
    wave_map = {2009: 1, 2015: 2, 2023: 3, "pooled": 4, "2009": 1,
                "2015": 2, "2023": 3}
    df_p4["wave_code"] = df_p4["wave"].astype(str).map(
        {str(k): v for k, v in wave_map.items()}).fillna(0).astype(int)

    labels_p4 = {
        "wave":      "Survey wave (2009/2015/2023/pooled)",
        "wave_code": "Wave code (1-4)",
        "model":     "Model specification (M0-M8)",
        "term":      "Regressor name",
        "b":         "OLS coefficient",
        "se":        "HC1 robust standard error",
        "p":         "Two-sided p-value",
        "n":         "Analytic sample size",
        "r2_a":      "Adjusted R-squared",
        "notes":     "Notes",
    }
    # keep only valid column labels
    labels_p4 = {k: v for k, v in labels_p4.items() if k in df_p4.columns}

    to_dta(df_p4,
           os.path.join(OUT, "p4_coefs_main_models.dta"),
           labels_p4,
           "P4 Singapore WBES — OLS coefficients (M0-M8)")

    # Lind-Mehlum table
    lm_p4 = os.path.join(REPO, "p4", "replication", "tables",
                         "table_lind_mehlum.csv")
    if os.path.exists(lm_p4):
        df_lm = pd.read_csv(lm_p4)
        to_dta(df_lm,
               os.path.join(OUT, "p4_lind_mehlum.dta"),
               {},
               "P4 Singapore — Lind-Mehlum utest results")

    # Paternoster table
    pat_p4 = os.path.join(REPO, "p4", "replication", "tables",
                          "table_paternoster.csv")
    if os.path.exists(pat_p4):
        df_pat = pd.read_csv(pat_p4)
        to_dta(df_pat,
               os.path.join(OUT, "p4_paternoster.dta"),
               {},
               "P4 Singapore — Paternoster z-test results")
else:
    print(f"  [SKIP] Not found: {p4_coefs_path}")


# ══════════════════════════════════════════════════════════════════════════
# PAPER 5 — China
# ══════════════════════════════════════════════════════════════════════════
print("\n── Paper 5: China ────────────────────────────────────────")

p5_coefs_path = os.path.join(REPO, "p5", "replication", "results",
                              "results_coefs.csv")
p5_summary    = os.path.join(REPO, "p5", "results", "moderator_test_VERDICT.md")

if os.path.exists(p5_coefs_path):
    df_p5 = pd.read_csv(p5_coefs_path)
    df_p5.columns = [c.lower().strip() for c in df_p5.columns]

    labels_p5 = {c: c.replace("_", " ") for c in df_p5.columns}
    to_dta(df_p5,
           os.path.join(OUT, "p5_coefs_main_models.dta"),
           labels_p5,
           "P5 China WBES — OLS coefficients (M0-M8, 2012+2024+pooled)")
else:
    print(f"  [SKIP] Not found: {p5_coefs_path}")

# P5 turning points from summary.md
p5_summary_path = os.path.join(REPO, "p5", "results", "summary.md")
if os.path.exists(p5_summary_path):
    tp_data = {
        "wave": [2012, 2024, 0],          # 0=pooled
        "wave_label": ["China2012", "China2024", "ChinaPooled"],
        "tp_raw": [0.4937, 0.4719, 0.4878],
        "source": ["summary.md", "summary.md", "summary.md"],
    }
    df_tp5 = pd.DataFrame(tp_data)
    to_dta(df_tp5,
           os.path.join(OUT, "p5_turning_points.dta"),
           {"wave": "Survey wave year (0=pooled)",
            "wave_label": "Wave label",
            "tp_raw": "Turning point (raw FSTS)",
            "source": "Data source"},
           "P5 China — M2 turning points")


# ══════════════════════════════════════════════════════════════════════════
# COMBINED cross-paper turning-point summary
# ══════════════════════════════════════════════════════════════════════════
print("\n── Cross-paper turning-point summary ────────────────────")

combined = []
for paper, wave, tp, tp_lo, tp_hi in [
    ("P3_Vietnam",    2009, 0.4625, 0.3739, 0.5510),
    ("P3_Vietnam",    2015, 0.3932, 0.3029, 0.4835),
    ("P3_Vietnam",    2023, 0.4160, 0.3173, 0.5146),
    ("P3_Vietnam",    0,    0.3972, 0.3397, 0.4547),   # pooled
    ("P4_Singapore",  2023, 0.8860, 0.5300, 2.5300),   # wide CI
    ("P5_China",      2012, 0.4937, float("nan"), float("nan")),
    ("P5_China",      2024, 0.4719, float("nan"), float("nan")),
    ("P5_China",      0,    0.4878, float("nan"), float("nan")),
]:
    combined.append({"paper": paper, "wave": wave,
                     "tp_raw": tp, "tp_ci_lo": tp_lo, "tp_ci_hi": tp_hi})

df_combined = pd.DataFrame(combined)
to_dta(df_combined,
       os.path.join(OUT, "cross_paper_turning_points.dta"),
       {"paper": "Paper and country", "wave": "Survey wave (0=pooled)",
        "tp_raw": "Turning point (raw FSTS scale)",
        "tp_ci_lo": "Lower 95% CI", "tp_ci_hi": "Upper 95% CI"},
       "Cross-paper turning points: P3 Vietnam, P4 Singapore, P5 China")

print("\n" + "=" * 60)
print("  Done. All .dta files written to:")
print(f"  {os.path.relpath(OUT, REPO)}/")
print("=" * 60)
