"""Dựng workbook kết quả riêng cho P9 (Ấn Độ) và P10 (Nhật Bản), đồng bộ
với định dạng P3..P8 (mỗi sheet = 1 bảng kết quả + sheet README mô tả nguồn).

Chỉ gom các CSV kết quả ĐÃ CÓ trong pipeline tái lập của từng paper — không
tính lại, không bịa số. Output:
  p9_india/replication/P9_results_workbook.xlsx
  p10_japan/replication/P10_results_workbook.xlsx

Chạy:  python3 scripts/build_p9_p10_workbooks.py
"""
import os
import pandas as pd
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# paper -> (output path, [(sheet<=31, rel csv, description)])
SPECS = {
    "P9": (
        "p9_india/replication/P9_results_workbook.xlsx", [
            ("P9_REPRO_estimates",     "p9_india/replication/REPRO_2026-06-23/estimates.csv", "Estimates tái lập (REPRO 2026-06-23)"),
            ("P9_coefs_main",          "p9_india/replication/results/p9_india_coefs_main_models.csv", "Hệ số mô hình chính (3 đợt 2014/2022/2025)"),
            ("P9_turning_points",      "p9_india/replication/results/p9_india_turning_points.csv", "Điểm uốn theo đợt (61,8 → 40,7 → tan biến)"),
            ("P9_uTest",               "p9_india/replication/results/p9_india_uTest.csv", "Lind–Mehlum U-test theo đợt"),
            ("P9_paternoster",         "p9_india/replication/results/p9_india_paternoster.csv", "Paternoster HC1"),
            ("P9_paternoster_cluster", "p9_india/replication/results/p9_india_paternoster_cluster.csv", "Paternoster cụm theo bang"),
            ("P9_moderators",          "p9_india/replication/results/p9_india_moderators.csv", "Điều tiết TCI/DAI"),
            ("P9_robustness",          "p9_india/replication/results/p9_india_robustness.csv", "Kiểm định độ vững"),
            ("P9_descriptives",        "p9_india/replication/results/p9_india_descriptives.csv", "Thống kê mô tả"),
            ("P9_3wave_pooled",        "p9_india/replication/results/p9_india_3wave_pooled.csv", "Mô hình gộp 3 đợt"),
        ]),
    "P10": (
        "p10_japan/replication/P10_results_workbook.xlsx", [
            ("P10_REPRO_estimates", "p10_japan/replication/REPRO_2026-06-23/estimates.csv", "Estimates tái lập + đối chiếu canonical (M1/M2, export premium, mô tả Bảng 1; N=2.168)"),
        ]),
}


def build(out_rel, spec):
    out = os.path.join(ROOT, out_rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    rows, written = [], []
    with pd.ExcelWriter(out, engine="openpyxl") as xw:
        for sheet, rel, desc in spec:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                print(f"[skip] missing: {rel}")
                continue
            df = pd.read_csv(path)
            df.to_excel(xw, sheet_name=sheet[:31], index=False)
            rows.append({"Sheet": sheet[:31], "Mô tả": desc,
                         "Nguồn (file)": rel, "Số dòng": len(df), "Số cột": df.shape[1]})
            written.append(sheet)
        pd.DataFrame(rows)[["Sheet", "Mô tả", "Nguồn (file)", "Số dòng", "Số cột"]] \
            .to_excel(xw, sheet_name="README", index=False)
    wb = openpyxl.load_workbook(out)
    wb.move_sheet("README", -(len(wb.sheetnames) - 1))
    wb.save(out)
    print(f"Saved: {out_rel}  ({len(written)} data sheets + README)")


if __name__ == "__main__":
    for _pid, (out_rel, spec) in SPECS.items():
        build(out_rel, spec)
    print("DONE")
