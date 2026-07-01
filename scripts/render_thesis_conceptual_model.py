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


def tier_band(ax, y0, y1, label):
    """Dải tầng bên trái: nhãn dọc + ngoặc vuông nhẹ để gom đúng tầng."""
    xb = 0.62
    ax.plot([xb, xb], [y0, y1], color="black", linewidth=0.8)
    ax.plot([xb, xb + 0.12], [y0, y0], color="black", linewidth=0.8)
    ax.plot([xb, xb + 0.12], [y1, y1], color="black", linewidth=0.8)
    ax.text(0.34, (y0 + y1) / 2, label, ha="center", va="center",
            fontsize=LB - 1, fontweight="bold", rotation=90)


def main():
    out = Path(__file__).resolve().parent.parent / "thesis" / "figures" / "fig_2_1_cdcm_conceptual_model.png"
    fig, ax = plt.subplots(figsize=(12, 9.2), dpi=DPI)
    ax.set_xlim(0, 12); ax.set_ylim(0, 9.2)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.text(6.0, 8.95, "Khung khái niệm tích hợp đa tầng CDCM",
            ha="center", va="center", fontsize=TT, fontweight="bold")
    ax.text(6.0, 8.58,
            "(Country–Digital–Capability Moderation): điều tiết thể chế – số – năng lực",
            ha="center", va="center", fontsize=LB, fontstyle="italic")

    # Dải ba tầng (bên trái) — gom ĐÚNG tầng: TCI và DAI cùng tầng doanh nghiệp
    tier_band(ax, 7.10, 8.15, "TẦNG\nQUỐC GIA")
    tier_band(ax, 3.85, 6.60, "TẦNG DOANH NGHIỆP")
    tier_band(ax, 1.40, 2.55, "TẦNG\nCÁ NHÂN")

    YM = 4.40
    # Trục quan hệ chính: biến độc lập → nút H1 → biến phụ thuộc
    box(ax, 2.05, YM, 2.6, 1.0, "QUỐC TẾ HÓA\n(FSTS, FSTS²)", bold=True)
    box(ax, 5.95, YM, 2.9, 0.95, "H1: quan hệ chữ U ngược\n(β₁ > 0; β₂ < 0)", bold=True, fs=10.5)
    box(ax, 9.95, YM, 2.7, 1.1, "HIỆU QUẢ\nDOANH NGHIỆP\n(năng suất lao động)",
        bold=True, fs=10.5)
    arrow(ax, (3.35, YM), (4.45, YM))
    arrow(ax, (7.45, YM), (8.55, YM))
    ax.text(5.95, YM - 0.74, "điểm uốn  TP* = −β₁ / (2·β₂)",
            ha="center", va="center", fontsize=LB - 0.5, fontstyle="italic", bbox=WBB)

    # Cạnh hộp H1
    TOPC = (5.95, YM + 0.475)
    TL, TR = (5.35, YM + 0.475), (6.55, YM + 0.475)
    BOTC = (5.95, YM - 0.475)

    # Tầng quốc gia: ICRV (H5) — trên cùng, đâm vào đỉnh hộp H1
    ellipse(ax, 5.95, 7.62, 3.4, 1.05, "Bối cảnh thể chế\nKhung ICRV (6 nhóm)")
    mod_arrow(ax, (5.95, 7.09), TOPC, "H5 (±)", (5.95, 5.62))

    # Tầng doanh nghiệp: NĂNG LỰC CÔNG NGHỆ (TCI, H2) và CHẤP NHẬN SỐ (DAI, H3)
    # — cùng tầng tổ chức, đặt ngay trên trục quan hệ
    ellipse(ax, 3.35, 6.05, 2.7, 0.95, "Năng lực công nghệ\n(TCI)")
    mod_arrow(ax, (4.20, 5.62), TL, "H2 (+)", (4.62, 5.08))
    ellipse(ax, 8.55, 6.05, 2.7, 0.95, "Chấp nhận số\n(DAI)")
    mod_arrow(ax, (7.70, 5.62), TR, "H3 (+)", (7.28, 5.08))

    # Tầng cá nhân: ĐẶC ĐIỂM NHÀ QUẢN TRỊ (H4) — dưới, đâm vào đáy hộp H1
    ellipse(ax, 5.95, 1.95, 3.5, 1.0, "Đặc điểm nhà quản trị\n(kinh nghiệm, giới tính)")
    mod_arrow(ax, (5.95, 2.45), BOTC, "H4 (+)", (6.55, 3.15))

    # Điều kiện biên FIP (H1b) — góc phải, điều kiện hoá quan hệ H1 tại SIDS
    box(ax, 9.95, 1.95, 3.0, 1.15,
        "Điều kiện biên (H1b)\nFIP tại SIDS:\nâm đơn điệu, không điểm uốn",
        italic=True, fs=9.0)
    arrow(ax, (9.95, 2.53), (7.42, YM - 0.30), dashed=True, curve=-0.18)

    # Biến kiểm soát
    box(ax, 6.0, 0.60, 9.8, 0.55,
        "Biến kiểm soát:  quy mô (log lao động),  tuổi doanh nghiệp,  "
        "sở hữu nước ngoài,  ngành (FE),  năm (FE)",
        italic=True, fs=9.0)
    arrow(ax, (3.6, 0.88), (4.55, YM - 0.40), dashed=True, curve=0.14)

    ax.text(6.0, 0.06,
            "Ghi chú: mũi tên liền = tác động trực tiếp; mũi tên đứt + dấu × = tác động "
            "điều tiết; mũi tên đứt = biến kiểm soát. TCI và DAI cùng thuộc tầng doanh "
            "nghiệp. Dấu kỳ vọng và mô tả chi tiết từng giả thuyết (gồm H6 dị biệt thời "
            "gian) xem Bảng 2.2. Nguồn: tác giả xây dựng.",
            ha="center", va="bottom", fontsize=LB - 1.5, fontstyle="italic")

    plt.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
