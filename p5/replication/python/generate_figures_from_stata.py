"""
P5 China — Publication-ready figure generation
Reads p5/replication/results/results_coefs.csv and produces three figures:
  Figure 1: Inverted-U curves (2012, 2024, pooled) with TP annotations
  Figure 2: Turning-point comparison with 95% CI error bars
  Figure 3: Paternoster z-test coefficient stability visualization

All figures follow academic style suitable for IBR / JIBS submission.

Usage:
    python generate_figures_from_stata.py [--outdir OUTDIR]

Default output: p5/replication/figures/
"""

import argparse
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(SCRIPT_DIR, "..", "results")
COEFS_CSV = os.path.join(RESULTS_DIR, "results_coefs.csv")
DEFAULT_OUTDIR = os.path.join(SCRIPT_DIR, "..", "figures")

# ── Turning-point CIs from delta method (summary.md) ──────────────────────
# Hardcoded from verified Python pipeline output (matches manuscript ±0.4 pp)
TP_CI = {
    "2012":   {"tp": 0.4937, "ci_lo": 0.4317, "ci_hi": 0.5557, "N": 2610},
    "2024":   {"tp": 0.4719, "ci_lo": 0.3446, "ci_hi": 0.5992, "N": 1934},
    "pooled": {"tp": 0.4878, "ci_lo": 0.4265, "ci_hi": 0.5491, "N": 4544},
}

# Paternoster z-test results (from summary.md)
PATERNOSTER = {
    "FSTS":   {"b_2012":  2.065, "se_2012": 0.379,
               "b_2024":  1.498, "se_2024": 0.578,
               "z": 0.821, "p": 0.412},
    "FSTSsq": {"b_2012": -2.092, "se_2012": 0.435,
               "b_2024": -1.587, "se_2024": 0.712,
               "z": -0.605, "p": 0.545},
}

# ── Academic style ─────────────────────────────────────────────────────────
WAVE_COLORS  = {"2012": "#2c7bb6", "2024": "#d7191c", "pooled": "#1a9641"}
WAVE_LABELS  = {"2012": "2012 (N=2,610)", "2024": "2024 (N=1,934)",
                "pooled": "Pooled (N=4,544)"}
WAVE_ORDER   = ["2012", "2024", "pooled"]

def set_academic_style():
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
        "axes.grid":         True,
        "grid.alpha":        0.35,
        "grid.linestyle":    "--",
        "lines.linewidth":   1.8,
    })


def load_m2_coefs(df: pd.DataFrame) -> dict:
    """Extract M2 FSTS and FSTSsq coefficients per wave."""
    m2 = df[df["model"] == "M2"].copy()
    coefs = {}
    for wave in WAVE_ORDER:
        sub = m2[m2["wave"] == wave]
        fsts_row    = sub[sub["var"] == "FSTS"]
        fstssq_row  = sub[sub["var"] == "FSTSsq"]
        if fsts_row.empty or fstssq_row.empty:
            raise ValueError(f"M2 coefficients not found for wave '{wave}'")
        coefs[wave] = {
            "b1":    float(fsts_row["coef"].iloc[0]),
            "se_b1": float(fsts_row["se"].iloc[0]),
            "b2":    float(fstssq_row["coef"].iloc[0]),
            "se_b2": float(fstssq_row["se"].iloc[0]),
            "N":     int(fsts_row["N"].iloc[0]),
        }
    return coefs


def partial_effect(fsts_grid, b1, b2):
    """Partial effect of FSTS on ln(LP): y = b1*x + b2*x^2."""
    return b1 * fsts_grid + b2 * fsts_grid ** 2


def partial_se(fsts_grid, se_b1, se_b2):
    """Approximate SE of partial effect (ignoring covariance term)."""
    return np.sqrt((fsts_grid * se_b1) ** 2 + (fsts_grid ** 2 * se_b2) ** 2)


# ── Figure 1: Inverted-U curves ────────────────────────────────────────────

