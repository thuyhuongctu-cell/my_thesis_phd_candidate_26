# Rà soát toàn bộ việc cần triển khai — P6 & Luận án

> Lập ngày 2026-05-27. Nguồn: tổng hợp các audit trong phiên (PREREG / DISSERTATION / OSF guide),
> quét `[TBD]`/placeholder toàn repo, và MASTER_PLAN.
> **Bối cảnh:** luận án 5 chương (`chuong_1`…`chuong_5`) đang viết *tạm* theo P6 hiện tại
> (k=238/K=288); sẽ điều chỉnh khi P6 mở rộng thật.
>
> Phân loại owner: 🤖 = tôi làm được trong repo · 🧑 = chỉ bạn · 🌐 = chặn bởi nguồn ngoài (DB/PDF/coder/tài khoản)

---

## A. Thượng nguồn — Formal-search expansion (chặn nhiều việc khác) 🌐
| # | Việc | Trạng thái | Owner |
|---|---|---|---|
| A1 | Resolve ~1.065 UNSURE → L2 full-text screening → trích effect-size từ PDF → merge → DB final (mục tiêu k≥250) | Đang dở (tracker 2.467 dòng) | 🌐 cần truy cập WoS/Scopus + PDF bản quyền |
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
| D1 | **Khung H5**: chương tổng hợp viện dẫn Q_M=17,35 của P6 như "xác nhận gradient"; nên ghi "P6 xác nhận *các chế độ khác biệt*, gradient/độ cong do **P7 thực nghiệm** xác lập" | Chờ bạn quyết (a/b/c) — *khuyến nghị HOÃN tới A4 vì P6 mở rộng có thể tự khớp* | 🤖 (sau xác nhận) |
| D2 | File nháp `04_05_chapters_results_discussion_vi.md` trùng lặp với `chuong_4/5` | ✅ **Đã đánh dấu SUPERSEDED** (banner đầu file; không xóa để giữ tham chiếu script/plan) | — |
| D3 | Front matter: trang xác nhận Hội đồng + chữ ký | Hoàn thiện **sau buổi bảo vệ** | 🧑 |
| — | ~~Nhãn phạm vi meta = toàn cầu~~ · ~~đối chiếu số P6~~ · ~~retarget IBR→MRQ~~ | ✅ **Đã xong** phiên này | — |

## E. Hồ sơ bản quyền MAIDA (tiếng Việt) 🧑
| # | Việc | Trạng thái | Owner |
|---|---|---|---|
| E1 | Điền thông tin cá nhân trong `maida_copyright/00_mo_ta_tac_pham_vi.md`: họ tên, ngày sinh, CCCD, địa chỉ, SĐT, email, ngày hoàn thành, năm © | Placeholder `[Điền…]` | 🧑 (dữ liệu cá nhân) |

## F. Các paper khác trong dossier (tham chiếu MASTER_PLAN) 🧑
| # | Việc | Owner |
|---|---|---|
| F1 | Xác nhận status & nộp: P8 (World Dev), P3 (APJM), P4 (MIR), P5 (IJOEM) | 🧑 |

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
