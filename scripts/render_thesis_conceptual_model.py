"""Vẽ Hình 2.1 — Khung khái niệm tích hợp đa tầng CDCM của luận án.

Chuẩn sơ đồ khái niệm Scopus/WoS, đơn sắc, tiếng Việt. Bố cục "nút quan hệ":
quan hệ chính H1 là một hộp ở giữa (biến độc lập → H1 → biến phụ thuộc); bốn
mũi tên điều tiết (3 tầng) đâm vào bốn cạnh của hộp H1 với dấu × tại đích;
nhãn giả thuyết ngắn có nền trắng để không bị mũi tên đè. Mô tả chi tiết
từng giả thuyết nằm ở chú thích hình (trong văn bản) và Bảng 2.2.

Chạy:  python3 scripts/render_thesis_conceptual_model.py
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
WBB = dict(boxstyle="square,pad=0.12", fc="white", ec="none")  # nền trắng che

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "font.size": FS,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})


def box(ax, x, y, w, h, text, *, bold=False, italic=False, fs=None):
    ax.add_patch(FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle="round,pad=0.06", linewidth=EDGE,
        edgecolor="black", facecolor="white"))
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fs or FS,
            fontweight="bold" if bold else "normal",
            fontstyle="italic" if italic else "normal")


def ellipse(ax, x, y, w, h, text, *, fs=None):
    ax.add_patch(Ellipse((x, y), w, h, linewidth=EDGE,
                         edgecolor="black", facecolor="white"))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs or FS)


def arrow(ax, start, end, *, dashed=False, curve=0.0):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle="->,head_width=4,head_length=7",
        linewidth=AW, color="black",
        linestyle="--" if dashed else "-",
        connectionstyle=f"arc3,rad={curve}", shrinkA=2, shrinkB=4))


def mod_arrow(ax, start, target, label, lxy):
    """Mũi tên điều tiết (đứt nét) → cạnh hộp H1, dấu × tại đích; nhãn ngắn có nền trắng."""
    ax.add_patch(FancyArrowPatch(
        start, target, arrowstyle="->,head_width=4,head_length=7",
        linewidth=AW, color="black", linestyle="--", shrinkA=2, shrinkB=7))
    ax.plot(target[0], target[1], marker="x", color="black",
            markersize=9, markeredgewidth=1.6)
    ax.text(lxy[0], lxy[1], label, ha="center", va="center",
            fontsize=LB, fontstyle="italic", bbox=WBB)


def main():
    out = Path(__file__).resolve().parent.parent / "thesis" / "figures" / "fig_2_1_cdcm_conceptual_model.png"
    fig, ax = plt.subplots(figsize=(12, 8.4), dpi=DPI)
    ax.set_xlim(0, 12); ax.set_ylim(0, 8.4)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.text(6.0, 8.10, "Khung khái niệm tích hợp đa tầng CDCM",
            ha="center", va="center", fontsize=TT, fontweight="bold")
    ax.text(6.0, 7.74,
            "(Country–Digital–Capability Moderation): điều tiết thể chế – số – năng lực",
            ha="center", va="center", fontsize=LB, fontstyle="italic")

    # Nhãn ba tầng (bên trái)
    for ty, lab in [(6.65, "TẦNG QUỐC GIA"),
                    (4.50, "TẦNG DOANH NGHIỆP"),
                    (2.35, "TẦNG CÁ NHÂN")]:
        ax.text(0.18, ty, lab, ha="center", va="center", fontsize=LB - 1,
                fontweight="bold", rotation=90)

    YM = 4.50
    # Biến độc lập, nút quan hệ H1, biến phụ thuộc
    box(ax, 2.05, YM, 2.6, 1.0, "QUỐC TẾ HÓA\n(FSTS, FSTS²)", bold=True)
    box(ax, 5.95, YM, 2.9, 0.95, "H1: quan hệ chữ U ngược\n(β₁ > 0; β₂ < 0)", bold=True, fs=10.5)
    box(ax, 9.95, YM, 2.7, 1.1, "HIỆU QUẢ\nDOANH NGHIỆP\n(năng suất lao động)",
        bold=True, fs=10.5)
    arrow(ax, (3.35, YM), (4.45, YM))
    arrow(ax, (7.45, YM), (8.55, YM))
    ax.text(5.95, YM - 0.78, "điểm uốn  TP* = −β₁ / (2·β₂)",
            ha="center", va="center", fontsize=LB - 0.5, fontstyle="italic", bbox=WBB)

    # Toạ độ 4 cạnh hộp H1 (đích mũi tên điều tiết)
    TL, TR = (5.10, YM + 0.475), (6.80, YM + 0.475)
    BL, BR = (5.10, YM - 0.475), (6.80, YM - 0.475)

    # Tầng quốc gia: ICRV (H5)
    ellipse(ax, 4.55, 6.70, 3.1, 1.0, "Bối cảnh thể chế\nKhung ICRV (6 nhóm)")
    mod_arrow(ax, (4.85, 6.20), TL, "H5 (±)", (4.55, 5.55))

    # Tầng doanh nghiệp: TCI (H2)
    ellipse(ax, 7.45, 6.70, 2.9, 1.0, "Năng lực công nghệ\n(TCI)")
    mod_arrow(ax, (7.15, 6.20), TR, "H2 (+)", (7.45, 5.55))

    # Tầng doanh nghiệp: DAI (H3)
    ellipse(ax, 4.55, 2.30, 2.9, 1.0, "Chấp nhận số\n(DAI)")
    mod_arrow(ax, (4.85, 2.80), BL, "H3 (+)", (4.55, 3.45))

    # Tầng cá nhân: nhà quản trị (H4)
    ellipse(ax, 7.45, 2.30, 3.1, 1.0, "Đặc điểm nhà quản trị\n(kinh nghiệm, giới tính)")
    mod_arrow(ax, (7.15, 2.80), BR, "H4 (+)", (7.45, 3.45))

    # Điều kiện biên FIP (H1b)
    box(ax, 9.95, 2.15, 2.9, 1.15,
        "Điều kiện biên (H1b)\nFIP tại SIDS:\nâm đơn điệu, không điểm uốn",
        italic=True, fs=9.0)
    arrow(ax, (9.95, 2.73), (9.95, YM - 0.56), dashed=True)

    # Biến kiểm soát
    box(ax, 6.0, 0.55, 9.7, 0.55,
        "Biến kiểm soát:  quy mô (log lao động),  tuổi doanh nghiệp,  "
        "sở hữu nước ngoài,  ngành (FE),  năm (FE)",
        italic=True, fs=9.0)
    arrow(ax, (8.7, 0.83), (9.3, YM - 0.58), dashed=True, curve=-0.12)

    ax.text(6.0, 0.04,
            "Ghi chú: mũi tên liền = tác động trực tiếp; mũi tên đứt + dấu × = tác động "
            "điều tiết; mũi tên đứt = biến kiểm soát. Dấu kỳ vọng và mô tả chi tiết từng "
            "giả thuyết (gồm H6 dị biệt thời gian) xem Bảng 2.2. Nguồn: tác giả xây dựng.",
            ha="center", va="bottom", fontsize=LB - 1.5, fontstyle="italic")

    plt.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
