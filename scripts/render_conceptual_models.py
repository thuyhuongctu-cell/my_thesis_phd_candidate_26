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


def render_dissertation_cimt_layered(path: Path):
    """Conceptual model for the dissertation — articulating the core
    theoretical contribution rather than enumerating hypotheses.

    Design philosophy (deep IB-scholar lens):
      - The theoretical contribution is the RELOCATED-OPTIMUM thesis:
        capability-institution mismatch deforms the I-P curve along
        a regime gradient. The diagram should show this *mechanism*,
        not list 15 boxes-and-arrows.
      - Three-stage causal chain (left -> right):
          [Capability × Institution]  =>  [CIMT 3 channels]
                                      =>  [I-P curve + relocated optimum]
      - CDCM (digital adoption) enters as a curve-shifting force from
        below, NOT as a parallel moderator (because in this dissertation,
        CDCM is positioned as the *observable signature* of CIMT under
        digital conditions; the cross-layer link IS the contribution).
      - H4 controls in a small bottom strip (one line; not a focal point).
      - Hypothesis labels (H1-H6) appear only where they anchor a specific
        causal arrow, not as decorative tags.
    """
    fig, ax = setup_axes(width=12.5, height=7.0)

    # Title
    ax.text(6.25, 6.78,
            "Conceptual Model — Capability-Institution Mismatch (CIMT) "
            "and the Relocated Optimum",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")
    ax.text(6.25, 6.42,
            "How firm capability × home-country institution jointly determine "
            "where internationalization pays",
            ha="center", va="center", fontsize=LABEL_SIZE - 1, fontstyle="italic")

    # ===== STAGE 1: Capability × Institution (left) =====
    # Capability composite
    add_box(ax, 1.55, 5.10, 2.3, 0.55,
            "Firm capability\n(TCI · DAI)", bold=True, fontsize=9)
    # Institution composite
    add_box(ax, 1.55, 3.40, 2.3, 0.55,
            "Home-country institution\n(ICRV Groups I–VI)",
            bold=True, fontsize=9)
    # "X" mismatch operator between them
    ax.text(1.55, 4.30, "×",
            ha="center", va="center", fontsize=22, fontweight="bold",
            color="black")
    ax.text(2.55, 4.30, "match /\nmismatch",
            ha="left", va="center", fontsize=7.5, fontstyle="italic",
            color="#444444")

    # ===== STAGE 2: CIMT mechanism (center) =====
    # Mechanism wrapper title (text only — no box)
    ax.text(6.25, 5.65,
            "Capability-Institution Mismatch (CIMT)",
            ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(6.25, 5.32,
            "middle-range integrative mechanism (Merton, 1968; Whetten, 1989; "
            "Corley & Gioia, 2011)",
            ha="center", va="center", fontsize=7, fontstyle="italic",
            color="#555555")

    # 3 channel arrows — DIRECTIONAL (each shows + / − contribution to payoff)
    # Channel arrow 1 — rent protection (strengthens with strong institutions)
    ax.text(5.05, 4.55, "+", fontsize=18, fontweight="bold",
            ha="center", va="center", color="black")
    ax.text(5.50, 4.55,
            "Rent protection\n(Kogut & Zander, 1993; Zaheer, 1995)",
            ha="left", va="center", fontsize=8)

    # Channel arrow 2 — LoF attenuation (strengthens with transparent institutions)
    ax.text(5.05, 4.05, "+", fontsize=18, fontweight="bold",
            ha="center", va="center", color="black")
    ax.text(5.50, 4.05,
            "LoF attenuation\n(Peng et al., 2008; Zaheer, 1995)",
            ha="left", va="center", fontsize=8)

    # Channel arrow 3 — institutional-void amplification (weakens with weak institutions)
    ax.text(5.05, 3.55, "−", fontsize=18, fontweight="bold",
            ha="center", va="center", color="black")
    ax.text(5.50, 3.55,
            "Institutional-void amplification\n(Khanna & Palepu, 1997, 2010)",
            ha="left", va="center", fontsize=8)

    # Arrow from STAGE 1 to STAGE 2 (capability×institution => CIMT)
    a_s1_s2 = FancyArrowPatch(
        (2.75, 4.30), (4.70, 4.05),
        arrowstyle="-|>,head_width=4.5,head_length=8",
        linewidth=1.3, color="black",
        shrinkA=4, shrinkB=4,
    )
    ax.add_patch(a_s1_s2)
    ax.text(3.70, 4.55, "interaction\nproduces",
            ha="center", va="center", fontsize=7, fontstyle="italic",
            color="#444444")

    # ===== STAGE 3: I-P outcome (right) — the relocated-optimum signature =====
    # Outcome label
    ax.text(10.55, 5.65,
            "I-P payoff: relocated optimum",
            ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(10.55, 5.32,
            "(curve shape, turning-point location)",
            ha="center", va="center", fontsize=7, fontstyle="italic",
            color="#555555")

    # I-P curve sub-icon — show 3 stylised regime curves
    _draw_ip_curves_subicon(ax, x0=8.85, y0=3.35, w=3.40, h=1.70)

    # Arrow from STAGE 2 to STAGE 3 (CIMT => I-P payoff)
    a_s2_s3 = FancyArrowPatch(
        (7.80, 4.05), (8.85, 4.20),
        arrowstyle="-|>,head_width=4.5,head_length=8",
        linewidth=1.3, color="black",
        shrinkA=4, shrinkB=4,
    )
    ax.add_patch(a_s2_s3)
    ax.text(8.30, 4.50, "shapes",
            ha="center", va="center", fontsize=7, fontstyle="italic",
            color="#444444")

    # ===== CDCM cross-layer modifier (from below, into Stage 2-3 boundary) =====
    add_box(ax, 7.10, 1.85, 4.5, 0.50,
            "CDCM: digital-for-institutional substitution\n"
            "DAI × ICRV (p = .049) — observable signature at firm level",
            italic=True, fontsize=8)
    # Curved dashed arrow from CDCM up into Stage 2 (mechanism reshape)
    a_cdcm = FancyArrowPatch(
        (7.10, 2.10), (5.50, 3.30),
        arrowstyle="-|>,head_width=4.0,head_length=6",
        linewidth=0.9, color="black", linestyle="--",
        connectionstyle="arc3,rad=-0.25",
        shrinkA=4, shrinkB=4,
    )
    ax.add_patch(a_cdcm)

    # ===== H4 Upper Echelons controls (small bottom strip) =====
    ax.text(0.25, 0.55,
            "Endogenous controls (H4): manager experience · education · "
            "female top management  (Upper Echelons; Hambrick & Mason, 1984)",
            ha="left", va="center", fontsize=7.5, fontstyle="italic",
            color="#444444")

    # ===== H1b boundary condition (small bottom strip) =====
    ax.text(0.25, 0.95,
            "H1b boundary condition: in extreme mismatch (Pacific SIDS, ICRV VI), "
            "the inverted-U collapses to a monotone negative relationship "
            "(Forced Internationalization Penalty).",
            ha="left", va="center", fontsize=7.5, fontstyle="italic",
            color="#444444")

    # Source line
    ax.text(12.25, 0.20,
            "Source: authors' own elaboration",
            ha="right", va="center", fontsize=7, fontstyle="italic",
            color="#444444")

    # Caption
    fig.text(
        0.5, -0.04,
        "Figure 2.1.  Conceptual model articulating the dissertation's central "
        "theoretical claim: the I-P relationship is universal in inverted-U form "
        "(H1) but its turning-point location is jointly determined by firm "
        "capability and home-country institutional regime. The CIMT mechanism "
        "synthesises three established channels through which capability-"
        "institution match shapes the payoff to internationalization: rent "
        "protection and LoF attenuation strengthen the payoff in strong "
        "institutional environments; institutional-void amplification erodes it "
        "in weak ones. The I-P curve in the right panel is therefore *relocated* "
        "along the ICRV institutional gradient — flat-positive in Advanced "
        "regimes (I-II), classical inverted-U in Upper-middle / Emerging regimes "
        "(III-IV), and (under the H1b boundary condition) monotone negative in "
        "Pacific SIDS (VI). Foundational digital adoption (DAI) acts as an "
        "observable signature of the substitution mechanism at the firm level "
        "(CDCM; H6: DAI × ICRV, p = .049): where institutions are weak, "
        "foundational digital infrastructure partly substitutes for the "
        "contract-enforcement and market-information functions that strong "
        "institutions otherwise supply.",
        ha="center", va="top", fontsize=LABEL_SIZE - 1, fontstyle="italic",
        wrap=True,
    )

    plt.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print(f"  wrote {path}")


def _draw_ip_curves_subicon(ax, x0, y0, w, h):
    """Draw 3 stylised I-P regime curves inside a [x0,x0+w] x [y0,y0+h]
    box, illustrating the 'relocated optimum' visually.
    Used by render_dissertation_cimt_layered.
    """
    import numpy as np
    # Frame
    frame = FancyBboxPatch(
        (x0, y0), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.04",
        facecolor="white", edgecolor="black", linewidth=1.0,
    )
    ax.add_patch(frame)

    # Axes labels
    ax.text(x0 + w / 2, y0 - 0.18, "FSTS",
            ha="center", va="center", fontsize=7.5,
            color="#333333", fontstyle="italic")
    ax.text(x0 - 0.18, y0 + h / 2, "ln(LP)",
            ha="center", va="center", fontsize=7.5,
            color="#333333", fontstyle="italic", rotation=90)

    # Parametric x (0..1 in FSTS units)
    xs = np.linspace(0.02, 0.98, 100)

    # Curve 1: Advanced regime (I-II) — flat-positive, near-linear
    ys1 = 0.40 + 0.55 * xs - 0.10 * xs ** 2
    ax.plot(x0 + xs * w, y0 + ys1 * h, "-", linewidth=1.4, color="black")
    ax.text(x0 + 0.93 * w, y0 + ys1[-1] * h + 0.05, "I-II",
            ha="left", va="bottom", fontsize=7, fontstyle="italic")

    # Curve 2: Upper-mid / Emerging regime (III-IV) — classical inverted-U, TP ~ 0.40
    ys2 = 0.20 + 2.0 * xs - 2.5 * xs ** 2
    ax.plot(x0 + xs * w, y0 + ys2 * h, "-", linewidth=1.4, color="black")
    ax.text(x0 + 0.42 * w, y0 + max(ys2) * h + 0.04, "III-IV",
            ha="center", va="bottom", fontsize=7, fontstyle="italic")

    # Curve 3: Pacific SIDS / FIP (VI) — monotone negative
    ys3 = 0.65 - 0.55 * xs
    ax.plot(x0 + xs * w, y0 + ys3 * h, "--", linewidth=1.4, color="black")
    ax.text(x0 + 0.62 * w, y0 + ys3[60] * h - 0.07, "VI (FIP)",
            ha="left", va="top", fontsize=7, fontstyle="italic")


def render_dissertation_unified(path: Path):
    """Unified dissertation conceptual model (CDCM).
    Context-Contingent Digital-and-Capability Model integrating
    all five moderating conditions across P3-P8.
    Three moderator ellipses (TCI, ICRV, DAI) each send a moderation
    arrow (dashed, X-mark) to the FSTS–performance relationship arrow.
    DAI×ICRV substitution is shown by a double-headed dashed line.
    Upper Echelons controls (H4) in a bottom box with dashed arrow to DV.
    """
    fig, ax = setup_axes(width=11.5, height=7.6)

    # Title
    ax.text(5, 7.38,
            "Unified Conceptual Model — Internationalization & Firm Performance",
            ha="center", va="center", fontsize=TITLE_SIZE, fontweight="bold")

    # Theory strip
    ax.text(5, 6.92,
            "Theoretical anchors:  Uppsala · RBV · Institutional Theory · "
            "Upper Echelons · Digital Capability (CDCM)",
            ha="center", va="center", fontsize=LABEL_SIZE - 1, fontstyle="italic")

    # IVs (left — observed)
    add_box(ax, 1.6, 4.60, 2.0, 0.55, "FSTS", bold=True)
    add_box(ax, 1.6, 3.72, 2.0, 0.55, r"FSTS$^2$", bold=True)
    ax.text(1.6, 5.05, "inverted-U  (turning pt ≈ 36%)",
            ha="center", va="center", fontsize=7, fontstyle="italic", color="#555555")

    # DV (right)
    add_box(ax, 8.85, 4.16, 2.3, 0.95,
            "ln(LP)\nFirm Performance", bold=True)

    # --- Main arrows IV → DV ---
    # H1a: FSTS → ln(LP)
    add_arrow(ax, (2.60, 4.60), (7.70, 4.32),
              label="H1a  (+)",
              label_pos="mid", label_offset=(0, 0.22))
    # H1b: FSTS² → ln(LP)
    add_arrow(ax, (2.60, 3.72), (7.70, 4.00),
              label="H1b  (−)",
              label_pos="mid", label_offset=(0, -0.23))
    # H1b SIDS/FIP boundary condition note
    ax.text(4.15, 3.35,
            "H1b boundary: SIDS/FIP → negative monotonic",
            ha="center", va="center", fontsize=7, fontstyle="italic", color="#444444")

    # --- TCI moderator (top centre, level-shift) ---
    add_ellipse(ax, 5.0, 6.35, 2.6, 0.70,
                "TCI\n(Technological Capability)", italic=True)
    add_mod_arrow(ax, (5.0, 6.00), (5.0, 4.32),
                  label="H2  (level-shift ↑)")

    # --- ICRV moderator (bottom-left, concavity/amplitude) ---
    add_ellipse(ax, 2.35, 1.90, 2.55, 0.70,
                "ICRV\n(Institutional Regime I–VI)", italic=True)
    add_mod_arrow(ax, (2.35, 2.25), (3.45, 4.14),
                  label="H5  (concavity/amplitude)")

    # --- DAI moderator (bottom-right, context-contingent) ---
    add_ellipse(ax, 7.65, 1.90, 2.55, 0.70,
                "DAI\n(Digital Adoption)", italic=True)
    add_mod_arrow(ax, (7.65, 2.25), (6.55, 4.14),
                  label="H3  (context-contingent)")

    # --- DAI × ICRV substitution (double-headed dashed line) ---
    a_sub = FancyArrowPatch(
        (3.63, 1.90), (6.37, 1.90),
        arrowstyle="<->,head_width=4.5,head_length=7",
        linewidth=1.0,
        color="black",
        linestyle="--",
        shrinkA=2,
        shrinkB=2,
    )
    ax.add_patch(a_sub)
    ax.text(5.0, 1.50,
            r"DAI$\times$ICRV  substitution ($p$ = .049)",
            ha="center", va="center", fontsize=LABEL_SIZE - 1, fontstyle="italic")

    # --- Upper Echelons controls (bottom) ---
    add_box(ax, 5.0, 0.55, 8.8, 0.52,
            "Upper Echelons Controls (H4):  "
            "Manager Experience  ·  Education  ·  Female",
            fontsize=LABEL_SIZE - 1, italic=True)
    add_arrow(ax, (9.3, 0.81), (9.3, 3.68), dashed=True, curve=0.12)

    # Caption
    fig.text(
        0.5, -0.04,
        "Hình 2.1 / Figure 2.1.  Unified Conceptual Model (CDCM — Context-Contingent "
        "Digital-and-Capability Model) integrating P3–P8. Rectangles denote observed "
        "variables; ellipses denote latent formative composites. H1a (+) and H1b (−) "
        "jointly specify the inverted-U export-intensity–performance relationship "
        "(turning point ≈ 36%; H1b boundary: SIDS/FIP — negative monotonic). "
        "H2 TCI raises the curve (level-shift). H3 DAI reshapes the curve in a "
        "context-contingent manner. H5 ICRV deepens concavity/amplitude under weak "
        "institutions. The double-headed dashed arrow denotes digital-for-institutional "
        "substitution (DAI×ICRV interaction, p = .049). Upper Echelons manager "
        "characteristics enter as controls (H4). Source: authors' own elaboration.",
        ha="center", va="top", fontsize=LABEL_SIZE - 1, fontstyle="italic",
        wrap=True,
    )

    plt.savefig(path, dpi=DPI, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print(f"  wrote {path}")


def main():
    base = Path(__file__).resolve().parent.parent / "manuscripts" / "figures"
    thesis_figs = Path(__file__).resolve().parent.parent / "thesis" / "figures"
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
        ("Dissertation Unified (CDCM legacy)",
         thesis_figs / "figure_conceptual_model_unified.png",
         render_dissertation_unified),
        ("Dissertation Layered (CIMT-ICRV-CDCM)",
         thesis_figs / "figure_conceptual_model_cimt_layered.png",
         render_dissertation_cimt_layered),
    ]
    for label, path, fn in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"[render] {label}")
        fn(path)


if __name__ == "__main__":
    main()
