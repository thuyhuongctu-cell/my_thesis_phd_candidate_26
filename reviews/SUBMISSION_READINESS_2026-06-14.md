# Submission readiness — what the project needs to submit (2026-06-14)

Đánh giá trạng thái và việc cần làm để (A) bảo vệ luận án và (B) nộp từng paper.
Phân loại: 🔴 chặn cứng (phải làm trước khi nộp) · 🟠 cần làm · 🟢 đã xong ·
👤 chỉ tác giả làm được (cần máy/quyết định của NCS).

---

## A. YÊU CẦU XUYÊN SUỐT (áp dụng cho MỌI lần nộp)

| # | Việc | Trạng thái |
|---|---|---|
| A1 | 🔴👤 **Đối chứng Stata** các do-file (`scripts/stata/*.do`) trên máy có license; xác nhận khớp pyfixest. Quy tắc liêm chính yêu cầu trước khi nộp. | Do-file sẵn (3) |
| A2 | 🔴👤 **Xác minh 62 DOI** "from training knowledge": chạy `python3 scripts/verify_dois.py` trên máy có mạng; sửa mọi NOT-FOUND. | Công cụ sẵn |
| A3 | 🟠👤 Tự chạy `python3 scripts/verify_all.py` (14/14) để tự tin cầm kết quả khi phản biện. | Sẵn, 6/6 fast |
| A4 | 🟢 AI-use disclosure: P10, P11 đã có; **cần thêm vào P3–P9** khi nộp (mẫu trong `REPRODUCIBILITY.md`). | Một phần |

---

## B. LUẬN ÁN (bảo vệ)

| # | Việc | Mức |
|---|---|---|
| B1 | **Xác nhận tên người hướng dẫn** — front matter còn placeholder "[NCS xác nhận: TS. Nguyễn Minh Cảnh / PGS.TS. Phan Anh Tú]". | 🔴👤 |
| B2 | **Chốt tiêu đề chính thức** — hiện ghi "(Tiêu đề dự thảo)". | 🔴👤 |
| B3 | Hoàn thiện Lời cảm ơn (đang để trống mẫu). | 🟠👤 |
| B4 | Số liệu canonical nhất quán toàn luận án (50 nền/88.869/43,6%/ba vùng; DAI level-shifter). | 🟢 |
| B5 | Build PDF chuẩn CTU (QĐ 1799): luận án 123tr + CĐ1 58tr + CĐ2 44tr, A4, 0 lỗi glyph. | 🟢 |
| B6 | Slide bảo vệ (19tr) đồng bộ số liệu. | 🟢 |
| B7 | Danh mục TLTK: orphan refs (tùy chọn dọn) + 62 DOI verify (A2). | 🟠 |
| B8 | Phụ lục tái lập + `REPRODUCIBILITY.md` (chống nghi AI). | 🟢 |

**Luận án về bản chất đã sẵn sàng về nội dung/định dạng; chặn cứng chỉ là B1–B2 (thông tin của NCS) + A1 (Stata).**

---

## C. TỪNG PAPER (xếp theo độ sẵn sàng để nộp)

| Paper | Đích | Sẵn sàng | Việc còn lại trước khi nộp |
|---|---|---|---|
| **P9 Ấn Độ** | MIR / IJOEM | ⭐ Cao nhất | A1, A2; format Springer; thừa nhận cross-section (đã có); OSF. **Nộp sớm nhất.** |
| **P10 Nhật Bản** | ABM | Cao | A1; gói nộp đủ (title/cover/docx/pdf) ✓; OSF. |
| **P11 JED (digital divide)** | JED SI "AI" | Cao | A1; chạy `jed_gni_axis.py` (trục thu nhập); **nên mở rộng 4.500→6.000+ từ** (lit review + sector nếu có item); **hạn 31/10/2026**. Gói nộp đủ ✓. |
| **P4 Singapore** | JABS | Trung-cao | A1; đã sửa nhãn TCI + TP; đóng khung "informative null" (đã có); OSF. |
| **P5 Trung Quốc** | IJOEM | Trung-cao | A1; đã hòa giải N; **nên thêm power/equivalence test** (bán "null" làm đóng góp chính); OSF. |
| **P3 Việt Nam** | JABS / JED regular | Trung-cao | A1; đã sửa LaTeX+TP+§; tinh chỉnh khung "inverted-U vs biên tham gia"; OSF. |
| **P7 Capstone** | IBR (không JIBS) | Trung | A1; đã tái ước lượng + viết lại đầy đủ ✓; **rà prose lần cuối**; OSF. |
| **P6 Meta** | IBR / JIM | Trung-thấp | 🔴👤 **ICR κ** (cần dữ liệu double-coding của NCS) + điền sơ đồ PRISMA cuối; **đối chứng R/metafor** (thay Stata); OSF (nhãn "registered analysis plan"). **Hạng mục lớn nhất còn lại.** |

---

## D. VIỆC TÔI CÓ THỂ LÀM TIẾP TRONG CONTAINER (nếu NCS muốn)

1. **Mở rộng P11 (JED) lên 6.000+ từ** — nhưng cần item ngành (a4a không đáng tin) hoặc trục GNI (mạng chặn) → phần còn lại cần NCS/máy mạng. Có thể đào sâu lit review + intro.
2. **Tạo gói nộp đầy đủ cho P6/P7/P8/P9** (title page + cover letter + AI-disclosure + docx) như P10/P11.
3. **Format từng paper theo template tạp chí đích** (Springer cho MIR; Emerald cho JABS/IJOEM/JED).
4. **Dựng skeleton OSF** từng paper (đã có hướng dẫn `osf/OSF_PROJECT_STRUCTURE.md`).
5. **Điền sơ đồ PRISMA P6** từ số liệu narrative đã có (line 169).
6. **Thêm AI-disclosure** vào P3–P9.
7. **Dọn orphan references** (nếu NCS quyết định).

## E. VIỆC CHỈ NCS LÀM ĐƯỢC (ngoài container)

- 👤 Đối chứng Stata (A1) · Verify 62 DOI (A2) · Tên GVHD + tiêu đề (B1–B2) · ICR κ P6 (cần double-coding) · Đẩy M-AIDA lên GitHub+Zenodo · Quyết định đích tạp chí cuối.

---

## Khuyến nghị trình tự
1. **NCS cung cấp:** tên GVHD + tiêu đề chính thức (B1–B2) → mở khóa luận án.
2. **NCS chạy 1 lần trên máy:** `verify_all.py`, `verify_dois.py`, đối chứng Stata (A1–A3).
3. **Nộp sớm:** P9 → P10 → P11 (kịp hạn JED 31/10).
4. **Tôi (trong container):** dựng gói nộp P7/P8/P9 + OSF skeleton + AI-disclosure + format tạp chí, song song.
