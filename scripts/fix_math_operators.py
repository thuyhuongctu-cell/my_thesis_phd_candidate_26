#!/usr/bin/env python3
"""One-off: convert bare Unicode math operators (outside existing LaTeX math)
to LaTeX inline math, so they render font-independently in xelatex PDF and
follow journal notation. Operates ONLY on non-math text segments; content
inside $...$, $$...$$, and \\begin{}..\\end{} is left untouched.
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
]
OPS = {"≈": r"$\approx$", "≥": r"$\geq$", "≤": r"$\leq$",
       "±": r"$\pm$", "≠": r"$\neq$", "∞": r"$\infty$"}

# Segment splitter: capture math spans so we can skip them.
MATH = re.compile(r"(\$\$.*?\$\$|\$[^$\n]*\$|\\begin\{[^}]*\}.*?\\end\{[^}]*\})", re.S)

def convert_nonmath(seg):
    for u, tex in OPS.items():
        seg = seg.replace(u, tex)
    return seg

def main():
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        parts = MATH.split(text)
        # split keeps delimiters at odd indices (the math spans)
        out = []
        for i, p in enumerate(parts):
            out.append(p if i % 2 == 1 else convert_nonmath(p))
        new = "".join(out)
        before = sum(text.count(u) for u in OPS)
        after = sum(new.count(u) for u in OPS)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print(f"{path}: bare ops {before}->{after} remaining (in-math preserved)")

if __name__ == "__main__":
    main()
