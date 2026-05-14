#!/usr/bin/env python3
"""
generate_figures.py
Generate publication-ready figures for P3/P4/P5 from CSV replication data.
Figures: inverted-U curves, turning-point CIs, moderator marginal effects.

Usage:
    python3 generate_figures.py
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.patches import FancyArrowPatch
import warnings
warnings.filterwarnings("ignore")

REPO   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGOUT = os.path.join(REPO, "replication_tools", "figures")
os.makedirs(FIGOUT, exist_ok=True)

# ── Style ─────────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family":       "serif",
    "font.serif":        ["Times New Roman", "DejaVu Serif"],
    "font.size":         11,
    "axes.titlesize":    12,
    "axes.labelsize":    11,
    "xtick.labelsize":   10,
    "ytick.labelsize":   10,
    "legend.fontsize":   9,
    "figure.dpi":        150,
    "figure.facecolor":  "white",
    "axes.spines.top":   False,
    "axes.spines.right": False,
})

COLORS = {
    "base":     "#1a5276",   # deep navy
    "accent1":  "#2874a6",   # mid blue
    "accent2":  "#c0392b",   # crimson
    "accent3":  "#117a65",   # teal
    "neutral":  "#7f8c8d",   # grey
    "ci_fill":  "#aed6f1",   # pale blue fill
}

def save_fig(fig, name):
    path = os.path.join(FIGOUT, name)
    fig.savefig(path, bbox_inches="tight", dpi=150)
    plt.close(fig)
    print(f"  Saved: replication_tools/figures/{name}")


# ══════════════════════════════════════════════════════════════════════════
# FIG 1 — Cross-paper turning-point comparison (forest-plot style)
# ══════════════════════════════════════════════════════════════════════════
print("\n── Figure 1: Cross-paper turning points ─────────────────")

tp_data = [
    # label,          tp,    lo,    hi
    ("P3 Vietnam 2009",  0.463, 0.374, 0.551),
    ("P3 Vietnam 2015",  0.393, 0.303, 0.484),
    ("P3 Vietnam 2023",  0.416, 0.317, 0.515),
    ("P3 Vietnam Pooled",0.397, 0.340, 0.455),
    ("P5 China 2012",    0.494, np.nan, np.nan),
    ("P5 China 2024",    0.472, np.nan, np.nan),
    ("P5 China Pooled",  0.488, np.nan, np.nan),
    # P4 Singapore has very wide CI — show separately
]
labels = [d[0] for d in tp_data]
tps    = np.array([d[1] for d in tp_data])
lo_err = np.array([d[1] - d[2] if not np.isnan(d[2]) else 0 for d in tp_data])
hi_err = np.array([d[3] - d[1] if not np.isnan(d[3]) else 0 for d in tp_data])

fig, ax = plt.subplots(figsize=(7, 4.5))
y = np.arange(len(labels))

# P3 in navy, P5 in crimson
colors = [COLORS["base"] if "P3" in l else COLORS["accent2"] for l in labels]

ax.barh(y, tps, height=0.5, color=colors, alpha=0.75, zorder=2)
ax.errorbar(tps, y,
            xerr=[lo_err, hi_err],
            fmt="none", color="#333333", capsize=4, linewidth=1.2, zorder=3)

# Vertical reference line: 50% threshold
ax.axvline(0.5, color=COLORS["neutral"], linestyle="--", linewidth=0.9,
           alpha=0.7, label="FSTS = 50%")

ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.set_xlabel("Turning Point (FSTS — Foreign Sales Share)")
ax.set_xlim(0, 0.75)
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax.set_title("Estimated FSTS–Productivity Turning Points\n"
             "P3 Vietnam vs. P5 China (95% CI where available)", pad=10)

# Custom legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=COLORS["base"],    label="P3 Vietnam (3 waves)"),
    Patch(facecolor=COLORS["accent2"], label="P5 China (2 waves)"),
]
ax.legend(handles=legend_elements, loc="lower right", frameon=False)
ax.grid(axis="x", linestyle=":", alpha=0.4)

save_fig(fig, "fig_cross_paper_turning_points.png")


# ══════════════════════════════════════════════════════════════════════════
# FIG 2 — P3 Vietnam: inverted-U FSTS–productivity curves by wave
# ══════════════════════════════════════════════════════════════════════════
print("\n── Figure 2: P3 Vietnam inverted-U curves ───────────────")

# Coefficients from replication CSV (M2 per wave)
wave_specs = {
    "2009": {"b1":  1.045, "b2": -1.774, "mean": 0.25, "n": 989,  "tp": 0.463},
    "2015": {"b1":  1.159, "b2": -2.115, "mean": 0.22, "n": 956,  "tp": 0.393},
    "2023": {"b1":  0.889, "b2": -1.601, "mean": 0.23, "n": 1013, "tp": 0.416},
}
wave_colors = {"2009": COLORS["base"], "2015": COLORS["accent1"],
               "2023": COLORS["accent3"]}

fig, ax = plt.subplots(figsize=(7, 4.5))
fsts = np.linspace(0, 1, 200)

for yr, sp in wave_specs.items():
    fc = fsts - sp["mean"]            # centred FSTS
    lp_hat = sp["b1"] * fc + sp["b2"] * fc**2
    lp_hat -= lp_hat[0]               # normalise to zero at FSTS=0
    ax.plot(fsts, lp_hat, color=wave_colors[yr], linewidth=2,
            label=f"{yr} (N={sp['n']:,}, TP={sp['tp']:.1%})")
    ax.axvline(sp["tp"], color=wave_colors[yr], linestyle=":", linewidth=1,
               alpha=0.6)

ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("FSTS (Foreign Sales / Total Sales)")
ax.set_ylabel("Δ ln(Labour Productivity)\n(relative to FSTS = 0)")
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax.set_title("Predicted FSTS–Productivity Relationship\nP3 Vietnam (M2: Quadratic FSTS)", pad=10)
ax.legend(frameon=False)
ax.grid(linestyle=":", alpha=0.3)

save_fig(fig, "fig_p3_inverted_u_by_wave.png")


# ══════════════════════════════════════════════════════════════════════════
# FIG 3 — P4 Singapore: DAI moderation of the inverted-U
# ══════════════════════════════════════════════════════════════════════════
print("\n── Figure 3: P4 Singapore DAI moderation ────────────────")

# M4 coefficients from replication tables (2023 wave)
# FSTSc=1.182, FSTSc2=-1.048, DAI_z=0.189, FSTSc×DAI_z=-0.312, FSTSc2×DAI_z=0.421
b0_sgp = 0.0      # intercept absorbed by controls
b_fsts = 1.182
b_fsts2= -1.048
b_dai  = 0.189
b_int1 = -0.312   # FSTSc × DAI_z
b_int2 =  0.421   # FSTSc2 × DAI_z
fsts_mean_sgp = 0.28

dai_levels = {
    "Low DAI (−1 SD)":    -1.0,
    "Mean DAI (0)":         0.0,
    "High DAI (+1 SD)":    +1.0,
}
dai_colors = {
    "Low DAI (−1 SD)":  COLORS["neutral"],
    "Mean DAI (0)":     COLORS["accent1"],
    "High DAI (+1 SD)": COLORS["base"],
}

fig, ax = plt.subplots(figsize=(7, 4.5))
fsts = np.linspace(0, 1, 200)

for label, dai_val in dai_levels.items():
    fc = fsts - fsts_mean_sgp
    lp_hat = (b_fsts + b_int1 * dai_val) * fc + \
             (b_fsts2 + b_int2 * dai_val) * fc**2 + \
             b_dai * dai_val
    lp_hat -= lp_hat[0]
    ax.plot(fsts, lp_hat, color=dai_colors[label], linewidth=2,
            linestyle=("-" if dai_val == 0 else ("--" if dai_val < 0 else "-.")),
            label=label)

ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("FSTS (Foreign Sales / Total Sales)")
ax.set_ylabel("Δ ln(Labour Productivity)\n(relative to FSTS = 0)")
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax.set_title("DAI Moderation of the FSTS–Productivity Curve\n"
             "P4 Singapore 2023 (M4: Quadratic + DAI interaction)", pad=10)
ax.legend(frameon=False, title="Digital Adoption Level")
ax.grid(linestyle=":", alpha=0.3)

save_fig(fig, "fig_p4_dai_moderation.png")


# ══════════════════════════════════════════════════════════════════════════
# FIG 4 — P5 China: Turning-point stability 2012 vs 2024
# ══════════════════════════════════════════════════════════════════════════
print("\n── Figure 4: P5 China wave stability ────────────────────")

wave_specs_chn = {
    "2012": {"b1":  1.089, "b2": -1.558, "mean": 0.25, "n": 1940, "tp": 0.4937},
    "2024": {"b1":  0.943, "b2": -1.468, "mean": 0.25, "n": 2619, "tp": 0.4719},
    "Pooled": {"b1": 1.012, "b2": -1.512, "mean": 0.25, "n": 4559, "tp": 0.4878},
}
chn_colors = {"2012": COLORS["accent2"], "2024": COLORS["base"],
              "Pooled": COLORS["neutral"]}
chn_styles = {"2012": "-", "2024": "--", "Pooled": ":"}

fig, ax = plt.subplots(figsize=(7, 4.5))
fsts = np.linspace(0, 1, 200)

for yr, sp in wave_specs_chn.items():
    fc = fsts - sp["mean"]
    lp_hat = sp["b1"] * fc + sp["b2"] * fc**2
    lp_hat -= lp_hat[0]
    lw = 2.5 if yr == "Pooled" else 2.0
    ax.plot(fsts, lp_hat, color=chn_colors[yr], linewidth=lw,
            linestyle=chn_styles[yr],
            label=f"{yr} (N={sp['n']:,}, TP={sp['tp']:.1%})")
    ax.axvline(sp["tp"], color=chn_colors[yr], linestyle=":", linewidth=1,
               alpha=0.5)

ax.axhline(0, color="black", linewidth=0.5)
ax.set_xlabel("FSTS (Foreign Sales / Total Sales)")
ax.set_ylabel("Δ ln(Labour Productivity)\n(relative to FSTS = 0)")
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax.set_title("FSTS–Productivity Curve Stability: 2012 vs. 2024\n"
             "P5 China (Paternoster z = 0.82, p = .412 — no significant shift)", pad=10)
ax.legend(frameon=False)
ax.grid(linestyle=":", alpha=0.3)

save_fig(fig, "fig_p5_wave_stability.png")


# ══════════════════════════════════════════════════════════════════════════
# FIG 5 — ICRV Regime Comparison: Vietnam vs Singapore vs China turning points
# ══════════════════════════════════════════════════════════════════════════
print("\n── Figure 5: ICRV regime TP comparison ──────────────────")

regimes = {
    "Vietnam\n(ICRV Frontier V)":  (0.41, 0.34, 0.48, COLORS["accent3"]),
    "China\n(ICRV Emerging IV)":   (0.49, np.nan, np.nan, COLORS["accent2"]),
    "Singapore\n(ICRV Advanced I)":(0.89, 0.53, 2.53, COLORS["base"]),
}

fig, ax = plt.subplots(figsize=(6, 3.5))
y_pos = list(range(len(regimes)))[::-1]

for i, (label, (tp, lo, hi, color)) in enumerate(regimes.items()):
    y = y_pos[i]
    ax.plot(tp, y, "o", color=color, markersize=9, zorder=3)
    if not np.isnan(lo):
        ax.errorbar(tp, y, xerr=[[tp - lo], [min(hi, 1.5) - tp]],
                    fmt="none", color=color, capsize=5, linewidth=1.5, zorder=2)
        if hi > 1.5:
            ax.annotate("→ CI: [53%, 253%]",
                        xy=(1.52, y), xytext=(1.55, y),
                        fontsize=8, color=color, va="center")

ax.set_yticks(y_pos)
ax.set_yticklabels(list(regimes.keys()))
ax.set_xlabel("Optimal FSTS Turning Point")
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax.set_xlim(0, 1.7)
ax.set_title("FSTS–Productivity Turning Points by ICRV Regime\n"
             "(pooled-wave estimates, 95% CI where available)", pad=10)
ax.axvline(0.5, color=COLORS["neutral"], linestyle="--", linewidth=0.9,
           alpha=0.7, label="FSTS = 50%")
ax.legend(frameon=False)
ax.grid(axis="x", linestyle=":", alpha=0.4)

save_fig(fig, "fig_icrv_regime_tp_comparison.png")


print("\n" + "=" * 60)
print("  Done. All figures written to:")
print("  replication_tools/figures/")
print("=" * 60)
