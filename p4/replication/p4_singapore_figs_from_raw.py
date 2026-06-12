#!/usr/bin/env python3
"""P3 Singapore — final figure generation from raw WBES DTA.
Confirmed spec: TCI=b8+e6+h1 z-each (>=2/3), sector: mfg(a4a=1)+constr(a4a=2),
no lnLP winsorization, FSTS=d3c/100 mean-centered.
"""
import pyreadstat, pandas as pd, numpy as np, warnings
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from statsmodels.formula.api import ols
warnings.filterwarnings('ignore')

UPLOAD = '/root/.claude/uploads/4342a099-4c09-46f0-a81b-f754f349e99f'
import os
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, 'manuscripts', 'figures', 'p3_singapore')
os.makedirs(OUT, exist_ok=True)

# ── 1. Load data ──────────────────────────────────────────────────────────────
df_raw, meta = pyreadstat.read_dta(f'{UPLOAD}/d0ca2a21-Singapore2023fulldata.dta')
df = df_raw.copy()

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].replace([-9, -8, -7, -6], np.nan)

print(f"Raw: {len(df)} firms")

# ── 2. Focal variables ────────────────────────────────────────────────────────
df['lnLP']      = np.where((df['d2']>0)&(df['l1']>0), np.log(df['d2']/df['l1']), np.nan)
df['FSTS']      = np.where(df['d3c'].notna(), df['d3c']/100, np.nan)
df['lnEmp']     = np.where(df['l1']>0, np.log(df['l1']), np.nan)
df['firmage']   = np.where((df['b5']>1900)&(df['b5']<=2023), 2023-df['b5'], np.nan)
df['foreigndum']= np.where(df['b2b'].notna(), (df['b2b']>0).astype(float), np.nan)

# Correct sector dummies (a4a 1-5: 1=Mfg, 2=Constr, 3=Wholesale, 4=Prof, 5=OtherSvc)
df['sec_mfg']    = (df['a4a']==1).astype(float)
df['sec_constr'] = (df['a4a']==2).astype(float)

# ── 3. TCI: b8+e6+h1, z-standardize each, rowmean >=2/3, re-standardize ─────
for item in ['b8','e6','h1']:
    df[f'{item}_bin'] = np.where(df[item]==1, 1.0, np.where(df[item]==2, 0.0, np.nan))
mat3 = pd.DataFrame({it: df[f'{it}_bin'] for it in ['b8','e6','h1']})
for c in mat3.columns:
    m,s = mat3[c].mean(), mat3[c].std()
    mat3[c] = (mat3[c]-m)/s if s>0 else 0.0
comp3 = mat3.mean(axis=1)
comp3[mat3.notna().sum(axis=1)<2] = np.nan
m,s = comp3.mean(), comp3.std()
df['TCI_z'] = (comp3-m)/s if s>0 else comp3

# ── 4. DAI: c22b_bin+k33+k38, z-each, rowmean >=2/3, re-standardize ─────────
df['c22b_bin'] = np.where(df['c22b']==1, 1.0, np.where(df['c22b']==2, 0.0, np.nan))
dai_cols = ['c22b_bin','k33','k38']
mat_d = pd.DataFrame({it: df[it] for it in dai_cols})
for c in mat_d.columns:
    m,s = mat_d[c].mean(), mat_d[c].std()
    mat_d[c] = (mat_d[c]-m)/s if s>0 else mat_d[c]
comp_d = mat_d.mean(axis=1)
comp_d[mat_d.notna().sum(axis=1)<2] = np.nan
m,s = comp_d.mean(), comp_d.std()
df['DAI_z'] = (comp_d-m)/s if s>0 else comp_d

# ── 5. FSTS mean-centering ────────────────────────────────────────────────────
fsts_mean = df.loc[df['FSTS'].notna(),'FSTS'].mean()
df['FSTS_c']   = df['FSTS'] - fsts_mean
df['FSTSsq_c'] = df['FSTS_c']**2
print(f"FSTS mean: {fsts_mean*100:.2f}%")

# ── 6. Sample flags ───────────────────────────────────────────────────────────
NEED_BASE = ['lnLP','FSTS_c','FSTSsq_c','lnEmp','firmage','foreigndum','sec_mfg','sec_constr']
NEED_FULL = NEED_BASE + ['TCI_z','DAI_z']

df['samp_base'] = df[NEED_BASE].notna().all(axis=1)
df['samp_tci']  = df['samp_base'] & df['TCI_z'].notna()
df['samp_dai']  = df['samp_base'] & df['DAI_z'].notna()
df['samp_full'] = df[NEED_FULL].notna().all(axis=1)

for s in ['base','tci','dai','full']:
    print(f"N {s}: {df[f'samp_{s}'].sum()}")

