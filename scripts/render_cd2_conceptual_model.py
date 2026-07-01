"""Vẽ lại Hình 2.1 của Chuyên đề 2 — Khung khái niệm tích hợp CDCM.

Thay hình cũ (lẫn tiếng Anh, nhiều màu, số liệu cũ 101.185/47). Bản mới: đơn
sắc, tiếng Việt, số liệu đã khóa (88.869 doanh nghiệp / 50 nền), bố cục nút
quan hệ H1 ở giữa giống Hình 2.1 của luận án, gắn năm tầng lý thuyết.

Chạy:  python3 scripts/render_cd2_conceptual_model.py
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
from pathlib import Path

FS = 11
LB = 9.5
TT = 13
EDGE = 1.2
AW = 1.1
DPI = 300
WBB = dict(boxstyle="square,pad=0.12", fc="white", ec="none")

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["DejaVu Serif"], "font.size": FS,
    "savefig.bbox": "tight", "savefig.facecolor": "white",
    "figure.facecolor": "white", "axes.facecolor": "white",
})


def box(ax, x, y, w, h, text, *, bold=False, italic=False, fs=None):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                 boxstyle="round,pad=0.06", linewidth=EDGE,
                 edgecolor="black", facecolor="white"))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs or FS,
            fontweight="bold" if bold else "normal",
            fontstyle="italic" if italic else "normal")


def ellipse(ax, x, y, w, h, text, *, fs=None):
    ax.add_patch(Ellipse((x, y), w, h, linewidth=EDGE,
                 edgecolor="black", facecolor="white"))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs or FS)


def arrow(ax, start, end, *, dashed=False, curve=0.0):
    ax.add_patch(FancyArrowPatch(start, end,
                 arrowstyle="->,head_width=4,head_length=7", linewidth=AW,
                 color="black", linestyle="--" if dashed else "-",
                 connectionstyle=f"arc3,rad={curve}", shrinkA=2, shrinkB=4))


def mod_arrow(ax, start, target, label, lxy):
    ax.add_patch(FancyArrowPatch(start, target,
                 arrowstyle="->,head_width=4,head_length=7", linewidth=AW,
                 color="black", linestyle="--", shrinkA=2, shrinkB=7))
    ax.plot(target[0], target[1], marker="x", color="black",
            markersize=9, markeredgewidth=1.6)
    ax.text(lxy[0], lxy[1], label, ha="center", va="center",
            fontsize=LB, fontstyle="italic", bbox=WBB)


def main():
    out = Path(__file__).resolve().parent.parent / "chuyen_de" / "cd2" / "figures" / "hinh_2_1_khung_khai_niem.png"
    fig, ax = plt.subplots(figsize=(12, 8.6), dpi=DPI)
    ax.set_xlim(0, 12); ax.set_ylim(0, 8.6)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.text(6.0, 8.30, "Khung khái niệm tích hợp Chuyên đề 2 (CDCM)",
            ha="center", va="center", fontsize=TT, fontweight="bold")
    ax.text(6.0, 7.96,
            "Mẫu gộp 88.869 doanh nghiệp · 50 nền kinh tế châu Á – Thái Bình Dương",
            ha="center", va="center", fontsize=LB, fontstyle="italic")

    # Chú giải năm tầng lý thuyết (góc trên trái)
    ax.text(0.15, 7.25,
            "Năm tầng lý thuyết: mô hình Uppsala (H1) · lý thuyết dựa trên nguồn lực (H2) · "
            "lăng kính năng lực số (H3) · lý thuyết thượng tầng quản trị (H4) · lý thuyết thể chế (H5)",
            ha="left", va="center", fontsize=LB - 1.5, fontstyle="italic")

    for ty, lab in [(6.45, "TẦNG QUỐC GIA"),
                    (4.35, "TẦNG DOANH NGHIỆP"),
                    (2.25, "TẦNG CÁ NHÂN")]:
        ax.text(0.18, ty, lab, ha="center", va="center", fontsize=LB - 1,
                fontweight="bold", rotation=90)

    YM = 4.35
    box(ax, 2.05, YM, 2.6, 1.0, "QUỐC TẾ HÓA (I)\n(FSTS, FSTS²)", bold=True)
    box(ax, 5.95, YM, 2.9, 0.95, "H1: quan hệ chữ U ngược\n(β₁ > 0; β₂ < 0)", bold=True, fs=10.5)
    box(ax, 9.95, YM, 2.7, 1.1, "HIỆU QUẢ (P)\n(năng suất lao động)", bold=True, fs=10.5)
    arrow(ax, (3.35, YM), (4.45, YM))
    arrow(ax, (7.45, YM), (8.55, YM))
    ax.text(5.95, YM - 0.78, "điểm uốn  TP* = −β₁ / (2·β₂)",
            ha="center", va="center", fontsize=LB - 0.5, fontstyle="italic", bbox=WBB)

    TL, TR = (5.10, YM + 0.475), (6.80, YM + 0.475)
    BL, BR = (5.10, YM - 0.475), (6.80, YM - 0.475)

    ellipse(ax, 4.55, 6.55, 3.1, 1.0, "Bối cảnh thể chế\nKhung ICRV (6 nhóm)")
    mod_arrow(ax, (4.85, 6.05), TL, "H5 (±)", (4.55, 5.42))
    ellipse(ax, 7.45, 6.55, 2.9, 1.0, "Năng lực công nghệ\n(TCI)")
    mod_arrow(ax, (7.15, 6.05), TR, "H2 (+)", (7.45, 5.42))
    ellipse(ax, 4.55, 2.20, 2.9, 1.0, "Chấp nhận số (DAI)\nTầng 1 + Tầng 2")
    mod_arrow(ax, (4.85, 2.70), BL, "H3 (theo chế độ)", (4.62, 3.38))
    ellipse(ax, 7.45, 2.20, 3.1, 1.0, "Đặc điểm nhà quản trị\n(kinh nghiệm, học vấn, giới tính)", fs=10)
    mod_arrow(ax, (7.15, 2.70), BR, "H4 (±)", (7.45, 3.38))

    box(ax, 6.0, 0.55, 9.8, 0.55,
        "Biến kiểm soát:  quy mô (log lao động),  tuổi doanh nghiệp,  "
        "sở hữu nước ngoài,  ngành (FE),  nền kinh tế (FE),  năm (FE)",
        italic=True, fs=9.0)
    arrow(ax, (8.7, 0.83), (9.3, YM - 0.58), dashed=True, curve=-0.12)

    ax.text(6.0, 0.05,
            "Ghi chú: mũi tên liền = tác động trực tiếp; mũi tên đứt + dấu × = tác động "
            "điều tiết; mũi tên đứt = biến kiểm soát. H3 phụ thuộc chế độ thể chế (H3a/H3b); "
            "H6 kiểm định dị biệt thời gian (xem Bảng 2.5). Nguồn: tác giả xây dựng.",
            ha="center", va="bottom", fontsize=LB - 1.5, fontstyle="italic")

    plt.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
