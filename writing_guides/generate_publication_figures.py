#!/usr/bin/env python3
"""
Generate publication-quality figures for all dissertation papers (P3, P4, P5, P7, P8).

Produces:
  - Conceptual model diagrams (black-and-white, boxes-and-arrows)
  - Inverted-U / FIP regression curves from actual coefficients
  - Institutional gradient / temporal evolution comparisons

Outputs saved to: p3/figures/, p4/figures/, p5/figures/, p7/figures/, p8/figures/
Run from repo root: python3 writing_guides/generate_publication_figures.py
"""
import os, csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.lines import Line2D

# ── repo root (script is in writing_guides/) ──────────────────────────────────
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def fig_dir(paper):
    d = os.path.join(REPO, paper, 'figures')
    os.makedirs(d, exist_ok=True)
    return d

def save(fig, path):
    fig.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  saved → {os.path.relpath(path, REPO)}")

# ── academic style ────────────────────────────────────────────────────────────
STYLE = {
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
}
plt.rcParams.update(STYLE)

# ── colour / line style palette (print-safe) ─────────────────────────────────
BW = {
    'main':   ('black',  'solid',   2.0),
    'alt1':   ('#555555','dashed',  1.5),
    'alt2':   ('#888888','dashdot', 1.5),
    'alt3':   ('#aaaaaa','dotted',  1.5),
}

# ══════════════════════════════════════════════════════════════════════════════
# HELPER: draw one inverted-U or monotone curve from b1, b2 coefficients
# ══════════════════════════════════════════════════════════════════════════════
def inverted_u_curve(ax, b1, b2, fsts_range=(0, 1.0), label='', color='black',
                     ls='solid', lw=2.0, tp_label=True, intercept=0):
    x = np.linspace(*fsts_range, 300)
    y = intercept + b1 * x + b2 * x**2
    # normalise to zero at x=0 for comparability
    y = y - y[0]
    ax.plot(x * 100, y, color=color, linestyle=ls, linewidth=lw, label=label)
    if b2 != 0 and tp_label:
        tp = -b1 / (2 * b2)
        if fsts_range[0] <= tp <= fsts_range[1]:
            tp_y = b1 * tp + b2 * tp**2
            tp_y = tp_y - (b1 * fsts_range[0] + b2 * fsts_range[0]**2)
            ax.axvline(tp * 100, color=color, linestyle=':', linewidth=0.8, alpha=0.6)
            ax.annotate(f'TP≈{tp*100:.0f}%',
                        xy=(tp * 100, tp_y), xytext=(tp * 100 + 3, tp_y * 0.85),
                        fontsize=7.5, color=color,
                        arrowprops=dict(arrowstyle='->', color=color, lw=0.7))
    return x, y

# ══════════════════════════════════════════════════════════════════════════════
# HELPER: draw conceptual model box-and-arrow diagram
# ══════════════════════════════════════════════════════════════════════════════
def draw_box(ax, text, xy, width=0.22, height=0.10, fontsize=9):
    x, y = xy
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.01",
                         edgecolor='black', facecolor='white', linewidth=1.0)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            multialignment='center')

def draw_arrow(ax, start, end, style='solid', label='', label_offset=(0, 0.03)):
    ls = '--' if style == 'dashed' else '-'
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color='black',
                                linestyle=ls, lw=1.2))
    if label:
        mx = (start[0] + end[0]) / 2 + label_offset[0]
        my = (start[1] + end[1]) / 2 + label_offset[1]
        ax.text(mx, my, label, ha='center', va='center', fontsize=8,
                style='italic')

