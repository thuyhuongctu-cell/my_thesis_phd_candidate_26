# BÁO CÁO REVIEW CHUYÊN ĐỀ TIẾN SĨ SỐ 1 (CĐ1)

**Files reviewed**: `thesis/14_cd1_part1_intro_theory_vi.md` · `thesis/15_cd1_part2_findings_vi.md` · `thesis/16_cd1_part3_cases_conclusion_vi.md`  
**Skill**: `phd-dissertation-review` (severity framework: 🔴Critical / 🟠Major / 🟡Minor / ⚪Stylistic)  
**Ngày review**: 2026-05-13  
**Readiness score**: **65%** (draft v3.x — nội dung phong phú nhưng có 5 vấn đề Critical về tính nhất quán số liệu và nhãn)

---

## TÓM TẮT ĐIỂM MẠNH

1. **Phạm vi dữ liệu ấn tượng**: Pool 101,185 firms × 47 nền kinh tế × 108 cặp QG×năm — rộng nhất trong văn liệu IB cho I–P châu Á.
2. **Khung lý thuyết đa tầng**: ICRV 6 sub-regimes + CDCM + VoC extension — mạch lý thuyết rõ và đổi mới.
3. **Tự phê bình tốt**: ICT exclusion test, Tier-1 saturation argument, BREADY schema effect — CĐ1 thừa nhận các ảo ảnh thống kê trước khi ai hỏi.
4. **Cập nhật 2026 đầy đủ**: ADB Vietnam Outlook 2026, IMF April 2026, AI Preparedness Index — tài liệu thực sự live.
5. **Pipeline tái lập được**: Cam kết replication package rõ ràng.

---

## 🔴 CRITICAL ISSUES — Phải sửa trước khi nộp cho phản biện

### C1 — Vietnam n: 2,958 vs 3,077 trong cùng tài liệu

**Vị trí**:
- `thesis/15` Mục 4.4.5.1, Bảng 4.4.5.1, Mục 6.1.2 Bảng 6.1.2: **n=2,958**
- `thesis/16` Mục 5.3 và Bảng 5.1: **n=3,077**

**Mức độ**: 119 firms (3.9% sample) — phản biện sẽ hỏi ngay.

**Giải thích khả dĩ**: 3,077 = tổng doanh nghiệp Việt Nam trong pool; 2,958 = subsample đủ biến hồi quy (complete case). **Nhưng khác biệt này không được ghi chú ở đâu trong tài liệu.**

**Hành động**: Thêm footnote tại Mục 5.3: *"n=3,077 firms tổng cộng; n=2,958 firms có đầy đủ dữ liệu cho phân tích hồi quy (complete case) — xem Mục 4.4.5.1."*

---

### C2 — 2025 cohort n: Mục 1.1 nói 17,107; Mục 4.1 và Bảng 4.10 nói 16,979

**Vị trí**:
- `thesis/14` Mục 1.1: **"14 đợt khảo sát với 17.107 doanh nghiệp"**
- `thesis/15` Mục 4.1: **"14 đợt khảo sát năm 2025 với 16.979 doanh nghiệp"**
- `thesis/15` Bảng 4.10 tổng hàng: **16,979**

**Xác minh độc lập**: Cộng từng dòng quốc gia trong Bảng 4.10:  
IND(10,479) + NPL(1,740) + SAU(1,002) + THA(813) + LKA(607) + MNG(601) + QAT(480) + AFG(480) + MDV(154) + FJI(151) + SLB(150) + BRN(150) + KWT(150) + KIR(150) = **17,107**

 đến Tổng hàng trong Bảng 4.10 **SAI** (16,979 ≠ 17,107); Mục 1.1 **đúng** (17,107).

**Hành động**: Sửa Mục 4.1 và tổng hàng Bảng 4.10 từ 16,979 đến 17,107. Nếu Nepal (NPL, n=1,740) bị loại khỏi phân tích do schema, ghi footnote rõ ràng.

---

### C3 — Bảng 4.1 n_firms vs Mục 4.1 pool breakdown: Frontier chênh 34%

**Vị trí**: `thesis/15` Mục 4.1 text vs Bảng 4.1 column "n_firms"

