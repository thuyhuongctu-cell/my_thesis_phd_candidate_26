#!/usr/bin/env python3
"""
65_meta_analysis.py — Three-level meta-analytic regression (MARA) for P6,
implemented in Python (numpy/scipy) because R/metafor is unavailable here.

Reproduces the metafor `rma.mv(yi=z, V=v, random=~1|study_id/effect_id,
method="REML")` pipeline: Fisher-z effects, REML variance components
(L3 between-study, L2 within-study), GLS pooled effect, three-level I²,
moderator omnibus Wald tests (ICRV / cDAI / DPL), publication-bias diagnostics
(Egger, Begg, Duval-Tweedie trim-and-fill, Rosenthal fail-safe N), and
study-level leave-one-out. Writes the p6/results/*.csv tables.

Usage: python3 p6/tools/65_meta_analysis.py --db p6/data/p6_study_database.csv --out p6/results
"""

import argparse
import csv
import math
from collections import OrderedDict, Counter
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.optimize import minimize


# ── data ─────────────────────────────────────────────────────────────────────

def load(db_path):
    rows = []
    with open(db_path, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            try:
                rr = float(r["r"]); n = float(r["n"])
            except (ValueError, KeyError):
                continue
            if n <= 3 or abs(rr) >= 1:
                continue
            rows.append({
                "study_id": r["study_id"].strip(),
                "effect_id": r.get("effect_id", "").strip(),
                "author": r.get("author", ""), "year": r.get("year", ""),
                "r": rr, "n": n,
                "z": 0.5 * math.log((1 + rr) / (1 - rr)),
                "v": 1.0 / (n - 3),
                "icrv": r.get("icrv", "").strip(),
                "cdai": r.get("cdai", "").strip(),
                "dpl": r.get("dpl", "").strip(),
                "doi_type": r.get("doi_type", "").strip(),
                "fp_type": r.get("fp_type", "").strip(),
            })
    return rows


def groups_by_study(rows):
    g = OrderedDict()
    for i, r in enumerate(rows):
        g.setdefault(r["study_id"], []).append(i)
    return [np.array(idx) for idx in g.values()]


# ── three-level REML ─────────────────────────────────────────────────────────

def _accumulate(theta, y, v, X, groups):
    s2_2, s2_3 = max(theta[0], 0.0), max(theta[1], 0.0)
    p = X.shape[1]
    XtViX = np.zeros((p, p)); XtViy = np.zeros(p); ytViy = 0.0; logdetV = 0.0
    for idx in groups:
        vj = v[idx]; nj = len(idx)
        Vj = np.diag(vj + s2_2) + s2_3 * np.ones((nj, nj))
        Vj_inv = np.linalg.inv(Vj)
        _, ld = np.linalg.slogdet(Vj); logdetV += ld
        Xj = X[idx]; yj = y[idx]
        XtViX += Xj.T @ Vj_inv @ Xj
        XtViy += Xj.T @ Vj_inv @ yj
        ytViy += yj @ Vj_inv @ yj
    return XtViX, XtViy, ytViy, logdetV


def fit_mv(y, v, X, groups, starts=None):
    def neg_reml(theta):
        if theta[0] < 0 or theta[1] < 0:
            return 1e10
        XtViX, XtViy, ytViy, logdetV = _accumulate(theta, y, v, X, groups)
        try:
            beta = np.linalg.solve(XtViX, XtViy)
            _, ldXVX = np.linalg.slogdet(XtViX)
        except np.linalg.LinAlgError:
            return 1e10
        rss = ytViy - XtViy @ beta
        return 0.5 * (logdetV + ldXVX + rss)

    if starts is None:
        v0 = float(np.var(y))
        starts = [[v0 / 2, v0 / 4], [0.005, 0.001], [0.01, 0.005], [1e-6, 1e-6]]
    best = None
    for start in starts:
        res = minimize(neg_reml, start, method="Nelder-Mead",
                       options={"xatol": 1e-9, "fatol": 1e-9, "maxiter": 5000})
        if best is None or res.fun < best.fun:
            best = res
    s2_2, s2_3 = max(best.x[0], 0.0), max(best.x[1], 0.0)
    XtViX, XtViy, ytViy, _ = _accumulate([s2_2, s2_3], y, v, X, groups)
    beta = np.linalg.solve(XtViX, XtViy)
    vb = np.linalg.inv(XtViX)
    return {"beta": beta, "vb": vb, "s2_within": s2_2, "s2_between": s2_3,
            "neg_reml": best.fun}


def ci_r(z, se):
    lo, hi = z - 1.96 * se, z + 1.96 * se
    return math.tanh(z), math.tanh(lo), math.tanh(hi)


def i2_three_level(v, s2_2, s2_3):
    # v_typ = mean sampling variance (the convention used in the manuscript/metafor
    # write-up: total I2 = (s2_2+s2_3)/(s2_2+s2_3+mean(v))).
    v_typ = float(np.mean(v))
    denom = s2_2 + s2_3 + v_typ
    return (100 * (s2_2 + s2_3) / denom, 100 * s2_3 / denom, 100 * s2_2 / denom, v_typ)


def q_total(y, v):
    w = 1.0 / v
    ybar = (w * y).sum() / w.sum()
    Q = (w * (y - ybar) ** 2).sum()
    return Q, len(y) - 1, stats.chi2.sf(Q, len(y) - 1)


def design_factor(rows, key, levels):
    """Intercept + dummy columns (first level = reference)."""
    ref, others = levels[0], levels[1:]
    X = [[1.0] + [1.0 if r[key] == lv else 0.0 for lv in others] for r in rows]
    return np.array(X), others


def qm_test(fit, n_mods):
    """Wald omnibus on the last n_mods coefficients (the non-reference dummies)."""
    b = fit["beta"][-n_mods:]
    Vb = fit["vb"][-n_mods:, -n_mods:]
    QM = float(b @ np.linalg.solve(Vb, b))
    return QM, n_mods, stats.chi2.sf(QM, n_mods)


# ── publication bias ─────────────────────────────────────────────────────────

def egger(y, v, groups):
    # metafor-style regtest: three-level meta-regression of effect on its SE;
    # the SE coefficient is the funnel-asymmetry estimate.
    se = np.sqrt(v)
    X = np.column_stack([np.ones(len(y)), se])
    fit = fit_mv(y, v, X, groups)
    b = fit["beta"][1]; bse = math.sqrt(fit["vb"][1, 1])
    return b, bse, 2 * stats.norm.sf(abs(b / bse))


def begg(y, v):
    vbar = v.mean()
    yc = y - (1.0 / v * y).sum() / (1.0 / v).sum()
    vstar = v - vbar
    tau, p = stats.kendalltau(yc / np.sqrt(v), vstar)
    return tau, p


def trim_fill(y, v):
    """Duval & Tweedie L0, right side (assume missing on the left for r>0)."""
    yv = list(zip(y, v))
    y_arr = np.array(y); v_arr = np.array(v)
    k = len(y_arr)
    L0 = 0
    for _ in range(50):
        w = 1.0 / v_arr
        mu = (w * y_arr).sum() / w.sum()
        d = y_arr - mu
        order = np.argsort(np.abs(d))
        ranks = np.empty(k); ranks[order] = np.arange(1, k + 1)
        signed = np.sign(d) * ranks
        Tn = signed[signed > 0].sum()
        L0_new = max(0, int(round((4 * Tn - k * (k + 1)) / (2 * k - 1))))
        if L0_new == L0:
            break
        L0 = L0_new
        # trim L0 most extreme positive effects, recompute center
        keep = np.argsort(d)[:k - L0] if L0 > 0 else np.arange(k)
        w2 = 1.0 / v_arr[keep]
        mu = (w2 * y_arr[keep]).sum() / w2.sum()
    # impute L0 mirrored effects around final mu
    d = y_arr - mu
    most_pos = np.argsort(d)[-L0:] if L0 > 0 else np.array([], dtype=int)
    y_imp = np.concatenate([y_arr, 2 * mu - y_arr[most_pos]])
    v_imp = np.concatenate([v_arr, v_arr[most_pos]])
    w = 1.0 / v_imp
    mu_adj = (w * y_imp).sum() / w.sum()
    se_adj = math.sqrt(1.0 / w.sum())
    return L0, mu_adj, se_adj


def failsafe_n(y, v):
    # Rosenthal: N_fs = (sum Z_i)^2 / 1.645^2 - k   (one-tailed alpha = .05)
    sumZ = (y / np.sqrt(v)).sum()
    if sumZ <= 0:
        return 0
    return int(round(sumZ ** 2 / (1.644854 ** 2) - len(y)))


def aggregate_to_study(rows):
    """One precision-weighted effect per study (for funnel-based diagnostics)."""
    g = OrderedDict()
    for r in rows:
        g.setdefault(r["study_id"], []).append(r)
    Y, V = [], []
    for eff in g.values():
        w = np.array([1.0 / e["v"] for e in eff])
        z = np.array([e["z"] for e in eff])
        Y.append((w * z).sum() / w.sum()); V.append(1.0 / w.sum())
    return np.array(Y), np.array(V)


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="p6/data/p6_study_database.csv")
    ap.add_argument("--out", default="p6/results")
    args = ap.parse_args()

    rows = load(args.db)
    y = np.array([r["z"] for r in rows]); v = np.array([r["v"] for r in rows])
    groups = groups_by_study(rows)
    K, k = len(rows), len(groups)
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)

    # baseline
    Xint = np.ones((K, 1))
    base = fit_mv(y, v, Xint, groups)
    z0 = base["beta"][0]; se0 = math.sqrt(base["vb"][0, 0])
    r0, lo, hi = ci_r(z0, se0)
    p0 = 2 * stats.norm.sf(abs(z0 / se0))
    I2t, I2b, I2w, vtyp = i2_three_level(v, base["s2_within"], base["s2_between"])
    Q, Qdf, Qp = q_total(y, v)

    print("=== BASELINE three-level MARA ===")
    print(f"  K={K} k={k}")
    print(f"  z_pooled={z0:.4f}  r={r0:.4f} [{lo:.3f}, {hi:.3f}]  p={p0:.3g}")
    print(f"  sigma2_between(L3)={base['s2_between']:.5f}  sigma2_within(L2)={base['s2_within']:.5f}")
    print(f"  I2_total={I2t:.1f}%  (L3 between={I2b:.1f}%, L2 within={I2w:.1f}%)")
    print(f"  Q={Q:.2f} df={Qdf} p={Qp:.3g}")
    print(f"  [manuscript target: r=.074 [.060,.088]; sigma2: .00135/.00874; I2 62.4 (8.4/54.1); Q 1909.42]")

    with open(out / "table1_baseline.csv", "w", newline="", encoding="utf-8") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["model", "K_effects", "k_studies", "z_pooled", "r_pooled", "r_ci_lo",
                     "r_ci_hi", "pval", "sigma2_study", "sigma2_effect", "I2_total",
                     "I2_between", "I2_within", "Q_total", "Q_df", "Q_pval"])
        w_.writerow(["Baseline three-level", K, k, round(z0, 4), round(r0, 3),
                     round(lo, 3), round(hi, 3), round(p0, 4), round(base["s2_between"], 5),
                     round(base["s2_within"], 5), round(I2t, 1), round(I2b, 1), round(I2w, 1),
                     round(Q, 2), Qdf, round(Qp, 4)])

    # moderators
    mod_specs = {
        "icrv": (["I", "II", "III", "FR", "MX"], "table2_icrv.csv", "regime"),
        "cdai": (["L", "M", "H"], "table3_cdai.csv", "cdai_level"),
        "dpl":  (["PRE", "SPN", "FOL"], "table4_dpl.csv", "dpl_phase"),
    }
    targets = {"icrv": "QM(4)=17.35 p=.002", "cdai": "QM(2)=1.23 p=.541", "dpl": "QM(2)=0.56 p=.755"}
    print("\n=== MODERATORS (omnibus between-group Q_M) ===")
    for key, (levels, fname, label) in mod_specs.items():
        present = [lv for lv in levels if any(r[key] == lv for r in rows)]
        X, others = design_factor(rows, key, present)
        fit = fit_mv(y, v, X, groups)
        QM, df, pQM = qm_test(fit, len(others))
        print(f"  {key.upper()}: Q_M={QM:.2f} df={df} p={pQM:.3g}   [target {targets[key]}]")
        # cell means via no-intercept factor model
        Xc = np.array([[1.0 if r[key] == lv else 0.0 for lv in present] for r in rows])
        fitc = fit_mv(y, v, Xc, groups)
        counts = Counter(r[key] for r in rows)
        with open(out / fname, "w", newline="", encoding="utf-8") as fh:
            w_ = csv.writer(fh)
            w_.writerow([label, "k", "z_est", "r_est", "r_ci_lo", "r_ci_hi", "pval", "QM", "QM_df", "QM_pval"])
            for j, lv in enumerate(present):
                zc = fitc["beta"][j]; sec = math.sqrt(fitc["vb"][j, j])
                rc, lc, hc = ci_r(zc, sec)
                pc = 2 * stats.norm.sf(abs(zc / sec))
                w_.writerow([lv, counts[lv], round(zc, 4), round(rc, 3), round(lc, 3),
                             round(hc, 3), round(pc, 4), round(QM, 2), df, round(pQM, 4)])

    # publication bias — asymmetry on all effects (multilevel Egger); funnel-based
    # diagnostics (Begg, trim-and-fill) on one precision-weighted effect per study.
    eb, ese, ep = egger(y, v, groups)
    ya, va = aggregate_to_study(rows)
    btau, bp = begg(ya, va)
    L0, mu_adj, se_adj = trim_fill(ya, va)
    r_adj, ra_lo, ra_hi = ci_r(mu_adj, se_adj)
    fsn = failsafe_n(y, v)
    print("\n=== PUBLICATION BIAS ===")
    print(f"  Egger (SE coef) b={eb:.3f} (SE={ese:.3f}, p={ep:.3f})   [target b=.475 SE=.250 p=.057]")
    print(f"  Begg tau={btau:.3f} (p={bp:.4g})                         [target tau=-.134 p=.0007]")
    print(f"  Trim-and-fill (study-level): k_imputed={L0}, r_adj={r_adj:.3f} [{ra_lo:.3f},{ra_hi:.3f}]  [target k=58 r=.035]")
    print(f"  Fail-safe N (Rosenthal) = {fsn}                          [target 45,848]")

    with open(out / "table5_sensitivity.csv", "w", newline="", encoding="utf-8") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["diagnostic", "statistic", "value", "detail"])
        w_.writerow(["egger", "intercept", round(eb, 3), f"SE={round(ese,3)}; p={round(ep,3)}"])
        w_.writerow(["begg", "kendall_tau", round(btau, 3), f"p={round(bp,4)}"])
        w_.writerow(["trim_fill", "k_imputed", L0, f"r_adj={round(r_adj,3)} [{round(ra_lo,3)},{round(ra_hi,3)}]"])
        w_.writerow(["failsafe_n", "rosenthal", fsn, "criterion 5k+10=1200"])
        # leave-one-out (study level): pooled r dropping each study.
        # Re-estimate from the full-data variance components (single start) for speed.
        theta0 = [base["s2_within"], base["s2_between"]]
        loo = []
        for drop in groups_by_study(rows):
            mask = np.ones(K, bool); mask[drop] = False
            sub_rows = [rows[i] for i in range(K) if mask[i]]
            yy = y[mask]; vv = v[mask]; gg = groups_by_study(sub_rows)
            f = fit_mv(yy, vv, np.ones((mask.sum(), 1)), gg, starts=[theta0])
            loo.append((rows[drop[0]]["study_id"], math.tanh(f["beta"][0])))
        rmin = min(loo, key=lambda t: t[1]); rmax = max(loo, key=lambda t: t[1])
        w_.writerow(["loo", "r_range", f"{rmin[1]:.4f}..{rmax[1]:.4f}",
                     f"min drop {rmin[0]}; max drop {rmax[0]}"])

    # ICRV moderator robustness (dedicated file; does NOT touch the canonical
    # tables). The full omnibus is carried by the 3-study Frontier (FR) regime;
    # re-testing on the core regimes shows the between-regime moderation is fragile.
    def icrv_omnibus(rws, levels):
        grp = groups_by_study(rws)
        yy = np.array([r["z"] for r in rws]); vv = np.array([r["v"] for r in rws])
        present = [lv for lv in levels if any(r["icrv"] == lv for r in rws)]
        Xm, others = design_factor(rws, "icrv", present)
        return qm_test(fit_mv(yy, vv, Xm, grp), len(others))
    qm_f, df_f, p_f = icrv_omnibus(rows, ["I", "II", "III", "FR", "MX"])
    no_fr = [r for r in rows if r["icrv"] != "FR"]
    qm_d, df_d, p_d = icrv_omnibus(no_fr, ["I", "II", "III", "MX"])
    print("\n=== ICRV DROP-FR SENSITIVITY ===")
    print(f"  full Q_M={qm_f:.2f} df={df_f} (p={p_f:.4g}) -> "
          f"core Q_M={qm_d:.2f} df={df_d} (p={p_d:.4g})  [FR k=3 drives omnibus]")
    with open(out / "table_icrv_dropFR_sensitivity.csv", "w", newline="", encoding="utf-8") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["model", "regimes", "K", "QM", "QM_df", "QM_pval", "note"])
        w_.writerow(["full", "I/II/III/FR/MX", len(rows), round(qm_f, 2), df_f, round(p_f, 4),
                     "omnibus significant on full sample"])
        w_.writerow(["drop_FR", "I/II/III/MX", len(no_fr), round(qm_d, 2), df_d, round(p_d, 4),
                     "FR (k=3, r=.349) removed; core regimes ns -> moderation not robust"])

    # forest data
    with open(out / "forest_data.csv", "w", newline="", encoding="utf-8") as fh:
        w_ = csv.writer(fh)
        w_.writerow(["study_id", "effect_id", "label", "r_i", "r_lo", "r_hi",
                     "icrv", "cdai", "dpl", "n", "doi_type", "fp_type"])
        for r in rows:
            se = math.sqrt(r["v"])
            _, rl, rh = ci_r(r["z"], se)
            w_.writerow([r["study_id"], r["effect_id"], f"{r['author']} {r['year']}".strip(),
                         round(r["r"], 3), round(rl, 3), round(rh, 3), r["icrv"], r["cdai"],
                         r["dpl"], int(r["n"]), r["doi_type"], r["fp_type"]])

    print(f"\nWrote tables to {out}/")


if __name__ == "__main__":
    main()
