# Upload Index — bộ nộp đầu tiên cho từng paper (P3–P9)

**Cập nhật:** 2026-06-10. Mỗi paper liệt kê **tạp chí nộp đầu tiên (Reach)**, các file cần upload (đường dẫn chuẩn trong repo), bản dịch VI, house style, và **cổng cần NCS xử lý trước khi nộp**. Tên tạp chí chỉ nêu chính thức sau khi được chấp nhận (Đ.15). Không nộp đồng thời; theo thang Reach → Target → Safe trong `reviews/JOURNAL_TARGETING_PLAN.md`.

> Lưu ý: đây là *chỉ mục* trỏ tới file gốc (tránh trùng lặp/lệch bản). Upload trực tiếp từ các đường dẫn dưới.

---

### P3 — Việt Nam → **MBR** (Emerald, Harvard)
- Manuscript (blinded): `p3/submission/mbr_package/01_manuscript_blinded.md` (.docx)
- Title page: `p3/submission/mbr_package/02_title_page.docx` · Cover: `…/03_cover_letter.docx`
- Bản dịch VI: `p3/submission/p3_vietnam_vi.docx`
- ✅ Đã xác minh sạch (p .660 nhất quán; WB 2025b/c đã có trong reflist). JED dùng `01_manuscript_blinded_8500` nếu xuống JED do giới hạn từ.

### P4 — Singapore → **MIR** (Springer, APA)
- Manuscript: `p4/submission/mir_package/01_manuscript_blinded.md` (.docx)
- Title page + Cover: `p4/submission/mir_package/02_title_page.docx`, `03_cover_letter.docx` *(mới tạo 2026-06-09)*
- Bản dịch VI: `p4/submission/p4_singapore_vi.docx`
- ✅ Đã sạch: Leon (2004) đã gỡ (2026-06-10, quyết định NCS) — thay bằng Cohen (1988) + Aguinis et al. (2005) sẵn có trong reflist. 18%/N=84 đã làm rõ (complete-case).

### P5 — Trung Quốc → **IJOEM** (Emerald, Harvard)
- Manuscript: `p5/submission/ijoem_package/01_manuscript_blinded.md` (.docx)
- Title page *(mới tạo)*: `…/02_title_page.docx` · Cover: `…/03_cover_letter.docx`
- Bản dịch VI: `p5/submission/p5_china_vi.docx`
- ✅ Đã xác minh: 49.4% khớp pipeline chuẩn `results_coefs.csv` — không cần sửa.

### P6 — Meta-analysis → **JWB** (Elsevier, APA)
- Manuscript: `p6/submission/jwb_package/01_manuscript_blinded.md` (.docx) · Title + Cover: `…/02_title_page.docx`, `03_cover_letter.docx`
- Bản dịch VI: `p6/submission/p6_meta_vi.docx`
- ⏳ **Cổng chính (đường găng):** điền κ/ICC (mã hóa kép 2 tác giả) vào 6 ô `[insert after dual-coding]`; đăng ký OSF → DOI. *(Off-by-one đã sửa — lỗi gõ count, không cần chạy lại Q_M.)*

### P7 — Capstone → **JIBS** (Springer, APA)
- Manuscript: `p7/submission/jibs_package/01_manuscript_blinded.md` (.docx)
- Title + Cover: `p7/submission/jibs_package/02_title_page.md`, `03_cover_letter.md`
- Bản dịch VI: `p7/submission/p7_capstone_vi.docx`
- ⏳ Trước nộp: không có cổng dữ liệu lớn; chỉ rà ref/format cuối.

### P8 — Pacific SIDS → **World Development** (Elsevier, APA)
- Manuscript: `p8/submission/world_development_package/01_manuscript_blinded.md` (.docx) · Title + Cover: `…/02_title_page.docx`, `03_cover_letter.docx`
- Bản dịch VI: `p8/submission/p8_pacific_sids_vi.docx`
- ✅ Bảng 1 ĐÃ điền (tính từ WBES data, tái tạo N=959); estimation N=209 đã minh bạch ở abstract/§4/Conclusion.

### P9 — Ấn Độ → **MIR** (Springer, APA; abstract **unstructured**) · *(IJOEM/JABS dùng abstract 7 mục Emerald)*
- Manuscript: `p9_india/submission/mir_package/01_manuscript_blinded.docx` (kèm 4 hình nhúng)
- Title + Cover: `…/02_title_page.docx`, `03_cover_letter.docx`
- Bản dịch VI: `p9_india/submission/p9_india_vi.docx`
- ✅ Đã thêm ref Hutzschenreuter & Voll (2008), JIBS 39(1), 53–70.

---

## Ghi chú hồ sơ chưa hoàn chỉnh (KHÔNG phải target nộp đầu)
- **P3 `jabs_package`**: ✅ đã dựng đầy đủ (4 hồ sơ P3 hoàn chỉnh).
- **P6 `ibr_package`**: là hồ sơ **legacy** (P6 đã rời IBR → JWB theo kế hoạch); còn manuscript, thiếu title/cover. 3 hồ sơ hiện hành của P6 là JWB/JIM/APJM.

## Trạng thái sẵn sàng nộp (sau khi xử lý cổng ⏳ tương ứng)
| Paper | Reach | Hồ sơ đầy đủ? | Cổng còn lại |
|---|---|:--:|---|
| P3 | MBR | ✅ | đã sạch |
| P4 | MIR | ✅ *(vừa bổ sung title/cover)* | đã sạch |
| P5 | IJOEM | ✅ | đã sạch |
| P6 | JWB | ✅ | **lớn (κ/ICC + OSF + Q_M)** |
| P7 | JIBS | ✅ | không đáng kể |
| P8 | World Development | ✅ | đã sạch |
| P9 | MIR | ✅ | đã sạch |

→ **Sẵn sàng nhất:** P7, P5, P3, P9 → P4 → P8 → **P6 (cuối, đường găng)**.
