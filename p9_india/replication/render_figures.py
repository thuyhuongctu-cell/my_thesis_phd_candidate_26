#!/usr/bin/env python3
"""
P9' India — Figure 2 + Figure 3 + Figure 4 rendering (300 DPI, B&W-safe).

Figure 1 (Conceptual model) — done separately via academic-conceptual-model-diagram
skill or PowerPoint; not rendered here.

Figure 2: Wave-specific predicted I-P curves (overlay 2014, 2022, 2025)
Figure 3: Turning-point estimates with 95% CI by wave
Figure 4: UPI quasi-experiment timeline (transaction volume + policy markers)

Outputs in p9_india/replication/figures/:
- figure_2_predicted_curves.png  (300 dpi)
- figure_2_predicted_curves.pdf  (vector)
- figure_3_turning_points.png
- figure_3_turning_points.pdf
- figure_4_upi_timeline.png
- figure_4_upi_timeline.pdf
"""

from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

ROOT = Path(__file__).resolve().parents[2]
RES = ROOT / "p9_india" / "replication" / "results"
OUT = ROOT / "p9_india" / "replication" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Academic style — B&W safe, serif fonts
mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Liberation Serif", "serif"],
    "font.size": 10,
    "axes.labelsize": 11,
    "axes.titlesize": 11,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.size": 4,
    "ytick.major.size": 4,
    "legend.frameon": False,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
})


def load_coefs():
    """Load M2 coefficients across 3 waves from CSV."""
    df = pd.read_csv(RES / "p9_india_coefs_main_models.csv")
    coefs = {}
    for w in (2014, 2022, 2025):
        sub = df[df["wave"] == w].set_index("term")
        coefs[w] = {
            "FSTS": sub.loc["FSTS", "coef"],
            "FSTSsq": sub.loc["FSTSsq", "coef"],
            "const": sub.loc["const", "coef"],
            "n": int(sub.loc["FSTS", "n"]),
        }
    return coefs


def load_tps():
    df = pd.read_csv(RES / "p9_india_turning_points.csv")
    return df.set_index("wave")


# ============================================================
# FIGURE 2 — Predicted I-P curves by wave
# ============================================================
def render_figure_2():
    coefs = load_coefs()
    tps = load_tps()

    fig, ax = plt.subplots(figsize=(6.5, 4.2))

    fsts = np.linspace(0, 1, 200)

    # Wave styling
    styles = {
        2014: {"color": "black", "linestyle": "-", "label": "2014 (PICS3, pre-reform)"},
        2022: {"color": "black", "linestyle": "--", "label": "2022 (BEE, mid-decade)"},
        2025: {"color": "black", "linestyle": ":", "label": "2025 (BREADY, post-reform)"},
    }

    for w in (2014, 2022, 2025):
        c = coefs[w]
        # Centred on each wave's intercept = 0 (show only FSTS-induced variation)
        predicted = c["FSTS"] * fsts + c["FSTSsq"] * fsts ** 2
        ax.plot(fsts * 100, predicted, linewidth=1.6, **styles[w])

        # Annotate turning point for waves with inverted-U
        tp = tps.loc[w, "tp_pct"]
        if 0 <= tp <= 100:
            tp_y = c["FSTS"] * (tp / 100) + c["FSTSsq"] * (tp / 100) ** 2
            ax.scatter([tp], [tp_y], color="black", s=24, zorder=5,
                       marker="o" if w == 2014 else ("s" if w == 2022 else "^"))
            ax.annotate(f"TP {tp:.1f}%", xy=(tp, tp_y),
                        xytext=(tp + 2, tp_y + 0.05),
                        fontsize=8, ha="left")

    ax.axhline(0, color="grey", linewidth=0.5, linestyle="-", alpha=0.4)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Export intensity (FSTS, %)")
    ax.set_ylabel("Predicted partial effect on ln(Labour Productivity)")
    ax.set_title("Figure 2.  Wave-specific predicted I-P relationship — India 2014, 2022, 2025",
                 loc="left", pad=10)
    ax.legend(loc="lower left", fontsize=9)

    ax.text(0.02, -0.18, "Notes: Curves show $\\hat\\beta_1\\!\\cdot\\!\\mathrm{FSTS} + \\hat\\beta_2\\!\\cdot\\!\\mathrm{FSTS}^2$ from "
                          "M2 regressions. Turning points (markers): 2014 = 61.8 %, 2022 = 40.7 %, "
                          "2025 = undefined (curvature non-significant). N = 8,941 (2014), 9,300 (2022), 10,476 (2025).",
            transform=ax.transAxes, fontsize=8, va="top", wrap=True)

    plt.subplots_adjust(bottom=0.25)
    plt.savefig(OUT / "figure_2_predicted_curves.png")
    plt.savefig(OUT / "figure_2_predicted_curves.pdf")
    plt.close()
    print(f"  ✓ Figure 2 → {OUT / 'figure_2_predicted_curves.png'}")


