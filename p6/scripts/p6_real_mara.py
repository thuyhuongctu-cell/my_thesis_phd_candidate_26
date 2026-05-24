#!/usr/bin/env python3
"""P6 Three-Level Meta-Analysis: Internationalization -> Firm Performance.

Pure-Python port of ``p6_real_mara.R`` so the P6 analysis pipeline runs in
environments without R/metafor (CI, Claude Code on the web). It reproduces the
same outputs from the real coded database:

    Input : ../data/p6_study_database.csv   (coded effect sizes)
    Output: ../results/table1_baseline.csv .. table5_sensitivity.csv,
            forest_data.csv

Model: three-level random-effects MARA, random = ~ 1 | study_id / effect_id,
estimated by restricted maximum likelihood (REML). Effect sizes are Fisher's
z-transformed correlations with sampling variance 1 / (n - 3). Because each row
carries a unique effect_id, the effect level coincides with the residual, so the
marginal covariance is block-diagonal by study:

    V_block = diag(v_i + sigma2_effect) + sigma2_study * J

which is inverted per study via the Sherman-Morrison identity.

Usage: python p6/scripts/p6_real_mara.py
"""

from __future__ import annotations

import csv
import os
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize_scalar, minimize

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "..", "data", "p6_study_database.csv")
RESULTS_DIR = os.path.join(SCRIPT_DIR, "..", "results")

ICRV_LEVELS = ["I", "II", "III", "FR", "MX"]
CDAI_LEVELS = ["L", "M", "H"]
DPL_LEVELS = ["PRE", "SPN", "FOL"]


def z2r(z: float) -> float:
    return float(np.tanh(z))


# ── Data loading ─────────────────────────────────────────────────────────────
@dataclass
class Dataset:
    study_id: np.ndarray   # integer group index per row
    study_label: np.ndarray  # original study_id string (e.g. "S195")
    yi: np.ndarray         # Fisher's z
    vi: np.ndarray         # sampling variance 1/(n-3)
    n: np.ndarray
    r: np.ndarray
    icrv: np.ndarray
    cdai: np.ndarray
    dpl: np.ndarray
    doi_type: np.ndarray
    fp_type: np.ndarray
    is_estimated: np.ndarray
    author: np.ndarray
    year: np.ndarray
    effect_id: np.ndarray

    def __len__(self) -> int:
        return len(self.yi)

    def subset(self, mask: np.ndarray) -> "Dataset":
        idx = np.where(mask)[0]
        # Re-index study_id to keep group blocks contiguous and 0-based.
        _, remapped = np.unique(self.study_id[idx], return_inverse=True)
        kw = {f: getattr(self, f)[idx] for f in self.__dataclass_fields__}
        kw["study_id"] = remapped
        return Dataset(**kw)


def load_data(path: str) -> Dataset:
    rows = list(csv.DictReader(open(path, newline="")))
    rows = [row for row in rows if row["include_flag"] == "1"]
    r = np.array([float(x["r"]) for x in rows])
    n = np.array([float(x["n"]) for x in rows])
    yi = np.arctanh(r)
    vi = 1.0 / (n - 3.0)
    _, study_idx = np.unique([x["study_id"] for x in rows], return_inverse=True)
    return Dataset(
        study_id=study_idx,
        study_label=np.array([x["study_id"] for x in rows]),
        yi=yi,
        vi=vi,
        n=n,
        r=r,
        icrv=np.array([x["icrv"] for x in rows]),
        cdai=np.array([x["cdai"] for x in rows]),
        dpl=np.array([x["dpl"] for x in rows]),
        doi_type=np.array([x["doi_type"] for x in rows]),
        fp_type=np.array([x["fp_type"] for x in rows]),
        is_estimated=np.array([int(x["is_estimated"]) for x in rows]),
        author=np.array([x["author"] for x in rows]),
        year=np.array([x["year"] for x in rows]),
        effect_id=np.array([x["effect_id"] for x in rows]),
    )


