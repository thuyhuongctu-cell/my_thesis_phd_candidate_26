# Báo cáo Tổng hợp Mức độ Sẵn sàng Nộp bài (Submission Readiness)
**Ngày:** 24/05/2026 · **Phạm vi:** CĐ1, CĐ2; P3–P8; 5 chương luận án
**Phương pháp:** 6 reviewer song song dùng các skill `academic-manuscript-submission-checker`, `academic-paper-reviewer`, `phd-dissertation-review`, `three-level-meta-analysis`, `vietnamese-academic-glossary-editor`.

> **Nguồn dữ liệu chuẩn (canonical) đã xác minh từ `p6_study_database_v2.csv`:**
> **k = 259 nghiên cứu · K = 309 effect sizes · r̄ = 0,074 [0,060; 0,088] · I² = 61,2% · ICRV Q_M = 10,16 (p = ,038) · DPL NS**
> (Con số I²=91,9% trong mô tả PR cũ là *stale* — giá trị đúng là 61,2%, nhất quán giữa manuscript P6 và luận án.)

---

## 1. Ma trận sẵn sàng

| Tài liệu | Tạp chí đích | Hạng | Kết luận | Blocker chính |
|----------|--------------|------|----------|---------------|
| **P3 Vietnam** | Journal of Asia Business Studies | ABS-2 | 🟡 CÓ ĐIỀU KIỆN | Thiếu mục tài liệu tham khảo (desk-reject); p-value .660 vs .730; DOI placeholder |
| **P4 Singapore** | Management International Review | ABS-3 | 🟡 CÓ ĐIỀU KIỆN | Turning point 82% vs 88,6%; hệ số −1,167 vs −1,177; nhãn cột M-model |
| **P5 China** | Int. Journal of Emerging Markets | ABS-2 | 🟡 CÓ ĐIỀU KIỆN | ✅ *Đã sửa* LaTeX `\b\beta`; còn N mẫu (4.559/4.544/3.559) chưa khớp |
| **P6 Meta** | International Business Review | ABS-3 | 🔴 CHƯA SẴN SÀNG | PRISMA còn k=287/[TBD]; bảng ICR rỗng; 2 bảng ICRV mâu thuẫn → **chờ hoàn tất extraction (đã hoãn theo yêu cầu)** |
| **P7 Multi-country** | Journal of Int. Business Studies | ABS-4* | 🔴 CHƯA SẴN SÀNG | Hệ số M10 mâu thuẫn (Bảng 3 vs §4.6); ✅ *đã sửa* "34 economies"; thiếu phương trình; nhãn DAI "capability"; đóng góp lý thuyết chưa đạt chuẩn 4* |
| **P8 SIDS** | World Development | ABS-3 | 🟡 CÓ ĐIỀU KIỆN | Bảng 1 rỗng; mâu thuẫn mẫu Comoros/Micronesia; số học −40,4% vs −33% |
| **CĐ1** | CTU chuyên đề | — | 🟡 CÓ ĐIỀU KIỆN | ✅ *Đã sửa* định nghĩa FSTS; còn n_firms Advanced/SIDS chưa khớp giữa các bảng |
| **CĐ2** | CTU chuyên đề | — | 🟢 SẴN SÀNG (nhẹ) | ✅ FSTS đã đồng bộ; còn dấu thập phân Anh ở đoạn P7 (dòng 920–922) |
| **Luận án Ch.1–5** | CTU bảo vệ | — | 🟡 CÓ ĐIỀU KIỆN | ✅ *Đã sửa* k=238→259 (Ch5), 8→6 nghiên cứu (Ch5); còn N Singapore 237 vs 623; 47 vs 49; wave 102 vs 108 |

---

## 2. Đã sửa trong lượt này (high-confidence)

