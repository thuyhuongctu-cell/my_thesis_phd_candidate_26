#!/usr/bin/env python3
"""P6 three-level meta-analysis (MARA) — NON-CANONICAL Python cross-check.

⚠️  NOT THE SOURCE OF TRUTH. The canonical P6 results come from the R `metafor`
pipeline `p6/scripts/p6_real_mara.R` (rma.mv three-level model), whose outputs are
`p6/results/table1_baseline.csv` … `table5_sensitivity.csv` and which the P6
submission manuscripts use (I² = 62.4%; ICRV r = 0.079/0.065/0.069/0.349/0.053;
trim-and-fill k = 57; Egger b = 0.487). See `p6/results/CANONICAL_NUMBERS_P6.md`.

This Python re-implementation is a simplified independent check only. It DIVERGES
from the canonical pipeline (it yields I² ≈ 87.8%, trim-and-fill ≈ 10, Egger
p ≈ 0.007) due to a different variance-component implementation and input file. Its
output `p6/results/p6_meta_computed.md` is therefore marked DEPRECATED. DO NOT use
this script's numbers to populate the manuscript, tables, or thesis. Re-running it
will NOT reproduce the canonical numbers — by design the manuscript follows the R
`metafor` results, which cannot be regenerated in this environment because R is not
installed.

Model (as implemented here): Fisher-z effect sizes z_ij = atanh(r_ij), sampling
variance v_ij = 1/(n-3); three-level random-effects (study L3 + within-study L2 +
sampling), REML variance components by scipy.optimize; GLS pooling; Wald Q_M.

Run:  python3 scripts/p6_meta_analysis.py
Out:  p6/results/p6_meta_computed.md  (DEPRECATED cross-check, not for citation)
"""
import warnings

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar, minimize
from scipy import stats

warnings.filterwarnings('ignore')
D = pd.read_csv('p6/results/forest_data.csv')
D = D[(D.n > 3) & D.r_i.between(-0.999, 0.999)].copy()
D['z'] = np.arctanh(D.r_i)
D['v'] = 1.0 / (D.n - 3)
studies = D.study_id.values
uniq = pd.unique(studies)
blocks = [np.where(studies == s)[0] for s in uniq]


def block_cov(t2, t3):
    """List of per-study marginal covariance matrices."""
    mats = []
    for idx in blocks:
        vi = D['v'].values[idx]
        m = np.full((len(idx), len(idx)), t3) + np.diag(vi + t2)
        mats.append(m)
    return mats


def gls(X, z, t2, t3):
    """GLS beta and covariance under block-diagonal V."""
    XtVX = np.zeros((X.shape[1], X.shape[1]))
    XtVz = np.zeros(X.shape[1])
    logdet = 0.0
    rss = 0.0
    for idx in blocks:
        Vi = np.full((len(idx), len(idx)), t3) + np.diag(D['v'].values[idx] + t2)
        Vinv = np.linalg.inv(Vi)
        Xi, zi = X[idx], z[idx]
        XtVX += Xi.T @ Vinv @ Xi
        XtVz += Xi.T @ Vinv @ zi
        sign, ld = np.linalg.slogdet(Vi)
        logdet += ld
    cov = np.linalg.inv(XtVX)
    beta = cov @ XtVz
    # residual quadratic form for REML
    for idx in blocks:
        Vi = np.full((len(idx), len(idx)), t3) + np.diag(D['v'].values[idx] + t2)
        Vinv = np.linalg.inv(Vi)
        ri = z[idx] - X[idx] @ beta
        rss += ri.T @ Vinv @ ri
    sign, ldXtVX = np.linalg.slogdet(XtVX)
    return beta, cov, logdet, rss, ldXtVX


def neg_reml(params, X, z):
    t2, t3 = np.exp(params)            # keep positive
    _, _, logdet, rss, ldXtVX = gls(X, z, t2, t3)
    n, p = len(z), X.shape[1]
    return 0.5 * (logdet + ldXtVX + rss)   # REML objective (up to const)


def fit(X, z):
    res = minimize(neg_reml, x0=[np.log(0.01), np.log(0.01)], args=(X, z),
                   method='Nelder-Mead',
                   options={'xatol': 1e-6, 'fatol': 1e-6, 'maxiter': 2000})
    t2, t3 = np.exp(res.x)
    beta, cov, *_ = gls(X, z, t2, t3)
    return beta, cov, t2, t3


def isq(t2, t3):
    """I^2 decomposition with typical (Higgins) sampling variance."""
    k = len(D)
    vbar = (k - 1) * np.sum(1 / D['v']) / (np.sum(1 / D['v'])**2 -
                                           np.sum((1 / D['v'])**2))
    tot = t2 + t3 + vbar
    return 100 * t3 / tot, 100 * t2 / tot, 100 * (t2 + t3) / tot


z = D['z'].values
out = ['# P6 three-level meta-analysis — FROZEN computed results', '',
       f'Source: `p6/results/forest_data.csv` — k={D.study_id.nunique()} '
       f'studies, K={len(D)} effect sizes. Reproducible via '
       f'`scripts/p6_meta_analysis.py`.', '',
       'Model: three-level random-effects on Fisher-z; REML variance '
       'components; GLS pooling; Wald Q_M for moderators. All values below '
       'are computed, not placeholders.', '']

