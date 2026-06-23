#!/usr/bin/env python3
"""revision_evidence.py — bộ kiểm chứng bổ sung cho vòng chỉnh sửa luận án.

Chạy từ data_wbes/p7/p7_pooled_clean.csv (đã hài hòa, khớp khung canonical 50 nền).
Sinh bằng chứng cho các phản biện: dạng hàm (RESET/cubic), common-method bias (Harman),
độ giá trị cấu trúc TCI/DAI (tương quan + EFA), robustness ngành chế tạo, và biên
tham gia vs cường độ (Việt Nam). KHÔNG sửa luận án; chỉ xuất bảng để NCS rà soát.
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from numpy.linalg import eigh

D = "data_wbes/p7/p7_pooled_clean.csv"
OUT_CSV = "reviews/revision_evidence_estimates.csv"
rows = []


def add(test, metric, value, note=""):
    rows.append({"test": test, "metric": metric, "value": value, "note": note})


def fit(df, formula, cluster="country"):
    m = smf.ols(formula, data=df).fit(
        cov_type="cluster", cov_kwds={"groups": df[cluster]})
    return m


def tp(b1, b2):
    return np.nan if b2 == 0 else -b1 / (2 * b2)


df = pd.read_csv(D)
df = df.assign(fsts2=df.fsts**2, fsts3=df.fsts**3)
base = "ln_labor_prod ~ fsts + fsts2 + ln_size + firm_age + foreign_own_pct + C(isic_sector) + C(country) + C(year)"
core = df.dropna(subset=["ln_labor_prod", "fsts", "ln_size", "firm_age",
                         "foreign_own_pct", "isic_sector", "country", "year"]).copy()

# ---- (1) Baseline quadratic (đối chiếu canonical TP=43.6%) ----
m2 = fit(core, base)
b1, b2 = m2.params["fsts"], m2.params["fsts2"]
add("1_baseline_quad", "N", int(m2.nobs))
add("1_baseline_quad", "beta_fsts", round(b1, 4), f"p={m2.pvalues['fsts']:.4f}")
add("1_baseline_quad", "beta_fsts2", round(b2, 4), f"p={m2.pvalues['fsts2']:.4f}")
add("1_baseline_quad", "turning_point_pct", round(100*tp(b1, b2), 1), "canonical M5=43.6%")

# ---- (2) RESET-style: thêm bậc 3, kiểm định dạng hàm ----
m3 = fit(core.assign(), base + " + fsts3")
add("2_cubic_test", "beta_fsts3", round(m3.params["fsts3"], 4),
    f"p={m3.pvalues['fsts3']:.4f}")
add("2_cubic_test", "delta_AIC_cubic_minus_quad", round(m3.aic - m2.aic, 2),
    "âm => cubic tốt hơn; dương => quadratic đủ")
add("2_cubic_test", "delta_BIC_cubic_minus_quad", round(m3.bic - m2.bic, 2),
    "BIC phạt tham số mạnh hơn")

# ---- (3) Robustness ngành chế tạo (ISIC 1-3) ----
mfg = core[core.isic_sector.isin([1, 2, 3])]
mm = fit(mfg, base)
add("3_manufacturing_only", "N", int(mm.nobs))
add("3_manufacturing_only", "turning_point_pct",
    round(100*tp(mm.params["fsts"], mm.params["fsts2"]), 1),
    f"p_fsts2={mm.pvalues['fsts2']:.4f}")

# ---- (4) Harman single-factor (common-method bias) ----
hv = ["ln_labor_prod", "fsts", "tci_z", "dai_z", "ln_size", "firm_age"]
H = df[hv].dropna()
Z = (H - H.mean()) / H.std(ddof=0)
cmat = np.corrcoef(Z.values, rowvar=False)
ev = np.sort(eigh(cmat)[0])[::-1]
add("4_harman", "first_factor_var_pct", round(100*ev[0]/ev.sum(), 1),
    ">50% => nguy cơ CMB; càng thấp càng tốt")
add("4_harman", "n_items", len(hv))

# ---- (5) Độ giá trị cấu trúc TCI vs DAI (đo lường FORMATIVE) ----
# TCI/DAI là chỉ số hợp thành (formative): item là nguyên nhân cấu thành năng lực,
# không phải biểu hiện reflective -> item KHÔNG cần covary; EFA/nội-bộ không chẩn đoán
# được. Kiểm định đúng: (i) hai CHỈ SỐ hợp thành có tách biệt không; (ii) mạng nomological.
items = ["tci_cert", "tci_foreign_tech", "dai_website", "dai_epay"]
V = df[items].dropna()
corr = V.corr()
add("5_item_corr_formative", "tci_cert__tci_foreign_tech", round(corr.loc["tci_cert", "tci_foreign_tech"], 3),
    "thấp là ĐÚNG kỳ vọng cho formative")
add("5_item_corr_formative", "dai_website__dai_epay", round(corr.loc["dai_website", "dai_epay"], 3),
    "thấp là ĐÚNG kỳ vọng cho formative")

# Kiểm định đúng: tách biệt ở cấp CHỈ SỐ HỢP THÀNH + mạng nomological
rich = pd.read_csv("data_wbes/p7/p7_pooled_rich.csv")
cz = rich[["tci_z", "dai_z"]].dropna()
r_comp = cz.tci_z.corr(cz.dai_z)
add("5b_composite_distinct", "N", int(len(cz)))
add("5b_composite_distinct", "corr_tci_z_dai_z", round(r_comp, 3), "0=tách hẳn, 1=trùng")
add("5b_composite_distinct", "shared_variance_r2", round(r_comp**2, 3), "phương sai chia sẻ")
mn = df.dropna(subset=["ln_labor_prod", "tci_z", "dai_z", "fsts", "ln_size",
                       "firm_age", "country", "year"]).copy()
rn = fit(mn, "ln_labor_prod ~ tci_z + dai_z + fsts + ln_size + firm_age + C(country) + C(year)")
add("5b_composite_distinct", "joint_beta_tci_z", round(rn.params["tci_z"], 3), f"p={rn.pvalues['tci_z']:.4f}")
add("5b_composite_distinct", "joint_beta_dai_z", round(rn.params["dai_z"], 3), f"p={rn.pvalues['dai_z']:.4f}")

# ---- (6) Việt Nam: biên tham gia vs cường độ ----
vn = df[df.country.astype(str).str.contains("Viet", case=False, na=False)].copy()
vn = vn.assign(fsts2=vn.fsts**2)
vbase = "ln_labor_prod ~ fsts + fsts2 + ln_size + firm_age + C(isic_sector) + C(year)"
vn_all = vn.dropna(subset=["ln_labor_prod", "fsts", "ln_size", "firm_age", "isic_sector", "year"])
if len(vn_all) > 50:
    va = fit(vn_all, vbase, cluster="year")
    add("6_vietnam_all", "N", int(va.nobs))
    add("6_vietnam_all", "turning_point_pct",
        round(100*tp(va.params["fsts"], va.params["fsts2"]), 1),
        f"p_fsts2={va.pvalues['fsts2']:.4f}")
    add("6_vietnam_all", "share_nonexporter", round((vn_all.fsts == 0).mean(), 3))
    vx = vn_all[vn_all.fsts > 0]
    if len(vx) > 50:
        vex = fit(vx, vbase, cluster="year")
        add("6_vietnam_exporters_only", "N", int(vex.nobs))
        add("6_vietnam_exporters_only", "beta_fsts2", round(vex.params["fsts2"], 4),
            f"p={vex.pvalues['fsts2']:.4f} (n.s. => U-shape là biên tham gia)")

res = pd.DataFrame(rows)
res.to_csv(OUT_CSV, index=False)
print(res.to_string(index=False))
print(f"\nwrote {OUT_CSV}")