# ══════════════════════════════════════════════════════════════════════════════
# P3 VIETNAM — conceptual model
# ══════════════════════════════════════════════════════════════════════════════
def p3_conceptual_model():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Figure 1. Conceptual Framework — P3 Vietnam\n'
                 '(Internationalization–Performance with Technology and Digital Moderation)',
                 fontsize=10, pad=10)

    # boxes
    draw_box(ax, 'FSTS\n(Export Intensity)', (0.15, 0.50))
    draw_box(ax, 'ln Labor\nProductivity', (0.85, 0.50))
    draw_box(ax, 'TCI\n(Tech. Capability)', (0.50, 0.82))
    draw_box(ax, 'DAI\n(Website Adoption,\nTier-1)', (0.50, 0.20))

    # direct effect IV → DV (inverted-U hypothesis)
    draw_arrow(ax, (0.26, 0.50), (0.74, 0.50), label='H1: inverted-U (+/−)')

    # moderation arrows (dashed, from moderator to midpoint of IV→DV arrow)
    draw_arrow(ax, (0.50, 0.77), (0.50, 0.53), style='dashed', label='H2 (+)')
    draw_arrow(ax, (0.50, 0.25), (0.50, 0.47), style='dashed', label='H3 (expl.)')

    # controls note
    ax.text(0.50, 0.01,
            'Controls: ln(Employees), Firm Age, Foreign Ownership, Sector FE, Wave FE',
            ha='center', va='bottom', fontsize=7.5, color='#555555')

    # legend
    legend_els = [
        Line2D([0], [0], color='black', lw=1.5, label='Direct effect (→)'),
        Line2D([0], [0], color='black', lw=1.5, ls='--', label='Moderating effect (- →)'),
    ]
    ax.legend(handles=legend_els, loc='lower right', fontsize=8,
              frameon=True, edgecolor='black')
    ax.text(0.01, 0.99,
            'Note: Solid arrows = direct effects. Dashed arrows = moderating effects\n'
            '(point to midpoint of moderated relationship). (+) positive; (−) negative.',
            ha='left', va='top', fontsize=7, color='#555555',
            transform=ax.transAxes)

    save(fig, os.path.join(fig_dir('p3'), 'figure_1_conceptual_model.png'))

# ── P3 inverted-U curves by wave ──────────────────────────────────────────────
def p3_invertedU():
    # Actual pooled & wave-level coefficients from p3 replication
    models = {
        'VNM2009':   (0.887, -1.122, 'VNM 2009', BW['alt1'][0], BW['alt1'][1]),
        'VNM2015':   (1.055, -1.470, 'VNM 2015', BW['alt2'][0], BW['alt2'][1]),
        'VNM2023':   (0.924, -1.193, 'VNM 2023', BW['alt3'][0], BW['alt3'][1]),
        'VNMpooled': (1.316, -1.810, 'Pooled',   BW['main'][0], BW['main'][1]),
    }

    fig, ax = plt.subplots(figsize=(7, 4.5))
    for key, (b1, b2, lbl, col, ls) in models.items():
        lw = 2.2 if 'pooled' in key else 1.4
        inverted_u_curve(ax, b1, b2, fsts_range=(0, 0.8), label=lbl,
                         color=col, ls=ls, lw=lw, tp_label=True)

    ax.set_xlabel('Export Intensity — FSTS (%)', fontsize=11)
    ax.set_ylabel('Δ ln Labor Productivity (centered)', fontsize=11)
    ax.set_title('Figure 2. Inverted-U Relationship: P3 Vietnam\n'
                 '(M2 quadratic coefficients, WBES 2009/2015/2023 pooled)',
                 fontsize=10)
    ax.axhline(0, color='#cccccc', linewidth=0.8)
    ax.set_xlim(0, 80)
    ax.legend(loc='upper right', frameon=True, edgecolor='black')
    ax.text(0.02, 0.03,
            'Note: Curves plot Δ ln LP = b₁·FSTS + b₂·FSTS² (centered at FSTS=0).\n'
            'Vertical dotted lines indicate turning points (TP).\n'
            'Source: WBES Vietnam 2009, 2015, 2023 (N=4,302 pooled).',
            transform=ax.transAxes, fontsize=7.5, va='bottom', color='#555555')
    save(fig, os.path.join(fig_dir('p3'), 'figure_2_invertedU_by_wave.png'))

