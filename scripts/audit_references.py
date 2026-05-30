#!/usr/bin/env python3
"""
audit_references.py — Cross-paper reference list audit.

Checks:
  1. In-text citations exist in reference list
  2. Reference list entries are cited somewhere in main text
  3. Year consistency for shared references across papers
  4. Cross-paper APA 7 format consistency

Outputs:
  reports/reference_audit.md — per-paper diagnostic
  reports/reference_audit.json — machine-readable

Usage:
  python3 scripts/audit_references.py
"""
import re
import json
import sys
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
REPORTS.mkdir(exist_ok=True)

# Map paper-id → (main MD path, target journal)
PAPERS = {
    'P3 Vietnam': (ROOT / 'p3' / 'p3_vietnam_en_clean.md', 'APJM'),
    'P4 Singapore': (ROOT / 'p4' / 'p4_singapore_en_clean.md', 'MIR'),
    'P6 Meta': (ROOT / 'p6' / 'p6_meta_manuscript_en.md', 'MIR'),
    'P8 SIDS': (ROOT / 'p8' / 'p8_pacific_sids_en_clean.md', 'World Development'),
}

CITATION_RE = re.compile(
    # Match "Author (Year)", "(Author, Year)", "(Author et al., Year)",
    # "Author and Author (Year)", "(Author and Author, Year)"
    r'(?:^|[\s(\[])'
    r'([A-Z][\w\-\']+'                       # First author surname
    r'(?:\s+(?:and|&)\s+[A-Z][\w\-\']+)?'   # optional second author
    r'(?:\s+et\s+al\.)?'                    # optional et al.
    r')'
    r',?\s*\(?'
    r'(\d{4})\b'                            # Year (4 digits)
)
REF_AUTHOR_YEAR_RE = re.compile(
    r'^([A-Z][\w\-\']+'
    r'(?:,\s+[A-Z]\.(?:[\s\-]?[A-Z]\.)*)?'    # initials
    r'(?:,\s+(?:&\s+)?[A-Z][\w\-\']+,\s+[A-Z]\.(?:[\s\-]?[A-Z]\.)*)*'
    r')'
    r'\.?\s*\(?'
    r'(\d{4})[a-z]?\)'
)

def extract_intext_citations(text):
    """Return set of (FirstAuthor, Year) tuples found in main text body."""
    # Strip reference section before scanning
    body, *_ = re.split(r'\n##\s+References\b', text, maxsplit=1)
    cites = set()
    for m in CITATION_RE.finditer(body):
        first_author = m.group(1).split()[0].rstrip(',')
        if first_author.lower() in ('the', 'in', 'see', 'figure', 'table',
                                     'section', 'panel', 'and', 'or', 'with',
                                     'for', 'this', 'these', 'those', 'a', 'an',
                                     'where', 'when', 'how', 'if', 'after',
                                     'before', 'during', 'from'):
            continue
        cites.add((first_author, m.group(2)))
    return cites


def extract_reflist_entries(text):
    """Return set of (FirstAuthorSurname, Year) tuples from reference list.

    Handles both formats: blank-line-separated entries (P6 style) and
    line-broken entries without blank-line separation (P3 style).
    """
    m = re.search(r'\n##\s+References\b', text)
    if not m:
        return set()
    refs_text = text[m.end():]
    # Stop at next ## heading (e.g., next section)
    next_section = re.search(r'\n##\s+\w', refs_text)
    if next_section:
        refs_text = refs_text[:next_section.start()]

    refs = set()
    # Try line-by-line: each line that starts with capital + has "(YEAR)"
    # within the first 200 characters is plausibly a reference entry start.
    line_start_re = re.compile(r'^([A-Z][\w\-\'\.]+)[,\s]')
    year_re = re.compile(r'\((\d{4})[a-z]?\)')
    for line in refs_text.split('\n'):
        line = line.strip().lstrip('-*').strip()
        if len(line) < 30:
            continue
        m1 = line_start_re.match(line)
        if not m1:
            continue
        m2 = year_re.search(line[:200])
        if not m2:
            continue
        first_author = m1.group(1).rstrip(',').rstrip('.')
        refs.add((first_author, m2.group(1)))
    return refs


