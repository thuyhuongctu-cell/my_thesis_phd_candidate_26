#!/usr/bin/env python3
"""
P9' India — Render Tables 1, 2, 4, 5 as Markdown (Table 3 is inline in §4.3).

Outputs:
- tables/table_1_descriptives.md   (Per-wave variable means/SD)
- tables/table_2_main_m2.md         (M2 across 3 waves with HC1 + cluster SE)
- tables/table_4_moderators.md      (TCI + DAI Tier-1 + DAI Tier-2)
- tables/table_5_robustness.md      (3-wave pooled + 5 robustness specs)
"""

from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / "p9_india" / "replication" / "results"
OUT = ROOT / "p9_india" / "replication" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def stars(p):
    if pd.isna(p):
        return ""
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    if p < 0.10:
        return "†"
    return ""


# ============================================================
# TABLE 1 — Descriptives by wave
# ============================================================
def render_table_1():
    df = pd.read_csv(RES / "p9_india_descriptives.csv")
    waves = [2014, 2022, 2025]
    var_order = ["lnLP", "FSTS", "TCI_full", "DAI_core", "DAI_epay",
                 "lnEmp", "firmage", "foreigndummy"]
    var_labels = {
        "lnLP": "ln(Labour Productivity)",
        "FSTS": "Export intensity (FSTS, 0-1)",
        "TCI_full": "Technological Capability Index (z)",
        "DAI_core": "DAI Tier-1 (website binary)",
        "DAI_epay": "DAI Tier-2 (e-payment, share)",
        "lnEmp": "ln(Permanent full-time employees)",
        "firmage": "Firm age (years)",
        "foreigndummy": "Foreign-owned (≥ 10 % foreign equity)",
    }

    md = "**Table 1.** Descriptive statistics by WBES wave, India 2014–2025.\n\n"
    md += "| Variable | 2014 (N=8,941) | 2022 (N=9,300) | 2025 (N=10,476) |\n"
    md += "|---|---:|---:|---:|\n"

    for v in var_order:
        row = f"| {var_labels[v]} | "
        for w in waves:
            sub = df[(df["wave"] == w) & (df["var"] == v)]
            if len(sub) == 0 or pd.isna(sub.iloc[0]["mean"]):
                row += "— | "
            else:
                m = sub.iloc[0]["mean"]
                sd = sub.iloc[0]["sd"]
                row += f"{m:.3f} ({sd:.3f}) | "
        md += row.rstrip(" |") + " |\n"

    md += "\n*Note: Cell entries are mean (standard deviation). FSTS is direct plus indirect exports as a share of total sales. "
    md += "TCI is the z-standardised mean of four binary capability items (quality certification, foreign technology licence, "
    md += "product innovation, R&D activity), available for firms responding to at least three items. DAI Tier-2 (e-payment share) "
    md += "is measured only in the 2025 BREADY wave.*\n"

    (OUT / "table_1_descriptives.md").write_text(md)
    print(f"  ✓ Table 1 → {OUT / 'table_1_descriptives.md'}")