| # | File | Sửa |
|---|------|-----|
| 1 | `p5/p5_china_en_clean.md` | Phương trình M6: `\b\beta`→`\beta` (×9), `\v\varepsilon`→`\varepsilon` — **desk-reject blocker** |
| 2 | `thesis/chuong_5_…vi.md` | "238 nghiên cứu" → "259 nghiên cứu" (dòng 203) |
| 3 | `thesis/chuong_5_…vi.md` | §5.6.1 "tám nghiên cứu" → "sáu nghiên cứu thành phần (P3–P8)"; P1/P2 reframe thành nền tảng |
| 4 | `p7/p7_capstone_en_clean.md` | "across 34 economies" → "across 49 economies" (dòng 207) |
| 5 | `chuyen_de/cd1/00_cd1_…vi.md` | FSTS = (d3b+d3c)/100 → **d3c/100** (đồng bộ CĐ2 + methodology + papers); sửa nhãn d3b/d3c bị đảo (×2 vị trí) |

---

## 3. Còn lại — cần tác giả quyết định / cần dữ liệu gốc

### P3 Vietnam (JABS) — CÓ ĐIỀU KIỆN
- 🔴 **Thiếu reference (desk-reject):** World Bank 2025b, 2025c, Johanson & Vahlne (1977, 2009), Barney (1991), Hitt et al. (1997) — được trích trong text nhưng không có trong danh mục.
- 🔴 **Mâu thuẫn p-value:** FSTS_c² (exporter-only pooled) ghi p=.660 (×4 chỗ) vs Bảng 4 p=.730 — cần đối chiếu output gốc.
- 🟠 DOI placeholder: Agarwal et al. (2026), Barattieri et al. (2026) "[DOI pending]".
- 🟠 Heckman: thiếu exclusion restriction; cite Wolfolds & Siegel (2019).

### P4 Singapore (MIR) — CÓ ĐIỀU KIỆN
- 🔴 **Turning point 82% vs 88,6%:** dòng 192 (β₁=2,652/β₂=−1,705 → 77,8%c +mean ≈82%) KHÁC dòng 253 (84,1%c → 88,6%). **Hai bộ hệ số khác nhau — cần xác định bộ M2 chính thức.**
- 🟠 Hệ số tương tác DAI: Bảng 2 = −1,167† vs §4.4 = −1,177 (p=.083).
- 🟠 Nhãn cột Bảng 2 (M0,M2,M5,M6,M7,M4,M8) không khớp stack phương trình M0–M8.
- 🟠 Cite Teece (2007) "Dynamic Capabilities" trên đường H3/DAI → rủi ro đọc DAI như dynamic capability; nên đổi sang ngôn ngữ coordination-platform.

### P5 China (IJOEM) — CÓ ĐIỀU KIỆN (đã sửa LaTeX)
- 🟠 N mẫu: focal 4.559 vs regression 4.544 vs three-way 3.559 — cần một câu hợp nhất.
- 🟠 Paternoster Δβ CI hiện là "approximate proxy" — nên báo cáo CI chính xác.

### P6 Meta (IBR) — CHƯA SẴN SÀNG (**hoãn theo yêu cầu, chờ extraction**)
- 🔴 PRISMA còn k=287/238/288 stale + "[TBD]"; flow không cộng ra k=259.
- 🔴 Bảng 3.1 ICR (κ/ICC) rỗng [TBD].
- 🟠 Hai bảng ICRV (4.1 vs 4.2) cho phân bố regime khác nhau cùng K=309.
- 🟠 Thiếu danh mục 259 nghiên cứu primary (IBR yêu cầu, thường ở phụ lục).
- ✅ I²=61,2% là ĐÚNG (không phải lỗi); OSF ID đúng.

### P7 Multi-country (JIBS, ABS-4*) — CHƯA SẴN SÀNG
- 🔴 **Hệ số M10 mâu thuẫn:** Bảng 3 (ICRV=+0,729, FSTS×ICRV=+1,636…) vs §4.6 (+0,763, +1,762…). Cùng model, số khác.
- 🔴 Thiếu phương trình ước lượng chính thức M0–M11 (JIBS bắt buộc).
- 🟠 **Nhãn DAI:** title/abstract dùng "Digital Capabilities" → vi phạm ràng buộc "Tier-1 foundational, KHÔNG dynamic capability". Cần quyết định tái định khung (đây là quyết định positioning của tác giả, không tự sửa).
- 🟠 Turning point thiếu CI (cần Fieller/delta); bảng chỉ có sao, thiếu SE/CI.
- 🟠 **Đóng góp lý thuyết cho 4\*:** hiện là "new context + bigger N" → rủi ro desk-reject; cần nêu rõ cơ chế lý thuyết MỚI (ICRV-contingent TP shifting, DAI×ICRV).

