#!/usr/bin/env python3
"""P7 FULL LADDER on the 50-economy frame (incl. Japan), canonical spec.

Extends scripts/p7_run_50econ.py from 2 models (M2/M5) to the full moderation
ladder, so the standalone P7 manuscript can be reconciled to the thesis
canonical numbers. Spec is IDENTICAL to the thesis canonical (so the anchors
reproduce exactly):
  DV    = lp_z (z of winsorised ln(d2/l1) within economy-year) — currency-neutral
  FSTS  = (d3b + d3c)/100, mean-centred (fsts_c); fsts_c2 = fsts_c^2
  TCI_z = z of mean(h8 R&D, b8 ISO) within economy-year
  DAI   = c22b website (binary)
  FE    = economy + year (two-way) THROUGHOUT;  vcov CRV1 by economy
Controls/moderators added in the ladder:
  fdi10 (b2b>=10), ln_age (yr-b5), ln_size (ln l1), fem_owner (b4 majority),
  mgr_exp (b7 years, z), mgr_fem (b7a female top manager), grp (ICRV 1..6)

Ladder (all two-way FE):
  M1 linear | M2 quad [ANCHOR 81,022/51.5%] | M3 +basic controls
  M4 +TCI+DAI [ANCHOR 79,080/43.6%] | M5 +FSTS×TCI,FSTS²×TCI
  M6 +FSTS×DAI,FSTS²×DAI | M7 +manager | M8 +ICRV moderation (FSTS×grp,FSTS²×grp)

Run:  python3 scripts/p7_full_ladder.py
Out:  data_wbes/analysis/p7_full_ladder_results.md
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
from p7_run_50econ import read                    # noqa: E402
import pyfixest as pf                             # noqa: E402

GRP_INT = {"Advanced_innovation": 1, "Advanced_resource": 2, "Upper_mid": 3,
           "Lower_mid_transition": 4, "Emerging": 5, "SIDS_small": 6}


def yn(s):
    return s.where(s.isin([1, 2])).map({1: 1.0, 2: 0.0})


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
        chosen.setdefault(key, f)

    cols = ['d2', 'l1', 'd3b', 'd3c', 'b2b', 'b5', 'c22b', 'h8', 'b8',
            'b7', 'b7a', 'b4']
    rows = []
    for (c, y), f in sorted(chosen.items()):
        d = read(f, cols)
        if d is None or 'd2' not in d or 'l1' not in d:
            continue
        d = d.where(~d.isin([-9, -8, -7, -6, -5, -4]))
        lnlp = np.log(d['d2'].where(d['d2'] > 0) / d['l1'].where(d['l1'] > 0))
        lnlp = lnlp.clip(lnlp.quantile(.01), lnlp.quantile(.99))
        lp_z = (lnlp - lnlp.mean()) / lnlp.std()
        b = d['d3b'].where(d['d3b'].between(0, 100)) if 'd3b' in d \
            else pd.Series(index=d.index, dtype=float)
        cc = d['d3c'].where(d['d3c'].between(0, 100)) if 'd3c' in d \
            else pd.Series(index=d.index, dtype=float)
        fsts = ((b.fillna(0) + cc.fillna(0)) / 100).where(b.notna() | cc.notna())
        fsts = fsts.where(fsts.between(0, 1))
        fo = d['b2b'].where(d['b2b'].between(0, 100)) if 'b2b' in d \
            else pd.Series(index=d.index, dtype=float)
        age = (y - d['b5'].where(d['b5'].between(1800, y))) if 'b5' in d \
            else pd.Series(index=d.index, dtype=float)
        rd = yn(d['h8']) if 'h8' in d else pd.Series(index=d.index, dtype=float)
        iso = yn(d['b8']) if 'b8' in d else pd.Series(index=d.index, dtype=float)
        tci = pd.concat([rd, iso], axis=1).mean(axis=1)
        tci_z = (tci - tci.mean()) / tci.std() if tci.std(skipna=True) \
            and tci.std() > 0 else tci * np.nan
        exp = d['b7'].where(d['b7'].between(0, 80)) if 'b7' in d \
            else pd.Series(index=d.index, dtype=float)
        fown = d['b4'].where(d['b4'].between(0, 100)) if 'b4' in d \
            else pd.Series(index=d.index, dtype=float)
        rows.append(pd.DataFrame({
            'economy': c, 'year': y, 'grp': GRP_INT[icrv[c]],
            'lp_z': lp_z, 'fsts': fsts,
            'fdi10': (fo >= 10).astype(float).where(fo.notna()),
            'ln_age': np.log(age.where((age >= 0) & (age <= 200)) + 1),
            'ln_size': np.log(d['l1'].where(d['l1'] > 0)),
            'tci_z': tci_z, 'dai': yn(d['c22b']) if 'c22b' in d else np.nan,
            'mgr_exp': exp, 'mgr_fem': yn(d['b7a']) if 'b7a' in d else np.nan,
            'fem_owner': (fown > 50).astype(float).where(fown.notna())}))
    df = pd.concat(rows, ignore_index=True)
    fbar = df['fsts'].mean()
    df['fsts_c'] = df['fsts'] - fbar
    df['fsts_c2'] = df['fsts_c'] ** 2
    df['mgr_exp_z'] = (df['mgr_exp'] - df['mgr_exp'].mean()) / df['mgr_exp'].std()
    df['ln_size_z'] = (df['ln_size'] - df['ln_size'].mean()) / df['ln_size'].std()
    df['fXt'] = df['fsts_c'] * df['tci_z']
    df['f2Xt'] = df['fsts_c2'] * df['tci_z']
    df['fXd'] = df['fsts_c'] * df['dai']
    df['f2Xd'] = df['fsts_c2'] * df['dai']
    df['fXg'] = df['fsts_c'] * df['grp']
    df['f2Xg'] = df['fsts_c2'] * df['grp']
    return df, fbar


def tp(b, fbar):
    if 'fsts_c2' in b and b['fsts_c2'] < 0:
        return (-b['fsts_c'] / (2 * b['fsts_c2']) + fbar) * 100
    return None


LADDER = [
    ('M1 linear', 'fsts_c'),
    ('M2 quadratic [anchor]', 'fsts_c + fsts_c2'),
    ('M3 +controls', 'fsts_c + fsts_c2 + fdi10 + ln_age + ln_size_z + fem_owner'),
    ('M4 +TCI+DAI [anchor]', 'fsts_c + fsts_c2 + fdi10 + ln_age + tci_z + dai'),
    ('M5 +FSTSxTCI', 'fsts_c + fsts_c2 + fdi10 + ln_age + tci_z + dai + fXt + f2Xt'),
    ('M6 +FSTSxDAI', 'fsts_c + fsts_c2 + fdi10 + ln_age + tci_z + dai + fXd + f2Xd'),
    ('M7 +manager', 'fsts_c + fsts_c2 + fdi10 + ln_age + tci_z + dai + mgr_exp_z + mgr_fem'),
    ('M8 +ICRVmod', 'fsts_c + fsts_c2 + fdi10 + ln_age + tci_z + dai + grp + fXg + f2Xg'),
]


def main():
    df, fbar = build()
    print(f'analytic rows: {len(df)} | economies: {df.economy.nunique()} '
          f'| pairs: {df.groupby(["economy", "year"]).ngroups} '
          f'| FSTS mean: {fbar*100:.1f}%')
    out = ['# P7 full ladder — 50-economy frame (incl. Japan), canonical spec',
           '', f'Analytic frame: {len(df)} firms, {df.economy.nunique()} '
           f'economies. DV lp_z; two-way FE economy+year; CRV1 economy. '
           f'FSTS mean {fbar*100:.1f}%.', '',
           '| Model | N | b1 (FSTS) | p | b2 (FSTS²) | p | TP % | key moderators |',
           '|---|--:|--:|--:|--:|--:|--:|---|']
    for label, rhs in LADDER:
        need = ['lp_z'] + [t.strip() for t in rhs.split('+')]
        d = df.dropna(subset=[c for c in need if c])
        fit = pf.feols(f'lp_z ~ {rhs} | economy + year', data=d,
                       vcov={'CRV1': 'economy'})
        b, p = fit.coef(), fit.pvalue()
        t = tp(b, fbar)
        mod = ''
        for k in ['fXt', 'f2Xt', 'fXd', 'f2Xd', 'mgr_exp_z', 'mgr_fem',
                  'grp', 'fXg', 'f2Xg', 'tci_z', 'dai']:
            if k in b:
                star = '***' if p[k] < .001 else '**' if p[k] < .01 \
                    else '*' if p[k] < .05 else ''
                mod += f'{k}={b[k]:+.3f}{star} '
        b1 = f"{b['fsts_c']:+.3f}" if 'fsts_c' in b else '—'
        p1 = f"{p['fsts_c']:.3f}" if 'fsts_c' in b else '—'
        b2 = f"{b['fsts_c2']:+.3f}" if 'fsts_c2' in b else '—'
        p2 = f"{p['fsts_c2']:.3f}" if 'fsts_c2' in b else '—'
        tps = f'{t:.1f}' if t else '—'
        print(f'{label:24s} N={int(fit._N):6d} b1={b1} b2={b2} TP={tps}')
        out.append(f'| {label} | {int(fit._N):,} | {b1} | {p1} | {b2} | {p2} '
                   f'| {tps} | {mod.strip()} |')
    # per-ICRV TP in canonical M4 form (with controls — matches thesis 43.0% etc.)
    out += ['', '## Per-ICRV turning points (M4 form: + fdi10+ln_age+tci_z+dai)',
            '', '| ICRV group | N | b1 | b2 | TP % |', '|---|--:|--:|--:|--:|']
    pic = 'fsts_c + fsts_c2 + fdi10 + ln_age + tci_z + dai'
    for name, gi in GRP_INT.items():
        g = df[df.grp == gi].dropna(
            subset=['lp_z', 'fsts_c', 'fsts_c2', 'fdi10', 'ln_age', 'tci_z',
                    'dai'])
        if len(g) < 200:
            continue
        try:
            fit = pf.feols(f'lp_z ~ {pic} | economy + year', data=g,
                           vcov={'CRV1': 'economy'})
            b = fit.coef()
            gb = g['fsts'].mean()
            t = (-b['fsts_c'] / (2 * b['fsts_c2']) + gb) * 100 \
                if b['fsts_c2'] < 0 else None
            out.append(f'| {name} | {int(fit._N):,} | {b["fsts_c"]:+.3f} '
                       f'| {b["fsts_c2"]:+.3f} | {t:.1f} |'
                       if t else f'| {name} | {int(fit._N):,} '
                       f'| {b["fsts_c"]:+.3f} | {b["fsts_c2"]:+.3f} | — |')
        except Exception as e:
            out.append(f'| {name} | err {e} |')
    path = 'data_wbes/analysis/p7_full_ladder_results.md'
    open(path, 'w').write('\n'.join(out) + '\n')
    print(f'\n-> {path}')


if __name__ == '__main__':
    main()
