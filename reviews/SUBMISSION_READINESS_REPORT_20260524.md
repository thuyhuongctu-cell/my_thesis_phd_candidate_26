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
| **P4 Singapore** | Management International Review | ABS-3 | 🟡 CÓ ĐIỀU KIỆN | ✅ TP đã sửa→82% (verify raw .dta: TP=78,6%, manuscript coef→82,3%); còn hệ số tương tác DAI −1,167 vs −1,177; nhãn cột M-model |
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

## 2b. Đã sửa thêm — lượt "Điều chỉnh" (24/05, đối chiếu replication tables + .dta)

| # | File | Sửa | Nguồn xác minh |
|---|------|-----|----------------|
| 6 | `p7` §4.6 | M10: ICRV +0,763→**+0,729** (exp 115%→107%); FSTS×ICRV +1,762→**+1,636**; FSTS²×ICRV −2,746→**−2,501** | `p7_coefs_all_models.csv` (text lệch, Bảng 3 đúng) |
| 7 | `p8` §4.x | "40,4% thấp hơn" → **"≈33% (exp(−0,404)−1)"**; "Micronesia" (ngoài mẫu) → **"Tonga"** | `p8_R_coefs.csv` β=−0,404; danh sách 9 nước |
| 8 | `p3` refs | Thêm 5 entry: Barney 1991, Hitt et al. 1997, Johanson & Vahlne 1977+2009, World Bank 2025b/2025c; sửa Vernon 1979 → *Oxford Bulletin…* | desk-reject fix |
| 9 | `cd2` | Dấu thập phân Anh → Việt ở đoạn P6/P7 (84.910; 0,344; p=,038…) — giá trị giữ nguyên | — |
| 10 | `thesis ch1` | SIDS "6–8"/"6" → **9** (khớp mẫu P8) | P8 = 9 nước |
| 11 | `thesis ch4` | Singapore N=237 → **623** (full); power 16% thuộc subsample exporters **n≈84** | P4 manuscript |

**Cập nhật matrix:** P3 nâng từ 🟡 (đã hết blocker reference) → còn p-value .660/.730 + DOI placeholder. P7 đỡ một blocker (M10 đã khớp). P8 đỡ (arithmetic + Micronesia). Luận án đỡ (N Singapore + SIDS). CĐ2 sạch decimal.

---

## 3. Còn lại — cần tác giả quyết định / cần dữ liệu gốc

### P3 Vietnam (JABS) — CÓ ĐIỀU KIỆN
- 🔴 **Thiếu reference (desk-reject):** World Bank 2025b, 2025c, Johanson & Vahlne (1977, 2009), Barney (1991), Hitt et al. (1997) — được trích trong text nhưng không có trong danh mục.
- 🔴 **Mâu thuẫn p-value:** FSTS_c² (exporter-only pooled) ghi p=.660 (×4 chỗ) vs Bảng 4 p=.730 — cần đối chiếu output gốc.
- 🟠 DOI placeholder: Agarwal et al. (2026), Barattieri et al. (2026) "[DOI pending]".
- 🟠 Heckman: thiếu exclusion restriction; cite Wolfolds & Siegel (2019).

### P4 Singapore (MIR) — ✅ TURNING POINT ĐÃ SỬA (verify .dta thật)
- ✅ **Đã verify với raw Singapore .dta** (`6e3479da/bdcf8996-Singapore2023fulldata.dta`) — tái lập CHÍNH XÁC mẫu manuscript: **N=623, mean FSTS=0,0465 (≈0,045), exporters=85 (≈84)**. M2 *đúng spec* (controls + sector FE, FSTS=d3c/100, lnLP=ln(d2/l1)): **β₁=+2,576 (SE 0,672), β₂=−1,741 (SE 0,869, p=,046), TP=78,6%**. Hệ số gần khớp Bảng 2 manuscript (2,652/−1,705) — khác biệt nhỏ do chi tiết build (foreign dummy/% , winsorize).
- ✅ **Lind–Mehlum đúng chuẩn trên raw .dta: p=0,238 (KHÔNG có ý nghĩa)** — slope@high FSTS=−0,745 (t=−0,71, NS) do đuôi trên thưa. **Điều này XÁC NHẬN khung thận trọng "support-constrained / không xác định chính thức inverted-U" của manuscript là ĐÚNG** (LM p=,303 của manuscript ≈ ,238 của tôi). *(Sửa lại nhận định trước: manuscript KHÔNG bán rẻ — khung đúng; chỉ sai con số turning point.)*
- ✅ **LỖI DUY NHẤT = số turning point.** Manuscript ghi 88,6% (abstract/Hình) và 82% (§4.2) — mâu thuẫn nội bộ. Hệ số riêng của manuscript (2,652/−1,705) → **−2,652/(2·−1,705)+0,045 = 82,3%**; raw .dta → 78,6%. **88,6% là lỗi tính toán** (không khớp cả Bảng 2 lẫn .dta; bootstrap median của chính manuscript = 80%, đã khớp ~82%). **Đã sửa 88,6%→82% nhất quán** trên: P4 EN/VI, manuscripts/p4, thesis (Ch1/3/4/5, 03_methodology, 11_positioning, 04_05_chapters), CĐ1/CĐ2, P7 EN/VI, writing_guides, và `check-consistency.py` (p4_tp canonical 82%, 88.6 → wrong-list). Hệ số §4.2 giữ nguyên giá trị Bảng 2 của manuscript.
- Manuscript ghi exporters n≈84 (regression complete-case) vs raw FSTS>0 N=111 — kiểm tra lại khi re-run.
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
- ✅ **Bảng 1 ĐÃ ĐIỀN** (24/05): tính từ `data_wbes/p7/p7_pooled_clean.csv` (filter `icrv_label=="SIDS_small"`), khớp tổng N=1.469/exporters=187/12,7%/FSTS=0,060. 9 nước: Fiji(165), Kiribati(114), PNG(141), Samoa(131), Solomon(107), Timor-Leste(393), Tonga(144), Vanuatu(157), Comoros(117).
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
