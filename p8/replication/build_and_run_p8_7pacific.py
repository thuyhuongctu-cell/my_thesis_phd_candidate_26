#!/usr/bin/env python3
"""P8 — 7 Pacific SIDS, built and estimated from the raw WBES .dta.

Canonical P8 sample = the SIDS_small (ICRV Group VI) economies of the P7 50-economy
pipeline, AFTER excluding Timor-Leste (not a World Bank Pacific Island Country; see
scripts/cd1_descriptives_pipeline.py). The seven economies are Fiji, Kiribati, Papua
New Guinea, Samoa, Solomon Islands, Tonga, Vanuatu.

Harmonisation is inherited verbatim from the P7 builder (dist/osf/P7_capstone/code/
p7_run_50econ.py): lp_z = z-score within economy-year of winsorised ln(d2/l1);
FSTS = (d3b+d3c)/100; fdi10 = b2b>=10; ln_age = ln(year-b5+1); tci_z = z of mean(h8,b8);
dai = c22b (website). This guarantees the SIDS numbers are on the same footing as the
mainland contrast.

Inference: two-way FE (economy + year), CRV1 cluster by economy, AND a wild-cluster
restricted bootstrap (Cameron-Gelbach-Miller 2008; Rademacher weights; null imposed via
FWL residualisation) appropriate for the 7-cluster design.

Outputs:
  p8/replication/data/p8_7pacific_pinned.csv     (pinned analytic dataset)
  p8/replication/reanalysis_7pacific/p8_7pacific_models.csv
"""
import importlib.util
import sys
import warnings

import numpy as np
import pandas as pd

sys.path.insert(0, 'scripts')
warnings.filterwarnings('ignore')

PACIFIC7 = ['Fiji', 'Kiribati', 'PapuaNewGuinea', 'Samoa',
            'SolomonIslands', 'Tonga', 'Vanuatu']
B_BOOT = 9999
SEED = 20260619


def load_p7_builder():
    spec = importlib.util.spec_from_file_location(
        'p7', 'dist/osf/P7_capstone/code/p7_run_50econ.py')
    p7 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(p7)
    return p7


def design(d, cols):
    """Two-way FE design matrix (economy + year dummies) + intercept."""
    parts = [pd.Series(1.0, index=d.index, name='const'), d[cols]]
    parts.append(pd.get_dummies(d.economy, prefix='e', drop_first=True).astype(float))
    parts.append(pd.get_dummies(d.year, prefix='y', drop_first=True).astype(float))
    X = pd.concat(parts, axis=1).astype(float)
    return X.loc[:, (X.nunique() > 1) | (X.columns == 'const')]


def ols(X, y):
    inv = np.linalg.pinv(X.T @ X)
    b = inv @ X.T @ y
    return b, inv, y - X @ b


def crv1(X, e, inv, groups):
    G = np.unique(groups)
    meat = np.zeros((X.shape[1], X.shape[1]))
    for g in G:
        m = groups == g
        s = X[m].T @ e[m]
        meat += np.outer(s, s)
    n, k = X.shape
    adj = (len(G) / (len(G) - 1)) * ((n - 1) / (n - k))
    V = inv @ meat @ inv * adj
    return np.sqrt(np.diag(V))


def wild_cluster_p(Xv, y, groups, j, rng, B=B_BOOT):
    """Restricted wild-cluster bootstrap p for coefficient j (H0: beta_j = 0).
    Rademacher cluster weights; null imposed by re-fitting without column j and
    bootstrapping the restricted residuals (CGM 2008)."""
    b, inv, e = ols(Xv, y)
    se = crv1(Xv, e, inv, groups)
    t_obs = b[j] / se[j]
    # restricted fit: drop column j, regress y on the rest
    keep = [c for c in range(Xv.shape[1]) if c != j]
    Xr = Xv[:, keep]
    br, invr, er = ols(Xr, y)
    yhat_r = Xr @ br
    G = np.unique(groups)
    count = 0
    for _ in range(B):
        w = rng.choice([-1.0, 1.0], size=len(G))
        wmap = dict(zip(G, w))
        wv = np.array([wmap[g] for g in groups])
        yb = yhat_r + er * wv
        bb, invb, eb = ols(Xv, yb)
        seb = crv1(Xv, eb, invb, groups)
        tb = bb[j] / seb[j]
        if abs(tb) >= abs(t_obs):
            count += 1
    return t_obs, (count + 1) / (B + 1)


