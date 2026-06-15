"""
Generate conceptual model figures for dissertation papers P3, P4, P5, P6, and CD2.
Applies standards from conceptual-model-international-business skill:
  - Theory-first design with clear IV/DV/moderator roles
  - Publication-quality (≥300 DPI, grayscale-compatible, serif fonts)
  - Proper figure captions following Q1-Q2 journal standards
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe
import numpy as np
import os

# ── Style constants ─────────────────────────────────────────────────────────
FONT = 'DejaVu Serif'
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['DejaVu Serif', 'Times New Roman', 'Georgia'],
    'font.size': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.bottom': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

COL_IV   = '#2C3E50'   # Dark navy — independent variables
COL_DV   = '#1A5276'   # Deep blue — dependent variable
COL_MOD  = '#5D6D7E'   # Medium slate — moderators
COL_CTRL = '#909497'   # Light gray — controls
COL_ARR  = '#2C3E50'   # Arrow color
EDGE_W   = 1.5

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..')


def box(ax, x, y, w, h, text, color=COL_IV, fontsize=9, bold=False, wrap=True):
    """Draw a rounded rectangle box with centered text."""
    fancy = FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.02",
        linewidth=EDGE_W, edgecolor=color,
        facecolor='white'
    )
    ax.add_patch(fancy)
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight=weight, color=color,
            wrap=True, multialignment='center')


def arrow(ax, x1, y1, x2, y2, label='', color=COL_ARR, style='solid', lw=1.5):
    """Draw an arrow between two points with an optional label."""
    linestyle = '--' if style == 'dashed' else '-'
    ax.annotate('',
                xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(
                    arrowstyle='->', color=color,
                    lw=lw, linestyle=linestyle,
                    connectionstyle='arc3,rad=0.0'
                ))
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my + 0.02, label, ha='center', va='bottom',
                fontsize=8, color=color, fontstyle='italic')


def curved_arrow(ax, x1, y1, x2, y2, label='', rad=0.3, color=COL_MOD, lw=1.5):
    """Draw a curved arrow (for moderation paths)."""
    ax.annotate('',
                xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(
                    arrowstyle='->', color=color, lw=lw,
                    linestyle='--',
                    connectionstyle=f'arc3,rad={rad}'
                ))
    if label:
        mx = (x1 + x2) / 2 + 0.05 * np.sign(rad)
        my = (y1 + y2) / 2
        ax.text(mx, my, label, ha='center', va='center',
                fontsize=8, color=color, fontstyle='italic')


# ══════════════════════════════════════════════════════════════════════════════
# P3 — Vietnam Conceptual Model
# ══════════════════════════════════════════════════════════════════════════════
def make_p3_conceptual_model(outdir):
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')

    # ── Main IV → DV spine ──
    box(ax, 0.18, 0.60, 0.28, 0.14,
        'Internationalization\n(FSTS, FSTS²_c)\nN = 24,782 firms\n3 waves: 2009/2015/2023',
        color=COL_IV, fontsize=8, bold=True)

    box(ax, 0.80, 0.60, 0.26, 0.14,
        'Firm Performance\nln(Labour Productivity)\nln(Revenue PPP / Workers)',
        color=COL_DV, fontsize=8, bold=True)

    arrow(ax, 0.33, 0.60, 0.67, 0.60,
          'H1: Inverted-U (β₁>0, β₂<0)\nTP ≈ 39–46% FSTS')

    # ── Moderator 1: TCI ──
    box(ax, 0.50, 0.88, 0.28, 0.12,
        'Technological Capability (TCI)\nISO · R&D · Foreign tech ·\nImported machinery\n[H2: Direct + Moderation]',
        color=COL_MOD, fontsize=7.5)

    curved_arrow(ax, 0.50, 0.82, 0.80, 0.68, label='H2 (+)', rad=-0.25, color=COL_MOD)
    ax.annotate('', xy=(0.50, 0.68), xytext=(0.50, 0.82),
                arrowprops=dict(arrowstyle='->', color=COL_MOD, lw=1.3, linestyle='--'))
    ax.text(0.50, 0.75, 'H2 (level-shift)', ha='center', fontsize=7.5,
            color=COL_MOD, fontstyle='italic')

    # ── Moderator 2: DAI ──
    box(ax, 0.50, 0.28, 0.28, 0.12,
        'Digital Adoption (DAI)\nTier-1: Website presence (c22b)\n[Exploratory: H4]',
        color=COL_MOD, fontsize=7.5)

    curved_arrow(ax, 0.50, 0.34, 0.80, 0.53, label='H4 (exploratory)', rad=0.25, color=COL_MOD)
    ax.annotate('', xy=(0.50, 0.52), xytext=(0.50, 0.34),
                arrowprops=dict(arrowstyle='->', color=COL_MOD, lw=1.3, linestyle='--'))

    # ── Controls box ──
    box(ax, 0.18, 0.28, 0.28, 0.12,
        'Controls\nfirm size · age · foreign own\nsector FE · wave FE · country FE',
        color=COL_CTRL, fontsize=7.5)
    ax.annotate('', xy=(0.67, 0.57), xytext=(0.33, 0.28),
                arrowprops=dict(arrowstyle='->', color=COL_CTRL, lw=1.0, linestyle=':'))

    # ── ICRV context label ──
    ax.text(0.50, 0.07,
            'ICRV Context: Vietnam — Frontier V | Theory: Uppsala + RBV + Institutional Theory',
            ha='center', va='center', fontsize=8, color='#566573',
            style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDFEFE', edgecolor='#AEB6BF', lw=0.8))

    ax.set_title('Figure 1. Conceptual Model — Vietnam (P3)', fontsize=11,
                 fontweight='bold', pad=10, color=COL_IV)

    out = os.path.join(outdir, 'p3/figures/vietnam/figure_1_conceptual_model.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# P4 — Singapore Conceptual Model
# ══════════════════════════════════════════════════════════════════════════════
def make_p4_conceptual_model(outdir):
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')

    # ── IV ──
    box(ax, 0.18, 0.60, 0.28, 0.16,
        'Internationalization\n(FSTS, FSTS²_c)\nN = 623 firms\nWBES Singapore 2023',
        color=COL_IV, fontsize=8, bold=True)

    # ── DV ──
    box(ax, 0.80, 0.60, 0.26, 0.14,
        'Firm Performance\nln(Labour Productivity)\nln(Revenue PPP / Workers)',
        color=COL_DV, fontsize=8, bold=True)

    arrow(ax, 0.33, 0.60, 0.67, 0.60,
          'H1: Inverted-U tendency\nTP ~88.6% FSTS (CI: 53–253%)')

    # ── TCI — direct effect ──
    box(ax, 0.18, 0.20, 0.28, 0.14,
        'Technological Capability (TCI)\nISO · R&D · Foreign tech · Machinery\n[H1-TCI: Direct level-shift]',
        color=COL_MOD, fontsize=7.5)
    arrow(ax, 0.33, 0.20, 0.67, 0.53,
          'H1-TCI (+)', color=COL_MOD)

    # ── DAI — conditional moderator ──
    box(ax, 0.50, 0.90, 0.30, 0.14,
        'Digital Adoption (DAI)\nTier-1+2: Website + E-payment\n[H2: Direct | H3: FSTS×DAI]',
        color=COL_MOD, fontsize=7.5)

    # DAI direct effect
    curved_arrow(ax, 0.65, 0.90, 0.80, 0.68,
                 label='H2 (non-uniform +)', rad=-0.2, color=COL_MOD)

    # DAI × FSTS moderation — the key hypothesis
    ax.annotate('', xy=(0.50, 0.66), xytext=(0.50, 0.83),
                arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.8, linestyle='--'))
    ax.text(0.52, 0.75, 'H3: FSTS×DAI\n(amplification at high FSTS)', ha='left',
            fontsize=7.5, color='#C0392B', fontstyle='italic')

    # ── Heckman selection note ──
    box(ax, 0.50, 0.10, 0.34, 0.10,
        'Heckman IMR check: Selection bias test\n(Exporter selection controlled)',
        color=COL_CTRL, fontsize=7.5)

    # ── Controls ──
    ax.text(0.80, 0.20,
            'Controls: firm size, age,\nforeign own, sector FE\nHeckman IMR (sensitivity)',
            ha='center', va='center', fontsize=7.5, color=COL_CTRL,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#FDFEFE', edgecolor='#BDC3C7', lw=0.8))

    ax.text(0.50, 0.03,
            'ICRV Context: Singapore — Advanced I | Theory: RBV + Dynamic Capabilities + Institutional Theory',
            ha='center', va='center', fontsize=8, color='#566573', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDFEFE', edgecolor='#AEB6BF', lw=0.8))

    ax.set_title('Figure 1. Conceptual Model — Singapore (P4)', fontsize=11,
                 fontweight='bold', pad=10, color=COL_IV)

    out = os.path.join(outdir, 'p4/figures/p4_singapore/figure_1_conceptual_model.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# P5 — China Conceptual Model
# ══════════════════════════════════════════════════════════════════════════════
def make_p5_conceptual_model(outdir):
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')

    # ── IV ──
    box(ax, 0.16, 0.62, 0.26, 0.16,
        'Internationalization\n(FSTS, FSTS²_c)\n2012: N=2,610 | 2024: N=1,940\nPooled panel: 217 firms',
        color=COL_IV, fontsize=7.8, bold=True)

    # ── DV ──
    box(ax, 0.81, 0.62, 0.24, 0.14,
        'Firm Performance\nln(Labour Productivity)\nln(Revenue PPP / Workers)',
        color=COL_DV, fontsize=8, bold=True)

    arrow(ax, 0.30, 0.62, 0.69, 0.62,
          'H1: Inverted-U (β₁>0, β₂<0)\nTP 2012≈49.4%, 2024≈47.2%')

    # ── TCI — stronger moderator in China ──
    box(ax, 0.50, 0.90, 0.30, 0.12,
        'Technological Capability (TCI)\nISO · R&D · Foreign tech · Machinery\n[H2: Direct + moderation]',
        color=COL_MOD, fontsize=7.5)

    curved_arrow(ax, 0.65, 0.90, 0.81, 0.69, label='H2 (+)', rad=-0.25, color=COL_MOD)
    ax.annotate('', xy=(0.50, 0.68), xytext=(0.50, 0.84),
                arrowprops=dict(arrowstyle='->', color=COL_MOD, lw=1.3, linestyle='--'))
    ax.text(0.52, 0.76, 'TCI×FSTS (+)', ha='left', fontsize=7.5, color=COL_MOD, fontstyle='italic')

    # ── DAI — thin Tier-1, control only ──
    box(ax, 0.16, 0.25, 0.26, 0.12,
        'Digital Adoption (DAI-thin)\nTier-1: Website (c22b)\n[Control — not moderator in CN]',
        color=COL_CTRL, fontsize=7.5)
    ax.annotate('', xy=(0.69, 0.58), xytext=(0.30, 0.27),
                arrowprops=dict(arrowstyle='->', color=COL_CTRL, lw=1.0, linestyle=':'))

    # ── Temporal heterogeneity (H6) ──
    box(ax, 0.80, 0.23, 0.26, 0.14,
        'Temporal Heterogeneity (H6)\nWave 2012 vs 2024\nPaternoster z=0.82 (p=.412)\nTP stable: Δ≈2.2 pp',
        color='#6C3483', fontsize=7.5)
    ax.annotate('', xy=(0.81, 0.55), xytext=(0.81, 0.37),
                arrowprops=dict(arrowstyle='->', color='#6C3483', lw=1.3, linestyle='--'))
    ax.text(0.83, 0.46, 'Stability\ntest', ha='left', fontsize=7.5, color='#6C3483', fontstyle='italic')

    # ── Sample attrition note ──
    ax.text(0.50, 0.06,
            'ICRV Context: China — Emerging IV | Theory: Uppsala + RBV + Organizational Learning\n'
            'Note: 2,610→1,940 attrition (−26%) verified; 217-firm panel sub-sample identified',
            ha='center', va='center', fontsize=7.5, color='#566573', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDFEFE', edgecolor='#AEB6BF', lw=0.8))

    ax.set_title('Figure 1. Conceptual Model — China (P5)', fontsize=11,
                 fontweight='bold', pad=10, color=COL_IV)

    out = os.path.join(outdir, 'p5/figures/figure_1_conceptual_model.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# P6 — Meta-Analysis MARA Conceptual Model
# ══════════════════════════════════════════════════════════════════════════════
# Design principles (meta-analysis-internationalization-performance skill):
#   - Show the conceptual I→P relationship, not just meta-analytic statistics
#   - Ground ALL moderators in published theory (no unpublished framework names)
#   - No citations to unpublished manuscripts
#   - Three-level MARA as method note only (not IV/DV labels)
def make_p6_conceptual_model(outdir):
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')

    # ── IV: Internationalization ──
    box(ax, 0.13, 0.60, 0.24, 0.22,
        'Internationalization\n(Primary Studies)\nFSTS · Geographic scope\nEntropy index · DOI\nNumber of countries\nk = 235 effect sizes\n89 primary studies (1977–2024)',
        color=COL_IV, fontsize=7.6, bold=True)

    # ── DV: Firm Performance ──
    box(ax, 0.86, 0.60, 0.24, 0.18,
        'Firm Performance\n(Primary Studies)\nROA · ROE · ROS\nTobin\'s Q · Firm value\nSales growth',
        color=COL_DV, fontsize=7.6, bold=True)

    # ── Main focal arrow ──
    arrow(ax, 0.26, 0.63, 0.74, 0.63,
          'H0: I→P positive (r̄ = 0.07; 95% CI [0.042, 0.102])\nHigh heterogeneity (I² = 87.92%) → moderation analysis')

    # ── Moderator 1: Country Digital Infrastructure (cDAI) ──
    # Grounded in: Goldfarb & Tucker (2019); IMF (2023) digital economy; WB DAI
    box(ax, 0.50, 0.92, 0.32, 0.13,
        'Country Digital Infrastructure (cDAI)\nITU ICT Development Index · WB Digital Adoption\n[H1: Higher cDAI → stronger I→P (+)]\n[Digital economy: Goldfarb & Tucker 2019]',
        color=COL_MOD, fontsize=7.3)
    curved_arrow(ax, 0.65, 0.92, 0.86, 0.70, label='H1 (+)', rad=-0.2, color=COL_MOD)
    ax.annotate('', xy=(0.50, 0.69), xytext=(0.50, 0.86),
                arrowprops=dict(arrowstyle='->', color=COL_MOD, lw=1.3, linestyle='--'))

    # ── Moderator 2: Institutional Context (ICRV Regime) ──
    # Grounded in: North (1990); Scott (1995); Peng, Wang & Jiang (2008)
    box(ax, 0.13, 0.23, 0.28, 0.20,
        'Institutional Context\n(ICRV Regime — 5 levels)\nAdvanced-I → Frontier-V\n[H2: Gradient effect:\nAdvanced > Emerging > Frontier]\n[Institutional Theory:\nNorth 1990; Peng et al. 2008]',
        color='#1E8449', fontsize=7.3)
    curved_arrow(ax, 0.27, 0.33, 0.73, 0.57, label='H2 (gradient)', rad=0.25, color='#1E8449')

    # ── Moderator 3: Study Period (Temporal Moderation) ──
    # Grounded in: Cohen & Levinthal (1990) absorptive capacity; Rogers (2003) diffusion
    box(ax, 0.86, 0.23, 0.25, 0.20,
        'Study Period\n(Temporal Moderation)\nPre-2009 · 2009–2015 · Post-2015\n[H3: Post-2009 positive shift]\n[Absorptive capacity:\nCohen & Levinthal 1990;\nDiffusion: Rogers 2003]',
        color='#6C3483', fontsize=7.3)
    ax.annotate('', xy=(0.86, 0.55), xytext=(0.86, 0.43),
                arrowprops=dict(arrowstyle='->', color='#6C3483', lw=1.3, linestyle='--'))
    ax.text(0.88, 0.49, 'H3 (+)', ha='left', fontsize=7.5, color='#6C3483', fontstyle='italic')

    # ── cDAI × Study Period interaction (H4) ──
    ax.annotate('', xy=(0.71, 0.43), xytext=(0.53, 0.88),
                arrowprops=dict(arrowstyle='->', color='#884EA0', lw=1.2, linestyle=':',
                                connectionstyle='arc3,rad=0.28'))
    ax.text(0.57, 0.65, 'H4: cDAI × Period\n(interaction)', ha='center', fontsize=7.3,
            color='#884EA0', fontstyle='italic')

    # ── Publication bias controls ──
    box(ax, 0.50, 0.08, 0.40, 0.10,
        'Publication Bias Controls: Egger\'s regression test · Trim-and-fill · PET-PEESE\n'
        'Sensitivity: Leave-one-out · Subgroup by database · High-quality studies only',
        color=COL_CTRL, fontsize=7.2)

    # ── Method + theory note (published bases only) ──
    ax.text(0.50, 0.01,
            'Theoretical bases: Resource-Based View (Barney 1991) · Institutional Theory (North 1990; Scott 1995; Peng et al. 2008) · '
            'Organizational Learning (Cohen & Levinthal 1990)\n'
            'Method: Three-level MARA (random effects; σ²₂ within-study, σ²₃ between-study) | Target: International Business Review',
            ha='center', va='bottom', fontsize=6.8, color='#566573', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDFEFE', edgecolor='#AEB6BF', lw=0.8))

    ax.set_title('Figure 1. Conceptual Model — Three-Level MARA: Internationalization–Performance (P6)',
                 fontsize=11, fontweight='bold', pad=12, color=COL_IV)

    out = os.path.join(outdir, 'p6/figures/figure_1_conceptual_model.png')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# CD2 — Integrated Conceptual Framework (Hình 2.1)
# ══════════════════════════════════════════════════════════════════════════════
def make_cd2_conceptual_model(outdir):
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')

    # ── Core I→P spine ──
    box(ax, 0.14, 0.55, 0.22, 0.18,
        'Internationalization (I)\nFSTS · FSTS²_c · FSTS³_c\nWBES d3c/100\nN = 101,185 firms\n47 economies',
        color=COL_IV, fontsize=7.5, bold=True)

    box(ax, 0.86, 0.55, 0.22, 0.16,
        'Firm Performance (P)\nln(Labour Productivity)\nln(Revenue PPP / Workers)',
        color=COL_DV, fontsize=8, bold=True)

    arrow(ax, 0.26, 0.55, 0.75, 0.55,
          'H1: Inverted-U / S-curve  (β₁>0, β₂<0)\nTP gradient: Frontier V → Advanced I')

    # ── H2: TCI (RBV) ──
    box(ax, 0.50, 0.92, 0.24, 0.12,
        'TCI — Technological Capability\nISO · R&D · Foreign tech · Machinery\n[H2: RBV — Direct + Moderation (+)]',
        color='#1A5276', fontsize=7.5)
    curved_arrow(ax, 0.62, 0.92, 0.86, 0.64, label='H2 (+)', rad=-0.2, color='#1A5276')
    ax.annotate('', xy=(0.50, 0.64), xytext=(0.50, 0.86),
                arrowprops=dict(arrowstyle='->', color='#1A5276', lw=1.3, linestyle='--'))
    ax.text(0.52, 0.75, 'level-shift', ha='left', fontsize=7, color='#1A5276', fontstyle='italic')

    # ── H3: DAI — CDCM (Digital Capability Lens) ──
    box(ax, 0.50, 0.25, 0.26, 0.14,
        'DAI — Digital Adoption (CDCM)\nTier-1: Website · Tier-2: E-payment\n[H3: Conditional scaling resource\nRegime × FSTS interaction]',
        color='#117A65', fontsize=7.5)
    curved_arrow(ax, 0.63, 0.25, 0.86, 0.47, label='H3 (conditional)', rad=0.2, color='#117A65')
    ax.annotate('', xy=(0.50, 0.45), xytext=(0.50, 0.32),
                arrowprops=dict(arrowstyle='->', color='#117A65', lw=1.3, linestyle='--'))

    # ── H4: Manager characteristics (Upper Echelons) ──
    box(ax, 0.14, 0.20, 0.22, 0.14,
        'Manager Characteristics (H4)\nExperience (b5) · Education (b7a)\nGender (b7)\n[Upper Echelons Theory]',
        color='#6C3483', fontsize=7.5)
    curved_arrow(ax, 0.26, 0.27, 0.75, 0.48, label='H4 (+)', rad=0.15, color='#6C3483')

    # ── H5: ICRV Regime (Institutional Theory) ──
    box(ax, 0.86, 0.20, 0.22, 0.16,
        'ICRV Regime (H5)\nI: Advanced-Innovation\nII: Advanced-Resource\nIII–VI: Frontier\n[Institutional Theory]',
        color='#1E8449', fontsize=7.5)
    ax.annotate('', xy=(0.86, 0.47), xytext=(0.86, 0.36),
                arrowprops=dict(arrowstyle='->', color='#1E8449', lw=1.3, linestyle='--'))
    ax.text(0.88, 0.415, 'H5\ngradient', ha='left', fontsize=7, color='#1E8449', fontstyle='italic')

    # ── H6: Temporal Heterogeneity ──
    ax.text(0.50, 0.07,
            'H6 — Temporal Heterogeneity: Year-bucket FE (2009–12 | 2013–17 | 2018–25)\n'
            '[Proposed temporal phases grounded in Cohen & Levinthal 1990; Rogers 2003 diffusion theory]',
            ha='center', va='center', fontsize=7.8, color='#884EA0', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#F9EBFF', edgecolor='#C39BD3', lw=0.8))

    # ── Controls ──
    ax.text(0.50, 0.52,
            'Controls: ln(emp), firm_age, foreign_own,\nsector FE, country FE, year FE',
            ha='center', va='center', fontsize=7, color=COL_CTRL,
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#F8F9FA', edgecolor='#BDC3C7', lw=0.7))

    # ── Theory layer legend ──
    legend_items = [
        mpatches.Patch(facecolor='white', edgecolor='#1A5276', label='RBV — TCI (H2)'),
        mpatches.Patch(facecolor='white', edgecolor='#117A65', label='Digital Capability (DAI/CDCM — proposed lens) (H3)'),
        mpatches.Patch(facecolor='white', edgecolor='#6C3483', label='Upper Echelons — Manager (H4)'),
        mpatches.Patch(facecolor='white', edgecolor='#1E8449', label='Institutional Theory — ICRV (H5)'),
        mpatches.Patch(facecolor='white', edgecolor=COL_IV, label='Uppsala Model — H1 (I→P nonlinear)'),
    ]
    ax.legend(handles=legend_items, loc='upper left', fontsize=7,
              framealpha=0.9, edgecolor='#D5D8DC', ncol=1,
              bbox_to_anchor=(0.01, 0.99))

    ax.set_title('Hình 2.1. Khung khái niệm tích hợp CĐ2 — Mô hình nghiên cứu đề xuất\n'
                 '(H1–H6 · Năm tầng lý thuyết · 101,185 doanh nghiệp · 47 nền kinh tế)',
                 fontsize=10.5, fontweight='bold', pad=12, color=COL_IV)

    out = os.path.join(outdir, 'chuyen_de/cd2/figures/hinh_2_1_khung_khai_niem.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# CD2 — CDCM Mechanism Detail (Hình 2.2)
# ══════════════════════════════════════════════════════════════════════════════
def make_cd2_cdcm_detail(outdir):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.5))

    regimes = [
        ('Advanced I\n(Singapore)', '#1A5276',
         'DAI Tier-1+2 = conditional\nscaling resource\nHigh digital saturation\n→ DAI amplifies FSTS×P\nat high export intensity\nCoeff: FSTS²×DAI = +3.119\n(P4 Singapore)'),
        ('Emerging IV\n(China)', '#117A65',
         'DAI Tier-1 = selection proxy\nMedium digital saturation\n→ OLS: DAI positive\n→ IV-corrected: null\n→ Selection bias\nconfounds OLS estimate\n(P5 China)'),
        ('Frontier V\n(Vietnam)', '#C0392B',
         'DAI Tier-1 = measurement\nconstraint (website only)\nLow digital saturation\n→ DAI exploratory probe\n→ Wave-specific signals\n→ Not main hypothesis\n(P3 Vietnam)'),
    ]

    for ax, (regime, color, detail) in zip(axes, regimes):
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        ax.axis('off')

        # Regime header
        fancy = FancyBboxPatch((0.05, 0.75), 0.90, 0.20,
                               boxstyle='round,pad=0.03',
                               linewidth=2, edgecolor=color, facecolor='white')
        ax.add_patch(fancy)
        ax.text(0.50, 0.85, regime, ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=color)

        # Detail box
        fancy2 = FancyBboxPatch((0.05, 0.08), 0.90, 0.63,
                                boxstyle='round,pad=0.03',
                                linewidth=1.2, edgecolor=color,
                                facecolor='#FDFEFE', alpha=0.8)
        ax.add_patch(fancy2)
        ax.text(0.50, 0.40, detail, ha='center', va='center',
                fontsize=8, color='#2C3E50', multialignment='center')

        # Arrow from header to detail
        ax.annotate('', xy=(0.50, 0.71), xytext=(0.50, 0.75),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.5))

    fig.suptitle('Hình 2.2. Cơ chế CDCM theo ba nhóm ICRV\n'
                 'Context-Contingent Digital Capability Model — DAI role varies by regime',
                 fontsize=10, fontweight='bold', color=COL_IV, y=1.01)

    out = os.path.join(outdir, 'chuyen_de/cd2/figures/hinh_2_2_cdcm_detail.png')
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# CD1 — Descriptive analytical framework (Hình 2.3.1.1)
# Correlational / descriptive (NOT hypothesis-testing): four firm/country factors
# vs standardized labour productivity, contextualised by ICRV regime over time.
# Faithful to CĐ1 §2.3.8 (Pearson correlations) and §2.3.9 (synthesis).
# ══════════════════════════════════════════════════════════════════════════════
def make_cd1_conceptual_model(outdir):
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')

    # ── Four explanatory factors (left, stacked) ──
    factors = [
        (0.80, 'FDI ≥ 10%\n(b2b)', 'r = +0,06 … +0,12'),
        (0.62, 'Quốc tế hóa — FSTS\n(d3b + d3c)', 'r = +0,139 → −0,009 (SIDS)'),
        (0.44, 'TCI — Năng lực công nghệ\n(R&D h8 · ISO b8)', 'r = +0,117 … +0,240'),
        (0.26, 'DAI — Hiện diện số\n(website c22b)', 'r = +0,090 … +0,201'),
    ]
    for y, label, rng in factors:
        box(ax, 0.15, y, 0.24, 0.12, label, color=COL_IV, fontsize=7.6, bold=True)
        arrow(ax, 0.275, y, 0.71, 0.44, color=COL_ARR, lw=1.0)
        ax.text(0.30, y + 0.052, rng, ha='left', va='bottom',
                fontsize=6.6, color='#34495E', fontstyle='italic')

    # ── Dependent variable (right) ──
    box(ax, 0.85, 0.44, 0.24, 0.17,
        'Năng suất lao động (LP-z)\nz-score ln(doanh thu / lao động)\ntrong từng nền × năm\n(bất biến tiền tệ)',
        color=COL_DV, fontsize=8, bold=True)

    # ── ICRV regime — cross-cutting contextual moderator (top) ──
    box(ax, 0.50, 0.93, 0.60, 0.10,
        'Bối cảnh thể chế — 6 nhóm ICRV (I Đổi mới → VI SIDS)\n'
        'điều tiết ĐỘ LỚN và (cá biệt) DẤU của các tương quan',
        color='#1E8449', fontsize=7.8, bold=True)
    ax.annotate('', xy=(0.62, 0.54), xytext=(0.62, 0.88),
                arrowprops=dict(arrowstyle='->', color='#1E8449', lw=1.4, linestyle='--'))
    ax.text(0.635, 0.71, 'điều tiết bối cảnh\n(gradient thể chế)', ha='left', va='center',
            fontsize=7, color='#1E8449', fontstyle='italic')

    # ── Key descriptive readings (annotation, below the factor stack) ──
    ax.text(0.50, 0.115,
            'Phát hiện mô tả: (i) TCI là tương quan dương mạnh & đồng đều nhất (level-shifter phổ quát); '
            '(ii) gradient FSTS giảm đơn điệu theo thể chế\nyếu dần, mất ý nghĩa/đổi dấu ở SIDS '
            '(giả thuyết chi phí buộc phải quốc tế hóa); (iii) phần bù DAI thấp nhất ở Nhóm I (bão hòa Tier-1)',
            ha='center', va='center', fontsize=6.7, color='#2C3E50',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#F8F9FA', edgecolor='#BDC3C7', lw=0.7))

    # ── Temporal dimension (bottom) ──
    ax.text(0.50, 0.03,
            'Chiều thời gian 2006–2026: nhảy vọt số Tier-1 (+21…+31 điểm % website ở nhóm IV/V/VI) · '
            'tái cân bằng GVC\n(mô tả cắt-ngang gộp nhiều đợt; quan hệ nhân quả dành cho Chuyên đề 2)',
            ha='center', va='center', fontsize=7.0, color='#7D6608', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF9E7', edgecolor='#D4AC0D', lw=0.8))

    ax.set_title('Hình 2.3.1.1. Khung phân tích mô tả CĐ1 — Tương quan giữa bốn yếu tố và năng suất lao động\n'
                 'theo bối cảnh thể chế ICRV (pool mô tả 88.869 doanh nghiệp · 50 nền · 2006–2026)',
                 fontsize=10, fontweight='bold', pad=12, color=COL_IV)

    out = os.path.join(outdir, 'chuyen_de/cd1/figures/cd1_fig_conceptual_model.png')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {out}')


# ══════════════════════════════════════════════════════════════════════════════
# Run all
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    base = OUTPUT_DIR
    print('Generating conceptual model figures...\n')
    make_p3_conceptual_model(base)
    make_p4_conceptual_model(base)
    make_p5_conceptual_model(base)
    make_p6_conceptual_model(base)
    make_cd1_conceptual_model(base)
    make_cd2_conceptual_model(base)
    make_cd2_cdcm_detail(base)
    print('\n✓ All 7 conceptual model figures generated at 300 DPI.')
