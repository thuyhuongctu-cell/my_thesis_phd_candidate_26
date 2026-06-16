# Hướng dẫn L2 Screening & Extraction — P6 Meta-Analysis

**Cập nhật**: 20/05/2026 (rev 2)
**File làm việc (canonical)**: `p6/tools/results/fulltext_to_extraction_tracker_v3.csv`  
**Cấu trúc**: 2,467 rows × 58 cột  
**File extraction queue** (652 Y, sorted by PDF status): `p6/tools/results/extraction_queue_y_20260520.csv`

---

## Trạng thái pipeline (20/05/2026 — sau auto-screen L2)

| Nhóm | Số lượng | Ghi chú |
|------|---------|---------|
| Existing coded (k=238 database) | 344 rows | seq ≤ 435 |
| New candidates tổng | 2,123 rows | seq > 435 |
| **Y (confirmed + auto-Y)** | **652** | sẵn sàng extraction |
| đến có local PDF | 78 | chạy `41_auto_extract_from_pdfs.py` ngay |
| đến có repo URL | 55 | tải thủ công + extract |
| đến không PDF | 519 | cần tìm PDF |
| N (auto-exclude) | 9 | meta-analyses, reviews, wrong-field |
| UNSURE (cần full-text) | 1,403 | đọc thủ công từng paper |
| blank | 0 | — |

**PDF coverage (sau Unpaywall + chờ S2):**
- Unpaywall: 78 PDF trực tiếp + 55 repo URL
- Semantic Scholar fallback: chạy từ GitHub Actions (263 papers còn lại)

**Scripts pipeline:**
```
40_batch_download_pdfs.py   — tải PDF về p6/pdfs/ (chạy local)
41_auto_extract_from_pdfs.py — auto-extract r từ PDF (chạy local sau 40)
44_auto_screen_l2_titles.py  — auto-screen blank rows (đã chạy)
45_export_extraction_queue.py — xuất queue Y papers (đã chạy)
42_merge_tracker_to_database.py — merge → database (khi ≥50 ready_for_r=1)
```

---

## Bước 1: Mở file làm việc

```
extraction_queue_y_20260520.csv  (652 Y rows, sorted by PDF status — dễ làm việc)
  ↕ sync từ/về ↕
fulltext_to_extraction_tracker_v3.csv  (toàn bộ 2,467 rows — canonical)
```

**Cách làm**: Mở `extraction_queue_y_20260520.csv` trong Excel. Bắt đầu từ `LOCAL_PDF` rows (78 papers). Điền vào các cột extraction. Sau khi xong một batch, copy kết quả về `tracker_v3.csv` (dùng `seq` làm key).

**Check nhanh tiến độ:**
```bash
python3 -c "
import csv
with open('p6/tools/results/fulltext_to_extraction_tracker_v3.csv') as f:
    rows = list(csv.DictReader(f))
ready = sum(1 for r in rows if r.get('ready_for_r','').strip() == '1')
r_done = sum(1 for r in rows if r.get('converted_r','').strip())
y = sum(1 for r in rows if r.get('fulltext_screening_decision','') == 'Y')
print(f'Y={y} | converted_r={r_done} | ready_for_r={ready}')
"
```

---

## Bước 2: Tiêu chí INCLUDE / EXCLUDE (L2 — 5 câu hỏi)

Trả lời tất cả 5 — **bất kỳ NO = EXCLUDE**:

| # | Câu hỏi | YES = tiếp tục | NO = loại ngay |
|---|---------|---------------|----------------|
| 1 | Unit of analysis là firm-level? | doanh nghiệp, nhà máy, SME | quốc gia, ngành, cá nhân |
| 2 | Có đo lường internationalization? | FSTS, DOI, export intensity, FDI, số quốc gia | không có I variable |
| 3 | Có đo lường firm performance? | ROA, ROE, Tobin's Q, productivity, sales growth | không có P variable |
| 4 | Có quan hệ I–P định lượng? | r, β, t, F, hoặc có thể tính r | chỉ mô tả, không có statistics |
| 5 | Peer-reviewed journal article? | có DOI hoặc ISSN | dissertation, book chapter, WP, conference |

### Red flags — loại ngay không cần đọc thêm

- `country-level / national-level analysis` đến loại (macro-level)
- `antecedents of internationalization` / `determinants of export` đến loại (I là DV, không phải P)
- `qualitative study` / `case study` đến loại
- `meta-analysis` / `systematic review` đến loại (không phải primary study)
- health, environment, education outcomes đến loại (off-domain)

---

## Bước 3: Trích xuất Effect Size (chỉ papers Y)

