"""Vẽ sơ đồ quy trình nghiên cứu (Hình 3.1).

Đơn sắc, tiếng Việt. Quy trình sáu bước + thiết kế hỗn hợp tổng hợp–thực
nghiệm hai giai đoạn (đối thoại hai chiều). Hai cột cách nhau một khe đủ
rộng; nhãn "đối thoại hai chiều" có nền trắng đặt gọn trong khe.

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
WBB = dict(boxstyle="square,pad=0.12", fc="white", ec="none")

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
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle=f"{style},head_width=3.5,head_length=7",
        linewidth=AW, color="black",
        linestyle="--" if dashed else "-",
        connectionstyle=f"arc3,rad={curve}", shrinkA=3, shrinkB=3))


def main():
    out = Path(__file__).resolve().parent.parent / "thesis" / "figures" / "fig_3_1_research_process.png"
    fig, ax = plt.subplots(figsize=(9.8, 11), dpi=DPI)
    ax.set_xlim(0, 9.8); ax.set_ylim(0, 11)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    C = 4.9          # tâm ngang
    LX, RX = 2.45, 7.35   # tâm hai cột
    CW = 3.5         # bề rộng cột
    WIDE = 8.7       # bề rộng hộp toàn chiều

    ax.text(C, 10.7, "Quy trình nghiên cứu của luận án",
            ha="center", va="center", fontsize=TT, fontweight="bold")

    box(ax, C, 9.9, WIDE, 0.8,
        "Bước 1.  Xác định khoảng trống nghiên cứu\n"
        "(tổng quan tài liệu + các phân tích tổng hợp trước)", bold=True, fs=10)
    box(ax, C, 8.6, WIDE, 0.8,
        "Bước 2.  Xây dựng khung lý thuyết tích hợp đa tầng (CDCM)\n"
        "và hệ giả thuyết H1–H6", bold=True, fs=10)
    arrow(ax, (C, 9.50), (C, 9.00))
    arrow(ax, (C, 8.20), (C, 7.58))

    # Hai nhánh giai đoạn
    box(ax, LX, 7.15, CW, 0.8,
        "GIAI ĐOẠN 1 (RQ1)\nPhân tích tổng hợp", bold=True, fs=10, shaded=True)
    box(ax, RX, 7.15, CW, 0.8,
        "GIAI ĐOẠN 2 (RQ2–RQ4)\nPhân tích thực nghiệm", bold=True, fs=10, shaded=True)
    arrow(ax, (C - 1.3, 8.20), (LX + 0.1, 7.57))
    arrow(ax, (C + 1.3, 8.20), (RX - 0.1, 7.57))

    box(ax, LX, 5.85, CW, 1.0,
        "Bước 3.  Phân tích tổng hợp\n1982–2026 theo PRISMA\n"
        "(k = 238 nghiên cứu;\nK = 288 cỡ ảnh hưởng)", fs=9)
    arrow(ax, (LX, 6.72), (LX, 6.37))
    box(ax, LX, 4.5, CW, 0.95,
        "Tổng hợp hiệu ứng đa tầng\n(MARA) + điều tiết theo\n"
        "gradient ICRV và năng lực số", fs=9)
    arrow(ax, (LX, 5.33), (LX, 4.99))

    box(ax, RX, 5.85, CW, 1.0,
        "Bước 4.  Thu thập & chuẩn hóa\ndữ liệu WBES 50 nền kinh tế\n"
        "(hòa hợp 3 thế hệ lược đồ:\nPICS3, Standardized, BREADY)", fs=9)
    arrow(ax, (RX, 6.72), (RX, 6.37))
    box(ax, RX, 4.5, CW, 0.95,
        "Bước 5.  Ước lượng mô hình\nthực nghiệm M0–M11\n"
        "(đơn quốc gia & đa quốc gia)", fs=9)
    arrow(ax, (RX, 5.33), (RX, 4.99))

    # Đối thoại hai chiều trong khe giữa (nhãn nền trắng che mũi tên)
    arrow(ax, (LX + CW / 2, 4.5), (RX - CW / 2, 4.5), double=True)
    ax.text(C, 4.5, "đối thoại\nhai chiều", ha="center", va="center",
            fontsize=LB - 0.5, fontstyle="italic", bbox=WBB)

    # Hợp nhất
    box(ax, C, 2.95, WIDE, 0.9,
        "Bước 6.  Kiểm định độ vững và tích hợp kết quả hai giai đoạn",
        bold=True, fs=10)
    arrow(ax, (LX, 4.02), (C - 1.4, 3.42))
    arrow(ax, (RX, 4.02), (C + 1.4, 3.42))
    arrow(ax, (C, 2.50), (C, 2.02))

    box(ax, C, 1.55, WIDE, 0.9,
        "Đóng góp lý thuyết (khung CDCM, phân loại ICRV, cấu trúc FIP)\n"
        "và hàm ý chính sách – quản trị theo bối cảnh thể chế",
        bold=True, fs=10, shaded=True)

    ax.text(C, 0.45,
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
