"""Vẽ Hình 2.1 — Khung khái niệm tích hợp đa tầng CDCM của luận án.

Chuẩn trình bày sơ đồ khái niệm Scopus/WoS, đơn sắc (đen–trắng):
- Biến độc lập (quốc tế hóa) bên trái, biến phụ thuộc (hiệu quả) bên phải,
  một quan hệ chính nằm ngang (H1, chữ U ngược).
- Ba tầng biến điều tiết: tầng quốc gia (thể chế, H5), tầng doanh nghiệp
  (năng lực công nghệ TCI – H2, và chấp nhận số DAI – H3), tầng cá nhân
  (đặc điểm nhà quản trị, H4). Mũi tên điều tiết hướng vào đường quan hệ
  chính, có dấu nhân (×) theo quy ước Baron–Kenny.
- Điều kiện biên FIP tại SIDS (H1b) đặt cạnh biến phụ thuộc.
- Biến kiểm soát ở hộp dưới cùng, mũi tên đứt nét.
- Toàn bộ tiếng Việt; chỉ giữ ký hiệu biến (FSTS, TCI, DAI, ICRV...).

Chạy từ thư mục gốc:
    python3 scripts/render_thesis_conceptual_model.py
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
from pathlib import Path

FS = 11          # cỡ chữ trong hộp
LB = 9.0         # cỡ nhãn mũi tên
TT = 13          # cỡ tiêu đề
EDGE = 1.2
AW = 1.1
DPI = 300

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],   # có đủ glyph tiếng Việt
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


def ellipse(ax, x, y, w, h, text, *, italic=True, fs=None):
    ax.add_patch(Ellipse((x, y), w, h, linewidth=EDGE,
                         edgecolor="black", facecolor="white"))
    ax.text(x, y, text, ha="center", va="center",
            fontsize=fs or FS, fontstyle="italic" if italic else "normal")


def arrow(ax, start, end, *, dashed=False, curve=0.0):
    ax.add_patch(FancyArrowPatch(
        start, end, arrowstyle="->,head_width=4,head_length=7",
        linewidth=AW, color="black",
        linestyle="--" if dashed else "-",
        connectionstyle=f"arc3,rad={curve}", shrinkA=2, shrinkB=4))


def mod_arrow(ax, start, target, label, *, lside="right"):
    """Mũi tên điều tiết (đứt nét) đâm vào đường quan hệ chính, dấu × tại đích."""
    ax.add_patch(FancyArrowPatch(
        start, target, arrowstyle="->,head_width=4,head_length=7",
        linewidth=AW, color="black", linestyle="--",
        shrinkA=2, shrinkB=8))
    ax.plot(target[0], target[1], marker="x", color="black",
            markersize=9, markeredgewidth=1.6)
    tt = 0.30
    mx = start[0] + (target[0] - start[0]) * tt
    my = start[1] + (target[1] - start[1]) * tt
    dx = 0.18 if lside == "right" else -0.18
    ax.text(mx + dx, my, label, ha="left" if lside == "right" else "right",
            va="center", fontsize=LB, fontstyle="italic")


def main():
    out = Path(__file__).resolve().parent.parent / "thesis" / "figures" / "fig_2_1_cdcm_conceptual_model.png"
    fig, ax = plt.subplots(figsize=(11.5, 8.2), dpi=DPI)
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 8.2)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.text(5.75, 7.95, "Khung khái niệm tích hợp đa tầng CDCM",
            ha="center", va="center", fontsize=TT, fontweight="bold")
    ax.text(5.75, 7.62,
            "(Country–Digital–Capability Moderation): điều tiết thể chế – số – năng lực",
            ha="center", va="center", fontsize=LB, fontstyle="italic")

    # Nhãn ba tầng (bên trái)
    for ty, lab in [(6.55, "TẦNG QUỐC GIA"),
                    (4.30, "TẦNG DOANH NGHIỆP"),
                    (1.75, "TẦNG CÁ NHÂN")]:
        ax.text(0.15, ty, lab, ha="left", va="center", fontsize=LB - 0.5,
                fontweight="bold", rotation=90)

    # Quan hệ chính: IV -> DV (y = 4.5)
    YM = 4.50
    box(ax, 2.15, YM, 2.5, 1.0, "QUỐC TẾ HÓA\n(FSTS, FSTS²)", bold=True)
    box(ax, 9.30, YM, 2.7, 1.0, "HIỆU QUẢ\nDOANH NGHIỆP\n(năng suất lao động)",
        bold=True, fs=10.5)
    arrow(ax, (3.42, YM), (7.92, YM))
    ax.text(5.67, YM + 0.30,
            "H1: quan hệ phi tuyến chữ U ngược (β₁ > 0, β₂ < 0)",
            ha="center", va="bottom", fontsize=LB, fontstyle="italic")
    ax.text(5.67, YM - 0.32, "điểm uốn  TP* = −β₁ / (2·β₂)",
            ha="center", va="top", fontsize=LB, fontstyle="italic")

    # Tầng quốc gia: ICRV (H5) — trên
    ellipse(ax, 4.55, 6.55, 3.0, 0.95,
            "Bối cảnh thể chế\nKhung ICRV (6 nhóm)")
    mod_arrow(ax, (4.55, 6.05), (4.55, YM + 0.06),
              "H5 (+/−)\ntheo gradient", lside="left")

    # Tầng doanh nghiệp: TCI (H2) — trên phải
    ellipse(ax, 7.05, 6.55, 2.9, 0.95,
            "Năng lực công nghệ\n(TCI)")
    mod_arrow(ax, (7.05, 6.05), (7.05, YM + 0.06),
              "H2 (+)\nnâng mặt bằng", lside="right")

    # Tầng doanh nghiệp: DAI (H3) — dưới trái
    ellipse(ax, 4.55, 2.45, 2.9, 0.95,
            "Chấp nhận số\n(DAI)")
    mod_arrow(ax, (4.55, 2.95), (4.55, YM - 0.06),
              "H3 (+)\nuốn đường cong", lside="left")

    # Tầng cá nhân: nhà quản trị (H4) — dưới phải
    ellipse(ax, 7.05, 2.45, 3.0, 0.95,
            "Đặc điểm nhà quản trị\n(kinh nghiệm, giới tính)")
    mod_arrow(ax, (7.05, 2.95), (7.05, YM - 0.06),
              "H4 (+)", lside="right")

    # Điều kiện biên FIP (H1b) tại SIDS — cạnh DV
    box(ax, 9.30, 2.30, 2.9, 1.15,
        "Điều kiện biên (H1b)\nFIP tại SIDS:\nâm đơn điệu, không điểm uốn",
        italic=True, fs=9.0)
    arrow(ax, (9.30, 2.88), (9.30, YM - 0.50), dashed=True)

    # Biến kiểm soát
    box(ax, 5.75, 0.55, 9.4, 0.55,
        "Biến kiểm soát:  quy mô (log lao động),  tuổi doanh nghiệp,  "
        "sở hữu nước ngoài,  ngành (FE),  năm (FE)",
        italic=True, fs=9.0)
    arrow(ax, (9.30, 0.83), (9.30, YM - 0.52), dashed=True, curve=-0.12)

    ax.text(5.75, 0.04,
            "Ghi chú: mũi tên liền = tác động trực tiếp; mũi tên đứt + dấu × = "
            "tác động điều tiết; mũi tên đứt = biến kiểm soát. "
            "H6 kiểm định dị biệt thời gian của dạng hàm (không thể hiện trên sơ đồ tĩnh). "
            "Nguồn: tác giả xây dựng.",
            ha="center", va="bottom", fontsize=LB - 1, fontstyle="italic")

    plt.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
