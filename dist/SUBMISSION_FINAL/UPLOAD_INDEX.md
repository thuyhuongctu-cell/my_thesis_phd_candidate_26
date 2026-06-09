# Upload Index — bộ nộp đầu tiên cho từng paper (P3–P9)

**Cập nhật:** 2026-06-09. Mỗi paper liệt kê **tạp chí nộp đầu tiên (Reach)**, các file cần upload (đường dẫn chuẩn trong repo), bản dịch VI, house style, và **cổng cần NCS xử lý trước khi nộp**. Tên tạp chí chỉ nêu chính thức sau khi được chấp nhận (Đ.15). Không nộp đồng thời; theo thang Reach → Target → Safe trong `reviews/JOURNAL_TARGETING_PLAN.md`.

> Lưu ý: đây là *chỉ mục* trỏ tới file gốc (tránh trùng lặp/lệch bản). Upload trực tiếp từ các đường dẫn dưới.

---

### P3 — Việt Nam → **MBR** (Emerald, Harvard)
- Manuscript (blinded): `p3/submission/mbr_package/01_manuscript_blinded.md` (.docx)
- Title page: `p3/submission/mbr_package/02_title_page.docx` · Cover: `…/03_cover_letter.docx`
- Bản dịch VI: `p3/submission/p3_vietnam_vi.docx`
- ⏳ Trước nộp: xác nhận p exporter-only (.660 vs .730); thêm chi tiết ref World Bank 2025b/c; (JED dùng bản `01_manuscript_blinded_8500` nếu chuyển xuống JED do giới hạn từ).

### P4 — Singapore → **MIR** (Springer, APA)
- Manuscript: `p4/submission/mir_package/01_manuscript_blinded.md` (.docx)
- Title page + Cover: `p4/submission/mir_package/02_title_page.docx`, `03_cover_letter.docx` *(mới tạo 2026-06-09)*
- Bản dịch VI: `p4/submission/p4_singapore_vi.docx`
- ⏳ Trước nộp: thêm ref **Leon (2004)**; làm rõ mâu thuẫn "18% vs N=84 exporter".

### P5 — Trung Quốc → **IJOEM** (Emerald, Harvard)
- Manuscript: `p5/submission/ijoem_package/01_manuscript_blinded.md` (.docx)
- Title page *(mới tạo)*: `…/02_title_page.docx` · Cover: `…/03_cover_letter.docx`
- Bản dịch VI: `p5/submission/p5_china_vi.docx`
- ⏳ Trước nộp: đối chiếu turning point R↔Stata (47.6 vs 49.4) → 1 con số chuẩn.

### P6 — Meta-analysis → **JWB** (Elsevier, APA)
- Manuscript: `p6/submission/jwb_package/01_manuscript_blinded.md` (.docx) · Title + Cover: `…/02_title_page.docx`, `03_cover_letter.docx`
- Bản dịch VI: `p6/submission/p6_meta_vi.docx`
- ⏳ **Cổng chính (đường găng):** điền κ/ICC (mã hóa kép 2 tác giả) vào 6 ô `[insert after dual-coding]`; OSF DOI; chạy lại Q_M cho 3 lệch off-by-one (Regime-III 90/78↔91/79; cDAI-M 75/76; DPL-Span 107/108).

### P7 — Capstone → **JIBS** (Springer, APA)
- Manuscript: `p7/submission/jibs_package/01_manuscript_blinded.md` (.docx)
- Title + Cover: `p7/submission/jibs_package/02_title_page_source.md`, `03_cover_letter_source.md` *(đổi tên thành 02_title_page/03_cover_letter khi upload)*
- Bản dịch VI: `p7/submission/p7_capstone_vi.docx`
- ⏳ Trước nộp: không có cổng dữ liệu lớn; chỉ rà ref/format cuối.

### P8 — Pacific SIDS → **World Development** (Elsevier, APA)
- Manuscript: `p8/submission/world_development_package/01_manuscript_blinded.md` (.docx) · Title + Cover: `…/02_title_page.docx`, `03_cover_letter.docx`
- Bản dịch VI: `p8/submission/p8_pacific_sids_vi.docx`
- ⏳ Trước nộp: **sinh số liệu Bảng 1** theo từng nước (7 SIDS); chốt cách trình bày estimation N=209 vs full 959.

### P9 — Ấn Độ → **MIR** (Springer, APA; abstract 4 mục) · *(IJOEM/JABS dùng abstract 7 mục Emerald đã tạo)*
- Manuscript: `p9_india/submission/mir_package/01_manuscript_blinded.docx` (kèm 4 hình nhúng)
- Title + Cover: `…/02_title_page.docx`, `03_cover_letter.docx`
- Bản dịch VI: `p9_india/submission/p9_india_vi.docx`
- ⏳ Trước nộp: quyết định ref **Hutzschenreuter & Voll (2008)** (thêm entry hoặc bỏ in-text).

---

## Ghi chú hồ sơ chưa hoàn chỉnh (KHÔNG phải target nộp đầu)
- **P3 `jabs_package`**: chỉ có README (stub). P3 đã đủ 3 hồ sơ hoàn chỉnh (MBR/Thunderbird/JED); jabs là tùy chọn 4 — cần dựng manuscript/title/cover nếu muốn dùng, hoặc bỏ.
- **P6 `ibr_package`**: là hồ sơ **legacy** (P6 đã rời IBR → JWB theo kế hoạch); còn manuscript, thiếu title/cover. 3 hồ sơ hiện hành của P6 là JWB/JIM/APJM.

## Trạng thái sẵn sàng nộp (sau khi xử lý cổng ⏳ tương ứng)
| Paper | Reach | Hồ sơ đầy đủ? | Cổng còn lại |
|---|---|:--:|---|
| P3 | MBR | ✅ | nhỏ (p-value, 2 ref) |
| P4 | MIR | ✅ *(vừa bổ sung title/cover)* | nhỏ (1 ref, 1 làm rõ) |
| P5 | IJOEM | ✅ *(vừa bổ sung title)* | nhỏ (1 đối chiếu TP) |
| P6 | JWB | ✅ | **lớn (κ/ICC + OSF + Q_M)** |
| P7 | JIBS | ✅ | không đáng kể |
| P8 | World Development | ✅ | vừa (Bảng 1 + estimation-N) |
| P9 | MIR | ✅ | nhỏ (1 ref) |

→ **Sẵn sàng nhất:** P7, P5, P3, P9 → P4 → P8 → **P6 (cuối, đường găng)**.
