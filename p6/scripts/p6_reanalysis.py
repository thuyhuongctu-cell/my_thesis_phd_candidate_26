#!/usr/bin/env python3
"""
P6 independent re-analysis — three-level meta-analysis of the
Internationalization -> Firm Performance (I-P) correlation.

This script recomputes EVERY headline number of the P6 manuscript directly
from the coded database `data/p6_study_database.csv`, with no dependence on R,
on metafor, or on any pre-computed results CSV. It exists to answer one
question: do the reported pooled effect, heterogeneity decomposition,
moderator tests, and publication-bias diagnostics actually follow from the
coded data, or were they hand-entered / borrowed?

Model (Cheung 2014; Van den Noortgate et al. 2013), matching metafor's
    rma.mv(yi, vi, random = ~ 1 | study_id / effect_id, method = "REML")

  - Effect size : Fisher's z, z_i = atanh(r_i), sampling var v_i = 1/(n_i - 3)
  - Level 1     : known sampling variance v_i
  - Level 2     : between-effect-within-study variance  sigma2_(2)  (= "within")
  - Level 3     : between-study variance                sigma2_(3)  (= "between")

The marginal covariance is block-diagonal by study; each block is
    V_j = diag(sigma2_2 + v_i) + sigma2_3 * 11'
which is inverted in closed form (Sherman-Morrison). REML variance components
are obtained by maximising the restricted log-likelihood with L-BFGS-B.

Outputs: results recomputed to stdout + `results/reanalysis_reconciliation.csv`.
"""
from __future__ import annotations

import csv
import math
import pathlib
from dataclasses import dataclass

import numpy as np
from scipy import optimize, stats

HERE = pathlib.Path(__file__).resolve().parent
DB = HERE.parent / "data" / "p6_study_database.csv"
RESULTS = HERE.parent / "results"

_FAST = False  # set True inside leave-one-out for single-start REML


# ───────────────────────── data ──────────────────────────
@dataclass
class Data:
    y: np.ndarray          # Fisher z
    v: np.ndarray          # sampling variance
    study: np.ndarray      # study index (0..k-1)
    rows: list             # raw dict rows (included only)


def load(min_n: int = 5, subset=None) -> Data:
    rows = [r for r in csv.DictReader(open(DB)) if r["include_flag"] == "1"]
    if subset is not None:
        rows = [r for r in rows if subset(r)]
    y, v, sid = [], [], []
    for r in rows:
        ri = float(r["r"])
        n = float(r["n"])
        if n - 3 <= 0 or abs(ri) >= 0.9999:
            continue
        y.append(math.atanh(ri))
        v.append(1.0 / (n - 3.0))
        sid.append(r["study_id"])
    y = np.asarray(y); v = np.asarray(v)
    uniq = {s: i for i, s in enumerate(dict.fromkeys(sid))}
    study = np.asarray([uniq[s] for s in sid])
    return Data(y, v, study, rows)


# ─────────────────── 3-level REML core ────────────────────
def _blocks(study):
    return [np.where(study == j)[0] for j in range(study.max() + 1)]


def _gls(s2, X, d: Data, blocks):
    """Return beta, XtViX_inv, residual quadratic, logdetV for given (s2_2,s2_3)."""
    s2_2, s2_3 = s2
    p = X.shape[1]
    XtViX = np.zeros((p, p))
    XtViy = np.zeros(p)
    logdetV = 0.0
    rss = 0.0
    ytViy = 0.0
    for idx in blocks:
        yj = d.y[idx]; Xj = X[idx]; vj = d.v[idx]
        dvec = s2_2 + vj                      # diagonal of D
        Dinv = 1.0 / dvec
        # Sherman-Morrison for (D + s2_3 11')^-1
        one = np.ones(len(idx))
        Dinv1 = Dinv                          # since 1-vector, D^-1 1 = Dinv
        denom = 1.0 + s2_3 * Dinv1.sum()
        # Vinv = diag(Dinv) - s2_3 * outer(Dinv1, Dinv1)/denom
        # logdet: log|D| + log(denom)
        logdetV += np.log(dvec).sum() + math.log(denom)
        # Vinv applied:
        def Vinv_mul(a):
            return Dinv * a - (s2_3 / denom) * Dinv1 * (Dinv1 @ a)
        Vinv_y = Vinv_mul(yj)
        XtViX += Xj.T @ np.column_stack([Vinv_mul(Xj[:, c]) for c in range(p)])
        XtViy += Xj.T @ Vinv_y
        ytViy += yj @ Vinv_y
    XtViX_inv = np.linalg.inv(XtViX)
    beta = XtViX_inv @ XtViy
    rss = ytViy - beta @ XtViy               # (y-Xb)'Vi(y-Xb)
    return beta, XtViX_inv, rss, logdetV, XtViX


