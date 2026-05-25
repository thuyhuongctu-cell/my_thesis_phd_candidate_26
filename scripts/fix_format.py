#!/usr/bin/env python3
"""One-off: format cleanup for the Vietnamese thesis documents.
  1. en-dash (–) -> hyphen (-), OUTSIDE existing LaTeX math (per user choice).
  2. collapse runs of 2+ spaces -> 1 (skip table rows, code fences, indentation).
  3. remove space before , . ; : and inside ( ) — skip "..." and table rows.
Quotes/ellipsis are left to pandoc `smart` at render time.
"""
import re

FILES = [
    "chuyen_de/cd1/00_cd1_ctu_final_vi.md",
    "chuyen_de/cd2/00_cd2_ctu_final_vi.md",
    "thesis/chuong_1_gioi_thieu_vi.md",
    "thesis/chuong_2_tong_quan_tai_lieu_vi.md",
    "thesis/chuong_3_phuong_phap_vi.md",
    "thesis/chuong_4_ket_qua_vi.md",
    "thesis/chuong_5_ket_luan_de_xuat_vi.md",
    "thesis/04_references_apa7.md",
]
MATH = re.compile(r"(\$\$.*?\$\$|\$[^$\n]*\$|\\begin\{[^}]*\}.*?\\end\{[^}]*\})", re.S)

def endash_to_hyphen(text):
    parts = MATH.split(text)
    return "".join(p if i % 2 else p.replace("–", "-") for i, p in enumerate(parts))

def fix_line_ws(line):
    # skip table rows, code fences, list-of-dashes
    if re.match(r"\s*\|", line) or line.strip().startswith("```") or re.match(r"\s*\|?-{3,}", line):
        return line
    # protect leading indentation
    m = re.match(r"(\s*)(.*)", line)
    lead, body = m.group(1), m.group(2)
    # don't touch lines inside inline math heavy? operate only on text; math spans have no double-space issues
    body = re.sub(r"  +", " ", body)                 # collapse multiple spaces
    body = re.sub(r" +([,;:])", r"\1", body)          # space before , ; :
    body = re.sub(r" +\.(?!\.)", ".", body)           # space before . (not ellipsis)
    body = re.sub(r"\( +", "(", body)                 # space after (
    body = re.sub(r" +\)", ")", body)                 # space before )
    return lead + body

def main():
    in_code = False
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        n_dash = text.count("–")
        text = endash_to_hyphen(text)
        out = []
        in_code = False
        for line in text.split("\n"):
            if line.strip().startswith("```"):
                in_code = not in_code
                out.append(line); continue
            out.append(line if in_code else fix_line_ws(line))
        new = "\n".join(out)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print(f"{path}: en-dash->hyphen {n_dash}; remaining en-dash {new.count('–')} (in-math)")

if __name__ == "__main__":
    main()
