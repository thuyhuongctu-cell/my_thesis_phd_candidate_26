#!/usr/bin/env python3
"""
54_fetch_s2_y_papers.py
Fetch S2 abstract + affiliations for Y papers with DOI.
Outputs:
  s2_y_abstracts_YYYYMMDD.csv      — abstract + affiliations per paper
  s2_y_r_candidates_YYYYMMDD.csv   — papers where r/n found in abstract
  icrv_y_s2_coded_YYYYMMDD.csv     — ICRV assignments from affiliations

Usage: python3 54_fetch_s2_y_papers.py [--limit N]
"""
import csv, re, time, sys, argparse, requests
from datetime import date
from pathlib import Path
from collections import Counter

TODAY  = date.today().strftime('%Y%m%d')
BASE   = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'
OUT_ABS  = BASE / f'p6/tools/results/s2_y_abstracts_{TODAY}.csv'
OUT_R    = BASE / f'p6/tools/results/s2_y_r_candidates_{TODAY}.csv'
OUT_ICRV = BASE / f'p6/tools/results/icrv_y_s2_coded_{TODAY}.csv'

S2_URL = 'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}'
S2_FIELDS = 'abstract,year,authors,externalIds,publicationTypes,journal'
SLEEP = 4.0   # unauthenticated rate limit

# ICRV mapping — country keyword → code
ICRV_MAP = {
    # 1 Advanced
    'united states': 1, 'usa': 1, 'u.s.': 1, 'american': 1,
    'united kingdom': 1, 'uk ': 1, 'british': 1, 'england': 1,
    'germany': 1, 'german': 1, 'france': 1, 'french': 1,
    'japan': 1, 'japanese': 1, 'korea': 1, 'korean': 1, 'south korea': 1,
    'australia': 1, 'australian': 1, 'canada': 1, 'canadian': 1,
    'sweden': 1, 'swedish': 1, 'netherlands': 1, 'dutch': 1,
    'norway': 1, 'norwegian': 1, 'denmark': 1, 'danish': 1,
    'finland': 1, 'finnish': 1, 'switzerland': 1, 'swiss': 1,
    'austria': 1, 'belgium': 1, 'belgian': 1, 'israel': 1, 'israeli': 1,
    'singapore': 1, 'taiwan': 1, 'hong kong': 1,
    'italy': 1, 'italian': 1, 'spain': 1, 'spanish': 1,
    'portugal': 1, 'portuguese': 1, 'ireland': 1, 'irish': 1,
    'new zealand': 1, 'greece': 1, 'greek': 1,
    # 2 Upper-middle
    'china': 2, 'chinese': 2, 'brazil': 2, 'brazilian': 2,
    'turkey': 2, 'turkish': 2, 'mexico': 2, 'mexican': 2,
    'malaysia': 2, 'malaysian': 2, 'thailand': 2, 'thai': 2,
    'russia': 2, 'russian': 2, 'argentina': 2, 'argentinian': 2,
    'colombia': 2, 'colombian': 2, 'south africa': 2, 'south african': 2,
    'poland': 2, 'polish': 2, 'czech': 2, 'hungary': 2, 'romanian': 2,
    'chile': 2, 'chilean': 2, 'croatia': 2, 'bulgaria': 2,
    'peru': 2, 'costa rica': 2, 'ecuador': 2,
    # 3 Emerging
    'india': 3, 'indian': 3, 'indonesia': 3, 'indonesian': 3,
    'vietnam': 3, 'vietnamese': 3, 'pakistan': 3, 'pakistani': 3,
    'philippines': 3, 'philippine': 3, 'nigeria': 3, 'nigerian': 3,
    'kenya': 3, 'kenyan': 3, 'ghana': 3, 'ghanaian': 3,
    'egypt': 3, 'egyptian': 3, 'bangladesh': 3, 'sri lanka': 3,
    'morocco': 3, 'moroccan': 3, 'cambodia': 3, 'myanmar': 3,
    # 4 Resource-rich/GCC
    'saudi': 4, 'uae': 4, 'qatar': 4, 'kuwait': 4,
    'oman': 4, 'bahrain': 4, 'iran': 4, 'iranian': 4,
    'kazakhstan': 4, 'azerbaijan': 4, 'algeria': 4,
    # 5 SIDS
    'mauritius': 5, 'fiji': 5, 'samoa': 5, 'maldives': 5,
    'barbados': 5, 'trinidad': 5, 'jamaica': 5, 'malta': 5, 'cyprus': 5,
    # 6 Frontier/LDC
    'ethiopia': 6, 'cambodia': 6, 'laos': 6, 'malawi': 6,
    'mozambique': 6, 'rwanda': 6, 'senegal': 6, 'tanzania': 6,
    'uganda': 6, 'zambia': 6, 'haiti': 6,
}

# R-value patterns in abstract
R_PATTERNS = [
    r'r\s*=\s*[–\-]?\s*(0\.\d{2,4})',
    r'r\s*=\s*[\(]?\s*[–\-]?\s*\.(\d{2,4})',
    r'correlation[^.]*?(0\.\d{2,4})',
    r'β\s*=\s*[–\-]?\s*(0\.\d{2,4})',
    r'beta\s*=\s*[–\-]?\s*(0\.\d{2,4})',
]
N_PATTERNS = [
    r'[nN]\s*=\s*(\d{2,6})',
    r'sample\s+(?:of|size)\s+(\d{2,6})',
    r'(\d{2,6})\s+(?:firms?|companies|observations|obs\.|enterprises)',
]