# ══════════════════════════════════════════════════════════════════════════════
# P4 SINGAPORE — conceptual model
# ══════════════════════════════════════════════════════════════════════════════
def p4_conceptual_model():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Figure 1. Conceptual Framework — P4 Singapore\n'
                 '(Inverted-U with TCI Amplification and DAI Moderation)',
                 fontsize=10, pad=10)

    draw_box(ax, 'FSTS\n(Export Intensity)', (0.15, 0.50))
    draw_box(ax, 'ln Labor\nProductivity', (0.85, 0.50))
    draw_box(ax, 'TCI\n(Tech. Capability\nIndex)', (0.50, 0.82))
    draw_box(ax, 'DAI\n(Digital Adoption,\nTier-1+2)', (0.50, 0.20))

    draw_arrow(ax, (0.26, 0.50), (0.74, 0.50), label='H1: inverted-U (+/−)')
    draw_arrow(ax, (0.50, 0.77), (0.50, 0.53), style='dashed', label='H2: amplifies (+)')
    draw_arrow(ax, (0.50, 0.25), (0.50, 0.47), style='dashed', label='H3: modifies TP')

    ax.text(0.50, 0.01,
            'Controls: ln(Employees), Firm Age, Foreign Ownership, Sector FE | N ≈ 617 (SGP 2023)',
            ha='center', va='bottom', fontsize=7.5, color='#555555')

    legend_els = [
        Line2D([0], [0], color='black', lw=1.5, label='Direct effect (→)'),
        Line2D([0], [0], color='black', lw=1.5, ls='--', label='Moderating effect (- →)'),
    ]
    ax.legend(handles=legend_els, loc='lower right', fontsize=8,
              frameon=True, edgecolor='black')
    ax.text(0.01, 0.99,
            'Note: Solid arrows = direct effects. Dashed arrows = moderating effects.\n'
            'DAI measured as Tier-1 (website) + Tier-2 (e-payment). Not dynamic digital capability.',
            ha='left', va='top', fontsize=7, color='#555555', transform=ax.transAxes)

    save(fig, os.path.join(fig_dir('p4'), 'figure_1_conceptual_model.png'))

def p4_invertedU():
    # M2: b1=2.652, b2=-1.705 (NS at 10%, TP=77%); M5 (+ TCI): b1=2.563, b2=-1.168
    fig, ax = plt.subplots(figsize=(7, 4.5))

    inverted_u_curve(ax, 2.652, -1.705, fsts_range=(0, 1.0),
                     label='M2: FSTS only (TP≈77%)',
                     color='black', ls='solid', lw=2.2, tp_label=True)
    inverted_u_curve(ax, 2.563, -1.168, fsts_range=(0, 1.0),
                     label='M5: + TCI (TP shifts)',
                     color='#555555', ls='dashed', lw=1.6, tp_label=True)

    ax.set_xlabel('Export Intensity — FSTS (%)', fontsize=11)
    ax.set_ylabel('Δ ln Labor Productivity (centered)', fontsize=11)
    ax.set_title('Figure 2. Inverted-U Relationship: P4 Singapore\n'
                 '(M2 and M5 quadratic models, WBES 2023)', fontsize=10)
    ax.axhline(0, color='#cccccc', linewidth=0.8)
    ax.set_xlim(0, 100)
    ax.legend(loc='upper left', frameon=True, edgecolor='black')
    ax.text(0.02, 0.03,
            'Note: M2 b₂ not significant at 10% (p=.068); TP at 77% FSTS outside typical sample range.\n'
            'M5 adds TCI direct effect (β=0.168, p<.001). N=617, SGP 2023.\n'
            'Source: World Bank Enterprise Survey Singapore 2023.',
            transform=ax.transAxes, fontsize=7.5, va='bottom', color='#555555')
    save(fig, os.path.join(fig_dir('p4'), 'figure_2_invertedU_singapore.png'))

