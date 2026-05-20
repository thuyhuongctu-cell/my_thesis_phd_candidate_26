"""
Generate publication-quality conceptual model diagrams for P3, P4, P5
per the academic-conceptual-model-diagram skill.

Layout rules (avoid arrow overlap):
- IVs stacked on the left, single horizontal relationship arrow to DV on right.
- Moderators placed above/below the relationship line; moderation arrows are
  vertical (down/up) and target the relationship-line midpoint with X-mark.
- Direct effects of moderators on DV (when present) are noted in the caption
  rather than drawn as crossing diagonal arrows.
- Controls in a separate horizontal box at the bottom; single dashed arrow
  to DV (right side, avoids crossings).
- Monochrome only; rounded boxes; black edges; white fill.

Run from project root:
    python3 scripts/render_conceptual_models.py
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

FONT_SIZE = 11
LABEL_SIZE = 9
TITLE_SIZE = 12
BOX_EDGE_W = 1.2
ARROW_W = 1.1
DPI = 300

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman", "Times"],
    "font.size": FONT_SIZE,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def add_box(ax, x, y, w, h, text, *, italic=False, bold=False, fontsize=None):
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.06",
        linewidth=BOX_EDGE_W,
        edgecolor="black",
        facecolor="white",
    )
    ax.add_patch(box)
    weight = "bold" if bold else "normal"
    style = "italic" if italic else "normal"
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fontsize or FONT_SIZE,
            fontweight=weight, fontstyle=style)


def add_arrow(ax, start, end, *, dashed=False, label=None,
              label_pos="mid", label_offset=(0, 0.12), label_side="above",
              curve=0):
    style = "->,head_width=4.5,head_length=7"
    ls = "--" if dashed else "-"
    connection = f"arc3,rad={curve}" if curve else "arc3"
    a = FancyArrowPatch(
        start, end,
        arrowstyle=style,
        linewidth=ARROW_W,
        color="black",
        linestyle=ls,
        connectionstyle=connection,
        shrinkA=2,
        shrinkB=4,
    )
    ax.add_patch(a)
    if label:
        if label_pos == "start":
            t = 0.18
        elif label_pos == "end":
            t = 0.82
        else:
            t = 0.5
        mx = start[0] + (end[0] - start[0]) * t + label_offset[0]
        my = start[1] + (end[1] - start[1]) * t + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=LABEL_SIZE, fontstyle="italic")


def add_mod_arrow(ax, mod_xy, target_xy, *, label=None):
    """Moderation arrow with X-mark at target (Baron & Kenny convention)."""
    a = FancyArrowPatch(
        mod_xy, target_xy,
        arrowstyle="->,head_width=4.5,head_length=7",
        linewidth=ARROW_W,
        color="black",
        linestyle="--",
        shrinkA=2,
        shrinkB=6,
    )
    ax.add_patch(a)
    ax.plot(target_xy[0], target_xy[1],
            marker="x", color="black", markersize=10, markeredgewidth=1.6)
    if label:
        mx = (mod_xy[0] + target_xy[0]) / 2
        my = (mod_xy[1] + target_xy[1]) / 2
        side = 0.5 if target_xy[1] < mod_xy[1] else -0.5  # offset to the right of vertical arrow
        ax.text(mx + side, my, label, ha="left" if side > 0 else "right",
                va="center", fontsize=LABEL_SIZE, fontstyle="italic")


def setup_axes(width=10, height=6):
    fig, ax = plt.subplots(figsize=(width, height), dpi=DPI)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    return fig, ax


# --- Paper-specific diagrams ---

def render_p3_vietnam(path: Path):
    """P3 Vietnam (3-wave): FSTS inverted-U with TCI and DAI as moderators.
    Direct effects of TCI/DAI on ln(LP) noted in caption to avoid crossings.
    """
    fig, ax = setup_axes(width=10, height=6.5)

    ax.text(5, 6.20, "Conceptual Model — P3 Vietnam (3-wave WBES)",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")

    # IVs (left stack)
    add_box(ax, 1.7, 3.7, 2.0, 0.55, "FSTS",   bold=True)
    add_box(ax, 1.7, 2.9, 2.0, 0.55, "FSTS$^2$", bold=True)

    # DV (right)
    add_box(ax, 8.3, 3.3, 2.2, 0.85,
            "ln(LP)\nLabour Productivity", bold=True)

    # Main horizontal IV→DV relationship arrows (no crossings)
    add_arrow(ax, (2.7, 3.7), (7.2, 3.45), label="H1 (linear)",
              label_pos="mid", label_offset=(0, 0.18))
    add_arrow(ax, (2.7, 2.9), (7.2, 3.15), label="H1 (quadratic)",
              label_pos="mid", label_offset=(0, -0.20))

    # TCI moderator (top center) — moderation arrow vertical down
    add_box(ax, 5.0, 5.30, 2.4, 0.55, "TCI  (capability)", italic=True)
    add_mod_arrow(ax, (5.0, 5.0), (5.0, 3.55), label="H2")

    # DAI moderator (bottom center) — moderation arrow vertical up
    add_box(ax, 5.0, 1.30, 2.4, 0.55, "DAI  (digital adoption)", italic=True)
    add_mod_arrow(ax, (5.0, 1.60), (5.0, 3.05), label="H4 (DAI × FSTS)")

    # Controls (bottom, full width, dashed arrow to DV)
    add_box(ax, 5.0, 0.40, 7.6, 0.40,
            "Controls:  log(Emp),  FirmAge,  ForeignOwned,  sector FE,  wave FE",
            fontsize=LABEL_SIZE, italic=True)
    add_arrow(ax, (8.7, 0.60), (8.7, 2.90), dashed=True, curve=0.10)

    # Caption
    fig.text(0.5, -0.03,
             "Figure 1.  Conceptual model of the internationalisation–performance "
             "relationship in P3.  Solid arrows denote primary effects "
             "(H1 inverted-U).  Dashed arrows with × denote moderation paths "
             "(H2 capability moderation, H4 digital-adoption moderation).  "
             "TCI and DAI also enter the model as direct level-shift terms "
             "(H3 in §3.3); these direct paths are noted but omitted from "
             "the diagram to keep arrows non-overlapping.  "
             "Source: authors' own elaboration.",
             ha="center", va="top", fontsize=LABEL_SIZE, fontstyle="italic",
             wrap=True)

    plt.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print(f"  wrote {path}")


def render_p4_singapore(path: Path):
    """P4 Singapore: FSTS inverted-U, DAI as conditional scaling moderator
    (H4: positive DAI × FSTS²), TCI direct effect (H1).
    """
    fig, ax = setup_axes(width=10, height=6.5)

    ax.text(5, 6.20,
            "Conceptual Model — P4 Singapore (WBES 2023)",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")

    add_box(ax, 1.7, 3.7, 2.0, 0.55, "FSTS",   bold=True)
    add_box(ax, 1.7, 2.9, 2.0, 0.55, "FSTS$^2$", bold=True)

    add_box(ax, 8.3, 3.3, 2.2, 0.85,
            "ln(LP)\nLabour Productivity", bold=True)

    # Main relationship arrows
    add_arrow(ax, (2.7, 3.7), (7.2, 3.45), label="curvature",
              label_pos="mid", label_offset=(0, 0.18))
    add_arrow(ax, (2.7, 2.9), (7.2, 3.15))

    # TCI moderator (top) — H1 direct effect to DV (right edge horizontal)
    add_box(ax, 5.0, 5.30, 2.4, 0.55, "TCI  (capability)", italic=True)
    # Direct effect: vertical down to DV midline at a separate x-offset, then horizontal
    add_arrow(ax, (5.0, 5.0), (7.2, 3.55), label="H1 (direct)",
              label_pos="end", label_offset=(0, 0.22), curve=-0.18)

    # DAI moderator (bottom) — H3 conditional + H4 positive quadratic moderation
    add_box(ax, 5.0, 1.30, 2.4, 0.55, "DAI  (Tier 1–2 digital)", italic=True)
    add_mod_arrow(ax, (5.0, 1.60), (5.0, 3.05),
                  label="H4  (DAI × FSTS$^2$ +)")

    add_box(ax, 5.0, 0.40, 7.6, 0.40,
            "Controls:  log(Emp),  FirmAge,  ForeignOwned,  sector FE",
            fontsize=LABEL_SIZE, italic=True)
    add_arrow(ax, (8.7, 0.60), (8.7, 2.90), dashed=True, curve=0.10)

    fig.text(0.5, -0.03,
             "Figure 1.  Conceptual model of the internationalisation–performance "
             "relationship in P4.  H1 hypothesises a direct association between "
             "technological capability and labour productivity; H4 hypothesises "
             "a positive quadratic moderation of foundational digital adoption "
             "on the export-intensity curvature; H3 (conditional DAI association) "
             "is tested via the joint F-test on the DAI direct and DAI × FSTS terms.  "
             "Source: authors' own elaboration.",
             ha="center", va="top", fontsize=LABEL_SIZE, fontstyle="italic",
             wrap=True)

    plt.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print(f"  wrote {path}")


def render_p5_china(path: Path):
    """P5 China (2-wave): cross-wave durability test.
    FSTS inverted-U (H1), D_{2024} wave shift (H2a/H2b competing),
    TCI moderator (H4a curvature), DAI level-shift only, working-capital
    exploratory (H3).
    """
    fig, ax = setup_axes(width=11, height=7.5)

    ax.text(5.5, 7.20,
            "Conceptual Model — P5 China (WBES 2012 & 2024)",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")

    # IVs stacked left
    add_box(ax, 1.7, 4.4, 2.0, 0.55, "FSTS",          bold=True)
    add_box(ax, 1.7, 3.6, 2.0, 0.55, "FSTS$^2$",        bold=True)
    add_box(ax, 1.7, 2.8, 2.0, 0.55, "$D_{2024}$ (wave)", bold=True)

    add_box(ax, 9.3, 3.8, 2.3, 0.85,
            "ln(LP)\nLabour Productivity", bold=True)

    # Main horizontal arrows (no crossings)
    add_arrow(ax, (2.7, 4.4), (8.15, 4.05), label="H1 (linear)",
              label_pos="mid", label_offset=(0, 0.18))
    add_arrow(ax, (2.7, 3.6), (8.15, 3.80))
    add_arrow(ax, (2.7, 2.8), (8.15, 3.55), dashed=True,
              label="H2a / H2b  (cross-wave shift)",
              label_pos="mid", label_offset=(0.6, -0.22))

    # TCI moderator (top) — H4a curvature moderation
    add_box(ax, 5.5, 6.10, 2.6, 0.55,
            r"TCI$_{\mathrm{full}}$  (capability)", italic=True)
    add_mod_arrow(ax, (5.5, 5.80), (5.5, 3.95),
                  label="H4a  (curvature mod)")

    # DAI level-shift only (lower, simple arrow to DV)
    add_box(ax, 5.5, 1.45, 2.6, 0.55,
            r"DAI$_{\mathrm{core}}$  (Tier-1 digital)", italic=True)
    add_arrow(ax, (5.5, 1.75), (8.15, 3.55),
              label="level shift only", label_pos="end",
              label_offset=(0.0, -0.25))

    # Working-capital block (right of DAI, exploratory dashed)
    add_box(ax, 8.5, 1.45, 2.6, 0.55,
            "Working capital (H3)\nexploratory",
            italic=True, fontsize=LABEL_SIZE)
    add_arrow(ax, (8.5, 1.75), (8.5, 3.4), dashed=True,
              label="H3 exploratory",
              label_pos="mid", label_offset=(0.5, 0))

    # Controls (bottom)
    add_box(ax, 5.5, 0.45, 8.5, 0.40,
            "Controls:  log(Emp),  FirmAge,  ForeignOwned;  "
            "cluster-robust SE on $idstd$",
            fontsize=LABEL_SIZE, italic=True)

    fig.text(0.5, -0.03,
             "Figure 1.  Conceptual model of P5: bounded internationalisation–"
             "performance relationship and cross-wave threshold stability in "
             "Chinese private firms.  H1 specifies the inverted-U curvature.  "
             "H2a and H2b are competing predictions about the cross-wave "
             "behaviour of the curvature (shift vs. structural durability).  "
             "H4a tests technological-capability moderation of the curvature.  "
             "DAI is retained as a level-shift control; H3 working-capital "
             "conditioning is exploratory.  Source: authors' own elaboration.",
             ha="center", va="top", fontsize=LABEL_SIZE, fontstyle="italic",
             wrap=True)

    plt.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print(f"  wrote {path}")


def main():
    base = Path(__file__).resolve().parent.parent / "manuscripts" / "figures"
    targets = [
        ("P3 Vietnam",
         base / "p3_vietnam" / "figure_1_conceptual_model.png",
         render_p3_vietnam),
        ("P4 Singapore",
         base / "p4_singapore" / "figure_1_conceptual_model.png",
         render_p4_singapore),
        ("P5 China",
         base / "p5_china" / "figure_1_conceptual_model.png",
         render_p5_china),
    ]
    for label, path, fn in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"[render] {label}")
        fn(path)


if __name__ == "__main__":
    main()