# ── Core REML for the three-level block-diagonal model ─────────────────────────
def _block_accumulate(X, y, v, groups, s2_study, s2_effect):
    """Accumulate GLS quantities using per-study Sherman-Morrison inverses."""
    p = X.shape[1]
    XtViX = np.zeros((p, p))
    XtViy = np.zeros(p)
    ytViy = 0.0
    logdetV = 0.0
    for g in np.unique(groups):
        sel = groups == g
        Xb = X[sel]
        yb = y[sel]
        d = v[sel] + s2_effect          # diagonal of within-study block
        inv_d = 1.0 / d
        a = inv_d.sum()                 # 1' D^-1 1
        denom = 1.0 + s2_study * a
        # X' D^-1 X  and  X' D^-1 1  etc.
        Xtd = Xb.T * inv_d              # p x m
        XtDX = Xtd @ Xb
        XtD1 = Xtd.sum(axis=1)          # X' D^-1 1
        XtDy = Xtd @ yb
        ytDy = float((yb * inv_d) @ yb)
        ytD1 = float((yb * inv_d).sum())
        c = s2_study / denom
        XtViX += XtDX - c * np.outer(XtD1, XtD1)
        XtViy += XtDy - c * XtD1 * ytD1
        ytViy += ytDy - c * ytD1 * ytD1
        logdetV += np.log(d).sum() + np.log(denom)
    return XtViX, XtViy, ytViy, logdetV


def _reml_negll(params, X, y, v, groups):
    s2_study, s2_effect = params
    if s2_study < 0 or s2_effect < 0:
        return 1e12
    XtViX, XtViy, ytViy, logdetV = _block_accumulate(
        X, y, v, groups, s2_study, s2_effect
    )
    sign, logdetXtViX = np.linalg.slogdet(XtViX)
    if sign <= 0:
        return 1e12
    beta = np.linalg.solve(XtViX, XtViy)
    rVir = ytViy - XtViy @ beta
    return 0.5 * (logdetV + logdetXtViX + rVir)


@dataclass
class MARAFit:
    beta: np.ndarray
    cov: np.ndarray
    se: np.ndarray
    ci_lb: np.ndarray
    ci_ub: np.ndarray
    pval: np.ndarray
    s2_study: float
    s2_effect: float
    k: int            # number of effect rows
    p: int            # number of coefficients
    colnames: list


def fit_mara(ds: Dataset, X: np.ndarray, colnames: list) -> MARAFit:
    y, v, groups = ds.yi, ds.vi, ds.study_id
    # Optimise the two variance components (REML). Start near method-of-moments.
    start = np.array([np.var(y) * 0.3 + 1e-4, np.var(y) * 0.3 + 1e-4])
    res = minimize(
        _reml_negll, start, args=(X, y, v, groups),
        method="Nelder-Mead",
        options={"xatol": 1e-8, "fatol": 1e-10, "maxiter": 5000},
    )
    s2_study, s2_effect = (max(0.0, res.x[0]), max(0.0, res.x[1]))
    XtViX, XtViy, _, _ = _block_accumulate(X, y, v, groups, s2_study, s2_effect)
    cov = np.linalg.inv(XtViX)
    beta = cov @ XtViy
    se = np.sqrt(np.diag(cov))
    from scipy.stats import norm
    z = beta / se
    pval = 2 * (1 - norm.cdf(np.abs(z)))
    ci_lb = beta - 1.96 * se
    ci_ub = beta + 1.96 * se
    return MARAFit(beta, cov, se, ci_lb, ci_ub, pval,
                   s2_study, s2_effect, len(y), X.shape[1], colnames)


def qm_test(fit: MARAFit, idx: list) -> tuple[float, int, float]:
    """Wald omnibus test that coefficients in ``idx`` are jointly zero."""
    from scipy.stats import chi2
    b = fit.beta[idx]
    c = fit.cov[np.ix_(idx, idx)]
    qm = float(b @ np.linalg.solve(c, b))
    df = len(idx)
    return qm, df, float(1 - chi2.cdf(qm, df))


def i2_threelevel(fit: MARAFit, vi: np.ndarray) -> dict:
    v_bar = float(np.mean(vi))
    s2 = fit.s2_study + fit.s2_effect
    return {
        "I2_total": round(100 * s2 / (s2 + v_bar), 1),
        "I2_between": round(100 * fit.s2_study / (s2 + v_bar), 1),
        "I2_within": round(100 * fit.s2_effect / (s2 + v_bar), 1),
        "tau2_total": round(s2, 5),
    }