| Sub-regime | Mục 4.1 text | Bảng 4.1 | Δ | Δ% |
|---|---|---|---|---|
| Advanced | 6,640 | 5,921 | -719 | -10.8% |
| Upper-middle | 16,693 | 15,174 | -1,519 | -9.1% |
| Emerging | 47,803 | 45,388 | -2,415 | -5.1% |
| **Frontier** | **28,678** | **18,877** | **-9,801** | **-34.2%** |
| SIDS | 1,371 | 1,097 | -274 | -20.0% |
| **Pool total** | **101,185** | **86,457** | **-14,728** | **-14.6%** |

**Giải thích khả dĩ**: Bảng 4.1 đo firms có đủ dữ liệu năng suất (productivity-complete), còn Mục 4.1 đo tổng pool. Nhưng **chênh 34% ở Frontier là bất thường**.

**Thêm vấn đề**: Cột "Cặp QG×năm" trong Bảng 4.1 cộng bằng **103**, không phải 108 (thiếu 5 cặp).

**Hành động**: (a) Thêm header note cho Bảng 4.1: *"n_firms = số doanh nghiệp có đầy đủ dữ liệu log năng suất; tổng pool = 101,185"*. (b) Giải thích 5 cặp QG×năm thiếu (103 vs 108). (c) Đặc biệt giải thích tại sao Frontier mất 34%.

---

### C4 — P3/P4 labeling đảo ngược: text vs file system

**Vị trí**:
- `thesis/15` Mục 4.4.5.1 và `thesis/16` Mục 5.1: **P3 = Singapore** (Mar et al., 2026 — MIR), **P4 = Việt Nam** (Đỗ & Phan, 2026 — APJM)
- `thesis/14` Mục 1.5: **P3 = Singapore**, **P4 = Việt Nam**
- **File system trong repo**: `p3/p3_vietnam_en_clean.md` đến P3=Việt Nam; `p4/p4_singapore_en_clean.md` đến P4=Singapore
- **Build script comment** (`build_dist.sh`): "P3 = Vietnam (theo content)", "P4 = Singapore (theo content)"

 đến Text luận án và file system **đảo ngược nhau hoàn toàn**.

**Hành động**: Giữ file system (P3=Vietnam, P4=Singapore) và sửa references trong thesis/14+15+16:
- `P3 (Singapore — MIR)` đến `P4 (Singapore — MIR)`
- `P4 (Việt Nam — APJM)` đến `P3 (Việt Nam — APJM)`

Grep trong 3 files: ~12 instances cần đổi.

---

### C5 — Bảng 4.9 Emerging sub-breakdown: VNM n thiếu nhất quán với Mục 5.3

**Vị trí**: `thesis/15` Mục 4.9 Bảng 4.9:
- "Emerging — FDI dẫn dắt SEA (VNM, IDN, PHL)": n_firms = 13,779 — đây là 3 nước gộp
- Mục 5.3 nói Vietnam riêng n=3,077 đến không thể cross-check

**Hành động**: Thêm breakdown country-level vào footnote Bảng 4.9: VNM (n=3,077), IDN (n=~7,500), PHL (n=~3,200) — tổng kiểm tra vs 13,779.

---

## 🟠 MAJOR ISSUES — Nên sửa trước khi nộp

### M1 — Mục 7.3.4 và Mục 7.4 items 1–6 và Mục 7.5: Placeholder text, không có nội dung

**Vị trí**: `thesis/16`
- Mục 7.3.4: `(Giữ nguyên từ v3.1a — xem commit b41dbb8...)` — trống
- Mục 7.4: `(Giữ nguyên từ v3.1a — 6 hạn chế.)` — items 1-6 không được viết ra
- Mục 7.5: `(Giữ nguyên từ v3.1a — 4 giai đoạn...)` — trống

**Mức độ**: Ba sections quan trọng nhất — hạn chế nghiên cứu, hàm ý CĐ2, kế hoạch hoàn thiện — **hoàn toàn trống**.

**Hành động**: Viết đầy đủ nội dung 3 sections này. Ưu tiên Mục 7.4 (hạn chế) vì phản biện luôn đọc section này trước.

---

### M2 — H1–H6 không có directional specification trong CĐ1

