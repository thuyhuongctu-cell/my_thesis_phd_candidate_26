#!/usr/bin/env python3
"""P5 China — replication with corrected spec.
Controls: lnEmp + firmage + foreigndummy (NO sector FE — matches do-file).
2012 TCI: e6+b8+CNo1+CNo3 (z-each, >=3/4)
2024 TCI: e6+b8+h1+h8 (z-each, >=3/4)
DAI: c22b+e6 (thin proxy, z-each)
"""
import pandas as pd, numpy as np, warnings
import pyreadstat
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from statsmodels.formula.api import ols
from scipy.stats import norm
warnings.filterwarnings('ignore')

UPLOAD = '/root/.claude/uploads/4342a099-4c09-46f0-a81b-f754f349e99f'
import os
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, 'manuscripts', 'figures', 'p5_china')
os.makedirs(OUT, exist_ok=True)

def safe_recode(df):
    """Recode WBES special values to NaN."""
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].replace([-9.0, -8.0, -7.0, -6.0], np.nan)
        elif df[col].dtype == object:
            # Try numeric conversion for string columns
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce').replace([-9,-8,-7,-6], np.nan)
            except:
                pass
    return df

# ── Load 2012 ─────────────────────────────────────────────────────────────────
print("=== China 2012 ===")
df12, meta12 = pyreadstat.read_dta(f'{UPLOAD}/3e36f503-China2012fullESN2700data.dta')
df12 = safe_recode(df12)
print(f"N={len(df12)}")
for v in ['d2','d3c','l1','b5','b2b','b8','e6','CNo1','CNo3','c22b']:
    nn = df12[v].notna().sum() if v in df12.columns else 0
    if v in df12.columns and nn>0:
        print(f"  {v}: N={nn}, min={df12[v].min():.0f}, max={df12[v].max():.0f}")
    elif v not in df12.columns:
        print(f"  {v}: NOT FOUND")

# ── Load 2024 (use pandas to avoid encoding error) ────────────────────────────
print("\n=== China 2024 ===")
df24 = pd.read_stata(f'{UPLOAD}/0331eb03-China2024fulldata.dta', convert_categoricals=False)
df24 = safe_recode(df24)
print(f"N={len(df24)}")
for v in ['d2','d3c','l1','b5','b2b','b8','e6','h1','h8','c22b']:
    nn = df24[v].notna().sum() if v in df24.columns else 0
    if v in df24.columns and nn>0:
        print(f"  {v}: N={nn}, min={df24[v].min():.0f}, max={df24[v].max():.0f}")
    elif v not in df24.columns:
        print(f"  {v}: NOT FOUND")

