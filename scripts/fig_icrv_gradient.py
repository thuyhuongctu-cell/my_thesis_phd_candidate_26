#!/usr/bin/env python3
"""Publication figure: institutional capability gradient by ICRV group.

Generated via the econ-visualization skill. Data: cd1_pipeline_by_icrv.csv
(raw WBES 49-economy frame, deduped, waves >= 2006). Reproduce:
    python3 scripts/fig_icrv_gradient.py
Outputs: thesis/figures/fig_icrv_capability_gradient.png (+ .pdf), 300 dpi.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data_wbes/analysis/cd1_pipeline_by_icrv.csv")
order = ["Advanced_innovation", "Advanced_resource", "Upper_mid",
         "Lower_mid_transition", "Emerging", "SIDS_small"]
labels = ["I\nAdv. đổi mới", "II\nAdv. tài nguyên", "III\nTrung bình cao",
          "IV\nChuyển đổi TB-thấp", "V\nĐang nổi", "VI\nSIDS"]
df = df.set_index("group").loc[order]

series = [("rd_pct", "Chi R&D", "0.15"),
          ("iso_cert_pct", "Chứng nhận ISO", "0.45"),
          ("website_pct", "Website (DAI Tier-1)", "0.75")]

fig, ax = plt.subplots(figsize=(7, 4))
x = range(len(order))
w = 0.26
for i, (col, lab, grey) in enumerate(series):
    ax.bar([p + (i - 1) * w for p in x], df[col], width=w,
           label=lab, color=str(grey), edgecolor="black", linewidth=0.5)

ax.set_xticks(list(x))
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel("Tỷ lệ doanh nghiệp (%)", fontsize=10)
ax.set_title("Gradient năng lực theo nhóm thể chế ICRV (WBES, 49 nền, ≥2006)",
             fontsize=11)
ax.legend(frameon=False, fontsize=9, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", linewidth=0.3, alpha=0.5)
ax.set_axisbelow(True)

for i, (col, _, _) in enumerate(series):
    for p, v in zip(x, df[col]):
        ax.annotate(f"{v:.0f}", (p + (i - 1) * w, v + 0.8),
                    ha="center", fontsize=7)

fig.tight_layout()
fig.savefig("thesis/figures/fig_icrv_capability_gradient.png", dpi=300)
fig.savefig("thesis/figures/fig_icrv_capability_gradient.pdf")
print("saved thesis/figures/fig_icrv_capability_gradient.{png,pdf}")