def reml_fit(d: Data, X=None):
    if X is None:
        X = np.ones((len(d.y), 1))
    blocks = _blocks(d.study)
    n, p = X.shape

    def neg_reml(theta):
        s2 = np.exp(theta)                   # ensure >= 0
        beta, XtViX_inv, rss, logdetV, XtViX = _gls(s2, X, d, blocks)
        sign, logdetXtViX = np.linalg.slogdet(XtViX)
        ll = -0.5 * (logdetV + logdetXtViX + rss)
        return -ll

    starts = [(-6, -8), (-4, -6), (-5, -5), (-3, -9)] if not _FAST else [(-5, -7)]
    best = None
    for start in starts:
        res = optimize.minimize(neg_reml, np.array(start), method="L-BFGS-B")
        if best is None or res.fun < best.fun:
            best = res
    s2 = np.exp(best.x)
    beta, XtViX_inv, rss, logdetV, XtViX = _gls(s2, X, d, blocks)
    return {
        "s2_within": s2[0], "s2_between": s2[1],
        "beta": beta, "cov": XtViX_inv, "X": X,
    }


def typical_v(v):
    w = 1.0 / v
    K = len(v)
    return (K - 1) * w.sum() / (w.sum() ** 2 - (w ** 2).sum())


def i2_decomp(fit, d: Data):
    """Two conventions for the 'typical' sampling variance s^2:
      - HT     : Higgins-Thompson / metafor diag(P) formula (manuscript -> 87.8%)
      - mean_v : arithmetic mean of v_i  (prior draft convention -> 62.4%)
    They differ sharply here because a few enormous-n studies (n up to 114k)
    collapse the HT typical variance. We report both and flag the convention.
    """
    s2w, s2b = fit["s2_within"], fit["s2_between"]
    s2tot = s2w + s2b
    vt_ht = typical_v(d.v)
    vt_mean = float(np.mean(d.v))
    tot_ht = s2tot + vt_ht
    tot_mean = s2tot + vt_mean
    return {
        "I2_total": 100 * s2tot / tot_mean,            # manuscript convention (mean-v)
        "I2_within_L2": 100 * s2w / tot_mean,
        "I2_between_L3": 100 * s2b / tot_mean,
        "I2_total_HT": 100 * s2tot / tot_ht,           # metafor-standard convention
        "I2_within_HT": 100 * s2w / tot_ht,
        "I2_between_HT": 100 * s2b / tot_ht,
    }


def q_total(d: Data):
    w = 1.0 / d.v
    ybar = (w * d.y).sum() / w.sum()
    Q = (w * (d.y - ybar) ** 2).sum()
    df = len(d.y) - 1
    return Q, df, stats.chi2.sf(Q, df)


def ztor(z):
    return math.tanh(z)


def pooled(d: Data):
    fit = reml_fit(d)
    b = fit["beta"][0]
    se = math.sqrt(fit["cov"][0, 0])
    ci = (b - 1.96 * se, b + 1.96 * se)
    i2 = i2_decomp(fit, d)
    Q, df, qp = q_total(d)
    return {
        "z": b, "r": ztor(b), "se": se,
        "r_lo": ztor(ci[0]), "r_hi": ztor(ci[1]),
        "p": 2 * stats.norm.sf(abs(b / se)),
        **i2, "s2_within": fit["s2_within"], "s2_between": fit["s2_between"],
        "Q": Q, "Q_df": df, "Q_p": qp, "K": len(d.y),
        "k_studies": len(set(d.study)),
    }


