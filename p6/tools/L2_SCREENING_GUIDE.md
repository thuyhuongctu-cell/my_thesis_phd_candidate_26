# Hướng dẫn L2 Screening — P6 Meta-Analysis

**File làm việc (canonical)**: `p6/tools/results/fulltext_to_extraction_tracker_v2.csv`  
**Cấu trúc**: 435 rows × 58 cột — superset của tất cả file trước (retrieval worklist + extraction template + workflow tracking)  
**Thứ tự ưu tiên**: `extraction_priority = 1_DOI_FIRST` (310 papers) → `2_NO_DOI_MANUAL` (125 papers)  
**Phân bố**: Y=435 (81.3%), N=100 (18.7%), UNSURE=0 (tất cả đã giải quyết xong 19/05/2026)  
**Template extraction**: `p6/tools/results/meta_analysis_extraction_ready_v1_1.csv` (v1.1, 435 rows × 40 cột, ICRV/DPL đầy đủ)

---

## Bước 1: Quy trình tổng thể

```
Mở fulltext_to_extraction_tracker_v2.csv
  ↓
prescreen_flag = Y (435 papers) → Đọc full-text → điền pdf_found + fulltext_screening_decision
prescreen_flag = N (100 papers) → Xác minh nhanh (giữ N hoặc chuyển UNSURE nếu nghi ngờ)
prescreen_flag = UNSURE → 0 papers còn lại (tất cả đã giải quyết)
  ↓
Ưu tiên theo cột extraction_priority trong tracker:
    1_DOI_FIRST   (310 papers có DOI) → download PDF tự động + trích xuất r
    2_NO_DOI_MANUAL (125 papers)     → tìm full-text thủ công qua Google Scholar / ResearchGate
  ↓
Điền include_flag + r + n + icrv + cdai + dpl + workflow columns cho mỗi paper
  ↓
Khi ready_for_r = Y → chuyển vào meta_analysis_extraction_ready_v1_1.csv
```

---

## Bước 2: Tiêu chí INCLUDE / EXCLUDE (L2)

### INCLUDE (Y) — Tất cả điều kiện phải đúng

| # | Tiêu chí | Ví dụ đạt | Ví dụ loại |
|---|----------|-----------|------------|
| 1 | **Firm-level unit** | phân tích trên doanh nghiệp/nhà máy/SME | phân tích cấp quốc gia, ngành |
| 2 | **Quantitative I→P** | báo cáo r, β, t, F, hoặc tính được r | chỉ mô tả định tính |
| 3 | **Peer-reviewed journal** | journal article có DOI hoặc ISSN rõ | book chapter, dissertation, conference paper |
| 4 | **I measure** | FSTS, DOI, export intensity, số quốc gia, subsidiary count, FDI | chỉ đo performance mà không có I variable |
| 5 | **P measure** | ROA, ROE, Tobin's Q, sales growth, lnLP, ROS, profit margin | không có performance outcome |
| 6 | **1977–2026** | dữ liệu bất kỳ năm trong phạm vi | dữ liệu trước 1977 |

### EXCLUDE (N) — Bất kỳ điều kiện nào đúng

| # | Lý do loại | Mã `include_reason` |
|---|-----------|---------------------|
| 1 | Phân tích cấp quốc gia / ngành (không phải firm) | `excl:macro-level` |
| 2 | Nghiên cứu định tính, conceptual, review, narrative | `excl:qualitative` |
| 3 | Không báo cáo effect size có thể trích xuất | `excl:no-effect-size` |
| 4 | Không có I→P relationship (chỉ đo 1 vế) | `excl:no-ip-relationship` |
| 5 | Meta-analysis hoặc systematic review (không phải primary) | `excl:meta-only` |
| 6 | Book chapter, dissertation, working paper, conference paper | `excl:grey-lit` |
| 7 | Trùng lặp với study đã có trong k=287 database | `excl:duplicate-existing` |
| 8 | Health, environment, education — ngoài IB domain | `excl:off-domain` |
| 9 | Case study (1–5 doanh nghiệp) | `excl:case-study` |