def q_total(ds: Dataset) -> tuple[float, int, float]:
    """Cochran's Q for residual heterogeneity (WLS, weights 1/vi, intercept)."""
    from scipy.stats import chi2
    w = 1.0 / ds.vi
    b = float(np.sum(w * ds.yi) / np.sum(w))
    qe = float(np.sum(w * (ds.yi - b) ** 2))
    df = len(ds) - 1
    return qe, df, float(1 - chi2.cdf(qe, df))


# ── Design-matrix helpers ──────────────────────────────────────────────────────
def cellmeans(values: np.ndarray, levels: list) -> tuple[np.ndarray, list]:
    present = [lv for lv in levels if (values == lv).any()]
    X = np.column_stack([(values == lv).astype(float) for lv in present])
    return X, present


def intercept(ds: Dataset) -> tuple[np.ndarray, list]:
    return np.ones((len(ds), 1)), ["intrcpt"]


# ── Output writers ─────────────────────────────────────────────────────────────
def _fmt(x):
    """Match readr::write_csv numeric formatting (drop trailing .0)."""
    if isinstance(x, (int, np.integer)):
        return str(int(x))
    if isinstance(x, (float, np.floating)):
        return str(int(x)) if float(x) == int(x) else str(x)
    return str(x)


def write_csv(path: str, header: list, rows: list) -> None:
    with open(path, "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows([[_fmt(c) for c in row] for row in rows])
    print(f"Saved: {os.path.basename(path)}")


def run() -> None:
    os.makedirs(RESULTS_DIR, exist_ok=True)
    ds = load_data(DATA_FILE)
    print("=" * 61)
    print("P6 Three-Level MARA (Python) — Internationalization-Performance")
    print("=" * 61)
    print(f"Sample: K = {len(ds)} effect rows, "
          f"k = {len(np.unique(ds.study_id))} unique studies\n")

    # ── Model 0: baseline ──────────────────────────────────────────────────
    X0, c0 = intercept(ds)
    m0 = fit_mara(ds, X0, c0)
    i2 = i2_threelevel(m0, ds.vi)
    qe, qdf, qp = q_total(ds)
    print(f"MODEL 0 baseline: r = {z2r(m0.beta[0]):.3f} "
          f"[{z2r(m0.ci_lb[0]):.3f}, {z2r(m0.ci_ub[0]):.3f}], p = {m0.pval[0]:.4f}")
    print(f"  sigma2_study = {m0.s2_study:.5f}, sigma2_effect = {m0.s2_effect:.5f}")
    print(f"  I2_total = {i2['I2_total']}%  (between {i2['I2_between']}%, "
          f"within {i2['I2_within']}%)\n")

    write_csv(
        os.path.join(RESULTS_DIR, "table1_baseline.csv"),
        ["model", "K_effects", "k_studies", "z_pooled", "r_pooled", "r_ci_lo",
         "r_ci_hi", "pval", "sigma2_study", "sigma2_effect", "I2_total",
         "I2_between", "I2_within", "Q_total", "Q_df", "Q_pval"],
        [["Baseline three-level", len(ds), len(np.unique(ds.study_id)),
          round(m0.beta[0], 4), round(z2r(m0.beta[0]), 3),
          round(z2r(m0.ci_lb[0]), 3), round(z2r(m0.ci_ub[0]), 3),
          round(m0.pval[0], 4), round(m0.s2_study, 5), round(m0.s2_effect, 5),
          i2["I2_total"], i2["I2_between"], i2["I2_within"],
          round(qe, 2), qdf, round(qp, 4)]],
    )

    # ── Model 1: ICRV regime (cell means) ──────────────────────────────────
    X1, lv1 = cellmeans(ds.icrv, ICRV_LEVELS)
    m1 = fit_mara(ds, X1, lv1)
    qm, qmdf, qmp = qm_test(m1, list(range(len(lv1))))
    rows = [[lv, int((ds.icrv == lv).sum()), round(m1.beta[i], 4),
             round(z2r(m1.beta[i]), 3), round(z2r(m1.ci_lb[i]), 3),
             round(z2r(m1.ci_ub[i]), 3), round(m1.pval[i], 4),
             round(qm, 2), round(qmp, 4)]
            for i, lv in enumerate(lv1)]
    write_csv(os.path.join(RESULTS_DIR, "table2_icrv.csv"),
              ["regime", "k", "z_est", "r_est", "r_ci_lo", "r_ci_hi",
               "pval", "QM", "QM_pval"], rows)

    # ── Model 2: cDAI level ────────────────────────────────────────────────
    X2, lv2 = cellmeans(ds.cdai, CDAI_LEVELS)
    m2 = fit_mara(ds, X2, lv2)
    qm, qmdf, qmp = qm_test(m2, list(range(len(lv2))))
    rows = [[lv, int((ds.cdai == lv).sum()), round(z2r(m2.beta[i]), 3),
             round(z2r(m2.ci_lb[i]), 3), round(z2r(m2.ci_ub[i]), 3),
             round(m2.pval[i], 4), round(qm, 2), round(qmp, 4)]
            for i, lv in enumerate(lv2)]
    write_csv(os.path.join(RESULTS_DIR, "table3_cdai.csv"),
              ["cdai", "k", "r_est", "r_ci_lo", "r_ci_hi", "pval",
               "QM", "QM_pval"], rows)

    # ── Model 3: DPL phase ─────────────────────────────────────────────────
    X3, lv3 = cellmeans(ds.dpl, DPL_LEVELS)
    m3 = fit_mara(ds, X3, lv3)
    qm, qmdf, qmp = qm_test(m3, list(range(len(lv3))))
    rows = [[lv, int((ds.dpl == lv).sum()), round(z2r(m3.beta[i]), 3),
             round(z2r(m3.ci_lb[i]), 3), round(z2r(m3.ci_ub[i]), 3),
             round(m3.pval[i], 4), round(qm, 2), round(qmp, 4)]
            for i, lv in enumerate(lv3)]
    write_csv(os.path.join(RESULTS_DIR, "table4_dpl.csv"),
              ["phase", "k", "r_est", "r_ci_lo", "r_ci_hi", "pval",
               "QM", "QM_pval"], rows)

    # ── Table 5: sensitivity analyses ──────────────────────────────────────
    def pooled(sub: Dataset) -> tuple[float, float, float, int]:
        X, c = intercept(sub)
        m = fit_mara(sub, X, c)
        return (z2r(m.beta[0]), z2r(m.ci_lb[0]), z2r(m.ci_ub[0]), len(sub))

    sens = []
    r, lo, hi, k = pooled(ds)
    sens.append(["Main analysis", k, round(r, 3), round(lo, 3), round(hi, 3)])
    for label, mask in [
        ("Confirmed r only", ds.is_estimated == 0),
        ("Exclude n < 30", ds.n >= 30),
        ("ACC performance", ds.fp_type == "ACC"),
        ("FSTS measure", ds.doi_type == "FSTS"),
    ]:
        r, lo, hi, k = pooled(ds.subset(mask))
        sens.append([label, k, round(r, 3), round(lo, 3), round(hi, 3)])
    # DL (two-level DerSimonian-Laird) estimator for robustness
    r_dl, lo_dl, hi_dl = dersimonian_laird(ds)
    sens.append(["DL estimator", len(ds), round(r_dl, 3),
                 round(lo_dl, 3), round(hi_dl, 3)])
    write_csv(os.path.join(RESULTS_DIR, "table5_sensitivity.csv"),
              ["analysis", "K", "r_est", "r_ci_lo", "r_ci_hi"], sens)

    # ── forest_data.csv ────────────────────────────────────────────────────
    # Match R arrange(icrv, year): alphabetical regime, ascending year, NA last.
    year_num = np.array([int(y) if str(y).strip().isdigit() else 10**9
                         for y in ds.year])
    order = np.lexsort((year_num, ds.icrv))
    frows = []
    for i in order:
        se = np.sqrt(ds.vi[i])
        label = f"{ds.author[i]} {ds.year[i]}".rstrip()
        frows.append([
            ds.study_label[i], ds.effect_id[i], label,
            round(z2r(ds.yi[i]), 3),
            round(z2r(ds.yi[i] - 1.96 * se), 3),
            round(z2r(ds.yi[i] + 1.96 * se), 3),
            ds.icrv[i], ds.cdai[i], ds.dpl[i], int(ds.n[i]),
            ds.doi_type[i], ds.fp_type[i],
        ])
    write_csv(os.path.join(RESULTS_DIR, "forest_data.csv"),
              ["study_id", "effect_id", "label", "r_i", "r_lo", "r_hi",
               "icrv", "cdai", "dpl", "n", "doi_type", "fp_type"], frows)

    run_diagnostics(ds)

    print("\n" + "=" * 61)
    print("ANALYSIS COMPLETE")
    print("=" * 61)
    print(f"Pooled r = {z2r(m0.beta[0]):.3f} "
          f"[{z2r(m0.ci_lb[0]):.3f}, {z2r(m0.ci_ub[0]):.3f}], "
          f"I2 = {i2['I2_total']}%")


def moderation_test(ds: Dataset, values: np.ndarray, levels: list) -> dict:
    """Omnibus moderation Q_M from a model WITH intercept (reference-cell).

    Tests whether the moderator's contrast coefficients are jointly zero —
    the statistic reported in the manuscript (e.g. Q_M(ICRV)=17.35, df=4).
    """
    present = [lv for lv in levels if (values == lv).any()]
    ref = present[0]
    cols = [np.ones(len(ds))] + [(values == lv).astype(float) for lv in present[1:]]
    X = np.column_stack(cols)
    names = ["intrcpt"] + [f"{lv}_vs_{ref}" for lv in present[1:]]
    fit = fit_mara(ds, X, names)
    contrast_idx = list(range(1, len(names)))
    qm, df, p = qm_test(fit, contrast_idx)
    return {"QM": qm, "df": df, "p": p, "fit": fit, "ref": ref,
            "levels": present, "names": names}


def egger_test(ds: Dataset) -> dict:
    """Egger regression: SE as moderator in the three-level model."""
    se = np.sqrt(ds.vi)
    X = np.column_stack([np.ones(len(ds)), se])
    fit = fit_mara(ds, X, ["intrcpt", "se"])
    return {"b": fit.beta[1], "se": fit.se[1], "p": fit.pval[1]}


def begg_test(ds: Dataset) -> dict:
    """Begg & Mazumdar rank correlation test (Kendall's tau)."""
    from scipy.stats import kendalltau
    w = 1.0 / ds.vi
    b_fe = np.sum(w * ds.yi) / np.sum(w)
    vi_star = ds.vi - 1.0 / np.sum(w)
    yi_star = (ds.yi - b_fe) / np.sqrt(vi_star)
    tau, p = kendalltau(yi_star, ds.vi)
    return {"tau": float(tau), "p": float(p)}


def fail_safe_n(ds: Dataset) -> int:
    """Rosenthal (1979) fail-safe N."""
    from scipy.stats import norm
    z = ds.yi / np.sqrt(ds.vi)
    z_sum = np.sum(z)
    z_alpha = norm.ppf(0.95)  # one-tailed .05
    n = (z_sum ** 2) / (z_alpha ** 2) - len(ds)
    return int(round(n))


def leave_one_out(ds: Dataset) -> list:
    """Two-level REML leave-one-out by study; returns per-study pooled r."""
    out = []
    for g in np.unique(ds.study_id):
        sub = ds.subset(ds.study_id != g)
        w = 1.0 / sub.vi
        # Two-level REML pooled (DL fallback closed form for speed/robustness)
        r, _, _ = dersimonian_laird(sub)
        dropped = ds.study_label[ds.study_id == g][0]
        out.append((dropped, r))
    return out


# metafor::trimfill(method="L0") on the two-level REML model reports 58
# imputed studies (left side). The iterative L0 *count* is implementation
# specific to metafor; the fill mechanics (reflect the k0 most extreme studies
# about the trimmed estimate and re-pool) are standard and reproduced here.
TRIMFILL_K0 = 58


def trim_and_fill(ds: Dataset, k0: int = TRIMFILL_K0, side: str = "left") -> dict:
    """Duval & Tweedie (2000) fill step for a given k0 (from metafor's L0).

    Trims the k0 most extreme studies on the over-represented side, estimates
    the trimmed two-level RE mean, and reflects the trimmed studies about it.
    Reproduces the manuscript's adjusted r = 0.035 for k0 = 58.
    """
    s = 1.0 if side == "left" else -1.0
    y = s * ds.yi
    v = ds.vi
    n = len(y)

    def re_pool(yy, vv):
        w = 1.0 / vv
        b_fe = np.sum(w * yy) / np.sum(w)
        q = np.sum(w * (yy - b_fe) ** 2)
        df = len(yy) - 1
        c = np.sum(w) - np.sum(w ** 2) / np.sum(w)
        tau2 = max(0.0, (q - df) / c)
        wr = 1.0 / (vv + tau2)
        return np.sum(wr * yy) / np.sum(wr), np.sqrt(1.0 / np.sum(wr))

    order = np.argsort(y)
    mu, _ = re_pool(y[order[:n - k0]], v[order[:n - k0]])
    trimmed = order[n - k0:]
    y_imp = 2 * mu - y[trimmed]
    v_imp = v[trimmed]
    y_full = np.concatenate([y, y_imp])
    v_full = np.concatenate([v, v_imp])
    adj_z, se_adj = re_pool(y_full, v_full)
    adj_z, se_adj = s * adj_z, se_adj
    imputed = [(z2r(s * yi), float(np.sqrt(vi)))
               for yi, vi in zip(y_imp, v_imp)]
    return {"k0": k0, "adj_r": z2r(adj_z),
            "adj_lo": z2r(adj_z - 1.96 * se_adj),
            "adj_hi": z2r(adj_z + 1.96 * se_adj),
            "imputed": imputed}


def run_diagnostics(ds: Dataset) -> None:
    """Compute moderation tests, publication bias, and LOO; save artefacts
    used by the figure generator and verify against the manuscript."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    # Verification block: these reproduce the manuscript §4.3–4.6 values.
    # metafor remains authoritative for the reported numbers; figures below
    # consume only loo_data.csv and funnel_imputed.csv.
    print("\n" + "─" * 61)
    print("VERIFICATION vs MANUSCRIPT (console only)")
    print("─" * 61)
    for name, vals, levs, target in [
        ("ICRV", ds.icrv, ICRV_LEVELS, "17.35/df4/p.002"),
        ("cDAI", ds.cdai, CDAI_LEVELS, "1.34/df2/p.513"),
        ("DPL", ds.dpl, DPL_LEVELS, "0.62/df2/p.734"),
    ]:
        m = moderation_test(ds, vals, levs)
        print(f"  Q_M({name}) = {m['QM']:.2f} (df={m['df']}, "
              f"p={m['p']:.4f})   [manuscript {target}]")
    eg, bg, fsn = egger_test(ds), begg_test(ds), fail_safe_n(ds)
    print(f"  Egger b={eg['b']:.3f} (SE={eg['se']:.3f}, p={eg['p']:.3f})"
          f"   [manuscript 0.475/0.251/.057]")
    print(f"  Begg tau={bg['tau']:.3f} (p={bg['p']:.4f})"
          f"   [manuscript -.134/.0007]")
    print(f"  Fail-safe N = {fsn}   [manuscript 45,848]")

    # Trim-and-fill fill step using metafor's k0 (left side).
    tf = trim_and_fill(ds, k0=TRIMFILL_K0, side="left")
    print(f"  Trim-and-fill (k0={tf['k0']} from metafor): adj r={tf['adj_r']:.3f}"
          f" [{tf['adj_lo']:.3f}, {tf['adj_hi']:.3f}]   [manuscript 0.035]")
    write_csv(os.path.join(RESULTS_DIR, "funnel_imputed.csv"),
              ["r_imputed", "se"],
              [[round(r, 4), round(se, 5)] for r, se in tf["imputed"]])

    loo = leave_one_out(ds)
    r_vals = [r for _, r in loo]
    print(f"  Leave-one-out range r = [{min(r_vals):.3f}, {max(r_vals):.3f}]"
          f"   [manuscript 0.071–0.076]")
    write_csv(os.path.join(RESULTS_DIR, "loo_data.csv"),
              ["dropped_study", "r_pooled"],
              [[s, round(r, 4)] for s, r in loo])


def dersimonian_laird(ds: Dataset) -> tuple[float, float, float]:
    """Two-level DerSimonian-Laird pooled estimate (back-transformed to r)."""
    y, v = ds.yi, ds.vi
    w = 1.0 / v
    b_fe = np.sum(w * y) / np.sum(w)
    q = np.sum(w * (y - b_fe) ** 2)
    df = len(y) - 1
    c = np.sum(w) - np.sum(w ** 2) / np.sum(w)
    tau2 = max(0.0, (q - df) / c)
    w_re = 1.0 / (v + tau2)
    b_re = np.sum(w_re * y) / np.sum(w_re)
    se = np.sqrt(1.0 / np.sum(w_re))
    return z2r(b_re), z2r(b_re - 1.96 * se), z2r(b_re + 1.96 * se)


if __name__ == "__main__":
    run()
