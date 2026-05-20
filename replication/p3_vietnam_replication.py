#!/usr/bin/env python3
"""P3 Vietnam — full replication from raw WBES DTA files.
3 waves: 2009, 2015, 2023.
Primary spec: TCI=b8+e6 (z-each, rowmean, re-std), DAI=c22b_bin (z-std).
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
OUT = os.path.join(REPO, 'manuscripts', 'figures', 'p3_vietnam')
os.makedirs(OUT, exist_ok=True)

# ── Helper to build wave dataframe ───────────────────────────────────────────
def build_wave(path, wave_year, encoding=None):
    """Load and construct analytic variables for one Vietnam WBES wave."""
    kwargs = {}
    if encoding:
        kwargs['encoding'] = encoding
    try:
        df, meta = pyreadstat.read_dta(path, **kwargs)
    except:
        df = pd.read_stata(path, convert_categoricals=False)

    # Recode WBES nonresponse
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].replace([-9,-8,-7,-6], np.nan)

    # ── Core variables ────────────────────────────────────────────────────────
    df['lnLP']      = np.where((df['d2']>0)&(df['l1']>0), np.log(df['d2']/df['l1']), np.nan)
    df['FSTS']      = np.where(df['d3c'].notna(), df['d3c']/100.0, np.nan)
    df['FSTS']      = df['FSTS'].clip(0, 1)
    df['lnEmp']     = np.where(df['l1']>0, np.log(df['l1']), np.nan)
    df['firmage']   = np.where((df['b5']>1900)&(df['b5']<=wave_year),
                                wave_year - df['b5'], np.nan)
    df['foreigndum']= np.where(df['b2b'].notna(), (df['b2b']>0).astype(float), np.nan)
    df['wave']      = wave_year

    # ── Sector dummies: manufacturing vs. services ────────────────────────────
    # 2009/2015: a4a uses ISIC codes; 2023: a4a uses 1-7
    if df['a4a'].max() > 10:
        # ISIC codes: manufacturing = 15-39 (some overlap)
        df['sec_mfg'] = ((df['a4a']>=15)&(df['a4a']<=36)).astype(float)
        # Construction = 45; Wholesale/Retail = 50-52
        df['sec_svc'] = ((df['a4a']==45)|(df['a4a']>=50)).astype(float)
    else:
        # 2023 Vietnam: 1-7 coding — need to check labels
        # From exploration: mean=4.02, so mostly services?
        # Try: 1-3 = manufacturing sectors, 4-7 = services
        df['sec_mfg'] = (df['a4a']<=3).astype(float)
        df['sec_svc'] = (df['a4a']>=5).astype(float)

    # ── TCI (primary): b8 + e6, z-each, rowmean, re-standardize ─────────────
    for item in ['b8','e6']:
        if item in df.columns:
            df[f'{item}_bin'] = np.where(df[item]==1, 1.0,
                                  np.where(df[item]==2, 0.0, np.nan))
        else:
            df[f'{item}_bin'] = np.nan

    tci_items = ['b8_bin','e6_bin']
    mat_tci = pd.DataFrame({it: df[it] for it in tci_items})
    for c in mat_tci.columns:
        m,s = mat_tci[c].mean(), mat_tci[c].std()
        mat_tci[c] = (mat_tci[c]-m)/s if s>0 else 0.0
    comp_tci = mat_tci.mean(axis=1)
    comp_tci[mat_tci.notna().sum(axis=1)<1] = np.nan  # require >=1 valid item
    m,s = comp_tci.mean(), comp_tci.std()
    df['TCI_z'] = (comp_tci-m)/s if s>0 else comp_tci

    # ── DAI (primary): c22b only, z-standardize ─────────────────────────────
    if 'c22b' in df.columns:
        df['c22b_bin'] = np.where(df['c22b']==1, 1.0,
                          np.where(df['c22b']==2, 0.0, np.nan))
    else:
        df['c22b_bin'] = np.nan
    m,s = df['c22b_bin'].mean(), df['c22b_bin'].std()
    df['DAI_z'] = (df['c22b_bin']-m)/s if s>0 else df['c22b_bin']

    # ── FSTS centering (within-wave) ─────────────────────────────────────────
    fsts_mean = df.loc[df['FSTS'].notna(),'FSTS'].mean()
    df['FSTS_c']   = df['FSTS'] - fsts_mean
    df['FSTSsq_c'] = df['FSTS_c']**2

    # ── Sample flags ─────────────────────────────────────────────────────────
    NEED_BASE = ['lnLP','FSTS_c','FSTSsq_c','lnEmp','firmage','foreigndum','sec_mfg','sec_svc']
    df['samp_base'] = df[NEED_BASE].notna().all(axis=1)
    df['samp_tci']  = df['samp_base'] & df['TCI_z'].notna()
    df['samp_dai']  = df['samp_base'] & df['DAI_z'].notna()
    df['samp_full'] = df['samp_tci'] & df['DAI_z'].notna()

    print(f"Wave {wave_year}: raw={len(df)}, base={df['samp_base'].sum()}, "
          f"TCI={df['samp_tci'].sum()}, DAI={df['samp_dai'].sum()}, full={df['samp_full'].sum()}")
    print(f"  FSTS mean: {fsts_mean*100:.2f}%, TCI mean={df['TCI_z'].mean():.3f}, DAI mean={df['DAI_z'].mean():.3f}")
    print(f"  sec_mfg: {df['sec_mfg'].sum()}, sec_svc: {df['sec_svc'].sum()}")

    df['fsts_mean'] = fsts_mean
    return df

# ── Load all three waves ─────────────────────────────────────────────────────
print("Loading waves...")
df09 = build_wave(f'{UPLOAD}/ce379f9e-Vietnam2009fulldata.dta', 2009)
df15 = build_wave(f'{UPLOAD}/2cf27baa-Vietnam2015fulldata.dta', 2015, encoding='latin1')
df23 = build_wave(f'{UPLOAD}/c5673dd2-VietNam2023fulldata.dta', 2023)

# ── OLS helper ───────────────────────────────────────────────────────────────
SEC = '+ sec_mfg + sec_svc'
CTRL = f'lnEmp + firmage + foreigndum{SEC}'

def run(formula, data):
    return ols(formula, data).fit(cov_type='HC1')

def run_wave(df, label):
    """Run M0-M8 for one wave. Returns dict of models."""
    d_b = df[df['samp_base']].copy()
    d_t = df[df['samp_tci']].copy()
    d_d = df[df['samp_dai']].copy()
    d_f = df[df['samp_full']].copy()

    mods = {}
    mods['M0'] = run(f'lnLP ~ {CTRL}', d_b)
    mods['M1'] = run(f'lnLP ~ FSTS_c + {CTRL}', d_b)
    mods['M2'] = run(f'lnLP ~ FSTS_c + FSTSsq_c + {CTRL}', d_b)
    mods['M3'] = run(f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + FSTS_c:TCI_z + {CTRL}', d_t)
    mods['M4'] = run(f'lnLP ~ FSTS_c + FSTSsq_c + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + {CTRL}', d_d)
    mods['M5'] = run(f'lnLP ~ TCI_z + {CTRL}', d_t)
    mods['M6'] = run(f'lnLP ~ DAI_z + {CTRL}', d_d)
    mods['M7'] = run(f'lnLP ~ TCI_z + DAI_z + {CTRL}', d_f)
    mods['M8'] = run(f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + {CTRL}', d_f)

    print(f"\n=== {label} ===")
    terms = ['FSTS_c','FSTSsq_c','TCI_z','DAI_z','FSTS_c:TCI_z','FSTS_c:DAI_z','FSTSsq_c:DAI_z']
    for mn, m in mods.items():
        present = [t for t in terms if t in m.params]
        if present:
            s = f"{mn} (N={int(m.nobs)}, R²={m.rsquared_adj:.3f}): "
            for t in present:
                p = m.pvalues[t]
                stars = '***' if p<.001 else '**' if p<.01 else '*' if p<.05 else ''
                s += f"{t}={m.params[t]:+.3f}{stars}  "
            print(f"  {s}")
        else:
            print(f"  {mn} (N={int(m.nobs)}, R²={m.rsquared_adj:.3f})")

    return mods, d_b, d_t, d_d, d_f

mods09, d_b09, d_t09, d_d09, d_f09 = run_wave(df09, '2009')
mods15, d_b15, d_t15, d_d15, d_f15 = run_wave(df15, '2015')
mods23, d_b23, d_t23, d_d23, d_f23 = run_wave(df23, '2023')

# ── Pooled dataset ────────────────────────────────────────────────────────────
print("\n=== POOLED ===")
df_pool = pd.concat([df09, df15, df23], ignore_index=True)
df_pool['w2015'] = (df_pool['wave']==2015).astype(float)
df_pool['w2023'] = (df_pool['wave']==2023).astype(float)

d_pool_b = df_pool[df_pool['samp_base']].copy()
d_pool_f = df_pool[df_pool['samp_full']].copy()

M_pool7 = run(f'lnLP ~ TCI_z + DAI_z + {CTRL} + w2015 + w2023', d_pool_f)
M_pool8 = run(f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + {CTRL} + w2015 + w2023', d_pool_f)
print(f"Pooled M7 (N={int(M_pool7.nobs)}): "
      f"TCI={M_pool7.params.get('TCI_z',np.nan):+.3f} "
      f"DAI={M_pool7.params.get('DAI_z',np.nan):+.3f}")
print(f"Pooled M8 (N={int(M_pool8.nobs)}): "
      f"TCI={M_pool8.params.get('TCI_z',np.nan):+.3f} "
      f"DAI={M_pool8.params.get('DAI_z',np.nan):+.3f} "
      f"INT_DAI={M_pool8.params.get('FSTSsq_c:DAI_z',np.nan):+.3f}")

# ── FIGURE 2: Predicted I-P curves (one per wave + pooled) ────────────────────
def plot_predicted_curve(M2, d_b, fsts_mean, wave_label, color, ax, N_base):
    """Plot predicted lnLP vs FSTS from M2 (quadratic base model)."""
    fsts_plot   = np.linspace(0, 0.8, 300)
    fsts_c_plot = fsts_plot - fsts_mean

    ctrl_names = [c for c in M2.params.index if c not in ['Intercept','FSTS_c','FSTSsq_c']]
    X_pred = pd.DataFrame({'Intercept': 1, 'FSTS_c': fsts_c_plot, 'FSTSsq_c': fsts_c_plot**2})
    for c in ctrl_names:
        if c in d_b.columns:
            X_pred[c] = d_b[c].mean()
        else:
            X_pred[c] = 0.0

    X_np    = X_pred[M2.params.index].values
    y_pred  = X_np @ M2.params.values
    se_pred = np.sqrt(np.diag(X_np @ M2.cov_params().values @ X_np.T))

    ax.fill_between(fsts_plot, y_pred-1.96*se_pred, y_pred+1.96*se_pred,
                     alpha=0.18, color=color)
    ax.plot(fsts_plot, y_pred, color=color, linewidth=2.2, label=f'{wave_label} (N={N_base:,})')

    # Turning point
    b1, b2 = M2.params.get('FSTS_c',0), M2.params.get('FSTSsq_c',0)
    if abs(b2)>1e-6 and b2<0:
        tp_c = -b1/(2*b2)
        tp   = tp_c + fsts_mean
        if 0 < tp < 0.8:
            tp_y = M2.params['Intercept'] + b1*tp_c + b2*tp_c**2
            ax.axvline(tp, color=color, linewidth=1, linestyle='--', alpha=0.7)
            ax.annotate(f'{tp*100:.0f}%', xy=(tp, tp_y), xytext=(tp+0.02, tp_y+0.05),
                        fontsize=8, color=color)

    # Rug
    ax.plot(d_b['FSTS'].clip(0,0.8).values, np.full(len(d_b), y_pred.min()-0.15),
            '|', color=color, alpha=0.25, markersize=3)

fig2, axes = plt.subplots(2, 2, figsize=(12, 9))
plt.rcParams.update({'font.size': 10})

wave_info = [
    (mods09['M2'], d_b09, df09.loc[df09['samp_base'],'fsts_mean'].iloc[0], '2009', '#1f6feb', axes[0,0]),
    (mods15['M2'], d_b15, df15.loc[df15['samp_base'],'fsts_mean'].iloc[0], '2015', '#d73a49', axes[0,1]),
    (mods23['M2'], d_b23, df23.loc[df23['samp_base'],'fsts_mean'].iloc[0], '2023', '#238636', axes[1,0]),
]

for M2, d_b, fm, wlabel, col, ax in wave_info:
    plot_predicted_curve(M2, d_b, fm, wlabel, col, ax, int(M2.nobs))
    ax.set_xlabel('Export Intensity (FSTS)', fontsize=10)
    ax.set_ylabel('Predicted ln(Labour Productivity)', fontsize=10)
    ax.set_title(f'Wave {wlabel} — M2 OLS-HC1', fontsize=11)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(fontsize=9)

# Panel 2d: pooled predicted curve
ax_pool = axes[1,1]
M2_pool = run(f'lnLP ~ FSTS_c + FSTSsq_c + {CTRL} + w2015 + w2023', d_pool_b)
fm_pool = d_pool_b['fsts_mean'].mean()  # weighted average (approx)
plot_predicted_curve(M2_pool, d_pool_b, fm_pool, 'Pooled', '#8250df', ax_pool, int(M2_pool.nobs))
ax_pool.set_xlabel('Export Intensity (FSTS)', fontsize=10)
ax_pool.set_ylabel('Predicted ln(Labour Productivity)', fontsize=10)
ax_pool.set_title(f'Pooled (2009+2015+2023) — M2 OLS-HC1', fontsize=11)
ax_pool.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax_pool.spines['top'].set_visible(False)
ax_pool.spines['right'].set_visible(False)
ax_pool.legend(fontsize=9)

fig2.suptitle('Figure 2: Predicted Internationalization–Performance Curves by Wave\nVietnam WBES — OLS M2 with HC1 SEs', fontsize=12)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_2_predicted_curves.png', dpi=300, bbox_inches='tight')
plt.close()
print("\nFigure 2 (2x2 combined) saved")

# Also save individual panels
for M2, d_b, fm, wlabel, col, _ in wave_info:
    fig, ax = plt.subplots(figsize=(7, 5))
    plot_predicted_curve(M2, d_b, fm, wlabel, col, ax, int(M2.nobs))
    ax.set_xlabel('Export Intensity (FSTS)', fontsize=11)
    ax.set_ylabel('Predicted ln(Labour Productivity)', fontsize=11)
    ax.set_title(f'Figure 2{chr(96+[w for _,_,_,w,_,_ in wave_info].index(wlabel)+1)}: Wave {wlabel} — I–P Curve\nVietnam WBES, OLS M2 (N={int(M2.nobs):,})', fontsize=11)
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    ax.legend(fontsize=10)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    tag = chr(96+[w for _,_,_,w,_,_ in wave_info].index(wlabel)+1)
    plt.savefig(f'{OUT}/figure_2{tag}.png', dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  figure_2{tag} ({wlabel}) saved")

# Pooled individual
fig, ax = plt.subplots(figsize=(7, 5))
plot_predicted_curve(M2_pool, d_pool_b, fm_pool, 'Pooled', '#8250df', ax, int(M2_pool.nobs))
ax.set_xlabel('Export Intensity (FSTS)', fontsize=11)
ax.set_ylabel('Predicted ln(Labour Productivity)', fontsize=11)
ax.set_title(f'Figure 2d: Pooled (2009+2015+2023) — I–P Curve\nVietnam WBES, OLS M2 (N={int(M2_pool.nobs):,})', fontsize=11)
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_2d.png', dpi=300, bbox_inches='tight')
plt.close()
print("  figure_2d (pooled) saved")

# ── FIGURE 3: TCI and DAI moderator coefficients by wave ─────────────────────
fig3, axes3 = plt.subplots(1, 2, figsize=(11, 5))

waves3     = ['2009', '2015', '2023']
colors3    = ['#1f6feb', '#d73a49', '#238636']
x          = np.arange(len(waves3))

# TCI linear interaction (M3: FSTS_c:TCI_z)
tci_betas = [mods09['M3'].params.get('FSTS_c:TCI_z',np.nan),
             mods15['M3'].params.get('FSTS_c:TCI_z',np.nan),
             mods23['M3'].params.get('FSTS_c:TCI_z',np.nan)]
tci_ses   = [mods09['M3'].bse.get('FSTS_c:TCI_z',np.nan),
             mods15['M3'].bse.get('FSTS_c:TCI_z',np.nan),
             mods23['M3'].bse.get('FSTS_c:TCI_z',np.nan)]

# DAI linear interaction (M4: FSTS_c:DAI_z)
dai_betas = [mods09['M4'].params.get('FSTS_c:DAI_z',np.nan),
             mods15['M4'].params.get('FSTS_c:DAI_z',np.nan),
             mods23['M4'].params.get('FSTS_c:DAI_z',np.nan)]
dai_ses   = [mods09['M4'].bse.get('FSTS_c:DAI_z',np.nan),
             mods15['M4'].bse.get('FSTS_c:DAI_z',np.nan),
             mods23['M4'].bse.get('FSTS_c:DAI_z',np.nan)]

for ax, betas, ses, title in [
    (axes3[0], tci_betas, tci_ses, 'TCI × FSTS Interaction (M3)'),
    (axes3[1], dai_betas, dai_ses, 'DAI × FSTS Interaction (M4)'),
]:
    ci95 = [1.96*se for se in ses]
    bars = ax.bar(x, betas, 0.55, color=colors3, alpha=0.82, yerr=ci95, capsize=5)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(waves3, fontsize=11)
    ax.set_ylabel('β (interaction, OLS-HC1)', fontsize=10)
    ax.set_title(title, fontsize=11)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for bar, b, se in zip(bars, betas, ses):
        if not np.isnan(b) and not np.isnan(se) and se>0:
            t_stat = abs(b/se)
            stars = '***' if t_stat>3.29 else '**' if t_stat>2.58 else '*' if t_stat>1.96 else ''
            ypos = b + (ci95[list(betas).index(b)] if not np.isnan(ci95[list(betas).index(b)]) else 0) + 0.03
            ax.text(bar.get_x()+bar.get_width()/2, ypos, f'{b:+.3f}{stars}',
                    ha='center', va='bottom', fontsize=8.5)

fig3.suptitle('Figure 3: Moderator Interaction Coefficients (TCI and DAI × FSTS)\nVietnam WBES 2009–2023', fontsize=12)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_3_moderator_marginals.png', dpi=300, bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# ── Save summary results ─────────────────────────────────────────────────────
import json
summary = {}
for wave, mods in [('2009', mods09), ('2015', mods15), ('2023', mods23)]:
    summary[wave] = {
        'M7_N': int(mods['M7'].nobs),
        'M7_TCI': round(float(mods['M7'].params.get('TCI_z',np.nan)), 3),
        'M7_DAI': round(float(mods['M7'].params.get('DAI_z',np.nan)), 3),
        'M7_adjR2': round(float(mods['M7'].rsquared_adj), 3),
        'M3_TCI_INT': round(float(mods['M3'].params.get('FSTS_c:TCI_z',np.nan)), 3),
        'M4_DAI_INT': round(float(mods['M4'].params.get('FSTS_c:DAI_z',np.nan)), 3),
        'M4_DAI_INT2': round(float(mods['M4'].params.get('FSTSsq_c:DAI_z',np.nan)), 3),
    }
summary['manuscript_targets'] = {
    '2009_M7_TCI': 0.215, '2009_M7_DAI': 0.175,
    '2015_M7_TCI': 0.128, '2015_M7_DAI': -0.044,
    '2023_M7_TCI': 0.123, '2023_M7_DAI': 0.095,
}
with open(f'{OUT}/results_p3.json','w') as f:
    json.dump(summary, f, indent=2)

print("\n=== REPLICATION SUMMARY (vs manuscript targets) ===")
targets = {'2009': (0.215, 0.175), '2015': (0.128, -0.044), '2023': (0.123, 0.095)}
for wave in ['2009','2015','2023']:
    t_tci, t_dai = targets[wave]
    r_tci = summary[wave]['M7_TCI']
    r_dai = summary[wave]['M7_DAI']
    print(f"  {wave}: TCI={r_tci:+.3f} (target {t_tci:+.3f}), DAI={r_dai:+.3f} (target {t_dai:+.3f})")

print("\nFigures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f"  {f}: {os.path.getsize(f'{OUT}/{f}'):,} bytes")
