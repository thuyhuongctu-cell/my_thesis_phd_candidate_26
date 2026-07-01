#!/usr/bin/env python3
"""Canonical descriptive re-lock — single source of truth for ALL descriptive
tables (thesis Table 4.1/4.2, CĐ1 Bảng 2.3.3.1-2.3.6).

Design goal: every descriptive number is reproducible from the committed raw
`.dta` using the SAME harmonisation as the P7 econometric pipeline, so the
descriptive frame and the regression frame are identical (50 economies with
committed raw data, incl. Japan, Timor-Leste and Azerbaijan; Timor-Leste is KEPT
in Group VI for the P7/descriptive frame — only the dedicated P8 SIDS study
excludes it via PACIFIC7. Azerbaijan (Group V) is covered across all four waves
2009/2013/2019/2024). This eliminates the multiple conflicting
"vintages" (SIDS counts of 1,781 / 1,916 / 2,038 / 2,295 / 2,809 across older
scripts) by deriving one coherent set.

Harmonisation (mirrors dist/osf/P7_capstone/code/p7_run_50econ.py):
  - file selection: standard cross-sections, year >= 2006, in ICRV frame,
    one cross-section per economy-year (dedup); icrv_map() KEEPS Timor in Grp VI.
  - LP    = ln(d2/l1), winsorised 1/99 WITHIN economy-year
  - dispersion = sd / P90/P10 / P75/P25 of LP demeaned WITHIN economy-year
    (Hsieh-Klenow), then aggregated across the group's firm-years
  - FSTS  = d3b + d3c (% of sales); exporter = FSTS > 0
  - fdi10 = b2b >= 10
  - rates (% Yes): product innov (h1), process innov (h5), R&D (h8),
    ISO cert (b8), website (c22b)

Out: data_wbes/analysis/descriptives_canonical_50econ.csv
Run: python3 scripts/relock_descriptives_canonical.py
"""
import glob
import sys
import warnings

import numpy as np
import pandas as pd

sys.path.insert(0, 'scripts')
warnings.filterwarnings('ignore')
from wbes_canon import parse                       # noqa: E402
from cd1_descriptives_pipeline import icrv_map      # noqa: E402

ORDER = ["Advanced_innovation", "Advanced_resource", "Upper_mid",
         "Lower_mid_transition", "Emerging", "SIDS_small"]
COLS = ['d2', 'l1', 'd3b', 'd3c', 'b2b', 'h1', 'h5', 'h8', 'b8', 'c22b']
MISSING = [-9, -8, -7, -6, -5, -4]


def read(path):
    try:
        import pyreadstat
        df, _ = pyreadstat.read_dta(path, usecols=COLS)
        return df.apply(pd.to_numeric, errors='coerce')
    except Exception:
        try:
            df = pd.read_stata(path, convert_categoricals=False)
            return df[[c for c in COLS if c in df.columns]].apply(pd.to_numeric, errors='coerce')
        except Exception:
            return None


def yes_rate(s):
    s = s.dropna()
    s = s[s.isin([1, 2])]
    return round(100 * (s == 1).mean(), 1) if len(s) else np.nan


def main():
    icrv = icrv_map()
    chosen = {}
    for f in sorted(glob.glob('data_wbes/raw_dta/*.dta')):
        m = parse(f)
        if m is None or not m['standard'] or m['panel'] or icrv.get(m['country']) is None:
            continue
        chosen.setdefault((m['country'], m['year']), f)

    rows = []
    for (c, y), f in sorted(chosen.items()):
        d = read(f)
        if d is None or 'd2' not in d or 'l1' not in d:
            continue
        d = d.where(~d.isin(MISSING))
        lp = np.log(d['d2'].where(d['d2'] > 0) / d['l1'].where(d['l1'] > 0))
        lo, hi = lp.quantile([0.01, 0.99])
        lp = lp.clip(lo, hi)
        b = d['d3b'].where(d['d3b'].between(0, 100)) if 'd3b' in d else pd.Series(index=d.index, dtype=float)
        cc = d['d3c'].where(d['d3c'].between(0, 100)) if 'd3c' in d else pd.Series(index=d.index, dtype=float)
        fsts = (b.fillna(0) + cc.fillna(0)).where(b.notna() | cc.notna()).clip(0, 100)
        fo = d['b2b'].where(d['b2b'].between(0, 100)) if 'b2b' in d else pd.Series(index=d.index, dtype=float)
        fdi10 = (fo >= 10).astype(float).where(fo.notna())
        rec = pd.DataFrame({'economy': c, 'year': y, 'group': icrv[c],
                            'lp': lp, 'fsts': fsts, 'fdi10': fdi10})
        for k in ('h1', 'h5', 'h8', 'b8', 'c22b'):
            rec[k] = d[k] if k in d else np.nan
        rows.append(rec)

    df = pd.concat(rows, ignore_index=True)
    # dispersion: demean LP within economy-year (currency-neutral, Hsieh-Klenow)
    df['lp_dm'] = df['lp'] - df.groupby(['economy', 'year'])['lp'].transform('mean')

    out = []
    for g in ORDER:
        s = df[df.group == g]
        dm = s['lp_dm'].dropna()
        out.append({
            'group': g,
            'n_econ': s.economy.nunique(),
            'n_waves': s.groupby(['economy', 'year']).ngroups,
            'n_lp_valid': int(s['lp'].notna().sum()),
            'sd_log_lp': round(dm.std(), 3),
            'p90_p10': round(np.exp(dm.quantile(.9) - dm.quantile(.1)), 1),
            'p75_p25': round(np.exp(dm.quantile(.75) - dm.quantile(.25)), 1),
            'fsts_mean': round(s['fsts'].mean(), 1),
            'exporter_pct': round(100 * (s['fsts'] > 0).mean(), 1),
            'fdi10_pct': round(100 * s['fdi10'].mean(), 1),
            'prod_innov_pct': yes_rate(s['h1']),
            'proc_innov_pct': yes_rate(s['h5']),
            'rd_pct': yes_rate(s['h8']),
            'iso_pct': yes_rate(s['b8']),
            'website_pct': yes_rate(s['c22b']),
        })
    res = pd.DataFrame(out)
    res.to_csv('data_wbes/analysis/descriptives_canonical_50econ.csv', index=False)
    tot_n = res['n_lp_valid'].sum()
    tot_e = res['n_econ'].sum()
    tot_w = res['n_waves'].sum()
    print(f"Frame: {tot_e} economies, {tot_w} economy-year cells, "
          f"{tot_n:,} LP-valid firms (per icrv_map; P7 frame keeps Timor in Group VI, "
          f"P8 SIDS study restricts to the 7 Pacific via PACIFIC7)\n")
    pd.set_option('display.width', 200, 'display.max_columns', 30)
    print(res.to_string(index=False))
    print('\nsaved -> data_wbes/analysis/descriptives_canonical_50econ.csv')


if __name__ == '__main__':
    main()