def fig_inverted_u(coefs: dict, outdir: str):
    set_academic_style()
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5), sharey=False)
    fig.suptitle(
        "Figure 1. Estimated FSTS–Labour Productivity Relationship (M2, P5 China)",
        fontsize=12, y=1.01,
    )

    fsts_grid = np.linspace(0, 1, 300)

    for ax, wave in zip(axes, WAVE_ORDER):
        c   = coefs[wave]
        b1, b2, se1, se2 = c["b1"], c["b2"], c["se_b1"], c["se_b2"]
        tp  = TP_CI[wave]

        y    = partial_effect(fsts_grid, b1, b2)
        y_se = partial_se(fsts_grid, se1, se2)

        color = WAVE_COLORS[wave]

        # Shaded 95% CI band
        ax.fill_between(
            fsts_grid * 100, (y - 1.96 * y_se), (y + 1.96 * y_se),
            alpha=0.15, color=color, label="_nolegend_",
        )
        # Main curve
        ax.plot(fsts_grid * 100, y, color=color, linewidth=2)

        # Turning-point vertical line
        tp_pct = tp["tp"] * 100
        ax.axvline(tp_pct, color=color, linestyle=":", linewidth=1.5, alpha=0.9)

        # TP CI bracket (horizontal span below the curve trough)
        y_min = y.min() - 0.05 * (y.max() - y.min())
        ci_lo_pct = tp["ci_lo"] * 100
        ci_hi_pct = tp["ci_hi"] * 100
        ax.annotate(
            "",
            xy=(ci_hi_pct, y_min), xytext=(ci_lo_pct, y_min),
            arrowprops=dict(arrowstyle="<->", color=color, lw=1.2),
        )
        ax.text(
            tp_pct, y_min - 0.01,
            f"TP = {tp_pct:.1f}%\n[{ci_lo_pct:.1f}%, {ci_hi_pct:.1f}%]",
            ha="center", va="top", fontsize=8, color=color,
        )

        # Reference line at y=0
        ax.axhline(0, color="grey", linewidth=0.8, linestyle="-", alpha=0.5)

        label_str = WAVE_LABELS[wave] if wave != "pooled" else "Pooled (N=4,544)"
        ax.set_title(label_str, fontsize=10)
        ax.set_xlabel("Export Intensity (FSTS, %)", fontsize=9)
        ax.set_ylabel("Partial effect on ln(Labour Productivity)", fontsize=9)
        ax.set_xlim(0, 100)

    fig.tight_layout()
    out_path = os.path.join(outdir, "figure1_inverted_u.pdf")
    fig.savefig(out_path)
    png_path = out_path.replace(".pdf", ".png")
    fig.savefig(png_path)
    print(f"  Saved: {out_path}")
    print(f"  Saved: {png_path}")
    plt.close(fig)


# ── Figure 2: Turning-point comparison ────────────────────────────────────

def fig_turning_points(outdir: str):
    set_academic_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    waves  = WAVE_ORDER
    labels = ["2012\n(N=2,610)", "2024\n(N=1,934)", "Pooled\n(N=4,544)"]
    tps    = [TP_CI[w]["tp"] * 100   for w in waves]
    lo_err = [TP_CI[w]["tp"] * 100 - TP_CI[w]["ci_lo"] * 100 for w in waves]
    hi_err = [TP_CI[w]["ci_hi"] * 100 - TP_CI[w]["tp"] * 100 for w in waves]
    colors = [WAVE_COLORS[w] for w in waves]

    x = np.arange(len(waves))
    bars = ax.bar(x, tps, color=colors, width=0.5, alpha=0.85, zorder=3)
    ax.errorbar(
        x, tps,
        yerr=[lo_err, hi_err],
        fmt="none", color="black", capsize=6, capthick=1.5, linewidth=1.5, zorder=4,
    )

    # Annotate TP values
    for xi, tp, lo, hi in zip(x, tps, lo_err, hi_err):
        ax.text(
            xi, tp + hi + 0.8,
            f"{tp:.1f}%",
            ha="center", va="bottom", fontsize=9, fontweight="bold",
        )

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Turning Point (% FSTS)", fontsize=10)
    ax.set_title(
        "Figure 2. Turning-Point Estimates Across Waves\n"
        "(M2; error bars = 95% CI, delta method)",
        fontsize=11,
    )
    ax.set_ylim(0, 80)
    ax.axhline(50, color="grey", linestyle="--", linewidth=0.9, alpha=0.6,
               label="50% reference")
    ax.legend(fontsize=8)

    fig.tight_layout()
    out_path = os.path.join(outdir, "figure2_turning_points.pdf")
    fig.savefig(out_path)
    png_path = out_path.replace(".pdf", ".png")
    fig.savefig(png_path)
    print(f"  Saved: {out_path}")
    print(f"  Saved: {png_path}")
    plt.close(fig)


