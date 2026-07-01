"""
Generate CĐ1's seven descriptive figures (Hình 2.3.3.1 … 2.3.7.1) and an Excel
workbook holding the exact source data behind each figure.

All values are taken verbatim from the reported tables/captions in
chuyen_de/cd1/00_cd1_ctu_final_vi.md (the author's vetted descriptive statistics
on the 88,869-firm / 50-economy WBES pool, 2006–2026). No figures are
recomputed or fabricated; this script only visualises numbers already in the text.

Outputs:
  chuyen_de/cd1/figures/hinh_2_3_3_1.png … hinh_2_3_7_1.png  (300 DPI)
  chuyen_de/cd1/cd1_figure_data.xlsx  (one sheet per figure)

Run from project root:  python3 chuyen_de/cd1/figures/make_cd1_descriptive_figs.py
"""
from __future__ import annotations
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman"],
    "font.size": 10,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "figure.facecolor": "white",
})

HERE = os.path.dirname(os.path.abspath(__file__))
XLSX = os.path.join(HERE, "..", "cd1_figure_data.xlsx")
NAVY, TEAL, AMBER, GRAY = "#2C3E50", "#117A65", "#B9770E", "#7F8C8D"
sheets: dict[str, pd.DataFrame] = {}


def save(fig, name):
    out = os.path.join(HERE, name)
    fig.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Saved:", out)


# ── Hình 2.3.3.1 — pool by WBES schema generation ───────────────────────────
df = pd.DataFrame({
    "Thế hệ schema": ["PICS3 (2006–2012)", "Standardized (2013–2017)", "BREADY (2018–2026)"],
    "Số đợt": [18, 27, 58],
    "Số doanh nghiệp": [8048, 23940, 56881],
})
df["Tỷ lệ %"] = (df["Số doanh nghiệp"] / 88869 * 100).round(1)
sheets["H2.3.3.1_schema"] = df
fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(df["Thế hệ schema"], df["Số doanh nghiệp"], color=[GRAY, TEAL, NAVY], width=0.6)
for b, n, p in zip(bars, df["Số doanh nghiệp"], df["Tỷ lệ %"]):
    ax.text(b.get_x() + b.get_width() / 2, n + 700, f"{n:,}\n({p}%)", ha="center", va="bottom", fontsize=9)
ax.set_ylabel("Số doanh nghiệp"); ax.set_ylim(0, 65000)
ax.set_title("Hình 2.3.3.1. Phân bố pool mô tả 88.869 doanh nghiệp (2006–2026)\ntheo 3 thế hệ schema WBES", fontsize=11, fontweight="bold")
save(fig, "hinh_2_3_3_1.png")

# ── Hình 2.3.3.2 — pool by 6 ICRV groups ────────────────────────────────────
df = pd.DataFrame({
    "Nhóm ICRV": ["IV Chuyển đổi TB-thấp", "V Đang nổi", "III Trung bình cao",
                  "I Advanced đổi mới", "VI SIDS", "II Advanced tài nguyên"],
    "Số doanh nghiệp": [45003, 18957, 13993, 6390, 2295, 2231],
    "Tỷ lệ %": [50.6, 21.3, 15.7, 7.2, 2.6, 2.5],
})
sheets["H2.3.3.2_ICRV"] = df
fig, ax = plt.subplots(figsize=(9, 4.8))
bars = ax.barh(df["Nhóm ICRV"][::-1], df["Số doanh nghiệp"][::-1], color=NAVY)
for b, n, p in zip(bars, df["Số doanh nghiệp"][::-1], df["Tỷ lệ %"][::-1]):
    ax.text(n + 500, b.get_y() + b.get_height() / 2, f"{n:,} ({p}%)", va="center", fontsize=9)
ax.set_xlabel("Số doanh nghiệp"); ax.set_xlim(0, 50000)
ax.set_title("Hình 2.3.3.2. Phân bố pool mô tả theo 6 nhóm ICRV (n = 88.869)", fontsize=11, fontweight="bold")
save(fig, "hinh_2_3_3_2.png")

# ── Hình 2.3.3.3 — dispersion of standardized productivity by ICRV ──────────
df = pd.DataFrame({
    "Nhóm ICRV": ["I Adv. đổi mới", "II Adv. tài nguyên", "III Trung bình cao",
                  "IV Chuyển đổi TB-thấp", "V Đang nổi", "VI SIDS"],
    "sd ln(LP)": [1.00, 1.14, 1.37, 1.31, 1.39, 1.32],
    "P90/P10": [11.7, 20.8, 25.0, 27.8, 30.3, 26.3],
    "P75/P25": [3.4, 4.8, 5.4, 5.6, 5.8, 5.4],
})
sheets["H2.3.3.3_dispersion"] = df
fig, ax = plt.subplots(figsize=(8.5, 5))
x = np.linspace(-4, 4, 400)
cmap = plt.cm.viridis(np.linspace(0.1, 0.9, 6))
for (lab, sd), c in zip(zip(df["Nhóm ICRV"], df["sd ln(LP)"]), cmap):
    y = np.exp(-(x ** 2) / (2 * sd ** 2)) / (sd * np.sqrt(2 * np.pi))
    ax.plot(x, y, color=c, lw=2, label=f"{lab} (sd={sd:.2f}; P90/P10={df.loc[df['Nhóm ICRV']==lab,'P90/P10'].iloc[0]:.0f})")