# ============================================================
# TABLE 2 — Main M2 across 3 waves with HC1 + cluster SE
# ============================================================
def render_table_2():
    coefs = pd.read_csv(RES / "p9_india_coefs_main_models.csv")
    rob = pd.read_csv(RES / "p9_india_robustness.csv")

    md = "**Table 2.** Wave-by-wave OLS estimates of the inverted-U M2 specification (HC1 and state-clustered SE).\n\n"
    md += "Dependent variable: ln(Labour Productivity)\n\n"
    md += "| Term | 2014 | 2022 | 2025 |\n"
    md += "|---|---:|---:|---:|\n"

    terms = [
        ("FSTS", "FSTS"),
        ("FSTSsq", "FSTS²"),
        ("lnEmp", "ln(Employees)"),
        ("firmage", "Firm age"),
        ("foreigndummy", "Foreign-owned"),
        ("const", "Constant"),
    ]

    for term, label in terms:
        row_coef = f"| {label} | "
        row_se = "|  | "
        row_se_cluster = "|  | "
        for w in (2014, 2022, 2025):
            # Main estimate from coefs_main_models
            sub = coefs[(coefs["wave"] == w) & (coefs["term"] == term)]
            # Cluster SE from robustness baseline rows
            rob_sub = rob[(rob["wave"] == w) & (rob["spec"] == "baseline")]
            if len(sub) > 0:
                b = sub.iloc[0]["coef"]
                se = sub.iloc[0]["se"]
                p = sub.iloc[0]["p"]
                row_coef += f"{b:+.3f}{stars(p)} | "
                row_se += f"({se:.3f}) | "
                # Cluster SE only available for FSTS and FSTSsq
                if term in ("FSTS", "FSTSsq") and len(rob_sub) > 0:
                    se_col = f"se_{term}_cluster"
                    p_col = f"p_{term}_cluster"
                    se_c = rob_sub.iloc[0][se_col]
                    p_c = rob_sub.iloc[0][p_col]
                    row_se_cluster += f"[{se_c:.3f}]{stars(p_c)} | "
                else:
                    row_se_cluster += " | "
            else:
                row_coef += "— | "
                row_se += " | "
                row_se_cluster += " | "

        md += row_coef.rstrip(" |") + " |\n"
        md += row_se.rstrip(" |") + " |\n"
        if term in ("FSTS", "FSTSsq"):
            md += row_se_cluster.rstrip(" |") + " |\n"

    md += "| N | "
    for w in (2014, 2022, 2025):
        sub = coefs[(coefs["wave"] == w) & (coefs["term"] == "FSTS")]
        if len(sub) > 0:
            md += f"{int(sub.iloc[0]['n']):,} | "
        else:
            md += "— | "
    md = md.rstrip(" |") + " |\n"

    md += "| R²_adj | "
    for w in (2014, 2022, 2025):
        sub = coefs[(coefs["wave"] == w) & (coefs["term"] == "FSTS")]
        if len(sub) > 0:
            md += f"{sub.iloc[0]['r2_adj']:.4f} | "
        else:
            md += "— | "
    md = md.rstrip(" |") + " |\n"

    md += "| Turning point (%) | "
    tps = pd.read_csv(RES / "p9_india_turning_points.csv").set_index("wave")
    for w in (2014, 2022, 2025):
        tp = tps.loc[w, "tp_pct"]
        if -50 <= tp <= 150:
            md += f"{tp:.1f} | "
        else:
            md += "n/a | "
    md = md.rstrip(" |") + " |\n"

    md += "| Lind–Mehlum inverted-U | "
    ut = pd.read_csv(RES / "p9_india_uTest.csv").set_index("wave")
    for w in (2014, 2022, 2025):
        sup = ut.loc[w, "inverted_U_supported"]
        p = ut.loc[w, "p_joint"]
        md += f"{'Yes' if sup else 'No'} (p = {p:.4f}) | "
    md = md.rstrip(" |") + " |\n"

    md += "\n*Note: Coefficients with HC1 robust standard errors in parentheses on the second row; "
    md += "state-clustered standard errors (Cameron et al., 2008; ~24 clusters per wave) in brackets on the third row "
    md += "for FSTS and FSTS² terms. Significance under each SE: † p < 0.10, * p < 0.05, ** p < 0.01, *** p < 0.001. "
    md += "Turning point computed as TP = −β̂₁ / (2β̂₂); reported only for waves with inverted-U supported in Lind–Mehlum test.*\n"

    (OUT / "table_2_main_m2.md").write_text(md)
    print(f"  ✓ Table 2 → {OUT / 'table_2_main_m2.md'}")


