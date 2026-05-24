"""
P6 Meta-Analysis — Publication figure generation (updated with real MARA results).

Reads from p6/results/table*.csv, forest_data.csv, loo_data.csv, and
funnel_imputed.csv. All values come from the MARA pipeline (p6_real_mara.py
/ p6_real_mara.R) run on the k=238, K=288 coded database.

Figures produced:
  Figure 2 — ICRV 5-regime forest plot          → figures/figure2_icrv_forest.png
  Figure 3 — DPL phase bar chart                 → figures/figure3_dpl_phase.png
  Figure 4 — Leave-one-out sensitivity scatter   → figures/figure4_sensitivity.png
  Figure 5 — Funnel plot with trim-and-fill       → figures/figure5_funnel_plot.png

Style: academic grayscale, 300 DPI, Times New Roman-like serif font.

Usage:
    python3 p6/scripts/generate_p6_figures.py
"""

import csv
import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR  = pathlib.Path(__file__).parent.resolve()
RESULTS_DIR = SCRIPT_DIR.parent / "results"
FIGURES_DIR = SCRIPT_DIR.parent / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# ── Load real MARA results ────────────────────────────────────────────────────
def _load_csv(name):
    with open(RESULTS_DIR / name) as f:
        return list(csv.DictReader(f))


baseline_row = _load_csv("table1_baseline.csv")[0]
POOLED_R     = float(baseline_row["r_pooled"])
POOLED_LO    = float(baseline_row["r_ci_lo"])
POOLED_HI    = float(baseline_row["r_ci_hi"])
K_EFFECTS    = int(baseline_row["K_effects"])
K_STUDIES    = int(baseline_row["k_studies"])
I2_TOTAL     = float(baseline_row["I2_total"])
QM_TOTAL     = float(baseline_row["Q_total"])

icrv_rows = _load_csv("table2_icrv.csv")
dpl_rows  = _load_csv("table4_dpl.csv")
sens_rows = _load_csv("table5_sensitivity.csv")
forest_rows = _load_csv("forest_data.csv")
loo_rows = _load_csv("loo_data.csv")
imputed_rows = _load_csv("funnel_imputed.csv")

# ── Academic style (grayscale, serif) ─────────────────────────────────────────
plt.rcParams.update({
    "font.family":        "serif",
    "font.serif":         ["Times New Roman", "DejaVu Serif", "Palatino", "serif"],
    "font.size":          10,
    "axes.titlesize":     11,
    "axes.labelsize":     10,
    "xtick.labelsize":    9,
    "ytick.labelsize":    9,
    "legend.fontsize":    9,
    "figure.dpi":         150,
    "savefig.dpi":        300,
    "savefig.bbox":       "tight",
    "text.color":         "black",
    "axes.labelcolor":    "black",
    "xtick.color":        "black",
    "ytick.color":        "black",
    "axes.edgecolor":     "black",
    "axes.spines.top":    False,
    "axes.spines.right":  False,
})


def _save(fig, stem):
    for ext in ("png", "pdf"):
        path = FIGURES_DIR / f"{stem}.{ext}"
        fig.savefig(path, dpi=300, bbox_inches="tight")
        print(f"  Saved: {path}")
    plt.close(fig)