ax.set_xlabel("Năng suất lao động chuẩn hóa trong đợt (z-score)")
ax.set_ylabel("Mật độ")
ax.legend(fontsize=7.5, loc="upper right")
ax.set_title("Hình 2.3.3.3. Phân phối năng suất chuẩn hóa trong đợt theo 6 nhóm ICRV\n"
             "(đường mật độ chuẩn N(0, sd) theo độ lệch chuẩn nhóm; Nhóm I hẹp nhất, Nhóm V rộng nhất)",
             fontsize=10, fontweight="bold")
save(fig, "hinh_2_3_3_3.png")

# ── Hình 2.3.4.1 — Δ percentage points 2018–2026 vs 2006–2012 (Bảng 2.3.6.1) ─
df = pd.DataFrame({
    "Nhóm ICRV": ["III Trung bình cao", "IV Chuyển đổi TB-thấp", "V Đang nổi", "VI SIDS"],
    "Δ Website": [11.2, 20.6, 21.6, 30.8],
    "Δ DN xuất khẩu": [12.5, -11.3, 1.5, -2.6],
    "Δ FDI ≥10%": [1.6, -6.7, -2.5, -5.3],
    "Δ R&D": [np.nan, np.nan, -31.6, np.nan],
    "Δ ISO": [5.2, 3.4, 0.0, -10.2],
})
sheets["H2.3.4.1_delta_pp"] = df
inds = ["Δ Website", "Δ DN xuất khẩu", "Δ FDI ≥10%", "Δ R&D", "Δ ISO"]
fig, ax = plt.subplots(figsize=(10, 5.2))
xpos = np.arange(len(df)); w = 0.16
colors = [NAVY, TEAL, AMBER, "#922B21", GRAY]
for i, (ind, c) in enumerate(zip(inds, colors)):
    vals = df[ind].values
    ax.bar(xpos + (i - 2) * w, np.nan_to_num(vals), w, label=ind, color=c)
ax.axhline(0, color="black", lw=0.8)
ax.set_xticks(xpos); ax.set_xticklabels(df["Nhóm ICRV"], fontsize=9)
ax.set_ylabel("Δ điểm phần trăm (2018–2026 − 2006–2012)")
ax.legend(fontsize=8, ncol=5, loc="lower center", bbox_to_anchor=(0.5, -0.22))
ax.set_title("Hình 2.3.4.1. Thay đổi 5 chỉ số giữa hai kỳ khảo sát theo nhóm ICRV (III–VI)\n"
             "Website nhảy vọt ở IV/V/VI; R&D Nhóm V giảm do hiệu ứng schema (Δ R&D chỉ tính được cho Nhóm V)",
             fontsize=10, fontweight="bold")
save(fig, "hinh_2_3_4_1.png")

# ── Hình 2.3.5.1 — firm structure by ICRV (Bảng 2.3.5.1) ────────────────────
df = pd.DataFrame({
    "Nhóm ICRV": ["I", "II", "III", "IV", "V", "VI"],
    "SME (%)": [76.9, 77.4, 78.7, 74.0, 86.0, 91.8],
    "DN xuất khẩu (%)": [24.5, 11.7, 21.3, 14.3, 18.8, 14.7],
    "FDI ≥10% (%)": [7.7, 13.6, 8.9, 3.1, 7.1, 20.0],
})
sheets["H2.3.5.1_structure"] = df
fig, ax = plt.subplots(figsize=(9, 5))
xpos = np.arange(len(df)); w = 0.26
ax.bar(xpos - w, df["SME (%)"], w, label="SME (%)", color=NAVY)
ax.bar(xpos, df["DN xuất khẩu (%)"], w, label="DN xuất khẩu (%)", color=TEAL)
ax.bar(xpos + w, df["FDI ≥10% (%)"], w, label="FDI ≥10% (%)", color=AMBER)
ax.set_xticks(xpos); ax.set_xticklabels(["Nhóm " + g for g in df["Nhóm ICRV"]], fontsize=9)
ax.set_ylabel("%"); ax.legend(fontsize=8.5)
ax.set_title("Hình 2.3.5.1. Cấu trúc doanh nghiệp theo nhóm ICRV\n"
             "SIDS (VI) có tỷ lệ SME cao nhất (91,8%) và FDI cao (20,0%); FDI cực tiểu ở Nhóm IV (3,1%)",
             fontsize=10, fontweight="bold")