**Vị trí**: Mục 4.7 (file 15) và Mục 7.3.4 (file 16) liệt kê H1-H6 chỉ bằng labels:
> "H1 phi tuyến; H2 TCI điều tiết; H3 DAI có điều kiện; H4 phân nhóm con thể chế; H5 cụm tài nguyên; H6 chi phí buộc phải quốc tế hóa"

**Vấn đề**: Không có formal hypothesis statements với (a) predicted sign, (b) named mechanism, (c) operationalization linkage.

**Hành động**: Viết đầy đủ H1-H6 với format. Ví dụ:
> **H1 (phi tuyến)**: FSTS đến log năng suất có dạng inverted-U: β₁>0 (FSTS), β₂<0 (FSTS²); dựa trên Lu & Beamish (2004) — bằng chứng Mục 6.1: điểm uốn VN ~39–46%, TQ ~47–49%.

---

### M3 — CĐ2 sub-regime count: 8 vs 9 (không nhất quán)

**Vị trí**:
- `thesis/16` Mục 7.2: "**CĐ2 mở rộng 9 phân nhóm con**"
- `thesis/15` Mục 4.7(b): "**8 phân nhóm con** với hiệu ứng cố định"
- `thesis/16` Mục 7.3.2: "**Phân loại 8 phân nhóm con cho CĐ2**"

**Hành động**: Thống nhất 1 con số và liệt kê rõ danh sách 8 hoặc 9 sub-regimes.

---

### M4 — Mục 2.3 framing tạo impression H1-H6 unanchored đến khi P6 xong

**Vị trí**: `thesis/14` Mục 2.3:
> "…dự kiến cung cấp pooled effect sizes để **neo thực nghiệm cho các giả thuyết H1–H6**"

**Vấn đề**: Phrasing ngụ ý chỉ P6 mới anchor được H1-H6, trong khi CĐ1 đã cung cấp bằng chứng mô tả mạnh (Chương 4-6).

**Hành động**: Sửa Mục 2.3: *"CĐ1 cung cấp existence evidence cho H1-H6 (Chương 4-6). P6 sẽ bổ sung magnitude evidence từ pooled effect sizes — phân biệt hai vai trò."*

---

### M5 — Mục 4.5.6 Bảng 4.5.6 gender data: explicitly estimates, not calculated values

**Vấn đề**: Bảng 4.5.6 dùng ranges (~26–30%, ~5–8%). Footnote thừa nhận "cần đối chiếu lại với dữ liệu `b7a` gốc".

**Hành động**: Tính actual values từ WBES `b7a`, hoặc đánh dấu rõ và di chuyển vào phụ lục.

---

## 🟡 MINOR ISSUES

### m1 — H7: Mục 1.5 introduce H7 nhưng Mục 4.7 và Mục 7.3.4 chỉ liệt kê H1-H6
**Hành động**: Quyết định H7 có hay không trong CĐ2, thống nhất trong tất cả files.

### m2 — 11 hình minh họa là code references, chưa được generate
**Hành động**: Chạy `python3 thesis/generate_figures.py` trước khi nộp.

### m3 — Bảng 4.1: P90/P10 và P75/P25 marked "(cập nhật GĐ1)" — placeholders
**Hành động**: Điền số thực khi có dữ liệu hoàn chỉnh.

### m4 — Số trang TOC đều là "…"
**Hành động**: Điền khi xuất Word/PDF.

### m5 — R&D Emerging -42.1 đpt chưa decomposed (schema vs thực tế)
**Hành động**: Thêm note tại Mục 4.6 phân biệt schema effect vs xu hướng thực.

---

## ⚪ STYLISTIC ISSUES

- Version tags in body text ("v3.1", "v3.2"…) — xóa trước khi nộp
- Commit hashes in body text ("commit `b41dbb8`"…) — di chuyển vào footnote hoặc xóa
- NotebookLM (2026) cited as primary source 4 lần — thay bằng "tác giả, ghi chú nội bộ"
- "(compressed — xem commit …)" trong table notes — không chuẩn học thuật

---

## MA TRẬN KIỂM TRA NHẤT QUÁN N