### Thứ tự ưu tiên lấy r

| Ưu tiên | Nguồn | Công thức | Ghi vào `conversion_formula` |
|---------|-------|-----------|------------------------------|
| 1 | Pearson r trực tiếp | r as-is | `direct` |
| 2 | Partial correlation | r as-is | `direct` + `is_partial=1` |
| 3 | Standardized β OLS/panel | r ≈ β | `beta` |
| 4 | t-statistic + df | r = t / √(t² + df) | `t_to_r` |
| 5 | F-stat (df₁=1) + N | r = √(F / (F + df_err)) | `F_to_r` |
| 6 | p-value + N | r via t-distribution (conservative) | `p_to_r` |

```
# Công thức Excel:
converted_r (từ t):  =t_value/SQRT(t_value^2 + df_for_t)
converted_r (từ F):  =SQRT(reported_coefficient/(reported_coefficient + sample_size_n - 2))
fisher_z:            =0.5*LN((1+converted_r)/(1-converted_r))
variance_z:          =1/(sample_size_n - 3)
```

### Nonlinear (inverted-U / U-shape)

- Điền `converted_r` = r từ linear term (β₁)
- Điền `curve_type` = `inverted_U` hoặc `U_shape`
- Ghi turning point vào `notes_for_extractor`: `TP = -β₁/(2β₂) = XX%`
- `effect_direction` = `nonlinear`

### Multiple effects từ 1 paper

Tạo thêm row trong tracker với cùng `authors + year`, khác `effect_size_type`.  
Ghi vào `notes_for_extractor`: `E1=ROA, E2=TobinQ`

---

## Bước 4: Coding Moderators

### ICRV (cột `icrv`) — Integer 1–6 hoặc 0

> Dựa trên quốc gia của **mẫu doanh nghiệp** (không phải destination market)

| Mã | Regime | Quốc gia ví dụ |
|----|--------|---------------|
| 1 | Advanced | Singapore, HK, Đài Loan, Hàn Quốc, Nhật, Úc, NZ, Israel, EU phát triển |
| 2 | Upper-Middle / Emerging Strong | Trung Quốc, Malaysia, Thái Lan, Brazil, Mexico, Thổ Nhĩ Kỳ, Nam Phi |
| 3 | Lower-Middle / Emerging Weak | Việt Nam, Ấn Độ, Indonesia, Philippines, Pakistan, Bangladesh |
| 4 | Resource-rich / GCC | Saudi Arabia, UAE, Qatar, Kuwait, Kazakhstan, Angola |
| 5 | SIDS | Fiji, PNG, Samoa, Tonga, Malta, Mauritius, Maldives |
| 6 | Frontier / LDC | Myanmar, Cambodia, Lào, Nepal, Ethiopia, Mozambique |
| 0 | Multi-country Mixed | Nhiều quốc gia khác regime đến dùng 0 |

**Đã pre-fill 38%** (202/538) — kiểm tra và điền phần còn lại khi đọc full-text.

### DPL (cột `dpl`) — **Đã pre-fill 100%** từ publication year

| Mã | Phase | Năm |
|----|-------|-----|
| 1 | Pre-digital | data midpoint < 2000 |
| 2 | Early digital | data midpoint 2000–2009 |
| 3 | Platform era | data midpoint ≥ 2010 |

> **Ưu tiên dùng năm thu thập dữ liệu** nếu paper ghi rõ (không phải pub year).  
> Sửa `dpl` nếu data year khác publication year.

### fp_type (cột `fp_type`) — **Đã pre-fill 85%**

| Mã | Mô tả |
|----|-------|
| `roa` | Return on Assets |
| `roe` | Return on Equity |
| `ros` | Return on Sales / profit margin |
| `tobin_q` | Tobin's Q, market-to-book |
| `sales_growth` | Sales/revenue growth rate |
| `productivity` | lnLP, TFP, output/labor |
| `market_return` | Abnormal return, stock price |
| `composite` | Tổng hợp nhiều measures |

### internationalization_measure_guess (cột `internationalization_measure_guess`)

| Mã | Mô tả |
|----|-------|
| `fsts` | Foreign sales to total sales |
| `entropy` | Entropy index, transnationality |
| `n_countries` | Số quốc gia, geographic spread |
| `fdi_stock` | FDI stock/flow |
| `export_dummy` | Export vs non-export (binary) |
| `composite` | DOI composite index |

---

## Bước 5: Cột workflow cần điền

### Nhóm A — Sau khi tìm được full-text

