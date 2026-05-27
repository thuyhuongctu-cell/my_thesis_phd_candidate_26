"""
P6 Meta-Analysis — Manuscript figure generation
Produces Figures 2–4 for p6_meta_manuscript_en.md.

ALL FIGURES USE SIMULATED DATA (framework validation only).
Replace with actual PRISMA-extracted data once coded effects available at
  data/p6_coded_effects.rds  (target: 06/2026).

Usage:  python p6/figures/generate_p6_figures.py
Output: p6/figures/  (PDF + PNG for each figure)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUTDIR = os.path.dirname(os.path.abspath(__file__))
LABEL_SIMULATED = "(Framework validation — illustrative based on simulated data)"

# ── Academic style ─────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family":       "serif",
    "font.size":         10,
    "axes.titlesize":    11,
    "axes.labelsize":    10,
    "xtick.labelsize":   9,
    "ytick.labelsize":   9,
    "legend.fontsize":   9,
    "figure.dpi":        150,
    "savefig.dpi":       300,
    "savefig.bbox":      "tight",
    "axes.spines.top":   False,
    "axes.spines.right": False,
})

def save(fig, name):
    for ext in ("pdf", "png"):
        p = os.path.join(OUTDIR, f"{name}.{ext}")
        fig.savefig(p)
        print(f"  Saved: {p}")
    plt.close(fig)


# ── Figure 2: ICRV 5-Regime Forest Plot ────────────────────────────────────
# Values from moderator RDS (combined model, simulated data):
# Intercept = Emerging (reference); regime estimates are relative to Emerging
# Converted back to absolute regime means for display.

def fig_icrv_forest():
    # regime: (r_mean, ci_lo, ci_hi, k_approx, description)
    regimes = {
        "I — Advanced-Innovation\n(SG, HK, JP, KR…)":   (0.051,  -0.057,  0.159,  "~18", "#1a4e8a"),
        "II — Upper-middle\n(CN, MY, TH…)":              (0.153,   0.008,  0.299,  "~42", "#2c7bb6"),
        "III — Emerging\n(VN, IN, PH…)":                 (0.204,   0.098,  0.309,  "~35", "#74add1"),
        "SIDS — Pacific Islands":                         (0.222,   0.010,  0.434,  "~5",  "#abd9e9"),
        "V — Frontier\n(BD, MM…)":                       (0.100,  -0.033,  0.233,  "~10", "#fee090"),
    }

    fig, ax = plt.subplots(figsize=(9, 5))

    y_ticks = list(range(len(regimes)))[::-1]
    for i, (label, (r, lo, hi, k, col)) in enumerate(regimes.items()):
        y = y_ticks[i]
        xerr_lo = r - lo
        xerr_hi = hi - r
        ax.errorbar(r, y, xerr=[[xerr_lo], [xerr_hi]],
                    fmt="s", color=col, markersize=10, capsize=6,
                    capthick=1.8, linewidth=2, markeredgecolor="black",
                    markeredgewidth=0.6, zorder=4)
        ax.text(hi + 0.01, y, f"r̄={r:.3f}  [{lo:.3f}, {hi:.3f}]  k{k}",
                va="center", fontsize=8.5)

    # Pooled baseline
    ax.axvline(0.142, color="grey", linestyle="--", linewidth=1.2,
               alpha=0.8, label="Pooled baseline r = 0.142")
    ax.axvline(0, color="black", linewidth=0.7, alpha=0.4)

    ax.set_yticks(y_ticks)
    ax.set_yticklabels(list(regimes.keys()), fontsize=9)
    ax.set_xlabel("Fisher's Z effect size (r)", fontsize=10)
    ax.set_xlim(-0.25, 0.65)
    ax.set_title(
        f"Figure 2. ICRV 5-Regime Moderation of I→P Effect (H1)\n{LABEL_SIMULATED}",
        fontsize=11,
    )
    ax.legend(fontsize=8, loc="lower right")
    fig.tight_layout()
    save(fig, "figure2_icrv_forest")


# ── Figure 3: Sensitivity Analysis Plot ────────────────────────────────────
# SA1–SA6 results from 04_sensitivity.R (simulated data)

def fig_sensitivity():
    analyses = [
        ("Baseline\n(k=186)",          0.142, 0.114, 0.170),
        ("SA1: Published only\n(k≈140)", 0.141, 0.112, 0.170),
        ("SA2: High quality\n(NOS≥7, k≈98)", 0.181, 0.142, 0.220),
        ("SA3: Winsorized\nESs",        0.139, 0.111, 0.167),
        ("SA4: Pre-2015\n(k≈90)",       0.153, 0.118, 0.188),
        ("SA4: 2015–2025\n(k≈96)",      0.126, 0.091, 0.161),
        ("SA6: WBES-only\n(k≈28)",      0.160, 0.048, 0.272),
    ]

    fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(analyses))

    for i, (label, r, lo, hi) in enumerate(analyses):
        color = "#2c7bb6" if i == 0 else "#74add1"
        ax.errorbar(i, r, yerr=[[r - lo], [hi - r]],
                    fmt="o", color=color, markersize=9, capsize=6,
                    capthick=1.8, linewidth=2, zorder=3)

    ax.axhline(0.142, color="grey", linestyle="--", linewidth=1.2,
               alpha=0.7, label="Baseline r = 0.142")
    ax.axhline(0, color="black", linewidth=0.7, alpha=0.3)

    ax.fill_between([-0.5, len(analyses) - 0.5], [0.114, 0.114], [0.170, 0.170],
                    alpha=0.12, color="#2c7bb6", label="Baseline 95% CI")

    ax.set_xticks(x)
    ax.set_xticklabels([a[0] for a in analyses], fontsize=8.5)
    ax.set_ylabel("Pooled effect size (Fisher's Z / r)", fontsize=10)
    ax.set_ylim(-0.05, 0.35)
    ax.set_title(
        f"Figure 4. Sensitivity Analysis — Robustness of Pooled I→P Effect\n{LABEL_SIMULATED}",
        fontsize=11,
    )
    ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    save(fig, "figure4_sensitivity")


# ── Figure 2b: DPL Phase moderation (temporal gradient) ────────────────────

def fig_dpl_phase():
    # Hypothesized DPL gradient from manuscript §4.5
    # Q_DPL = 9.2, df=2, p=.010 — illustrative values matching manuscript
    phases = [
        ("Precede\n(<2009)", 0.02, -0.04, 0.08,  "#fee090"),
        ("Span\n(2005–2014)", 0.06, 0.02, 0.10,  "#74add1"),
        ("Follow\n(>2014)", 0.12, 0.07, 0.17,   "#1a4e8a"),
    ]

    fig, ax = plt.subplots(figsize=(6, 4))

    for i, (label, r, lo, hi, col) in enumerate(phases):
        ax.bar(i, r, color=col, width=0.5, alpha=0.85, zorder=3)
        ax.errorbar(i, r, yerr=[[r - lo], [hi - r]],
                    fmt="none", color="black", capsize=8, capthick=1.5,
                    linewidth=1.5, zorder=4)
        ax.text(i, hi + 0.005, f"r̄={r:.2f}", ha="center", va="bottom",
                fontsize=9, fontweight="bold")

    ax.axhline(0.07, color="grey", linestyle="--", linewidth=1.2,
               alpha=0.7, label="ICBEF 2025 baseline r = 0.07")
    ax.set_xticks(range(len(phases)))
    ax.set_xticklabels([p[0] for p in phases], fontsize=9)
    ax.set_ylabel("Pooled I→P effect size (r)", fontsize=10)
    ax.set_ylim(-0.1, 0.25)
    ax.set_title(
        f"Figure 3. DPL Phase Temporal Gradient (H2)\n"
        f"Q_DPL = 9.2, df = 2, p = .010\n{LABEL_SIMULATED}",
        fontsize=10,
    )
    ax.legend(fontsize=8)
    fig.tight_layout()
    save(fig, "figure3_dpl_phase")


# ── Main ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nGenerating P6 manuscript figures → {OUTDIR}")
    print("NOTE: All figures use simulated data for framework validation.\n")
    fig_icrv_forest()
    fig_dpl_phase()
    fig_sensitivity()
    print("\nDone. 6 files written (PDF + PNG for each figure).")
