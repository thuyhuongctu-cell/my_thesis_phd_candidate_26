#!/usr/bin/env python3
"""Measure main-text word count of a manuscript markdown file, using the same
definition as the word-count compliance report:
  main text = body from after the Abstract to before References, EXCLUDING
  the abstract, declaration sections, tables (| rows), images, and code blocks;
  headings ARE counted.

Usage: python3 scripts/wc_maintext.py <file.md> [<file.md> ...]
"""
import pathlib, re, sys

DECL = re.compile(r"^#+\s*(acknowledg|funding|conflict|competing|disclosure|"
                  r"data availability|data access|ethic|use of (generative )?ai|"
                  r"declaration of (generative )?ai|ai (use|and data)|highlights)", re.I)

def main_words(path):
    t = pathlib.Path(path).read_text(encoding="utf-8")
    m = re.search(r"(?m)^#+\s*References\s*$", t)
    if m: t = t[:m.start()]
    out=[]; skip=False; ab=False; code=False
    for ln in t.split("\n"):
        s=ln.strip()
        if s.startswith("```"): code=not code; continue
        if code: continue
        if re.match(r"^#+\s", ln):
            if re.match(r"^#+\s*abstract", ln, re.I): ab=True; skip=False; continue
            if DECL.match(ln): skip=True; ab=False; continue
            ab=False; skip=False; out.append(re.sub(r"^#+\s*","",ln)); continue
        if ab or skip: continue
        if s.startswith("|") or s.startswith("!["): continue
        out.append(ln)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*",
                          re.sub(r"[*_`#>\-]+"," "," ".join(out))))

if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(f"{main_words(p):>7,}  {p}")
