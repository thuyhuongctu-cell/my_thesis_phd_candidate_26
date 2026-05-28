# Lộ trình hoàn thành chương trình tiến sĩ — bản đồ tuần tự

> Lập 2026-05-28. Bổ trợ cho `OUTSTANDING_ISSUES.md` (bảng việc chi tiết). File này sắp xếp việc
> theo **trình tự + phụ thuộc + chủ thể**, để biết làm gì trước, cái gì khoá cái gì.
> Owner: 🤖 = tôi (trong repo) · 🧑 = bạn · 🌐 = cần nguồn ngoài (PDF / mạng-mở / coder / tài khoản).

## Trạng thái nền (đã xong phiên này)
- ✅ 5 chương + tóm tắt + CĐ1 viết xong, đã humanize (gỡ em-dash văn xuôi; số liệu/bảng/trích dẫn nguyên vẹn).
- ✅ 6 bản thảo tiếng Anh P3–P8 qua stop-slop; khung H5 ở `chuong_5` đã khớp `chuong_4` và bản P6 (P6 = "các chế độ khác biệt"; P7 = hình dạng gradient/độ cong).
- ✅ Gói nộp MRQ dựng xong; hồ sơ bản quyền MAIDA (mô tả + CITATION.cff) chuẩn học thuật.

---

## GIAI ĐOẠN 1 — Nộp được ngay (không phụ thuộc formal-search)
**Mục tiêu:** đưa các sản phẩm đã chín vào quy trình bình duyệt.

| Bước | Việc | Phụ thuộc | Owner |
|---|---|---|---|
| 1.1 | **Nộp P6 → MRQ** (Springer Editorial Manager): manuscript_blinded + title_page + cover_letter + 5 hình | xem ⚠️ chặn dưới | 🧑 |
| 1.2 | Nộp các paper khác theo MASTER_PLAN: P8→World Dev, P3→APJM, P4→MIR, P5→IJOEM | — | 🧑 |
| 1.3 | Điền thông tin cá nhân vào hồ sơ MAIDA → nộp Cục Bản quyền (COV) | — | 🧑 |

> ⚠️ **Chặn nộp P6 (1.1):** manuscript còn `[TBD]` ở **Bảng 3.1 (inter-coder reliability)** và **PRISMA
> final counts**. Phải xử lý một trong hai hướng trước khi nộp:
> - (a) Hoàn tất GĐ2–GĐ3 (formal-search + coder thứ 2) rồi điền số thật; hoặc
> - (b) **Quyết định nộp trên corpus hiện tại k=238/K=288**: bỏ phần "PRISMA search đang tiến hành",
>   trình bày k=238 là corpus cuối (hand-search + backward citation), và hoặc có ICR trên mẫu đã code
>   hoặc nêu rõ giới hạn single-coder. ← **cần bạn quyết (🧑); tôi 🤖 thực thi việc viết lại sau khi chọn.**

## GIAI ĐOẠN 2 — Formal-search expansion (nút thắt lớn nhất) 🌐
**Mục tiêu:** k=238 → k≥250, mở khoá final counts + ICR + điều chỉnh chương.

| Bước | Việc | Phụ thuộc | Owner |
|---|---|---|---|
| 2.1 | Trích r/n từ PDF cho ~207 nghiên cứu trong `extraction_queue_y_20260520.csv` | máy **mạng-mở** + **PDF nghiên cứu gốc** (môi trường này chặn API 403, repo không có PDF) | 🌐🧑 |
| 2.2 | Merge → DB final → tính lại pooled r, Q_M, trim-and-fill trên k mới | 2.1 | 🤖 |
| 2.3 | **Inter-coder reliability**: coder thứ 2 code 20% mẫu → κ, ICC → điền Bảng 3.1 | coder thứ 2 | 🌐🧑 |
| 2.4 | Điền **final k/K + PRISMA exclusion counts** (manuscript + `p6_prisma_flow.md`) | 2.2 | 🤖 |

## GIAI ĐOẠN 3 — Đồng bộ luận án theo P6 mở rộng
| Bước | Việc | Phụ thuộc | Owner |
|---|---|---|---|
| 3.1 | Cập nhật số P6 trong 5 chương + tóm tắt (provisional → final) | 2.2–2.4 | 🤖 |
| 3.2 | Cập nhật gói OSF (`5_Results`, `00_START_HERE`) theo final counts | 2.4 | 🤖 |
| 3.3 | OSF: đặt License (CC-BY; cân nhắc CC0 dataset) → Make Public **sau khi nộp MRQ** | 1.1 | 🧑 |

## GIAI ĐOẠN 4 — Bảo vệ
| Bước | Việc | Phụ thuộc | Owner |
|---|---|---|---|
| 4.1 | Hoàn thiện front matter: trang xác nhận Hội đồng + chữ ký | sau bảo vệ | 🧑 |
| 4.2 | Chuẩn bị slide/bài trình bày bảo vệ (tôi hỗ trợ dựng từ 5 chương) | 3.x | 🤖+🧑 |

---

## Đường tới hạn (critical path)
**GĐ2.1 (trích PDF) là nút thắt** khoá 2.2→2.4→3.1→3.2. Cần lên lịch chạy ở **máy mạng-mở + có PDF
thư viện CTU**. Trong khi chờ, GĐ1 (nộp MRQ theo hướng (b), nộp các paper khác, hồ sơ MAIDA) chạy
song song được ngay.

## Việc 🤖 tôi làm được ngay khi bạn bật đèn xanh
- Viết lại phần PRISMA/ICR của P6 theo hướng (b) nếu bạn chọn nộp trên k=238.
- Dựng khung slide bảo vệ từ 5 chương.
- Sau khi có đầu vào GĐ2: tính lại số liệu, điền placeholder, đồng bộ chương + OSF.
