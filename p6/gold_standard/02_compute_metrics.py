#!/usr/bin/env python3
"""
02_compute_metrics.py — Compute gold-standard validation metrics for the
                       LLM-assisted extraction workflow.

Compares manual extraction (gold_standard_manual_filled.csv) against the
locked database (gold_standard_sample.csv, which represents the
LLM-draft + human-review output already in p6_study_database.csv).

Computed metrics:
  Continuous quantities (r, N, year):
    - % exact agreement
    - % agreement within tolerance (r: |Δ| ≤ 0.005; N: exact; year: exact)
    - Mean absolute deviation
  Categorical quantities (icrv, dpl, doi_type, fp_type, country):
    - Cohen's kappa (with linear weights for ordinal where applicable)
    - % agreement
    - Confusion matrix top mismatches

Outputs:
  p6/gold_standard/validation_report.json   (machine-readable)
  p6/gold_standard/validation_report.md     (human-readable, for S-MAIDA.4)

Usage:
  cd /path/to/MY_THESIS_PHD_CANDIDATE_26
  # 1. Fill p6/gold_standard/gold_standard_manual_filled.csv from PDFs
  # 2. python3 p6/gold_standard/02_compute_metrics.py
"""
import csv, json, sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT     = Path(__file__).resolve().parents[2]
SAMPLE   = ROOT / 'p6' / 'gold_standard' / 'gold_standard_sample.csv'
MANUAL   = ROOT / 'p6' / 'gold_standard' / 'gold_standard_manual_filled.csv'
JSON_OUT = ROOT / 'p6' / 'gold_standard' / 'validation_report.json'
MD_OUT   = ROOT / 'p6' / 'gold_standard' / 'validation_report.md'

R_TOLERANCE = 0.005     # |Δr| ≤ 0.005 counts as agreement
KAPPA_THRESHOLD = 0.70  # pre-registered ceiling for categorical agreement
NUM_THRESHOLD   = 0.90  # pre-registered ceiling for % agreement within tolerance


def cohens_kappa(rater1, rater2):
    """Plain Cohen's kappa on aligned categorical lists. Returns (kappa, n_observed)."""
    pairs = [(a, b) for a, b in zip(rater1, rater2) if a not in ('', None) and b not in ('', None)]
    if not pairs:
        return None, 0
    n = len(pairs)
    categories = sorted(set([a for a, _ in pairs] + [b for _, b in pairs]))
    # Observed agreement
    po = sum(1 for a, b in pairs if a == b) / n
    # Expected agreement (marginal probabilities)
    m1 = Counter(a for a, _ in pairs)
    m2 = Counter(b for _, b in pairs)
    pe = sum((m1[c] / n) * (m2[c] / n) for c in categories)
    if pe >= 1.0:
        return 1.0 if po >= 1.0 else float('nan'), n
    return (po - pe) / (1.0 - pe), n


def load_aligned():
    if not MANUAL.exists():
        print(f"ERROR: {MANUAL} not found.", file=sys.stderr)
        print(f"       Fill gold_standard_manual_template.csv and save as gold_standard_manual_filled.csv first.", file=sys.stderr)
        sys.exit(1)

    sample = {(r['study_id'], r['effect_id']): r for r in csv.DictReader(open(SAMPLE,  encoding='utf-8'))}
    manual = {(r['study_id'], r['effect_id']): r for r in csv.DictReader(open(MANUAL, encoding='utf-8'))}

    common = sorted(set(sample) & set(manual))
    missing_in_manual = set(sample) - set(manual)
    if missing_in_manual:
        print(f"WARNING: {len(missing_in_manual)} sample rows missing in manual file:", file=sys.stderr)
        for k in sorted(missing_in_manual)[:5]:
            print(f"  {k}", file=sys.stderr)
    print(f"Aligned rows: {len(common)} / {len(sample)} sample rows")
    return [(k, sample[k], manual[k]) for k in common]


