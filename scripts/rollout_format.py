#!/usr/bin/env python3
"""rollout_format.py — chuẩn hóa toàn bộ submission packages theo house-style tạp chí:
  1) Tạo 2 gói mới cho P10 (APJM Springer, IJOEM Emerald) từ gói ABM.
  2) Mask self-citation (double-blind) trong mọi gói live.
  3) Abstract house-style: Emerald=structured (giữ), khác=unstructured (gỡ nhãn).
  4) Điền OSF DOI placeholder.
Không đụng gói DEPRECATED (p3/thunderbird, p6/ibr, p7/jibs, p8/world_development_package).
"""
import re, os, shutil, glob, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
os.chdir(ROOT)

# (paper_dir, pkg, publisher)  publisher in {Emerald,Springer,Elsevier,TF,Wiley,Palgrave}
PACKAGES = [
    ('p3','jed','Emerald'), ('p3','mbr','Emerald'), ('p3','jabs','Emerald'),
    ('p4','mir','Springer'), ('p4','apbr','TF'), ('p4','mbr','Emerald'),
    ('p5','ijoem','Emerald'), ('p5','cms','Emerald'), ('p5','apbr','TF'),
    ('p6','jwb','Elsevier'), ('p6','jim','Elsevier'), ('p6','apjm','Springer'),
    ('p7','ibr','Elsevier'), ('p7','apjm','Springer'),
    ('p8','world_development_redesign','Elsevier'), ('p8','jid','Wiley'), ('p8','ejdr','Palgrave'),
    ('p9_india','mir','Springer'), ('p9_india','ijoem','Emerald'), ('p9_india','jabs','Emerald'),
    ('p10_japan','abm','Palgrave'), ('p10_japan','apjm','Springer'), ('p10_japan','ijoem','Emerald'),
]

def mask_refs(s):
    pat = re.compile(r'(?:Do|Đỗ),\s?T\.?\s?H\.?[^\n]*?(?:and|&)\s+Phan[^\n]*(?:\n(?!\n)[^\n]*)*')
    def repl(m):
        ym = re.search(r'\((\d{4})', m.group(0))
        yr = ym.group(1) if ym else 'n.d.'
        return f'Authors ({yr}). Details omitted for double-blind review.'
    return pat.sub(repl, s)

def mask_intext(s):
    s = re.sub(r'\((?:Do|Đỗ)\s+(?:and|&)\s+Phan,\s*(\d{4}[a-z]?)[^)]*\)', r'(Authors, \1)', s)
    s = re.sub(r'\b(?:Do|Đỗ)\s+(?:and|&)\s+Phan\s+\((\d{4}[a-z]?)\)', r'Authors (\1)', s)
    return s

LABELS = re.compile(r'\*\*(Purpose|Design/methodology/approach|Findings|'
                    r'Originality/value|Research limitations(?:/implications)?|'
                    r'Practical implications|Social implications)[:.]?\*\*[:.,]?\s*')

def destructure(s):
    m = re.search(r'(##\s*Abstract\s*\n)(.*?)(\n\*\*Keywords)', s, re.S)
    if not m:
        return s
    return s[:m.start(2)] + LABELS.sub('', m.group(2)) + s[m.end(2):]

def process_md(path, publisher):
    s = open(path, encoding='utf-8').read()
    o = s
    s = mask_refs(s)
    s = mask_intext(s)
    if publisher != 'Emerald':
        s = destructure(s)
    s = s.replace('[insert OSF DOI at submission]', '10.17605/OSF.IO/Z37KN')
    if s != o:
        open(path, 'w', encoding='utf-8').write(s)
    return s != o

def make_p10(pkg, journal_full):
    src = ROOT/'p10_japan/submission/abm_package'
    dst = ROOT/f'p10_japan/submission/{pkg}_package'
    dst.mkdir(parents=True, exist_ok=True)
    for name in ['01_manuscript_blinded.md','02_title_page.md','03_cover_letter.md']:
        shutil.copy(src/name, dst/name)
    # adjust journal references in title page + cover letter
    for name in ['02_title_page.md','03_cover_letter.md']:
        p = dst/name; t = p.read_text(encoding='utf-8')
        t = t.replace('Asian Business & Management', journal_full)
        t = t.replace('Asian Business and Management', journal_full)
        p.write_text(t, encoding='utf-8')

# --- 1. P10 new packages (copy from structured ABM source) ---
if not (ROOT/'p10_japan/submission/apjm_package/01_manuscript_blinded.md').exists():
    make_p10('apjm', 'Asia Pacific Journal of Management')
    print('  + created p10_japan/apjm_package')
if not (ROOT/'p10_japan/submission/ijoem_package/01_manuscript_blinded.md').exists():
    make_p10('ijoem', 'International Journal of Emerging Markets')
    print('  + created p10_japan/ijoem_package')

# --- 2. process all live packages ---
print("\n  package                          pub        changed  leak_after  abstract")
for paper, pkg, pub in PACKAGES:
    d = ROOT/f'{paper}/submission/{pkg}_package'
    if not d.exists():
        d = ROOT/f'{paper}/submission/{pkg}'   # e.g. world_development_redesign (no _package suffix)
    mds = sorted(d.glob('01_manuscript_blinded*.md'))
    if not mds:
        print(f"  {paper}/{pkg:<20} MISSING"); continue
    changed = any(process_md(m, pub) for m in mds)
    main = mds[0]; s = open(main, encoding='utf-8').read()
    leak = len(re.findall(r'\((?:Do|Đỗ)\s+(?:and|&)\s+Phan|(?:Do|Đỗ)\s+(?:and|&)\s+Phan\s+\(|(?:Do|Đỗ),\s?T\.?\s?H\.?', s))
    struct = 'STRUCT' if re.search(r'\*\*(Purpose|Design/methodology)', s) else 'UNSTRUCT'
    want = 'STRUCT' if pub=='Emerald' else 'UNSTRUCT'
    flag = '' if struct==want else '  <-- MISMATCH'
    print(f"  {paper}/{pkg:<22} {pub:<10} {str(changed):<7}  {leak:<10}  {struct}{flag}")