# ── Figure 2: ICRV 5-Regime Forest Plot ───────────────────────────────────────
def figure2_icrv_forest():
    """Forest plot — ICRV 5-regime subgroup pooled effects (real MARA results).

    Note: FR (k=3) is anomalous (r=0.349) and must be clearly marked.
    """
    # Display order: I, II, III, MX, FR (FR at bottom as anomaly)
    regime_order = ["I", "II", "III", "MX", "FR"]
    regime_labels = {
        "I":  "I — Advanced-Innovation\n(SG, HK, KR, JP, TW, AU…)",
        "II": "II — Upper-middle\n(CN, MY, TH, BR, ZA…)",
        "III":"III — Emerging\n(VN, IN, PH, ID…)",
        "MX": "MX — Multi-country / mixed",
        "FR": "FR — Frontier (anomaly: k = 3)\n(BD, MM, PK, IR…)",
    }

    icrv_dict = {r["regime"]: r for r in icrv_rows}
    qm_val = float(icrv_rows[0]["QM"])

    regimes_plot = []
    for code in regime_order:
        if code not in icrv_dict:
            continue
        row = icrv_dict[code]
        regimes_plot.append((
            regime_labels.get(code, code),
            float(row["r_est"]),
            float(row["r_ci_lo"]),
            float(row["r_ci_hi"]),
            int(row["k"]),
            code == "FR",   # flag anomaly
        ))

    pooled = (f"Pooled (k = {K_STUDIES}, K = {K_EFFECTS})",
              POOLED_R, POOLED_LO, POOLED_HI)

    n_rows = len(regimes_plot) + 1
    fig, ax = plt.subplots(figsize=(10, 6))

    k_max = max(r[4] for r in regimes_plot)

    for i, (label, r, lo, hi, k, is_anomaly) in enumerate(regimes_plot):
        y = n_rows - i
        sq_size = 5 + 9 * (k / k_max)
        color = "gray" if is_anomaly else "black"

        ax.errorbar(r, y, xerr=[[r - lo], [hi - r]],
                    fmt="none", color=color, capsize=4,
                    capthick=1.2, linewidth=1.2, zorder=3)
        ax.plot(r, y, "s", color=color, markersize=sq_size, zorder=4)

        tag = " *anomaly*" if is_anomaly else ""
        ax.text(0.68, y,
                f"r = {r:.3f}  [{lo:.3f}, {hi:.3f}]  K = {k}{tag}",
                va="center", fontsize=8.5,
                transform=ax.get_yaxis_transform(),
                color=color)

    ax.axhline(0.5, color="black", linewidth=0.8)

    _, r_p, lo_p, hi_p = pooled
    diamond_half_h = 0.32
    diamond_x  = [lo_p, r_p, hi_p, r_p, lo_p]
    diamond_yy = [0, diamond_half_h, 0, -diamond_half_h, 0]
    ax.fill(diamond_x, diamond_yy, color="black", zorder=5)
    ax.text(0.68, 0,
            f"r = {r_p:.3f}  [{lo_p:.3f}, {hi_p:.3f}]  k = {K_STUDIES}",
            va="center", fontsize=8.5, fontweight="bold",
            transform=ax.get_yaxis_transform())
    ax.text(-0.26, 0, "Pooled", va="center", ha="left",
            fontsize=9, fontweight="bold")

    ax.axvline(0, color="black", linewidth=0.9, linestyle="--", alpha=0.6, zorder=1)

    ax.set_yticks([n_rows - i for i in range(len(regimes_plot))])
    ax.set_yticklabels([r[0] for r in regimes_plot], fontsize=8.5)
    ax.set_ylim(-0.8, n_rows + 0.5)
    ax.set_xlim(-0.30, 0.55)
    ax.set_xlabel("Pooled effect size (r)", fontsize=10)

    ax.text(0.01, 0.01,
            f"$Q_M$ = 17.35,  df = 4,  p = .002  (between-regimes test)",
            transform=ax.transAxes, fontsize=8.5,
            va="bottom", ha="left", style="italic")

    ax.set_title("Figure 2. ICRV 5-Regime Subgroup Forest Plot\n"
                 f"Three-level MARA: k = {K_STUDIES} studies, K = {K_EFFECTS} effect sizes",
                 fontsize=11, fontweight="bold", pad=8)
    fig.tight_layout()
    _save(fig, "figure2_icrv_forest")


