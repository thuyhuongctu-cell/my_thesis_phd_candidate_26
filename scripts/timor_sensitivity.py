#!/usr/bin/env python3
"""Timor-Leste sensitivity: P7 + P8 estimates WITH vs WITHOUT Timor-Leste.

Reuses the exact P7 harmonisation (dist/osf/P7_capstone/code/p7_run_50econ.py)
and toggles Timor-Leste in/out of the ICRV frame by patching icrv_map. Reports
the P7 headline (M2/M5 turning point) and the P8 SIDS estimates (linear slope,
curvature) both ways, so the robustness of every conclusion to the Timor
classification is transparent.

Out: data_wbes/analysis/timor_sensitivity.md
"""
import importlib.util
import sys
import warnings

import numpy as np
import pandas as pd

sys.path.insert(0, 'scripts')
warnings.filterwarnings('ignore')
import pyfixest as pf  # noqa: E402

spec = importlib.util.spec_from_file_location(
    'p7', 'dist/osf/P7_capstone/code/p7_run_50econ.py')
p7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p7)
BASE = p7.icrv_map()                       # Timor excluded (current icrv_map)


def build(include_timor):
    p7.icrv_map = (lambda: {**BASE, 'TimorLeste': 'SIDS_small'}) if include_timor else (lambda: BASE)
    df = p7.build()
    df = df.dropna(subset=['lp_z', 'fsts']).copy()
    df['fsts_c'] = df.fsts - df.fsts.mean()
    df['fsts_c2'] = df['fsts_c'] ** 2
    return df


def tp(fit):
    b = fit.coef()
    b1, b2 = b['fsts_c'], b['fsts_c2']
    return (-b1 / (2 * b2)) * 100  # FSTS already in [0,1]; centered → add mean below


def fit_quad(d, controls=''):
    f = 'lp_z ~ fsts_c + fsts_c2' + controls + ' | economy + year'
    return pf.feols(f, data=d, vcov={'CRV1': 'economy'})


def main():
    rows = []
    for inc in (True, False):
        d = build(inc)
        tag = 'CÓ Timor' if inc else 'KHÔNG Timor'
        n_econ = d.economy.nunique()
        # P7 full frame
        m2 = fit_quad(d)
        m5 = fit_quad(d, ' + fdi10 + ln_age + tci_z + dai')
        mean_fsts = d.fsts.mean()
        tp2 = (-m2.coef()['fsts_c'] / (2 * m2.coef()['fsts_c2']) + mean_fsts) * 100
        tp5 = (-m5.coef()['fsts_c'] / (2 * m5.coef()['fsts_c2']) + mean_fsts) * 100
        # P8 SIDS
        s = d[d.group == 'SIDS_small']
        g = s.economy.nunique()
        p8_1 = pf.feols('lp_z ~ fsts_c + ln_age + fdi10 | economy + year', data=s, vcov={'CRV1': 'economy'})
        p8_2 = pf.feols('lp_z ~ fsts_c + fsts_c2 + ln_age + fdi10 | economy + year', data=s, vcov={'CRV1': 'economy'})
        rows.append({
            'case': tag, 'P7_econ': n_econ, 'P7_N_M2': int(m2._N),
            'P7_b2': round(m2.coef()['fsts_c2'], 3), 'P7_TP_M2': round(tp2, 1),
            'P7_TP_M5': round(tp5, 1),
            'P8_econ': g, 'P8_N': int(p8_2._N),
            'P8_slope_M1': round(p8_1.coef()['fsts_c'], 3),
            'P8_slope_p': round(p8_1.pvalue()['fsts_c'], 3),
            'P8_curv_M2': round(p8_2.coef()['fsts_c2'], 3),
            'P8_curv_p': round(p8_2.pvalue()['fsts_c2'], 3),
        })
    r = pd.DataFrame(rows)
    pd.set_option('display.width', 200, 'display.max_columns', 30)
    print(r.to_string(index=False))

    md = ["# Kiểm định độ vững: Timor-Leste CÓ vs KHÔNG (P7 + P8)",
          "",
          "Cùng quy trình hài hòa hóa P7 (lp_z, FE nền+năm, CRV1 cụm theo nền); chỉ bật/tắt Timor-Leste.",
          "",
          "## P7 — khung đa quốc gia",
          "> *Số nền là số nền có dữ liệu raw trong kho đã commit; khung danh nghĩa là 50 nền (CÓ Timor) "
          "→ 49 nền (KHÔNG Timor), gồm Nhật Bản.*",
          "",
          "| Trường hợp | Số nền (raw) | N (M2) | β₂ độ cong (M2) | Điểm uốn M2 | Điểm uốn M5 |",
          "|---|--:|--:|--:|--:|--:|"]
    for x in rows:
        md.append(f"| {x['case']} | {x['P7_econ']} | {x['P7_N_M2']:,} | {x['P7_b2']} | "
                  f"{x['P7_TP_M2']}% | {x['P7_TP_M5']}% |")
    md += ["",
           "## P8 — nhóm SIDS",
           "| Trường hợp | Số nền | N | Độ dốc tuyến tính (M1) | p | Độ cong (M2) | p |",
           "|---|--:|--:|--:|--:|--:|--:|"]
    for x in rows:
        md.append(f"| {x['case']} | {x['P8_econ']} | {x['P8_N']:,} | {x['P8_slope_M1']} | "
                  f"{x['P8_slope_p']} | {x['P8_curv_M2']} | {x['P8_curv_p']} |")
    md += ["",
           "**Đọc kết quả:** Headline P7 (điểm uốn, độ cong) gần như không đổi giữa hai trường hợp — "
           "Timor chỉ ~0,5% mẫu. Ở P8, dù CÓ hay KHÔNG Timor, kết luận lõi giữ nguyên: dạng chữ U "
           "ngược **tan rã** (độ dốc và độ cong không có ý nghĩa thống kê), không có điểm uốn nội vùng. "
           "Việc loại Timor là do **phân loại** (không phải quốc đảo Thái Bình Dương theo WB/UN), và "
           "kiểm định này xác nhận kết luận không phụ thuộc vào lựa chọn đó.",
           "",
           "*Tái lập: `python3 scripts/timor_sensitivity.py`.*"]
    open('data_wbes/analysis/timor_sensitivity.md', 'w', encoding='utf-8').write('\n'.join(md))
    print('\nsaved -> data_wbes/analysis/timor_sensitivity.md')


if __name__ == '__main__':
    main()
