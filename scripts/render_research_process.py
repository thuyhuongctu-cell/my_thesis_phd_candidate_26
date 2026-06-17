"""Vẽ sơ đồ quy trình nghiên cứu (Hình 3.1) và sơ đồ thiết kế hỗn hợp.

Đơn sắc, tiếng Việt, chuẩn trình bày sơ đồ học thuật. Thể hiện quy trình
sáu bước và thiết kế hỗn hợp tổng hợp–thực nghiệm hai giai đoạn (đối thoại
hai chiều) của luận án.

Chạy:  python3 scripts/render_research_process.py
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

FS = 10.5
LB = 9.0
TT = 13
EDGE = 1.2
AW = 1.1
DPI = 300

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "font.size": FS,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def box(ax, x, y, w, h, text, *, bold=False, italic=False, fs=None, shaded=False):
    ax.add_patch(FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.06", linewidth=EDGE,
        edgecolor="black", facecolor="0.92" if shaded else "white"))
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fs or FS,
            fontweight="bold" if bold else "normal",
            fontstyle="italic" if italic else "normal")


def arrow(ax, start, end, *, dashed=False, curve=0.0, double=False):
    style = "<|-|>" if double else "-|>"
    a = FancyArrowPatch(
        start, end, arrowstyle=f"{style},head_width=3.5,head_length=7",
        linewidth=AW, color="black",
        linestyle="--" if dashed else "-",
        connectionstyle=f"arc3,rad={curve}", shrinkA=3, shrinkB=3)
    ax.add_patch(a)


def main():
    out = Path(__file__).resolve().parent.parent / "thesis" / "figures" / "fig_3_1_research_process.png"
    fig, ax = plt.subplots(figsize=(9.5, 11), dpi=DPI)
    ax.set_xlim(0, 9.5); ax.set_ylim(0, 11)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.text(4.75, 10.7, "Quy trình nghiên cứu của luận án",
            ha="center", va="center", fontsize=TT, fontweight="bold")

    # Bước 1, 2 (toàn chiều rộng)
    box(ax, 4.75, 9.9, 8.4, 0.85,
        "Bước 1.  Xác định khoảng trống nghiên cứu\n"
        "(tổng quan văn liệu + các phân tích tổng hợp trước)", bold=True, fs=10)
    box(ax, 4.75, 8.6, 8.4, 0.85,
        "Bước 2.  Xây dựng khung lý thuyết tích hợp đa tầng (CDCM)\n"
        "và hệ giả thuyết H1–H6", bold=True, fs=10)
    arrow(ax, (4.75, 9.47), (4.75, 9.03))
    arrow(ax, (4.75, 8.17), (4.75, 7.55))

    # Hai nhánh giai đoạn
    box(ax, 2.65, 7.15, 3.9, 0.8,
        "GIAI ĐOẠN 1 (RQ1)\nPhân tích tổng hợp", bold=True, fs=10, shaded=True)
    box(ax, 6.85, 7.15, 3.9, 0.8,
        "GIAI ĐOẠN 2 (RQ2–RQ4)\nPhân tích thực nghiệm", bold=True, fs=10, shaded=True)
    # rẽ nhánh từ bước 2
    arrow(ax, (3.6, 8.17), (2.65, 7.58), curve=0.0)
    arrow(ax, (5.9, 8.17), (6.85, 7.58), curve=0.0)

    # Bước 3 (giai đoạn 1)
    box(ax, 2.65, 5.85, 3.9, 1.0,
        "Bước 3.  Phân tích tổng hợp\n1982–2026 theo PRISMA\n"
        "(k = 238 nghiên cứu; K = 288\ncỡ ảnh hưởng)", fs=9)
    arrow(ax, (2.65, 6.72), (2.65, 6.38))
    box(ax, 2.65, 4.5, 3.9, 0.95,
        "Tổng hợp hiệu ứng đa tầng\n(MARA) + điều tiết theo\ngradient ICRV và năng lực số", fs=9)
    arrow(ax, (2.65, 5.32), (2.65, 4.99))

    # Bước 4, 5 (giai đoạn 2)
    box(ax, 6.85, 5.85, 3.9, 1.0,
        "Bước 4.  Thu thập & chuẩn hóa\ndữ liệu WBES 50 nền kinh tế\n"
        "(hòa hợp 3 thế hệ lược đồ:\nPICS3, Standardized, BREADY)", fs=9)
    arrow(ax, (6.85, 6.72), (6.85, 6.38))
    box(ax, 6.85, 4.5, 3.9, 0.95,
        "Bước 5.  Ước lượng mô hình\nthực nghiệm M0–M11\n(đơn quốc gia & đa quốc gia)", fs=9)
    arrow(ax, (6.85, 5.32), (6.85, 4.99))

    # Đối thoại hai chiều giữa hai giai đoạn
    arrow(ax, (4.62, 4.5), (4.88, 4.5), double=True)
    ax.text(4.75, 4.85, "đối thoại\nhai chiều", ha="center", va="center",
            fontsize=LB - 0.5, fontstyle="italic")

    # Bước 6 (hợp nhất)
    box(ax, 4.75, 2.95, 8.4, 0.9,
        "Bước 6.  Kiểm định độ vững và tích hợp kết quả hai giai đoạn",
        bold=True, fs=10)
    arrow(ax, (2.65, 4.02), (4.2, 3.42), curve=0.0)
    arrow(ax, (6.85, 4.02), (5.3, 3.42), curve=0.0)
    arrow(ax, (4.75, 2.5), (4.75, 2.0))

    # Đóng góp
    box(ax, 4.75, 1.55, 8.4, 0.9,
        "Đóng góp lý thuyết (khung CDCM, phân loại ICRV, cấu trúc FIP)\n"
        "và hàm ý chính sách – quản trị theo bối cảnh thể chế",
        bold=True, fs=10, shaded=True)

    ax.text(4.75, 0.45,
            "Ghi chú: mũi tên liền = trình tự thực hiện; mũi tên hai chiều = quan hệ "
            "bổ sung giữa hai giai đoạn\n(phân tích tổng hợp gợi ý biến điều tiết; phân "
            "tích thực nghiệm bổ sung bằng chứng châu Á – Thái Bình Dương). "
            "Nguồn: tác giả xây dựng.",
            ha="center", va="center", fontsize=LB - 1, fontstyle="italic")

    plt.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
