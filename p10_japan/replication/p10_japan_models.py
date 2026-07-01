#!/usr/bin/env python3
"""P10 Japan 2025 — replication of all reported models and tables.

Data : data_wbes/raw_dta/Japan-2025-full-data.dta (inaugural WBES wave, N=2,168)
Spec : DV ln(d2/l1) winsorised 1/99; FSTS=(d3b+d3c)/100 mean-centred (+ d3c-only
       robustness); sector FE (a4a, 13 strata); HC1 robust SEs.
Run  : python3 p10_japan/replication/p10_japan_models.py   (from repo root)
Note : pyfixest is the reghdfe-equivalent used throughout the dissertation;
       re-validate with Stata before journal submission.

Outputs, in order:
  Table 1  Descriptive statistics
  Table 2  Pairwise correlations with ln labour productivity
  Table 4  Hierarchical I-P estimates (M1-M5) + d3c robustness
  Table 3  Extensive margin: who exports (LPM on P(exporter))
  Table 5  Robustness battery on the linear/quadratic export effect
  Exporter productivity premium
"""
import warnings

import numpy as np
import pandas as pd
import pyfixest as pf

warnings.filterwarnings('ignore')

df = pd.read_stata('data_wbes/raw_dta/Japan-2025-full-data.dta',
                   convert_categoricals=False)
cols = ['d2', 'l1', 'd3b', 'd3c', 'b2b', 'b5', 'c22b', 'h8', 'b8', 'h1',
        'b7a', 'a4a']
d = df[cols].apply(pd.to_numeric, errors='coerce')
d = d.where(~d.isin([-9, -8, -7, -6, -5, -4]))

lnlp = np.log(d['d2'].where(d['d2'] > 0) / d['l1'].where(d['l1'] > 0))
lnlp = lnlp.clip(lnlp.quantile(.01), lnlp.quantile(.99))
b = d['d3b'].where(d['d3b'].between(0, 100))
c = d['d3c'].where(d['d3c'].between(0, 100))
fsts = ((b.fillna(0) + c.fillna(0)) / 100).where(b.notna() | c.notna())
fo = d['b2b'].where(d['b2b'].between(0, 100))
age = 2025 - d['b5'].where(d['b5'].between(1800, 2025))
yn = lambda v: d[v].where(d[v].isin([1, 2])).map({1: 1.0, 2: 0.0})
tci = pd.concat([yn('h8'), yn('b8'), yn('h1')], axis=1).mean(axis=1)

J = pd.DataFrame({
    'lnlp': lnlp, 'fsts': fsts,
    'exporter': (fsts > 0).astype(float).where(fsts.notna()),
    'fdi10': (fo >= 10).astype(float).where(fo.notna()),
    'age': age.where((age >= 0) & (age <= 200)),
    'ln_age': np.log(age.where((age >= 0) & (age <= 200)) + 1),
    'dai': yn('c22b'), 'fem': yn('b7a'),
    'tci_raw': tci,
    'tci_z': (tci - tci.mean()) / tci.std(),
    'lnL': np.log(d['l1'].where(d['l1'] > 0)),
    'a4a': d['a4a'], 'fsts_dc': (c / 100).where(c.notna())})
fbar = J.fsts.mean()
J['fsts_c'] = J.fsts - fbar
J['fsts_c2'] = J.fsts_c ** 2
J['fXt'] = J.fsts_c * J.tci_z
J['fXd'] = J.fsts_c * J.dai
J['fdc_c'] = J.fsts_dc - J.fsts_dc.mean()
J['fdc_c2'] = J.fdc_c ** 2
J['lnL_z'] = (J.lnL - J.lnL.mean()) / J.lnL.std()

# ----------------------------------------------------------------- Table 1
print('=' * 64)
print('TABLE 1  Descriptive statistics (Japan 2025 WBES)')
print('=' * 64)
desc = ['lnlp', 'fsts', 'exporter', 'tci_raw', 'dai', 'fdi10', 'age', 'fem',
        'lnL']
for v in desc:
    s = J[v].dropna()
    print(f'   {v:10s} N={len(s):5d}  mean={s.mean():+8.3f}  sd={s.std():7.3f}'
          f'  min={s.min():+7.2f}  max={s.max():+8.2f}')
exp = J[J.fsts > 0]
print(f'   mean FSTS among exporters = {exp.fsts.mean()*100:.1f}%')
print(f'   share indirect>0 among exporters = '
      f'{100*(d.loc[exp.index, "d3b"].fillna(0) > 0).mean():.1f}%')

# ----------------------------------------------------------------- Table 2
print('=' * 64)
print('TABLE 2  Pairwise correlations with ln labour productivity')
print('=' * 64)
for v in ['fsts', 'exporter', 'tci_raw', 'dai', 'fdi10', 'age', 'fem', 'lnL']:
    pair = J[['lnlp', v]].dropna()
    r = pair['lnlp'].corr(pair[v])
    n = len(pair)
    t = r * np.sqrt((n - 2) / (1 - r ** 2))
    from scipy import stats as _st
    p = 2 * (1 - _st.t.cdf(abs(t), n - 2))
    print(f'   lnlp ~ {v:10s} r={r:+.3f}  (N={n}, p={p:.3f})')

