#!/usr/bin/env python3
"""Generate publication-quality P3 Vietnam figures from pre-computed coefficients.

Source: p3/replication/coefs_main_models.csv
Outputs: p3/replication/figures/  (PNG + PDF for each figure)
"""
import os, csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.lines import Line2D

# ── paths ─────────────────────────────────────────────────────────────────────
REPO   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COEFS  = os.path.join(REPO, 'replication', 'coefs_main_models.csv')
OUT    = os.path.join(REPO, 'replication', 'figures')
os.makedirs(OUT, exist_ok=True)

# ── academic style ────────────────────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

WAVE_PALETTE = {
    'VNM2009':   ('#2166ac', 'solid',   '2009'),
    'VNM2015':   ('#d6604d', 'dashed',  '2015'),
    'VNM2023':   ('#1a9641', 'dashdot', '2023'),
    'VNMpooled': ('#762a83', 'dotted',  'Pooled'),
}

# FSTS means from Table 1 (all-firm, including FSTS=0 for non-exporters)
FSTS_MEAN = {
    'VNM2009':   0.168,
    'VNM2015':   0.119,
    'VNM2023':   0.131,
    'VNMpooled': 0.139,
}

# ── load coefficients ─────────────────────────────────────────────────────────
def load_coefs(path):
    coefs = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            k = (row['sample'], row['model'])
            if k not in coefs:
                coefs[k] = {}
            coefs[k][row['term']] = {
                'b':  float(row['b']),
                'se': float(row['se']),
                'p':  float(row['p']),
                'ci_lo': float(row['ci_lo']),
                'ci_hi': float(row['ci_hi']),
            }
    return coefs

coefs = load_coefs(COEFS)

def get(coefs, sample, model, term):
    return coefs.get((sample, model), {}).get(term, {}).get('b', None)

# ── Figure 2a–2d: individual wave inverted-U curves ──────────────────────────
def plot_wave_curve(ax, sample, color, label):
    m   = FSTS_MEAN[sample]
    b1  = get(coefs, sample, 'M2', 'FSTSc')
    b2  = get(coefs, sample, 'M2', 'FSTSc2')
    if b1 is None or b2 is None:
        return None
    # turning point in raw FSTS
    tp_c   = -b1 / (2 * b2)
    tp_raw = tp_c + m

    # fitted curve over raw FSTS ∈ [0, 1]
    fsts_raw = np.linspace(0, 1, 300)
    fsts_c   = fsts_raw - m
    y = b1 * fsts_c + b2 * fsts_c**2

    ax.plot(fsts_raw * 100, y, color=color, lw=2, label=label)
    ax.axvline(tp_raw * 100, color=color, lw=1.2, ls='--', alpha=0.7)
    ax.text(tp_raw * 100 + 1, ax.get_ylim()[0] + 0.02 if ax.get_ylim()[0] != 0 else -0.15,
            f'{tp_raw*100:.1f}%', color=color, fontsize=8, va='bottom')
    return tp_raw

fig2, axes2 = plt.subplots(2, 2, figsize=(9, 7), sharey=False)
wave_order = [('VNM2009','a'), ('VNM2015','b'), ('VNM2023','c'), ('VNMpooled','d')]
ns = {'VNM2009': 989, 'VNM2015': 956, 'VNM2023': 1013, 'VNMpooled': 2958}

for (sample, letter), ax in zip(wave_order, axes2.flat):
    color, _, wave_label = WAVE_PALETTE[sample]
    ax.axhline(0, color='gray', lw=0.6, ls=':')
    tp = plot_wave_curve(ax, sample, color, wave_label)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Export intensity — FSTS (%)', fontsize=9)
    ax.set_ylabel('Δ ln(labour productivity)', fontsize=9)
    title = f'({letter}) {wave_label}  [N = {ns[sample]:,}]'
    ax.set_title(title, fontsize=10)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())

fig2.suptitle(
    'Figure 2. Wave-specific inverted-U relationship between export intensity\n'
    'and labour productivity — Vietnam WBES 2009, 2015, 2023, and Pooled (Model M2)',
    fontsize=10, y=1.01
)
fig2.tight_layout()
for ext in ('png', 'pdf'):
    fig2.savefig(os.path.join(OUT, f'figure_2_wave_curves.{ext}'),
                 bbox_inches='tight', dpi=200 if ext == 'png' else None)
plt.close(fig2)
print('Figure 2 saved.')