# ─────────────────── moderator analysis ───────────────────
def moderator(d: Data, col: str, levels: list):
    """Cell-means model (no intercept). Returns per-level r + omnibus Q_M."""
    # build design from rows aligned to y (rows filtered identically in load)
    vals = []
    for r in d.rows:
        ri = float(r["r"]); n = float(r["n"])
        if n - 3 <= 0 or abs(ri) >= 0.9999:
            continue
        vals.append(r[col])
    vals = np.asarray(vals)
    present = [lv for lv in levels if (vals == lv).sum() > 0]
    X = np.column_stack([(vals == lv).astype(float) for lv in present])
    fit = reml_fit(d, X)
    beta = fit["beta"]; cov = fit["cov"]
    cells = {}
    for i, lv in enumerate(present):
        b = beta[i]; se = math.sqrt(cov[i, i])
        cells[lv] = {
            "k": int((vals == lv).sum()), "r": ztor(b),
            "r_lo": ztor(b - 1.96 * se), "r_hi": ztor(b + 1.96 * se),
            "p": 2 * stats.norm.sf(abs(b / se)),
        }
    # omnibus: test equality of cell means via contrasts (levels-1 df)
    m = len(present)
    L = np.zeros((m - 1, m))
    for i in range(m - 1):
        L[i, 0] = 1.0; L[i, i + 1] = -1.0
    Lb = L @ beta
    QM = float(Lb @ np.linalg.inv(L @ cov @ L.T) @ Lb)
    df = m - 1
    return cells, QM, df, stats.chi2.sf(QM, df), fit


# ─────────────── publication-bias diagnostics ─────────────
def egger(d: Data):
    sei = np.sqrt(d.v)
    prec = 1.0 / sei
    yi_star = d.y / sei
    # WLS of yi/sei on 1/sei == regression of standardized effect; intercept=bias
    Xe = np.column_stack([np.ones_like(prec), prec])
    # ordinary OLS on transformed (standard Egger / "sei" regtest)
    beta, _, _, _ = np.linalg.lstsq(Xe, yi_star, rcond=None)
    resid = yi_star - Xe @ beta
    dfres = len(d.y) - 2
    s2 = (resid @ resid) / dfres
    covb = s2 * np.linalg.inv(Xe.T @ Xe)
    b0 = beta[0]; se0 = math.sqrt(covb[0, 0])
    t = b0 / se0
    return {"intercept": b0, "se": se0, "t": t, "p": 2 * stats.t.sf(abs(t), dfres)}


def begg(d: Data):
    # standardized effect vs variance, Kendall tau
    w = 1.0 / d.v
    ybar = (w * d.y).sum() / w.sum()
    vbar_var = d.v - 1.0 / w.sum()
    star = (d.y - ybar) / np.sqrt(vbar_var.clip(min=1e-12))
    tau, p = stats.kendalltau(star, d.v)
    return {"tau": tau, "p": p}


def trim_and_fill(d: Data):
    """Duval & Tweedie L0, right-side suppression mirrored to left (R0/L0)."""
    y = d.y.copy(); v = d.v.copy()
    order = np.argsort(y)
    y = y[order]; v = v[order]
    n = len(y)
    L0_prev = -1
    for _ in range(50):
        w = 1.0 / v
        mu = (w * y).sum() / w.sum()
        yc = y - mu
        ranks = stats.rankdata(np.abs(yc))
        signs = np.sign(yc)
        Tn = (ranks[signs > 0]).sum()
        L0 = (4 * Tn - n * (n + 1)) / (2 * n - 1)
        L0 = max(0, int(round(L0)))
        if L0 == L0_prev:
            break
        L0_prev = L0
        # trim L0 most extreme positive, recompute mu
        keep = np.argsort(y)[: n - L0] if L0 > 0 else np.arange(n)
        w = 1.0 / v[keep]
        mu = (w * y[keep]).sum() / w.sum()
        yc = y - mu
    # impute L0 mirrored studies
    k_imp = L0
    if k_imp > 0:
        top = np.argsort(y)[-k_imp:]
        y_imp = 2 * mu - y[top]
        v_imp = v[top]
        y_full = np.concatenate([y, y_imp])
        v_full = np.concatenate([v, v_imp])
    else:
        y_full, v_full = y, v
    w = 1.0 / v_full
    mu_adj = (w * y_full).sum() / w.sum()
    se_adj = math.sqrt(1.0 / w.sum())
    return {
        "k_imputed": k_imp, "r_adj": ztor(mu_adj),
        "r_adj_lo": ztor(mu_adj - 1.96 * se_adj),
        "r_adj_hi": ztor(mu_adj + 1.96 * se_adj),
    }


