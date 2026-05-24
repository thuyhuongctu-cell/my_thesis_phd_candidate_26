"""
Generate dissertation overview visuals:
  (1) dissertation_linkage_map.png — architecture linking P3-P8, CD1/CD2, 5 chapters
  (2) results_synthesis.png        — turning-point gradient by ICRV regime + curve family
Run: python3 thesis/figures/generate_dissertation_overview.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})

# Palette
C_FOUND = "#9e9e9e"; C_EMP = "#1f77b4"; C_SYN = "#2ca02c"
C_INT = "#d62728"; C_THESIS = "#6a3d9a"; C_EXT = "#ff7f0e"
INK = "#1a1a1a"

def box(ax, x, y, w, h, text, fc, fontsize=8, tc="white", bold=True):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.02",
                       linewidth=1.1, edgecolor=INK, facecolor=fc, zorder=3)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fontsize,
            color=tc, weight="bold" if bold else "normal", zorder=4, linespacing=1.25)

def arrow(ax, x1, y1, x2, y2, style="-|>", color=INK, lw=1.3, ls="-", rad=0.0):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                 mutation_scale=12, lw=lw, color=color, linestyle=ls,
                 connectionstyle=f"arc3,rad={rad}", zorder=2))

# ============================================================
# FIGURE 1 — DISSERTATION LINKAGE MAP
# ============================================================
fig, ax = plt.subplots(figsize=(15.5, 9.2))
ax.set_xlim(0, 16); ax.set_ylim(0, 10); ax.axis("off")

ax.text(8, 9.65, "Kiến trúc Luận án: Quốc tế hóa → Hiệu quả Doanh nghiệp ở Châu Á–Thái Bình Dương",
        ha="center", fontsize=15, weight="bold", color=INK)
ax.text(8, 9.25, "Sự liên kết giữa 6 nghiên cứu thành phần (P3–P8), 2 chuyên đề (CĐ1/CĐ2) và 5 chương luận án",
        ha="center", fontsize=10, color="#555", style="italic")

# Column headers
heads = [(1.6,"NỀN TẢNG",C_FOUND),(4.6,"NGHIÊN CỨU\nQUỐC GIA",C_EMP),
         (8.0,"TỔNG HỢP",C_SYN),(11.2,"TÍCH HỢP",C_INT),(14.3,"LUẬN ÁN",C_THESIS)]
for hx, ht, hc in heads:
    ax.text(hx, 8.75, ht, ha="center", fontsize=9.5, weight="bold", color=hc)

# Foundation
box(ax, 0.5, 7.4, 2.2, 0.95, "P1 + P2\nICBEF 2024\n(k=113, r=0,07)\nbaseline + CDCM", C_FOUND, 7.3)

# Empirical country studies (by ICRV regime)
box(ax, 3.5, 7.55, 2.3, 0.9, "P4 Singapore\nMIR (ABS-3)\nICRV-1 Advanced\nTP≈82% (saturation)", C_EMP, 7.0)
box(ax, 3.5, 6.35, 2.3, 0.9, "P5 China\nIJOEM (ABS-2)\nICRV-2 Upper-mid\nTP≈48,8% (stable)", C_EMP, 7.0)
box(ax, 3.5, 5.15, 2.3, 0.9, "P3 Vietnam\nJABS (ABS-2)\nICRV-3 Emerging\nTP≈39,7% (inverted-U)", C_EMP, 7.0)
box(ax, 3.5, 3.75, 2.3, 0.95, "P8 Pacific SIDS\nWorld Development\nICRV-5/6 Frontier\nForced Penalty (no TP)", C_EXT, 7.0)

# Synthesis
box(ax, 6.9, 6.55, 2.3, 1.05, "P6 Meta-analysis\nIBR (ABS-3)\nk=259, K=309\nr̄=0,074  I²=61,2%\nICRV mod. p=,038", C_SYN, 7.2)
box(ax, 6.9, 4.7, 2.3, 1.05, "P7 Đa quốc gia\nJIBS (ABS-4*)\n49 nền KT, N≈85k\nTP≈36% (28%→55%\ntheo ICRV)", C_SYN, 7.2)

# Integration
box(ax, 10.2, 6.4, 2.1, 1.0, "CĐ1\nPhân tích pool\n101.185 DN\n47 nền kinh tế\n(mô tả)", C_INT, 7.3)
box(ax, 10.2, 4.85, 2.1, 1.0, "CĐ2\nMô hình lý thuyết\nH1–H6, M0–M7\nCDCM + ICRV", C_INT, 7.3)

# Thesis chapters
chs = [("Ch.1 Giới thiệu",7.7),("Ch.2 Tổng quan",6.75),("Ch.3 Phương pháp",5.8),
       ("Ch.4 Kết quả",4.85),("Ch.5 Kết luận",3.9)]
for ct, cy in chs:
    box(ax, 13.3, cy, 2.2, 0.72, ct, C_THESIS, 8, bold=True)

# Arrows: foundation -> studies/meta
arrow(ax, 2.7, 7.85, 3.5, 6.8, color=C_FOUND, lw=1.6)
arrow(ax, 2.7, 7.7, 6.9, 7.2, color=C_FOUND, lw=1.4, rad=0.15)
# country studies -> P6 meta (evidence)
for sy in (8.0, 6.8, 5.6):
    arrow(ax, 5.8, sy, 6.9, 7.1, color=C_EMP, lw=1.1, rad=-0.12)
# country studies + SIDS -> P7
for sy in (7.7, 6.5, 5.3, 4.2):
    arrow(ax, 5.8, sy, 6.9, 5.2, color=C_EMP, lw=1.0, rad=0.12)
# P6, P7 -> CD2 (theory) and CD1 (pool)
arrow(ax, 9.2, 7.05, 10.2, 6.9, color=C_SYN, lw=1.4)
arrow(ax, 9.2, 5.2, 10.2, 5.35, color=C_SYN, lw=1.4)
arrow(ax, 9.2, 6.7, 10.2, 5.6, color=C_SYN, lw=1.0, rad=0.1)
# CD1, CD2 -> thesis
arrow(ax, 12.3, 6.9, 13.3, 6.0, color=C_INT, lw=1.3, rad=0.1)
arrow(ax, 12.3, 5.35, 13.3, 5.2, color=C_INT, lw=1.3)
# P7/P6 also feed thesis ch4 directly
arrow(ax, 9.2, 5.0, 13.3, 5.1, color=C_SYN, lw=0.9, ls="--", rad=-0.18)

# Shared-construct band (connective tissue)
band = FancyBboxPatch((0.5, 2.35), 15.0, 0.95, boxstyle="round,pad=0.02,rounding_size=0.03",
                      linewidth=1.2, edgecolor="#444", facecolor="#fff3e0", zorder=1)
ax.add_patch(band)
ax.text(8, 3.05, "KHUNG CONSTRUCT DÙNG CHUNG (connective tissue)", ha="center",
        fontsize=9, weight="bold", color="#bf6000")
ax.text(8, 2.62, "FSTS = d3c/100 (cường độ xuất khẩu)   ·   TCI (năng lực công nghệ)   ·   "
        "DAI (Tier-1/Tier-1+2 áp dụng số nền tảng — KHÔNG phải dynamic capability)   ·   "
        "ICRV (6 nhóm thể chế)", ha="center", fontsize=8.4, color="#7a4a00")

# Central thesis statement
ax.text(8, 1.75, '"Không có một mức quốc tế hóa tối ưu duy nhất — điểm uốn (turning point) phụ thuộc bối cảnh thể chế (ICRV);',
        ha="center", fontsize=9.2, style="italic", color=INK, weight="bold")
ax.text(8, 1.42, 'thể chế càng yếu → turning point càng muộn; ở SIDS cực yếu, quốc tế hóa gây bất lợi (Forced Internationalization Penalty)."',
        ha="center", fontsize=9.2, style="italic", color=INK, weight="bold")

# Legend
ax.text(0.5, 0.75, "Mũi tên: dòng bằng chứng/đóng góp.  ", fontsize=7.6, color="#666")
ax.text(0.5, 0.45, "Màu: ⬤ nền tảng  ⬤ thực nghiệm quốc gia  ⬤ tổng hợp  ⬤ tích hợp (CĐ)  ⬤ luận án  ⬤ bối cảnh cực biên (SIDS)",
        fontsize=7.6, color="#666")
ax.text(15.5, 0.45, "k=259/K=309 · 24/05/2026", fontsize=7.2, color="#999", ha="right")

plt.tight_layout()
fig.savefig("thesis/figures/dissertation_linkage_map.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# ============================================================
# FIGURE 2 — RESULTS SYNTHESIS
# ============================================================
fig, (axL, axR) = plt.subplots(1, 2, figsize=(15, 6.4))

# ---- Panel A: turning-point gradient by ICRV regime ----
# Country study points (ICRV regime -> turning point %)
pts = [("P4 Singapore", 1, 82.0, "saturation\n(support-constrained)", C_EMP),
       ("P5 China", 2, 48.8, "stable over time", C_EMP),
       ("P3 Vietnam", 3, 39.7, "inverted-U", C_EMP),
       ("P7 pooled", 2.5, 36.0, "49 economies", C_SYN)]
# P7 cross-regime band: Group I ~28% -> Group V/VI ~55%
reg_x = np.array([1, 2, 3, 4, 5, 6])
reg_tp = np.array([28, 34, 40, 47, 55, np.nan])  # VI = forced penalty (no TP)
axL.plot(reg_x[:5], reg_tp[:5], "o--", color=C_SYN, lw=2, ms=7,
         label="P7: turning point theo nhóm ICRV (28%→55%)", zorder=3)
axL.fill_between(reg_x[:5], reg_tp[:5]-5, reg_tp[:5]+5, color=C_SYN, alpha=0.12, zorder=1)

for name, xr, tp, note, col in pts:
    mk = "D" if name.startswith("P7") else "o"
    axL.scatter(xr, tp, s=130, color=col, edgecolor=INK, zorder=5, marker=mk)
    dy = 6 if name != "P5 China" else -10
    axL.annotate(f"{name}\n{tp}%", (xr, tp), textcoords="offset points",
                 xytext=(8, dy), fontsize=8, weight="bold")

# SIDS forced penalty zone
axL.axvspan(5.5, 6.5, color=C_EXT, alpha=0.15, zorder=0)
axL.scatter(6, 8, s=160, color=C_EXT, edgecolor=INK, marker="X", zorder=5)
axL.annotate("P8 SIDS\nForced Penalty\n(không có TP — quan hệ âm)", (6, 8),
             textcoords="offset points", xytext=(-12, 14), fontsize=8,
             weight="bold", color="#a14a00", ha="center")

axL.set_xticks(range(1, 7))
axL.set_xticklabels(["1\nAdvanced", "2\nUpper-mid", "3\nEmerging", "4\nResource",
                     "5\nSIDS", "6\nFrontier"], fontsize=8)
axL.set_xlabel("Nhóm thể chế ICRV (mạnh → yếu)", fontsize=10, weight="bold")
axL.set_ylabel("Điểm uốn / Turning point (% FSTS)", fontsize=10, weight="bold")
axL.set_title("(A) Turning point là hàm của chất lượng thể chế (ICRV)", fontsize=11, weight="bold")
axL.set_ylim(0, 100); axL.set_xlim(0.5, 6.6)
axL.grid(alpha=0.25, ls=":")
axL.legend(loc="upper left", fontsize=8, framealpha=0.9)

# ---- Panel B: family of context-dependent inverted-U curves ----
x = np.linspace(0, 1, 300)
curves = [("ICRV-1 Advanced (TP≈28%)", 0.28, C_EMP, 1.0),
          ("ICRV-3 Emerging (TP≈40%)", 0.40, "#17a2b8", 1.0),
          ("ICRV-5 SIDS-adj (TP≈55%)", 0.55, C_SYN, 1.0)]
for lbl, tp, col, a in curves:
    # inverted-U with peak at tp: y = -(x-tp)^2 scaled
    y = 1.0 - 6.0 * (x - tp) ** 2
    axR.plot(x * 100, y, color=col, lw=2.4, alpha=a, label=lbl)
    axR.axvline(tp * 100, color=col, ls=":", lw=1, alpha=0.6)

# Forced penalty curve (monotonic decline, SIDS)
y_fp = 0.6 - 1.4 * x
axR.plot(x * 100, y_fp, color=C_EXT, lw=2.6, ls="--",
         label="ICRV-6 SIDS: Forced Penalty (âm đơn điệu)")

axR.axhline(0, color="#999", lw=0.8)
axR.set_xlabel("Cường độ quốc tế hóa FSTS (%)", fontsize=10, weight="bold")
axR.set_ylabel("Hiệu quả (ln năng suất, chuẩn hoá)", fontsize=10, weight="bold")
axR.set_title("(B) Họ đường cong I→P phụ thuộc bối cảnh", fontsize=11, weight="bold")
axR.set_ylim(-1.0, 1.2); axR.set_xlim(0, 100)
axR.grid(alpha=0.25, ls=":")
axR.legend(loc="lower left", fontsize=8, framealpha=0.9)

fig.suptitle("Tổng hợp Kết quả: Quan hệ Quốc tế hóa–Hiệu quả theo Bối cảnh Thể chế (P3–P8, k=259)",
             fontsize=13, weight="bold", y=1.00)
plt.tight_layout()
fig.savefig("thesis/figures/results_synthesis.png", dpi=200, bbox_inches="tight")
plt.close(fig)

print("Saved: thesis/figures/dissertation_linkage_map.png")
print("Saved: thesis/figures/results_synthesis.png")
