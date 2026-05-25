#!/usr/bin/env python3
"""One-off: replace the awkward "văn liệu" with natural academic Vietnamese
for "the literature". Base term -> "các nghiên cứu"; context-specific specials
(literature-review headings, integrative-review method, a citation, and two
phrasings that would otherwise duplicate "nghiên cứu") handled first.
"""
import re

FILES = [
    "chuyen_de/cd1/00_cd1_ctu_final_vi.md",
    "chuyen_de/cd2/00_cd2_ctu_final_vi.md",
    "thesis/14_cd1_part1_intro_theory_vi.md",
    "thesis/15_cd1_part2_findings_vi.md",
    "thesis/16_cd1_part3_cases_conclusion_vi.md",
    "thesis/04_05_chapters_results_discussion_vi.md",
    "thesis/chuong_4_ket_qua_vi.md",
    "thesis/p6_prisma_protocol.md",
]

# Order matters: specials before the two base replacements.
SPECIALS = [
    ("lối tổng quan văn liệu tích hợp", "lối tổng quan tài liệu tích hợp"),
    ("Tổng quan văn liệu về quan hệ quốc tế hóa và hiệu quả kinh doanh",
     "Tổng quan tài liệu về quan hệ quốc tế hóa và hiệu quả kinh doanh"),
    ("Văn liệu kinh doanh quốc tế (international business, IB) đã ghi nhận",
     "Các nghiên cứu trong lĩnh vực kinh doanh quốc tế (international business, IB) đã ghi nhận"),
    ("và văn liệu Caballero, Hoshi và Kashyap", "và nghiên cứu của Caballero, Hoshi và Kashyap"),
    ("Văn liệu về quan hệ quốc tế hóa – hiệu quả là một trong những dòng nghiên cứu",
     "Quan hệ quốc tế hóa – hiệu quả là một trong những dòng nghiên cứu"),
    ("mở rộng văn liệu I–P", "mở rộng dòng nghiên cứu về quan hệ I–P"),
    ("trong văn liệu I–P cho châu Á", "trong các nghiên cứu về quan hệ I–P cho châu Á"),
]
BASE = [
    ("Văn liệu", "Các nghiên cứu"),
    ("văn liệu", "các nghiên cứu"),
]

def main():
    for path in FILES:
        try:
            with open(path, encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"SKIP (missing): {path}")
            continue
        before = len(re.findall(r"[Vv]ăn liệu", text))
        for old, new in SPECIALS + BASE:
            text = text.replace(old, new)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        after = len(re.findall(r"[Vv]ăn liệu", text))
        print(f"{path}: before={before} after={after}")

if __name__ == "__main__":
    main()