### UNSURE — Khi không đủ thông tin từ abstract

Giữ `include_flag = UNSURE` nếu:
- Không đọc được full-text để xác định unit of analysis
- Abstract không rõ performance variable là gì
- Cần xem correlation matrix hoặc regression table để biết có extractable r không

---

## Bước 3: Trích xuất Effect Size (chỉ cho papers Y)

### Thứ tự ưu tiên lấy r

```
1. Pearson r trực tiếp → cột `r`
2. r từ t-statistic:       r = t / sqrt(t² + N - 2)         → cột `r_from_t`
3. r từ F-statistic (df₁=1): r = sqrt(F / (F + N - 2))     → cột `r_from_F`
4. r từ standardized β:    r ≈ β / sqrt(β² + 1)            → ghi chú cột `r_note`
5. r từ eta²:             r = sqrt(eta²)                   → ghi chú cột `r_note`
```

### Nonlinear (inverted-U / U-shape)

Nếu paper báo cáo cả β₁ (linear) và β₂ (quadratic):
- Điền `r` = partial r từ linear term (nếu có)
- Điền `r_quadratic` = partial r từ quadratic term
- Điền `turning_point` = -β₁ / (2β₂) nếu paper báo cáo
- Ghi `nonlinear = Y`

### N (sample size)

Dùng N của regression model cụ thể (không phải N tổng của paper nếu có nhiều sub-samples).

---

## Bước 4: Coding các biến Moderator

### ICRV (cột `icrv`) — Integer 1–6

| Mã | Regime | Quốc gia ví dụ |
|----|--------|---------------|
| 1 | Advanced Innovation-Driven | Singapore, Hong Kong, Đài Loan, Hàn Quốc, Nhật Bản, Úc, NZ, Israel |
| 2 | Advanced Resource/Trade-Driven | Brunei, Qatar, UAE, Kuwait, Saudi Arabia |
| 3 | Upper-Middle / Emerging Strong | Trung Quốc, Malaysia, Thái Lan, Ấn Độ, Brazil, Mexico, Thổ Nhĩ Kỳ |
| 4 | Lower-Middle / Frontier Weak | Việt Nam, Philippines, Indonesia, Bangladesh, Pakistan, Egypt |
| 5 | Least Developed / Frontier | Myanmar, Cambodia, Lào, Nepal, Afghanistan, Ethiopia |
| 6 | Pacific SIDS | Fiji, PNG, Samoa, Tonga, Vanuatu, Solomon Islands |
| 0 | Multi-country Mixed | Nghiên cứu cover nhiều regime → `icrv = 0` |

**Quy tắc**: Dùng chế độ của **quốc gia của mẫu doanh nghiệp** (không phải destination market).

### cDAI (cột `cdai`) — Continuous 0–1

World Bank Digital Adoption Index (DAI) cho quốc gia của mẫu, năm trung bình của data collection:

| Quốc gia | cDAI ước tính (2015–2020) | Nguồn |
|---------|--------------------------|-------|
| Singapore | 0.82 | WB DAI 2016 |
| Hàn Quốc | 0.78 | WB DAI 2016 |
| Trung Quốc | 0.58 | WB DAI 2016 |
| Ấn Độ | 0.39 | WB DAI 2016 |
| Việt Nam | 0.42 | WB DAI 2016 |
| Indonesia | 0.40 | WB DAI 2016 |
| Thailand | 0.52 | WB DAI 2016 |
| Malaysia | 0.62 | WB DAI 2016 |

Nếu không tìm được WB DAI: dùng ITU IDI (Internet Development Index) normalized, hoặc để trống và ghi `cdai_source = unknown`.

**Proxy đơn giản nếu không có data**: L=0.25, M=0.50, H=0.75 → nhưng phải ghi `cdai_proxy = Y`.

### DPL (cột `dpl`) — Integer 1/2/3

