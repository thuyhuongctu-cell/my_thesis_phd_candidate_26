#!/usr/bin/env python3
"""
52_extract_r_from_abstracts.py
Extract effect sizes (r, β) from S2 abstracts for Y papers.
Sets ready_for_r=1 where a convertible statistic is found.

Input:  fulltext_to_extraction_tracker_v3.csv  (Y rows, converted_r blank)
        s2_abstracts_unsure_YYYYMMDD.csv        (already fetched abstracts)
        (also queries S2 for Y papers not already in abstract file)
Output: results/r_extraction_log_YYYYMMDD.csv
        UPDATES tracker: converted_r, sample_size_n, ready_for_r, conversion_formula

Conversion formulas used:
  r = t / sqrt(t^2 + df)        [t-to-r, Borenstein 2009]
  r = sqrt(F / (F + df_error))   [F-to-r, df1=1 assumed]
  r ≈ β (standardized)           [for OLS standardized beta]
"""
import csv, re, time, json, math, sys
from datetime import date
from pathlib import Path
from urllib import request, error

TODAY = date.today().strftime('%Y%m%d')
BASE  = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'
S2_ABSTRACT_FILE = BASE / f'p6/tools/results/s2_abstracts_unsure_{TODAY}.csv'
OLD_ABSTRACT_FILE = BASE / 'p6/tools/results/abstracts_20260520.csv'  # fallback cache
OUT_LOG = BASE / f'p6/tools/results/r_extraction_log_{TODAY}.csv'

DELAY = 4.0
S2_BASE = 'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}'

# ── Regex patterns for statistical values ────────────────────────────────────
PAT_R     = re.compile(r'\br\s*[=≈]\s*([-−]?\d+\.\d+)', re.I)
PAT_BETA  = re.compile(r'\bβ\s*[=≈]\s*([-−]?\d+\.\d+)|\bstandardized (?:beta|coefficient)\s+(?:of\s+)?([-−]?\d+\.\d+)', re.I)
PAT_T     = re.compile(r'\bt\s*[=≈(]\s*([-−]?\d+\.?\d*)[\s,;)]\s*(?:df\s*[=≈]\s*(\d+))?', re.I)
PAT_N     = re.compile(r'\bn\s*[=≈]\s*(\d{2,6})\b|sample\s+(?:size\s+)?(?:of\s+)?n?\s*=?\s*(\d{2,6})', re.I)
PAT_F     = re.compile(r'\bF\s*\((\d+)\s*[,;]\s*(\d+)\)\s*[=≈]\s*(\d+\.?\d*)', re.I)
PAT_CORR  = re.compile(r'correlation\s+(?:coefficient\s+)?(?:of\s+|was\s+)?([-−]?\d+\.\d+)', re.I)
PAT_NEGNUM = re.compile(r'−')

def clean_num(s: str) -> float:
    """Handle Unicode minus sign."""
    return float(PAT_NEGNUM.sub('-', s))

def extract_stats(text: str) -> dict:
    """Extract r/β/t/F/n from text. Returns dict with found values."""
    result = {}
    text = text.replace('−', '-').replace('–', '-')

    m = PAT_R.search(text)
    if m:
        try: result['r'] = abs(clean_num(m.group(1))); result['formula'] = 'direct'
        except: pass

    m = PAT_CORR.search(text)
    if m and 'r' not in result:
        try: result['r'] = abs(clean_num(m.group(1))); result['formula'] = 'direct_corr'
        except: pass

    m = PAT_BETA.search(text)
    if m and 'r' not in result:
        val = m.group(1) or m.group(2)
        if val:
            try: result['r'] = abs(clean_num(val)); result['formula'] = 'beta_as_r'
            except: pass

    m = PAT_N.search(text)
    if m:
        try: result['n'] = int(m.group(1) or m.group(2))
        except: pass

    # t → r conversion (need both t and n)
    if 'r' not in result:
        m = PAT_T.search(text)
        if m:
            try:
                t = abs(clean_num(m.group(1)))
                n_val = result.get('n', 0)
                if n_val > 2:
                    df = n_val - 2
                    r = t / math.sqrt(t**2 + df)
                    result['r'] = round(r, 4); result['formula'] = 't_to_r'
            except: pass

    # F → r (need F(1, df) form)
    if 'r' not in result:
        m = PAT_F.search(text)
        if m:
            try:
                df1, df2, fval = int(m.group(1)), int(m.group(2)), float(m.group(3))
                if df1 == 1:
                    r = math.sqrt(fval / (fval + df2))
                    result['r'] = round(r, 4); result['formula'] = 'F_to_r'
            except: pass

    return result

