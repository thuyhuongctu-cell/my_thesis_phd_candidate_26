"""
P5 China — estimates table generator for REPRO_2026-06-23.

Thin wrapper around build_and_run.py: re-uses its build_wave / lind_mehlum_utest
so there is a single source of truth for the data build. Adds the POOLED
all-frame M2 model (with wave2024 dummy) that the base runner does not print,
captures the inverted-U b2 coefficient + p-value, and emits a long-format
estimates.csv (model, term, coef, se, p, n).

Run from anywhere; reads raw from data_wbes/raw_dta/ via build_and_run defaults.
"""
import os
import sys
import importlib.util

import numpy as np
import pandas as pd
import statsmodels.api as sm

# Import the canonical runner as a module (single source of truth for the build).
_RUNNER = os.path.join(os.path.dirname(__file__), '..', 'python', 'build_and_run.py')
_spec = importlib.util.spec_from_file_location('build_and_run', _RUNNER)
br = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(br)

OUT = os.path.join(os.path.dirname(__file__), 'estimates.csv')

TERMS = ['const', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy', 'wave2024']


def quad_model(df, sample_col, pooled=False):
    """OLS lnLP ~ FSTS + FSTSsq + controls (+wave2024 if pooled), HC1."""
    d = df[df[sample_col]].copy()
    cols = ['FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy']
    if pooled:
        cols = cols + ['wave2024']
    X = sm.add_constant(d[cols].to_numpy())
    model = sm.OLS(d['lnLP'].to_numpy(), X).fit(cov_type='HC1')
    names = ['const'] + cols
    return model, names


def turning_point(model, names):
    b1 = model.params[names.index('FSTS')]
    b2 = model.params[names.index('FSTSsq')]
    if b2 >= 0:
        return None
    return -b1 / (2 * b2)


def emit_rows(rows, label, model, names):
    n = int(model.nobs)
    for i, nm in enumerate(names):
        rows.append({
            'model': label,
            'term': nm,
            'coef': round(float(model.params[i]), 6),
            'se': round(float(model.bse[i]), 6),
            'p': round(float(model.pvalues[i]), 6),
            'n': n,
        })


def main():
    df12_raw, _ = br.pyreadstat.read_dta(br.D2012)
    df24_raw, _ = br.pyreadstat.read_dta(br.D2024, encoding='utf-8')

    rows = []
    tp_summary = []

    for frame in ['all', 'mfg']:
        df12 = br.build_wave(df12_raw, 2012, mfg_filter=frame)
        df24 = br.build_wave(df24_raw, 2024, mfg_filter=frame)
        common = [c for c in df12.columns if c in df24.columns]
        pooled = pd.concat([df12[common], df24[common]], ignore_index=True)

        for label_wave, d in [('2012', df12), ('2024', df24)]:
            m, names = quad_model(d, 'sample_base', pooled=False)
            lbl = f'M2_{frame}_{label_wave}'
            emit_rows(rows, lbl, m, names)
            tp = turning_point(m, names)
            tp_summary.append((lbl, tp, int(m.nobs)))

        mp, namesp = quad_model(pooled, 'sample_base', pooled=True)
        lblp = f'M2_{frame}_pooled'
        emit_rows(rows, lblp, mp, namesp)
        tpp = turning_point(mp, namesp)
        tp_summary.append((lblp, tpp, int(mp.nobs)))

    out = pd.DataFrame(rows, columns=['model', 'term', 'coef', 'se', 'p', 'n'])
    out.to_csv(OUT, index=False)

    print("Wrote", OUT)
    print("\n--- TURNING POINTS ---")
    for lbl, tp, n in tp_summary:
        tps = f"{tp*100:.2f}%" if tp is not None else "n/a (b2>=0)"
        print(f"  {lbl:<22} TP={tps:<10} N={n}")

    print("\n--- INVERTED-U b2 (FSTSsq) ---")
    for lbl in out['model'].unique():
        r = out[(out['model'] == lbl) & (out['term'] == 'FSTSsq')].iloc[0]
        print(f"  {lbl:<22} b2={r['coef']:>9.4f}  se={r['se']:.4f}  p={r['p']:.3g}")


if __name__ == '__main__':
    main()