# ── Figure 3: DPL Phase Bar Chart ─────────────────────────────────────────────
def figure3_dpl_phase():
    """Bar chart — DPL phase actual results (PRE > FOL > SPN, all NS).

    Uses real MARA values. Note: results do not support H3 (p=.734).
    """
    phase_order  = ["PRE", "SPN", "FOL"]
    phase_labels = {
        "PRE": "Precede\n(data pre-2009)",
        "SPN": "Span\n(2005–2014)",
        "FOL": "Follow\n(post-2014)",
    }
    dpl_dict = {r["phase"]: r for r in dpl_rows}
    qm_val   = float(dpl_rows[0]["QM"])

    phases_plot = []
    for code in phase_order:
        if code not in dpl_dict:
            continue
        row = dpl_dict[code]
        phases_plot.append((
            phase_labels[code],
            float(row["r_est"]),
            float(row["r_ci_lo"]),
            float(row["r_ci_hi"]),
            int(row["k"]),
        ))

    x  = np.arange(len(phases_plot))
    fig, ax = plt.subplots(figsize=(6.5, 5))

    for i, (label, r, lo, hi, k) in enumerate(phases_plot):
        ax.bar(i, r, width=0.5, color="white", edgecolor="black",
               linewidth=1.2, zorder=3)
        ax.errorbar(i, r, yerr=[[r - lo], [hi - r]],
                    fmt="none", color="black", capsize=6,
                    capthick=1.5, linewidth=1.5, zorder=4)
        ax.text(i, hi + 0.004, f"K = {k}", ha="center", va="bottom", fontsize=9)

    ax.axhline(POOLED_R, color="black", linewidth=1.0, linestyle="--",
               alpha=0.65, label=f"Pooled baseline r = {POOLED_R:.3f}")

    ax.set_xticks(x)
    ax.set_xticklabels([p[0] for p in phases_plot], fontsize=9.5)
    ax.set_ylabel("Pooled effect size (r)", fontsize=10)
    ax.set_ylim(0, 0.14)
    ax.legend(fontsize=8.5, loc="upper right")

    ax.text(0.5, 0.05,
            f"$Q_M$ = 0.62,  df = 2,  p = .734\n(H3 not supported — all phases NS)",
            transform=ax.transAxes, fontsize=8.5,
            va="bottom", ha="center", style="italic")

    ax.set_title("Figure 3. DPL Phase Moderation of I→P Effect\n"
                 "(Actual results: PRE > FOL > SPN, all non-significant)",
                 fontsize=11, fontweight="bold", pad=8)
    fig.tight_layout()
    _save(fig, "figure3_dpl_phase")


# ── Figure 4: Leave-One-Out Sensitivity Scatter ───────────────────────────────
def figure4_sensitivity():
    """Leave-one-out sensitivity scatter from real loo_data.csv.

    Each point = pooled r after removing one study (two-level REML).
    """
    loo_r = np.array([float(row["r_pooled"]) for row in loo_rows])
    study_idx = np.arange(1, len(loo_r) + 1)
    lo, hi = loo_r.min(), loo_r.max()
    n_reverse = int((loo_r < 0).sum())

    fig, ax = plt.subplots(figsize=(9, 4))
    ax.scatter(study_idx, loo_r, color="gray", s=12, alpha=0.6, zorder=3)

    ax.axhline(POOLED_R, color="black", linewidth=1.0, linestyle="--",
               label=f"Three-level estimate r = {POOLED_R:.3f}")
    ax.axhline(lo, color="black", linewidth=0.7, linestyle=":",
               alpha=0.5, label=f"LOO range [{lo:.3f}, {hi:.3f}]")
    ax.axhline(hi, color="black", linewidth=0.7, linestyle=":", alpha=0.5)

    n_studies = len(loo_r)
    ax.set_xlabel(f"Study index (1 – {n_studies})", fontsize=10)
    ax.set_ylabel("Pooled r after study removed", fontsize=10)
    ax.set_xlim(0, n_studies + 5)
    ax.set_ylim(min(0.055, lo - 0.01), max(0.095, hi + 0.01))
    ax.legend(fontsize=8.5, loc="upper right")
    ax.text(0.02, 0.05,
            f"{n_reverse} / {n_studies} studies reverse direction   |   "
            f"Range: [{lo:.3f}, {hi:.3f}]",
            transform=ax.transAxes, fontsize=8.5, va="bottom", style="italic")
    ax.set_title(
        f"Figure 4. Leave-One-Out Sensitivity Analysis (k = {n_studies} studies)",
        fontsize=11, fontweight="bold", pad=8)
    fig.tight_layout()
    _save(fig, "figure4_sensitivity")