### P8 SIDS (World Development) — CÓ ĐIỀU KIỆN
- 🔴 **Bảng 1 rỗng** (chỉ có dòng Total) — desk-reject; cần điền số theo từng nước.
- 🔴 Mâu thuẫn mẫu: Comoros (không phải Pacific) trong "Pacific SIDS"; Micronesia (dòng 59) không có trong danh sách 9 nước.
- 🟠 Số học: β=−0,404 trên ln(LP) ≈ −33%, không phải −40,4%.
- 🟠 Logic turning point §4.3 tự mâu thuẫn (0,712 < 0,80 nhưng nói "outside sample").
- ✅ Nhãn DAI ĐẠT (đã ghi rõ "không phải dynamic capability").

### CĐ1 — CÓ ĐIỀU KIỆN (đã sửa FSTS)
- 🟠 n_firms Advanced (6.640 vs 5.921 vs 12.300) và SIDS (1.371 vs 1.097 vs 2.385) không khớp giữa thân bài/Bảng 2.3.3.1/Phụ lục A.
- 🟠 n Việt Nam 3.077 vs FSTS 23,2/16,1 vs Bảng 19,1%.
- 🟡 Singapore website 66,1% (CĐ1) vs 67% (CĐ2).

### CĐ2 — SẴN SÀNG (nhẹ)
- 🟠 Đoạn P6/P7 (dòng 920–922) dùng dấu thập phân Anh (0.344; p<.05) lẫn với dấu phẩy Việt — cần đồng bộ.
- ✅ k=259/K=309 đúng; H3 reframe điều kiện đúng; DAI đúng nhãn; Hạn chế 3 phần đủ.

### Luận án 5 chương — CÓ ĐIỀU KIỆN (đã sửa Ch5)
- 🔴 **N Singapore 237 (Ch4) vs 623 (Ch3)** — làm rõ 623=tổng, 237=exporters.
- 🟡 47 vs 49 nền kinh tế; wave 102 vs 108; 6 vs 9 Pacific SIDS (Ch1).
- ⚠️ **Skill `thesis-number-consistency` chứa số CŨ (k=238/K=288/I²=62,4%) — KHÔNG dùng làm chuẩn; cần cập nhật skill.**

---

## 4. Quyết định hợp nhất nhánh (consolidation)

- **Base = nhánh hiện tại** `claude/edit-vietnamese-academic-standards-xcAmn` (có k=259/K=309 đúng + ký hiệu kỹ thuật nguyên vẹn).
- **KHÔNG merge** `polish-main-cd-papers`: tuy có dọn em-dash nhưng **regress P6 về k=238** (lỗi số liệu) — chỉ là cải thiện hình thức, có thể áp dụng lại sau.
- **KHÔNG merge** `cd1-inline-and-cleanup` (−296k dòng, xoá PDF/scripts — rủi ro cao).

## 5. Thứ tự ưu tiên đề xuất

1. **P6** — hoàn tất extraction (đang hoãn) → khoá k/K/PRISMA/ICR.
2. **P3** — bổ sung 5 reference thiếu (15 phút, desk-reject).
3. **P7** — sửa mâu thuẫn hệ số M10 + thêm phương trình + quyết định nhãn DAI (lớn nhất cho 4*).
4. **P8** — điền Bảng 1 + sửa định nghĩa mẫu Pacific.
5. **P4/P5** — đối chiếu turning point/N với output Stata gốc.
6. **Luận án** — khoá N Singapore + 47/49 + wave 102/108.