# ----------------------------------------------------------------- Table 4
print('=' * 64)
print('TABLE 4  Hierarchical I-P estimates (DV: ln labour productivity)')
print('=' * 64)
MODELS = [
    ('M1', 'lnlp ~ fsts_c | a4a'),
    ('M2', 'lnlp ~ fsts_c + fsts_c2 | a4a'),
    ('M3', 'lnlp ~ fsts_c + fsts_c2 + fdi10 + ln_age + fem | a4a'),
    ('M4', 'lnlp ~ fsts_c + fsts_c2 + fdi10 + ln_age + fem + tci_z + dai | a4a'),
    ('M5', 'lnlp ~ fsts_c + fsts_c2 + fdi10 + ln_age + fem + tci_z + dai '
           '+ fXt + fXd | a4a'),
    ('R1 (d3c only)', 'lnlp ~ fdc_c + fdc_c2 + fdi10 + ln_age + fem | a4a'),
]
for label, fml in MODELS:
    rhs = fml.split('~')[1].split('|')[0]
    need = ['lnlp'] + [t.strip() for t in rhs.split('+')]
    fit = pf.feols(fml, data=J.dropna(subset=need), vcov='HC1')
    bb, pp = fit.coef(), fit.pvalue()
    print(f'== {label}  (N={int(fit._N)}, R2={fit._r2:.3f}) ==')
    for k in bb.index:
        print(f'   {k:10s} {bb[k]:+.4f} (p={pp[k]:.4f})')
    if 'fsts_c2' in bb and bb['fsts_c2'] < 0:
        print(f'   TP (algebraic) = '
              f'{(-bb["fsts_c"] / (2 * bb["fsts_c2"]) + fbar) * 100:.1f}%')

# ----------------------------------------------------------------- Table 3
print('=' * 64)
print('TABLE 3  Extensive margin: who exports (LPM, DV=exporter)')
print('=' * 64)
ext = 'exporter ~ tci_z + dai + fdi10 + ln_age + fem + lnL_z | a4a'
need = ['exporter', 'tci_z', 'dai', 'fdi10', 'ln_age', 'fem', 'lnL_z']
fit = pf.feols(ext, data=J.dropna(subset=need), vcov='HC1')
bb, pp = fit.coef(), fit.pvalue()
print(f'== (N={int(fit._N)}, R2={fit._r2:.3f}) ==')
for k in bb.index:
    print(f'   {k:10s} {bb[k]:+.4f} (p={pp[k]:.4f})')

# ----------------------------------------------------------------- Table 5
print('=' * 64)
print('TABLE 5  Robustness battery (linear + quadratic export effect)')
print('=' * 64)
# R2: add firm size control
r2 = J.dropna(subset=['lnlp', 'fsts_c', 'fsts_c2', 'fdi10', 'ln_age', 'fem',
                      'lnL_z'])
f2 = pf.feols('lnlp ~ fsts_c + fsts_c2 + fdi10 + ln_age + fem + lnL_z | a4a',
              data=r2, vcov='HC1')
# R3: domestic-owned only (fdi10==0)
r3 = J[J.fdi10 == 0].dropna(subset=['lnlp', 'fsts_c', 'fsts_c2', 'ln_age',
                                    'fem'])
f3 = pf.feols('lnlp ~ fsts_c + fsts_c2 + ln_age + fem | a4a', data=r3,
              vcov='HC1')
# R5: winsor 5/95
lp5 = lnlp.clip(lnlp.quantile(.05), lnlp.quantile(.95))
J5 = J.assign(lnlp5=lp5)
r5 = J5.dropna(subset=['lnlp5', 'fsts_c', 'fsts_c2', 'fdi10', 'ln_age', 'fem'])
f5 = pf.feols('lnlp5 ~ fsts_c + fsts_c2 + fdi10 + ln_age + fem | a4a',
              data=r5, vcov='HC1')
# R6: exporters-only intensity margin
r6 = J[J.fsts > 0].copy()
r6['fe_c'] = r6.fsts - r6.fsts.mean()
r6['fe_c2'] = r6.fe_c ** 2
r6 = r6.dropna(subset=['lnlp', 'fe_c', 'fe_c2', 'fdi10', 'ln_age', 'fem'])
f6 = pf.feols('lnlp ~ fe_c + fe_c2 + fdi10 + ln_age + fem | a4a', data=r6,
              vcov='HC1')
for label, fit, k1, k2 in [
        ('R2 +ln firm size', f2, 'fsts_c', 'fsts_c2'),
        ('R3 domestic-owned', f3, 'fsts_c', 'fsts_c2'),
        ('R5 winsor 5/95   ', f5, 'fsts_c', 'fsts_c2'),
        ('R6 exporters only ', f6, 'fe_c', 'fe_c2')]:
    bb, pp = fit.coef(), fit.pvalue()
    print(f'   {label}  N={int(fit._N):5d}  '
          f'b1={bb[k1]:+.3f}(p={pp[k1]:.3f})  '
          f'b2={bb[k2]:+.3f}(p={pp[k2]:.3f})')

# --------------------------------------------------------- exporter premium
print('=' * 64)
pe = J.dropna(subset=['lnlp', 'exporter', 'fdi10', 'ln_age', 'fem', 'a4a'])
fp = pf.feols('lnlp ~ exporter + fdi10 + ln_age + fem | a4a', data=pe,
              vcov='HC1')
print(f'Exporter productivity premium = '
      f'{fp.coef()["exporter"]:+.3f} '
      f'(p={fp.pvalue()["exporter"]:.4f}, N={int(fp._N)})')
print(f'FSTS mean = {fbar*100:.1f}% | exporters = {100*(J.fsts>0).mean():.1f}%')
