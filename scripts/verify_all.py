#!/usr/bin/env python3
"""verify_all.py — one-command reproducibility check for the dissertation.

Re-runs the core estimations from raw data and ASSERTS each headline number
against the locked values in data_wbes/analysis/CANONICAL_NUMBERS.md. A clean
PASS is the strongest evidence that the reported results are genuinely
reproducible from the data and code, not asserted. Intended for the committee /
reviewers / the author to run on demand.

Run:  python3 scripts/verify_all.py          (full; re-estimates from .dta)
      python3 scripts/verify_all.py --fast    (P6 meta only; CSV-based, ~5s)

Exit code 0 = all checks pass; 1 = at least one mismatch.
"""
import sys
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')
sys.path.insert(0, 'scripts')
FAST = '--fast' in sys.argv
TOL = 0.05            # tolerance on coefficients / TPs (percentage points / SD)
checks = []           # (label, expected, got, ok)


def chk(label, expected, got, tol=TOL):
    ok = abs(expected - got) <= tol
    checks.append((label, expected, got, ok))
    flag = 'PASS' if ok else 'FAIL'
    print(f'  [{flag}] {label}: expected {expected}, got {got:.3f}')


# ---------------------------------------------------------------- P6 meta
# Uses the GENUINE three-level random-effects pipeline (not a re-implementation)
print('== P6 three-level meta-analysis (forest_data.csv) ==')
import p6_meta_analysis as p6                                    # noqa: E402
r_pool, lo, hi, t2, t3, isq = p6.baseline()
chk('P6 pooled r', 0.074, r_pool, tol=0.005)
chk('P6 k studies', 238, p6.D.study_id.nunique(), tol=0)
chk('P6 K effects', 288, len(p6.D), tol=0)
for col, name, exp in [('icrv', 'ICRV', 17.35), ('cdai', 'cDAI', 1.23),
                       ('dpl', 'DPL', 0.56)]:
    Q, dfm, p, lv = p6.moderator(col)
    chk(f'P6 Q_M {name}', exp, float(Q), tol=0.5)

if not FAST:
    # ------------------------------------------------------------ P7 anchors
    print('== P7 50-economy anchors (re-estimate from .dta) ==')
    from p7_run_50econ import build as p7build, run_quad           # noqa: E402
    d = p7build()
    chk('P7 analytic rows', 88869, len(d), tol=0)
    chk('P7 economies', 50, d.economy.nunique(), tol=0)
    import pyfixest as pf                                          # noqa: E402
    fbar = d['fsts'].mean()
    dd = d.dropna(subset=['lp_z', 'fsts']).copy()
    dd['fc'] = dd['fsts'] - fbar
    dd['fc2'] = dd['fc'] ** 2
    m2 = pf.feols('lp_z ~ fc + fc2 | economy + year', data=dd,
                  vcov={'CRV1': 'economy'})
    b = m2.coef()
    tp2 = (-b['fc'] / (2 * b['fc2']) + fbar) * 100
    chk('P7 M2 N', 81022, int(m2._N), tol=0)
    chk('P7 M2 turning point %', 51.5, float(tp2), tol=0.5)
    dd5 = d.dropna(subset=['lp_z', 'fsts', 'fdi10', 'ln_age', 'tci_z', 'dai']).copy()
    dd5['fc'] = dd5['fsts'] - fbar
    dd5['fc2'] = dd5['fc'] ** 2
    m5 = pf.feols('lp_z ~ fc + fc2 + fdi10 + ln_age + tci_z + dai '
                  '| economy + year', data=dd5, vcov={'CRV1': 'economy'})
    b5 = m5.coef()
    tp5 = (-b5['fc'] / (2 * b5['fc2']) + fbar) * 100
    chk('P7 M5 N', 79080, int(m5._N), tol=0)
    chk('P7 M5 turning point %', 43.6, float(tp5), tol=0.6)

    # ------------------------------------------------------------ P10 Japan
    print('== P10 Japan headline (re-estimate from .dta) ==')
    df = pd.read_stata('data_wbes/raw_dta/Japan-2025-full-data.dta',
                       convert_categoricals=False)
    jd = df[['d2', 'l1', 'd3b', 'd3c', 'a4a']].apply(pd.to_numeric,
                                                     errors='coerce')
    jd = jd.where(~jd.isin([-9, -8, -7, -6, -5, -4]))
    lp = np.log(jd['d2'].where(jd['d2'] > 0) / jd['l1'].where(jd['l1'] > 0))
    lp = lp.clip(lp.quantile(.01), lp.quantile(.99))
    fs = ((jd['d3b'].where(jd['d3b'].between(0, 100)).fillna(0) +
           jd['d3c'].where(jd['d3c'].between(0, 100)).fillna(0)) / 100)
    fs = fs.where(jd['d3b'].notna() | jd['d3c'].notna())
    J = pd.DataFrame({'lp': lp, 'fc': fs - fs.mean(), 'a4a': jd['a4a']}).dropna()
    jm = pf.feols('lp ~ fc | a4a', data=J, vcov='HC1')
    chk('P10 Japan FSTS linear', 0.671, float(jm.coef()['fc']), tol=0.02)

    # ------------------------------------------------------------ JED paper
    print('== P11 JED digital-divide premium (re-estimate) ==')
    from p7_full_ladder import build as ddbuild                    # noqa: E402
    g, _ = ddbuild()
    gg = g.dropna(subset=['lp_z', 'dai', 'tci_z'])
    jp = pf.feols('lp_z ~ dai + tci_z | economy + year', data=gg,
                  vcov={'CRV1': 'economy'})
    chk('P11 pooled DAI premium', 0.241, float(jp.coef()['dai']), tol=0.02)

# ---------------------------------------------------------------- summary
n_pass = sum(c[3] for c in checks)
print('\n' + '=' * 56)
print(f'REPRODUCIBILITY CHECK: {n_pass}/{len(checks)} passed'
      f'{"  (--fast: P6 only)" if FAST else ""}')
fails = [c[0] for c in checks if not c[3]]
if fails:
    print('FAILED:', '; '.join(fails))
print('=' * 56)
sys.exit(0 if not fails else 1)
