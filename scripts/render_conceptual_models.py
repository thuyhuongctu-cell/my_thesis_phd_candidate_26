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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
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
    """Rectangle (with rounded corners) for observed/measured variables."""
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


def add_ellipse(ax, x, y, w, h, text, *, italic=False, bold=False, fontsize=None):
    """Ellipse for latent constructs (formative/reflective composites).

    Per the conceptual-model-scopus-wos skill: ellipse shapes denote latent
    constructs not directly observed (e.g. TCI and DAI here are formative
    composites of WBES item indicators).
    """
    e = Ellipse((x, y), w, h,
                linewidth=BOX_EDGE_W,
                edgecolor="black",
                facecolor="white")
    ax.add_patch(e)
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
    """P3 Vietnam (3-wave): FSTS inverted-U with TCI and DAI as latent
    moderators (ellipses for formative composites; rectangles for observed
    FSTS/FSTS²/ln(LP)).  Sign markers (+/-) on arrows per Scopus/WoS
    conceptual-model convention.
    """
    fig, ax = setup_axes(width=10, height=6.5)

    ax.text(5, 6.20, "Conceptual Model — P3 Vietnam (3-wave WBES)",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")

    # IVs (left stack — observed)
    add_box(ax, 1.7, 3.7, 2.0, 0.55, "FSTS",   bold=True)
    add_box(ax, 1.7, 2.9, 2.0, 0.55, "FSTS$^2$", bold=True)

    # DV (right — observed)
    add_box(ax, 8.3, 3.3, 2.2, 0.85,
            "ln(LP)\nLabour Productivity", bold=True)

    # Main horizontal IV→DV relationship arrows with signed labels
    add_arrow(ax, (2.7, 3.7), (7.2, 3.45),
              label="H1a  (+)",
              label_pos="mid", label_offset=(0, 0.18))
    add_arrow(ax, (2.7, 2.9), (7.2, 3.15),
              label="H1b  (−)",
              label_pos="mid", label_offset=(0, -0.20))

    # TCI moderator — latent (ellipse), moderation arrow vertical down
    add_ellipse(ax, 5.0, 5.30, 2.6, 0.7, "TCI\n(capability)", italic=True)
    add_mod_arrow(ax, (5.0, 4.95), (5.0, 3.55),
                  label="H2  (+ flattening)")

    # DAI moderator — latent (ellipse), moderation arrow vertical up
    add_ellipse(ax, 5.0, 1.30, 2.6, 0.7, "DAI\n(digital adoption)", italic=True)
    add_mod_arrow(ax, (5.0, 1.65), (5.0, 3.05),
                  label="H4  (− 2023 obsolescence)")

    # Controls
    add_box(ax, 5.0, 0.40, 7.6, 0.40,
            "Controls:  log(Emp),  FirmAge,  ForeignOwned,  sector FE,  wave FE",
            fontsize=LABEL_SIZE, italic=True)
    add_arrow(ax, (8.7, 0.60), (8.7, 2.90), dashed=True, curve=0.10)

    fig.text(0.5, -0.03,
             "Figure 1.  Conceptual model of P3 (Vietnam, 3-wave WBES).  "
             "Rectangles denote observed (measured) variables; ellipses denote "
             "latent formative composites (TCI, DAI).  Sign markers indicate "
             "the expected direction of association: H1a (+) linear FSTS, "
             "H1b (−) quadratic curvature, H2 (+) capability flattening of the "
             "post-threshold downturn, H4 (−) Tier-1 DAI×FSTS interaction "
             "(consistent with Tier-1 proxy obsolescence in 2023).  Direct "
             "level-shift roles of TCI and DAI (H3) are tested in the regression "
             "but omitted from the diagram for clarity.  Source: authors' own "
             "elaboration.",
             ha="center", va="top", fontsize=LABEL_SIZE, fontstyle="italic",
             wrap=True)

    plt.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print(f"  wrote {path}")


def render_p4_singapore(path: Path):
    """P4 Singapore: FSTS inverted-U + TCI direct (H1) + DAI conditional
    (H3) and positive DAI × FSTS² moderation (H4).  Latent constructs
    drawn as ellipses; signed arrows per Scopus/WoS conventions.
    """
    fig, ax = setup_axes(width=10, height=6.5)

    ax.text(5, 6.20,
            "Conceptual Model — P4 Singapore (WBES 2023)",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")

    # IVs (observed)
    add_box(ax, 1.7, 3.7, 2.0, 0.55, "FSTS",   bold=True)
    add_box(ax, 1.7, 2.9, 2.0, 0.55, "FSTS$^2$", bold=True)

    # DV (observed)
    add_box(ax, 8.3, 3.3, 2.2, 0.85,
            "ln(LP)\nLabour Productivity", bold=True)

    # Main relationship arrows with sign markers
    add_arrow(ax, (2.7, 3.7), (7.2, 3.45),
              label="(+) linear",
              label_pos="mid", label_offset=(0, 0.18))
    add_arrow(ax, (2.7, 2.9), (7.2, 3.15),
              label="(−) curvature",
              label_pos="mid", label_offset=(0, -0.20))

    # TCI latent moderator (top); H1 direct association to DV
    add_ellipse(ax, 5.0, 5.30, 2.6, 0.7, "TCI\n(capability)", italic=True)
    add_arrow(ax, (5.0, 4.95), (7.2, 3.55),
              label="H1  (+)",
              label_pos="end", label_offset=(0, 0.22), curve=-0.18)

    # DAI latent moderator (bottom); H4 positive quadratic moderation
    add_ellipse(ax, 5.0, 1.30, 2.6, 0.7,
                "DAI\n(Tier 1+2 digital)", italic=True)
    add_mod_arrow(ax, (5.0, 1.65), (5.0, 3.05),
                  label="H4  (+ DAI × FSTS$^2$)")

    add_box(ax, 5.0, 0.40, 7.6, 0.40,
            "Controls:  log(Emp),  FirmAge,  ForeignOwned,  sector FE",
            fontsize=LABEL_SIZE, italic=True)
    add_arrow(ax, (8.7, 0.60), (8.7, 2.90), dashed=True, curve=0.10)

    fig.text(0.5, -0.03,
             "Figure 1.  Conceptual model of P4 (Singapore, WBES 2023).  "
             "Rectangles denote observed variables; ellipses denote latent "
             "formative composites.  Sign markers indicate the expected "
             "direction of association: linear FSTS (+), quadratic curvature "
             "(−), H1 capability direct effect on productivity (+), H4 "
             "positive quadratic moderation of DAI on the export-intensity "
             "curvature (consistent with conditional digital complementarity).  "
             "H3 (conditional DAI–productivity association) is tested via the "
             "joint F-test on the DAI direct and DAI × FSTS interaction terms.  "
             "Source: authors' own elaboration.",
             ha="center", va="top", fontsize=LABEL_SIZE, fontstyle="italic",
             wrap=True)

    plt.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print(f"  wrote {path}")


def render_p5_china(path: Path):
    """P5 China (2-wave): cross-wave durability test.
    Latent ellipses for TCI_full and DAI_core; signed and dashed arrows
    per Scopus/WoS convention.  H2a/H2b drawn as a single dashed arrow
    labelled with competing predictions.
    """
    fig, ax = setup_axes(width=11, height=7.5)

    ax.text(5.5, 7.20,
            "Conceptual Model — P5 China (WBES 2012 & 2024)",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")

    # IVs stacked left (observed)
    add_box(ax, 1.7, 4.4, 2.0, 0.55, "FSTS",            bold=True)
    add_box(ax, 1.7, 3.6, 2.0, 0.55, "FSTS$^2$",          bold=True)
    add_box(ax, 1.7, 2.8, 2.0, 0.55, "$D_{2024}$ (wave)", bold=True)

    add_box(ax, 9.3, 3.8, 2.3, 0.85,
            "ln(LP)\nLabour Productivity", bold=True)

    # Main horizontal arrows
    add_arrow(ax, (2.7, 4.4), (8.15, 4.05),
              label="H1a  (+)",
              label_pos="mid", label_offset=(0, 0.18))
    add_arrow(ax, (2.7, 3.6), (8.15, 3.80),
              label="H1b  (−)",
              label_pos="mid", label_offset=(0, -0.20))
    # H2a (shift) vs H2b (durability): dashed arrow because the directional
    # prediction is contested.
    add_arrow(ax, (2.7, 2.8), (8.15, 3.55), dashed=True,
              label="H2a / H2b  (shift  vs.  durability)",
              label_pos="mid", label_offset=(0.6, -0.22))

    # TCI latent moderator (top) — H4a curvature moderation
    add_ellipse(ax, 5.5, 6.10, 2.8, 0.7,
                r"TCI$_{\mathrm{full}}$" + "\n(capability)", italic=True)
    add_mod_arrow(ax, (5.5, 5.75), (5.5, 3.95),
                  label="H4a  (curvature mod)")

    # DAI latent level-shift only (no curvature moderation hypothesis)
    add_ellipse(ax, 5.5, 1.45, 2.8, 0.7,
                r"DAI$_{\mathrm{core}}$" + "\n(Tier-1 digital)", italic=True)
    add_arrow(ax, (5.5, 1.80), (8.15, 3.55),
              label="(+) level shift", label_pos="end",
              label_offset=(0.0, -0.25))

    # Working-capital block (right of DAI, exploratory dashed)
    add_box(ax, 8.5, 1.45, 2.6, 0.55,
            "Working capital  (H3)\nexploratory",
            italic=True, fontsize=LABEL_SIZE)
    add_arrow(ax, (8.5, 1.75), (8.5, 3.4), dashed=True,
              label="H3  (?) exploratory",
              label_pos="mid", label_offset=(0.5, 0))

    # Controls (bottom)
    add_box(ax, 5.5, 0.45, 8.5, 0.40,
            "Controls:  log(Emp),  FirmAge,  ForeignOwned;  "
            "cluster-robust SE on $idstd$",
            fontsize=LABEL_SIZE, italic=True)

    fig.text(0.5, -0.03,
             "Figure 1.  Conceptual model of P5 (China, WBES 2012 and 2024).  "
             "Rectangles denote observed variables; ellipses denote latent "
             "formative composites.  H1a (+) and H1b (−) jointly specify the "
             "inverted-U.  H2a and H2b are competing predictions about the "
             "cross-wave behaviour of the curvature (shift vs. structural "
             "durability), drawn as a single dashed arrow because the "
             "direction is contested.  H4a tests technological-capability "
             "moderation of the curvature.  $\\mathrm{DAI}_{\\text{core}}$ "
             "enters as a level-shift control; H3 working-capital "
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