def main():
    p7 = load_p7_builder()
    df = p7.build()
    S = df[df.group == 'SIDS_small'].copy()
    S = S[S.economy.isin(PACIFIC7)]
    S = S.dropna(subset=['lp_z', 'fsts']).copy()
    S['fsts_c'] = S.fsts - S.fsts.mean()
    S['fsts_c2'] = S['fsts_c'] ** 2

    # pin dataset
    keep = ['economy', 'year', 'lp_z', 'fsts', 'fsts_c', 'fsts_c2',
            'fdi10', 'ln_age', 'tci_z', 'dai']
    S[keep].to_csv('p8/replication/data/p8_7pacific_pinned.csv', index=False)

    print('=== P8 — 7 Pacific SIDS (Timor-Leste excluded), from raw .dta ===')
    print('Economies:', sorted(S.economy.unique()))
    print(f'N = {len(S)} | clusters = {S.economy.nunique()} | '
          f'exporters (FSTS>0) = {int((S.fsts > 0).sum())} '
          f'({100 * (S.fsts > 0).mean():.1f}%) | mean FSTS = {S.fsts.mean():.3f}')
    print(S.groupby('economy').agg(N=('lp_z', 'size'),
                                   exporters=('fsts', lambda x: int((x > 0).sum()))).to_string())

    rng = np.random.default_rng(SEED)
    specs = [
        ('M0 (size only)', ['ln_age', 'fdi10']),
        ('M1 (linear)', ['fsts_c', 'ln_age', 'fdi10']),
        ('M2 (quadratic)', ['fsts_c', 'fsts_c2', 'ln_age', 'fdi10']),
        ('M3 (+capability)', ['fsts_c', 'fsts_c2', 'tci_z', 'dai', 'ln_age', 'fdi10']),
    ]
    rows = []
    focal = {'fsts_c', 'fsts_c2', 'tci_z', 'dai'}
    for label, cols in specs:
        d = S.dropna(subset=cols).copy()
        X = design(d, cols)
        Xv = X.values
        y = d['lp_z'].values
        groups = d.economy.values
        b, inv, e = ols(Xv, y)
        se = crv1(Xv, e, inv, groups)
        bm = dict(zip(X.columns, b))
        sm = dict(zip(X.columns, se))
        for c in cols:
            if c not in focal:
                continue
            j = list(X.columns).index(c)
            t_obs, p_wild = wild_cluster_p(Xv, y, groups, j, rng)
            from math import erf, sqrt
            p_crv = 2 * (1 - 0.5 * (1 + erf(abs(bm[c] / sm[c]) / sqrt(2))))
            rows.append({'model': label, 'term': c, 'N': len(d),
                         'beta': round(bm[c], 4), 'se_crv1': round(sm[c], 4),
                         'p_crv1': round(p_crv, 4), 'p_wild': round(p_wild, 4)})
            print(f'  {label:18s} {c:8s} beta={bm[c]:+.3f} '
                  f'SE={sm[c]:.3f} p_CRV1={p_crv:.3f} p_wild={p_wild:.3f}')
    out = pd.DataFrame(rows)
    out.to_csv('p8/replication/reanalysis_7pacific/p8_7pacific_models.csv', index=False)
    print('\nsaved -> p8/replication/data/p8_7pacific_pinned.csv')
    print('saved -> p8/replication/reanalysis_7pacific/p8_7pacific_models.csv')


if __name__ == '__main__':
    main()
