"""
Consolidate the underlying results data behind the empirical papers (P3–P9) into
a single Excel workbook for submission transparency. Sources ONLY the curated
result CSVs already produced by each paper's replication pipeline (turning points,
coefficients, moderator/robustness tables, P6 forest data). No raw microdata, no
recomputation, no fabrication — this script only gathers existing files.

Output: dist/figure_data/dissertation_results_data.xlsx
Run from project root: python3 scripts/build_results_data_workbook.py
"""
import os
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dist", "figure_data", "dissertation_results_data.xlsx")

# (sheet_name<=31 chars, relative path, short description)
SPEC = [
    ("P3_VNM_turning_points", "p3/replication/data/p3_R_turning_points.csv", "P3 Vietnam — turning points (inverted-U)"),
    ("P3_VNM_coefs",          "p3/replication/data/p3_R_coefs.csv",          "P3 Vietnam — regression coefficients"),
    ("P4_SGP_turning_points", "p4/replication/tables/p4_R_turning_points.csv", "P4 Singapore — turning points"),
    ("P4_SGP_coefs",          "p4/replication/tables/p4_R_coefs.csv",          "P4 Singapore — coefficients"),
    ("P4_SGP_robustness",     "p4/replication/tables/table_3_robustness.csv",  "P4 Singapore — robustness (Table 3)"),
    ("P5_CHN_turning_points", "p5/replication/results/p5_R_turning_points.csv", "P5 China — turning points (2 waves)"),
    ("P5_CHN_coefs",          "p5/replication/results/p5_R_coefs.csv",          "P5 China — coefficients"),
    ("P6_meta_forest_data",   "p6/results/forest_data.csv",                     "P6 meta — per-study effect sizes (k=238/K=288)"),
    ("P6_meta_baseline",      "p6/results/table1_baseline.csv",                 "P6 meta — three-level baseline"),
    ("P6_meta_ICRV",          "p6/results/table2_icrv.csv",                     "P6 meta — ICRV moderation"),
    ("P6_meta_cDAI",          "p6/results/table3_cdai.csv",                     "P6 meta — cDAI moderation"),
    ("P6_meta_DPL",           "p6/results/table4_dpl.csv",                      "P6 meta — DPL phase moderation"),
    ("P6_meta_sensitivity",   "p6/results/table5_sensitivity.csv",             "P6 meta — sensitivity/robustness"),
    ("P7_50econ_canonical",  "data_wbes/analysis/p7_50econ_models.csv",        "P7 capstone — CANONICAL 50-economy models + per-ICRV turning points (M2 N=81,022, TP 51.5%)"),
    ("P8_SIDS_coefs",         "p8/replication/reanalysis_7pacific/p8_7pacific_coefs.csv", "P8 Pacific SIDS — coefficients (FIP)"),
    ("P9_IND_turning_points", "p9_india/replication/results/p9_india_turning_points.csv", "P9 India — turning points"),
    ("P9_IND_coefs",          "p9_india/replication/results/p9_india_coefs_main_models.csv", "P9 India — main-model coefficients"),
    ("P9_IND_moderators",     "p9_india/replication/results/p9_india_moderators.csv", "P9 India — moderators"),
]

readme_rows, written = [], []
with pd.ExcelWriter(OUT, engine="openpyxl") as xw:
    # placeholder; README written after we know which sheets succeeded
    for sheet, rel, desc in SPEC:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"[skip] missing: {rel}")
            continue
        df = pd.read_csv(path)
        df.to_excel(xw, sheet_name=sheet[:31], index=False)
        readme_rows.append({"Sheet": sheet[:31], "Paper": sheet.split("_")[0],
                            "Mô tả": desc, "Nguồn (file)": rel, "Số dòng": len(df)})
        written.append(sheet)
    readme = pd.DataFrame(readme_rows)[["Sheet", "Paper", "Mô tả", "Nguồn (file)", "Số dòng"]]
    readme.to_excel(xw, sheet_name="README", index=False)

# move README to front
import openpyxl
wb = openpyxl.load_workbook(OUT)
wb.move_sheet("README", -(len(wb.sheetnames) - 1))
wb.save(OUT)
print(f"\nSaved: {os.path.relpath(OUT, ROOT)}  ({len(written)} data sheets + README)")
