#!/usr/bin/env python3
"""P8 Figure 1: the inverted-U dissolves at the periphery.
Mainland transition (P7 Lower-mid): concave inverted-U (beta1=+0.709, beta2=-1.012).
Pacific SIDS (M3, capability-conditioned): only a suggestive, marginal positive
curvature (beta1=-0.860, beta2=+0.844, p_wild=.07) — presented as a hint of a
convex pattern, not a confirmed reversal. Monochrome, journal style.
Outputs VN (thesis) and EN (submission package) versions."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

LABELS = {
    'vi': {
        'xlabel': 'Cường độ xuất khẩu FSTS (%)',
        'ylabel': 'Năng suất dự báo (tương đối)',
        'tp': 'điểm uốn ≈ 43%',
        'zone': 'vùng phạt\n(đa số DN)',
        'title_a': '(a) Lục địa — chế độ chuyển đổi (Nhóm IV)\nChữ U ngược: $\\beta_2=-1.012^{***}$',
        'title_b': '(b) Pacific SIDS — có điều kiện năng lực (M3)\n'
                   'Độ cong dương ở mức biên (gợi ý): $\\beta_2=+0.844$ ($p_{wild}=.07$)',
        'suptitle': 'Hình 4.7.1. Sự tan rã của chữ U ngược ở biên cực đoan: '
                    'lục địa (∩) so với Pacific SIDS (độ cong không có ý nghĩa)',
    },
    'en': {
        'xlabel': 'Export intensity FSTS (%)',
        'ylabel': 'Predicted productivity (relative)',
        'tp': 'turning point ≈ 43%',
        'zone': 'penalty zone\n(most firms)',
        'title_a': '(a) Mainland — transition regime (Group IV)\nInverted-U: $\\beta_2=-1.012^{***}$',
        'title_b': '(b) Pacific SIDS — capability-conditioned (M3)\n'
                   'Suggestive marginal convexity: $\\beta_2=+0.844$ ($p_{wild}=.07$)',
        'suptitle': 'Figure 1. The inverted-U dissolves at the periphery: '
                    'mainland (∩) vs Pacific SIDS (curvature not significant)',
    },
}


def render(lang, outpaths):
    L = LABELS[lang]
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.9), sharey=False)
    x = np.linspace(0, 0.8, 300)
    # Mainland: centered at its mean (~0.09); demeaned predicted productivity
    m_mean = 0.09
    xc = x - m_mean
    y_main = 0.709 * xc - 1.012 * xc ** 2
    y_main -= y_main.max()
    ax = axes[0]
    ax.plot(x * 100, y_main, color='black', lw=2)
    tp = 0.43
    ax.axvline(tp * 100, color='0.55', ls='--', lw=1)
    ax.annotate(L['tp'], xy=(tp * 100, y_main.max()),
                xytext=(tp * 100 + 6, y_main.max() - 0.06), fontsize=8.5, color='0.3')
    ax.set_title(L['title_a'], fontsize=9.5)
    ax.set_xlabel(L['xlabel'], fontsize=9)
    ax.set_ylabel(L['ylabel'], fontsize=9)
    # SIDS: M3 suggestive convex (capability-conditioned)
    s_mean = 0.062
    xs = x - s_mean
    y_sids = -0.860 * xs + 0.844 * xs ** 2
    y_sids -= y_sids.max()
    ax = axes[1]
    ax.plot(x * 100, y_sids, color='black', lw=2)
    mn = 0.860 / (2 * 0.844) + s_mean
    ax.axvline(mn * 100, color='0.55', ls=':', lw=1)
    # shade the penalty zone (low-moderate, where most firms are)
    ax.axvspan(0, mn * 100, color='0.9')
    ax.annotate(L['zone'], xy=(15, y_sids[int(15 / 0.8 / 100 * 300)]),
                xytext=(2, y_sids.min() + 0.02), fontsize=8.5, color='0.3')
    ax.set_title(L['title_b'], fontsize=9.5)
    ax.set_xlabel(L['xlabel'], fontsize=9)
    for ax in axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(labelsize=8)
    fig.suptitle(L['suptitle'], fontsize=10.5, y=1.04)
    fig.tight_layout()
    for p in outpaths:
        fig.savefig(p, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print('saved ' + ', '.join(outpaths))


render('vi', ['p8/figures/p8_fig1_dissolution.png',
              'thesis/figures/fig_4_7_1_sids_inversion.png'])
render('en', ['p8/figures/p8_fig1_dissolution_en.png',
              'p8/submission/world_development_redesign/figures/p8_fig1_dissolution_en.png'])
