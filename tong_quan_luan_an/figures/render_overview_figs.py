#!/usr/bin/env python3
"""render_overview_figs.py — publication PNGs for the dissertation overview package.

Renders two schematics used in tong_quan_luan_an/02_truc_quan_hoa_quan_he.md so the
visualisations are usable in Word/PDF/print (GitHub renders the Mermaid source; this
gives static raster equivalents). Monochrome, journal-style. No external data.

Run:  python3 tong_quan_luan_an/figures/render_overview_figs.py
Out:  tong_quan_luan_an/figures/fig_integration_map.png
      tong_quan_luan_an/figures/fig_three_zone.png
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent
INK = "#1a1a1a"
GREY = "#666666"
LIGHT = "#f2f2f2"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})


def _box(ax, x, y, w, h, text, *, fc="white", ec=INK, fs=8.5, bold=False, lw=1.1):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.02",
        linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fs, color=INK, zorder=3,
            fontweight="bold" if bold else "normal", wrap=True)


def _arrow(ax, p0, p1, *, color=GREY, lw=1.0, style="-|>"):
    ax.add_patch(FancyArrowPatch(
        p0, p1, arrowstyle=style, mutation_scale=11,
        linewidth=lw, color=color, zorder=1,
        connectionstyle="arc3,rad=0.0"))


# ---------------------------------------------------------------- Figure 1
def integration_map():
    fig, ax = plt.subplots(figsize=(11.0, 7.4))
    ax.set_xlim(0, 12); ax.set_ylim(0, 9); ax.axis("off")
    ax.text(6, 8.75, "Bản đồ tích hợp luận án: câu hỏi nghiên cứu → nghiên cứu thành phần "
            "→ khung CDCM → tuyên bố lý thuyết", ha="center", va="center",
            fontsize=11, fontweight="bold", color=INK)

    # Column 1 — RQs
    rqs = [
        ("RQ1\nQuan hệ I–P tồn tại &\nbị thể chế điều tiết?", 7.0),
        ("RQ2\nDạng hàm theo từng\nchế độ đơn quốc gia?", 5.3),
        ("RQ3\nCDCM khái quát hóa &\nnăng lực số/công nghệ?", 3.6),
        ("RQ4\nPhổ thể chế điều tiết\ndạng hàm & điều kiện biên?", 1.9),
    ]
    for t, y in rqs:
        _box(ax, 0.3, y - 0.62, 2.5, 1.24, t, fc=LIGHT, bold=True, fs=8)

    # Column 2 — studies
    studies = {
        "P6 — Meta 3 tầng\nk=238; r̄=0,074; Q_M=17,35": 7.55,
        "P4 Singapore (I) · P3 Việt Nam (IV)\nP5 Trung Quốc (III)": 5.3,
        "P7 — 50 nền\nM2 51,5% / M5 43,6%  ·  P8 SIDS": 3.6,
        "P9 Ấn Độ (điểm uốn tan biến)\nP10 Nhật (biên trên) · Chương sách (H4)": 1.55,
    }
    ys_rq = [r[1] for r in rqs]
    ys_st = list(studies.values())
    for (t, y), yst in zip(studies.items(), ys_st):
        _box(ax, 3.5, y - 0.55, 3.7, 1.1, t, fs=7.6)
    # arrows RQ -> studies (aligned by order)
    for yr, yst in zip(ys_rq, ys_st):
        _arrow(ax, (2.8, yr), (3.5, yst))

    # P1 foundation
    _box(ax, 3.5, 0.15, 3.7, 0.7, "P1 — Nền tảng 17 nền (lá chắn số)", fc=LIGHT, fs=7.6)

    # Column 3 — CDCM core
    _box(ax, 8.0, 3.7, 3.4, 2.2,
         "KHUNG CDCM – ICRV – FIP\n\nHình thái BA VÙNG\n(thể chế điều tiết\nDẤU & DẠNG hàm)",
         fc="#e8e8e8", bold=True, fs=9, lw=1.6)
    for yst in ys_st:
        _arrow(ax, (7.2, yst), (8.0, 4.8), color="#999999")
    _arrow(ax, (7.2, 0.5), (8.0, 3.9), color="#bbbbbb")

    # thesis statement
    _box(ax, 8.0, 0.9, 3.4, 2.2,
         "TUYÊN BỐ LÝ THUYẾT\n\n“Dạng hàm của quan hệ\nI–P là một hàm của\nvị trí thể chế.”",
         fc=LIGHT, bold=True, fs=9, lw=1.3)
    _arrow(ax, (9.7, 3.7), (9.7, 3.1), color=INK, lw=1.4)

    ax.text(6, 0.05, "Nguồn: tác giả tổng hợp · số liệu khớp CANONICAL_NUMBERS.md (khung 50 nền / 88.869 DN).",
            ha="center", va="bottom", fontsize=7, color=GREY, style="italic")
    fig.tight_layout()
    p = OUT / "fig_integration_map.png"
    fig.savefig(p, dpi=200, bbox_inches="tight"); plt.close(fig)
    print(f"  wrote {p.relative_to(OUT.parents[1])}")


# ---------------------------------------------------------------- Figure 2
def three_zone():
    import numpy as np
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    x = np.linspace(0, 1, 200)

    # top zone: near-linear positive
    ax.plot(x, 0.15 + 0.9 * x, color=INK, lw=2.0)
    # middle zone: sharp inverted-U, TP ~0.43
    yU = 0.2 + 2.2 * x - 2.55 * x ** 2
    ax.plot(x, yU, color=INK, lw=2.0, ls="--")
    # bottom zone: monotone negative (dissolution / FIP limiting case)
    ax.plot(x, 0.55 - 0.55 * x, color=INK, lw=2.0, ls=":")

    ax.axvline(0.43, color=GREY, lw=0.8, ls="-")
    ax.text(0.43, -0.06, "điểm uốn ≈ 43%\n(Nhóm IV)", ha="center", va="top", fontsize=8, color=GREY)

    ax.text(0.86, 1.0, "BIÊN TRÊN (I–II)\ngần tuyến tính dương\nP4, P10", fontsize=8.5, color=INK)
    ax.text(0.30, 0.86, "VÙNG GIỮA (III–IV)\nchữ U ngược sắc nét\nP3, P5, P7-M5, P9", fontsize=8.5, color=INK)
    ax.text(0.62, 0.10, "BIÊN DƯỚI (V–VI)\nmất cấu trúc / FIP\nP8 (giới hạn)", fontsize=8.5, color=INK)

    ax.set_xlabel("Cường độ quốc tế hóa (FSTS)", fontsize=9.5)
    ax.set_ylabel("Hiệu quả doanh nghiệp (năng suất chuẩn hóa)", fontsize=9.5)
    ax.set_title("Hình thái BA VÙNG của quan hệ quốc tế hóa–hiệu quả theo phổ thể chế ICRV",
                 fontsize=10.5, fontweight="bold")
    ax.set_xlim(0, 1); ax.set_ylim(-0.05, 1.25)
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_yticks([])
    fig.tight_layout()
    p = OUT / "fig_three_zone.png"
    fig.savefig(p, dpi=200, bbox_inches="tight"); plt.close(fig)
    print(f"  wrote {p.relative_to(OUT.parents[1])}")


if __name__ == "__main__":
    integration_map()
    three_zone()
    print("done.")
