# Hướng dẫn L2 Screening & Extraction — P6 Meta-Analysis

**Cập nhật**: 22/05/2026 (rev 6)
**File làm việc (canonical)**: `p6/tools/results/fulltext_to_extraction_tracker_v3.csv`  
**Cấu trúc**: 2510 rows × 59 cột  
**Scope**: Full candidate pool từ WoS/Scopus/OpenAlex, bao gồm L2 decisions + extraction tracking

---

## Trạng thái pipeline (22/05/2026 — tracker v3)

| Nhóm | Số lượng | Ghi chú |
|------|---------|---------|
| **Tổng rows** | **2510** | full candidate pool |
| Priority A (`1_DOI_FIRST`) | 1864 | có DOI → dễ truy cập |
| Priority B (`2_NO_DOI_MANUAL`) | 646 | không DOI → tìm thủ công |
| `fulltext_screening_decision = Y` | 785 | INCLUDE → cần trích xuất r |
| `fulltext_screening_decision = N` | 352 | EXCLUDE |
| `fulltext_screening_decision` trống | 0 | L2 screening đã xong |
| `ready_for_r = 1` | 34 | đủ điều kiện MARA |
| `converted_r` đã điền | 27 | extraction đang tiến hành |

**Scripts pipeline:**
```
57_claude_api_extract_r.py    — auto-extract r từ PDF via Claude Haiku (GitHub Actions)
59_groq_extract_r.py          — auto-extract r từ PDF via Groq LLM (GitHub Actions)
40_batch_download_pdfs.py     — tải PDF về p6/pdfs/ (chạy local)
42_merge_tracker_to_database.py — merge → database (khi ≥50 ready_for_r=1)
meta_r_scripts/00_mara_starter_20260522.R — chạy MARA khi ready_for_r ≥ 50
```

**GitHub Actions workflows:**
```
claude_api_extract_r.yml   — Claude Haiku r-extraction (queue_file: extraction_queue_pdf_20260522.csv — 116 OA papers)
semantic_scholar_query.yml — S2 fallback PDF lookup (manifest_file: s2_fallback_queue_20260522.csv — 425 closed-access)
unpaywall_gap.yml          — Unpaywall OA lookup cho gap papers
mara_workflow.yml          — Chạy MARA R script (khi converted_r ≥ 50)
```

**Extraction queues (22/05/2026):**
```
extraction_queue_pdf_20260522.csv   — 116 Y papers có OA PDF, Priority A (chạy claude_api_extract_r)
s2_fallback_queue_20260522.csv      — 425 Y papers closed-access → S2 fallback
```

**Database tổng hợp:**
```
p6/data/p6_study_database_v2.csv    — k=259 studies, K=309 effects (merged + harmonized + fisher_z/vi)
```

**Preliminary MARA (k=259, K=309) — 22/05/2026:**
```
r̄ = 0.074 [0.060, 0.088]  p < .001
I² = 91.9% (between=12.6%, within=79.3%)
ICRV: QM(3)=8.56, p=.036  ✅ significant
DPL:  QM(2)=1.11, p=.575  (NS)
Egger b=0.077, p<.001
```

---

## Bước 1: Mở file làm việc

**File canonical duy nhất:**
```
p6/tools/results/fulltext_to_extraction_tracker_v3.csv  (2510 rows × 59 cột)
```

**Cách làm**: Mở `fulltext_to_extraction_tracker_v3.csv` trong Excel. Lọc `fulltext_screening_decision = Y` (785 papers). Bắt đầu từ `1_DOI_FIRST` rows (những papers có DOI). Điền vào các cột extraction theo thứ tự ưu tiên. Lưu file và commit sau mỗi batch.

**Cấu trúc 59 cột của tracker v3:**

| Nhóm cột | Cột | Mô tả |
|----------|-----|-------|
| **Identification** | `seq`, `priority_rank`, `doi_status` | Số thứ tự, xếp hạng ưu tiên, trạng thái DOI |
| **Metadata** | `icrv`, `dpl`, `year`, `authors`, `title`, `journal`, `doi` | Thông tin bài báo |
| **Retrieval** | `extraction_priority`, `doi_link`, `oa_link`, `oa_status` | Link và trạng thái truy cập |
| **Workflow — PDF** | `pdf_found`, `pdf_source`, `pdf_path` | Kết quả tìm PDF |
| **Workflow — L2** | `fulltext_screening_decision`, `fulltext_screening_reason` | Quyết định include/exclude |
| **Workflow — Extraction** | `ready_for_r`, `extracted_by`, `checked_by` | Tiến độ trích xuất |
| **Effect size** | `converted_r`, `conversion_formula`, `sample_size_n` | Giá trị r và cách tính |
| **Statistics** | `reported_coefficient`, `t_value`, `df_for_t`, `p_value` | Thống kê gốc từ paper |
| **Moderators** | `fp_type`, `internationalization_measure_guess`, `effect_direction`, `curve_type` | Mã hóa moderators |
| **QA** | `table_or_page`, `notes_for_extractor`, `fisher_z`, `variance_z` | Kiểm tra và ghi chú |