# ── Build analytic dataset ─────────────────────────────────────────────────────
def build_china(df, year, tci_items):
    """Construct China analytic variables. No sector FE per do-file."""
    df = df.copy()

    df['lnLP']       = np.where((df['d2']>0)&(df['l1']>0), np.log(df['d2']/df['l1']), np.nan)
    df['FSTS']       = np.where(df['d3c'].notna(), df['d3c']/100.0, np.nan)
    df['FSTS']       = df['FSTS'].clip(0, 1)
    df['FSTSsq']     = df['FSTS']**2
    df['lnEmp']      = np.where(df['l1']>0, np.log(df['l1']), np.nan)
    df['firmage']    = np.where((df['b5']>1900)&(df['b5']<=year), year-df['b5'], np.nan)
    df['foreigndummy']= np.where(df['b2b'].notna(), (df['b2b']>0).astype(float), np.nan)

    # Binary recode
    for item in ['b8','e6','c22b']:
        if item in df.columns:
            df[f'{item}_bin'] = np.where(df[item]==1, 1.0,
                                  np.where(df[item]==2, 0.0, np.nan))
        else:
            df[f'{item}_bin'] = np.nan

    for item in ['CNo1','CNo3','h1','h8']:
        if item in df.columns:
            df[f'{item}_bin'] = np.where(df[item]==1, 1.0,
                                  np.where(df[item]==2, 0.0, np.nan))
        else:
            df[f'{item}_bin'] = np.nan

    # TCI: z-standardize each item, rowmean, require >=3 of 4
    available_tci = [it for it in tci_items if df[it].notna().sum() > 100]
    print(f"  TCI items ({year}): {available_tci}")
    for it in available_tci:
        print(f"    {it}: N_nonmissing={df[it].notna().sum()}")

    mat_tci = pd.DataFrame({it: df[it] for it in available_tci})
    for c in mat_tci.columns:
        m,s = mat_tci[c].mean(), mat_tci[c].std()
        mat_tci[c] = (mat_tci[c]-m)/s if s>0 else 0.0

    comp_tci = mat_tci.mean(axis=1)
    min_tci  = 3 if len(available_tci) >= 4 else max(1, len(available_tci)-1)
    comp_tci[mat_tci.notna().sum(axis=1) < min_tci] = np.nan
    m,s = comp_tci.mean(), comp_tci.std()
    df['TCIfull'] = (comp_tci-m)/s if s>0 else comp_tci

    # DAI thin: c22b_bin + e6_bin (per do-file comment)
    dai_items = ['c22b_bin','e6_bin']
    avail_dai = [it for it in dai_items if df[it].notna().sum() > 100]
    mat_dai = pd.DataFrame({it: df[it] for it in avail_dai})
    for c in mat_dai.columns:
        m,s = mat_dai[c].mean(), mat_dai[c].std()
        mat_dai[c] = (mat_dai[c]-m)/s if s>0 else 0.0
    comp_dai = mat_dai.mean(axis=1)
    comp_dai[mat_dai.notna().sum(axis=1)<1] = np.nan
    m,s = comp_dai.mean(), comp_dai.std()
    df['DAIthin'] = (comp_dai-m)/s if s>0 else comp_dai

    # FSTS centering
    fm = df.loc[df['FSTS'].notna(),'FSTS'].mean()
    df['FSTS_c']   = df['FSTS'] - fm
    df['FSTSsq_c'] = df['FSTS_c']**2

    # Sample flags (NO sector control)
    BASE  = ['lnLP','FSTS_c','FSTSsq_c','lnEmp','firmage','foreigndummy']
    df['samp_base'] = df[BASE].notna().all(axis=1)
    df['samp_tci']  = df['samp_base'] & df['TCIfull'].notna()
    df['samp_dai']  = df['samp_base'] & df['DAIthin'].notna()
    df['samp_full'] = df['samp_tci'] & df['DAIthin'].notna()

    print(f"  base={df['samp_base'].sum()}, TCI={df['samp_tci'].sum()}, "
          f"DAI={df['samp_dai'].sum()}, full={df['samp_full'].sum()}")
    print(f"  FSTS mean={fm*100:.2f}%")
    df['fsts_mean'] = fm
    df['wave']      = year
    return df

CTRL_12 = ['e6_bin','b8_bin','CNo1_bin','CNo3_bin']
CTRL_24 = ['e6_bin','b8_bin','h1_bin','h8_bin']

df12 = build_china(df12, 2012, CTRL_12)
df24 = build_china(df24, 2024, CTRL_24)

# ── OLS helper ───────────────────────────────────────────────────────────────
CTRL = 'lnEmp + firmage + foreigndummy'

def run(formula, data):
    return ols(formula, data).fit(cov_type='HC1')