# ── 7. Run models M0–M8 ───────────────────────────────────────────────────────
SEC = '+ sec_mfg + sec_constr'
CTRL = f'lnEmp + firmage + foreigndum{SEC}'

d_b = df[df['samp_base']].copy()
d_t = df[df['samp_tci']].copy()
d_d = df[df['samp_dai']].copy()
d_f = df[df['samp_full']].copy()

def run(formula, data):
    return ols(formula, data).fit(cov_type='HC1')

M0 = run(f'lnLP ~ {CTRL}', d_b)
M1 = run(f'lnLP ~ FSTS_c + {CTRL}', d_b)
M2 = run(f'lnLP ~ FSTS_c + FSTSsq_c + {CTRL}', d_b)
M3 = run(f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + {CTRL}', d_t)
M4 = run(f'lnLP ~ FSTS_c + FSTSsq_c + DAI_z + {CTRL}', d_d)
M5 = run(f'lnLP ~ TCI_z + {CTRL}', d_t)
M6 = run(f'lnLP ~ DAI_z + {CTRL}', d_d)
M7 = run(f'lnLP ~ TCI_z + DAI_z + {CTRL}', d_f)
M8 = run(f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + {CTRL}', d_f)

models = [M0,M1,M2,M3,M4,M5,M6,M7,M8]
names  = ['M0','M1','M2','M3','M4','M5','M6','M7','M8']

print("\n=== KEY RESULTS ===")
for m, n in zip(models, names):
    print(f"\n{n} (N={int(m.nobs)}, AdjR²={m.rsquared_adj:.3f}):")
    for term in ['FSTS_c','FSTSsq_c','TCI_z','DAI_z','FSTS_c:DAI_z','FSTSsq_c:DAI_z']:
        if term in m.params:
            p = m.pvalues[term]
            stars = '***' if p<0.001 else '**' if p<0.01 else '*' if p<0.05 else ''
            print(f"  {term}: β={m.params[term]:+.3f}{stars}  SE={m.bse[term]:.3f}  p={p:.3f}")

# ── 8. Turning point (M2) ────────────────────────────────────────────────────
b1, b2 = M2.params['FSTS_c'], M2.params['FSTSsq_c']
tp_c   = -b1/(2*b2)
tp     = tp_c + fsts_mean
cov2   = M2.cov_params()
g1 = -1/(2*b2); g2 = b1/(2*b2**2)
se_tp  = np.sqrt(g1**2*M2.bse['FSTS_c']**2 + g2**2*M2.bse['FSTSsq_c']**2
                  + 2*g1*g2*cov2.loc['FSTS_c','FSTSsq_c'])
ci_lo, ci_hi = tp-1.96*se_tp, tp+1.96*se_tp

print(f"\nM2 Turning point: {tp*100:.1f}% [{ci_lo*100:.1f}%–{ci_hi*100:.1f}%]")
print(f"  b1={b1:+.4f}  b2={b2:+.4f}")

# ── 9. FIGURE 2: Marginal effect of DAI on lnLP ─────────────────────────────
fig2, ax2 = plt.subplots(figsize=(8.5, 5.5))
plt.rcParams.update({'font.size': 11})

fsts_c_range = np.linspace(d_f['FSTS_c'].min(), d_f['FSTS_c'].max(), 200)
fsts_range   = fsts_c_range + fsts_mean

b_dai  = M8.params['DAI_z']
b_int1 = M8.params['FSTS_c:DAI_z']
b_int2 = M8.params['FSTSsq_c:DAI_z']
me_dai = b_dai + b_int1*fsts_c_range + b_int2*fsts_c_range**2

cov8 = M8.cov_params()
idx  = list(M8.params.index)
i_d  = idx.index('DAI_z')
i_i1 = idx.index('FSTS_c:DAI_z')
i_i2 = idx.index('FSTSsq_c:DAI_z')
se_me = np.sqrt(
    cov8.iloc[i_d,i_d]
    + fsts_c_range**2 * cov8.iloc[i_i1,i_i1]
    + fsts_c_range**4 * cov8.iloc[i_i2,i_i2]
    + 2*fsts_c_range    * cov8.iloc[i_d,i_i1]
    + 2*fsts_c_range**2 * cov8.iloc[i_d,i_i2]
    + 2*fsts_c_range**3 * cov8.iloc[i_i1,i_i2]
)

ax2.axhline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.6)
ax2.fill_between(fsts_range, me_dai-1.96*se_me, me_dai+1.96*se_me,
                  alpha=0.20, color='steelblue', label='95% CI')
ax2.plot(fsts_range, me_dai, color='steelblue', linewidth=2.2, label='Marginal effect of DAI')

# Rug plot
ax2.plot(d_f['FSTS'].values, np.full(len(d_f), me_dai.min()-0.04),
         '|', color='gray', alpha=0.3, markersize=4)
ax2.axvspan(0.70, fsts_range.max(), alpha=0.07, color='gray', label='Thin support (FSTS>70%)')

ax2.set_xlabel('Export Intensity (FSTS = direct exports / total sales)', fontsize=11)
ax2.set_ylabel('Marginal effect of DAI on ln(Labour Productivity)', fontsize=11)
ax2.set_title(f'Figure 2: Marginal Effect of DAI across Export Intensity\n'
              f'Singapore WBES 2023, M8 OLS-HC1 (N={int(M8.nobs)})', fontsize=12)
ax2.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax2.legend(fontsize=10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_2_dai_marginal_effect.png', dpi=300, bbox_inches='tight')
plt.close()
print("\nFigure 2 saved")

# ── 10. FIGURE 3: Predicted I–P curve (M2) ───────────────────────────────────
fig3, ax3 = plt.subplots(figsize=(8.5, 5.5))

fsts_plot   = np.linspace(0, 1, 300)
fsts_c_plot = fsts_plot - fsts_mean

# Predict with controls at means
ctrl_names = [c for c in M2.params.index if c not in ['Intercept','FSTS_c','FSTSsq_c']]
X_pred = pd.DataFrame({'Intercept': 1, 'FSTS_c': fsts_c_plot, 'FSTSsq_c': fsts_c_plot**2})
for c in ctrl_names:
    X_pred[c] = d_b[c].mean()

y_pred  = X_pred[M2.params.index].values @ M2.params.values
cov_mat = M2.cov_params().values
X_np    = X_pred[M2.params.index].values
se_pred = np.sqrt(np.diag(X_np @ cov_mat @ X_np.T))

ax3.fill_between(fsts_plot, y_pred-1.96*se_pred, y_pred+1.96*se_pred,
                  alpha=0.18, color='tomato', label='95% CI')
ax3.plot(fsts_plot, y_pred, color='tomato', linewidth=2.2, label='Predicted ln(LP) (M2)')

# Turning point
ax3.axvline(tp, color='steelblue', linewidth=1.5, linestyle='--',
            label=f'Turning point ≈ {tp*100:.1f}% [{ci_lo*100:.0f}%–{ci_hi*100:.0f}%]')
ax3.axvspan(max(0, ci_lo), min(1, ci_hi), alpha=0.12, color='steelblue')

# Rug
ax3.plot(d_b['FSTS'].values, np.full(len(d_b), y_pred.min()-0.08),
         '|', color='gray', alpha=0.25, markersize=4)

ax3.set_xlabel('Export Intensity (FSTS)', fontsize=11)
ax3.set_ylabel('Predicted ln(Labour Productivity)', fontsize=11)
ax3.set_title(f'Figure 3: Predicted Internationalization–Performance Curve\n'
              f'Singapore WBES 2023, OLS M2 (N={int(M2.nobs)})', fontsize=12)
ax3.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax3.legend(fontsize=10)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_3_predicted_ip_curve.png', dpi=300, bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# ── 11. Print summary ─────────────────────────────────────────────────────────
import json
results = {
    'spec': '3-item TCI (b8+e6+h1 z-each), sector: mfg+constr, no winsor, FSTS=d3c',
    'M8_N': int(M8.nobs),
    'M8_TCI_b': round(float(M8.params['TCI_z']), 3),
    'M8_TCI_p': round(float(M8.pvalues['TCI_z']), 3),
    'M8_INT_b': round(float(M8.params['FSTSsq_c:DAI_z']), 3),
    'M8_adjR2': round(float(M8.rsquared_adj), 3),
    'M2_TP_pct': round(float(tp*100), 1),
    'M2_TP_ci_lo': round(float(ci_lo*100), 1),
    'M2_TP_ci_hi': round(float(ci_hi*100), 1),
    'manuscript_targets': {'TCI': 0.153, 'INT': 3.119, 'AdjR2': 0.196, 'N': 617}
}
with open(f'{OUT}/results_p3.json','w') as f:
    json.dump(results, f, indent=2)

print("\n=== REPLICATION SUMMARY ===")
print(f"  M8 N={results['M8_N']} (target 617)")
print(f"  M8 TCI={results['M8_TCI_b']} (target 0.153)")
print(f"  M8 INT(FSTSsq_c:DAI_z)={results['M8_INT_b']} (target 3.119)")
print(f"  M8 AdjR²={results['M8_adjR2']} (target 0.196)")
print(f"  M2 Turning point: {results['M2_TP_pct']}% [{results['M2_TP_ci_lo']}%–{results['M2_TP_ci_hi']}%]")
print("\nFigures saved:")
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f"  {f}: {os.path.getsize(f'{OUT}/{f}'):,} bytes")
