#!/usr/bin/env python3
"""Generate corrected Figure 1: Conceptual model for P3 Vietnam.

Fixes: Vietnam ICRV label = Group IV (Emerging), not Frontier V.
Outputs: p3/figures/vietnam/figure_1_conceptual_model.png + .pdf
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(REPO, 'figures', 'vietnam')
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'figure.dpi': 300,
})

fig, ax = plt.subplots(figsize=(10, 6.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# ── helper: draw rounded box ──────────────────────────────────────────────────
def box(ax, cx, cy, w, h, text, fontsize=9, style='round,pad=0.1',
        fc='white', ec='black', lw=1.2, linestyle='solid'):
    bp = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                        boxstyle=style, facecolor=fc,
                        edgecolor=ec, linewidth=lw, linestyle=linestyle,
                        zorder=3)
    ax.add_patch(bp)
    ax.text(cx, cy, text, ha='center', va='center',
            fontsize=fontsize, wrap=True, zorder=4,
            multialignment='center')

# ── helper: draw arrow ────────────────────────────────────────────────────────
def arrow(ax, x0, y0, x1, y1, label='', label_offset=(0, 0.15),
          style='solid', color='black', lw=1.2):
    ls = '-' if style == 'solid' else '--'
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, linestyle=ls),
                zorder=2)
    if label:
        mx = (x0 + x1) / 2 + label_offset[0]
        my = (y0 + y1) / 2 + label_offset[1]
        ax.text(mx, my, label, ha='center', va='center',
                fontsize=8.5, color='black', zorder=5)

# ── boxes ─────────────────────────────────────────────────────────────────────
# Independent variable (FSTS)
box(ax, 2.0, 4.5, 2.6, 1.2,
    'Export Intensity\n(FSTS_c, FSTS_c²)\n[inverted-U, H1]',
    fontsize=9)

# Moderators / direct effects
box(ax, 2.0, 2.5, 2.6, 1.0,
    'Technological Capability\n(TCI_z)\n[direct: H2a]',
    fontsize=9)

box(ax, 2.0, 0.9, 2.6, 1.0,
    'Digital Adoption\n(DAI_z — Tier-1 proxy)\n[exploratory: H4a/b]',
    fontsize=9, linestyle='dashed', ec='#444444')

# Dependent variable
box(ax, 7.5, 3.5, 2.5, 1.1,
    'Labour Productivity\nln(LP)\n[Dependent]',
    fontsize=9)

# Controls
box(ax, 7.5, 1.2, 2.5, 1.0,
    'Controls\nFirm size, age,\nforeign ownership,\nsector & wave FE',
    fontsize=8.5, ec='#777777', linestyle='dotted')

# Context annotation
ctx = FancyBboxPatch((0.3, 5.7), 9.4, 1.0,
                     boxstyle='round,pad=0.1', facecolor='#f5f5f5',
                     edgecolor='#888888', linewidth=1.0, linestyle='solid',
                     zorder=1)
ax.add_patch(ctx)
ax.text(5.0, 6.2,
        'Context: Vietnam (single-country) — '
        'ICRV Group IV (Emerging) — '
        'WBES 2009, 2015, 2023 (N = 1,131–3,091 obs. per wave)',
        ha='center', va='center', fontsize=8.5, color='#333333', zorder=4)

# ── arrows ────────────────────────────────────────────────────────────────────
# FSTS → LP (main H1, solid)
arrow(ax, 3.3, 4.5, 6.25, 3.8,
      label='H1: β₁>0, β₂<0\nTP≈39–46%',
      label_offset=(0.2, 0.35))

# TCI → LP (direct H2a, solid)
arrow(ax, 3.3, 2.5, 6.25, 3.2,
      label='H2a: direct (+)',
      label_offset=(0.25, 0.25))

# DAI → LP (exploratory, dashed)
arrow(ax, 3.3, 0.9, 6.25, 2.95,
      label='H4a: direct (ns)',
      label_offset=(0.3, 0.2), style='dashed', color='#444444')

# Controls → LP (dotted-style, grey)
arrow(ax, 6.25, 1.2, 6.25, 2.95,
      style='dashed', color='#777777')

# ── legend ────────────────────────────────────────────────────────────────────
legend_items = [
    mpatches.Patch(facecolor='white', edgecolor='black', lw=1.2,
                   label='Hypothesized direct effect (solid box)'),
    mpatches.Patch(facecolor='white', edgecolor='#444444', lw=1.2,
                   linestyle='--', label='Exploratory probe (dashed box)'),
]
from matplotlib.lines import Line2D
legend_items += [
    Line2D([0], [0], color='black', lw=1.2,
           label='Direct effect (solid arrow)'),
    Line2D([0], [0], color='#444444', lw=1.2, linestyle='--',
           label='Exploratory effect (dashed arrow)'),
]
ax.legend(handles=legend_items, loc='lower left', fontsize=7.5,
          framealpha=0.9, edgecolor='#aaaaaa')

# ── title / caption ───────────────────────────────────────────────────────────
ax.set_title(
    'Figure 1. Conceptual Framework — P3 Vietnam\n'
    'Internationalisation–Performance Relationship with Technological Capability '
    'and Foundational Digital Adoption',
    fontsize=10, pad=8)

ax.text(5.0, 0.07,
        'Note. Dashed arrows indicate exploratory probes not formalised as primary hypotheses. '
        'DAI_z = Tier-1 digital proxy (website presence, WBES item c22b). '
        'ICRV = Group IV (Emerging) per the 6-regime classification.',
        ha='center', va='bottom', fontsize=7.5, color='#555555', style='italic')

plt.tight_layout()

for ext in ('png', 'pdf'):
    path = os.path.join(OUT, f'figure_1_conceptual_model.{ext}')
    plt.savefig(path, dpi=300, bbox_inches='tight')
    print(f'Saved: {path}')

plt.close()
print('Done.')
