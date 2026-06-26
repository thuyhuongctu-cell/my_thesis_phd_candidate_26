# P6 — Ghi chú bàn giao Phase B (cô triển khai trên máy có mạng)

**Cập nhật:** 2026-06-26 · **Trạng thái:** Phase A (chuẩn bị trong container) đã xong & đẩy lên PR #17.
**Nhánh:** `claude/phd-thesis-review-L9Gml`

---

## Đã xong (Phase A — không cần làm lại)

- **S238 đã đóng khe k=238.** Thêm "Srividhya & Vidya (2024), *Journal of Economic Integration, 39*(2),
  https://doi.org/10.11130/jei.2024033" vào `thesis/phu_luc_D_p6_primary_studies_vi.md` và
  `p6/p6_study_database_coded.md`. Nguồn: `forest_data.csv` (study_id S238, E288) + hồ sơ WoS/Crossref
  của dự án (`p6/data/p6_study_database.csv`, WoS 001303672500007). Phụ lục D nay đủ 238 dòng.
- **Worklist hoàn thiện trích dẫn:** `reviews/P6_completion_worklist_2026-06-26.md`
  - 103 stub còn lại, phân loại: **52 Type V** (đã có DOI ứng viên trong repo → chỉ xác nhận) +
    **51 Type L** (tra từ đầu).
  - 27 orphan kèm bảng quyết định cite-or-remove (Phần 2 của file).

## Cô cần làm (Phase B — máy có mạng)

1. **Chạy kiểm DOI:**
   ```bash
   python3 scripts/verify_dois.py thesis/phu_luc_D_p6_primary_studies_vi.md
   python3 scripts/verify_dois.py thesis/04_references_apa7.md
   # → reviews/doi_verification_report.md (PASS / TITLE-MISMATCH / NOT-FOUND)
   ```
   Xử lý mọi dòng NOT-FOUND / TITLE-MISMATCH.

2. **Hoàn thiện 103 stub** theo `reviews/P6_completion_worklist_2026-06-26.md`:
   - **Type V (52):** mở DOI ứng viên trên Crossref/WoS, xác nhận đúng bài → điền cột
     "Trích dẫn đã xác minh", đánh dấu Verified.
   - **Type L (51):** tra WoS/Scopus bằng tác giả–năm + tạp chí → lấy trích dẫn đầy đủ + DOI.
   - Dán trích dẫn đã xác minh vào `thesis/phu_luc_D_p6_primary_studies_vi.md`, thay phần
     `*[cần xác minh đầy đủ từ WoS/Scopus/Crossref]*`.

3. **27 orphan:** duyệt bảng quyết định (Phần 2 worklist) → cite tại vị trí gợi ý hoặc bỏ khỏi
   `thesis/04_references_apa7.md`.

## Phase C — gửi lại cho tôi (trong container)

Sau khi cô có trích dẫn đã xác minh, gửi lại → tôi sẽ: nhập vào Phụ lục D, tái sinh
`latex/ctu/LUAN_AN_CTU.tex` + `dist/word/LUAN_AN_vi.docx`, chạy `check-consistency.py` +
`reference_audit.py`, dựng PDF kiểm chứng, commit & push.

## Nguyên tắc bất biến
KHÔNG bịa trích dẫn/DOI từ trí nhớ. Mọi trích dẫn đầy đủ phải đối chiếu WoS/Scopus/Crossref.

## File liên quan
- `reviews/P6_completion_worklist_2026-06-26.md` — worklist chính (103 stub + 27 orphan)
- `reviews/APA7_orphan_doi_audit_2026-06-26.md` — chi tiết 27 orphan
- `scripts/verify_dois.py` — kiểm DOI online
- `thesis/phu_luc_D_p6_primary_studies_vi.md` — Phụ lục D (238 nghiên cứu)