**6 cột workflow quan trọng:**

| Cột | Giá trị hợp lệ | Điền khi nào |
|-----|----------------|--------------|
| `pdf_found` | `Y` / `N` | Sau khi tìm kiếm full-text |
| `fulltext_screening_decision` | `Y` / `N` / `UNSURE` | Sau khi đọc abstract/full-text |
| `ready_for_r` | `1` / (blank) | Khi đủ: `converted_r` + `sample_size_n` + `icrv` + `dpl` + `fp_type` |
| `extracted_by` | tên người | Khi trích xuất xong |
| `checked_by` | tên người | Sau double-coding (20% subsample) |
| `conversion_formula` | `direct` / `beta` / `t_to_r` / `F_to_r` | Cùng lúc với `converted_r` |

**Check nhanh tiến độ:**
```bash
python3 -c "
import csv
with open('p6/tools/results/fulltext_to_extraction_tracker_v3.csv') as f:
    rows = list(csv.DictReader(f))
ready = sum(1 for r in rows if r.get('ready_for_r','').strip() == '1')
r_done = sum(1 for r in rows if r.get('converted_r','').strip())
y = sum(1 for r in rows if r.get('fulltext_screening_decision','') == 'Y')
n = sum(1 for r in rows if r.get('fulltext_screening_decision','') == 'N')
todo = sum(1 for r in rows if not r.get('fulltext_screening_decision','').strip())
print(f'Y={y} | N={n} | TODO={todo} | converted_r={r_done} | ready_for_r={ready}')
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
| 4 | Có quan hệ I→P định lượng? | r, β, t, F, hoặc có thể tính r | chỉ mô tả, không có statistics |
| 5 | Peer-reviewed journal article? | có DOI hoặc ISSN | dissertation, book chapter, WP, conference |

### Red flags — loại ngay không cần đọc thêm

- `country-level / national-level analysis` → loại (macro-level)
- `antecedents of internationalization` / `determinants of export` → loại (I là DV, không phải P)
- `qualitative study` / `case study` → loại
- `meta-analysis` / `systematic review` → loại (không phải primary study)
- health, environment, education outcomes → loại (off-domain)

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
| 0 | Multi-country Mixed | Nhiều quốc gia khác regime → dùng 0 |

**Đã pre-fill cho toàn bộ 2510 rows** — kiểm tra và sửa khi đọc full-text nếu context quốc gia không rõ.

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
y = [r for r in rows if r.get('fulltext_screening_decision','')=='Y']
done  = sum(1 for r in y if r.get('ready_for_r','')=='1')
r_filled = sum(1 for r in y if r.get('converted_r','').strip())
print(f'Y papers: {len(y)} | ready_for_r=1: {done} | converted_r filled: {r_filled}')
print(f'Remaining: {len(y)-done}')
"

# Sau khi extraction xong: chạy MARA
Rscript p6/tools/meta_r_scripts/00_mara_starter_20260522.R

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
   Rscript p6/tools/meta_r_scripts/00_mara_starter_20260522.R

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

- **Batch 50 papers** mỗi phiên — lọc `fulltext_screening_decision = Y`, sort theo `extraction_priority` (`1_DOI_FIRST` trước)
- **785 Y papers** cần trích xuất r — dùng cột `doi_link` cho DOI papers
- **`ready_for_r = 1` chỉ khi đủ 5 trường**: `converted_r`, `sample_size_n`, `icrv`, `dpl`, `fp_type`
- **Nonlinear papers**: ghi cả β₁ và β₂, turning point → `notes_for_extractor`
- **Auto-extraction**: `claude_api_extract_r.yml` chạy qua GitHub Actions (limit=100/lần); `groq_extract_r.yml` backup
- **Ước tính thời gian**: 785 papers × 5 phút/paper ≈ 65 giờ → 21–26 ngày làm 3h/ngày; auto-extraction giảm ~70%
- **ICRV đã pre-filled** — kiểm tra lại khi đọc full-text nếu context country không rõ
