"""Vẽ lại Hình khung phân tích mô tả của Chuyên đề 1 (cd1_fig_conceptual_model).

Thay hình cũ (nhiều màu, vài chữ Anh: pool, level-shifter, Tier-1, GVC,
z-score). Bản mới: đơn sắc, tiếng Việt. Đây là khung MÔ TẢ tương quan (không
phải kiểm định giả thuyết): bốn yếu tố cấp doanh nghiệp/quốc gia tương quan
với năng suất lao động chuẩn hóa, được bối cảnh thể chế ICRV điều tiết.

Chạy:  python3 scripts/render_cd1_conceptual_model.py
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

FS = 10.5
LB = 9.0
TT = 12.5
EDGE = 1.2
AW = 1.0
DPI = 300
WBB = dict(boxstyle="square,pad=0.12", fc="white", ec="none")

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["DejaVu Serif"], "font.size": FS,
    "savefig.bbox": "tight", "savefig.facecolor": "white",
    "figure.facecolor": "white", "axes.facecolor": "white",
})


def box(ax, x, y, w, h, text, *, bold=False, italic=False, fs=None, shaded=False):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                 boxstyle="round,pad=0.05", linewidth=EDGE, edgecolor="black",
                 facecolor="0.92" if shaded else "white"))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs or FS,
            fontweight="bold" if bold else "normal",
            fontstyle="italic" if italic else "normal")


def arrow(ax, start, end, *, dashed=False, curve=0.0):
    ax.add_patch(FancyArrowPatch(start, end,
                 arrowstyle="->,head_width=4,head_length=7", linewidth=AW,
                 color="black", linestyle="--" if dashed else "-",
                 connectionstyle=f"arc3,rad={curve}", shrinkA=2, shrinkB=4))


def main():
    out = Path(__file__).resolve().parent.parent / "chuyen_de" / "cd1" / "figures" / "cd1_fig_conceptual_model.png"
    fig, ax = plt.subplots(figsize=(11.5, 8.2), dpi=DPI)
    ax.set_xlim(0, 11.5); ax.set_ylim(0, 8.2)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.text(5.75, 7.95,
            "Khung phân tích mô tả Chuyên đề 1 — tương quan bốn yếu tố với năng suất lao động",
            ha="center", va="center", fontsize=TT, fontweight="bold")
    ax.text(5.75, 7.60,
            "theo bối cảnh thể chế ICRV · mẫu mô tả 88.869 doanh nghiệp · 50 nền kinh tế · 2006–2026",
            ha="center", va="center", fontsize=LB, fontstyle="italic")

    # Biến điều tiết bối cảnh (trên)
    box(ax, 5.75, 6.70, 7.4, 0.8,
        "Bối cảnh thể chế — 6 nhóm ICRV (I Đổi mới → VI SIDS):\n"
        "điều tiết độ lớn và (cá biệt) dấu của các tương quan",
        bold=True, fs=9.5, shaded=True)

    # Biến phụ thuộc (phải)
    DVx, DVy = 9.45, 4.05
    box(ax, DVx, DVy, 2.9, 1.5,
        "Năng suất lao động\n(chuẩn hóa z)\nln(doanh thu / lao động)\n"
        "trong từng nền × năm\n(bất biến tiền tệ)", bold=True, fs=9.5)

    # Bốn yếu tố giải thích (trái)
    factors = [
        (5.55, "FDI ≥ 10%\n(b2b)", "r = +0,06 … +0,12"),
        (4.55, "Quốc tế hóa — FSTS\n(d3b + d3c)", "r = +0,139 → −0,009 (SIDS)"),
        (3.55, "Năng lực công nghệ — TCI\n(R&D h8 · ISO b8)", "r = +0,117 … +0,240"),
        (2.55, "Chấp nhận số — DAI\n(website c22b)", "r = +0,090 … +0,201"),
    ]
    for y, label, rng in factors:
        box(ax, 2.0, y, 2.7, 0.8, label, bold=True, fs=9.0)
        arrow(ax, (3.35, y), (7.95, DVy + (y - 4.05) * 0.18))
        ax.text(4.05, y + 0.34, rng, ha="left", va="center",
                fontsize=LB - 1, fontstyle="italic", bbox=WBB)

    # Mũi tên điều tiết bối cảnh
    arrow(ax, (5.75, 6.30), (5.75, 4.55), dashed=True)
    ax.text(5.95, 5.45, "điều tiết bối cảnh\n(gradient thể chế)", ha="left", va="center",
            fontsize=LB - 0.5, fontstyle="italic", bbox=WBB)

    # Phát hiện mô tả
    box(ax, 5.75, 1.35, 10.6, 0.95,
        "Phát hiện mô tả: (i) năng lực công nghệ (TCI) là tương quan dương mạnh và đồng đều nhất "
        "(nâng mặt bằng phổ quát); (ii) gradient quốc tế hóa (FSTS) giảm đơn điệu khi thể chế yếu dần, "
        "mất ý nghĩa hoặc đổi dấu\nở nhóm đảo nhỏ (gánh nặng quốc tế hóa bắt buộc); "
        "(iii) phần bù của chấp nhận số (DAI) thấp nhất ở Nhóm I do bão hòa Tầng 1.",
        italic=True, fs=8.6)

    # Chiều thời gian
    box(ax, 5.75, 0.42, 10.6, 0.62,
        "Chiều thời gian 2006–2026: nhảy vọt số Tầng 1 (+21…+31 điểm phần trăm website ở nhóm IV/V/VI) "
        "và tái cân bằng chuỗi giá trị toàn cầu\n(mô tả lát cắt ngang gộp nhiều đợt; quan hệ nhân quả dành cho Chuyên đề 2).",
        italic=True, fs=8.6, shaded=True)

    plt.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
