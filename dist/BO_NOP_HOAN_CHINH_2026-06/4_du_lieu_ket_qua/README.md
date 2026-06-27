# 4. Dữ liệu & kết quả (replication)

Thư mục này gom **dữ liệu nguồn, kết quả ước lượng, hình/bảng và mã** để hội đồng
kiểm chứng (reproducibility) các con số trong papers và luận án.

## `ket_qua_excel/` — Excel kết quả
- `P3..P8_results_workbook.xlsx` — workbook kết quả từng paper (hệ số ước lượng,
  turning point, kiểm định, dữ liệu hình/bảng). *(P9/P10: kết quả nằm trong
  `ALL_PAPERS_results_data.xlsx` và `dissertation_results_data.xlsx`.)*
- `ALL_PAPERS_results_data.xlsx` — tổng hợp kết quả 8 paper P3–P10.
- `MASTER_du_lieu_luan_an.xlsx` / `dissertation_results_data.xlsx` — số liệu luận án.
- `chuong3_phuong_phap_tables.xlsx`, `chuong4_ket_qua_data.xlsx`, `cd2_tables.xlsx`
  — dữ liệu bảng của các chương/chuyên đề.

## `p7_du_lieu_gop_50_nuoc/` — file gộp 50 nền cho P7 (capstone)
- `p7_pooled_clean.csv` (**~21 MB**) — bảng phân tích đã **gộp toàn bộ 50 nền /
  103 sóng WBES (88.869 DN)**, là dữ liệu master để ước lượng P7 (M2 N=81.022;
  TP 51,5% → 43,6%). Sinh bằng `p7/replication/01_build_p7_dataset.py`.
- `p7_manifest.csv` — danh mục nước/sóng đưa vào gộp.
- `p7_variable_log.csv` — nhật ký định nghĩa biến.
- Chạy mô hình: `p7/replication/02_run_p7_models.py` (hoặc `scripts/p7_run_50econ.py`).
  Số khóa: `data_wbes/analysis/CANONICAL_NUMBERS.md`.

## `ma_stata_do/` — mã Stata (.do)
Do-file build dữ liệu + chạy mô hình cho **P3, P4, P5, P9** (`p*/replication/do/`)
và **P7, P8** (`scripts/stata/`: tái ước lượng P7, wild-cluster bootstrap & FIP cho
SIDS). *(P6 meta-analysis và P10 dùng Python: `scripts/p6_meta_analysis.py`,
`p10_japan/replication/p10_japan_models.py`.)* Tên file phẳng theo dạng
`đường__dẫn__gốc.do` để truy nguyên về repo.

> Dữ liệu thô WBES (.dta) **không** đính kèm (dung lượng lớn, tải công khai từ
> World Bank Enterprise Surveys). Đường dẫn build: `data_wbes/raw_dta/`.
> Đối chiếu chéo Python↔Stata: `reviews/REPLICATION_CROSSCHECK_2026-06-23.md`.
