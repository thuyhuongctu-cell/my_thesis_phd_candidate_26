#!/usr/bin/env python3
"""
50_fetch_s2_abstracts_unsure.py
Fetch abstracts for UNSURE papers (with DOIs) from Semantic Scholar API.
Also captures: year, venue, authors, country affiliations for ICRV coding.

Input:  fulltext_to_extraction_tracker_v3.csv  (UNSURE rows with DOI)
Output: results/s2_abstracts_unsure_YYYYMMDD.csv  (seq, doi, abstract, s2_year, s2_venue, affiliations)
        results/s2_auto_screen_YYYYMMDD.csv       (auto-screened decisions)

Rate: 1 req / 4s unauthenticated (~757 papers = ~50 min)
"""
import csv, time, json, sys, re
from datetime import date
from pathlib import Path
from urllib import request, error

TODAY = date.today().strftime('%Y%m%d')
BASE  = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'
OUT_ABS  = BASE / f'p6/tools/results/s2_abstracts_unsure_{TODAY}.csv'
OUT_SCREEN = BASE / f'p6/tools/results/s2_auto_screen_{TODAY}.csv'

S2_BASE = 'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}'
S2_FIELDS = 'title,abstract,year,venue,publicationTypes,authors,openAccessPdf'
DELAY = 4.0   # 4s between requests = safe below 100/5min limit

# ── L2 exclusion rules (any hit = N) ──────────────────────────────────────
EXCLUDE_PATTERNS = [
    r'\bcountry.?level\b', r'\bmacro.?level\b', r'\bnational.?level\b',
    r'\bqualitative\b', r'\bcase study\b', r'\bethno',
    r'\bhealth\b', r'\bmedical\b', r'\bclinical\b',
    r'\benvironment\b', r'\bcarbon\b', r'\bsustainab',
    r'\bannual report\b', r'\bfinancial report',
    r'\bconceptual\b', r'\btheoretical framework\b',
    r'\bdeterminants? of (export|internationaliz|FDI)\b',
    r'\bantecedents? of\b',
    r'\bexport barriers\b',
    r'\bwhy firms internationaliz',
    r'\bimmigrant\b', r'\bwage\b', r'\bemployment\b',
    r'\bliterature review\b', r'\bmeta.?analysis\b', r'\bsystematic review\b',
    r'\binnovation\b.*\bperformance\b(?!.*export)',  # innovation-only studies
]
INCLUDE_SIGNALS = [
    r'\bfirm.?level\b', r'\bfirm performance\b',
    r'\bROA\b', r'\bROE\b', r'\bTobin', r'\bsales growth\b', r'\bproductivity\b',
    r'\bexport intensity\b', r'\bexport ratio\b', r'\bFSTS\b',
    r'\bdegree of internationali',
    r'\bforeign sales\b', r'\boutward FDI\b',
    r'\bpanel data\b', r'\bregression\b', r'\bOLS\b',
    r'\bfixed effect\b', r'\brandom effect\b',
]

def s2_fetch(doi: str) -> dict | None:
    url = S2_BASE.replace('{doi}', doi) + '?fields=' + S2_FIELDS
    try:
        req = request.Request(url, headers={
            'User-Agent': 'P6-MetaAnalysis/1.0 (mailto:huongdt@vlute.edu.vn)',
            'Accept': 'application/json'
        })
        with request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode())
    except error.HTTPError as e:
        if e.code == 429:
            print(f'  Rate limited — sleeping 30s')
            time.sleep(30)
        return None
    except Exception:
        return None

def auto_screen(title: str, abstract: str) -> tuple[str, str]:
    """Returns (decision, reason): Y/N/UNSURE"""
    text = (title + ' ' + abstract).lower()
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, text, re.I):
            return 'N', f'auto-N: matches exclusion pattern [{pat[:40]}]'
    include_hits = sum(1 for p in INCLUDE_SIGNALS if re.search(p, text, re.I))
    if include_hits >= 3:
        return 'UNSURE_L2', 'auto-flagged: multiple include signals; needs full-text review'
    if include_hits >= 1:
        return 'UNSURE', 'auto: some include signals but insufficient for Y'
    return 'N', 'auto-N: no firm-level I→P signals in title/abstract'

def main():
    # Load UNSURE papers with DOI
    with open(TRACKER, newline='', encoding='utf-8') as f:
        tracker_rows = list(csv.DictReader(f))

    unsure_doi = [r for r in tracker_rows
                  if r.get('fulltext_screening_decision','').strip() == 'UNSURE'
                  and r.get('doi','').strip()]
    print(f'UNSURE papers with DOI: {len(unsure_doi)}')

    abs_rows = []
    screen_rows = []

    for i, row in enumerate(unsure_doi, 1):
        seq = row['seq'].strip()
        doi = row['doi'].strip()
        title = row.get('title','').strip()

        if i % 50 == 0:
            print(f'  [{i}/{len(unsure_doi)}] fetching seq={seq}', flush=True)

        data = s2_fetch(doi)
        time.sleep(DELAY)

        if not data:
            abs_rows.append({'seq': seq, 'doi': doi, 'abstract': '', 'source': 'S2_FAIL',
                             's2_year': '', 's2_venue': '', 'affiliations': ''})
            screen_rows.append({'seq': seq, 'doi': doi, 'title': title,
                                 'auto_decision': 'UNSURE', 'auto_reason': 'S2 fetch failed'})
            continue

        abstract = data.get('abstract') or ''
        s2_year  = str(data.get('year') or '')
        s2_venue = data.get('venue') or ''
        # Affiliations — for ICRV coding
        authors = data.get('authors') or []
        affils = '; '.join(a.get('affiliations', [{}])[0].get('name', '') if a.get('affiliations') else ''
                           for a in authors[:5] if a.get('affiliations'))

        abs_rows.append({'seq': seq, 'doi': doi, 'abstract': abstract,
                         'source': 'S2', 's2_year': s2_year,
                         's2_venue': s2_venue, 'affiliations': affils})

        decision, reason = auto_screen(title, abstract)
        screen_rows.append({'seq': seq, 'doi': doi, 'title': title,
                             'abstract_snippet': abstract[:200],
                             'auto_decision': decision, 'auto_reason': reason})

    # Write outputs
    abs_fields = ['seq','doi','abstract','source','s2_year','s2_venue','affiliations']
    with open(OUT_ABS, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=abs_fields)
        w.writeheader(); w.writerows(abs_rows)

    screen_fields = ['seq','doi','title','abstract_snippet','auto_decision','auto_reason']
    with open(OUT_SCREEN, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=screen_fields)
        w.writeheader(); w.writerows(screen_rows)

    from collections import Counter
    dec_counts = Counter(r['auto_decision'] for r in screen_rows)
    print(f'\nDone. Fetched {len(abs_rows)} abstracts.')
    print(f'Auto-screen: {dict(dec_counts)}')
    print(f'Abstracts → {OUT_ABS}')
    print(f'Screen log → {OUT_SCREEN}')

if __name__ == '__main__':
    main()