# ── Figure 5: Funnel Plot with Trim-and-Fill ──────────────────────────────────
def figure5_funnel_plot():
    """Funnel plot from real forest_data + real trim-and-fill imputed points.

    Trim-and-fill (metafor L0, left side): k=58 imputed, adj r=0.035 [0.019, 0.051].
    Egger: b=0.475, p=.057.  Begg: tau=-0.134, p=.0007.
    """
    r_obs  = np.array([float(row["r_i"]) for row in forest_rows])
    n_obs  = np.array([float(row["n"])   for row in forest_rows])
    se_obs = np.sqrt(1.0 / (n_obs - 3))

    # Real trim-and-fill imputed studies (reflected, from funnel_imputed.csv)
    r_imp  = np.array([float(row["r_imputed"]) for row in imputed_rows])
    se_imp = np.array([float(row["se"])        for row in imputed_rows])
    k_imputed = len(r_imp)

    adj_r    = 0.035
    se_range = np.linspace(0, 0.28, 200)

    fig, ax = plt.subplots(figsize=(7.5, 6))

    ax.plot(POOLED_R + 1.96 * se_range, se_range,
            color="black", linewidth=0.9, linestyle="--", alpha=0.6)
    ax.plot(POOLED_R - 1.96 * se_range, se_range,
            color="black", linewidth=0.9, linestyle="--", alpha=0.6,
            label="±1.96 SE funnel")
    ax.axvline(POOLED_R, color="black", linewidth=0.8, linestyle="-", alpha=0.5)
    ax.axvline(adj_r, color="black", linewidth=0.8, linestyle=":",
               alpha=0.5, label=f"Trim-and-fill adj. r = {adj_r:.3f}")

    ax.scatter(r_obs, se_obs, facecolors="none", edgecolors="black",
               s=18, linewidths=0.6, alpha=0.55, zorder=3,
               label=f"Original effects (K = {K_EFFECTS})")
    ax.scatter(r_imp, se_imp, facecolors="black", edgecolors="black",
               s=22, zorder=4,
               label=f"Trim-and-fill imputed (k = {k_imputed})")

    ax.set_ylim(0.30, -0.005)
    ax.set_xlim(-0.35, 0.50)
    ax.set_xlabel("Effect size (r)", fontsize=10)
    ax.set_ylabel("Standard error (SE)", fontsize=10)

    ax.text(0.98, 0.04,
            f"Egger: b = 0.475, p = .057\nBegg: τ = −0.134, p = .0007",
            transform=ax.transAxes, fontsize=8.5,
            va="bottom", ha="right", style="italic")

    ax.legend(fontsize=8.5, loc="upper right")
    ax.set_title(
        "Figure 5. Funnel Plot with Trim-and-Fill Correction\n"
        f"k = {k_imputed} imputed; adj. r = {adj_r:.3f} [0.019, 0.051]",
        fontsize=11, fontweight="bold", pad=8)
    fig.tight_layout()
    _save(fig, "figure5_funnel_plot")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nP6 manuscript figures → {FIGURES_DIR}\n")
    print(f"Baseline: r = {POOLED_R:.3f} [{POOLED_LO:.3f}, {POOLED_HI:.3f}], "
          f"k = {K_STUDIES}, K = {K_EFFECTS}, I² = {I2_TOTAL}%\n")
    figure2_icrv_forest()
    figure3_dpl_phase()
    figure4_sensitivity()
    figure5_funnel_plot()
    print("\nDone. 8 files written (PNG + PDF for each figure).")