# ── Figure 3: Paternoster z-test (cross-wave stability) ───────────────────

def fig_paternoster(outdir: str):
    set_academic_style()
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))
    fig.suptitle(
        "Figure 3. Cross-Wave Coefficient Stability (Paternoster z-test, M2)",
        fontsize=12, y=1.02,
    )

    coef_vars  = ["FSTS", "FSTSsq"]
    panel_titles = ["(a) FSTS (linear term)", "(b) FSTSsq (quadratic term)"]

    for ax, var, ptitle in zip(axes, coef_vars, panel_titles):
        p = PATERNOSTER[var]
        b_vals  = [p["b_2012"],  p["b_2024"]]
        se_vals = [p["se_2012"], p["se_2024"]]
        labels  = ["2012", "2024"]
        colors  = [WAVE_COLORS["2012"], WAVE_COLORS["2024"]]
        x       = np.array([0, 1])

        for xi, bv, sv, lbl, col in zip(x, b_vals, se_vals, labels, colors):
            ax.errorbar(
                xi, bv, yerr=1.96 * sv,
                fmt="o", color=col, markersize=9, capsize=8, capthick=2,
                linewidth=2, label=f"{lbl}: β = {bv:.3f} (SE = {sv:.3f})",
                zorder=4,
            )

        # Connect the two point estimates with a dashed line
        ax.plot(x, b_vals, linestyle="--", color="grey", linewidth=1.0,
                alpha=0.6, zorder=2)

        ax.axhline(0, color="black", linewidth=0.8, linestyle="-", alpha=0.4)
        ax.set_xticks(x)
        ax.set_xticklabels(["2012", "2024"], fontsize=10)
        ax.set_ylabel("Coefficient estimate (β)", fontsize=9)
        ax.set_title(
            f"{ptitle}\nz = {p['z']:.3f}, p = {p['p']:.3f} "
            f"({'stable' if p['p'] > 0.10 else 'unstable'})",
            fontsize=10,
        )
        ax.legend(fontsize=8, loc="best")

        # Annotate stability verdict
        verdict_color = "#1a9641" if p["p"] > 0.10 else "#d7191c"
        verdict_text  = "p > 0.10 → equality NOT rejected\nCoefficients stable across waves"
        ax.text(
            0.5, 0.05, verdict_text,
            transform=ax.transAxes,
            ha="center", va="bottom", fontsize=8,
            color=verdict_color,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor=verdict_color, alpha=0.8),
        )

    fig.tight_layout()
    out_path = os.path.join(outdir, "figure3_paternoster.pdf")
    fig.savefig(out_path)
    png_path = out_path.replace(".pdf", ".png")
    fig.savefig(png_path)
    print(f"  Saved: {out_path}")
    print(f"  Saved: {png_path}")
    plt.close(fig)


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate P5 publication figures")
    parser.add_argument("--outdir", default=DEFAULT_OUTDIR,
                        help="Output directory for figures (default: p5/replication/figures/)")
    args = parser.parse_args()

    outdir = os.path.normpath(args.outdir)
    os.makedirs(outdir, exist_ok=True)

    if not os.path.isfile(COEFS_CSV):
        print(f"ERROR: results_coefs.csv not found at {COEFS_CSV}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(COEFS_CSV)
    required_cols = {"model", "var", "coef", "se", "N", "wave"}
    missing = required_cols - set(df.columns)
    if missing:
        print(f"ERROR: results_coefs.csv missing columns: {missing}", file=sys.stderr)
        sys.exit(1)

    coefs = load_m2_coefs(df)

    print(f"\nGenerating figures → {outdir}")
    print("  M2 coefficients loaded:")
    for wave, c in coefs.items():
        tp_pct = (-c["b1"] / (2 * c["b2"])) * 100
        print(f"    {wave:6s}: FSTS={c['b1']:+.4f}  FSTSsq={c['b2']:+.4f}  "
              f"TP={tp_pct:.2f}%  N={c['N']}")

    print()
    fig_inverted_u(coefs, outdir)
    fig_turning_points(outdir)
    fig_paternoster(outdir)
    print("\nDone. 6 files written (PDF + PNG for each figure).")


if __name__ == "__main__":
    main()