# ══════════════════════════════════════════════════════════════════════════════
# P5 CHINA — conceptual model + temporal evolution
# ══════════════════════════════════════════════════════════════════════════════
def p5_conceptual_model():
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Figure 1. Conceptual Framework — P5 China\n'
                 '(Temporal Stability of Inverted-U with Capabilities and Digital Moderation)',
                 fontsize=10, pad=10)

    draw_box(ax, 'FSTS\n(Export Intensity)', (0.13, 0.50))
    draw_box(ax, 'ln Labor\nProductivity', (0.87, 0.50))
    draw_box(ax, 'TCI\n(Tech. Capability)', (0.50, 0.84))
    draw_box(ax, 'DAI\n(Digital Adoption,\nTier-1)', (0.50, 0.18))
    draw_box(ax, 'Survey Wave\n(2012 vs 2024)', (0.50, 0.50), width=0.18, height=0.09)

    draw_arrow(ax, (0.24, 0.50), (0.41, 0.50), label='H1: inverted-U')
    draw_arrow(ax, (0.59, 0.50), (0.76, 0.50), label='')
    draw_arrow(ax, (0.50, 0.79), (0.50, 0.55), style='dashed', label='H2')
    draw_arrow(ax, (0.50, 0.23), (0.50, 0.45), style='dashed', label='H3')
    # temporal arrow pointing at main path
    draw_arrow(ax, (0.50, 0.46), (0.50, 0.435), style='dashed', label='H6: wave')

    ax.text(0.50, 0.01,
            'Controls: ln(Employees), Firm Age, Foreign Ownership, Sector FE | N≈2,600 per wave',
            ha='center', va='bottom', fontsize=7.5, color='#555555')
    legend_els = [
        Line2D([0], [0], color='black', lw=1.5, label='Direct effect (→)'),
        Line2D([0], [0], color='black', lw=1.5, ls='--', label='Moderating effect (- →)'),
    ]
    ax.legend(handles=legend_els, loc='lower right', fontsize=8,
              frameon=True, edgecolor='black')
    save(fig, os.path.join(fig_dir('p5'), 'figure_1_conceptual_model.png'))

def p5_temporal_evolution():
    # Actual coefficients from p5_R_coefs.csv
    waves = {
        '2012': (0.9437, -1.2839, 47.6, 'CHN 2012', 'black',   'solid',   2.2),
        '2024': (1.0333, -1.3440, 47.5, 'CHN 2024', '#555555', 'dashed',  1.8),
    }
    # Paternoster z-test: z=0.82, p=.412 → turning points NOT significantly different

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel A: overlaid curves
    ax = axes[0]
    for key, (b1, b2, tp, lbl, col, ls, lw) in waves.items():
        inverted_u_curve(ax, b1, b2, fsts_range=(0, 0.9),
                         label=f'{lbl} (TP≈{tp:.0f}%)',
                         color=col, ls=ls, lw=lw, tp_label=True)
    ax.set_xlabel('Export Intensity — FSTS (%)', fontsize=11)
    ax.set_ylabel('Δ ln Labor Productivity (centered)', fontsize=11)
    ax.set_title('Panel A. Inverted-U Curves\nby Wave (M2)', fontsize=10)
    ax.axhline(0, color='#cccccc', lw=0.8)
    ax.set_xlim(0, 90)
    ax.legend(loc='upper right', frameon=True, edgecolor='black')
    ax.text(0.02, 0.03,
            'Paternoster z-test: z=0.82, p=.412\n→ Turning points not significantly different',
            transform=ax.transAxes, fontsize=7.5, color='#555555')

    # Panel B: TP comparison bar chart
    ax2 = axes[1]
    labels = ['CHN 2012\n(M2)', 'CHN 2024\n(M2)', 'Pooled\n(M2)']
    tps = [47.6, 47.5, 47.6]
    bars = ax2.bar(labels, tps, color=['black', '#555555', '#aaaaaa'],
                   edgecolor='black', width=0.5)
    ax2.set_ylabel('Turning Point — FSTS (%)', fontsize=11)
    ax2.set_title('Panel B. Turning Point Stability\nAcross Waves', fontsize=10)
    ax2.set_ylim(0, 70)
    for bar, tp in zip(bars, tps):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{tp:.1f}%', ha='center', va='bottom', fontsize=9)
    ax2.axhline(48, color='black', ls='dotted', lw=0.8, alpha=0.5)
    ax2.text(2.6, 48.5, '≈48% avg', fontsize=8, color='#555555')
    ax2.text(0.02, 0.03,
            'Note: All TPs ≈ 47–48% FSTS. Paternoster cross-wave\ntest: z=0.82, p=.412 → temporal stability confirmed.',
            transform=ax2.transAxes, fontsize=7.5, color='#555555')

    fig.suptitle('Figure 2. Temporal Stability of Inverted-U — P5 China\n'
                 '(WBES 2012 and 2024, N≈2,600 per wave)', fontsize=10, y=1.01)
    fig.tight_layout()
    save(fig, os.path.join(fig_dir('p5'), 'figure_2_temporal_evolution.png'))