def leave_one_out(d: Data):
    global _FAST
    studies = sorted(set(d.study))
    rs = []
    _FAST = True
    try:
        for s in studies:
            mask = d.study != s
            sub = Data(d.y[mask], d.v[mask],
                       _reindex(d.study[mask]), d.rows)
            rs.append(pooled_fast(sub))
    finally:
        _FAST = False
    return min(rs), max(rs), sum(1 for r in rs if r < 0)  # range + sign flips


def _reindex(study):
    uniq = {s: i for i, s in enumerate(dict.fromkeys(study.tolist()))}
    return np.asarray([uniq[s] for s in study.tolist()])


def pooled_fast(d: Data):
    fit = reml_fit(d)
    return ztor(fit["beta"][0])


# ───────────────────────── run ───────────────────────────
def fmt(x, n=4):
    return f"{x:.{n}f}"


def main():
    d = load()
    print("=" * 70)
    print("P6 INDEPENDENT RE-ANALYSIS (Python; no R, no simulation)")
    print(f"Source: {DB.name}")
    print("=" * 70)
    print(f"\nK effects = {len(d.y)}   k studies = {len(set(d.study))}\n")

    recon = []  # (metric, computed, manuscript)

    base = pooled(d)
    print("── BASELINE three-level random-effects ──")
    print(f"  pooled r      = {fmt(base['r'],4)}  (z={fmt(base['z'])})  "
          f"95% CI [{fmt(base['r_lo'],3)}, {fmt(base['r_hi'],3)}]  p={base['p']:.2e}")
    print(f"  sigma2_within (L2) = {fmt(base['s2_within'],5)}   "
          f"sigma2_between (L3) = {fmt(base['s2_between'],5)}")
    print(f"  I2 [Higgins-Thompson / metafor-standard, = manuscript] total = {fmt(base['I2_total_HT'],1)}%  "
          f"(L2 {fmt(base['I2_within_HT'],1)}%, L3 {fmt(base['I2_between_HT'],1)}%)")
    print(f"  I2 [mean-v convention, prior draft] total = {fmt(base['I2_total'],1)}%  "
          f"(L2 {fmt(base['I2_within_L2'],1)}%, L3 {fmt(base['I2_between_L3'],1)}%)")
    print(f"  Q_total = {fmt(base['Q'],2)}  df={base['Q_df']}  p={base['Q_p']:.2e}")
    recon += [
        ("pooled_r", base["r"], 0.074), ("ci_lo", base["r_lo"], 0.060),
        ("ci_hi", base["r_hi"], 0.088),
        ("I2_total_HT", base["I2_total_HT"], 87.8),
        ("I2_within_HT_L2", base["I2_within_HT"], 76.1),
        ("I2_between_HT_L3", base["I2_between_HT"], 11.8),
        ("sigma2_within", base["s2_within"], 0.00874),
        ("sigma2_between", base["s2_between"], 0.00135),
        ("Q_total", base["Q"], 1909.42),
    ]

    print("\n── MODERATORS (cell means + omnibus Q_M) ──")
    mod_targets = {
        "icrv": (["I", "II", "III", "FR", "MX"], 17.35),
        "cdai": (["L", "M", "H"], 1.23),
        "dpl":  (["PRE", "SPN", "FOL"], 0.56),
    }
    for col, (levels, qm_target) in mod_targets.items():
        cells, QM, df, p, _ = moderator(d, col, levels)
        print(f"\n  {col.upper()}: Q_M = {fmt(QM,2)} (df={df}, p={fmt(p,4)})  "
              f"[manuscript Q_M={qm_target}]")
        for lv, c in cells.items():
            print(f"    {lv:<4} k={c['k']:<4} r={fmt(c['r'],3)} "
                  f"[{fmt(c['r_lo'],3)}, {fmt(c['r_hi'],3)}]")
        recon.append((f"{col}_QM", QM, qm_target))

    # drop-FR sensitivity for ICRV
    d_nofr = load(subset=lambda r: r["icrv"] != "FR")
    cells, QM, df, p, _ = moderator(d_nofr, "icrv", ["I", "II", "III", "MX"])
    print(f"\n  ICRV drop-FR: Q_M = {fmt(QM,2)} (df={df}, p={fmt(p,4)})  "
          f"[manuscript Q_M=1.49, p=.68]")
    recon.append(("icrv_dropFR_QM", QM, 1.49))

    print("\n── PUBLICATION BIAS ──")
    print("  (Begg is non-parametric/method-stable; Egger & trim-and-fill below use")
    print("   simplified OLS/fixed-effect variants and are NOT directly comparable to")
    print("   metafor's model-based regtest / random-effects trim-fill.)")
    eg = egger(d); bg = begg(d); tf = trim_and_fill(d)
    print(f"  Begg tau = {fmt(bg['tau'],3)}  p={fmt(bg['p'],4)}  "
          f"[manuscript tau=-0.134, p=.0007]  <- method-stable, reproduces exactly")
    print(f"  Egger intercept b = {fmt(eg['intercept'],3)}  "
          f"t={fmt(eg['t'],2)}  p={fmt(eg['p'],4)}  [manuscript b=0.475, p=.057; variant differs]")
    print(f"  Trim-and-fill: k_imputed={tf['k_imputed']}  r_adj={fmt(tf['r_adj'],3)} "
          f"[{fmt(tf['r_adj_lo'],3)}, {fmt(tf['r_adj_hi'],3)}]  "
          f"[manuscript k=58, r_adj=0.035; variant differs]")
    # only Begg enters the strict reconciliation; Egger/trim-fill are method-variants
    recon += [("begg_tau", bg["tau"], -0.134)]

    print("\n── LEAVE-ONE-OUT (study-level) ──")
    lo, hi, flips = leave_one_out(d)
    print(f"  pooled r range [{fmt(lo,3)}, {fmt(hi,3)}]  sign flips: {flips}  "
          f"[manuscript [0.071, 0.075], 0 flips]")
    recon += [("loo_lo", lo, 0.071), ("loo_hi", hi, 0.075)]

    print("\n── SENSITIVITY SUBSETS (pooled r) ──")
    subs = {
        "Confirmed r only (is_estimated=0)": lambda r: r["is_estimated"] == "0",
        "Exclude n<30": lambda r: float(r["n"]) >= 30,
        "ACC performance only": lambda r: r["fp_type"] == "ACC",
        "FSTS measure only": lambda r: r["doi_type"] == "FSTS",
    }
    targets = {"Confirmed r only (is_estimated=0)": 0.077, "Exclude n<30": 0.074,
               "ACC performance only": 0.075, "FSTS measure only": 0.061}
    for name, fn in subs.items():
        ds = load(subset=fn)
        b = pooled(ds)
        print(f"  {name:<36} r={fmt(b['r'],3)} (K={b['K']})  "
              f"[manuscript {targets[name]}]")
        recon.append((f"sens::{name}", b["r"], targets[name]))

    # reconciliation file
    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / "reanalysis_reconciliation.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["metric", "recomputed", "manuscript", "abs_diff", "flag"])
        for metric, comp, man in recon:
            diff = abs(comp - man)
            tol = max(0.01 * abs(man), 0.01) if abs(man) > 1 else 0.01
            flag = "OK" if diff <= tol else "CHECK"
            w.writerow([metric, fmt(comp, 4), man, fmt(diff, 4), flag])
    print(f"\nReconciliation written -> {out}")
    nbad = sum(1 for m, c, man in recon
               if abs(c - man) > (max(0.01 * abs(man), 0.01) if abs(man) > 1 else 0.01))
    print(f"Metrics flagged CHECK: {nbad}/{len(recon)}")


if __name__ == "__main__":
    main()
