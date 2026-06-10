# Kiểm tra liêm chính số liệu — Luận án 5 chương + 2 Chuyên đề (2026-06-10)

Rà soát **trạng thái hiện tại** (sau các sửa đổi 06-08/06-09), đối chiếu số liệu trong văn bản với **dữ liệu thật** `data_wbes/p7/p7_pooled_clean.csv`. Bổ sung cho `REVIEW_luan_an_vi_2026-06-07.md` (đã nêu MAJOR REVISION) — nhiều vấn đề M1 cũ **đã được khắc phục**.

> Nguyên tắc: không bịa. Các điểm lệch dưới đây cần **tác giả** quyết định quy tắc gộp/lọc; máy chỉ đối chiếu và flag, không tự điền.

---

## A. ✅ ĐÃ NHẤT QUÁN (cải thiện rõ so với review 06-07)
- **"49 nền kinh tế"** nhất quán toàn bộ 5 chương (hết mâu thuẫn 47 vs 49).
- **k = 113** nhất quán (Ch2/Ch4/Ch5).
- **N = 959** cho mẫu phân tích Pacific SIDS — nhất quán (Ch3/Ch5) và **khớp đúng** với bài P8 đã tái xác minh.
- **N_SIDS 1.371 vs 1.469** không còn xuất hiện trong các chương (đã dọn).

## B. ⚠️ ĐIỂM CẦN TÁC GIẢ LÀM RÕ

### B1. Số nền kinh tế: văn bản "49" vs dữ liệu "52"
Dữ liệu `p7_pooled_clean.csv`:
- 55 giá trị `country` thô, nhưng **3 là bản trùng do dựng panel**: `Mongolia_panel`, `Nepal_panel`, `Philippines_panel` (đã có Mongolia/Nepal/Philippines riêng) → **không phải nền kinh tế độc lập**.
- → **52 nền kinh tế thật**, khớp tổng 6 regime ICRV: Advanced_innovation 6 · Advanced_resource 6 · Emerging 17 · Lower_mid_transition 7 · SIDS_small 9 · Upper_mid 7 = **52**.
- Luận án ghi **49** → còn lệch **3 nền kinh tế**.

**Khả năng (NCS xác nhận):** "49 nền kinh tế **châu Á và Pacific**" có thể đã loại (a) Comoros (Ấn Độ Dương/châu Phi, không thuộc Á–TBD) + TimorLeste khỏi nhóm headline, và/hoặc (b) Oman (rớt khi yêu cầu biến focal). Cần nêu rõ **quy tắc gồm/loại** ở §3 và bảng thành phần regime sao cho tổng = 49 (hoặc sửa "49" cho khớp 52 nếu thực tế dùng đủ).
> Cảnh báo kỹ thuật: nếu code đếm `df.country.nunique()` sẽ ra **55** (gồm 3 `_panel`). Cần lọc hậu tố `_panel` trước khi đếm/báo cáo số nền kinh tế.

### B2. SIDS "9" (Ch2) vs "7 nước" (Ch3) — ✅ ĐÃ SỬA (2026-06-10)
Nhãn bảng Ch2 đã đổi: *"P8 — Pacific SIDS (mẫu chính 7 nước, N=959; kiểm định độ vững mở rộng 9 nước Nhóm VI)"* — khớp Ch3 + bài P8; đồng bộ `thesis/` + `dist/source_md/` + docx. Nội dung gốc bên dưới để tham chiếu.


- Dữ liệu: regime `SIDS_small` = **9 nền kinh tế** (Comoros, Fiji, Kiribati, PNG, Samoa, Solomon, TimorLeste, Tonga, Vanuatu).
- Bài P8 + Ch3: **mẫu chính = 7 nước Pacific**, N=959 (loại Comoros + TimorLeste); 9-nước chỉ là **robustness** (N≈1.469).
- → Dòng bảng Ch2 *"P8 — SIDS (9 nền kinh tế, Nhóm VI)"* gán 9 cho P8 dễ gây hiểu nhầm: P8 **chính** phân tích 7 Pacific. **Đề nghị** sửa nhãn thành "Nhóm VI SIDS (regime 9 nền; P8 phân tích 7 nước Pacific, N=959)".

## C. 📋 2 CHUYÊN ĐỀ

### CĐ1 — "Thực trạng HĐKD doanh nghiệp ở Châu Á" (HD: TS. Nguyễn Minh Cảnh)
- Trạng thái: `cd1_review_report.md` đánh giá **~65%, draft v3.x, cần 1–2 vòng revision** (Major + Minor).
- ⚠️ **Số liệu dao động cần đối chiếu:** trong CĐ1 xuất hiện đồng thời "14 quốc gia", "17 nền kinh tế", "40.633", "47.803", và "49 nền". Cần xác định rõ con số nào thuộc phạm vi nào (P1 emerging-Asia = 17 nền/40.633 obs theo Ch3) và thống nhất, tránh người chấm bắt lỗi.

### CĐ2 — "Xây dựng mô hình nghiên cứu I→P" (HD: PGS.TS. Phan Anh Tú)
- Chuyên đề khái niệm (conceptual model), trọng tâm ICRV/khung lý thuyết — không nêu nhiều số mẫu nên ít rủi ro mâu thuẫn số liệu.
- Cần một lượt rà thuật ngữ/khung giả thuyết cho khớp hệ H1–H6/H1b của luận án (như Ch2 đã chuẩn hóa).

---

## D. PHẠM VI ĐÃ LÀM & CHƯA LÀM (minh bạch)
- **Đã làm phiên này:** kiểm tra liêm chính **số liệu** (đối chiếu văn bản ↔ data thật) cho 5 chương + quét nhanh 2 chuyên đề.
- **Chưa làm phiên này:** review học thuật toàn diện 5 chương + CĐ (lập luận, cấu trúc, citation từng đoạn) — đã có bản 06-07; nếu cần, chạy lại `academic-paper-reviewer` trên trạng thái mới.

**Việc NCS cần quyết:** (1) quy tắc 49-vs-52 nền kinh tế + lọc `_panel`; ~~(2) nhãn SIDS 9/7 ở Ch2~~ ✅ ĐÃ SỬA; (3) thống nhất số liệu CĐ1 (14/17/40.633/47.803/49).

---

## E. ✅ Trạng thái 5 vấn đề MAJOR của review 2026-06-07 (kiểm tra lại hôm nay)
| Mã | Vấn đề (06-07) | Trạng thái hiện tại |
|---|---|---|
| M1 | Mâu thuẫn số liệu (47/49, SIDS, N, k) | ✅ Phần lớn đã sửa; còn B1 (49-vs-52) + C (CĐ1) cần NCS |
| M2 | Bản 5 chương thiếu front matter | ✅ Đầy đủ: Cam đoan/Tóm tắt/Abstract/Mục lục/Từ viết tắt/DM Bảng/DM Hình/DM công trình NCS (`00_phan_dau_vi.md`) |
| M3 | Thiếu hình mô hình khái niệm | ✅ Fig 2.1 CDCM có trong §2.5.1, kèm caption đầy đủ |
| M4 | TLTK chưa hợp nhất | ✅ `04_references_apa7.md` hợp nhất ~271 entry APA7 |
| M5 | Hệ giả thuyết rò mã chưa định nghĩa | ✅ H1–H6/H1b + H2b/H4a-b/E1a-b định nghĩa ở Ch2 §2.5 (ghi chú ký hiệu) |

→ Luận án đã từ **MAJOR REVISION** tiến tới **gần sẵn sàng**; chỉ còn các điểm reconcile số liệu (quyết định của NCS) ở B1 + C.