# ══════════════════════════════════════════════════════════════════════════════
# P7 MULTI-COUNTRY — conceptual model + ICRV gradient
# ══════════════════════════════════════════════════════════════════════════════
def p7_conceptual_model():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Figure 1. Conceptual Framework — P7 Multi-Country Asia\n'
                 '(Three-Way Moderation: Digital Capability × Institutional Regime × Manager)',
                 fontsize=10, pad=10)

    # Main IV and DV
    draw_box(ax, 'FSTS\n(Export Intensity)', (0.12, 0.50), width=0.20)
    draw_box(ax, 'ln Labor\nProductivity', (0.88, 0.50), width=0.20)

    # Moderators
    draw_box(ax, 'TCI\n(Tech. Capability)', (0.50, 0.88), width=0.18)
    draw_box(ax, 'DAI\n(Digital Adoption\nTier-1 or Tier-1+2)', (0.50, 0.62), width=0.21)
    draw_box(ax, 'ICRV\n(Institutional Regime\n1–6)', (0.50, 0.38), width=0.21)
    draw_box(ax, 'Manager Experience\n& Gender', (0.50, 0.14), width=0.22)

    # Main effect arrow
    draw_arrow(ax, (0.22, 0.50), (0.78, 0.50), label='H1: inverted-U (+/−)')

    # Moderation arrows
    draw_arrow(ax, (0.50, 0.83), (0.50, 0.67), style='dashed', label='H2')
    draw_arrow(ax, (0.50, 0.57), (0.50, 0.53), style='dashed', label='H3')
    draw_arrow(ax, (0.50, 0.33), (0.50, 0.47), style='dashed', label='H4')
    draw_arrow(ax, (0.50, 0.19), (0.50, 0.44), style='dashed', label='H5')

    # Three-way bracket indication
    ax.annotate('', xy=(0.62, 0.55), xytext=(0.62, 0.63),
                arrowprops=dict(arrowstyle='<->', color='black', lw=0.8))
    ax.text(0.64, 0.59, 'H6:\nDAI×ICRV\n×FSTS', ha='left', va='center',
            fontsize=7.5, style='italic')

    ax.text(0.50, 0.01,
            'Controls: ln(Employees), Firm Age, Foreign Ownership | Country-Year FE | N=84,910–29,840; 49 economies',
            ha='center', va='bottom', fontsize=7.5, color='#555555')

    legend_els = [
        Line2D([0], [0], color='black', lw=1.5, label='Direct effect (→)'),
        Line2D([0], [0], color='black', lw=1.5, ls='--', label='Moderating effect (- →)'),
        Line2D([0], [0], color='black', lw=1.0, marker='<', markersize=5, label='Three-way interaction (H6)'),
    ]
    ax.legend(handles=legend_els, loc='lower right', fontsize=8,
              frameon=True, edgecolor='black')
    save(fig, os.path.join(fig_dir('p7'), 'figure_1_conceptual_model.png'))

