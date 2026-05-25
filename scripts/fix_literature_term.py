#!/usr/bin/env python3
"""One-off: normalize the bare English word "literature" (the body of scholarship)
to natural Vietnamese. Collocation-specific replacements run first; the generic
"trong literature" runs last. The reference title "Writing integrative literature
reviews" (Torraco, 2005) is deliberately left untranslated.
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

# Specific phrases first (longest/overlap-sensitive ordered before shorter).
PAIRS = [
    ("meta-analytic literature về I–P", "các nghiên cứu meta-analysis về quan hệ I–P"),
    ("trong literature internationalization–performance", "trong các nghiên cứu về quan hệ I–P"),
    ("literature internationalization–performance", "các nghiên cứu về quan hệ I–P"),
    ("trong I–P literature", "trong các nghiên cứu I–P"),
    ("I–P literature (Sullivan", "các nghiên cứu I–P (Sullivan"),
    ("literature về digital capability", "các nghiên cứu về năng lực số"),
    ("digital capability literature", "các nghiên cứu về năng lực số"),
    ("literature về internationalization và SIDS", "các nghiên cứu về quốc tế hóa và SIDS"),
    ("literature về firm productivity", "các nghiên cứu về firm productivity"),
    ("literature về I–P", "các nghiên cứu về quan hệ I–P"),
    ("literature về châu Á", "các nghiên cứu về châu Á"),
    ("literature về số hóa và quốc tế hóa", "các nghiên cứu về số hóa và quốc tế hóa"),
    ("literature I–P", "các nghiên cứu I–P"),
    ("literature IB", "các nghiên cứu IB"),
    ("literature kinh doanh quốc tế", "tài liệu nghiên cứu kinh doanh quốc tế"),
    ("literature toàn cầu", "các nghiên cứu toàn cầu"),
    ("literature 1982–2026", "các nghiên cứu giai đoạn 1982–2026"),
    ("tổng hợp literature trong giai đoạn", "tổng hợp các nghiên cứu trong giai đoạn"),
    ("literature gần đây", "các nghiên cứu gần đây"),
    ("literature Lu và Beamish", "các nghiên cứu của Lu và Beamish"),
    ("literature hiện tại", "các nghiên cứu hiện tại"),
    ("phần lớn literature trước", "phần lớn các nghiên cứu trước"),
    ("tổng hợp literature để trả lời RQ1", "tổng hợp các nghiên cứu để trả lời RQ1"),
    # generic last
    ("Trong literature", "Trong các nghiên cứu"),
    ("trong literature", "trong các nghiên cứu"),
]

def main():
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        for old, new in PAIRS:
            text = text.replace(old, new)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        rem = text.count("literature")
        note = " (reference title only)" if rem == 1 and "integrative literature reviews" in text else ""
        print(f"{path}: remaining 'literature'={rem}{note}")

if __name__ == "__main__":
    main()
