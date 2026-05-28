#!/usr/bin/env python3
"""Independent Python reimplementation of the P6 three-level rma.mv (REML) model
to recompute the between-group moderator Q_M (matches metafor ~ factor(mod)).
Validates against the known baseline before trusting moderator tests.
Random structure ~1|study/effect => per-study block V = diag(vi)+s2e*I + s2s*J.
"""
import csv, numpy as np
from scipy.optimize import minimize
from scipy.stats import chi2

rows = list(csv.DictReader(open('p6/results/forest_data.csv')))
r = np.array([float(x['r_i']) for x in rows])
n = np.array([float(x['n']) for x in rows])
yi = np.arctanh(r)                 # Fisher z
vi = 1.0 / (n - 3.0)               # ZCOR sampling variance
study = [x['study_id'] for x in rows]

# group row indices by study (preserve order)
from collections import OrderedDict
groups = OrderedDict()
for i, s in enumerate(study):
    groups.setdefault(s, []).append(i)
blocks = [np.array(idx) for idx in groups.values()]

def reml_fit(X):
    """Fit 3-level REML given design X (N x p). Returns dict with beta, vb, s2s, s2e, ll."""
    N, p = X.shape
    def neg_ll(theta):
        s2s, s2e = np.exp(theta)            # ensure >=0
        logdetV = 0.0
        XtViX = np.zeros((p, p)); XtViy = np.zeros(p); ytViy = 0.0
        for idx in blocks:
            m = len(idx)
            Vb = np.diag(vi[idx] + s2e) + s2s * np.ones((m, m))
            Vinv = np.linalg.inv(Vb)
            sign, ld = np.linalg.slogdet(Vb)
            logdetV += ld
            Xb = X[idx]; yb = yi[idx]
            XtViX += Xb.T @ Vinv @ Xb
            XtViy += Xb.T @ Vinv @ yb
            ytViy += yb @ Vinv @ yb
        sign2, ld2 = np.linalg.slogdet(XtViX)
        XtViX_inv = np.linalg.inv(XtViX)
        beta = XtViX_inv @ XtViy
        rss = ytViy - XtViy @ beta
        ll = -0.5 * (logdetV + ld2 + rss)   # REML (drop const)
        return -ll
    # optimize on log scale for nonnegativity; start near baseline
    res = minimize(neg_ll, np.log([0.0014, 0.0088]), method='Nelder-Mead',
                   options={'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 5000})
    s2s, s2e = np.exp(res.x)
    # recompute final quantities
    p_ = X.shape[1]
    XtViX = np.zeros((p_, p_)); XtViy = np.zeros(p_)
    for idx in blocks:
        m = len(idx)
        Vb = np.diag(vi[idx] + s2e) + s2s * np.ones((m, m))
        Vinv = np.linalg.inv(Vb)
        Xb = X[idx]
        XtViX += Xb.T @ Vinv @ Xb
        XtViy += Xb.T @ Vinv @ yi[idx]
    vb = np.linalg.inv(XtViX)
    beta = vb @ XtViy
    return dict(beta=beta, vb=vb, s2s=s2s, s2e=s2e, ll=-res.fun)

def QM(X, n_mod):
    """Wald omnibus test on the last n_mod coefficients (the moderator contrasts)."""
    fit = reml_fit(X)
    b = fit['beta'][-n_mod:]
    Vb = fit['vb'][-n_mod:, -n_mod:]
    q = float(b @ np.linalg.inv(Vb) @ b)
    p = float(chi2.sf(q, n_mod))
    return q, n_mod, p, fit

def dummies(col, levels):
    vals = [x[col] for x in rows]
    # intercept + (L-1) dummies, drop first level as reference
    ref = levels[0]
    cols = [np.ones(len(rows))]
    for lv in levels[1:]:
        cols.append(np.array([1.0 if v == lv else 0.0 for v in vals]))
    return np.column_stack(cols), len(levels) - 1

# ---- validate baseline (intercept only) ----
base = reml_fit(np.ones((len(rows), 1)))
print("BASELINE  r_pooled=%.4f  s2_study(L3)=%.5f  s2_effect(L2)=%.5f"
      % (np.tanh(base['beta'][0]), base['s2s'], base['s2e']))
print("  (manuscript: r=0.074, s2_study=0.00135, s2_effect=0.00874)\n")

# ---- moderator between-group Q_M ----
for col, levels, ref_note in [
    ('icrv', ['I', 'II', 'III', 'FR', 'MX'], 'H1'),
    ('cdai', ['L', 'M', 'H'], 'H3'),
    ('dpl',  ['PRE', 'SPN', 'FOL'], 'H2'),
]:
    # use only levels present, in fixed order
    present = [lv for lv in levels if any(x[col] == lv for x in rows)]
    X, nmod = dummies(col, present)
    q, df, p, fit = QM(X, nmod)
    print("%-5s (%s) levels=%s  Q_M(%d)=%.2f  p=%.4f"
          % (col.upper(), ref_note, present, df, q, p))
print("\n  (manuscript: ICRV Q_M(4)=17.35 p=.002 | cDAI Q_M(2)=1.23 p=.541 | DPL Q_M(2)=0.56 p=.755)")
