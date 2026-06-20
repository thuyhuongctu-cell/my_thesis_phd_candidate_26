#!/usr/bin/env python3
"""build_journal_latex.py — sinh .tex submission đầy đủ từ manuscript markdown,
theo document class của tạp chí đích, rồi biên dịch PDF (xelatex).

- Tạp chí Emerald (JED/IJOEM/MBR/CMS/JABS) nộp Word qua ScholarOne → KHÔNG sinh LaTeX.
- Elsevier dùng `elsarticle` (có sẵn trong TeX Live). Springer/T&F/Wiley/Palgrave
  cần .cls chính thức (svjour3/interact/WileyNJD); ở đây dùng article-fallback để
  biên dịch xác minh, và ghi chú swap class cho bản nộp cuối.

Cách dùng:  python3 scripts/build_journal_latex.py p4_mir p4_apbr
            python3 scripts/build_journal_latex.py --all
"""
import re, sys, subprocess, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
os.chdir(ROOT)

# documentclass: 'elsarticle' (native) | 'article' (fallback cho Springer/T&F/Wiley)
TARGETS = {
  # P4 Singapore
  'p4_mir':  dict(pkg='p4/submission/mir_package',  cls='article',
                  journal='Management International Review (Springer Nature)',
                  swap='Springer svjour3.cls (smallextended) — tải từ Springer Nature LaTeX support; article fallback dùng để xác minh'),
  'p4_apbr': dict(pkg='p4/submission/apbr_package', cls='article',
                  journal='Asia Pacific Business Review (Taylor & Francis)',
                  swap='T&F interact.cls (interactapasample) — tải từ Taylor & Francis; article fallback dùng để xác minh'),
}

def parse_md(md_path):
    s = open(md_path, encoding='utf-8').read()
    lines = s.split('\n')
    title = re.sub(r'^#\s*', '', lines[0]).strip()
    m = re.search(r'##\s*Abstract\s*\n(.*?)\n\*\*Keywords', s, re.S)
    abstract = m.group(1).strip() if m else ''
    mk = re.search(r'\*\*Keywords:?\*\*\s*(.*?)(?:\n\n|\n##)', s, re.S)
    keywords = ' '.join(mk.group(1).split()) if mk else ''
    mb = re.search(r'\n(##\s+1\b.*)$', s, re.S)
    body = mb.group(1).strip() if mb else ''
    return title, abstract, keywords, body

HEADER_TEX = r"""
\setcounter{secnumdepth}{-1}  % giữ numbering thủ công trong manuscript
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{newunicodechar}
\newunicodechar{₀}{\textsubscript{0}}\newunicodechar{₁}{\textsubscript{1}}
\newunicodechar{₂}{\textsubscript{2}}\newunicodechar{₃}{\textsubscript{3}}
\newunicodechar{₄}{\textsubscript{4}}\newunicodechar{₅}{\textsubscript{5}}
\newunicodechar{≈}{$\approx$}\newunicodechar{≤}{$\leq$}\newunicodechar{≥}{$\geq$}
\newunicodechar{×}{$\times$}\newunicodechar{−}{$-$}
"""

def build(key, t):
    pkg = pathlib.Path(t['pkg'])
    md = pkg / '01_manuscript_blinded.md'
    if not md.exists():
        cand = list(pkg.glob('01_manuscript_blinded*.md'))
        md = cand[0] if cand else md
    title, abstract, keywords, body = parse_md(md)

    yaml = "---\ntitle: |\n  " + title + "\nabstract: |\n"
    for ln in abstract.split('\n'):
        yaml += ("  " + ln + "\n") if ln.strip() else "\n"
    yaml += "---\n\n"
    tmpmd = yaml + "**Keywords:** " + keywords + "\n\n" + body

    tmp_path = pkg / '.tmp_journal.md'
    hdr_path = pkg / '.hdr.tex'
    tmp_path.write_text(tmpmd, encoding='utf-8')
    hdr_path.write_text(HEADER_TEX, encoding='utf-8')

    tex_out = pkg / '04_manuscript_latex.tex'
    cmd = ['pandoc', str(tmp_path), '--standalone', '--pdf-engine=xelatex',
           '-V','documentclass=article','-V','classoption=12pt,a4paper',
           '-V','geometry:margin=2.5cm','-V','linestretch=2.0',
           '-V','mainfont=TeX Gyre Termes','-V','mathfont=TeX Gyre Termes Math',
           '-V','colorlinks=true','-V','linkcolor=black','-V','citecolor=black','-V','urlcolor=blue',
           '-V','lang=en','--include-in-header='+str(hdr_path),
           '-f','markdown-yaml_metadata_block+yaml_metadata_block',
           '-o', str(tex_out)]
    subprocess.run(cmd, check=True)

    # prepend journal banner comment
    banner = (f"% ============================================================\n"
              f"% Submission LaTeX source — {t['journal']}\n"
              f"% Document class for final submission: {t['swap']}\n"
              f"% Compile: xelatex 04_manuscript_latex.tex (x2). Figures submitted separately.\n"
              f"% ============================================================\n")
    tex_out.write_text(banner + tex_out.read_text(encoding='utf-8'), encoding='utf-8')

    # compile twice
    ok = True
    for _ in range(2):
        r = subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',
                            '04_manuscript_latex.tex'], cwd=str(pkg),
                           capture_output=True, text=True)
        ok = (r.returncode == 0)
    pdf = pkg / '04_manuscript_latex.pdf'
    # cleanup aux + temp
    for ext in ['.aux','.log','.out']:
        (pkg / ('04_manuscript_latex'+ext)).unlink(missing_ok=True)
    tmp_path.unlink(missing_ok=True); hdr_path.unlink(missing_ok=True)
    miss = ''
    pages = ''
    if pdf.exists():
        try:
            import subprocess as sp
            out = sp.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
            mm = re.search(r'Pages:\s*(\d+)', out); pages = mm.group(1) if mm else '?'
        except Exception:
            pages = '?'
    print(f"  {key:<10} tex={'OK' if tex_out.exists() else 'FAIL'}  pdf={'OK('+pages+'p)' if pdf.exists() else 'FAIL'}")
    return tex_out.exists() and pdf.exists()

if __name__ == '__main__':
    keys = list(TARGETS) if (len(sys.argv)>1 and sys.argv[1]=='--all') else sys.argv[1:]
    if not keys:
        print("usage: build_journal_latex.py <key...> | --all\nkeys:", ', '.join(TARGETS)); sys.exit(1)
    allok = True
    for k in keys:
        if k not in TARGETS:
            print(f"  unknown target {k}"); allok=False; continue
        allok &= build(k, TARGETS[k])
    sys.exit(0 if allok else 1)
