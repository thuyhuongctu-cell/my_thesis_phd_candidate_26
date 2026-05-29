# Formal-search — trạng thái & handoff (thử "nhánh nhỏ" 2026-05-27)

> Mục tiêu thử: đẩy formal-search expansion (k=238 → k≥250) bằng API mở trong môi trường Claude Code.
> Kết quả: **bị chặn tại bước trích xuất**; phần offline làm được thì đã có sẵn. Tài liệu này ghi
> chính xác trạng thái để bàn giao cho máy/người không bị chặn.

## 1. Môi trường chặn gì
| Kênh | Kết quả | Ghi chú |
|---|---|---|
| OpenAlex / Crossref / Semantic Scholar / Unpaywall API | **403 (chặn)** | network policy chỉ cho allowlist; `github.com` = 200 ⇒ chặn chọn lọc, không phải mất mạng |
| PDF nghiên cứu gốc trong repo | **Không có** | 28 PDF trong repo là guides/hội thảo/đào tạo; không có primary-study nào |
| ⇒ Trích effect-size offline | **Không thể** | thiếu cả API lẫn PDF |

## 2. Pipeline đang ở đâu (đã làm được, có trong repo)
- **Screening abstract đã chạy** (`p6/tools/results/abstract_screened_20260520.csv`): từ 1.543 UNSURE →
  **Y = 210**, N = 151, còn UNSURE = 1.182 (≈783 không có abstract nên không screen offline được).
- **Extraction queue đã dựng** (`p6/tools/results/extraction_queue_y_20260520.csv`, 654 dòng): đủ 28 cột
  template (n, converted_r, t_value, conversion_formula, doi_link, google_scholar…), **chứa 207/210
  abstract-Y**. 3 abstract-Y (seq) chưa nằm trong queue → re-run script dựng queue sẽ cuốn vào.
- **`ready_for_r` ≈ 0** (NO/0/EMPTY) ⇒ **chưa trích r/n từ bất kỳ nghiên cứu mới nào**.
- `pdf_status`: LOCAL_PDF=78 (stale, không có file), REPO_URL=76, NO_PDF=500.

## 3. Nút thắt thật & lối gỡ (cần máy/người KHÔNG bị chặn)
Để tăng k cần **trích effect-size từ full-text**, gồm:
1. **Lấy PDF** 654 ứng viên trong queue — dùng truy cập thư viện CTU (institutional) hoặc chạy lại
   các script fetch (`24_fetch_openalex_abstracts_pdfs.py`, `40_batch_download_pdfs.py`,
   `30_oa_check_and_download.py`) ở máy có mạng mở. Ưu tiên 76 dòng `REPO_URL` + các DOI có sẵn.
2. **Trích r / n** từ PDF (thủ công theo codebook, hoặc `41_auto_extract_from_pdfs.py` /
   `32_extract_pdf_stats.py`), điền `converted_r`, `sample_size_n`, `conversion_formula` → bật
   `ready_for_r=YES`.
3. **Merge** các dòng ready vào `p6/data/p6_study_database.csv` (script `42_merge_tracker_to_database.py`),
   gán moderator ICRV/cDAI/DPL còn thiếu, rồi chạy lại `p6/scripts/p6_real_mara.R` (hoặc
   `verify_moderator_qm.py`) → cập nhật k/K + bảng.
4. **Chất lượng mã hóa**: single-coder (không tính κ — đã gỡ Bảng 3.1); đối soát double-entry r/n + mã moderator với PDF gốc. Double-coding để báo κ là việc của đợt mở rộng nếu có coder thứ 2.

## 4. Ước lượng thực tế
- Trần lý thuyết nếu trích hết queue: 238 + tối đa ~210 ⇒ có thể vượt k≥250 **nếu** một phần đáng kể
  có effect-size trích được. Nhưng phụ thuộc tỉ lệ PDF lấy được + tỉ lệ báo cáo đủ thống kê.
- **Không có bước nào trong (1)–(4) chạy được trong môi trường Claude Code hiện tại** (chặn API + không
  có PDF). Đây là việc cho máy có mạng mở / truy cập thư viện, không tự động hóa thêm được ở đây.

## 5. Kết luận
Đã thử nhánh API mở → chặn. Phần offline (screening + dựng extraction queue) **đã hoàn tất từ trước**;
không có thêm bước formal-search nào tiến được trong môi trường này. Bàn giao: dùng `extraction_queue_y_20260520.csv`
làm worklist trích xuất trên máy không bị chặn.
