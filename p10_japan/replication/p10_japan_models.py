#!/usr/bin/env python3
"""P10 Japan 2025 — replication of all reported models.

Data : data_wbes/raw_dta/Japan-2025-full-data.dta (inaugural WBES wave, N=2,168)
Spec : DV ln(d2/l1) winsorised 1/99; FSTS=(d3b+d3c)/100 mean-centred (+ d3c-only
       robustness); sector FE (a4a, 13 strata); HC1 robust SEs.
Run  : python3 p10_japan/replication/p10_japan_models.py   (from repo root)
Note : pyfixest is the reghdfe-equivalent used throughout the dissertation;
       re-validate with Stata before journal submission.
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
    'fdi10': (fo >= 10).astype(float).where(fo.notna()),
    'ln_age': np.log(age.where((age >= 0) & (age <= 200)) + 1),
    'dai': yn('c22b'), 'fem': yn('b7a'),
    'tci_z': (tci - tci.mean()) / tci.std(),
    'a4a': d['a4a'], 'fsts_dc': (c / 100).where(c.notna())})
fbar = J.fsts.mean()
J['fsts_c'] = J.fsts - fbar
J['fsts_c2'] = J.fsts_c ** 2
J['fXt'] = J.fsts_c * J.tci_z
J['fXd'] = J.fsts_c * J.dai
J['fdc_c'] = J.fsts_dc - J.fsts_dc.mean()
J['fdc_c2'] = J.fdc_c ** 2

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
print(f'FSTS mean = {fbar*100:.1f}% | exporters = {100*(J.fsts>0).mean():.1f}%')
