#!/usr/bin/env python3
"""Orphan / missing reference audit for the dissertation bibliography.

Compares full APA entries in thesis/04_references_apa7.md against in-text
citations across all manuscript Markdown files (thesis, chuyen_de, p10_japan,
manuscripts). Reports:
  - ORPHANS  : bibliography entries never cited in any manuscript
  - MISSING  : (author, year) cited in text but absent from the bibliography

Matching is by (first-author-surname, year), accent-folded and lowercased, with
year-suffix tolerance (2026a/2026b collapse to 2026 for a relaxed second pass).
This is a *report only* tool; it never edits the bibliography.

Run: python3 scripts/reference_audit.py
"""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / 'thesis' / '04_references_apa7.md'
SRC_GLOBS = ['thesis/*.md', 'chuyen_de/*/*.md', 'p10_japan/*.md',
             'manuscripts/*.md']


def fold(s: str) -> str:
    """Lowercase + strip diacritics (NFD) so Vietnamese/accents match ASCII."""
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.lower().strip()


# --- 1. Parse bibliography entries -> {(surname, year): raw line} ----------
def parse_bib(text: str):
    entries = {}
    # An entry starts at line-start, optional ** bold, then
    # "Surname[ prefix], I." ... "(YEAR" somewhere early.
    line_re = re.compile(r'^\*{0,2}([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ \'\-]+?),\s'
                         r'[^()]*?\((\d{4})[a-z]?')
    for raw in text.splitlines():
        m = line_re.match(raw)
        if not m:
            continue
        surname = fold(m.group(1).split(',')[0].split(' ')[0])
        # use the LAST whitespace-token of the surname phrase for multiword
        surname_full = fold(m.group(1))
        key = (surname_full.split()[-1], m.group(2))
        entries.setdefault(key, raw.strip())
    return entries


# --- 2. Parse in-text citations across manuscripts -> set of keys ----------
CITE_PATTERNS = [
    # (Author, 2020) / (Author & Other, 2020) / (Author et al., 2020)
    re.compile(r'\(([A-ZÀ-Ý][A-Za-zÀ-ÿ\'\-]+)[^()]*?(\d{4})[a-z]?\)'),
    # Author (2020) / Author et al. (2020) / Author & Other (2020)
    re.compile(r'([A-ZÀ-Ý][A-Za-zÀ-ÿ\'\-]+)\s'
               r'(?:et al\.|và|&|and|,)?[^()\n]{0,40}?\((\d{4})[a-z]?\)'),
]


def parse_citations():
    keys = set()
    files = []
    for g in SRC_GLOBS:
        files.extend(ROOT.glob(g))
    for f in files:
        if f.name == '04_references_apa7.md':
            continue
        txt = f.read_text(encoding='utf-8', errors='ignore')
        for pat in CITE_PATTERNS:
            for m in pat.finditer(txt):
                keys.add((fold(m.group(1)).split()[-1], m.group(2)))
    return keys, len(files)


def main():
    bib = parse_bib(BIB.read_text(encoding='utf-8'))
    cited, nfiles = parse_citations()
    cited_years = {y for (_, y) in cited}
    cited_relaxed = {s for (s, _) in cited}

    orphans, weak = [], []
    for key, raw in sorted(bib.items()):
        surname, year = key
        if key in cited:
            continue
        # relaxed: same surname cited in a neighbouring year suffix
        if surname in cited_relaxed and year in cited_years:
            weak.append((key, raw))
        else:
            orphans.append((key, raw))

    bib_keys = set(bib)
    missing = sorted(k for k in cited if k not in bib_keys
                     and k[0] not in {'p', 'wbes', 'icrv', 'cdcm', 'fip'})

    print(f'Bibliography entries parsed : {len(bib)}')
    print(f'Manuscript files scanned    : {nfiles}')
    print(f'Distinct in-text cite keys  : {len(cited)}')
    print(f'STRONG orphans (no surname+year match)     : {len(orphans)}')
    print(f'WEAK   orphans (surname cited, year off)    : {len(weak)}')
    print(f'MISSING (cited but not in bib)              : {len(missing)}')
    return bib, orphans, weak, missing


if __name__ == '__main__':
    bib, orphans, weak, missing = main()
    if '--report' in sys.argv:
        out = ROOT / 'reviews' / 'orphan_reference_audit_2026-06-13.md'
        L = ['# Kiểm toán orphan references — 2026-06-13', '',
             'Sinh tự động bởi `scripts/reference_audit.py`. *Chỉ báo cáo, '
             'không tự xóa.* Khớp theo (họ tác giả đầu, năm), bỏ dấu.', '',
             f'- Tổng entry thư mục: **{len(bib)}**',
             f'- STRONG orphan (không khớp họ+năm ở bất kỳ bản thảo nào): '
             f'**{len(orphans)}**',
             f'- WEAK orphan (cùng họ được trích, lệch năm — cần soát tay): '
             f'**{len(weak)}**',
             f'- MISSING (trích trong văn bản nhưng thiếu trong thư mục): '
             f'**{len(missing)}**', '',
             '## STRONG orphans (ứng viên gỡ bỏ — cần NCS xác nhận)', '']
        for (s, y), raw in orphans:
            L.append(f'- ({s}, {y}) — {raw[:120]}')
        L += ['', '## WEAK orphans (soát tay — có thể là biến thể năm)', '']
        for (s, y), raw in weak:
            L.append(f'- ({s}, {y}) — {raw[:120]}')
        L += ['', '## MISSING (trích nhưng thiếu entry — cần bổ sung)', '']
        for s, y in missing:
            L.append(f'- ({s}, {y})')
        out.write_text('\n'.join(L) + '\n', encoding='utf-8')
        print(f'\nReport -> {out.relative_to(ROOT)}')
