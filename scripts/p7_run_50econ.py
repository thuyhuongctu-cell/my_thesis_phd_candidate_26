#!/usr/bin/env python3
"""P7 re-estimation on the 50-economy frame (including Japan 2025).

Authorised by the author (NCS) for the first-publication dissertation: estimate
the I-P inverted-U on the full 50-economy descriptive frame with a fully
documented, reproducible specification, replacing the earlier vintage numbers.

Spec (mirrors scripts/stata/00_prep_data.do + p7_reestimate.do):
  lnLP   = ln(d2/l1), winsorised 1/99 within economy-year
  lp_z   = z-score of lnLP within economy-year   (currency-neutral)
  FSTS   = (d3b + d3c)/100 in [0,1]; 0 if both reported 0; missing if unanswered
  fsts_c = FSTS - mean(FSTS);  fsts_c2 = fsts_c^2
  Controls: fdi10 (b2b>=10), ln_age (survey year - b5), tci_z (z of mean(h8,b8)
            within economy-year), dai (c22b website)
  M2: lp_z ~ fsts_c + fsts_c2                      | economy + year, CRV1 economy
  M5: M2 + fdi10 + ln_age + tci_z + dai            | economy + year, CRV1 economy
  TP  = -b1/(2*b2) + mean(FSTS)   (reported in % of sales)
  Lind-Mehlum: slope sign + significance at FSTS min and max (one-sided)
  Per-ICRV-group TP from M5-form within each group; SIDS linear FIP model.

Run:  python3 scripts/p7_run_50econ.py
Out:  data_wbes/analysis/p7_50econ_results.md, p7_50econ_models.csv
"""
import glob
import sys
import warnings

import numpy as np
import pandas as pd

sys.path.insert(0, 'scripts')
warnings.filterwarnings('ignore')
from wbes_canon import parse                      # noqa: E402
from cd1_descriptives_pipeline import icrv_map    # noqa: E402
import pyfixest as pf                             # noqa: E402

ORDER = ["Advanced_innovation", "Advanced_resource", "Upper_mid",
         "Lower_mid_transition", "Emerging", "SIDS_small"]


def read(f, cols):
    try:
        import pyreadstat
        df, _ = pyreadstat.read_dta(f, usecols=cols)
        return df.apply(pd.to_numeric, errors='coerce')
    except Exception:
        try:
            df = pd.read_stata(f, convert_categoricals=False)
            return df[[c for c in cols if c in df.columns]].apply(
                pd.to_numeric, errors='coerce')
        except Exception:
            return None


def build():
    icrv = icrv_map()
    chosen = {}
    for f in sorted(glob.glob('data_wbes/raw_dta/*.dta')):
        m = parse(f)
        if m is None or not m['standard'] or m['panel']:
            continue
        if icrv.get(m['country']) is None:
            continue
        key = (m['country'], m['year'])
        if key not in chosen:
            chosen[key] = f

    cols = ['d2', 'l1', 'd3b', 'd3c', 'b2b', 'b5', 'c22b', 'h8', 'b8']
    rows = []
    for (c, y), f in sorted(chosen.items()):
        d = read(f, cols)
        if d is None or 'd2' not in d or 'l1' not in d:
            continue
        d = d.where(~d.isin([-9, -8, -7, -6, -5, -4]))
        lnlp = np.log(d['d2'].where(d['d2'] > 0) / d['l1'].where(d['l1'] > 0))
        # winsorise 1/99 within wave
        lo, hi = lnlp.quantile(0.01), lnlp.quantile(0.99)
        lnlp = lnlp.clip(lo, hi)
        lp_z = (lnlp - lnlp.mean()) / lnlp.std()
        b = d['d3b'].where(d['d3b'].between(0, 100)) if 'd3b' in d else pd.Series(index=d.index, dtype=float)
        cc = d['d3c'].where(d['d3c'].between(0, 100)) if 'd3c' in d else pd.Series(index=d.index, dtype=float)
        fsts = ((b.fillna(0) + cc.fillna(0)) / 100).where(b.notna() | cc.notna())
        fsts = fsts.where(fsts.between(0, 1))
        fo = d['b2b'].where(d['b2b'].between(0, 100)) if 'b2b' in d else pd.Series(index=d.index, dtype=float)
        fdi10 = (fo >= 10).astype(float).where(fo.notna())
        age = (y - d['b5'].where(d['b5'].between(1800, y))) if 'b5' in d else pd.Series(index=d.index, dtype=float)
        ln_age = np.log(age.where((age >= 0) & (age <= 200)) + 1)
        dai = d['c22b'].where(d['c22b'].isin([1, 2])).map({1: 1.0, 2: 0.0}) if 'c22b' in d else pd.Series(index=d.index, dtype=float)
        rd = d['h8'].where(d['h8'].isin([1, 2])).map({1: 1.0, 2: 0.0}) if 'h8' in d else pd.Series(index=d.index, dtype=float)
        iso = d['b8'].where(d['b8'].isin([1, 2])).map({1: 1.0, 2: 0.0}) if 'b8' in d else pd.Series(index=d.index, dtype=float)
        tci = pd.concat([rd, iso], axis=1).mean(axis=1)
        tci_z = (tci - tci.mean()) / tci.std() if tci.std() and tci.std() > 0 else tci * np.nan
        rows.append(pd.DataFrame({
            'economy': c, 'year': y, 'group': icrv[c],
            'lp_z': lp_z, 'fsts': fsts, 'fdi10': fdi10,
            'ln_age': ln_age, 'tci_z': tci_z, 'dai': dai}))
    df = pd.concat(rows, ignore_index=True)
    return df


