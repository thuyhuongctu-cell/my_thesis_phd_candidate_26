# P6 — Hướng dẫn Tìm kiếm PRISMA trên Web of Science, Scopus & Cơ sở dữ liệu bổ sung

> **Mục đích**: Ghi lại từng bước thực hiện tìm kiếm hệ thống cho meta-analysis P6  
> **Chuẩn**: PRISMA 2020 (Page et al., 2021)  
> **Người thực hiện**: Đỗ Thùy Hương  
> **Ngày search**: ___/___/2026  
> **Phiên bản**: v2 — Chuỗi toàn cầu (không bộ lọc địa lý); bổ sung ABI/INFORM, Business Source Complete, ScienceDirect, SpringerLink, Emerald Insight  
> **Loại ấn phẩm**: Chỉ bài báo peer-reviewed trên tạp chí học thuật và articles in press có DOI. Luận án, working papers, conference papers, book chapters **không** đưa vào corpus chính.  

---

## PHẦN 1 — WEB OF SCIENCE

### 1.1 Truy cập

- URL: https://www.webofscience.com
- Chọn: **Advanced Search**
- Đăng nhập bằng tài khoản tổ chức (Đại học Cần Thơ)

---

### 1.2 Query — Copy nguyên đoạn dưới vào ô Advanced Search

> **Lưu ý ký tự đại diện (wildcard):** WoS hỗ trợ `*` bên ngoài dấu ngoặc kép.  
> `internationaliz*` bắt: internationalization, internationalized, internationalizing, internationalizes  
> `internationalis*` bắt: internationalisation, internationalised, internationalising (British English)  
> Không cần liệt kê từng biến thể — dùng wildcard ngắn gọn hơn và bắt đầy đủ hơn.

```
TS=(internationaliz* OR internationalis* OR multinationality 
    OR "degree of internationalization" OR "degree of internationalisation"
    OR "international diversification" OR "geographic diversification"
    OR "foreign sales" OR "foreign sales to total sales" OR FSTS
    OR "foreign assets" OR "foreign assets to total assets" OR FATA
    OR "export intensity" OR "export scope" OR "export ratio"
    OR "foreign market entry" OR "foreign subsidiaries")
AND 
TS=("firm performance" OR "enterprise performance" OR "corporate performance"
    OR "financial performance" OR "business performance"
    OR "labor productivity" OR "labour productivity" OR profitability 
    OR "Tobin's q" OR "return on assets" OR ROA OR "return on equity"
    OR "return on sales" OR "total factor productivity" OR "firm efficiency")
AND
TS=(correlation OR regression OR coefficient OR "effect size" OR "r =")
```

> **Các biến thể được bắt bởi wildcard `internationaliz*` / `internationalis*`:**
> - Danh từ: internationalization / internationalisation  
> - Động từ: internationalize / internationalise  
> - Tính từ: internationalized / internationalised  
> - Phân từ hiện tại: internationalizing / internationalising  
> - Số nhiều: internationalizations / internationalisations
>
> **Lưu ý bổ sung v2 (global search, không có bộ lọc địa lý):** Chuỗi tìm kiếm đã mở rộng để bắt đầy đủ các thước đo quốc tế hóa (FSTS, FATA, geographic diversification, export ratio, foreign subsidiaries) và không giới hạn vùng địa lý. Kết quả sẽ nhiều hơn đáng kể so với chuỗi có bộ lọc châu Á–Thái Bình Dương trước đây.

---

### 1.3 Bộ lọc (áp dụng sau khi có kết quả)

| Bộ lọc | Giá trị cần chọn |
|--------|-----------------|
| Timespan | **1977–2026** |
| Document Types | **Article** (bỏ Review, Book Chapter, Proceedings, Editorial) |
| Language | **English** |
| Databases | Web of Science Core Collection |

---

### 1.4 Ghi lại kết quả

```
Ngày thực hiện:  ___/___/2026
Số kết quả WoS:  n = ________
```

---

### 1.5 Export

1. Chọn **tất cả kết quả** (nếu > 500: export từng batch 500)
2. Nhấn **Export** → **Excel** (hoặc Plain Text)
3. Tick chọn: **Full Record + Cited References**
4. Lưu file: `p6/data/wos_raw_YYYYMMDD.xlsx`

---

## PHẦN 2 — SCOPUS

### 2.1 Truy cập

- URL: https://www.scopus.com
- Chọn: **Advanced Search**

---

### 2.2 Query — Copy nguyên đoạn dưới vào ô Advanced Search

