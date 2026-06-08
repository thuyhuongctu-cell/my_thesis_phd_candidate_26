"""
Comprehensive academic portfolio overview for PhD dissertation:
  Published (P1 VEFR, P2 JFAR, Meta-2025 ICBEF, Book Chapter IntechOpen 2025)
  + 6 working manuscripts (P3-P8) with primary + backup journals
  + 2 chuyên đề (CD1 descriptive pool, CD2 theoretical model)
  + 5 thesis chapters
  + Shared construct framework (FSTS/TCI/DAI/ICRV/CDCM)

Run: python3 thesis/figures/generate_portfolio_overview.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8})

# Palette
C_PUB = "#2e7d32"   # published (green)
C_EMP = "#1565c0"   # empirical paper (blue)
C_META = "#6a1b9a"  # meta-analysis (purple)
C_EXT = "#e65100"   # extreme context / SIDS (orange)
C_INT = "#c62828"   # synthesis (red)
C_THESIS = "#4527a0"# thesis (deep purple)
C_BACKUP = "#666"   # backup journal text
INK = "#1a1a1a"

def box(ax, x, y, w, h, text, fc, fs=7, tc="white", bold=True):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.025",
                       linewidth=1.0, edgecolor=INK, facecolor=fc, zorder=3)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            color=tc, weight="bold" if bold else "normal", zorder=4, linespacing=1.2)

def arrow(ax, x1, y1, x2, y2, color=INK, lw=1.0, ls="-", rad=0.0):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=9, lw=lw, color=color, linestyle=ls,
                 connectionstyle=f"arc3,rad={rad}", zorder=2))

fig, ax = plt.subplots(figsize=(17, 10.5))
ax.set_xlim(0, 17); ax.set_ylim(0, 11); ax.axis("off")

# ── Title ──
ax.text(8.5, 10.5, "Danh mục Hồ sơ Khoa học — Luận án Tiến sĩ NCS Đỗ Thùy Hương (CTU)",
        ha="center", fontsize=15, weight="bold", color=INK)
ax.text(8.5, 10.10, "Quốc tế hóa → Hiệu quả Doanh nghiệp ở Châu Á–Thái Bình Dương · 4 công bố + 6 bản thảo + 2 chuyên đề + 5 chương luận án",
        ha="center", fontsize=9.5, color="#555", style="italic")

# ── Column headers ──
heads = [(2.0,"ĐÃ CÔNG BỐ",C_PUB), (5.6,"BẢN THẢO QUỐC GIA",C_EMP),
         (9.6,"TỔNG HỢP",C_META), (12.8,"TÍCH HỢP",C_INT), (15.5,"LUẬN ÁN",C_THESIS)]
for hx, ht, hc in heads:
    ax.text(hx, 9.55, ht, ha="center", fontsize=10, weight="bold", color=hc)

# ── Column 1: Published (4 items) ──
box(ax, 0.4, 8.5, 3.2, 0.85, "P1 — Tổng quan châu Á 17 nền KT mới nổi\nVEFR (Vietnam Econ. & Finance Review)\n✅ ĐÃ XUẤT BẢN", C_PUB, 7.0)
box(ax, 0.4, 7.5, 3.2, 0.85, "P2 — Quốc tế hóa DNNVV Trung Quốc\nJFAR (J. Finance & Acc. Research)\n✅ ĐÃ XUẤT BẢN + ảnh bìa", C_PUB, 7.0)
box(ax, 0.4, 6.5, 3.2, 0.85, "Meta-2025 (Đỗ & Phan) — k=113, r=0,07\nHội thảo Kinh tế 2024 / kỷ yếu ICBEF\n✅ minh chứng cv7857/BGDĐT", C_PUB, 7.0)
box(ax, 0.4, 5.5, 3.2, 0.85, "Book Chapter — Internationalization\n& Firm Performance (IntechOpen UK 2025)\n✅ Acceptance + peer review + bìa", C_PUB, 7.0)

# ── Column 2: Country / extreme empirical (P3-P5, P8) ──
box(ax, 4.2, 8.5, 2.9, 0.85, "P3 Việt Nam — JABS (ABS-2)\nN=2.958 (3 sóng); TP≈39,7%\nLower-mid Transition (ICRV-3)", C_EMP, 7.0)
box(ax, 4.2, 7.5, 2.9, 0.85, "P4 Singapore — MIR (ABS-3)\nN=623; TP=82% (support-cstr.)\nAdvanced I (ICRV-1)", C_EMP, 7.0)
box(ax, 4.2, 6.5, 2.9, 0.85, "P5 Trung Quốc — IJOEM (ABS-2)\nN=4.544 (2012/2024); TP≈48,8%\nUpper-mid (ICRV-2)", C_EMP, 7.0)
ax.text(5.65, 6.32, "↳ Backup: Chinese Management Studies", fontsize=6.5, color=C_BACKUP, ha="center", style="italic")
box(ax, 4.2, 5.3, 2.9, 0.85, "P8 Pacific SIDS — World Development\nN=1.469 / 9 nước; β=−0,404 (FIP)\nFrontier/SIDS (ICRV-5/6)", C_EXT, 7.0)

# ── Column 3: Synthesis / multi-country ──
box(ax, 7.6, 8.0, 3.6, 1.1, "P6 Meta-analysis ba tầng — IBR (ABS-3)\nk=259, K=309 (cập nhật 23/05)\nr̄=0,074 [0,060; 0,088]; I²=61,2%\nICRV moderator Q_M=10,16 (p=,038)", C_META, 7.2)
box(ax, 7.6, 6.5, 3.6, 1.1, "P7 Capstone 49 nền KT — JIBS (ABS-4*)\nN=84.910-91.982; 102 country-year\nTP≈36% (M11: 34,6%, p=,002)\nDAI×ICRV p=,012", C_META, 7.2)
ax.text(9.4, 6.32, "↳ Backup: International Business Review (IBR)", fontsize=6.5, color=C_BACKUP, ha="center", style="italic")

# ── Column 4: Integration (CD1, CD2) ──
box(ax, 11.7, 8.0, 2.6, 1.0, "CĐ1 — Phân tích pool mô tả\n101.185 DN · 47 nền KT\n14 sóng WBES · 108 country-year\nKhung ICRV 6 nhóm", C_INT, 7.2)
box(ax, 11.7, 6.5, 2.6, 1.0, "CĐ2 — Mô hình lý thuyết\nUppsala + RBV + Institutional\n+ Upper Echelons + CDCM\nH1–H6, M0–M7", C_INT, 7.2)

# ── Column 5: 5 thesis chapters ──
for i, (ct, cy) in enumerate([("Ch.1 Giới thiệu", 8.7), ("Ch.2 Tổng quan tài liệu", 7.8),
                              ("Ch.3 Phương pháp", 6.9), ("Ch.4 Kết quả", 6.0),
                              ("Ch.5 Kết luận & Đề xuất", 5.1)]):
    box(ax, 14.6, cy, 2.2, 0.7, ct, C_THESIS, 7.5)

# ── Arrows: evidence flow ──
# Published feeds baseline of integration
arrow(ax, 3.6, 6.92, 7.6, 6.92, color=C_PUB, lw=1.1, rad=-0.05)  # Meta→P6
arrow(ax, 3.6, 6.0, 11.7, 6.95, color=C_PUB, lw=0.8, rad=0.08, ls="--")  # IntechOpen→CD1
# P3/P4/P5/P8 feed P6 (meta-analysis pool) and P7 (multi-country)
for ey in (8.92, 7.92, 6.92):
    arrow(ax, 7.1, ey, 7.6, 8.5, color=C_EMP, lw=0.9, rad=-0.08)
for ey in (8.92, 7.92, 6.92, 5.72):
    arrow(ax, 7.1, ey, 7.6, 7.0, color=C_EMP, lw=0.9, rad=0.10)
# P6, P7 → CD1, CD2
arrow(ax, 11.2, 8.5, 11.7, 8.5, color=C_META, lw=1.1)
arrow(ax, 11.2, 7.0, 11.7, 7.0, color=C_META, lw=1.1)
arrow(ax, 11.2, 8.5, 11.7, 7.0, color=C_META, lw=0.7, rad=0.1)
# CD1, CD2 → thesis chapters
arrow(ax, 14.3, 8.5, 14.6, 7.5, color=C_INT, lw=0.9, rad=0.1)
arrow(ax, 14.3, 7.0, 14.6, 6.5, color=C_INT, lw=0.9)
# Direct P6/P7 → Ch.4 (results)
arrow(ax, 11.2, 8.0, 14.6, 6.3, color=C_META, lw=0.7, ls="--", rad=-0.15)

# ── Construct framework band ──
band = FancyBboxPatch((0.4, 3.4), 16.4, 1.0,
                      boxstyle="round,pad=0.02,rounding_size=0.03",
                      linewidth=1.0, edgecolor="#444", facecolor="#fff3e0", zorder=1)
ax.add_patch(band)
ax.text(8.6, 4.10, "KHUNG CONSTRUCT DÙNG CHUNG — connective tissue",
        ha="center", fontsize=9, weight="bold", color="#bf6000")
ax.text(8.6, 3.70, "FSTS = d3c/100 (cường độ xuất khẩu trực tiếp)   ·   TCI (năng lực công nghệ, z-std)   ·   "
        "DAI Tier-1/Tier-1+2 (áp dụng số nền tảng — KHÔNG dynamic capability)",
        ha="center", fontsize=7.8, color="#7a4a00")
ax.text(8.6, 3.50, "ICRV (6 chế độ thể chế: Advanced-Innovation / Advanced-Resource / Upper-mid / Emerging / Frontier / SIDS)   ·   "
        "CDCM (Context-Contingent Digital-and-Capability Model)",
        ha="center", fontsize=7.8, color="#7a4a00")

# ── Central thesis statement ──
ax.text(8.5, 2.85, '"Không có một mức quốc tế hóa tối ưu duy nhất — turning point phụ thuộc bối cảnh thể chế (ICRV);',
        ha="center", fontsize=9.2, style="italic", color=INK, weight="bold")
ax.text(8.5, 2.55, 'thể chế càng yếu → turning point càng muộn; ở SIDS cực yếu, quốc tế hóa gây bất lợi (Forced Internationalization Penalty)."',
        ha="center", fontsize=9.2, style="italic", color=INK, weight="bold")

# ── Status legend ──
ax.text(0.4, 1.95, "Trạng thái & màu:", fontsize=8.2, weight="bold")
items = [
    (0.4, 1.55, C_PUB, "● Đã công bố (P1, P2, Meta-2025, Book Chapter IntechOpen 2025)"),
    (0.4, 1.25, C_EMP, "● Bản thảo nghiên cứu quốc gia (P3 JABS, P4 MIR, P5 IJOEM)"),
    (0.4, 0.95, C_EXT, "● Bối cảnh cực biên (P8 SIDS — World Development)"),
    (0.4, 0.65, C_META, "● Tổng hợp đa quốc gia (P6 IBR, P7 JIBS)"),
    (0.4, 0.35, C_INT, "● Tích hợp lý thuyết (CĐ1, CĐ2)"),
    (8.6, 1.55, C_THESIS, "● 5 chương luận án (Ch.1–Ch.5)"),
    (8.6, 1.25, "#666", "─── mũi tên đặc: dòng bằng chứng/đóng góp chính"),
    (8.6, 0.95, "#666", "─ ─ mũi tên đứt: đóng góp phụ trợ"),
]
for x, y, c, t in items:
    ax.text(x, y, t, fontsize=7.5, color=c)

ax.text(16.8, 0.35, "Cập nhật: 28/05/2026", fontsize=7, color="#999", ha="right")

plt.tight_layout()
fig.savefig("thesis/figures/portfolio_overview_full.png", dpi=200, bbox_inches="tight")
plt.close(fig)
print("Saved: thesis/figures/portfolio_overview_full.png")