# ── Figure 2a–2d as separate files (manuscript may need individual panels) ────
for (sample, letter) in wave_order:
    color, _, wave_label = WAVE_PALETTE[sample]
    fig, ax = plt.subplots(figsize=(4.5, 3.5))
    ax.axhline(0, color='gray', lw=0.6, ls=':')
    plot_wave_curve(ax, sample, color, wave_label)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Export intensity — FSTS (%)', fontsize=9)
    ax.set_ylabel('Δ ln(labour productivity)', fontsize=9)
    ax.set_title(f'({letter}) Vietnam {wave_label}  [N = {ns[sample]:,}]', fontsize=10)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter())
    fig.tight_layout()
    for ext in ('png', 'pdf'):
        fig.savefig(os.path.join(OUT, f'figure_2{letter}.{ext}'),
                    bbox_inches='tight', dpi=200 if ext == 'png' else None)
    plt.close(fig)
print('Figures 2a–2d (individual panels) saved.')

# ── Figure 2_overlay: all 4 waves on one plot ─────────────────────────────────
fig_ov, ax_ov = plt.subplots(figsize=(6, 4))
ax_ov.axhline(0, color='gray', lw=0.6, ls=':')
for sample, (color, ls, label) in WAVE_PALETTE.items():
    m   = FSTS_MEAN[sample]
    b1  = get(coefs, sample, 'M2', 'FSTSc')
    b2  = get(coefs, sample, 'M2', 'FSTSc2')
    if b1 is None or b2 is None:
        continue
    tp_c   = -b1 / (2 * b2)
    tp_raw = tp_c + m
    fsts_raw = np.linspace(0, 1, 300)
    fsts_c   = fsts_raw - m
    y = b1 * fsts_c + b2 * fsts_c**2
    ax_ov.plot(fsts_raw * 100, y, color=color, lw=2, ls=ls, label=f'{label} (TP={tp_raw*100:.1f}%)')
    ax_ov.axvline(tp_raw * 100, color=color, lw=0.8, ls=':', alpha=0.6)

ax_ov.set_xlim(0, 100)
ax_ov.set_xlabel('Export intensity — FSTS (%)')
ax_ov.set_ylabel('Δ ln(labour productivity)')
ax_ov.set_title(
    'Structural stability of the inverted-U turning point\n'
    'across Vietnam WBES waves 2009–2023 (Model M2)', fontsize=10
)
ax_ov.xaxis.set_major_formatter(mtick.PercentFormatter())
ax_ov.legend(fontsize=8, loc='lower center', framealpha=0.9)
ax_ov.text(0.02, 0.97, 'Shaded band: 39–46% FSTS', transform=ax_ov.transAxes,
           fontsize=7.5, va='top', color='gray')
ax_ov.axvspan(39, 46, alpha=0.08, color='steelblue')
fig_ov.tight_layout()
for ext in ('png', 'pdf'):
    fig_ov.savefig(os.path.join(OUT, f'figure_2_overlay.{ext}'),
                   bbox_inches='tight', dpi=200 if ext == 'png' else None)
plt.close(fig_ov)
print('Figure 2_overlay saved.')

# ── Figure 3: TCI moderator marginal effects ──────────────────────────────────
# Marginal effect of FSTS at TCI = low/mean/high (+/- 1 SD)
# ME = b_FSTSc + b_FSTS_TCI*TCI + 2*(b_FSTScsq + b_FSTSsq_TCI*TCI)*FSTSc

TCI_LEVELS = {'TCI = -1 SD': -1, 'TCI = Mean': 0, 'TCI = +1 SD': +1}
TCI_COLORS = {-1: '#d7191c', 0: '#fdae61', 1: '#1a9641'}
TCI_LS     = {-1: 'dashed', 0: 'solid', 1: 'dotted'}

fig3, axes3 = plt.subplots(1, 2, figsize=(9, 4))

# Panel A: TCI marginal effects on FSTS slope (pooled M3)
ax = axes3[0]
sample = 'VNMpooled'
b_f   = get(coefs, sample, 'M3', 'FSTSc')
b_f2  = get(coefs, sample, 'M3', 'FSTSc2')
b_t   = get(coefs, sample, 'M3', 'TCI_z')
b_ft  = get(coefs, sample, 'M3', 'FSTSc_TCIz')
b_f2t = get(coefs, sample, 'M3', 'FSTSc2_TCIz')
m     = FSTS_MEAN[sample]
fsts_raw = np.linspace(0, 1, 300)
fsts_c   = fsts_raw - m

if all(v is not None for v in [b_f, b_f2, b_ft, b_f2t]):
    for label, tci_val in TCI_LEVELS.items():
        y = ((b_f + b_ft * tci_val) * fsts_c
             + (b_f2 + b_f2t * tci_val) * fsts_c**2)
        ax.plot(fsts_raw * 100, y, color=TCI_COLORS[tci_val],
                lw=2, ls=TCI_LS[tci_val], label=label)

