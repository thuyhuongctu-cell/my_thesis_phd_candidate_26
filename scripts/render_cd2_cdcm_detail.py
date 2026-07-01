"""Vẽ lại Hình 2.2 của Chuyên đề 2 — Cơ chế CDCM của chấp nhận số (DAI)
theo ba nhóm ICRV đại diện.

Thay hình cũ (lẫn tiếng Anh, nhiều màu, gán nhãn chế độ sai: 'Emerging IV
(China)', 'Frontier V (Vietnam)'). Bản mới: đơn sắc, tiếng Việt, nhãn chế
độ ICRV đúng (Singapore = Nhóm I; Trung Quốc = Nhóm III; Việt Nam = Nhóm IV)
và cơ chế DAI khớp bằng chứng P3/P4/P5.

Chạy:  python3 scripts/render_cd2_cdcm_detail.py
"""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from pathlib import Path

DPI = 300
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["DejaVu Serif"], "font.size": 10,
    "savefig.bbox": "tight", "savefig.facecolor": "white",
    "figure.facecolor": "white", "axes.facecolor": "white",
})


def panel(ax, x, w, header, body):
    # header (nền xám) + thân (trắng)
    ax.add_patch(FancyBboxPatch((x, 4.55), w, 0.95, boxstyle="round,pad=0.04",
                 linewidth=1.2, edgecolor="black", facecolor="0.90"))
    ax.text(x + w / 2, 5.02, header, ha="center", va="center",
            fontsize=10.5, fontweight="bold")
    ax.add_patch(FancyBboxPatch((x, 0.85), w, 3.55, boxstyle="round,pad=0.04",
                 linewidth=1.2, edgecolor="black", facecolor="white"))
    ax.text(x + w / 2, 2.62, body, ha="center", va="center", fontsize=9.3)


def main():
    out = Path(__file__).resolve().parent.parent / "chuyen_de" / "cd2" / "figures" / "hinh_2_2_cdcm_detail.png"
    fig, ax = plt.subplots(figsize=(12, 6), dpi=DPI)
    ax.set_xlim(0, 12); ax.set_ylim(0, 6)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

    ax.text(6.0, 5.78,
            "Cơ chế điều tiết của chấp nhận số (DAI) theo ba nhóm ICRV đại diện",
            ha="center", va="center", fontsize=12.5, fontweight="bold")

    panel(ax, 0.3, 3.6, "Nhóm I — Singapore\n(tiên tiến đổi mới)",
          "Bão hòa số cao.\n\nDAI Tầng 1 + Tầng 2 vận hành\nnhư nguồn lực mở rộng tình huống:\n"
          "khuếch đại quan hệ ở mức cường độ\nxuất khẩu cao.\n\n"
          "Tương tác DAI × FSTS² = +3,119\n(p = 0,005; nghiên cứu P4).")
    panel(ax, 4.2, 3.6, "Nhóm III — Trung Quốc\n(trung bình cao)",
          "Bão hòa số trung bình – cao.\n\nDAI Tầng 1 (website) phổ biến\n> 60%, mất khả năng phân biệt\n"
          "giữa các doanh nghiệp.\n\nGiữ như biến kiểm soát,\nkhông phải biến điều tiết\n(nghiên cứu P5).")
    panel(ax, 8.1, 3.6, "Nhóm IV — Việt Nam\n(chuyển đổi thu nhập\ntrung bình – thấp)",
          "Bão hòa số thấp.\n\nDAI Tầng 1 là ràng buộc đo lường\n(chỉ có website).\n\n"
          "Dương theo OLS nhưng null sau\nhiệu chỉnh nội sinh (β = 0,018);\n"
          "phụ thuộc chọn lựa và giai đoạn\n(nghiên cứu P3).")

    ax.text(6.0, 0.30,
            "Ghi chú: cùng một cấu trúc DAI cho kết quả khác nhau theo chế độ thể chế và mức "
            "bão hòa số — minh họa luận điểm “nguồn lực phụ thuộc bối cảnh” của khung CDCM. "
            "Nguồn: tác giả xây dựng từ bằng chứng P3, P4, P5.",
            ha="center", va="center", fontsize=8.0, fontstyle="italic")

    plt.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.2)
    plt.close(fig)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