# ============================================================
# FIGURE 3 — Turning points with 95% CI by wave
# ============================================================
def render_figure_3():
    tps = load_tps()

    fig, axes = plt.subplots(1, 2, figsize=(7.5, 3.8), gridspec_kw={"width_ratios": [2, 1]})

    # Panel A — 2014 and 2022 TPs with CI
    ax = axes[0]
    waves_with_tp = [2014, 2022]
    for i, w in enumerate(waves_with_tp):
        tp = tps.loc[w, "tp_pct"]
        lo = tps.loc[w, "ci_low_pct"]
        hi = tps.loc[w, "ci_high_pct"]
        ax.errorbar([i], [tp], yerr=[[tp - lo], [hi - tp]],
                    fmt="o", color="black", capsize=5, markersize=8, linewidth=1.2)
        ax.text(i, hi + 4, f"{tp:.1f}%\n[{lo:.1f}, {hi:.1f}]",
                ha="center", fontsize=9)

    ax.set_xticks(range(len(waves_with_tp)))
    ax.set_xticklabels([f"2014\n(PICS3)", f"2022\n(BEE)"])
    ax.set_ylabel("Turning point (FSTS %)")
    ax.set_ylim(0, 80)
    ax.set_title("Panel A: Estimated turning points (2014, 2022)", loc="left", pad=8)
    ax.axhline(50, color="grey", linewidth=0.4, linestyle=":", alpha=0.6)

    # Panel B — 2025 "no TP" with monotone-negative slope diagram
    ax = axes[1]
    ax.text(0.5, 0.6,
            "2025 (BREADY)\n\n$\\hat\\beta_2 = -0.16$\n$p = 0.42$",
            ha="center", va="center", fontsize=10, transform=ax.transAxes)
    ax.text(0.5, 0.18,
            "Inverted-U not\nsupported.\nNo turning point\nin [0, 100].",
            ha="center", va="center", fontsize=9, transform=ax.transAxes,
            style="italic", color="dimgrey")

    # Schematic monotone-negative curve in upper-left corner
    ax_in = ax.inset_axes([0.08, 0.78, 0.35, 0.20])
    xs = np.linspace(0, 1, 50)
    ax_in.plot(xs, -xs * 0.4 - xs ** 2 * 0.16, color="black", linewidth=1.2)
    ax_in.set_xticks([])
    ax_in.set_yticks([])
    ax_in.set_title("predicted I-P", fontsize=7, pad=2)
    for spine in ["top", "right"]:
        ax_in.spines[spine].set_visible(False)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Panel B: 2025 collapse", loc="left", pad=8)
    for spine in ["top", "right", "bottom", "left"]:
        ax.spines[spine].set_visible(False)

    fig.suptitle("Figure 3.  Turning-point estimates and 2025 threshold collapse",
                 x=0.05, ha="left", fontsize=11, y=1.01)

    fig.text(0.05, -0.05,
             "Notes: Panel A shows turning points TP = −β̂₁ / (2β̂₂) from M2 regressions with delta-method 95 % CI. "
             "Panel B summarises the 2025 collapse: the quadratic curvature is not statistically distinguishable "
             "from zero (β̂₂ = −0.16, p = 0.42 HC1; p = 0.59 cluster-robust), and the implied 'turning point' "
             "lies outside [0, 100 %]. Lind–Mehlum joint U-test fails (p = 0.99). The 2025 panel deliberately "
             "omits a numerical TP estimate to avoid the misleading delta-method CI of [−472 %, +248 %].",
             fontsize=8, va="top", wrap=True)

    plt.savefig(OUT / "figure_3_turning_points.png")
    plt.savefig(OUT / "figure_3_turning_points.pdf")
    plt.close()
    print(f"  ✓ Figure 3 → {OUT / 'figure_3_turning_points.png'}")