ax.axhline(0, color='gray', lw=0.6, ls=':')
ax.set_xlim(0, 100)
ax.set_xlabel('Export intensity — FSTS (%)')
ax.set_ylabel('Δ ln(labour productivity)')
ax.set_title('(A) TCI moderator — Pooled (M3)', fontsize=10)
ax.xaxis.set_major_formatter(mtick.PercentFormatter())
ax.legend(fontsize=8, loc='upper right')

# Panel B: Wave-specific TCI direct effects (M3 coefficients)
ax2 = axes3[1]
waves_labels = ['2009', '2015', '2023', 'Pooled']
waves_keys   = ['VNM2009', 'VNM2015', 'VNM2023', 'VNMpooled']
tci_betas = []
tci_ci_lo = []
tci_ci_hi = []
for wk in waves_keys:
    c = coefs.get((wk, 'M3'), {}).get('TCI_z', {})
    tci_betas.append(c.get('b', np.nan))
    tci_ci_lo.append(c.get('ci_lo', np.nan))
    tci_ci_hi.append(c.get('ci_hi', np.nan))

colors_bar = ['#2166ac','#d6604d','#1a9641','#762a83']
y_pos = np.arange(len(waves_labels))
bars = ax2.barh(y_pos, tci_betas, xerr=[
    [b - lo for b, lo in zip(tci_betas, tci_ci_lo)],
    [hi - b for b, hi in zip(tci_betas, tci_ci_hi)]
], color=colors_bar, alpha=0.8, capsize=4, height=0.5)
ax2.axvline(0, color='gray', lw=0.8, ls=':')
ax2.set_yticks(y_pos)
ax2.set_yticklabels(waves_labels)
ax2.set_xlabel('β (TCI_z coefficient, 95% CI)')
ax2.set_title('(B) TCI direct effects by wave (M3)', fontsize=10)

fig3.suptitle(
    'Figure 3. Technological Capability (TCI) moderator marginal effects\n'
    'on export intensity–productivity relationship — Vietnam WBES', fontsize=10
)
fig3.tight_layout()
for ext in ('png', 'pdf'):
    fig3.savefig(os.path.join(OUT, f'figure_3_tci_moderator.{ext}'),
                 bbox_inches='tight', dpi=200 if ext == 'png' else None)
plt.close(fig3)
print('Figure 3 saved.')

# ── Figure 4: DAI proxy-obsolescence trajectory ───────────────────────────────
fig4, ax4 = plt.subplots(figsize=(6, 4))

wave_keys2 = ['VNM2009', 'VNM2015', 'VNM2023']
dai_direct = []
dai_interact = []
years = [2009, 2015, 2023]
for wk in wave_keys2:
    c4  = coefs.get((wk, 'M4'), {})
    b_d = c4.get('DAI_z', {}).get('b', np.nan)
    b_fd= c4.get('FSTSc_DAIz', {}).get('b', np.nan)
    dai_direct.append(b_d)
    dai_interact.append(b_fd)

x = np.arange(3)
w = 0.35
bars1 = ax4.bar(x - w/2, dai_direct,   w, label='Direct effect (β_DAI)', color='#4575b4', alpha=0.85)
bars2 = ax4.bar(x + w/2, dai_interact, w, label='FSTS × DAI interaction', color='#d73027', alpha=0.85)
ax4.axhline(0, color='gray', lw=0.7, ls=':')
ax4.set_xticks(x)
ax4.set_xticklabels(['2009', '2015', '2023'])
ax4.set_xlabel('Survey wave')
ax4.set_ylabel('Coefficient (β)')
ax4.set_title(
    'Figure 4. DAI (website binary, Tier-1) proxy-obsolescence trajectory\n'
    'Direct and interactive effects with FSTS across waves (Model M4)', fontsize=10
)
ax4.legend(fontsize=8)

for bar_group in [bars1, bars2]:
    for bar in bar_group:
        h = bar.get_height()
        if not np.isnan(h):
            ax4.text(bar.get_x() + bar.get_width()/2, h + 0.01 if h >= 0 else h - 0.06,
                     f'{h:.3f}', ha='center', va='bottom', fontsize=8)
fig4.tight_layout()
for ext in ('png', 'pdf'):
    fig4.savefig(os.path.join(OUT, f'figure_4_dai_obsolescence.{ext}'),
                 bbox_inches='tight', dpi=200 if ext == 'png' else None)
plt.close(fig4)
print('Figure 4 saved.')

print(f'\nAll P3 figures written to {OUT}/')
print('Files:', sorted(os.listdir(OUT)))