| Cột | Giá trị | Ghi chú |
|-----|---------|---------|
| `pdf_found` | Y / N | Tìm được PDF không? |
| `pdf_source` | `unpaywall` / `sci-hub` / `researchgate` / `library` | |
| `fulltext_screening_decision` | Y / N / UNSURE | Quyết định L2 cuối cùng |
| `exclusion_reason` | `excl:macro-level` etc. | Chỉ điền nếu N |

### Nhóm B — Khi trích xuất stats

| Cột | Giá trị | |
|-----|---------|--|
| `sample_size_n` | Integer | N của regression model cụ thể |
| `reported_coefficient` | Decimal | β hoặc F-stat được báo cáo |
| `t_value` | Decimal | t-statistic nếu có |
| `df_for_t` | Integer | Degrees of freedom |
| `p_value` | Decimal | p-value |
| `converted_r` | Decimal | r sau khi tính (hoặc trực tiếp) |
| `conversion_formula` | `direct` / `beta` / `t_to_r` / `F_to_r` | |
| `effect_direction` | `+` / `-` / `nonlinear` | |
| `table_or_page` | e.g. `Table 3, p.15` | Vị trí trong paper |
| `icrv` | 0–6 | Kiểm tra/sửa pre-filled value |
| `dpl` | 1/2/3 | Sửa nếu data year ≠ pub year |
| `fp_type` | xem Bước 4 | Kiểm tra/sửa pre-filled value |

### Nhóm C — QA

| Cột | Khi điền |
|-----|----------|
| `ready_for_r` | Đặt = `1` khi có đủ: `converted_r`, `sample_size_n`, `icrv`, `dpl`, `fp_type` |
| `extracted_by` | Tên người trích xuất |
| `checked_by` | Tên người kiểm tra (double-coding 20%) |

---

## Bước 6: Script hỗ trợ

```bash
# Kiểm tra tiến độ extraction
python3 -c "
import csv
with open('p6/tools/results/fulltext_to_extraction_tracker_v3.csv') as f:
    rows = list(csv.DictReader(f))
new_y = [r for r in rows if int(r.get('seq',0))>435 and r['fulltext_screening_decision']=='Y']
done  = sum(1 for r in new_y if r.get('ready_for_r','')=='1')
r_filled = sum(1 for r in new_y if r.get('converted_r','').strip())
print(f'Y papers: {len(new_y)} | ready_for_r=1: {done} | converted_r filled: {r_filled}')
print(f'Remaining: {len(new_y)-done}')
"

# Sau khi extraction xong: chạy MARA
Rscript p6/tools/meta_r_scripts/00_mara_starter_20260520.R

# Chọn 20% subsample cho double-coding
python3 p6/tools/09_select_reliability_subsample.py \
  --input  p6/tools/results/fulltext_to_extraction_tracker_v3.csv \
  --output p6/tools/results/reliability_subsample.csv \
  --seed   42
```

---

## Bước 7: Sau khi hoàn thành L2 + extraction

```
1. Khi ready_for_r = 1 cho ≥ 50 papers mới
   → Chạy p6/tools/10_merge_new_studies.py để merge vào p6_study_database.csv

2. Chạy MARA cập nhật:
   Rscript p6/tools/meta_r_scripts/00_mara_starter_20260520.R

3. Cập nhật manuscript p6/p6_meta_manuscript_en.md:
   - k (số studies), K (số effect sizes)
   - r̄, I², τ², Q
   - Moderator tables (ICRV, DPL, cDAI)

4. Inter-coder reliability (κ ≥ 0.70):
   python3 p6/tools/09_select_reliability_subsample.py
   → Double-code 20% independently
   → Rscript p6/tools/compute_reliability.R
```

---

## Mẹo thực tế

- **Batch 50 papers** mỗi phiên — `extraction_queue_20260520.csv` đã sort theo ưu tiên, bắt đầu từ row 1
- **396 DOI_FIRST** — dùng cột `doi_link` để mở trực tiếp
- **`ready_for_r = 1` chỉ khi đủ 5 trường**: `converted_r`, `sample_size_n`, `icrv`, `dpl`, `fp_type`
- **Nonlinear papers**: ghi cả β₁ và β₂, turning point đến `notes_for_extractor`
- **Server block tất cả API**: Unpaywall, OpenAlex, CrossRef đều 403 từ server — download PDF locally
- **Ước tính thời gian**: 538 papers × 5 phút/paper ≈ 45 giờ đến 15–20 ngày làm 3h/ngày
- **ICRV pre-filled chỉ 38%** — ưu tiên điền icrv khi đọc full-text (quan trọng cho MARA)