def lind_mehlum(fit, b1n, b2n, fmin_c, fmax_c):
    """Slopes at the FSTS extremes with one-sided p (Lind & Mehlum 2010)."""
    b = fit.coef()
    V = fit._vcov
    names = list(fit.coefnames if hasattr(fit, 'coefnames') else fit._coefnames)
    i1, i2 = names.index(b1n), names.index(b2n)
    out = {}
    for tag, x in (('min', fmin_c), ('max', fmax_c)):
        s = b[b1n] + 2 * b[b2n] * x
        var = V[i1, i1] + 4 * x * V[i1, i2] + 4 * x * x * V[i2, i2]
        t = s / np.sqrt(var)
        out[tag] = (s, t)
    from scipy.stats import t as tdist
    dfree = max(int(fit._N) - len(names) - 1, 10)
    p_min = 1 - tdist.cdf(out['min'][1], dfree)        # H1: slope_min > 0
    p_max = tdist.cdf(out['max'][1], dfree)            # H1: slope_max < 0
    p_lm = max(p_min, p_max)
    return out['min'][1], out['max'][1], p_lm


def run_quad(d, label, controls=''):
    d = d.copy()
    fbar = d['fsts'].mean()
    d['fsts_c'] = d['fsts'] - fbar
    d['fsts_c2'] = d['fsts_c'] ** 2
    rhs = 'fsts_c + fsts_c2' + (' + ' + controls if controls else '')
    need = ['lp_z', 'fsts_c', 'fsts_c2'] + ([c.strip() for c in controls.split('+')] if controls else [])
    d = d.dropna(subset=[c for c in need if c])
    fit = pf.feols(f'lp_z ~ {rhs} | economy + year', data=d,
                   vcov={'CRV1': 'economy'})
    b = fit.coef()
    p = fit.pvalue()
    b1, b2 = b['fsts_c'], b['fsts_c2']
    tp = (-b1 / (2 * b2) + fbar) * 100 if b2 < 0 else None
    tmin, tmax, p_lm = lind_mehlum(fit, 'fsts_c', 'fsts_c2',
                                   d['fsts_c'].min(), d['fsts_c'].max())
    r2w = fit._r2_within if hasattr(fit, '_r2_within') else np.nan
    return {
        'model': label, 'N': int(fit._N), 'b1': b1, 'p1': p['fsts_c'],
        'b2': b2, 'p2': p['fsts_c2'],
        'TP_pct': tp, 'p_LM': p_lm, 'r2_within': r2w}


def run_linear(d, label, controls=''):
    d = d.copy()
    d['fsts_c'] = d['fsts'] - d['fsts'].mean()
    rhs = 'fsts_c' + (' + ' + controls if controls else '')
    need = ['lp_z', 'fsts_c'] + ([c.strip() for c in controls.split('+')] if controls else [])
    d = d.dropna(subset=[c for c in need if c])
    fit = pf.feols(f'lp_z ~ {rhs} | economy + year', data=d,
                   vcov={'CRV1': 'economy'})
    return {'model': label, 'N': int(fit._N),
            'b1': fit.coef()['fsts_c'], 'p1': fit.pvalue()['fsts_c'],
            'b2': np.nan, 'p2': np.nan, 'TP_pct': None, 'p_LM': np.nan,
            'r2_within': np.nan}


def main():
    df = build()
    print(f'analytic rows: {len(df)} | economies: {df.economy.nunique()} '
          f'| pairs: {df.groupby(["economy", "year"]).ngroups}')
    res = []
    A = df.dropna(subset=['lp_z', 'fsts'])
    res.append(run_quad(A, 'M2 (FSTS + FSTS^2, FE)'))
    res.append(run_quad(A, 'M5 (+ controls, FE)',
                        'fdi10 + ln_age + tci_z + dai'))
    # per-ICRV turning points (M5-form)
    for g in ORDER:
        sub = A[A.group == g]
        try:
            if g == 'SIDS_small':
                res.append(run_linear(sub, f'{g} (linear FIP)',
                                      'fdi10 + ln_age + tci_z + dai'))
                res.append(run_quad(sub, f'{g} (quad)',
                                    'fdi10 + ln_age + tci_z + dai'))
            else:
                res.append(run_quad(sub, f'{g}',
                                    'fdi10 + ln_age + tci_z + dai'))
        except Exception as e:
            print(f'  {g}: FAILED {e}')
    R = pd.DataFrame(res)
    R.to_csv('data_wbes/analysis/p7_50econ_models.csv', index=False)
    pd.set_option('display.width', 200)
    print(R.round(4).to_string(index=False))


if __name__ == '__main__':
    main()
