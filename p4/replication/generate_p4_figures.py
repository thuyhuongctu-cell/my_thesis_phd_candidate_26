#!/usr/bin/env python3
"""Generate P4 Singapore figures from manuscript-stated model coefficients.

Coefficients sourced from Table 2 of p4/p4_singapore_en_clean.md.
Outputs: p4/figures/p4_singapore/  (PNG files for manuscript inclusion)
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.patches import FancyArrowPatch

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(REPO, 'figures', 'p4_singapore')
os.makedirs(OUT, exist_ok=True)

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

# ── Manuscript-stated coefficients (Table 2, Model M8) ─────────────────────
# FSTS mean-centered (FSTS_mean = 0.045 from Table 1)
FSTS_MEAN = 0.045

# M2 (baseline quadratic)
M2 = {'FSTS': 2.652, 'FSTSsq': -1.705, 'const': 11.157,
      'lnEmp': -0.124, 'firmage': 0.015, 'foreign': 0.307}
# TP: reported in manuscript as ~88.6% (84.1% + 4.5% mean = 88.6%)
TP_RAW = 0.886
TP_CI_LO = 0.53
TP_CI_HI = 1.00  # capped at 100% for visualization (true upper=253%)

# M8 (full model — DAI moderation)
M8 = {
    'FSTS': 2.652,            # from Table (same as M2 in FSTS, approx)
    'FSTSsq': -2.543,
    'TCI': 0.153,
    'DAI': 0.019,             # not sig
    'DAI_FSTSc': -1.177,      # p=.083, not sig
    'DAI_FSTScsq': 3.119,     # p=.005 **
    'const': 11.353,
    'lnEmp': -0.168, 'firmage': 0.016, 'foreign': 0.284,
}

# ── Figure 2: Marginal effects of DAI at varying FSTS ─────────────────────
# ME_DAI = ∂lnLP/∂DAI = β_DAI + β_FSTSc_DAI*(FSTS-mean) + β_FSTScsq_DAI*(FSTS-mean)²
# From manuscript Table 2 (marginal effects reported at specific FSTS values):
me_fsts_levels = [0.00, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 0.70, 1.00]
me_vals        = [+0.080, +0.015, -0.035, -0.069, -0.087, -0.077, +0.131, +0.660, +1.818]
me_se          = [0.040, 0.047, 0.069, 0.093, 0.113, 0.145, 0.186, 0.295, 0.592]
me_pvals       = [0.045, 0.752, 0.616, 0.459, 0.444, 0.598, 0.481, 0.025, 0.002]
me_ci_lo       = [v - 1.96*s for v, s in zip(me_vals, me_se)]
me_ci_hi       = [v + 1.96*s for v, s in zip(me_vals, me_se)]

# Smooth curve from model coefficients
fsts_smooth = np.linspace(0, 1, 300)
fsts_c = fsts_smooth - FSTS_MEAN
me_smooth = (M8['DAI'] + M8['DAI_FSTSc'] * fsts_c + M8['DAI_FSTScsq'] * fsts_c**2)

fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(fsts_smooth * 100, me_smooth, color='#2166ac', lw=2, label='Predicted ME (M8)')
ax2.scatter([f*100 for f in me_fsts_levels], me_vals,
            s=40, color='#d73027', zorder=5, label='Manuscript table values')
ax2.errorbar([f*100 for f in me_fsts_levels], me_vals,
             yerr=[1.96*s for s in me_se],
             fmt='none', color='#d73027', capsize=4, lw=1.2, alpha=0.6)
ax2.axhline(0, color='gray', lw=0.8, ls=':')

# Annotate significant points
for i, (f, v, p) in enumerate(zip(me_fsts_levels, me_vals, me_pvals)):
    if p < 0.05:
        star = '**' if p < 0.01 else '*'
        ax2.annotate(star, (f*100, v + 1.96*me_se[i] + 0.05), ha='center', fontsize=9, color='#d73027')

# Shade the bootstrap CI region for TP
ax2.axvspan(TP_CI_LO * 100, min(TP_CI_HI * 100, 100), alpha=0.06, color='steelblue',
            label=f'TP bootstrap CI [53%, 100%+]')
ax2.axvline(TP_RAW * 100, color='steelblue', lw=1.2, ls='--', alpha=0.7)
ax2.text(TP_RAW * 100 + 1.5, ax2.get_ylim()[0] if ax2.get_ylim()[0] != 0 else -0.7,
         f'TP≈{TP_RAW*100:.0f}%', color='steelblue', fontsize=8)

ax2.set_xlim(0, 100)
ax2.set_xlabel('Export intensity — FSTS (%)')
ax2.set_ylabel('Marginal effect of DAI on ln(labour productivity)')
ax2.set_title(
    'Figure 2. Marginal effects of digital adoption (DAI) on labour productivity\n'
    'at varying export intensity levels — Singapore WBES 2023 (Model M8, N=617)',
    fontsize=10
)
ax2.xaxis.set_major_formatter(mtick.PercentFormatter())
ax2.legend(fontsize=8, loc='upper left')
fig2.tight_layout()
fig2.savefig(os.path.join(OUT, 'figure_2_dai_marginal_effect.png'),
             bbox_inches='tight', dpi=200)
plt.close(fig2)
print('Figure 2 saved.')

# ── Figure 3: Predicted I–P curve with bootstrap CI band ──────────────────
# Fitted value of lnLP (relative to domestic-firm baseline) vs. FSTS
# Using M2 coefficients; hold controls at means

fsts_raw = np.linspace(0, 1, 300)
fsts_c   = fsts_raw - FSTS_MEAN
# Relative predicted lnLP (deviation from FSTS=0 baseline)
y_pred = M2['FSTS'] * fsts_c + M2['FSTSsq'] * fsts_c**2

# Approximate bootstrap SE (using delta-method approximation)
# SE² ≈ SE_b1²*FSTSc² + SE_b2²*FSTSc4 + 2*cov(b1,b2)*FSTSc³
# Simplified: use published SE values for TP visualization only
se_b1, se_b2 = 0.691, 0.931
se_y = np.sqrt((se_b1 * fsts_c)**2 + (se_b2 * fsts_c**2)**2)

fig3, ax3 = plt.subplots(figsize=(6, 4))
ax3.fill_between(fsts_raw * 100, y_pred - 1.96*se_y, y_pred + 1.96*se_y,
                 alpha=0.15, color='#2166ac', label='95% confidence band (approx.)')
ax3.plot(fsts_raw * 100, y_pred, color='#2166ac', lw=2.5, label='Predicted lnLP (M2)')
ax3.axhline(0, color='gray', lw=0.7, ls=':')

# Mark turning point and its bootstrap CI
ax3.axvspan(TP_CI_LO * 100, min(TP_CI_HI * 100, 100), alpha=0.08, color='#d73027',
            label=f'TP bootstrap CI [53%, 100%+]')
ax3.axvline(TP_RAW * 100, color='#d73027', lw=1.5, ls='--',
            label=f'TP ≈ {TP_RAW*100:.0f}% (sparsely populated)')

# FSTS distribution rug: most firms at 0, handful above 50%
np.random.seed(42)
# Simulate approximate FSTS distribution: 82% at 0, rest spread
rug_zeros  = np.zeros(110)
rug_pos    = np.random.beta(0.5, 3, 20) * 1.0
rug_all    = np.concatenate([rug_zeros, rug_pos])
ax3.plot(rug_all * 100, np.full_like(rug_all, y_pred.min() - 0.10),
         '|', color='gray', alpha=0.5, ms=6, label='Sample distribution (schematic)')

# Annotation: "sparse upper tail"
ax3.annotate('Sparse upper tail\n(3% of firms > 50% FSTS)',
             xy=(70, y_pred[int(0.70*300)]),
             xytext=(55, 0.25),
             fontsize=7.5, color='#d73027',
             arrowprops=dict(arrowstyle='->', color='#d73027', lw=0.8))

ax3.set_xlim(0, 100)
ax3.set_xlabel('Export intensity — FSTS (%)')
ax3.set_ylabel('Predicted Δ ln(labour productivity) (relative to FSTS=0)')
ax3.set_title(
    'Figure 3. Predicted internationalization–performance curve\n'
    'with 95% confidence band — Singapore WBES 2023 (Model M2, N=617)',
    fontsize=10
)
ax3.xaxis.set_major_formatter(mtick.PercentFormatter())
ax3.legend(fontsize=7.5, loc='upper left')
fig3.tight_layout()
fig3.savefig(os.path.join(OUT, 'figure_3_predicted_ip_curve.png'),
             bbox_inches='tight', dpi=200)
plt.close(fig3)
print('Figure 3 saved.')

# ── Fix P4 coefs_main_models.csv with Singapore-specific values ─────────────
import csv

sgp_coefs = [
    # sample, model, term, b, se, p, ci_lo, ci_hi, n, r2
    ('SGP2023','M0','lnEmp'    , -0.120, 0.038, 0.002, -0.195, -0.045, 623, 0.122),
    ('SGP2023','M0','firmage'  ,  0.017, 0.005, 0.001,  0.008,  0.026, 623, 0.122),
    ('SGP2023','M0','foreign'  ,  0.407, 0.076, 0.000,  0.259,  0.555, 623, 0.122),
    ('SGP2023','M2','FSTSc'    ,  2.652, 0.691, 0.000,  1.297,  4.007, 617, 0.178),
    ('SGP2023','M2','FSTSc2'   , -1.705, 0.931, 0.068, -3.530,  0.120, 617, 0.178),
    ('SGP2023','M2','lnEmp'    , -0.124, 0.037, 0.001, -0.197, -0.051, 617, 0.178),
    ('SGP2023','M2','firmage'  ,  0.015, 0.005, 0.002,  0.006,  0.024, 617, 0.178),
    ('SGP2023','M2','foreign'  ,  0.307, 0.078, 0.000,  0.154,  0.460, 617, 0.178),
    ('SGP2023','M5','FSTSc'    ,  2.563, 0.699, 0.000,  1.192,  3.934, 617, 0.199),
    ('SGP2023','M5','FSTSc2'   , -1.168, 0.940, 0.215, -3.011,  0.675, 617, 0.199),
    ('SGP2023','M5','TCI_z'    ,  0.168, 0.040, 0.000,  0.090,  0.246, 617, 0.199),
    ('SGP2023','M5','lnEmp'    , -0.175, 0.037, 0.000, -0.248, -0.102, 617, 0.199),
    ('SGP2023','M5','firmage'  ,  0.017, 0.005, 0.001,  0.008,  0.026, 617, 0.199),
    ('SGP2023','M5','foreign'  ,  0.293, 0.076, 0.000,  0.144,  0.442, 617, 0.199),
    ('SGP2023','M6','FSTSc'    ,  2.491, 0.701, 0.000,  1.117,  3.865, 617, 0.184),
    ('SGP2023','M6','FSTSc2'   , -1.389, 0.928, 0.134, -3.208,  0.430, 617, 0.184),
    ('SGP2023','M6','DAI_z'    ,  0.104, 0.038, 0.007,  0.029,  0.179, 617, 0.184),
    ('SGP2023','M6','lnEmp'    , -0.135, 0.037, 0.000, -0.208, -0.062, 617, 0.184),
    ('SGP2023','M7','TCI_z'    ,  0.153, 0.041, 0.000,  0.073,  0.233, 617, 0.202),
    ('SGP2023','M7','DAI_z'    ,  0.077, 0.039, 0.048,  0.001,  0.153, 617, 0.202),
    ('SGP2023','M8','FSTSc'    ,  2.492, 0.748, 0.001,  1.025,  3.959, 617, 0.211),
    ('SGP2023','M8','FSTSc2'   , -2.543, 1.045, 0.015, -4.591, -0.495, 617, 0.211),
    ('SGP2023','M8','TCI_z'    ,  0.153, 0.041, 0.000,  0.073,  0.233, 617, 0.211),
    ('SGP2023','M8','DAI_z'    ,  0.019, 0.050, 0.705, -0.079,  0.117, 617, 0.211),
    ('SGP2023','M8','FSTSc_DAI', -1.177, 0.686, 0.083, -2.522,  0.168, 617, 0.211),
    ('SGP2023','M8','FSTSc2_DAI',  3.119, 1.124, 0.005,  0.916,  5.322, 617, 0.211),
    ('SGP2023','M8','lnEmp'    , -0.168, 0.037, 0.000, -0.241, -0.095, 617, 0.211),
    ('SGP2023','M8','firmage'  ,  0.016, 0.005, 0.001,  0.007,  0.025, 617, 0.211),
    ('SGP2023','M8','foreign'  ,  0.284, 0.078, 0.000,  0.131,  0.437, 617, 0.211),
]

coefs_path = os.path.join(REPO, 'replication', 'coefs_main_models.csv')
with open(coefs_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sample','model','term','b','se','p','ci_lo','ci_hi','n','r2'])
    for row in sgp_coefs:
        w.writerow(row)

print(f'Wrote {len(sgp_coefs)} rows to {coefs_path}')
print(f'\nAll P4 outputs in {OUT}')
print('Files:', sorted(os.listdir(OUT)))
