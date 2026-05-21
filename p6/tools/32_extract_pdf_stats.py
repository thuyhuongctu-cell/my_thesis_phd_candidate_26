#!/usr/bin/env python3
"""
Extract candidate statistics from academic PDF for meta-analysis L2 coding.
Reduces manual extraction time by pre-filling candidate r values from β/t/F.

Usage:
  python3 32_extract_pdf_stats.py paper.pdf
  python3 32_extract_pdf_stats.py --batch p6/tools/pdfs/ --output results/batch_stats.csv

Requires: pip install pdfplumber pandas
"""
import pdfplumber, re, sys, json, math, argparse, csv
from pathlib import Path


def extract_stats_from_pdf(pdf_path: Path) -> dict:
    results = {
        'file': pdf_path.name,
        'sample_sizes': [],
        'correlations': [],
        'betas': [],
        'tstats': [],
        'fstats': [],
        'n_tables': 0,
        'modal_n': None,
        'candidate_r': []
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ''
            for page in pdf.pages:
                text = page.extract_text() or ''
                full_text += text + '\n'
                tables = page.extract_tables()
                results['n_tables'] += len(tables) if tables else 0
    except Exception as e:
        results['error'] = str(e)
        return results

    # Sample size patterns
    n_patterns = [
        r'[Nn]\s*=\s*(\d{2,6})',
        r'[Nn]\s*=\s*(\d{1,3}[,]\d{3})',
        r'observations[:\s=]+(\d{2,6})',
        r'sample.*?(\d{3,6})\s+firms',
        r'(\d{3,6})\s+observations',
    ]
    for pat in n_patterns:
        for m in re.findall(pat, full_text):
            n = int(str(m).replace(',', ''))
            if 30 <= n <= 500000:
                results['sample_sizes'].append(n)

    # Correlation r patterns
    for pat in [r'\br\s*=\s*(-?0?\.\d{2,4})', r'r\s*=\s*(-?\.\d{2,4})']:
        results['correlations'].extend(re.findall(pat, full_text))

    # Beta patterns
    for pat in [r'β\s*=\s*(-?0?\.\d{2,4})', r'[Bb]eta\s*=\s*(-?0?\.\d{2,4})']:
        results['betas'].extend(re.findall(pat, full_text))

    # t-statistic patterns
    for pat in [r'\bt\s*=\s*(-?\d{1,2}\.\d{1,3})', r't-stat[:\s]+(-?\d{1,2}\.\d{1,3})']:
        results['tstats'].extend(re.findall(pat, full_text))

    # F-statistic patterns
    for pat in [r'\bF\s*=\s*(\d{1,4}\.\d{1,3})', r'F-stat[:\s]+(\d{1,4}\.\d{1,3})']:
        results['fstats'].extend(re.findall(pat, full_text))

    # Modal N
    if results['sample_sizes']:
        from collections import Counter
        results['modal_n'] = Counter(results['sample_sizes']).most_common(1)[0][0]

    # Build candidate r list
    candidates = []

    for r_str in results['correlations'][:5]:
        try:
            r_val = float(r_str)
            if -1 < r_val < 1 and abs(r_val) > 0.01:
                candidates.append({'r': round(r_val, 4), 'source': 'direct_r', 'estimated': 0})
        except: pass

    for b_str in results['betas'][:8]:
        try:
            b_val = float(b_str)
            if -1 < b_val < 1 and abs(b_val) > 0.03:
                candidates.append({'r': round(b_val, 4), 'source': 'beta_approx', 'estimated': 1})
        except: pass

    if results['modal_n']:
        n = results['modal_n']
        for t_str in results['tstats'][:8]:
            try:
                t_val = float(t_str)
                df = max(n - 15, 10)
                r_val = t_val / math.sqrt(t_val**2 + df)
                if -1 < r_val < 1 and abs(r_val) > 0.02:
                    candidates.append({
                        'r': round(r_val, 4),
                        'source': f't_to_r(t={t_val:.2f},n={n})',
                        'estimated': 1
                    })
            except: pass

    # De-duplicate by rounding to 2 decimals
    seen = set()
    for c in candidates:
        key = round(c['r'], 2)
        if key not in seen:
            seen.add(key)
            results['candidate_r'].append(c)
        if len(results['candidate_r']) >= 5:
            break

    return results


def print_results(res: dict):
    print(f"\n{'='*60}")
    print(f"FILE: {res['file']}")
    print(f"{'='*60}")
    if 'error' in res:
        print(f"  ERROR: {res['error']} (likely scanned PDF — manual extraction needed)")
        return
    print(f"  Sample sizes found: {list(set(res['sample_sizes']))[:8]}")
    print(f"  Modal N:            {res['modal_n']}")
    print(f"  Tables detected:    {res['n_tables']}")
    print(f"  Direct r values:    {res['correlations'][:6]}")
    print(f"  Beta values:        {res['betas'][:6]}")
    print(f"  t-statistics:       {res['tstats'][:6]}")
    print(f"\n  CANDIDATE r VALUES (fill into tracker):")
    if not res['candidate_r']:
        print("  ⚠️  No candidates found — manual coding or scanned PDF")
    for c in res['candidate_r']:
        flag = '⭐' if c['estimated'] == 0 else '~'
        print(f"    {flag} r = {c['r']:+.4f}   source={c['source']}   is_estimated={c['estimated']}")


def batch_process(pdf_dir: Path, output_csv: Path):
    pdfs = list(pdf_dir.glob('*.pdf'))
    print(f"Processing {len(pdfs)} PDFs from {pdf_dir}...")

    rows = []
    for i, pdf in enumerate(pdfs, 1):
        print(f"  [{i}/{len(pdfs)}] {pdf.name}", end='', flush=True)
        res = extract_stats_from_pdf(pdf)
        best = res['candidate_r'][0] if res['candidate_r'] else {}
        rows.append({
            'filename': pdf.name,
            'doi': pdf.stem,
            'modal_n': res.get('modal_n', ''),
            'best_r': best.get('r', ''),
            'best_r_source': best.get('source', ''),
            'is_estimated': best.get('estimated', ''),
            'all_candidates': json.dumps(res['candidate_r']),
            'n_tables': res.get('n_tables', 0),
            'error': res.get('error', '')
        })
        status = '✅' if best else '⚠️'
        print(f" {status} r={best.get('r','?')} n={res.get('modal_n','?')}")

    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    found = sum(1 for r in rows if r['best_r'])
    print(f"\nDone: {found}/{len(pdfs)} PDFs yielded candidate r values")
    print(f"Output: {output_csv}")


def main():
    parser = argparse.ArgumentParser(description='Extract stats from academic PDFs')
    parser.add_argument('input', nargs='?', help='Single PDF file or directory for batch')
    parser.add_argument('--batch', help='Directory of PDFs for batch processing')
    parser.add_argument('--output', default='batch_stats.csv', help='Output CSV for batch mode')
    args = parser.parse_args()

    if args.batch:
        batch_process(Path(args.batch), Path(args.output))
    elif args.input:
        p = Path(args.input)
        if p.is_dir():
            batch_process(p, Path(args.output))
        else:
            res = extract_stats_from_pdf(p)
            print_results(res)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