def run_wave(df, wave_label):
    d_b = df[df['samp_base']].copy()
    d_t = df[df['samp_tci']].copy()
    d_d = df[df['samp_dai']].copy()
    d_f = df[df['samp_full']].copy()
    fm  = df['fsts_mean'].iloc[0]

    M0 = run(f'lnLP ~ {CTRL}', d_b)
    M1 = run(f'lnLP ~ FSTS_c + {CTRL}', d_b)
    M2 = run(f'lnLP ~ FSTS_c + FSTSsq_c + {CTRL}', d_b)
    M5 = run(f'lnLP ~ TCIfull + {CTRL}', d_t)
    M6 = run(f'lnLP ~ DAIthin + {CTRL}', d_d)
    M7 = run(f'lnLP ~ TCIfull + DAIthin + {CTRL}', d_f)
    M8 = run(f'lnLP ~ FSTS_c + FSTSsq_c + TCIfull + DAIthin + {CTRL}', d_f)

    print(f"\n=== China {wave_label} ===")
    for mn, m in [('M0',M0),('M1',M1),('M2',M2),('M5',M5),('M6',M6),('M7',M7),('M8',M8)]:
        terms = ['FSTS_c','FSTSsq_c','TCIfull','DAIthin']
        present = [t for t in terms if t in m.params]
        s = f"{mn} (N={int(m.nobs)}, R²={m.rsquared_adj:.3f}): "
        for t in present:
            p = m.pvalues[t]
            stars = '***' if p<.001 else '**' if p<.01 else '*' if p<.05 else ''
            s += f"{t}={m.params[t]:+.3f}{stars}  "
        print(f"  {s}")

    b1 = M2.params.get('FSTS_c',0)
    b2 = M2.params.get('FSTSsq_c',0)
    if abs(b2) > 1e-6:
        tp = -b1/(2*b2) + fm
        print(f"  M2 turning point: {tp*100:.2f}%")

    return dict(M0=M0,M1=M1,M2=M2,M5=M5,M6=M6,M7=M7,M8=M8), d_b, d_t, d_d, d_f, fm

mods12, d_b12, d_t12, d_d12, d_f12, fm12 = run_wave(df12, '2012')
mods24, d_b24, d_t24, d_d24, d_f24, fm24 = run_wave(df24, '2024')

# ── Paternoster ───────────────────────────────────────────────────────────────
print("\n=== PATERNOSTER Z-TEST ===")
def pat_z(b1, se1, b2, se2):
    z = (b1-b2)/np.sqrt(se1**2+se2**2)
    p = 2*(1-norm.cdf(abs(z)))
    return z, p

z_F, p_F = pat_z(mods12['M2'].params['FSTS_c'], mods12['M2'].bse['FSTS_c'],
                  mods24['M2'].params['FSTS_c'], mods24['M2'].bse['FSTS_c'])
z_F2, p_F2 = pat_z(mods12['M2'].params['FSTSsq_c'], mods12['M2'].bse['FSTSsq_c'],
                    mods24['M2'].params['FSTSsq_c'], mods24['M2'].bse['FSTSsq_c'])
print(f"  FSTS  : z={z_F:.3f}  p={p_F:.3f}")
print(f"  FSTSsq: z={z_F2:.3f}  p={p_F2:.3f}")
print(f"  Manuscript targets: p≈0.412, p≈0.545")

# ── FIGURES ───────────────────────────────────────────────────────────────────
# Figure 2: Turning point forest plot
def tp_and_ci(M2, fm):
    b1 = M2.params.get('FSTS_c',0)
    b2 = M2.params.get('FSTSsq_c',0)
    if abs(b2)<1e-6: return None, None, None
    tp_c = -b1/(2*b2)
    tp   = tp_c + fm
    cov  = M2.cov_params()
    g1 = -1/(2*b2); g2 = b1/(2*b2**2)
    se_tp = np.sqrt(g1**2*M2.bse['FSTS_c']**2 + g2**2*M2.bse['FSTSsq_c']**2
                     + 2*g1*g2*cov.loc['FSTS_c','FSTSsq_c'])
    return tp, tp-1.96*se_tp, tp+1.96*se_tp

tp12, lo12, hi12 = tp_and_ci(mods12['M2'], fm12)
tp24, lo24, hi24 = tp_and_ci(mods24['M2'], fm24)

# Also get pooled
df_pool = pd.concat([df12, df24], ignore_index=True)
df_pool['wave2024'] = (df_pool['wave']==2024).astype(float)
d_pool_b = df_pool[df_pool['samp_base']].copy()
M2_pool = run(f'lnLP ~ FSTS_c + FSTSsq_c + {CTRL} + wave2024', d_pool_b)
fm_pool = d_pool_b['fsts_mean'].mean()
tp_p, lo_p, hi_p = tp_and_ci(M2_pool, fm_pool)