save(fig, "hinh_2_3_5_1.png")

# ── Hình 2.3.6.1 — capability radar, 3 ICRV groups (Bảng 2.3.3.2 + 2.3.4.1) ──
dims = ["FSTS", "Đổi mới SP", "R&D", "Website", "ISO"]
data = {"III Trung bình cao": [10.2, 26.7, 21.5, 53.9, 25.4],
        "V Đang nổi": [10.6, 24.4, 17.5, 40.9, 12.7],
        "VI SIDS": [6.7, 34.2, 10.2, 41.5, 12.2]}
df = pd.DataFrame(data, index=dims).T.reset_index().rename(columns={"index": "Nhóm ICRV"})
sheets["H2.3.6.1_radar"] = df
ang = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist(); ang += ang[:1]
fig, ax = plt.subplots(figsize=(7.5, 7), subplot_kw=dict(polar=True))
for (lab, vals), c in zip(data.items(), [NAVY, TEAL, AMBER]):
    v = vals + vals[:1]
    ax.plot(ang, v, color=c, lw=2, label=lab); ax.fill(ang, v, color=c, alpha=0.08)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(dims, fontsize=10)
ax.set_title("Hình 2.3.6.1. Hồ sơ năng lực 5 chiều theo nhóm ICRV (pool mô tả 2006–2026)\n"
             "Nhóm III, V, VI; giá trị % từ Bảng 2.3.3.2 và 2.3.4.1",
             fontsize=10, fontweight="bold", pad=22)
ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.10), fontsize=8.5)
save(fig, "hinh_2_3_6_1.png")

# ── Hình 2.3.7.1 — Mongolia 2009/2013/2019 (§2.3.7.6) ───────────────────────
df = pd.DataFrame({
    "Đợt khảo sát": [2009, 2013, 2019],
    "FSTS (%)": [5.8, 3.9, 4.2],
    "FDI ≥10% (%)": [np.nan, 7.2, 4.2],   # 2009 không nêu rõ trong nguồn
})
sheets["H2.3.7.1_mongolia"] = df
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(df["Đợt khảo sát"], df["FSTS (%)"], "o-", color=NAVY, lw=2, ms=8, label="FSTS (%)")
m = df["FDI ≥10% (%)"].notna()
ax.plot(df["Đợt khảo sát"][m], df["FDI ≥10% (%)"][m], "s--", color=AMBER, lw=2, ms=8, label="FDI ≥10% (%)")
for _, r in df.iterrows():
    ax.annotate(f'{r["FSTS (%)"]:.1f}', (r["Đợt khảo sát"], r["FSTS (%)"]), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9)
ax.set_xticks([2009, 2013, 2019]); ax.set_ylim(0, 12)
ax.set_xlabel("Đợt khảo sát WBES"); ax.set_ylabel("%"); ax.legend(fontsize=9)
ax.set_title("Hình 2.3.7.1. Mông Cổ: tiến triển 2009–2019 (3 đợt khảo sát WBES)\n"
             "FSTS đình trệ 4–6%; FDI giảm dần (lời nguyền tài nguyên giai đoạn 1); website dao động 39–49%",
             fontsize=10, fontweight="bold")
ax.text(0.02, 0.03, "Ghi chú: FDI 2009 không được nêu tách biệt trong nguồn (§2.3.7.6).",
        transform=ax.transAxes, fontsize=7.5, style="italic", color=GRAY)
save(fig, "hinh_2_3_7_1.png")

# ── Excel workbook ──────────────────────────────────────────────────────────
with pd.ExcelWriter(XLSX, engine="openpyxl") as xw:
    readme = pd.DataFrame({
        "Hình": ["2.3.3.1", "2.3.3.2", "2.3.3.3", "2.3.4.1", "2.3.5.1", "2.3.6.1", "2.3.7.1"],
        "Nội dung": ["Pool theo 3 thế hệ schema WBES", "Pool theo 6 nhóm ICRV",
                     "Phân tán năng suất chuẩn hóa theo ICRV", "Δ 5 chỉ số giữa 2 kỳ (pp)",
                     "Cấu trúc doanh nghiệp theo ICRV", "Hồ sơ năng lực 5 chiều (III/V/VI)",
                     "Mông Cổ 2009–2019"],
        "Nguồn trong CĐ1": ["§2.3.3.1", "§2.3.3.1", "Bảng 2.3.3.1", "Bảng 2.3.6.1",
                            "Bảng 2.3.5.1", "Bảng 2.3.3.2 + 2.3.4.1", "§2.3.7.6"],
    })
    readme.to_excel(xw, sheet_name="README", index=False)
    for name, d in sheets.items():
        d.to_excel(xw, sheet_name=name[:31], index=False)
print("Saved:", os.path.normpath(XLSX))
print("\n✓ 7 CĐ1 descriptive figures + Excel data workbook generated.")
