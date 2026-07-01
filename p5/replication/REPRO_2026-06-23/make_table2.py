"""
P5 China — full Table 2 generator (all-frame M2) for the IJOEM manuscript.

Re-uses build_and_run.build_wave (single source of truth for the data build) and
emits, for each of 2012 / 2024 / pooled, the complete Table 2 the manuscript
prints: coefficient, HC1 SE, p-value, significance stars, R-squared, F-stat,
N, the delta-method turning point and its 95% CI. This is the authoritative
source for reconciling the manuscript's Table 2 to the committed raw .dta.

Run from anywhere; reads raw from data_wbes/raw_dta/ via build_and_run defaults.
"""
import os
import importlib.util

import numpy as np
import statsmodels.api as sm
import pandas as pd

_RUNNER = os.path.join(os.path.dirname(__file__), '..', 'python', 'build_and_run.py')
_spec = importlib.util.spec_from_file_location('build_and_run', _RUNNER)
br = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(br)


def stars(p):
    return '***' if p < .001 else '**' if p < .01 else '*' if p < .05 else ''


def fit(df, sample_col, pooled=False):
    d = df[df[sample_col]].copy()
    cols = ['FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy']
    if pooled:
        cols = cols + ['wave2024']
    X = sm.add_constant(d[cols].to_numpy())
    m = sm.OLS(d['lnLP'].to_numpy(), X).fit(cov_type='HC1')
    return m, ['const'] + cols


def tp_with_ci(m, names):
    """Delta-method turning point TP = -b1/(2 b2) and its 95% CI."""
    i1, i2 = names.index('FSTS'), names.index('FSTSsq')
    b1, b2 = m.params[i1], m.params[i2]
    tp = -b1 / (2 * b2)
    cov = m.cov_params()
    g1 = -1 / (2 * b2)
    g2 = b1 / (2 * b2 ** 2)
    se = np.sqrt(g1 ** 2 * m.bse[i1] ** 2 + g2 ** 2 * m.bse[i2] ** 2
                 + 2 * g1 * g2 * cov[i1, i2])
    return tp, tp - 1.96 * se, tp + 1.96 * se


def report(label, m, names):
    print(f"\n{'='*64}\n{label}  (N={int(m.nobs)})\n{'='*64}")
    for i, nm in enumerate(names):
        print(f"  {nm:<14} {m.params[i]:+.4f}{stars(m.pvalues[i]):<3} "
              f"(SE {m.bse[i]:.3f})  p={m.pvalues[i]:.4g}")
    tp, lo, hi = tp_with_ci(m, names)
    print(f"  R2={m.rsquared:.3f}  F={m.fvalue:.1f}  "
          f"TP={tp*100:.1f}%  CI=[{lo*100:.1f}%, {hi*100:.1f}%]")


def main():
    df12_raw, _ = br.pyreadstat.read_dta(br.D2012)
    df24_raw, _ = br.pyreadstat.read_dta(br.D2024, encoding='utf-8')

    df12 = br.build_wave(df12_raw, 2012, mfg_filter='all')
    df24 = br.build_wave(df24_raw, 2024, mfg_filter='all')
    common = [c for c in df12.columns if c in df24.columns]
    pooled = pd.concat([df12[common], df24[common]], ignore_index=True)

    m12, n12 = fit(df12, 'sample_base')
    m24, n24 = fit(df24, 'sample_base')
    mp, npn = fit(pooled, 'sample_base', pooled=True)

    report('M2 all-frame 2012', m12, n12)
    report('M2 all-frame 2024', m24, n24)
    report('M2 all-frame POOLED', mp, npn)


if __name__ == '__main__':
    main()