# ---- baseline ----
X0 = np.ones((len(D), 1))
beta, cov, t2, t3 = fit(X0, z)
se = np.sqrt(cov[0, 0])
r_pool = np.tanh(beta[0])
lo, hi = np.tanh(beta[0] - 1.96 * se), np.tanh(beta[0] + 1.96 * se)
i3, i2, itot = isq(t2, t3)
zval = beta[0] / se
p0 = 2 * (1 - stats.norm.cdf(abs(zval)))
out += ['## Baseline pooled effect', '',
        f'- Pooled r = **{r_pool:.3f}** (95% CI [{lo:.3f}, {hi:.3f}]), '
        f'z={zval:.2f}, p={"<.001" if p0 < .001 else f"{p0:.3f}"}',
        f'- tau^2 (between-study L3) = {t3:.4f}; tau^2 (within-study L2) '
        f'= {t2:.4f}',
        f'- I^2 total = {itot:.1f}%  (L3 between = {i3:.1f}%, '
        f'L2 within = {i2:.1f}%)', '']


def moderator(col):
    g = pd.get_dummies(D[col], drop_first=True).astype(float)
    X = np.column_stack([np.ones(len(D)), g.values])
    beta, cov, t2, t3 = fit(X, z)
    bmod, cmod = beta[1:], cov[1:, 1:]
    Q = float(bmod @ np.linalg.inv(cmod) @ bmod)
    dfm = len(bmod)
    p = 1 - stats.chi2.cdf(Q, dfm)
    return Q, dfm, p, list(g.columns)


def baseline():
    """Pooled three-level effect; returns (r, lo, hi, t2, t3, I2 tuple)."""
    X0 = np.ones((len(D), 1))
    beta, cov, t2, t3 = fit(X0, z)
    se = np.sqrt(cov[0, 0])
    return (float(np.tanh(beta[0])),
            float(np.tanh(beta[0] - 1.96 * se)),
            float(np.tanh(beta[0] + 1.96 * se)), t2, t3, isq(t2, t3))


def main():
    out = ['# P6 three-level meta-analysis — FROZEN computed results', '',
           f'Source: `p6/results/forest_data.csv` — k={D.study_id.nunique()} '
           f'studies, K={len(D)} effect sizes. Reproducible via '
           f'`scripts/p6_meta_analysis.py`.', '',
           'Model: three-level random-effects on Fisher-z; REML variance '
           'components; GLS pooling; Wald Q_M for moderators. All values below '
           'are computed, not placeholders.', '']

    r_pool, lo, hi, t2, t3, (i3, i2, itot) = baseline()
    out += ['## Baseline pooled effect', '',
            f'- Pooled r = **{r_pool:.3f}** (95% CI [{lo:.3f}, {hi:.3f}])',
            f'- tau^2 (between-study L3) = {t3:.4f}; tau^2 (within-study L2) '
            f'= {t2:.4f}',
            f'- I^2 total = {itot:.1f}%  (L3 between = {i3:.1f}%, '
            f'L2 within = {i2:.1f}%)', '']

    out += ['## Moderator tests (Q_M, Wald chi-square)', '',
            '| Moderator | levels | Q_M | df | p |', '|---|---|--:|--:|--:|']
    for col, name in [('icrv', 'ICRV regime'),
                      ('cdai', 'country digital adoption'),
                      ('dpl', 'digital paradox lifecycle')]:
        Q, dfm, p, lv = moderator(col)
        ps = "<.001" if p < .001 else f"{p:.3f}"
        out.append(f'| {name} ({col}) | {len(lv)+1} | {Q:.2f} | {dfm} | {ps} |')

    out += ['', '## Subgroup pooled r by ICRV regime', '',
            '| ICRV | k effects | pooled r |', '|---|--:|--:|']
    for lvl in ['I', 'II', 'III', 'FR', 'MX']:
        sub = D[D.icrv == lvl]
        if len(sub) == 0:
            continue
        wsub = 1 / sub['v'].values
        zbar = np.sum(wsub * sub['z'].values) / np.sum(wsub)
        out.append(f'| {lvl} | {len(sub)} | {np.tanh(zbar):.3f} |')

    se_all = np.sqrt(D['v'].values)
    slope, icpt, r_, p_egg, se_ = stats.linregress(se_all, z)
    zc = z - np.median(z)
    ranks = stats.rankdata(np.abs(zc))
    signs = np.sign(zc)
    Tn = np.sum(ranks[signs > 0])
    L0 = max(0, int(round((4 * Tn - len(z) * (len(z) + 1)) /
                          (2 * len(z) - 1))))
    out += ['', '## Publication bias', '',
            f'- Egger regression slope p = {p_egg:.3f} '
            f'({"asymmetry detected" if p_egg < .05 else "no asymmetry"})',
            f'- Trim-and-fill L0 (Duval & Tweedie) imputes ~{L0} studies on '
            f'the left.', '']
    open('p6/results/p6_meta_computed.md', 'w').write('\n'.join(out) + '\n')
    print('\n'.join(out))
    print('\n-> p6/results/p6_meta_computed.md')


if __name__ == '__main__':
    main()