> **Lưu ý Scopus:** Scopus hỗ trợ wildcard `*` tương tự WoS, nhưng **bên trong** TITLE-ABS-KEY.  
> Dùng `internationaliz*` và `internationalis*` để bắt toàn bộ dạng từ (xem ghi chú §1.2).

```
TITLE-ABS-KEY(internationaliz* OR internationalis*
    OR multinationality OR "degree of internationalization"
    OR "degree of internationalisation"
    OR "international diversification" OR "geographic diversification"
    OR "foreign sales" OR "foreign sales to total sales" OR FSTS
    OR "foreign assets" OR "foreign assets to total assets" OR FATA
    OR "export intensity" OR "export scope" OR "export ratio"
    OR "foreign market entry" OR "foreign subsidiaries")
AND
TITLE-ABS-KEY("firm performance" OR "enterprise performance"
    OR "corporate performance" OR "financial performance" OR "business performance"
    OR "labor productivity" OR "labour productivity" OR profitability
    OR "return on assets" OR Tobin OR "return on equity"
    OR "return on sales" OR "total factor productivity" OR "firm efficiency")
AND
TITLE-ABS-KEY(correlation OR regression OR coefficient OR "effect size")
AND PUBYEAR > 1976 AND PUBYEAR < 2027
AND DOCTYPE(ar)
AND LANGUAGE(english)
```

---

### 2.3 Ghi lại kết quả

```
Ngày thực hiện:    ___/___/2026
Số kết quả Scopus: n = ________
```

---

### 2.4 Export

1. Chọn **tất cả** → **Export** → **CSV / Excel**
2. Lưu file: `p6/data/scopus_raw_YYYYMMDD.csv`

---

## PHẦN 3 — CƠ SỞ DỮ LIỆU BỔ SUNG

Sau WoS và Scopus, thực hiện tìm kiếm bổ sung tại các cơ sở dữ liệu sau. Dùng chuỗi tìm kiếm ngắn gọn hơn (không cần layer thứ ba về thống kê vì các cơ sở dữ liệu này ít hỗ trợ wildcard phức tạp).

| Cơ sở dữ liệu | Truy cập | Ghi chú |
|---------------|----------|---------|
| ABI/INFORM Complete | ProQuest | Mạnh về quản trị, kinh doanh quốc tế |
| Business Source Complete | EBSCO | Bao phủ tạp chí IBR, JWB, MIR |
| ScienceDirect | Elsevier | IBR, JIBS, JWB (Elsevier-owned) |
| SpringerLink | Springer | MIR, APJM, management journals |
| Emerald Insight | Emerald | Tạp chí chuyên ngành management |

**Chuỗi tìm kiếm rút gọn (cho cơ sở dữ liệu bổ sung):**
```
(internationalization OR internationalisation OR "foreign sales" OR FSTS OR FATA
 OR "export intensity" OR "foreign subsidiaries")
AND
("firm performance" OR "financial performance" OR "labor productivity"
 OR profitability OR "return on assets" OR "Tobin's Q")
```

**Bộ lọc:** Article / Journal Article; English; 1977–2026

```
ABI/INFORM:           n = ________
Business Source:      n = ________
ScienceDirect:        n = ________
SpringerLink:         n = ________
Emerald Insight:      n = ________
Forward citation (Google Scholar, 5 anchors): n = ________
```

---

## PHẦN 4 — DEDUPLICATION (Loại trùng)

Sau khi có tất cả kết quả từ WoS, Scopus và cơ sở dữ liệu bổ sung:

1. Gộp tất cả file vào 1 bảng Excel
2. Xóa trùng theo **DOI** (ưu tiên) hoặc Title + Year
3. Dùng Excel: **Data → Remove Duplicates** (cột DOI)

```
Tổng tất cả nguồn:       n = ________
Sau khi loại trùng:      n = ________   ← ghi vào PRISMA flow
```

---

## PHẦN 5 — SCREENING LEVEL 1 (Tiêu đề + Tóm tắt)

Duyệt từng dòng trong Excel, thêm cột **Decision** (INCLUDE / EXCLUDE) và cột **Reason**.

### Loại ngay nếu (bất kỳ điều kiện nào):

| # | Lý do loại | Ghi vào cột Reason |
|---|-----------|-------------------|
| 1 | Không xét mối quan hệ I → FP | not_IP |
| 2 | Phân tích cấp quốc gia/ngành (không phải firm-level) | not_firm |
| 3 | Nghiên cứu định tính hoặc conceptual thuần túy | qualitative |
| 4 | Meta-analysis hoặc systematic review (không phải primary study) | meta |
| 5 | Không phải tiếng Anh | language |
| 6 | Không phải bài báo peer-reviewed trên tạp chí học thuật (luận án, working paper, conference paper, book chapter, institutional report) | non_peer_reviewed |