def s2_fetch_abstract(doi: str) -> str:
    url = S2_BASE.replace('{doi}', doi) + '?fields=abstract'
    try:
        req = request.Request(url, headers={
            'User-Agent': 'P6-MetaAnalysis/1.0 (mailto:huongdt@vlute.edu.vn)',
            'Accept': 'application/json'
        })
        with request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode())
            return data.get('abstract') or ''
    except:
        return ''

def main():
    # Load existing abstracts — old cache first, then today's S2 fetch (overwrites if both)
    existing_abstracts = {}
    if OLD_ABSTRACT_FILE.exists():
        with open(OLD_ABSTRACT_FILE, newline='', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                if row.get('abstract','').strip():
                    existing_abstracts[row['seq'].strip()] = row['abstract'].strip()
        print(f'Loaded {len(existing_abstracts)} abstracts from old cache {OLD_ABSTRACT_FILE.name}')
    if S2_ABSTRACT_FILE.exists():
        with open(S2_ABSTRACT_FILE, newline='', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                if row.get('abstract','').strip():
                    existing_abstracts[row['seq'].strip()] = row['abstract'].strip()
        print(f'Loaded/merged {len(existing_abstracts)} total cached abstracts (incl. {S2_ABSTRACT_FILE.name})')

    with open(TRACKER, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Y papers with no converted_r
    targets = [r for r in rows
               if r.get('fulltext_screening_decision','').strip() == 'Y'
               and not r.get('converted_r','').strip()]
    print(f'Y papers needing r extraction: {len(targets)}')

    log_rows = []
    updated = 0
    fetched = 0

    for i, row in enumerate(targets, 1):
        seq = row['seq'].strip()
        doi = row.get('doi','').strip()
        title = row.get('title','').strip()

        if i % 50 == 0:
            print(f'  [{i}/{len(targets)}] seq={seq} | updated so far: {updated}', flush=True)

        # Get abstract
        abstract = existing_abstracts.get(seq, '')
        if not abstract and doi:
            abstract = s2_fetch_abstract(doi)
            time.sleep(DELAY)
            fetched += 1

        if not abstract:
            log_rows.append({'seq': seq, 'doi': doi, 'title': title[:60],
                              'r_found': '', 'n_found': '', 'formula': '',
                              'source': 'no_abstract'})
            continue

        stats = extract_stats(abstract)
        r_val = stats.get('r', '')
        n_val = stats.get('n', '')
        formula = stats.get('formula', '')

        log_rows.append({'seq': seq, 'doi': doi, 'title': title[:60],
                          'r_found': r_val, 'n_found': n_val, 'formula': formula,
                          'source': 'S2_abstract'})

        if r_val and 0 < float(r_val) < 1:
            for r in rows:
                if r['seq'].strip() == seq:
                    r['converted_r'] = str(round(float(r_val), 4))
                    if n_val:
                        r['sample_size_n'] = str(int(n_val))
                    r['conversion_formula'] = formula
                    r['ready_for_r'] = '1'
                    updated += 1
                    break

    # Write log
    with open(OUT_LOG, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['seq','doi','title','r_found','n_found','formula','source'])
        w.writeheader(); w.writerows(log_rows)

    # Update tracker
    with open(TRACKER, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

    print(f'\nExtracted r from {updated} papers (fetched {fetched} new abstracts).')
    ready_total = sum(1 for r in rows if str(r.get('ready_for_r','')).strip() == '1')
    print(f'Total ready_for_r=1: {ready_total}')
    print(f'Log → {OUT_LOG}')

if __name__ == '__main__':
    main()