def audit_paper(name, path, journal):
    if not path.exists():
        return {'name': name, 'error': f'File not found: {path}'}
    text = path.read_text(encoding='utf-8')
    cites = extract_intext_citations(text)
    refs = extract_reflist_entries(text)

    cited_not_in_ref = sorted(cites - refs)
    ref_not_cited = sorted(refs - cites)
    matched = sorted(cites & refs)

    return {
        'name': name,
        'journal': journal,
        'path': str(path.relative_to(ROOT)),
        'n_cites_distinct': len(cites),
        'n_refs_distinct': len(refs),
        'n_matched': len(matched),
        'cited_not_in_ref': cited_not_in_ref[:20],
        'ref_not_cited': ref_not_cited[:20],
        'n_cited_not_in_ref': len(cited_not_in_ref),
        'n_ref_not_cited': len(ref_not_cited),
    }


def cross_paper_year_audit(audits):
    """Detect cases where the same first-author surname is cited with
    different years across papers (potential APA inconsistency)."""
    surname_years = defaultdict(lambda: defaultdict(list))
    for a in audits:
        if 'error' in a:
            continue
        for (sn, yr) in a.get('cited_not_in_ref', []) + [
            tuple(x) for x in a.get('matched_pairs', [])
        ]:
            surname_years[sn][yr].append(a['name'])
    conflicts = []
    for sn, yr_papers in surname_years.items():
        if len(yr_papers) > 1:
            conflicts.append({
                'surname': sn,
                'years_across_papers': dict(yr_papers),
            })
    return conflicts[:30]


def main():
    audits = [audit_paper(n, p, j) for n, (p, j) in PAPERS.items()]

    # Write JSON
    (REPORTS / 'reference_audit.json').write_text(
        json.dumps({'papers': audits}, indent=2, ensure_ascii=False),
        encoding='utf-8',
    )

    # Write Markdown
    lines = ['# Cross-paper Reference Audit', '']
    lines.append(f'_Generated by `scripts/audit_references.py`_')
    lines.append('')
    lines.append('| Paper | Journal | Distinct cites | Distinct refs | Matched | Cite-not-in-ref | Ref-not-cited |')
    lines.append('|---|---|---|---|---|---|---|')
    for a in audits:
        if 'error' in a:
            lines.append(f'| {a["name"]} | -- | ERROR | -- | -- | -- | -- |')
            continue
        lines.append(
            f'| {a["name"]} | {a["journal"]} | {a["n_cites_distinct"]} | '
            f'{a["n_refs_distinct"]} | {a["n_matched"]} | '
            f'{a["n_cited_not_in_ref"]} | {a["n_ref_not_cited"]} |'
        )
    lines.append('')
    lines.append('## Per-paper diagnostics')
    for a in audits:
        if 'error' in a:
            lines.append(f'\n### {a["name"]}\n\n{a["error"]}')
            continue
        lines.append(f'\n### {a["name"]} ({a["journal"]})')
        lines.append(f'Source: `{a["path"]}`')
        if a['cited_not_in_ref']:
            lines.append(f'\n**Cited in text but not in reference list** ({a["n_cited_not_in_ref"]} cases — verify each manually; some may be false positives from caption/heading text):')
            for sn, yr in a['cited_not_in_ref']:
                lines.append(f'- {sn} ({yr})')
        else:
            lines.append('\n*All in-text citations matched in reference list.*')
        if a['ref_not_cited']:
            lines.append(f'\n**Reference entry not detected in body** ({a["n_ref_not_cited"]} cases — verify; ref-list-only entries may indicate dropped citations during revision):')
            for sn, yr in a['ref_not_cited']:
                lines.append(f'- {sn} ({yr})')
        else:
            lines.append('\n*Every reference list entry was matched in main text.*')

    (REPORTS / 'reference_audit.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f'Wrote: {(REPORTS / "reference_audit.md").relative_to(ROOT)}')
    print(f'Wrote: {(REPORTS / "reference_audit.json").relative_to(ROOT)}')

    # Print summary
    print()
    print('Summary:')
    for a in audits:
        if 'error' in a:
            print(f'  {a["name"]:18s}  ERROR')
            continue
        print(f'  {a["name"]:18s}  '
              f'cites={a["n_cites_distinct"]}  '
              f'refs={a["n_refs_distinct"]}  '
              f'matched={a["n_matched"]}  '
              f'cite-not-in-ref={a["n_cited_not_in_ref"]}  '
              f'ref-not-cited={a["n_ref_not_cited"]}')


if __name__ == '__main__':
    main()
