#!/usr/bin/env python3
"""P8 Figure 1: the inverted-U inverts at the periphery.
Mainland transition (P7 Lower-mid): concave inverted-U (β₁=+0.709, β₂=-1.012).
Pacific SIDS (M3, capability-conditioned): convex U-shape (β₁=-0.860, β₂=+0.844).
Monochrome, journal style."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.9), sharey=False)
x = np.linspace(0, 0.8, 300)
# Mainland: centered at its mean (~0.09); demeaned predicted productivity
m_mean=0.09; xc=x-m_mean; y_main = 0.709*xc - 1.012*xc**2; y_main-=y_main.max()
ax=axes[0]; ax.plot(x*100, y_main, color='black', lw=2)
tp=0.43; ax.axvline(tp*100, color='0.55', ls='--', lw=1)
ax.annotate('điểm uốn ≈ 43%', xy=(tp*100, y_main.max()), xytext=(tp*100+6, y_main.max()-0.06),
            fontsize=8.5, color='0.3')
ax.set_title('(a) Lục địa — chế độ chuyển đổi (Nhóm IV)\nChữ U ngược: $\\beta_2=-1.012^{***}$', fontsize=9.5)
ax.set_xlabel('Cường độ xuất khẩu FSTS (%)', fontsize=9); ax.set_ylabel('Năng suất dự báo (tương đối)', fontsize=9)
# SIDS: M3 convex
s_mean=0.062; xs=x-s_mean; y_sids = -0.860*xs + 0.844*xs**2; y_sids-=y_sids.max()
ax=axes[1]; ax.plot(x*100, y_sids, color='black', lw=2)
mn=0.860/(2*0.844)+s_mean; ax.axvline(mn*100, color='0.55', ls=':', lw=1)
# shade the penalty zone (low-moderate, where most firms are)
ax.axvspan(0, mn*100, color='0.9')
ax.annotate('vùng phạt\n(đa số DN)', xy=(15, y_sids[int(15/0.8/100*300)]), xytext=(2, y_sids.min()+0.02),
            fontsize=8.5, color='0.3')
ax.set_title('(b) Pacific SIDS — có điều kiện năng lực (M3)\nChữ U xuôi: $\\beta_2=+0.844$ ($p_{wild}=.07$)', fontsize=9.5)
ax.set_xlabel('Cường độ xuất khẩu FSTS (%)', fontsize=9)
for ax in axes:
    ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=8)
fig.suptitle('Hình 4.7.1. Chữ U ngược đảo chiều ở biên cực đoan: lục địa (∩) so với Pacific SIDS (∪)', fontsize=10.5, y=1.04)
fig.tight_layout()
fig.savefig('p8/figures/p8_fig1_dissolution.png', dpi=200, bbox_inches='tight')
fig.savefig('thesis/figures/fig_4_7_1_sids_inversion.png', dpi=200, bbox_inches='tight')
print('saved p8/figures/p8_fig1_dissolution.png + thesis/figures/fig_4_7_1_sids_inversion.png')