Dựa trên **năm xuất bản** (publication year):

| Mã | Tên | Publication year |
|----|-----|-----------------|
| 1 | Precede (PRE) | Trước 2000 |
| 2 | Spawn (SPN) | 2000–2009 |
| 3 | Follow (FOL) | 2010 trở đi |

**Dựa trên data collection year** nếu paper báo cáo: ưu tiên dùng year của dữ liệu thay vì publication year.

### doi_type (cột `doi_type`) — Loại đo lường I

| Mã | Mô tả | Ví dụ biến |
|----|-------|-----------|
| `FSTS` | Foreign sales to total sales | export ratio, FSTS, export intensity |
| `export_ratio` | Export value / total revenue | xuất khẩu/doanh thu |
| `geographic_diversification` | Số quốc gia, entropy index | DOI entropy, Herfindahl |
| `DOI` | Composite internationalization | Sullivan's DOI index |
| `FDI` | FDI flows hoặc stocks | outward FDI, OFDI |
| `subsidiary` | Số subsidiaries / affiliates | foreign affiliates |
| `other` | Khác | board internationalization |

### fp_type (cột `fp_type`) — Loại đo lường Performance

| Mã | Mô tả | Ví dụ biến |
|----|-------|-----------|
| `financial_perf` | Kết quả tài chính (accounting) | ROA, ROE, ROS, profit margin |
| `Tobin_Q` | Market-based performance | Tobin's Q, market-to-book |
| `labor_productivity` | Năng suất lao động | lnLP, revenue/employee |
| `sales_growth` | Tăng trưởng doanh thu | revenue growth rate |
| `innovation` | Innovation output | patent count, R&D intensity |

---

## Bước 5: Workflow thực tế với CSV (58 cột — fulltext_to_extraction_tracker_v2.csv)

### Nhóm 1: Workflow tracking (điền khi có full-text)

| Cột | Nguồn | Ghi chú |
|-----|-------|---------|
| `pdf_found` | Y / N | Tìm được full-text PDF không? |
| `pdf_filename` | Tên file | ví dụ: `smith2020_fsts_roa.pdf` |
| `pdf_source` | Nguồn | `unpaywall`, `sci-hub`, `researchgate`, `email_author` |
| `fulltext_screening_decision` | Y / N / UNSURE | Quyết định L2 sau khi đọc full-text |
| `exclusion_reason` | Mã excl: | ví dụ: `excl:macro-level` |

### Nhóm 2: Effect size extraction (điền khi trích xuất r)

| Cột | Nguồn | Ghi chú |
|-----|-------|---------|
| `include_flag` | Quyết định L2 | Y / N / UNSURE |
| `include_reason` | Lý do ngắn | `incl:firm-level-fsts` |
| `r` | Từ paper | Pearson r trực tiếp hoặc converted |
| `r_note` | Ghi chú | `from t-stat`, `from beta` |
| `n` | Từ paper | Sample size của regression model |
| `df_for_t` | Từ paper | df nếu dùng công thức r từ t |
| `table_or_page` | Từ paper | ví dụ: `Table 3, p.15` |
| `statistic_location` | Từ paper | Vị trí cụ thể trong paper |
| `conversion_formula` | Công thức dùng | `r=sqrt(t²/(t²+df))` hoặc `r=beta/sqrt(beta²+1)` |
| `effect_direction` | `+` / `-` | Chiều của mối quan hệ I→P |
| `icrv` | Coding | Integer 1–6 hoặc MX |
| `cdai` | WB DAI | Decimal 0–1 |
| `cdai_proxy` | Y/N | Y nếu dùng L/M/H proxy |
| `dpl` | Pub year / data year | 1 / 2 / 3 |
| `doi_type` | Từ paper | Xem bảng Bước 4 |
| `fp_type` | Từ paper | Xem bảng Bước 4 |
| `nonlinear` | Y/N | Y nếu báo cáo quadratic term |
| `turning_point` | Từ paper | TP = -β₁/(2β₂), nếu có |

