# DANH MỤC HỒ SƠ NỘP — LUẬN ÁN TIẾN SĨ

**Nghiên cứu sinh:** Đỗ Thùy Hương · **Hướng dẫn:** PGS.TS. Phan Anh Tú
**Đề tài:** Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp ở châu Á
**Ngày tổng hợp hồ sơ:** 2026-05-28

Đây là bộ hồ sơ đầy đủ, tổng hợp toàn bộ tài liệu của luận án vào một thư mục để nộp. Mọi tệp DOCX/PDF được dựng từ bản nguồn Markdown mới nhất; mọi tệp dữ liệu lấy từ bộ dữ liệu phân tích cuối.

---

## Cấu trúc thư mục

| Thư mục | Nội dung | Định dạng |
|---|---|---|
| `01_LUAN_AN/` | Luận án đầy đủ (`LUAN_AN_FULL_vi`) + 5 chương riêng + tài liệu tham khảo APA7 | DOCX + PDF |
| `02_TOM_TAT/` | Tóm tắt luận án | DOCX |
| `03_CHUYEN_DE/` | Chuyên đề 1 (CĐ1) + Chuyên đề 2 (CĐ2) | DOCX + PDF |
| `04_BAI_BAO_VI/` | 6 bài báo thành phần P3–P8 (bản tiếng Việt) | DOCX + PDF |
| `05_BAI_BAO_EN/` | 6 bài báo thành phần P3–P8 (bản tiếng Anh) | DOCX + PDF |
| `06_DU_LIEU_OSF_P6/` | Bộ dữ liệu công bố OSF cho meta-analysis P6 + bảng kết quả + báo cáo tái lập | CSV + MD |

**Bài báo thành phần (P3–P8):** P3 Việt Nam · P4 Singapore · P5 Trung Quốc · P6 Meta-analysis · P7 đa quốc gia (capstone) · P8 Pacific SIDS.

---

## Tiêu chuẩn áp dụng

- **Luận án + chương + tóm tắt + chuyên đề (tiếng Việt):** định dạng CTU theo Quyết định 1799/2021 (A4, Times/Liberation Serif 13pt, lề 3-2-2-2 cm, giãn dòng 1,2).
- **Bài báo tiếng Anh (P3–P8):** chuẩn Scopus/WoS — biến số/ký hiệu thống kê định dạng LaTeX (β → $\beta$, R² → $R^2$, FSTS_c² × DAI_z → $\text{FSTS}_c^2 \times \text{DAI}_z$), không còn ký hiệu Unicode rời trong câu văn, không mũi tên (→ thay bằng chữ); ngôn ngữ học thuật đã kiểm.
- **Tài liệu tham khảo:** APA 7th (297 mục, đã đối chiếu chéo với mọi trích dẫn inline).

## Trạng thái rà soát (kiểm bằng công cụ trong `scripts/`)

| Hạng mục | Công cụ | Kết quả |
|---|---|---|
| Nhất quán số liệu cốt lõi (50 file) | `check-consistency.py` | ✅ 0 vấn đề |
| Trích dẫn ↔ tài liệu tham khảo APA7 | `format-apa7.py` | ✅ 297 mục, mọi citation đều có entry |
| Ngôn ngữ học thuật (6 bài báo EN) | `academic_language_check.py` | ✅ 0 lỗi |
| Thuật ngữ song ngữ VI (6 bài báo) | `audit_vn_glossary.py` | ✅ 0 thuật ngữ dịch sai; theo glossary chuẩn v1.4 (chính tả hiện đại "hóa", "áp dụng số") |
| Đồng bộ DOCX/PDF với bản nguồn | so khớp commit | ✅ toàn bộ deliverable đã build lại từ source mới nhất |

## Ghi chú phiên cập nhật gần nhất (P6 — meta-analysis)

Bổ sung kiểm định độ vững **drop-Frontier** cho điều tiết thể chế ICRV: omnibus toàn mẫu có ý nghĩa (Q_M = 17,35, p = ,002) nhưng **không bền vững** — bỏ ô Frontier (k = 3) thì về không có ý nghĩa (Q_M = 1,49, df = 3, p = ,68). Diễn giải đã được điều chỉnh nhất quán ở P6 (EN/VI), Chương 2/4/5 và tóm tắt: điều tiết thể chế trực tiếp ở cấp văn liệu là yếu/không robust; tính ngữ cảnh thể chế được xác lập robust ở cấp doanh nghiệp qua **tương tác có điều kiện** (FSTS×ICRV, p < ,001). Xem `06_DU_LIEU_OSF_P6/table_icrv_dropFR_sensitivity.csv` và `p6_reproduction_validation.md`.

---

*Tổng: 55 tệp. Bộ hồ sơ này tự chứa, không phụ thuộc tệp ngoài thư mục. Mọi DOCX/PDF được dựng lại từ bản nguồn mới nhất; chương 2 và CĐ2 đã nhúng mô hình khái niệm thống nhất CDCM (Hình 2.1).*