# ============================================================
# TABLE 4 — Capability moderators (TCI + DAI Tier-1 + DAI Tier-2)
# ============================================================
def render_table_4():
    mod = pd.read_csv(RES / "p9_india_moderators.csv")

    md = "**Table 4.** Capability moderation models — TCI, DAI Tier-1, and DAI Tier-2 (UPI e-payment).\n\n"
    md += "Dependent variable: ln(Labour Productivity)\n\n"

    # M3 (TCI) and M4 (DAI Tier-1) for each wave; M4b (Tier-2) only 2025
    md += "| Term | M3 TCI 2014 | M3 TCI 2022 | M3 TCI 2025 | M4 DAI Tier-1 2025 | M4b DAI Tier-2 2025 |\n"
    md += "|---|---:|---:|---:|---:|---:|\n"

    terms_to_show = [
        ("FSTS", "FSTS"),
        ("FSTSsq", "FSTS²"),
        ("TCI_full", "TCI"),
        ("FSTS:TCI_full", "FSTS × TCI"),
        ("FSTSsq:TCI_full", "FSTS² × TCI"),
        ("DAI_core", "DAI Tier-1"),
        ("FSTS:DAI_core", "FSTS × DAI Tier-1"),
        ("FSTSsq:DAI_core", "FSTS² × DAI Tier-1"),
        ("DAI_epay", "DAI Tier-2 (e-payment)"),
        ("FSTS:DAI_epay", "FSTS × DAI Tier-2"),
        ("FSTSsq:DAI_epay", "FSTS² × DAI Tier-2"),
    ]

    # Map column choice to model spec
    # M3 TCI uses interaction terms: FSTS:TCI_full and FSTSsq:TCI_full (from statsmodels naming)
    # The actual names in CSV may use FSTS_x_TCI etc.
    name_map = {
        "FSTS:TCI_full": ["FSTS_x_TCI", "FSTS:TCI_full"],
        "FSTSsq:TCI_full": ["FSTSsq_x_TCI", "FSTSsq:TCI_full"],
        "FSTS:DAI_core": ["FSTS_x_DAI", "FSTS:DAI_core"],
        "FSTSsq:DAI_core": ["FSTSsq_x_DAI", "FSTSsq:DAI_core"],
        "FSTS:DAI_epay": ["FSTS_x_DAIepay", "FSTS:DAI_epay"],
        "FSTSsq:DAI_epay": ["FSTSsq_x_DAIepay", "FSTSsq:DAI_epay"],
    }

    def find_term(model_label, wave, term_lookup):
        candidates = name_map.get(term_lookup, [term_lookup])
        for c in candidates:
            sub = mod[(mod["model"] == model_label) & (mod["wave"] == wave) & (mod["term"] == c)]
            if len(sub) > 0:
                return sub.iloc[0]
        return None

    cols = [
        ("M3_TCI", 2014),
        ("M3_TCI", 2022),
        ("M3_TCI", 2025),
        ("M4_DAI_tier1", 2025),
        ("M4b_DAI_tier2", 2025),
    ]

    for term, label in terms_to_show:
        row = f"| {label} | "
        for model_label, wave in cols:
            r = find_term(model_label, wave, term)
            if r is not None:
                b = r["coef"]
                p = r["p"]
                row += f"{b:+.3f}{stars(p)} | "
            else:
                row += " | "
        md += row.rstrip(" |") + " |\n"

    # Add N row
    md += "| N | "
    for model_label, wave in cols:
        sub = mod[(mod["model"] == model_label) & (mod["wave"] == wave)]
        if len(sub) > 0:
            md += f"{int(sub.iloc[0]['n']):,} | "
        else:
            md += "— | "
    md = md.rstrip(" |") + " |\n"

    md += "| R²_adj | "
    for model_label, wave in cols:
        sub = mod[(mod["model"] == model_label) & (mod["wave"] == wave)]
        if len(sub) > 0:
            md += f"{sub.iloc[0]['r2_adj']:.4f} | "
        else:
            md += "— | "
    md = md.rstrip(" |") + " |\n"

    md += "\n*Note: M3 augments M2 with TCI and FSTS × TCI / FSTS² × TCI interactions. "
    md += "M4 augments M2 with DAI Tier-1 (own-website binary) and corresponding interactions. "
    md += "M4b augments M2 with DAI Tier-2 (% sales received via electronic payment, 2025 BREADY only) "
    md += "and corresponding interactions. All HC1 robust standard errors. Significance: † p < 0.10, "
    md += "* p < 0.05, ** p < 0.01, *** p < 0.001. Controls (ln(Employees), firm age, foreign ownership) included "
    md += "but suppressed for space.*\n"

    (OUT / "table_4_moderators.md").write_text(md)
    print(f"  ✓ Table 4 → {OUT / 'table_4_moderators.md'}")


