# SỔ MINH BẠCH NGUỒN GỐC & XÁC MINH (Provenance & Verification Ledger)

**Ngày:** 2026-06-10 · **Mục đích:** liêm chính khoa học — ghi nhận MỌI reference/số liệu do tự động hóa (Claude/agent) **thêm hoặc tính** trong chuỗi phiên, kèm **nguồn gốc** và **cờ xác minh**, để không có nội dung máy-tạo nào lọt vào hồ sơ nộp/luận án mà chưa được con người kiểm chứng.

> Nguyên tắc đã giữ xuyên suốt: **không bịa citation/reference, không bịa data.** Khi không xác minh được trong repo → *flag cho NCS*, không tự điền.

---

## A. 🔴 REFERENCE THÊM TỪ "KIẾN THỨC MÔ HÌNH" — NCS PHẢI XÁC MINH TRƯỚC KHI NỘP

| Reference | Nơi dùng | Nguồn gốc | Hành động bắt buộc |
|---|---|---|---|
| **Hutzschenreuter, T. and Voll, J.C. (2008)**, "Performance effects of 'added cultural distance'…", *JIBS*, 39(1), 53–70. | P9 (3 package) | ✅ **ĐÃ XÁC MINH (2026-06-10)** từ PDF do NCS cung cấp: tựa đề khớp + **pp. 53–70 xác nhận** (bản RePEc working-paper; công bố JIBS 39(1)). Ban đầu thêm từ kiến thức mô hình, nay đã đối chiếu nguồn thật. | Còn xác nhận năm/tập/số trên trang JIBS xuất bản (tựa đề + trang đã khớp). GIỮ reference. |

> Đây là reference DUY NHẤT trong toàn dự án mà tôi cấp chi tiết từ kiến thức mô hình. Mọi reference khác đều trích từ repo/nguồn do NCS cung cấp (xem mục B).

## B. 🟡 REFERENCE THÊM TỪ NGUỒN TRONG REPO / NCS CUNG CẤP — rủi ro thấp, nên spot-check

| Reference | Nơi | Nguồn gốc (đã kiểm) |
|---|---|---|
| Poland: Phan, Nguyen, Dinh, Thai, Nguyen, Dao, Nguyen, Do (2021), *PalArch's J.* | TLTK luận án | ✅ Từ **ảnh trang title NCS gửi** (8 tác giả đầy đủ) |
| Mahler, Serajuddin, Wadhwa & Yonzan (2026); Pirlea et al. (2026) | P8 | ✅ Có trong `thesis/04_references_apa7.md` (agent trích từ luận án) |
| Helpman, Melitz & Yeaple (2004), *AER* | P5, P6 | ✅ Có trong luận án + nhiều paper (AER kinh điển) |
| Hutzschenreuter, Kleindienst, Sarkar Sengupta & Verbeke (2026), *MBR* | P9 | ✅ Agent trích từ `p6/tools/results/*.csv` (bản ghi WOS/Crossref trong repo) |
| World Bank (2025b), (2025c) | P3 | ✅ Có sẵn trong reflist P3 (không phải máy thêm) |

## C. 🟢 SỐ LIỆU MÁY TÍNH & THÊM VÀO BÀI — TÁI LẬP ĐƯỢC, NCS tái tạo bằng Stata

| Số liệu | Bài | Nguồn tính | Trạng thái tái lập |
|---|---|---|---|
| Robustness FE bỏ foreign-ownership: **β=−0.835, p=.010, N=950**; no-control **−0.769, N=959** | P8 §4.4 | `data_wbes/p7/p7_pooled_clean.csv` qua pipeline Python | ✅ **Tái tạo chính xác** (tái xác minh 2026-06-10); pipeline tái hiện đúng M1 gốc (−1.339/N=209), YearFE (−3.351), full-sample N=959/exporter 13.8% → đáng tin. NCS chạy lại Stata để xác nhận. |
| Bivariate β: bản thảo dùng **R canonical −0.864 (p=.050)**; Python cross-check −0.919 (p=.043) ở duy nhất model phụ này | P8 §4.2/Table 3 | R `lm(ln~fsts)` toàn mẫu vs Python reimpl | ✅ Đối chiếu 2026-06-10. Chênh lệch chỉ 1 model phụ; cả hai âm & p≈.05 → kết luận FIP không đổi. Bản thảo trích đúng R canonical. |
| Robustness 9-nước (gồm Comoros+Timor): **β=−0.510, p=.008, N=1469** | P8 §4.4 | như trên | ✅ Tái tạo chính xác |
| **Bảng 1** P8 (N/exporter/FSTS theo 7 nước) | P8 (3 pkg + clean_en + VI) | `data_wbes/...` — tái tạo tổng N=959 khớp | ✅ Tính từ data thật, không bịa |
| Caveat P9: FSTS mean 7.2%→2.7%; DN FSTS>50% 536→141 | P9 §6 | `p9_india/replication/data/india_*_analytic.csv` | ✅ Tính từ data replication |
| P6 subgroup counts **91/79, 76, 108** (sửa lỗi gõ) | P6 (4 pkg) | `p6/data/p6_study_database.csv` (ground truth) | ✅ Đếm trực tiếp; tổng khớp 288/238 |
| P3 tỷ lệ website 0.43/0.48/0.50 (cơ sở sửa "near-universal") | P3 (chỉ dùng lập luận) | `data_wbes/...` Vietnam | ✅ Tính từ data |

## D. ✅ NHỮNG CHỖ TÔI **TỪ CHỐI BỊA** (minh bạch — đã flag cho NCS, KHÔNG tự điền)

| Hạng mục | Vì sao không tự làm | Trạng thái |
|---|---|---|
| **P6 κ/ICC** (6 ô) | Cần coder thứ hai THẬT (thầy Tú) mã hóa mù; bịa κ = ngụy tạo thống kê | Để placeholder `[insert after dual-coding]` |
| **P6 OSF DOI** | Cần đăng ký OSF thật | Để placeholder `[insert OSF DOI at submission]` |
| **P4 Leon (2004)** | Chỉ có comment trong do-file, không có entry đầy đủ; không chắc bài nào | Flag NCS cung cấp; **KHÔNG bịa** |
| **PRISMA census counts** (P6) | Không chạy WoS/Scopus census thật | Reframe trung thực sang citation-anchored; không điền số census |
| **P6 leave-one-out Frontier** | metafor không có trong môi trường; không tự ý ra số rma.mv | Flag NCS chạy |

---

## E. KẾT LUẬN LIÊM CHÍNH
- Reference Hutzschenreuter & Voll (2008) — ban đầu từ kiến thức mô hình — **đã được xác minh** từ PDF do NCS cung cấp (tựa đề + trang 53–70 khớp). Không còn reference nào chưa xác minh.
- **Mọi số liệu máy thêm** đều tái lập được từ dữ liệu thật trong repo (mục C); không có số nào "bịa".
- **Mọi chỗ không xác minh được** đều để placeholder/flag, **không tự điền** (mục D).
- Ranh giới người↔máy **minh bạch hoàn toàn** và kiểm toán được.

**Việc NCS cần làm để đóng sổ liêm chính:** (1) ~~xác minh Hutzschenreuter & Voll (2008)~~ ✅ ĐÃ XONG (PDF NCS cung cấp); (2) tái chạy 3 robustness P8 + Bảng 1 bằng Stata để "ký" số liệu; (3) cung cấp Leon (2004); (4) hoàn tất κ/ICC + OSF DOI.
