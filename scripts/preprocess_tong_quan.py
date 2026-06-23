#!/usr/bin/env python3
"""preprocess_tong_quan.py — chuẩn bị Markdown gói "Tổng quan luận án" cho bản in.

GitHub hiển thị sơ đồ Mermaid trực tiếp; Word/PDF thì không. Script này:
  1. Gỡ các khối ```mermaid ... ``` (chỉ dùng để xem trên kho lưu trữ).
  2. Đặt 2 ảnh tĩnh PNG (đã commit) làm HÌNH có chú thích đúng mục:
       - Mục 2.1 (sơ đồ tích hợp)  -> figures/fig_integration_map.png
       - Mục 2.3 (hình thái ba vùng) -> figures/fig_three_zone.png
     Mục 2.2 (ánh xạ nghiên cứu↔chương) không có ảnh tĩnh -> chèn ghi chú nguồn.
  3. Gộp 4 tài liệu theo thứ tự, chèn ngắt trang giữa các phần.

Xuất Markdown đã hợp nhất ra stdout (build script đẩy vào pandoc).
"""
from __future__ import annotations

import sys
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent / "tong_quan_luan_an"

FILES = [
    "01_gioi_thieu_chung_du_an.md",
    "02_truc_quan_hoa_quan_he.md",
    "03_dong_gop_va_tinh_moi.md",
    "04_vi_tri_trong_literature.md",
]

# Ảnh tĩnh thay cho sơ đồ Mermaid, khóa theo tiền tố mục.
FIGURES = {
    "2.1": (
        "tong_quan_luan_an/figures/fig_integration_map.png",
        "**Hình 2.1.** Bản đồ tích hợp: câu hỏi nghiên cứu → nghiên cứu thành "
        "phần → khung CDCM → tuyên bố lý thuyết trung tâm.",
    ),
    "2.2": (
        "tong_quan_luan_an/figures/fig_study_chapter_map.png",
        "**Hình 2.2.** Ánh xạ nghiên cứu thành phần · chuyên đề → chương luận án "
        "(trục xương sống Ch.1→Ch.5 là mạch lập luận; cung xiên là đầu vào nội dung).",
    ),
    "2.3": (
        "tong_quan_luan_an/figures/fig_three_zone.png",
        "**Hình 2.3.** Hình thái ba vùng của quan hệ quốc tế hóa–hiệu quả theo "
        "phổ thể chế ICRV (biên trên gần tuyến tính · vùng giữa chữ U ngược · "
        "biên dưới mất cấu trúc / FIP).",
    ),
}

# Mục không có ảnh tĩnh -> chèn ghi chú nguồn (hiện đã đủ 3 hình, để rỗng).
SECTION_NOTE: dict[str, str] = {}

PAGE_BREAK = "\n\n\\newpage\n\n"


def current_section(line: str) -> str | None:
    """Trả về tiền tố mục (vd '2.1') nếu dòng là tiêu đề '## 2.1 ...'."""
    s = line.lstrip("#").strip()
    head = s.split(" ", 1)[0]
    return head if head[:1].isdigit() and "." in head else None


def strip_and_place(text: str) -> str:
    """Gỡ khối mermaid; thay bằng hình/ghi chú theo mục hiện tại."""
    out: list[str] = []
    lines = text.splitlines()
    i = 0
    section: str | None = None
    while i < len(lines):
        line = lines[i]
        sec = current_section(line)
        if sec:
            section = sec

        # Gỡ 2 dòng ảnh tĩnh nằm trong blockquote đầu file (đặt lại đúng mục).
        if line.lstrip().startswith(">") and "figures/fig_" in line:
            i += 1
            continue
        if line.lstrip().startswith(">") and "Phiên bản ảnh tĩnh" in line:
            i += 1
            continue

        if line.strip().startswith("```mermaid"):
            # nuốt tới khi đóng khối ```
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                i += 1
            i += 1  # bỏ dòng đóng

            fig = FIGURES.get(section or "")
            if fig:
                path, caption = fig
                out.append("")
                out.append(f"![{caption}]({path}){{width=85%}}")
                out.append("")
            elif section in SECTION_NOTE:
                out.append("")
                out.append(SECTION_NOTE[section])
                out.append("")
            continue

        out.append(line)
        i += 1
    return "\n".join(out)


def main() -> int:
    title_block = (
        "% Tổng quan luận án — gói tài liệu định hướng\n"
        "% NCS Đỗ Thùy Hương · GVHD: PGS.TS. Phan Anh Tú\n"
        "% 2026-06-23\n\n"
    )
    parts = [title_block]
    for idx, name in enumerate(FILES):
        raw = (PKG / name).read_text(encoding="utf-8")
        parts.append(strip_and_place(raw))
        if idx < len(FILES) - 1:
            parts.append(PAGE_BREAK)
    sys.stdout.write("\n".join(parts) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
