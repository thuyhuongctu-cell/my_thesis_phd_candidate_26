# Lộ trình hoàn thành chương trình tiến sĩ — bản đồ tuần tự

> **Cập nhật 2026-06-03 (post commit `0e9a0e0`).** Lập 2026-05-28; updated end of finalization session với 12+ commits resolving 6 strategic groups (PROJECT_SELF_CRITIQUE B/C/D/G/H/I). Bổ trợ cho `OUTSTANDING_ISSUES.md` (bảng việc) và `PROJECT_SELF_CRITIQUE.md` (10-group strategic tracker).
> Owner: 🤖 = tôi (trong repo) · 🧑 = NCS · 🌐 = nguồn ngoài (PDF / mạng-mở / coder / tài khoản).

## Trạng thái nền (post-session 2026-06-03)
- ✅ 5 chương + tóm tắt + CĐ1 + CĐ2 viết xong, humanized, em-dash count 0 trong inserts mới.
- ✅ 7 bản thảo tiếng Anh P3–P9' qua stop-slop + humanizer; CIMT–ICRV–CDCM hierarchy nhất quán xuyên 15 anchor files (Ch.1/2/5 + CĐ1/CĐ2 + tomtat + cumulative + defense + 4 papers + cover + refs + README + M-AIDA).
- ✅ 7 submission packages structurally complete (manuscript + title + cover + figures + README + replication). All blind-clean: 0/11 author-identifier hits.
- ✅ Word counts: P3 11597 / P4 12096 / P5 7238 / P6 11384 / P7 12085 / P8 8784 / P9' 8424 — toàn bộ within journal caps với ≥200w buffer.
- ✅ M-AIDA v2.1 description synced với CIMT framing; SHA-256 file integrity confirmed; supplement warning banner enforced.
- ✅ 4 ADRs documented (`docs/adr/`) cho journal switches.
- ⚪ NCS-side outstanding: Stata local exec / OSF Path B (k≈600-700) / κ second coder / supplement_s_maida [TO FILL] fields.

---

## GIAI ĐOẠN 1 — Nộp được ngay (không phụ thuộc formal-search)
**Mục tiêu:** đưa các sản phẩm đã chín vào quy trình bình duyệt.

| Bước | Việc | Phụ thuộc | Owner |
|---|---|---|---|
| 1.1 | **Nộp P6 → MRQ** (Springer Editorial Manager): manuscript_blinded + title_page + cover_letter + 5 hình | xem ⚠️ chặn dưới | 🧑 |
| 1.2 | **Nộp 7 papers — TOÀN BỘ ✅ READY** (commit `1061efa`, 2026-06-03): **P3 → JED Q1** (11,597w); **P4 → JABES Q1** (12,096w); **P5 → IJOEM Q1** (7,331w); **P6 → APJM Q1** (11,167w, NEW retarget from MIR); **P7 → JIBS ABS-4*** (13,140w, CIMT central); **P8 → JED Q1** (8,683w, 4 robustness panels resolved); **P9' → MIR/IJOEM Q1** (8,424w). 7/7 pass blind + APA7 + consistency sweep. Recommended submission order: P5 + P9' first (cleanest, fastest review); P3 + P8 next (JED parallel); P4 (JABES Emerald); P6 (APJM Springer); P7 (JIBS — most ambitious, last). | — | 🧑 |
| 1.3 | Điền thông tin cá nhân vào hồ sơ MAIDA → nộp Cục Bản quyền (COV) | — | 🧑 |

> ✅ **Hướng (b) ĐÃ THỰC HIỆN (2026-05-28):** manuscript được reframe — corpus phân tích là **k=238/K=288
> (Path A: backward/forward citation tracking 5 anchor meta + hand-search)**; WoS/Scopus database search
> được trình bày là **Path B — mở rộng đã đăng ký, trích xuất đang tiến hành, KHÔNG thuộc effect đang
> phân tích**. Đã gỡ mọi `[TBD]` "pending extraction" ở PRISMA narrative + Appendix A; abstract sửa lại
> đúng provenance (không còn quy k=238 cho WoS/Scopus search). **Không bịa số** — các số 238/288/497/478/19
> lấy từ `p6_prisma_flow.md`.
>
> ⚠️ **Còn lại trước khi nộp P6:**
> - **Bảng 3.1 ICR** vẫn `[TBD]` (theo bạn chọn "giữ, xử lý sau") — cần coder thứ 2 hoặc quyết trình bày
>   single-coder như giới hạn. Đây là việc duy nhất còn chặn 1.1.
> - **🧑 cần xác minh sự thật:** §3.2 hiện ghi "two independent screeners… third reviewer" và §3.3.2 ghi
>   "both coders independently coded". Nếu thực tế là **PI + script** (single), hai câu này phải sửa cho
>   đúng (tôi 🤖 sửa sau khi bạn xác nhận) — tránh khẳng định quy trình chưa thực sự diễn ra.

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