def guess_icrv_from_text(text):
    t = text.lower()
    for kw, code in ICRV_MAP.items():
        if kw in t:
            return code, kw
    return 0, ''

def scan_r(abstract):
    """Scan abstract for r values. Returns list of (value, pattern_type)."""
    hits = []
    for pat in R_PATTERNS:
        for m in re.finditer(pat, abstract, re.IGNORECASE):
            val = m.group(1)
            try:
                fval = float('0.' + val) if not val.startswith('0') else float(val)
                if 0 < fval < 1:
                    hits.append(fval)
            except:
                pass
    return hits

def scan_n(abstract):
    """Scan abstract for sample size."""
    for pat in N_PATTERNS:
        m = re.search(pat, abstract, re.IGNORECASE)
        if m:
            try:
                n = int(m.group(1))
                if 10 < n < 500000:
                    return n
            except:
                pass
    return None

def fetch_s2(doi):
    try:
        url = S2_URL.format(doi=doi)
        r = requests.get(url, params={'fields': S2_FIELDS}, timeout=15)
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 429:
            time.sleep(30)
            return None
        return None
    except:
        return None

def main(limit=None):
    with open(TRACKER, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    y_with_doi = [r for r in rows
                  if r.get('fulltext_screening_decision','').strip() == 'Y'
                  and r.get('doi','').strip()
                  and not r.get('converted_r','').strip()]  # skip already extracted

    if limit:
        y_with_doi = y_with_doi[:limit]

    print(f'Y papers with DOI (pending extraction): {len(y_with_doi)}')

    abs_rows, r_rows, icrv_rows = [], [], []
    icrv_updates = {}  # seq → icrv code

    for i, row in enumerate(y_with_doi, 1):
        seq = row['seq']
        doi = row['doi'].strip()
        title = row.get('title','')
        current_icrv = row.get('icrv','').strip()

        if i % 25 == 0:
            print(f'  [{i}/{len(y_with_doi)}] seq={seq}')
            # Save interim
            _write(abs_rows, r_rows, icrv_rows)

        data = fetch_s2(doi)
        time.sleep(SLEEP)

        if not data:
            abs_rows.append({'seq': seq, 'doi': doi, 'title': title,
                             's2_found': 0, 'abstract': '', 'affiliations': '',
                             'r_found': '', 'n_found': '', 'icrv_s2': ''})
            continue

        abstract = data.get('abstract') or ''
        authors  = data.get('authors') or []
        affil_text = ' '.join(
            a.get('affiliations', [''])[0] if a.get('affiliations') else ''
            for a in authors
        ).strip()

        # Guess ICRV
        icrv_code, icrv_source = 0, ''
        if not current_icrv:
            icrv_code, icrv_kw = guess_icrv_from_text(affil_text + ' ' + title)
            if icrv_code:
                icrv_source = f'affil:{icrv_kw}'
                icrv_updates[seq] = str(icrv_code)
                icrv_rows.append({'seq': seq, 'doi': doi, 'title': title[:80],
                                  'icrv_coded': icrv_code, 'source': icrv_source,
                                  'affil_snippet': affil_text[:100]})

        # Scan for r/n
        r_vals = scan_r(abstract) if abstract else []
        n_val  = scan_n(abstract) if abstract else None

        abs_row = {
            'seq': seq, 'doi': doi, 'title': title[:100],
            's2_found': 1, 'abstract': abstract[:500],
            'affiliations': affil_text[:200],
            'r_found': ';'.join(str(v) for v in r_vals),
            'n_found': str(n_val) if n_val else '',
            'icrv_s2': str(icrv_code) if icrv_code else ''
        }
        abs_rows.append(abs_row)

        if r_vals or n_val:
            r_rows.append({**abs_row, 'r_candidates': str(r_vals), 'n_candidate': str(n_val)})

    _write(abs_rows, r_rows, icrv_rows)

    # Apply ICRV updates to tracker
    if icrv_updates:
        print(f'\nApplying {len(icrv_updates)} ICRV updates to tracker...')
        for row in rows:
            if row['seq'] in icrv_updates and not row.get('icrv','').strip():
                row['icrv'] = icrv_updates[row['seq']]
        with open(TRACKER, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader(); w.writerows(rows)
        print(f'Tracker updated with {len(icrv_updates)} new ICRV codes.')

    print(f'\nDone. Abstracts: {len(abs_rows)} | R-candidates: {len(r_rows)} | ICRV coded: {len(icrv_rows)}')
    print(f'Output: {OUT_ABS}')

def _write(abs_rows, r_rows, icrv_rows):
    if abs_rows:
        with open(OUT_ABS, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=abs_rows[0].keys())
            w.writeheader(); w.writerows(abs_rows)
    if r_rows:
        with open(OUT_R, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=r_rows[0].keys())
            w.writeheader(); w.writerows(r_rows)
    if icrv_rows:
        with open(OUT_ICRV, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=icrv_rows[0].keys())
            w.writeheader(); w.writerows(icrv_rows)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--limit', type=int, default=None, help='Limit number of papers (for testing)')
    args = p.parse_args()
    main(args.limit)
