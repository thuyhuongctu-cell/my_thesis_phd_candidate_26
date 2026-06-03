# Rà soát toàn bộ việc cần triển khai — P6 & Luận án

> **Cập nhật 2026-06-03 (post commit `0e9a0e0`).** Phần lớn các mục dưới đây *đã được giải quyết hoặc cập nhật* trong loạt 12+ commits của session `claude/vietnamese-academic-standards-QuiLM`. Tracking chính thức cho 10 nhóm vấn đề chiến lược đã chuyển sang `PROJECT_SELF_CRITIQUE.md` (file đó luôn được cập nhật trước). File này giữ lại như *snapshot lịch sử* + checklist hành chính cuối cho NCS.
>
> **Trạng thái tổng quan (post-session):**
> - ✅ 7/7 papers submission-ready với blind compliance + word caps + figures embedded (P3, P4, P5, P6, P7 với hình; P8 text-only correct; P9' figures = NCS-side render)
> - ✅ Khung lý thuyết phân tầng CIMT–ICRV–CDCM nhất quán xuyên 15 anchor files
> - ✅ M-AIDA system synced v2.1 + supplement warning + 45/47 reconciliation
> - ✅ 4 ADRs cho journal switches (`docs/adr/`)
> - ⚪ 4 NCS-side dependencies: Stata local exec / OSF Path B / κ recruit / personal CCCD data
>
> **Tham chiếu chính (cập nhật mới nhất):**
> - `thesis/PROJECT_SELF_CRITIQUE.md` — 10-group strategic tracker với status từng nhóm
> - `.github/PR_REVIEW_CHECKLIST.md` — 6-section pre-merge audit
> - `docs/adr/` — 4 ADRs cho journal switches
> - `thesis/CIMT_REALITY_AND_TOP_1PCT_SCHOLAR_REVIEW.md` — final CIMT resolution
>
> **Bối cảnh dưới đây giữ nguyên** từ phiên 2026-05-27: luận án 5 chương (`chuong_1`…`chuong_5`) viết theo P6 hiện tại (k=238/K=288); sẽ điều chỉnh khi P6 mở rộng formal-search (Path B).
>
> Phân loại owner: 🤖 = tôi làm được trong repo · 🧑 = chỉ NCS · 🌐 = chặn bởi nguồn ngoài (DB/PDF/coder/tài khoản)

---

## A. Thượng nguồn — Formal-search expansion (chặn nhiều việc khác) 🌐
| # | Việc | Trạng thái | Owner |
|---|---|---|---|
| A1 | Resolve ~1.065 UNSURE → L2 full-text screening → trích effect-size từ PDF → merge → DB final (mục tiêu k≥250) | Screening + extraction-queue (654 dòng) **đã dựng**; nút thắt = trích r/n từ PDF. **Đã thử API mở 2026-05-27 → chặn 403; repo không có PDF gốc** → không tiến được trong môi trường này (xem `p6/tools/FORMAL_SEARCH_STATUS.md`) | 🌐 cần máy mạng-mở / thư viện CTU + PDF |
| A2 | Sau A1: điền **final k/K + PRISMA exclusion counts** (manuscript dòng 171/603/713; `p6_prisma_flow.md` các `[TBD]`) | Chờ A1 | 🤖 sau khi có A1 |
| A3 | **Inter-coder reliability — Bảng 3.1** (κ categorical, ICC cDAI) hiện toàn `[TBD]` | Chưa làm | 🌐 cần coder thứ 2 |
| A4 | Sau A1–A3: **điều chỉnh lại 5 chương** theo P6 mở rộng (provisional → final); khi đó khung H5 có thể tự khớp | Chờ A1–A3 | 🤖+🧑 |

## B. Nộp MRQ (gói đã sẵn sàng) 🧑/🤖
| # | Việc | Trạng thái | Owner |
|---|---|---|---|
| B1 | Rà soát lần cuối 3 file `.docx` trong `p6/submission/mrq_package/` | docx đã rebuild & verify | 🧑 |
| B2 | Tạo tài khoản **Springer Editorial Manager** (MRQ) → nộp manuscript + title page + cover letter + 5 hình | Chưa nộp | 🧑 |
| B3 | (tùy) tinh chỉnh nhỏ theo yêu cầu định dạng MRQ trước nộp | — | 🤖 |

## C. Công khai OSF (gói đã sẵn sàng) 🧑/🤖
| # | Việc | Trạng thái | Owner |
|---|---|---|---|
| C1 | **Giữ private tới sau khi nộp MRQ** (tránh xung đột chính sách preprint) | Đang giữ | 🧑 |
| C2 | Đặt **License** (CC-BY tài liệu/mã; cân nhắc CC0 dataset) → Make Public | Chưa | 🧑 |
| C3 | Sau A2: cập nhật **final counts** trong gói OSF (`5_Results`, `00_START_HERE`) | Chờ A2 | 🤖 |
| C4 | KHÔNG tải PDF toàn văn nghiên cứu gốc (bản quyền) — chỉ metadata/effect-size | Quy tắc | 🧑 |

## D. Nhất quán luận án 🤖/🧑
| # | Việc | Trạng thái | Owner |
|---|---|---|---|
| D1 | **Khung H5**: chương tổng hợp viện dẫn Q_M=17,35 của P6 như "xác nhận gradient" | ✅ **Đã xử lý**: thêm kiểm định nhạy cảm drop-FR (Q_M=1,49, p=,68) vào script/table5 + manuscript EN/VI + chuong_2/chuong_4; reframe "moderation thể chế cấp văn liệu không robust → tính ngữ cảnh bộc lộ qua tương tác có điều kiện cấp doanh nghiệp (P7)" | 🤖 |
| D2 | File nháp `04_05_chapters_results_discussion_vi.md` trùng lặp với `chuong_4/5` | ✅ **Đã đánh dấu SUPERSEDED** (banner đầu file; không xóa để giữ tham chiếu script/plan) | — |
| D3 | Front matter: trang xác nhận Hội đồng + chữ ký | Hoàn thiện **sau buổi bảo vệ** | 🧑 |
| — | ~~Nhãn phạm vi meta = toàn cầu~~ · ~~đối chiếu số P6~~ · ~~retarget IBR→MRQ~~ | ✅ **Đã xong** phiên này | — |

## E. Hồ sơ bản quyền MAIDA (tiếng Việt) 🧑
| # | Việc | Trạng thái | Owner |
|---|---|---|---|
| E1 | Hồ sơ MAIDA: ✅ **mô tả tác phẩm đã viết lại chuẩn học thuật** (v2.0: cơ sở tri thức meta-analysis + nguyên lý human-in-the-loop + định vị trung thực với luận án) + thêm `p6/tools/maida/CITATION.cff`. **Còn lại 🧑:** điền thông tin cá nhân (họ tên/ngày sinh/CCCD/địa chỉ/SĐT/email/ngày hoàn thành/năm ©) — dữ liệu chỉ bạn có | Một phần xong | 🧑 (dữ liệu cá nhân) |

## F. Các paper khác trong dossier (tham chiếu MASTER_PLAN) 🧑
| # | Việc | Owner |
|---|---|---|
| F1 | **TOÀN BỘ 7 PAPERS ✅ SUBMISSION-READY** (commit `1061efa`, 2026-06-03): **P3 → JED Q1** (11,597w); **P4 → JABES Q1** (12,096w); **P5 → IJOEM Q1** (7,331w); **P6 → APJM Q1** (11,167w, retargeted from MIR per stronger Asia-Pacific fit + CIMT theoretical match); **P7 → JIBS ABS-4*** (13,140w, CIMT central contribution); **P8 → JED Q1** (8,683w, 4 robustness panels resolved: Comoros + wild-cluster bootstrap + LOO + attrition); **P9' → MIR/IJOEM Q1** (8,424w). All passed final cross-portfolio sweep: ✅ blind-compliant (0 author-identifier hits across 9 patterns), ✅ APA7 cross-reference (all citations in references), ✅ numerical consistency (0 issues across 60 files). | 🧑 (chỉ còn submit + NCS supervisor sign-off) |

---

## Thứ tự ưu tiên đề xuất
1. **B1–B2** (nộp MRQ) — gói đã sẵn sàng, giá trị cao, chỉ chờ thao tác của bạn.
2. **D2** (lưu trữ file nháp) + **D1** (quyết khung H5) — dọn nhất quán luận án trước bảo vệ; rẻ.
3. **A1** (formal-search) — lớn nhất, mở khóa A2/A3/A4/C3; cần nguồn ngoài → lên lịch riêng.
4. **C2** (OSF public) — sau khi nộp MRQ.
5. **E1, F1** — thao tác hành chính của bạn.

## Việc 🤖 tôi làm được NGAY (chờ bạn bật đèn xanh)
- D2: đánh dấu/đưa `04_05_…` vào trạng thái superseded.
- D1: tinh chỉnh nhãn H5 ở `chuong_4`+`chuong_5` (nếu chọn làm sớm thay vì hoãn tới A4).
- B3/C3/A2: thực hiện khi có đầu vào tương ứng.