| Metric | Mục 4.1 text | Bảng 4.1 | Mục 5.3/5.8 | Mục 4.4.5.1 | Status |
|---|---|---|---|---|---|
| Pool total | 101,185 | 86,457 | — | — | ⚠️ discrepancy |
| Vietnam n | — | — | **3,077** | **2,958** | 🔴 conflict |
| Emerging total | 47,803 | 45,388 | — | — | ⚠️ discrepancy |
| **Frontier total** | **28,678** | **18,877** | — | — | 🔴 34% gap |
| SIDS total | 1,371 | 1,097 | 1,371 | — | ⚠️ discrepancy |
| 2025 cohort | 16,979 | 16,979 (wrong) | — | — | 🔴 sum=17,107 |
| Singapore n | — | — | 623 | 623 | Có consistent |

---

## CROSS-CHAPTER CONSISTENCY: Mục 2.3 ↔ Mục 7.4(8)

| Item | Mục 2.3 (file 14) | Mục 7.4(8) (file 16) | Status |
|---|---|---|---|
| P6 status | "in preparation" | "chưa hoàn thành" | Có consistent |
| P6 role | "empirical anchor H1-H6" | "meta-analysis" | Có consistent |
| CĐ1 substitute method | "systematic narrative review" | "PRISMA 2020" | Có consistent |

---

## HYPOTHESIS FALSIFIABILITY QUICK CHECK

| H | Label | Falsifiable? | Directional? | Theory anchor | Evidence in CĐ1 |
|---|---|---|---|---|---|
| H1 | Phi tuyến I–P | Có (β₂<0) | ⚠️ cần specify | Lu & Beamish (2004) | TP VN 39–46%; TQ 47–49% |
| H2 | TCI điều tiết | Có | ⚠️ cần specify | Cohen & Levinthal (1990) | Bảng 6.1 TCI +0.128 Advanced |
| H3 | DAI có điều kiện | Có | ⚠️ by regime | Verhoef 4-Tier; CDCM | Bảng 6.1 DAI -0.129 Advanced |
| H4 | Phân nhóm con | Có | ⚠️ 8 hay 9 sub? | Hall & Soskice VoC | Bảng 4.1 phân tán divergent |
| H5 | Cụm tài nguyên | Có | ⚠️ cần specify | Hertog (2010) | Mục 5.2 sd log Vịnh 0.31–0.47 |
| H6 | Forced I penalty | Có | Có âm | Briguglio (1995) | Mục 5.7 SIDS Kiribati FSTS 1% |

---

## READINESS SCORE BREAKDOWN

| Dimension | Score | Ghi chú |
|---|---|---|
| Nội dung thực chất | 85% | Rất phong phú, cập nhật 2026 |
| Tính nhất quán số liệu | 45% | 5 Critical discrepancies |
| Completeness | 60% | Mục 7.3.4, Mục 7.4(1-6), Mục 7.5 trống |
| Cấu trúc lý thuyết | 80% | ICRV/CDCM solid; H1-H6 cần formal |
| Trích dẫn & tài liệu TK | 90% | APA 7th nhất quán, coverage đầy đủ |
| **Tổng thể** | **65%** | Draft v3.x — cần 1–2 revision rounds |

---

## ACTION PLAN THEO ƯU TIÊN

### Ưu tiên 1 (trong 1 tuần — Critical):
1. **C4**: Fix P3/P4 labeling (~15 min grep+replace)
2. **C2**: Fix 2025 cohort n 16,979 đến 17,107 trong Mục 4.1 và Bảng 4.10 (~10 min)
3. **C1**: Thêm footnote Vietnam n=3,077 vs n=2,958 distinction (~15 min)
4. **C3**: Thêm header note cho Bảng 4.1 + giải thích 103 vs 108 cặp (~30 min)
5. **C5**: Thêm VNM/IDN/PHL breakdown footnote Bảng 4.9 (~10 min)

### Ưu tiên 2 (trước nộp initial draft):
6. **M1**: Viết đầy đủ Mục 7.3.4 + Mục 7.4 items 1–6 + Mục 7.5
7. **M2**: Formal H1-H6 statements với directional predictions
8. **M3**: Thống nhất 8 vs 9 sub-regimes

### Ưu tiên 3 (trước nộp final):
9. **M4**: Revise Mục 2.3 P6 framing
10. **M5**: Tính actual gender data từ `b7a`
11. **m1–m5**: Minor issues + Stylistic cleanup

---

*Review generated by `phd-dissertation-review` skill | Branch: `claude/edit-vietnamese-academic-standards-xcAmn`*
