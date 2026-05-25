#!/usr/bin/env python3
"""One-off: normalize bare-prose statistical notation to the thesis's dominant
Vietnamese convention (spaced operators, comma decimal, leading zero for p).
Targets only the specific inconsistent tokens identified by audit; the English
abstract's APA p-values (e.g. "p = .942") and all LaTeX math are left untouched.
"""
FILES = [
    "chuyen_de/cd1/00_cd1_ctu_final_vi.md",
    "chuyen_de/cd2/00_cd2_ctu_final_vi.md",
    "thesis/chuong_3_phuong_phap_vi.md",
    "thesis/chuong_4_ket_qua_vi.md",
    "thesis/chuong_5_ket_luan_de_xuat_vi.md",
]
# Specific inconsistent tokens -> dominant Vietnamese convention.
PAIRS = [
    ("p=.0007", "p < 0,001"),
    ("p=.002", "p = 0,002"),
    ("p<.001", "p < 0,001"),
    ("p<.05", "p < 0,05"),
    ("p=.012", "p = 0,012"),
    ("p=0,005", "p = 0,005"),
    ("p<0,001", "p < 0,001"),
    ("β=+0.155", "β = +0,155"),
    ("β=+0,155", "β = +0,155"),
    ("β=3,119", "β = 3,119"),
    ("β=1,639", "β = 1,639"),
    ("N=84,910–91,982", "N = 84.910–91.982"),
]

def main():
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        n = 0
        for old, new in PAIRS:
            c = text.count(old)
            if c:
                text = text.replace(old, new)
                n += c
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{path}: {n} token(s) normalized")

if __name__ == "__main__":
    main()
