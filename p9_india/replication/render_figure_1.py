#!/usr/bin/env python3
"""
P9' India — Figure 1 (Conceptual Model)

Renders the conditional inverted-U conceptual framework:
- IV: FSTS (Export Intensity), quadratic specification
- DV: lnLP (Labour Productivity)
- Moderators: TCI, DAI Tier-1, DAI Tier-2 (above main arrow)
- Institutional Scope Condition: outer dashed frame
- Controls: bottom box

Style: B&W academic publication standard, 300 DPI, serif fonts,
matching figure_2/3/4 in the same folder.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.lines import Line2D

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Academic style — matches figures 2, 3, 4
mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Liberation Serif", "serif"],
    "font.size": 9,
    "axes.linewidth": 0,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})


def draw_box(ax, x, y, w, h, text, fontsize=9, weight="normal", linestyle="-", linewidth=1.0):
    """Draw a rectangular box with centered text."""
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.02",
        linewidth=linewidth, edgecolor="black", facecolor="white",
        linestyle=linestyle,
    )
    ax.add_patch(box)
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight, wrap=True)


def draw_arrow(ax, x1, y1, x2, y2, label=None, label_offset=(0, 0.05),
               linestyle="-", arrowstyle="-|>", mutation_scale=14):
    """Draw an arrow with optional centred label."""
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=arrowstyle, mutation_scale=mutation_scale,
        linewidth=1.1, color="black", linestyle=linestyle,
    )
    ax.add_patch(arrow)
    if label:
        mx, my = (x1 + x2) / 2 + label_offset[0], (y1 + y2) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=8, style="italic",
                bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                          edgecolor="white", alpha=0.95))


def render_figure_1():
    fig = plt.figure(figsize=(7.5, 5.6))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis("off")

    # ─── Outer frame: Institutional Scope Condition (dashed) ───
    outer = Rectangle((0.25, 0.35), 9.5, 6.85,
                      linewidth=1.2, edgecolor="black",
                      facecolor="none", linestyle=(0, (6, 4)))
    ax.add_patch(outer)
    ax.text(0.45, 7.05, "INSTITUTIONAL SCOPE CONDITION (Section 2.2)",
            ha="left", va="center", fontsize=8.5, fontweight="bold",
            style="italic",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="white",
                      edgecolor="black", linewidth=0.6))

    # Scope condition explanation (top, inside frame)
    ax.text(5.0, 6.55,
            "Institutional stability (Peng et al., 2008) → inverted-U holds (2014, 2022)\n"
            "Institutional shift (demonetisation, GST, IBC, UPI, PLI, COVID, Atmanirbhar Bharat) → threshold dissolves (2025)",
            ha="center", va="center", fontsize=7.8, style="italic")

    # ─── Three capability moderators (top row inside frame) ───
    mod_y = 5.4
    # TCI
    draw_box(ax, 2.2, mod_y, 2.0, 0.85,
             "TCI\n(Technological Capability)\nz-standardised, 4 items",
             fontsize=8)
    # DAI Tier-1
    draw_box(ax, 5.0, mod_y, 2.0, 0.85,
             "DAI Tier-1\n(Private digital)\nWebsite binary",
             fontsize=8)
    # DAI Tier-2
    draw_box(ax, 7.8, mod_y, 2.0, 0.85,
             "DAI Tier-2\n(Public digital — UPI)\ne-payment share (2025 only)",
             fontsize=8)

    # ─── IV box (left) ───
    draw_box(ax, 1.4, 3.0, 1.9, 1.0,
             "EXPORT INTENSITY\n(FSTS)\n\nFSTS + FSTS²\n(quadratic specification)",
             fontsize=8.5, weight="bold", linewidth=1.4)

    # ─── DV box (right) ───
    draw_box(ax, 8.6, 3.0, 1.9, 1.0,
             "FIRM PRODUCTIVITY\n(ln Labour Productivity)\n\nln(Annual Sales / Employees)",
             fontsize=8.5, weight="bold", linewidth=1.4)

    # ─── Main IV → DV arrow ───
    draw_arrow(ax, 2.4, 3.0, 7.6, 3.0)
    # Hypothesis labels on main arrow
    ax.text(5.0, 3.32, "H1: Inverted-U\n(scope-conditional)",
            ha="center", va="center", fontsize=8, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.20", facecolor="white",
                      edgecolor="black", linewidth=0.5))
    ax.text(5.0, 2.65, "H2a (shift) vs H2b (durability) across 2014/2022/2025",
            ha="center", va="center", fontsize=7.8, style="italic")

    # ─── Moderator arrows pointing at IV→DV relationship (mid-arrow) ───
    # TCI → midpoint of IV-DV relation
    arrow1 = FancyArrowPatch((2.2, mod_y - 0.45), (3.7, 3.05),
                              arrowstyle="-|>", mutation_scale=12,
                              linewidth=1.0, color="black")
    ax.add_patch(arrow1)
    ax.text(2.85, 4.30, "H3a / H3b",
            ha="center", va="center", fontsize=7.8, style="italic",
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                      edgecolor="white", alpha=0.95))

    # DAI Tier-1 → midpoint
    arrow2 = FancyArrowPatch((5.0, mod_y - 0.45), (5.0, 3.45),
                              arrowstyle="-|>", mutation_scale=12,
                              linewidth=1.0, color="black")
    ax.add_patch(arrow2)
    ax.text(5.45, 4.30, "H4a",
            ha="center", va="center", fontsize=7.8, style="italic",
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                      edgecolor="white", alpha=0.95))

    # DAI Tier-2 → midpoint
    arrow3 = FancyArrowPatch((7.8, mod_y - 0.45), (6.3, 3.05),
                              arrowstyle="-|>", mutation_scale=12,
                              linewidth=1.0, color="black")
    ax.add_patch(arrow3)
    ax.text(7.15, 4.30, "H4b (refuted)",
            ha="center", va="center", fontsize=7.8, style="italic",
            bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                      edgecolor="white", alpha=0.95))

    # ─── Controls box (bottom inside frame) ───
    draw_box(ax, 5.0, 1.20, 6.5, 0.85,
             "CONTROL VARIABLES\nln(Employees)  •  Firm age  •  Foreign ownership (≥ 10 %)  •  State fixed effects (cluster-robust SE)",
             fontsize=8, linestyle=(0, (3, 2)), linewidth=0.9)
    # Arrow from controls to DV
    arrow_c = FancyArrowPatch((7.5, 1.45), (8.55, 2.45),
                               arrowstyle="-|>", mutation_scale=10,
                               linewidth=0.8, color="black", linestyle=(0, (3, 2)))
    ax.add_patch(arrow_c)

    # ─── Figure caption (below figure, outside the axes) ───
    fig.text(0.5, 0.02,
             "Figure 1.  Conceptual model: conditional inverted-U with capability moderation under institutional scope condition.\n"
             "Source: Authors' compilation (2026).",
             ha="center", va="bottom", fontsize=8.5, style="italic")

    # Save
    out_png = OUT / "figure_1_conceptual_model.png"
    out_pdf = OUT / "figure_1_conceptual_model.pdf"
    plt.savefig(out_png)
    plt.savefig(out_pdf)
    plt.close()
    print(f"  ✓ Figure 1 → {out_png}")
    print(f"  ✓ Figure 1 → {out_pdf}")


if __name__ == "__main__":
    print("Rendering P9' India Figure 1 (Conceptual Model)…")
    render_figure_1()
    print("Done.")