def main():
    data = load_aligned()

    # Continuous: r
    r_diffs = []
    r_exact = 0
    r_within_tol = 0
    n_r = 0
    for _, s, m in data:
        try:
            sr = float(s['r']); mr = float(m['manual_r'])
        except (ValueError, KeyError):
            continue
        n_r += 1
        d = mr - sr
        r_diffs.append(d)
        if d == 0: r_exact += 1
        if abs(d) <= R_TOLERANCE: r_within_tol += 1

    # Continuous: N
    n_exact = 0; n_count = 0
    for _, s, m in data:
        try:
            if int(float(s['n'])) == int(float(m['manual_n'])):
                n_exact += 1
            n_count += 1
        except (ValueError, KeyError):
            continue

    # Continuous: year
    y_exact = 0; y_count = 0
    for _, s, m in data:
        try:
            if int(s['year']) == int(m['year']):
                y_exact += 1
            y_count += 1
        except (ValueError, KeyError):
            continue

    # Categorical: icrv, dpl, doi_type, fp_type, country
    cats = {
        'icrv':     ('icrv',         'manual_icrv'),
        'dpl':      ('dpl',          'manual_dpl'),
        'doi_type': ('doi_type',     'manual_doi_type'),
        'fp_type':  ('fp_type',      'manual_fp_type'),
        'country':  ('country',      'manual_country'),
    }
    cat_results = {}
    for name, (s_col, m_col) in cats.items():
        v1 = [s.get(s_col, '').strip() for _, s, m in data]
        v2 = [m.get(m_col, '').strip() for _, s, m in data]
        kappa, n = cohens_kappa(v1, v2)
        if n == 0:
            cat_results[name] = {'kappa': None, 'n': 0, 'pct_agreement': None, 'top_mismatches': []}
            continue
        agree = sum(1 for a, b in zip(v1, v2) if a == b and a != '')
        mismatches = Counter((a, b) for a, b in zip(v1, v2) if a != b and a != '' and b != '')
        cat_results[name] = {
            'kappa': round(kappa, 3) if kappa is not None else None,
            'n': n,
            'pct_agreement': round(agree / n * 100, 1),
            'meets_threshold': (kappa is not None and kappa >= KAPPA_THRESHOLD),
            'top_mismatches': [{'system': a, 'manual': b, 'count': c}
                                for (a, b), c in mismatches.most_common(5)],
        }

    cont_results = {
        'r': {
            'n': n_r,
            'pct_exact':       round(r_exact / n_r * 100, 1)        if n_r else None,
            'pct_within_tol':  round(r_within_tol / n_r * 100, 1)   if n_r else None,
            'mean_abs_dev':    round(sum(abs(d) for d in r_diffs) / n_r, 4) if n_r else None,
            'max_abs_dev':     round(max(abs(d) for d in r_diffs), 4)        if n_r else None,
            'tolerance':       R_TOLERANCE,
            'meets_threshold': (n_r > 0 and r_within_tol / n_r >= NUM_THRESHOLD),
        },
        'n': {
            'count': n_count,
            'pct_exact': round(n_exact / n_count * 100, 1) if n_count else None,
            'meets_threshold': (n_count > 0 and n_exact / n_count >= NUM_THRESHOLD),
        },
        'year': {
            'count': y_count,
            'pct_exact': round(y_exact / y_count * 100, 1) if y_count else None,
            'meets_threshold': (y_count > 0 and y_exact / y_count >= NUM_THRESHOLD),
        },
    }

    report = {
        'gold_standard_n_rows': len(data),
        'gold_standard_n_studies': len(set(s['study_id'] for _, s, _ in data)),
        'thresholds': {
            'kappa_min': KAPPA_THRESHOLD,
            'numeric_pct_min': NUM_THRESHOLD * 100,
            'r_tolerance': R_TOLERANCE,
        },
        'continuous': cont_results,
        'categorical': cat_results,
    }

    JSON_OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')

    # Markdown report
    lines = [
        '# Gold-Standard Validation Report',
        '',
        f'**Sample size:** {len(data)} effect-rows ({report["gold_standard_n_studies"]} unique studies)',
        f'**Pre-registered thresholds:** Cohen kappa >= {KAPPA_THRESHOLD}; numeric % agreement >= {int(NUM_THRESHOLD*100)}%; r tolerance |delta| <= {R_TOLERANCE}',
        '',
        '## Continuous quantities',
        '',
        '| Quantity | n | % exact | % within tolerance | Mean |delta| | Max |delta| | Meets threshold |',
        '|---|---|---|---|---|---|---|',
        f'| r        | {cont_results["r"]["n"]}    | {cont_results["r"]["pct_exact"]}% | {cont_results["r"]["pct_within_tol"]}% | {cont_results["r"]["mean_abs_dev"]} | {cont_results["r"]["max_abs_dev"]} | {"YES" if cont_results["r"]["meets_threshold"] else "NO"} |',
        f'| N        | {cont_results["n"]["count"]} | {cont_results["n"]["pct_exact"]}% | (exact only) | -- | -- | {"YES" if cont_results["n"]["meets_threshold"] else "NO"} |',
        f'| year     | {cont_results["year"]["count"]} | {cont_results["year"]["pct_exact"]}% | (exact only) | -- | -- | {"YES" if cont_results["year"]["meets_threshold"] else "NO"} |',
        '',
        '## Categorical quantities',
        '',
        '| Quantity | n | Cohen kappa | % agreement | Meets threshold |',
        '|---|---|---|---|---|',
    ]
    for name in ['icrv', 'dpl', 'doi_type', 'fp_type', 'country']:
        r = cat_results[name]
        meets = "YES" if r.get('meets_threshold') else "NO"
        kappa = f'{r["kappa"]:.3f}' if r["kappa"] is not None else 'N/A'
        pct = f'{r["pct_agreement"]}%' if r["pct_agreement"] is not None else 'N/A'
        lines.append(f'| {name:8s} | {r["n"]} | {kappa} | {pct} | {meets} |')

    lines += ['', '## Top categorical mismatches']
    for name, r in cat_results.items():
        if not r.get('top_mismatches'):
            continue
        lines.append(f'\n### {name}')
        lines.append('| System (LLM-draft + reviewed) | Manual (gold) | Count |')
        lines.append('|---|---|---|')
        for m in r['top_mismatches']:
            lines.append(f'| {m["system"]} | {m["manual"]} | {m["count"]} |')

    overall_pass = (cont_results['r']['meets_threshold'] and
                    cont_results['n']['meets_threshold'] and
                    all(r.get('meets_threshold') for r in cat_results.values() if r['n']))
    lines += ['', '## Overall verdict',
              f'**{"PASS — workflow validated, use for primary analysis" if overall_pass else "FAIL — at least one quantity below threshold; manual re-extraction required for that quantity"}**',
              '',
              'Threshold rule: any quantity below threshold triggers full manual re-extraction for that quantity across the entire corpus (pre-registered).']
    MD_OUT.write_text('\n'.join(lines), encoding='utf-8')

    print(f"Wrote: {JSON_OUT.relative_to(ROOT)}")
    print(f"Wrote: {MD_OUT.relative_to(ROOT)}")
    print()
    if overall_pass:
        print("OVERALL: PASS — workflow validated.")
    else:
        print("OVERALL: FAIL — see report for which quantities require manual re-extraction.")


if __name__ == '__main__':
    main()
