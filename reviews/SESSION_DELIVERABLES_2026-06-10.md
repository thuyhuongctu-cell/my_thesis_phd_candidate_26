# Báo cáo bàn giao phiên — 2026-06-10 (cập nhật)

Tổng hợp toàn bộ việc đã thực hiện trong phiên và **các cổng còn lại cần tác giả (NCS)**. Nguyên tắc xuyên suốt: **không bịa citation/reference, không bịa data**; mọi chỗ không xác minh được đều flag, không tự điền.

---

## A. Đã hoàn thành trong phiên (máy làm được, đã commit + push PR #17)

| # | Hạng mục | Commit | Ghi chú |
|---|---|---|---|
| 1 | **Tái xác minh P8 trực tiếp** từ `p7_pooled_clean.csv` (build từ SIDS .dta) | `664d43e` | M1 β=−1.339/N=209, full N=959/13.8% tái hiện exact |
| 2 | **Rà soát .dta toàn bộ nhánh** | — | Xác nhận 7 SIDS .dta KHÔNG có trên bất kỳ nhánh nào; India .dta chỉ ở nhánh `vietnamese-academic-standards-QuiLM` |
| 3 | **Xác minh chéo số đầu bài P3–P9** | `664d43e` | Mọi turning point truy vết tới file kết quả đã commit (xem `CROSS_PAPER_NUMBER_VERIFICATION_2026-06-10.md`) |
| 4 | **Toolkit mã hóa kép P6** (`p6/icr/`) | `5a20a7f` | Rút mẫu k=47 (seed 2026); script tính κ/ICC; từ chối chạy nếu thiếu dữ liệu coder 2; toán đã unit-test |
| 5 | **Gỡ ref Leon (2004) khỏi P4** | `8416f01` | Thay bằng Cohen (1988) + Aguinis et al. (2005) sẵn có; 3 package + clean_en + do-file |
| 6 | **Đồng bộ schema M-AIDA (v7.0.1)** | `9d37f3b` | ICRV sửa về institutional I/II/III/FR/MX; cDAI đến Digital Adoption Index 0–1; DOI/FP enum khớp DB; LLM không còn đoán moderator |
| 7 | **Triển khai `ANTHROPIC_DEFAULT_FABLE_MODEL`** toàn dự án | `c883186` | Chuỗi phân giải `ANTHROPIC_MODEL > ANTHROPIC_DEFAULT_FABLE_MODEL > fallback`; mặc định `claude-fable-5` |
| 8 | Regenerate docx lỗi thời (P4 title, P9 cover) + 4 docx P6 + 3 docx P4 | rải rác | docx đồng bộ với .md |

## B. Trạng thái 7 paper

| Paper | Reach | Sẵn sàng? | Cổng còn lại (tác giả) |
|---|---|:--:|---|
| P3 Việt Nam | MBR | Có | — |
| P4 Singapore | MIR | Có | — *(Leon đã gỡ)* |
| P5 Trung Quốc | IJOEM | Có | — |
| P6 Meta | JWB | ⏳ | **dual-coding κ/ICC + OSF DOI + 3 lệch Bảng 3.1 (mục C)** |
| P7 Capstone | JIBS | Có | — |
| P8 Pacific SIDS | World Development | Có | (tùy chọn) ký lại bằng Stata |
| P9 Ấn Độ | MIR | Có | — |

 đến **6/7 sạch, sẵn sàng nộp.** P6 là đường găng duy nhất.

## C. 🔴 Cổng tác giả còn lại (KHÔNG tự làm — cần quyết định/dữ liệu thật)

### C1. P6 — mã hóa kép (đường găng)
1. Thầy Tú điền `p6/icr/icr_coding_sheet_coder2_BLANK.csv` (47 nghiên cứu, mù).
2. Chạy `python3 p6/icr/02_compute_icr.py` đến ra 6 giá trị κ/ICC.
3. Điền vào 6 ô `[insert after dual-coding]` ở 4 package + bản VI; regenerate docx.
4. Đăng ký OSF đến lấy DOI thật, thay placeholder `[insert OSF DOI at submission]`.

### C2. P6 — 3 điểm lệch Bảng 3.1 (manuscript ↔ database thật)
*(Đã ghi chi tiết trong `p6/icr/README_ICR_VI.md`. Đây là quyết định thiết kế báo cáo của NCS — không tự sửa vì có thể NCS chủ ý gộp nhóm.)*

| Dòng Bảng 3.1 | Bản thảo ghi | Database thật | Cần làm |
|---|---|---|---|
| DOI measure | Categorical **(4)** | **6** loại: FSTS/GEO/EXP/FDI/COMP/OTH | Sửa thành "(6)" HOẶC nêu rõ cách gộp 6 đến 4 |
| cDAI score | **Continuous (0–1), ICC(2,1)** | **ordinal H/M/L** | Bổ sung cột điểm liên tục 0–1, HOẶC đổi dòng thành "Ordinal (3), weighted κ" |
| Industry sector | Categorical (3) | **không có cột industry** | Bổ sung cột & mã hóa, HOẶC bỏ dòng khỏi Bảng 3.1 |

### C3. Các cổng nhỏ khác
- **P8 (tùy chọn):** NCS chạy lại robustness/Bảng 1 bằng Stata để "ký" số (số đã tái lập exact từ data, không bắt buộc trước nộp).
- **Hồ sơ COV M-AIDA:** nếu đã nộp bản mô tả cũ, nộp kèm bản cập nhật v7.0.1; nếu chưa nộp thì dùng thẳng bản trong repo.

## D. Liêm chính — không có nợ
- Mọi reference đã xác minh (Hutzschenreuter & Voll 2008 từ PDF NCS; Leon 2004 đã gỡ).
- Mọi số liệu máy thêm đều tái lập được từ data thật trong repo.
- Mọi chỗ cần con người (κ/ICC, OSF DOI, quyết định schema Bảng 3.1) đều để placeholder/flag, **không bịa**.
- Ranh giới người↔máy minh bạch, kiểm toán được qua `PROVENANCE_VERIFICATION_LEDGER.md`.