### Nhóm 3: QA và computed columns

| Cột | Nguồn | Ghi chú |
|-----|-------|---------|
| `ready_for_r` | Y / N | Tất cả thông tin đủ để chạy MARA? |
| `extracted_by` | Tên | Người trích xuất |
| `checked_by` | Tên | Người kiểm tra (double-coding) |
| `converted_r` | Công thức tự động | `=SQRT(t²/(t²+df))` hoặc điền tay |
| `fisher_z` | Công thức | `=0.5*LN((1+r)/(1-r))` |
| `variance_z` | Công thức | `=1/(n-3)` |

### Cột đã điền sẵn (chỉ cần kiểm tra)

- `prescreen_flag` — Y / N / UNSURE (từ keyword engine)
- `prescreen_reason` — lý do prescreen
- `icrv` — ICRV đã điền đầy đủ (0 trống)
- `dpl` — DPL đã điền đầy đủ (0 trống)
- `extraction_priority` — `1_DOI_FIRST` (310) / `2_NO_DOI_MANUAL` (125)
- `doi`, `doi_link`, `google_scholar`, `openalex_search`, `unpaywall_api` — links đã điền

---

## Bước 6: Sau khi hoàn thành L2

```bash
# OA check và download PDF (chạy LOCAL — server block Unpaywall/OpenAlex)
python3 p6/tools/30_oa_check_and_download.py \
  --input  p6/tools/results/fulltext_to_extraction_tracker_v2.csv \
  --output p6/tools/results/oa_check_20260519.csv \
  --pdfs   p6/tools/pdfs/ \
  --email  seranguyenct@gmail.com

# Chọn subsample 20% để double-coding
python3 p6/tools/09_select_reliability_subsample.py \
  --input  p6/tools/results/fulltext_to_extraction_tracker_v2.csv \
  --output p6/tools/results/reliability_subsample.csv \
  --seed   42

# Merge vào database chính (sau khi reliability đạt κ≥0.70)
python3 p6/tools/10_merge_new_studies.py \
  --new      p6/tools/results/fulltext_to_extraction_tracker_v2.csv \
  --existing p6/data/p6_study_database.csv \
  --output   p6/data/p6_study_database_updated.csv

# Chạy MARA cập nhật
Rscript p6/scripts/p6_mara_updated.R
```

---

## Mẹo thực tế

- **File canonical**: `fulltext_to_extraction_tracker_v2.csv` là file làm việc duy nhất — không cần dùng thêm file nào khác
- **Batch 50 papers** mỗi lần để tránh fatigue — 435 papers Y ≈ 9 batch
- **Ưu tiên `extraction_priority = 1_DOI_FIRST`** (310 papers có DOI) — cột này đã có sẵn trong tracker v2, không cần file ưu tiên riêng
- **Priority A (310 papers DOI)**: điền `pdf_found`, download PDF tự động qua `30_oa_check_and_download.py` (chạy local), rồi điền `conversion_formula` + `converted_r`
- **Priority B (125 papers no-DOI)**: tìm full-text thủ công qua Google Scholar / ResearchGate, điền `pdf_source`
- **Công thức chuyển đổi** (điền vào cột `conversion_formula`):
  - `r = sqrt(t² / (t² + df))`
  - `Fisher_z = 0.5 * ln((1 + r) / (1 - r))`
  - `variance_z = 1 / (n - 3)`
- **100 prescreen_flag=N**: chỉ xác minh nhanh nếu nghi ngờ
- **`ready_for_r = Y`** khi đã có: `r`, `n`, `icrv`, `dpl`, `doi_type`, `fp_type` — chỉ khi đó mới chuyển qua MARA
- Tổng ước tính: **15–25 giờ** nếu làm đều đặn 2–3 giờ/ngày → **7–12 ngày**
- **Lưu ý server**: Tất cả API học thuật (Unpaywall, OpenAlex, CrossRef) bị block (HTTP 403) từ server này — phải chạy OA download locally