fig2, ax2 = plt.subplots(figsize=(8.5, 4.5))
for (wave, tp, lo, hi, N, col), y in zip([
    ('2012', tp12, lo12, hi12, int(mods12['M2'].nobs), '#1f6feb'),
    ('2024', tp24, lo24, hi24, int(mods24['M2'].nobs), '#d73a49'),
    ('Pooled', tp_p, lo_p, hi_p, int(M2_pool.nobs), '#238636'),
], [2,1,0]):
    lo_c = max(lo, 0) if lo is not None else 0
    hi_c = min(hi, 1.5) if hi is not None else 1.0
    ax2.plot([lo_c, hi_c], [y, y], color=col, linewidth=2.5, zorder=3)
    if tp is not None:
        ax2.plot(tp, y, 'o', color=col, markersize=9, zorder=4)
        ax2.text(hi_c+0.01, y,
                 f"{tp*100:.1f}% [{lo_c*100:.0f}%–{hi_c*100:.0f}%]\nN={N:,}",
                 va='center', fontsize=9, color=col)

ax2.axvspan(0.30, 0.60, alpha=0.08, color='green', label='Safe zone (30–60%)')
ax2.axvline(0.5, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
ax2.set_yticks([0,1,2])
ax2.set_yticklabels(['Pooled','2024','2012'], fontsize=11)
ax2.set_xlabel('Export Intensity Turning Point (FSTS)', fontsize=11)
ax2.set_title('Figure 2: Turning-Point Estimates with 95% CI\nChina Private Firms (M2 OLS-HC1)', fontsize=11)
ax2.text(0.01, -0.45,
         f"Paternoster z-tests: FSTS p={p_F:.3f}; FSTSsq p={p_F2:.3f}\n"
         f"→ {'Equality rejected' if (p_F<0.05 or p_F2<0.05) else 'Equality NOT rejected — threshold stability'}",
         fontsize=8, color='#555', va='bottom',
         bbox=dict(boxstyle='round,pad=0.4', fc='#fffbe6', ec='#ccc', alpha=0.9))
ax2.set_xlim(0, 1.5); ax2.set_ylim(-0.8, 2.8)
ax2.legend(loc='upper right', fontsize=9)
ax2.spines['top'].set_visible(False); ax2.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_2_turning_points.png', dpi=300, bbox_inches='tight')
plt.close()
print("\nFigure 2 saved")

# Figure 3: Predicted I-P curves overlay
fig3, ax3 = plt.subplots(figsize=(8.5, 5))
fsts_plot = np.linspace(0, 0.9, 300)
for wave, M2, fm, col, ls in [
    ('2012', mods12['M2'], fm12, '#1f6feb', '-'),
    ('2024', mods24['M2'], fm24, '#d73a49', '--'),
    ('Pooled', M2_pool, fm_pool, '#238636', ':'),
]:
    fsts_c = fsts_plot - fm
    b1 = M2.params.get('FSTS_c',0)
    b2 = M2.params.get('FSTSsq_c',0)
    pred = b1*fsts_c + b2*fsts_c**2
    pred -= pred[0]
    ax3.plot(fsts_plot, pred, color=col, linewidth=2.2, linestyle=ls,
             label=f'{wave} (N={int(M2.nobs):,})')
    if abs(b2)>1e-6 and b2<0:
        tp = -b1/(2*b2)+fm
        if 0<tp<0.9:
            ax3.axvline(tp, color=col, linewidth=0.8, linestyle=':', alpha=0.6)
            ax3.annotate(f'{tp*100:.0f}%', xy=(tp, b1*(tp-fm)+b2*(tp-fm)**2),
                         xytext=(tp+0.015, 0.02), fontsize=8, color=col)

ax3.axvspan(0.30, 0.60, alpha=0.06, color='green')
ax3.axhline(0, color='gray', linewidth=0.6, alpha=0.4)
ax3.set_xlabel('Export Intensity (FSTS)', fontsize=11)
ax3.set_ylabel('Δ ln(Labour Productivity) vs FSTS=0', fontsize=11)
ax3.set_title('Figure 3: Predicted I–P Curves by Wave\nChina Private Firms — OLS M2 (HC1)', fontsize=12)
ax3.legend(fontsize=10)
ax3.spines['top'].set_visible(False); ax3.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_3_predicted_curves.png', dpi=300, bbox_inches='tight')
plt.close()
print("Figure 3 saved")

# Figure 4: TCI/DAI bar charts
fig4, axes = plt.subplots(1, 2, figsize=(10, 4.5))
x = np.arange(2)
colors4 = ['#1f6feb','#d73a49']
for ax, coef, title, model in [(axes[0],'TCIfull','Tech Capability (TCI)','M5'),
                                 (axes[1],'DAIthin','Digital Adoption (DAI)','M6')]:
    betas = [mods12[model].params.get(coef,np.nan), mods24[model].params.get(coef,np.nan)]
    ses   = [mods12[model].bse.get(coef,np.nan),   mods24[model].bse.get(coef,np.nan)]
    ci95  = [1.96*se if not np.isnan(se) else 0 for se in ses]
    bars  = ax.bar(x, betas, 0.55, color=colors4, alpha=0.82, yerr=ci95, capsize=5)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(['2012','2024'], fontsize=11)
    ax.set_ylabel('β (z-std, OLS-HC1)', fontsize=10)
    ax.set_title(f'{title}\nDirect level-shift on ln(LP)', fontsize=11)
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    for bar, b, se in zip(bars, betas, ses):
        if not np.isnan(b) and not np.isnan(se) and se>0:
            t_stat = abs(b/se)
            stars = '***' if t_stat>3.29 else '**' if t_stat>2.58 else '*' if t_stat>1.96 else ''
            ax.text(bar.get_x()+bar.get_width()/2, b+1.96*se+0.005,
                    f'{b:+.3f}{stars}', ha='center', va='bottom', fontsize=9)

fig4.suptitle('Figure 4: TCI and DAI Direct Effect Coefficients by Wave\nChina (OLS-HC1, 95% CI)', fontsize=12)
plt.tight_layout()
plt.savefig(f'{OUT}/figure_4_level_shifts.png', dpi=300, bbox_inches='tight')
plt.close()
print("Figure 4 saved")

# ── Summary ───────────────────────────────────────────────────────────────────
print("\n=== REPLICATION SUMMARY ===")
targets = {
    '2012': {'N':2610, 'TP':49.37, 'TCI':0.2757, 'DAI':0.0772},
    '2024': {'N':1934, 'TP':47.19, 'TCI':0.4258, 'DAI':0.1876},
    'pat_FSTS': 0.412, 'pat_FSTSsq': 0.545,
}

for wave, mods, fm, d_b in [('2012',mods12,fm12,d_b12),('2024',mods24,fm24,d_b24)]:
    t = targets[wave]
    M2, M5, M6 = mods['M2'], mods['M5'], mods['M6']
    b1 = M2.params.get('FSTS_c',0)
    b2 = M2.params.get('FSTSsq_c',0)
    tp = (-b1/(2*b2)+fm)*100 if abs(b2)>1e-6 else np.nan
    print(f"China {wave}:")
    print(f"  M2 N={int(M2.nobs)} (target {t['N']})")
    print(f"  M2 turning point={tp:.1f}% (target {t['TP']:.1f}%)")
    print(f"  M5 TCI={M5.params.get('TCIfull',np.nan):.4f} (target {t['TCI']:.4f})")
    print(f"  M6 DAI={M6.params.get('DAIthin',np.nan):.4f} (target {t['DAI']:.4f})")

print(f"Paternoster: FSTS p={p_F:.3f} (target {targets['pat_FSTS']}), "
      f"FSTSsq p={p_F2:.3f} (target {targets['pat_FSTSsq']})")

print("\nFigures saved to", OUT)
for f in sorted(os.listdir(OUT)):
    if f.endswith('.png'):
        print(f"  {f}: {os.path.getsize(f'{OUT}/{f}'):,} bytes")
