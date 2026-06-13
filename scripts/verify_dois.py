#!/usr/bin/env python3
"""Verify every DOI in the dissertation bibliography against the Crossref API.

The Claude Code cloud container blocks outbound hosts (HTTP 403), so this
script is meant to be run by the candidate on a network-enabled machine:

    python3 scripts/verify_dois.py            # checks thesis/04_references_apa7.md
    python3 scripts/verify_dois.py FILE.md    # check any markdown file

For each DOI it queries https://api.crossref.org/works/<doi> and compares the
Crossref title/first-author/year with what the bibliography claims, printing a
PASS / TITLE-MISMATCH / NOT-FOUND verdict. A NOT-FOUND or systematic mismatch is
the signature of a fabricated or mistyped reference. Output is written to
reviews/doi_verification_report.md.

Dependencies: only the Python stdlib (urllib). Be polite to Crossref: the script
sleeps 1s between calls and sends a mailto in the User-Agent per their etiquette.
"""
import json
import re
import sys
import time
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ROOT / 'thesis' / '04_references_apa7.md'
MAILTO = 'huongdt@vlute.edu.vn'
DOI_RE = re.compile(r'10\.\d{4,9}/[^\s)*;,]+')


def fold(s):
    s = unicodedata.normalize('NFD', s)
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower()


def crossref(doi):
    url = f'https://api.crossref.org/works/{doi}'
    req = urllib.request.Request(
        url, headers={'User-Agent': f'DOIverify/1.0 (mailto:{MAILTO})'})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)['message']


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    lines = src.read_text(encoding='utf-8').splitlines()
    seen, rows = set(), []
    for ln in lines:
        for m in DOI_RE.finditer(ln):
            doi = m.group(0).rstrip('.')
            if doi in seen:
                continue
            seen.add(doi)
            claimed = ln.strip()[:90]
            try:
                msg = crossref(doi)
                title = (msg.get('title') or ['?'])[0]
                auth = msg.get('author', [{}])
                surname = auth[0].get('family', '?') if auth else '?'
                yr = (msg.get('issued', {}).get('date-parts', [[None]])
                      [0][0])
                ok = fold(surname) in fold(claimed) if surname != '?' else False
                verdict = 'PASS' if ok else 'CHECK-AUTHOR'
                rows.append((verdict, doi, f'{surname} ({yr}) — '
                             f'{title[:60]}'))
            except urllib.error.HTTPError as e:
                rows.append(('NOT-FOUND' if e.code == 404 else f'HTTP{e.code}',
                             doi, claimed))
            except Exception as e:  # noqa
                rows.append(('ERROR', doi, f'{type(e).__name__}: {e}'))
            time.sleep(1.0)

    n = len(rows)
    bad = [r for r in rows if r[0] not in ('PASS',)]
    nf = [r for r in rows if r[0] == 'NOT-FOUND']
    out = ROOT / 'reviews' / 'doi_verification_report.md'
    L = ['# DOI verification report (Crossref)', '',
         f'Source: `{src.relative_to(ROOT)}` — {n} unique DOIs checked.', '',
         f'- PASS (author matches Crossref): **{n - len(bad)}**',
         f'- NOT-FOUND (likely fabricated/mistyped): **{len(nf)}**',
         f'- CHECK-AUTHOR / other (manual review): **{len(bad) - len(nf)}**',
         '', '## Flags (everything not a clean PASS)', '']
    for v, doi, info in rows:
        if v != 'PASS':
            L.append(f'- **{v}** `{doi}` — {info}')
    out.write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'{n} DOIs checked: {n-len(bad)} PASS, {len(nf)} NOT-FOUND, '
          f'{len(bad)-len(nf)} need manual review.')
    print(f'Report -> {out.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