```
Số bài sau Level 1:  n = ________
Số bài bị loại:      n = ________
```

---

## PHẦN 6 — SCREENING LEVEL 2 (Full Text — PICO)

Tải PDF từng bài còn lại, kiểm tra 4 tiêu chí:

| Ký hiệu | Tiêu chí | Yêu cầu cụ thể |
|---------|---------|----------------|
| **P** | Population | Phân tích cấp **doanh nghiệp** (firm-level) |
| **I** | Intervention | IV = **DOI**: FSTS, FATA, GEO count, composite index, EXP intensity |
| **O** | Outcome | DV = **firm performance**: ROA, ROE, Tobin's Q, ROS, năng suất lao động, doanh thu |
| **S** | Statistics | Có **r Pearson**, hoặc β + SE + n để tính r; hoặc t-stat + n |

### Loại nếu:
- Không trích được r (không đủ thông số)
- Mẫu trùng với bài đã có → giữ bài **n lớn hơn** hoặc **mới hơn**
- DOI là **biến điều tiết** (moderator), không phải IV
- DV là rủi ro tài chính, quản trị thu nhập, cấu trúc vốn — không phải firm performance

```
Số bài sau Level 2 (đủ điều kiện):  k = ________   ← k MỚI từ formal search
Số bài bị loại Level 2:             n = ________
```

---

## PHẦN 6 — ĐIỀN VÀO PRISMA FLOW

Sau khi hoàn thành, mở file `p6/p6_prisma_flow.md` và điền tất cả chỗ `[n = TBD]`:

```
WoS Core Collection:           n = ___
Scopus:                        n = ___
Tổng trước deduplication:      n = ___
Sau deduplication:             n = ___
Loại ở Level 1:                n = ___
Đến Level 2:                   n = ___
Loại ở Level 2:                n = ___
  - Không extractable r:       n = ___
  - Duplicate sample:          n = ___
  - Không phải firm-level:     n = ___
  - Meta-analysis:             n = ___
  - Thiếu thông tin:           n = ___
INCLUDED (k mới):              k = ___
```

---

## PHẦN 7 — CẬP NHẬT DATABASE

Với mỗi bài **mới** (chưa có trong forest_data.csv):

1. Trích xuất r (hoặc tính từ β/t/F)
2. Gán Study ID tiếp theo: **S239, S240, S241…**
3. Thêm dòng vào `p6/results/forest_data.csv` theo format:

| Cột | Giá trị |
|-----|---------|
| study_id | S239 |
| first_author | [họ tác giả đầu] |
| year | [năm] |
| country | [ISO code] |
| n | [cỡ mẫu] |
| r | [giá trị r] |
| doi_type | EXP / FDI / GEO / COMP |
| fp_type | ACC / MKT / LAB / MIX |
| icrv | I / II / III / FR / SIDS / MX |
| cdai | H / M / L |
| dpl_phase | PRE / SPN / FOL |

4. Thêm trích dẫn APA 7 vào `p6/p6_primary_studies_apa7.md` Phần 5

---

## CHECKLIST CUỐI

- [ ] WoS search đã chạy và ghi kết quả n
- [ ] Scopus search đã chạy và ghi kết quả n
- [ ] File Excel gộp đã deduplication
- [ ] Level 1 screening hoàn thành
- [ ] Level 2 screening (PICO) hoàn thành
- [ ] Tất cả [TBD] trong `p6_prisma_flow.md` đã điền
- [ ] Bài mới đã thêm vào `forest_data.csv`
- [ ] Bài mới đã thêm vào `p6_primary_studies_apa7.md`
- [ ] k và K mới đã cập nhật trong `21_p6_meta_vi.md` và `p6_meta_manuscript_en.md`
- [x] Single-coder: đối soát double-entry r/n + mã moderator với PDF gốc (không tính κ — đã nêu deviation)

---

## Tóm tắt mục tiêu

| Chỉ số | Hiện tại (baseline) | Mục tiêu sau search |
|--------|--------------------|--------------------|
| k (số nghiên cứu) | 238 | ≥ 250 |
| K (số effect sizes) | 288 | TBD |
| Khoảng thời gian | 1982–2026 | 1977–2026 |

---

*File tạo: 16/05/2026. Tham chiếu: `p6/p6_prisma_flow.md` v2.1*