def p7_icrv_gradient():
    # P7 actual turning points by ICRV regime from p7_R_turning_points.csv
    # M6 country FE: overall TP=40.4%
    # By ICRV subgroup (tp_raw from csv):
    icrv_data = {
        'Advanced\nInnovation': (0.934, -1.071, 56.6, 'black',   'solid'),
        'Emerging':             (2.026, -2.995, 43.9, '#444444', 'dashed'),
        'Lower-mid\nTransition':(3.130, -4.413, 44.5, '#777777', 'dashdot'),
        'Upper-mid':            (-0.107, -0.798, 5.5, '#aaaaaa', 'dotted'),
    }
    # Note: SIDS_small shows U-shape (FIP), not inverted-U

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Panel A: Inverted-U by ICRV regime
    ax = axes[0]
    for regime, (b1, b2, tp, col, ls) in icrv_data.items():
        inverted_u_curve(ax, b1, b2, fsts_range=(0, 0.9),
                         label=f'{regime.replace(chr(10), " ")} (TP≈{tp:.0f}%)',
                         color=col, ls=ls, lw=1.8, tp_label=False)

    # Add vertical TP indicators
    tps = [56.6, 43.9, 44.5]
    cols = ['black', '#444444', '#777777']
    for tp, col in zip(tps, cols):
        ax.axvline(tp, color=col, ls=':', lw=0.7, alpha=0.5)

    ax.set_xlabel('Export Intensity — FSTS (%)', fontsize=11)
    ax.set_ylabel('Δ ln Labor Productivity (centered)', fontsize=11)
    ax.set_title('Panel A. I-P Curves by ICRV Regime\n(P7 Multi-country, M6 country FE)', fontsize=10)
    ax.axhline(0, color='#cccccc', lw=0.8)
    ax.set_xlim(0, 90)
    ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=8)
    ax.text(0.02, 0.03,
            'Note: Upper-mid regime shows low b₁, suggesting minimal positive range.\n'
            'SIDS regime (FIP) plotted separately in P8 figures.',
            transform=ax.transAxes, fontsize=7, color='#555555')

    # Panel B: TP summary bar chart by regime
    ax2 = axes[1]
    regimes = ['Advanced\nInnovation\n(Regime I)', 'Emerging\n(Regime II)',
               'Lower-mid\nTransition\n(Regime III)', 'Upper-mid\n(Regime II-III)', 'Overall\nM6']
    tp_vals = [56.6, 43.9, 44.5, 5.5, 40.4]
    bar_cols = ['black', '#444444', '#777777', '#aaaaaa', '#333333']
    bars = ax2.bar(range(len(regimes)), tp_vals,
                   color=bar_cols, edgecolor='black', width=0.6)
    ax2.set_xticks(range(len(regimes)))
    ax2.set_xticklabels(regimes, fontsize=8)
    ax2.set_ylabel('Turning Point — FSTS (%)', fontsize=11)
    ax2.set_title('Panel B. Institutional Gradient:\nTurning Points by ICRV Regime', fontsize=10)
    ax2.set_ylim(0, 80)
    for bar, tp in zip(bars, tp_vals):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{tp:.1f}%', ha='center', va='bottom', fontsize=8)
    ax2.text(0.02, 0.03,
            'Note: TP declines as institutional quality decreases (Regimes I→III).\n'
            'Upper-mid TP near zero reflects b₁ ≈ 0 (weak linear component).\n'
            'Source: P7 multi-country WBES, R replication (p7_R_turning_points.csv).',
            transform=ax2.transAxes, fontsize=7, color='#555555')

    fig.suptitle('Figure 2. Institutional Gradient in I-P Relationship — P7 Multi-Country Asia\n'
                 '(N=84,910–91,982; 49 economies; country-year FE)', fontsize=10, y=1.01)
    fig.tight_layout()
    save(fig, os.path.join(fig_dir('p7'), 'figure_2_icrv_gradient.png'))

