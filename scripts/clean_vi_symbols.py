#!/usr/bin/env python3
"""One-off: normalize non-standard symbols in Vietnamese thesis files for Scopus/WoS.

Safe, high-volume transforms only:
  - " — " (spaced em-dash, U+2014) -> ", "
  - I→P / I → P  -> I-P  (en-dash, U+2013)
  - "hóa → hiệu" -> "hóa – hiệu"  (internationalization-performance relationship)
  - "Internationalization → Performance" -> "Internationalization–Performance"
Edge cases (no-space em-dashes, varied causal/numeric arrows) are left for manual review.
"""
import re
import sys

EM = "—"   # —
EN = "–"   # –

FILES = [
    "chuyen_de/cd1/00_cd1_ctu_final_vi.md",
    "chuyen_de/cd2/00_cd2_ctu_final_vi.md",
    "thesis/chuong_1_gioi_thieu_vi.md",
    "thesis/chuong_2_tong_quan_tai_lieu_vi.md",
    "thesis/chuong_3_phuong_phap_vi.md",
    "thesis/chuong_4_ket_qua_vi.md",
    "thesis/chuong_5_ket_luan_de_xuat_vi.md",
]

ARROW_RULES = [
    (re.compile(r"I\s*→\s*P"), "I" + EN + "P"),
    (re.compile(r"hóa\s*→\s*hiệu"), "hóa " + EN + " hiệu"),
    (re.compile(r"Internationalization\s*→\s*Performance"),
     "Internationalization" + EN + "Performance"),
]

def process(text):
    counts = {}
    for rx, repl in ARROW_RULES:
        text, n = rx.subn(repl, text)
        counts[rx.pattern] = n
    # spaced em-dash -> comma
    spaced = " " + EM + " "
    counts["spaced_emdash"] = text.count(spaced)
    text = text.replace(spaced, ", ")
    return text, counts

def main():
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            original = f.read()
        new, counts = process(original)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        remaining_arrows = len(re.findall(r"[→←↔⇒↑↓]", new))
        remaining_em = new.count(EM)
        print(f"{path}")
        print(f"   {counts}")
        print(f"   remaining arrows={remaining_arrows} remaining em-dash={remaining_em}")

if __name__ == "__main__":
    main()
