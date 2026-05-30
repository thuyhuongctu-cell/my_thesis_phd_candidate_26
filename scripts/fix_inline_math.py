#!/usr/bin/env python3
"""One-off (task c): convert the high-frequency bare Unicode math tokens
(coefficient subscripts β₀–β₅ and squared/cubed terms) to LaTeX inline math.
Operates ONLY on text outside existing $...$ / $$...$$ / \\begin..\\end math,
so pre-formatted equations are untouched. Ordered longest-first to avoid
partial-overlap corruption (e.g. ΔR² before R²).
"""
import re

FILES = [
    "chuyen_de/cd1/00_cd1_ctu_final_vi.md",
    "chuyen_de/cd2/00_cd2_ctu_final_vi.md",
    "thesis/chuong_3_phuong_phap_vi.md",
    "thesis/chuong_4_ket_qua_vi.md",
    "thesis/chuong_5_ket_luan_de_xuat_vi.md",
]
# Order matters: specific/compound tokens before plain ones.
PAIRS = [
    ("FSTS_c²", r"$\text{FSTS}_c^2$"),
    ("DDXK_c²", r"$\text{DDXK}_c^2$"),
    ("ΔR²", r"$\Delta R^2$"),
    ("FSTS³", r"$\text{FSTS}^3$"),
    ("FSTS²", r"$\text{FSTS}^2$"),
    ("R²", r"$R^2$"),
    ("I²", r"$I^2$"),
    ("f²", r"$f^2$"),
    ("β₀", r"$\beta_0$"), ("β₁", r"$\beta_1$"), ("β₂", r"$\beta_2$"),
    ("β₃", r"$\beta_3$"), ("β₄", r"$\beta_4$"), ("β₅", r"$\beta_5$"),
]
MATH = re.compile(r"(\$\$.*?\$\$|\$[^$\n]*\$|\\begin\{[^}]*\}.*?\\end\{[^}]*\})", re.S)

def conv(seg):
    for old, new in PAIRS:
        seg = seg.replace(old, new)
    return seg

def main():
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        parts = MATH.split(text)
        new = "".join(p if i % 2 else conv(p) for i, p in enumerate(parts))
        n = sum(text.count(o) for o, _ in PAIRS) - sum(new.count(o) for o, _ in PAIRS)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print(f"{path}: {n} tokens converted")

if __name__ == "__main__":
    main()