# ══════════════════════════════════════════════════════════════════════════════
# P8 SIDS — conceptual model + FIP curve
# ══════════════════════════════════════════════════════════════════════════════
def p8_conceptual_model():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Figure 1. Conceptual Framework — P8 Pacific SIDS\n'
                 '(Forced Internationalization Penalty: FIP as Boundary Condition)',
                 fontsize=10, pad=10)

    # Structural prerequisites boxes (left side — violated)
    draw_box(ax, '3 Violated\nStructural\nPrerequisites', (0.18, 0.72), width=0.26, height=0.16)
    ax.text(0.18, 0.59,
            '(1) Non-viable domestic market\n(2) Extreme trade costs\n(3) Institutional voids',
            ha='center', va='top', fontsize=7.5, color='#444444')

    # IV and DV
    draw_box(ax, 'FSTS\n(Survival-Based\nInternationalization)', (0.15, 0.35))
    draw_box(ax, 'ln Labor\nProductivity', (0.85, 0.35))

    # Capability moderators (null)
    draw_box(ax, 'TCI\n(Tech. Capability)', (0.50, 0.80))
    draw_box(ax, 'DAI\n(Website Adoption,\nTier-1 proxy)', (0.50, 0.18))

    # FIP main effect — NEGATIVE monotone (thick dashed arrow below main line)
    draw_arrow(ax, (0.26, 0.35), (0.74, 0.35),
               label='H1: FIP — monotone negative (−)')

    # Structural prerequisites → shapes the entire relationship
    ax.annotate('', xy=(0.15, 0.43), xytext=(0.18, 0.64),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.0, ls='dashed'))
    ax.text(0.10, 0.54, 'Structural\ncondition', ha='center', fontsize=7.5, style='italic')

    # Capability null moderations
    draw_arrow(ax, (0.50, 0.75), (0.50, 0.40), style='dashed', label='H2: null (n.s.)')
    draw_arrow(ax, (0.50, 0.23), (0.50, 0.30), style='dashed', label='H2: null (n.s.)')

    # FIP label
    ax.text(0.50, 0.27, 'FIP: β = −0.404, p = .032\n(N=1,469; 9 Pacific SIDS)',
            ha='center', va='top', fontsize=8, color='black',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0', edgecolor='black', lw=0.8))

    ax.text(0.50, 0.01,
            'Controls: ln(Employees), Firm Age, Foreign Ownership | Country + Year FE',
            ha='center', va='bottom', fontsize=7.5, color='#555555')

    legend_els = [
        Line2D([0], [0], color='black', lw=2.0, label='Direct effect: H1 FIP (monotone −)'),
        Line2D([0], [0], color='black', lw=1.2, ls='--', label='Null moderation: H2 (n.s.)'),
    ]
    ax.legend(handles=legend_els, loc='lower right', fontsize=8,
              frameon=True, edgecolor='black')
    ax.text(0.01, 0.99,
            'Note: Unlike mainland Asian papers, no inverted-U expected. FIP predicts\n'
            'monotone negative relationship with no turning point within observed range.',
            ha='left', va='top', fontsize=7, color='#555555', transform=ax.transAxes)

    save(fig, os.path.join(fig_dir('p8'), 'figure_1_conceptual_model.png'))

def p8_fip_curve():
    # P8 actual coefficients: M1 β=-0.404, M_yearFE β=-1.236, M_biv β=-1.596
    # No turning point — monotone negative

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Panel A: FIP vs hypothetical inverted-U
    ax = axes[0]
    x = np.linspace(0, 1, 300)

    # FIP lines (actual data — M1 country+year FE)
    y_m1     = -0.404 * x
    y_yearFE = -1.236 * x
    y_biv    = -1.596 * x

    # Hypothetical inverted-U for contrast (e.g., P3 pooled)
    y_hyp = 1.316 * x + (-1.810) * x**2
    y_hyp = y_hyp - y_hyp[0]

    ax.plot(x * 100, y_m1,     color='black',   ls='solid',   lw=2.2,
            label='M1 FIP: β=−0.404* (country+year FE)')
    ax.plot(x * 100, y_yearFE, color='#555555', ls='dashed',  lw=1.6,
            label='M_yearFE: β=−1.236*** (year FE only)')
    ax.plot(x * 100, y_biv,    color='#888888', ls='dashdot', lw=1.4,
            label='M_bivariate: β=−1.596***')
    ax.plot(x * 100, y_hyp,    color='#aaaaaa', ls='dotted',  lw=1.4,
            label='Reference: inverted-U\n(P3 pooled TP≈36%)', alpha=0.7)

    ax.axhline(0, color='#cccccc', lw=0.8)
    ax.set_xlabel('Export Intensity — FSTS (%)', fontsize=11)
    ax.set_ylabel('Δ ln Labor Productivity', fontsize=11)
    ax.set_title('Panel A. Forced Internationalization Penalty\nvs Reference Inverted-U', fontsize=10)
    ax.set_xlim(0, 100)
    ax.legend(loc='upper right', frameon=True, edgecolor='black', fontsize=8)

    # Shade negative region
    ax.fill_between(x * 100, y_m1, 0, where=(y_m1 < 0),
                    alpha=0.08, color='black', label='_nolegend_')
    ax.text(55, -0.12, 'FIP zone\n(persistent penalty)',
            ha='center', fontsize=8, color='#333333', style='italic')

    # Panel B: four-specification comparison bar chart
    ax2 = axes[1]
    specs = ['M1\n(country+year FE)', 'M_yearFE\n(year FE only)', 'M_bivariate\n(no controls)',
             'Exporters-only\n(N=187)']
    betas = [-0.404, -1.236, -1.596, -0.901]
    sigs  = ['*', '***', '***', '*']
    bar_cols = ['black', '#555555', '#888888', '#aaaaaa']

    bars = ax2.bar(range(len(specs)), betas, color=bar_cols,
                   edgecolor='black', width=0.6)
    ax2.set_xticks(range(len(specs)))
    ax2.set_xticklabels(specs, fontsize=8)
    ax2.set_ylabel('β (FSTS coefficient)', fontsize=11)
    ax2.set_title('Panel B. FIP Robustness\nAcross Four Specifications', fontsize=10)
    ax2.axhline(0, color='black', lw=0.8)
    ax2.set_ylim(-2.0, 0.3)

    for bar, beta, sig in zip(bars, betas, sigs):
        ypos = beta - 0.06 if beta < 0 else beta + 0.02
        ax2.text(bar.get_x() + bar.get_width()/2, ypos,
                 f'{beta:.3f}{sig}', ha='center', va='top', fontsize=8, color='white'
                 if beta < -0.5 else 'black')

    ax2.text(0.02, 0.03,
            'Note: All β < 0 across specifications. No turning point detected\n'
            '(M2 quadratic FSTS_c² NS, p=.508). FIP confirmed.\n'
            'Source: WBES Pacific SIDS 2009–2025, R replication.',
            transform=ax2.transAxes, fontsize=7.5, color='#555555')

    fig.suptitle('Figure 2. Forced Internationalization Penalty (FIP) — P8 Pacific SIDS\n'
                 '(N=1,469 firms; 9 economies; WBES 2009–2025)', fontsize=10, y=1.01)
    fig.tight_layout()
    save(fig, os.path.join(fig_dir('p8'), 'figure_2_fip_curve.png'))

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generating publication figures for all papers...")
    print("\n── P3 Vietnam ──")
    p3_conceptual_model()
    p3_invertedU()

    print("\n── P4 Singapore ──")
    p4_conceptual_model()
    p4_invertedU()

    print("\n── P5 China ──")
    p5_conceptual_model()
    p5_temporal_evolution()

    print("\n── P7 Multi-country Asia ──")
    p7_conceptual_model()
    p7_icrv_gradient()

    print("\n── P8 Pacific SIDS ──")
    p8_conceptual_model()
    p8_fip_curve()

    print("\nAll figures generated successfully.")
    print("Outputs in: p3/figures/, p4/figures/, p5/figures/, p7/figures/, p8/figures/")
