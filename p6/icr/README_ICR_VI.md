# Hướng dẫn mã hóa kép P6 (Inter-Coder Reliability) — dành cho Coder 2

**Mục đích:** điền 6 ô `[insert after dual-coding]` trong Bảng 3.1 của P6 (4 package) bằng số liệu **thật** từ mã hóa kép. Protocol theo Mục 3.3.2 bản thảo: 2 tác giả mã hóa độc lập **20% stratified subsample (k = 47 studies)**, mù lẫn nhau, bất đồng giải quyết bằng thảo luận.

## Quy trình 4 bước

### Bước 1 — Đã xong (máy đã rút mẫu)
`01_draw_icr_subsample.py` đã rút **47 nghiên cứu** (seed 2026, phân tầng theo ICRV: I=21, III=16, MX=5, II=4, FR=1) từ 238 nghiên cứu:
- `icr_subsample_master.csv` — mã của Coder 1 (NCS/PI), lấy từ database hiện hành. **Coder 2 KHÔNG được xem file này.**
- `icr_coding_sheet_coder2_BLANK.csv` — phiếu trống cho Coder 2.

### Bước 2 — Coder 2 (thầy Tú) mã hóa
**Khuyến nghị:** mở `icr_coding_sheet_coder2_BLANK.xlsx` — phiếu Excel có **dropdown** (chỉ chọn
giá trị hợp lệ, ô vàng = cần điền, kèm sheet *Codebook*). Lưu thành `icr_coding_sheet_coder2_FILLED.xlsx`.
*(Phương án thay thế: bản CSV `icr_coding_sheet_coder2_BLANK.csv` → lưu `..._FILLED.csv`. Script
`02_compute_icr.py` đọc được cả .xlsx lẫn .csv. Công thức κ/ICC: xem `CONG_THUC_KAPPA_ICC_VI.md`.)*

Với từng nghiên cứu (đọc bài gốc/abstract), điền 5 cột theo codebook:

| Cột | Giá trị hợp lệ | Ý nghĩa |
|---|---|---|
| `icrv` | `I` / `II` / `III` / `FR` / `MX` | Chế độ thể chế ICRV của mẫu nghiên cứu |
| `dpl` | `PRE` / `SPN` / `FOL` | Pha Digital Paradox Lifecycle của giai đoạn mẫu |
| `doi_type` | `FSTS` / `GEO` / `EXP` / `FDI` / `COMP` / `OTH` | Thước đo mức độ quốc tế hóa |
| `fp_type` | `ACC` / `MKT` / `LAB` / `MIX` | Thước đo hiệu quả doanh nghiệp |
| `cdai` | `L` / `M` / `H` | Mức cDAI (bối cảnh số) của quốc gia-thời kỳ |

Lưu thành **`icr_coding_sheet_coder2_FILLED.csv`** (cùng thư mục). Không để ô trống.

### Bước 3 — Tính ICR
```bash
python3 p6/icr/02_compute_icr.py
```
Script in bảng κ cho 4 biến categorical + κ (unweighted & linear-weighted) cho `cdai` ordinal, kèm danh sách nghiên cứu bất đồng. **Script từ chối chạy nếu phiếu Coder 2 thiếu/không đầy đủ** — không thể tạo số liệu từ dữ liệu khống.

### Bước 4 — Điền vào bản thảo
Chép giá trị κ vào 6 ô `[insert after dual-coding]` trong `01_manuscript_blinded.md` của **cả 4 package** (jwb/jim/apjm/ibr) + bản VI, rồi regenerate docx. Bất đồng giải quyết bằng thảo luận và cập nhật database nếu cần (ghi chú vào cột notes).

## ⚠️ 3 điểm lệch bản thảo ↔ database — tác giả cần quyết trước khi nộp

1. **DOI measure:** bản thảo ghi *"Categorical (4)"* nhưng database có **6** giá trị (`FSTS/GEO/EXP/FDI/COMP/OTH`). đến Sửa bản thảo thành "(6)" hoặc nêu rõ cách gộp về 4 nhóm.
2. **cDAI:** bản thảo ghi *"Continuous (0–1), ICC(2,1)"* nhưng database lưu **ordinal H/M/L**. đến Hoặc bổ sung cột điểm liên tục 0–1 (khi đó script tự tính ICC(2,1)), hoặc sửa dòng Bảng 3.1 thành "Ordinal (3), weighted κ".
3. **Industry sector:** bản thảo có dòng *"Industry sector, Categorical (3)"* nhưng database **không có cột industry**. đến Hoặc bổ sung cột và mã hóa, hoặc bỏ dòng này khỏi Bảng 3.1.

*(Cả 3 đều là lệch mô tả, không ảnh hưởng kết quả meta-analysis; nhưng reviewer sẽ bắt nếu Bảng 3.1 không khớp dữ liệu công bố.)*