# ============================================================
# TABLE 5 — Robustness summary
# ============================================================
def render_table_5():
    rob = pd.read_csv(RES / "p9_india_robustness.csv")

    md = "**Table 5.** Robustness specifications — five sub-samples and one alternative dependent variable.\n\n"
    md += "M2 specification: ln(Labour Productivity) = β₀ + β₁ FSTS + β₂ FSTS² + controls.\n\n"
    md += "| Specification | Wave | N | β̂₁ FSTS | β̂₂ FSTS² | TP (%) | Inv-U? |\n"
    md += "|---|---:|---:|---:|---:|---:|:-:|\n"

    spec_labels = {
        "baseline": "Baseline (full sample)",
        "R1_manufacturing_only": "R1: Manufacturing only",
        "R2_trimmed_FSTS_le095": "R2: Trimmed FSTS ≤ 0.95",
        "R3a_SME_emp_lt100": "R3a: SME (employees < 100)",
        "R3b_Large_emp_ge100": "R3b: Large (employees ≥ 100)",
        "R4_DV_levels_std": "R4: Alt DV (standardised levels)",
    }

    spec_order = ["baseline", "R1_manufacturing_only", "R2_trimmed_FSTS_le095",
                  "R3a_SME_emp_lt100", "R3b_Large_emp_ge100", "R4_DV_levels_std"]

    for spec in spec_order:
        for w in (2014, 2022, 2025):
            r = rob[(rob["spec"] == spec) & (rob["wave"] == w)]
            if len(r) == 0:
                continue
            r = r.iloc[0]
            b1 = r["b_FSTS"]
            p1 = r["p_FSTS_HC1"]
            b2 = r["b_FSTSsq"]
            p2 = r["p_FSTSsq_HC1"]
            tp = r["tp_pct"]
            inv = "Yes" if r["lm_inverted_U"] else "No"
            tp_display = f"{tp:.1f}" if -50 <= tp <= 150 else "n/a"
            label = spec_labels[spec] if w == 2014 else ""
            md += f"| {label} | {w} | {int(r['N']):,} | {b1:+.3f}{stars(p1)} | {b2:+.3f}{stars(p2)} | {tp_display} | {inv} |\n"
        # Spacer row between specs
        md += "| | | | | | | |\n"

    md = md.rstrip("| | | | | | | |\n") + "\n"

    md += "\n*Note: HC1 robust standard errors used throughout. Significance: † p < 0.10, * p < 0.05, "
    md += "** p < 0.01, *** p < 0.001. Inv-U? column indicates whether Lind–Mehlum (2010) joint U-test "
    md += "supports inverted-U at the 5 % level. Manufacturing classification uses ISIC Rev 3.1 codes 15–37 "
    md += "for 2014 PICS3 and ISIC Rev 4 codes 10–33 for 2022 BEE and 2025 BREADY. R4 uses standardised "
    md += "labour productivity in levels (z-score within wave) as the dependent variable.*\n"

    (OUT / "table_5_robustness.md").write_text(md)
    print(f"  ✓ Table 5 → {OUT / 'table_5_robustness.md'}")


if __name__ == "__main__":
    print("Rendering P9' India tables…")
    render_table_1()
    render_table_2()
    render_table_4()
    render_table_5()
    print("Done.")