# ============================================================
# FIGURE 4 — UPI quasi-experiment timeline
# ============================================================
def render_figure_4():
    fig, ax1 = plt.subplots(figsize=(7.5, 4.0))

    # UPI monthly transaction volume (billions, approximate) by year
    # Source: NPCI UPI Product Statistics, https://www.npci.org.in/what-we-do/upi/product-statistics
    years = np.array([2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
    upi_bn_per_month = np.array([0.001, 0.05, 0.5, 1.0, 2.2, 4.0, 7.0, 9.0, 12.0])

    ax1.fill_between(years, 0, upi_bn_per_month, color="lightgrey", alpha=0.7, label="UPI monthly transactions (B)")
    ax1.plot(years, upi_bn_per_month, color="black", linewidth=1.2, marker="o", markersize=4)
    ax1.set_xlim(2013.5, 2025.5)
    ax1.set_ylim(0, 14)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("UPI monthly transactions (billions)")

    # WBES wave markers
    wave_years = [2014, 2022, 2025]
    wave_labels = ["WBES PICS3\n(pre-UPI)", "WBES BEE\n(UPI saturating)", "WBES BREADY\n(UPI saturated)"]
    for wy, wl in zip(wave_years, wave_labels):
        ax1.axvline(wy, color="black", linestyle="--", linewidth=0.8, alpha=0.6)
        ax1.text(wy, 13.5, wl, ha="center", va="top", fontsize=8, style="italic")

    # Institutional shock markers (below the curve)
    shocks = [
        (2016.4, "UPI launch\nApr 2016"),
        (2016.9, "Demonetisation\nNov 2016"),
        (2017.5, "GST\nJul 2017"),
        (2020.2, "COVID-19 +\nAtmanirbhar Bharat\n+ PLI"),
    ]
    for sy, sl in shocks:
        ax1.annotate(sl, xy=(sy, 0.3), xytext=(sy, -2.8),
                     ha="center", fontsize=7.5, color="dimgrey",
                     arrowprops=dict(arrowstyle="->", color="dimgrey", lw=0.6))

    ax1.set_title("Figure 4.  UPI rollout and Indian institutional shocks, 2014–2025",
                  loc="left", pad=10)

    fig.text(0.05, -0.16,
             "Notes: UPI monthly transaction volume from NPCI Product Statistics (https://www.npci.org.in/). "
             "Dashed vertical lines mark the three WBES survey waves used in the analysis. The pre-UPI 2014 "
             "wave provides the baseline; the 2022 BEE wave captures the UPI-saturating period; the 2025 BREADY "
             "wave captures the post-saturation environment with Tier-2 e-payment measurement available "
             "(variable k33: % sales received via electronic payment).",
             fontsize=8, va="top", wrap=True)

    plt.subplots_adjust(bottom=0.30)
    plt.savefig(OUT / "figure_4_upi_timeline.png")
    plt.savefig(OUT / "figure_4_upi_timeline.pdf")
    plt.close()
    print(f"  ✓ Figure 4 → {OUT / 'figure_4_upi_timeline.png'}")


if __name__ == "__main__":
    print("Rendering P9' India figures…")
    render_figure_2()
    render_figure_3()
    render_figure_4()
    print("Done.")
