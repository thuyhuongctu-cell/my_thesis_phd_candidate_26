"""
Render the dissertation's Hình 4.x — I–P curves by ICRV regime — from the
CANONICAL P7 50-economy results (data_wbes/analysis/p7_50econ_models.csv,
scripts/p7_run_50econ.py; confirmed by verify_all 14/14).

Replaces the previous STATIC (no-generator) thesis/figures/fig_4_x_ip_curves_icrv_gradient.png,
which was stale and WRONG: it showed the institutional gradient reversed
(Nhóm I TP≈28% rising to Frontier≈55%) with obsolete 4-group labels. The
canonical gradient is the opposite and is what the chapter's own Bảng 4.5 reports:
turning point is HIGHEST in the strongest-institution regime and DECLINES toward
weaker regimes — I ≈ 79% → II ≈ 62% → III ≈ 55% → IV ≈ 43% → V ≈ 35%; SIDS (VI)
has no inverted-U (Forced Internationalization Penalty, negative-monotonic).

Each curve is an inverted-U peaking at its canonical raw turning point, with the
canonical group curvature (β₂) controlling steepness; the y-axis is relative
(centered) productivity, so the figure is illustrative of shape/location, not of
absolute level. No values are invented — TPs and β₂ come from the canonical CSV.

Output (3 mirrored copies kept in sync):
  thesis/figures/fig_4_x_ip_curves_icrv_gradient.png
  latex/ctu/figures/fig_4_x_ip_curves_icrv_gradient.png
  dist/luan_an_ctu/source_md/figures/fig_4_x_ip_curves_icrv_gradient.png
"""
import csv
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "data_wbes", "analysis", "p7_50econ_models.csv")
OUT_REL = "figures/fig_4_x_ip_curves_icrv_gradient.png"
OUT_DIRS = ["thesis", "latex/ctu", "dist/luan_an_ctu/source_md"]

plt.rcParams.update({"font.family": "serif",
                     "font.serif": ["DejaVu Serif", "Times New Roman"]})

rows = {}
with open(CSV, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows[r["model"]] = r

# canonical regime key -> (Vietnamese label, line style, grayscale)
regimes = [
    ("Advanced_innovation",  "Nhóm I — Advanced đổi mới",     "solid",   "black"),
    ("Advanced_resource",    "Nhóm II — Advanced tài nguyên", (0, (6, 2)), "#222222"),
    ("Upper_mid",            "Nhóm III — Trung bình cao",     "dashed",  "#444444"),
    ("Lower_mid_transition", "Nhóm IV — Chuyển đổi TB-thấp",  "dashdot", "#666666"),
    ("Emerging",             "Nhóm V — Đang nổi",             "dotted",  "#888888"),
]

fig, ax = plt.subplots(figsize=(9.2, 6))
x = np.linspace(0, 1.0, 300)
PEAK = 0.5
for key, label, ls, col in regimes:
    r = rows[key]
    b2 = float(r["b2"]); tp = float(r["TP_pct"]) / 100.0
    y = b2 * (x - tp) ** 2 + PEAK            # inverted-U peaking at canonical raw TP
    ax.plot(x * 100, y, color=col, lw=2.0, linestyle=ls,
            label=f"{label} (TP≈{float(r['TP_pct']):.0f}%)")
    ax.axvline(float(r["TP_pct"]), color=col, ls=":", lw=0.6, alpha=0.4)

# SIDS (VI) — Forced Internationalization Penalty: negative-monotonic.
# Dissertation SIDS evidence is the dedicated P8 study (β = −1.339, 7 Pacific),
# read from its canonical coefficient file (not P7's tiny SIDS_small subgroup).
FIP_BETA = -1.339   # P8 M1 fsts_c; see p8/replication/reanalysis_7pacific/p8_7pacific_coefs.csv
ax.plot(x * 100, FIP_BETA * x, color="black", lw=2.6,
        label="Nhóm VI — SIDS (FIP, β = −1,339)")
ax.annotate("FIP: âm đơn điệu, không điểm uốn", xy=(60, FIP_BETA * 0.62),
            fontsize=8, style="italic", color="#333333")

ax.axhline(0, color="#cccccc", lw=0.8)
ax.set_xlim(0, 100); ax.set_ylim(-1.5, 0.62)
ax.set_xlabel("Cường độ quốc tế hóa — FSTS (%)", fontsize=11)
ax.set_ylabel("Hiệu quả (năng suất lao động, tương đối)", fontsize=11)
ax.annotate("Thể chế mạnh hơn → điểm uốn dịch phải (cao hơn) →",
            xy=(30, 0.55), fontsize=8.5, style="italic", color="#1A5276")
ax.legend(loc="lower left", fontsize=8, framealpha=0.95, edgecolor="#999999")
ax.set_title("Hình 4.x. Họ đường cong I–P phụ thuộc chế độ thể chế ICRV\n"
             "Điểm uốn CAO ở thể chế mạnh và GIẢM dần theo chiều thể chế yếu (I→V); "
             "SIDS chuyển sang âm đơn điệu (FIP, H1b)",
             fontsize=11, fontweight="bold")
ax.text(0.005, -0.115, "Nguồn: Nhóm I–V từ P7 50 nền (gồm Nhật Bản, p7_50econ_models.csv), điểm uốn khớp Bảng 4.5; "
        "Nhóm VI (SIDS) từ P8 (β = −1,339).\nTrục tung là năng suất tương đối (minh họa hình dạng/vị trí, không phải mức tuyệt đối).",
        transform=ax.transAxes, fontsize=7, color="#666666")

for d in OUT_DIRS:
    out = os.path.join(ROOT, d, OUT_REL)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    print("Saved:", os.path.relpath(out, ROOT))
plt.close(fig)
