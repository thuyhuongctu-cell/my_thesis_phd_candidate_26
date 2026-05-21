#!/usr/bin/env python3
"""
51_icrv_from_s2_affiliations.py
Auto-code ICRV for Y papers with blank ICRV (=0) using Semantic Scholar affiliations.

Input:  fulltext_to_extraction_tracker_v3.csv  (Y rows, ICRV blank/0)
        (optional) s2_abstracts_unsure_YYYYMMDD.csv  for extra affiliation data
Output: results/icrv_s2_coded_YYYYMMDD.csv  (seq, doi, detected_country, icrv_coded)
        UPDATES tracker directly with coded ICRV

ICRV classification rules (6-group):
  1=Advanced: USA UK Germany Japan Korea Singapore Switzerland Australia Canada NL France Italy...
  2=Upper-middle: China Malaysia Thailand Brazil Turkey Mexico Poland Czech Hungary Romania Bulgaria...
  3=Emerging: Vietnam India Indonesia Philippines Pakistan Bangladesh Sri Lanka Ghana Kenya...
  4=Resource-rich/GCC: Saudi Arabia UAE Qatar Kuwait Nigeria Bahrain Oman Azerbaijan Kazakhstan...
  5=SIDS: Fiji Samoa Malta Mauritius Jamaica Trinidad Barbados...
  6=Frontier/LDC: Cambodia Myanmar Ethiopia Laos Tanzania Uganda Mozambique Niger Rwanda...
  0=Multi-country: multiple countries or ambiguous
"""
import csv, time, json, re, sys
from datetime import date
from pathlib import Path
from urllib import request, error
from collections import Counter

TODAY = date.today().strftime('%Y%m%d')
BASE  = Path('/home/user/PAPERS_IN_PHD_2026')
TRACKER = BASE / 'p6/tools/results/fulltext_to_extraction_tracker_v3.csv'
OUT_LOG  = BASE / f'p6/tools/results/icrv_s2_coded_{TODAY}.csv'

DELAY = 4.0
S2_BASE = 'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}'

# Country → ICRV mapping (lowercase keywords in affiliation strings)
ICRV_MAP = {
    1: ['united states','usa','u.s.a','u.s.','united kingdom','uk','england','scotland','wales',
        'germany','germany','german','japan','japan','korea','south korea','republic of korea',
        'singapore','switzerland','australia','canada','netherlands','holland','france','italy',
        'spain','sweden','norway','denmark','finland','austria','belgium','new zealand','ireland',
        'israel','hong kong','taiwan','czech republic','slovakia','portugal','greece'],
    2: ['china','chinese','malaysia','thailand','brazil','turkey','mexico','poland','hungary',
        'romania','bulgaria','croatia','serbia','ukraine','russia','russian','estonia','latvia',
        'lithuania','chile','argentina','colombia','peru','south africa','egypt','morocco','jordan',
        'malaysia','indonesia','philippines'],
    3: ['vietnam','india','indian','indonesia','philippines','pakistan','bangladesh','sri lanka',
        'ghana','kenya','nigeria','ethiopia','nepal','cambodia','myanmar'],
    4: ['saudi arabia','saudi','uae','united arab emirates','qatar','kuwait','bahrain','oman',
        'azerbaijan','kazakhstan','nigeria','angola','algeria'],
    5: ['fiji','samoa','tonga','vanuatu','solomon islands','kiribati','malta','mauritius',
        'barbados','jamaica','trinidad','bahamas','maldives','seychelles','cape verde'],
    6: ['cambodia','myanmar','burma','ethiopia','laos','tanzania','uganda','mozambique',
        'niger','rwanda','sierra leone','malawi','zambia','zimbabwe','sudan','mali','chad'],
}

# Build reverse lookup: keyword → icrv code
def build_lookup():
    lookup = {}
    for code, keywords in ICRV_MAP.items():
        for kw in keywords:
            lookup[kw] = code
    return lookup
KW_LOOKUP = build_lookup()

def detect_icrv(text: str) -> tuple[int, str]:
    """Detect ICRV from affiliation/abstract text. Returns (icrv_code, matched_country)."""
    text_l = text.lower()
    hits = {}
    for kw, code in KW_LOOKUP.items():
        if kw in text_l:
            hits[code] = hits.get(code, []) + [kw]
    if not hits:
        return 0, ''
    if len(hits) > 1:
        # Multiple ICRV groups → multi-country
        countries = [v[0] for v in hits.values()]
        return 0, f'multi: {", ".join(countries[:3])}'
    code = list(hits.keys())[0]
    country = hits[code][0]
    return code, country

def s2_fetch(doi: str) -> dict | None:
    url = S2_BASE.replace('{doi}', doi) + '?fields=authors,venue,abstract'
    try:
        req = request.Request(url, headers={
            'User-Agent': 'P6-MetaAnalysis/1.0 (mailto:huongdt@vlute.edu.vn)',
            'Accept': 'application/json'
        })
        with request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None

def main():
    with open(TRACKER, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Y papers with blank ICRV
    targets = [r for r in rows
               if r.get('fulltext_screening_decision','').strip() == 'Y'
               and (not r.get('icrv','').strip() or r.get('icrv','').strip() == '0')]
    print(f'Y papers with blank ICRV: {len(targets)}')

    log_rows = []
    updated = 0

    for i, row in enumerate(targets, 1):
        seq = row['seq'].strip()
        doi = row.get('doi','').strip()
        title = row.get('title','').strip()

        if i % 25 == 0:
            print(f'  [{i}/{len(targets)}] seq={seq}', flush=True)

        # Try to detect from title first (fast, no API)
        icrv_code, matched = detect_icrv(title)
        source = 'title'

        if icrv_code == 0 and doi:
            data = s2_fetch(doi)
            time.sleep(DELAY)
            if data:
                aff_text = ' '.join(
                    a.get('affiliations', [{}])[0].get('name', '') if a.get('affiliations') else ''
                    for a in (data.get('authors') or [])[:5]
                )
                icrv_code, matched = detect_icrv(aff_text + ' ' + (data.get('abstract') or ''))
                source = 'S2_affil'

        log_rows.append({'seq': seq, 'doi': doi, 'title': title[:80],
                          'detected_country': matched, 'icrv_coded': icrv_code, 'source': source})

        if icrv_code != 0:
            # Find this row in full tracker and update
            for r in rows:
                if r['seq'].strip() == seq:
                    r['icrv'] = str(icrv_code)
                    updated += 1
                    break

    # Write log
    with open(OUT_LOG, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['seq','doi','title','detected_country','icrv_coded','source'])
        w.writeheader(); w.writerows(log_rows)

    # Update tracker
    with open(TRACKER, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

    icrv_dist = Counter(r['icrv_coded'] for r in log_rows)
    print(f'\nCoded {updated} ICRV entries.')
    print(f'ICRV distribution: {dict(sorted(icrv_dist.items()))}')
    print(f'Log → {OUT_LOG}')

if __name__ == '__main__':
    main()
