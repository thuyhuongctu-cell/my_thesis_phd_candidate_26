# KẾ HOẠCH HOÀN THIỆN DỰ ÁN — Luận án TS & 9 nghiên cứu thành phần

**NCS:** Đỗ Thùy Hương · **GVHD:** PGS.TS. Phan Anh Tú · **Lập:** 2026-06-09 · **Nhánh:** `claude/phd-thesis-review-L9Gml`

> Mục tiêu: đưa luận án + 9 paper (P1–P9) đến trạng thái (a) bảo vệ luận án tại CTU và (b) nộp tạp chí với xác suất chấp nhận cao nhất. Tài liệu này là kế hoạch tổng, cập nhật khi có tiến triển.

---

## 0. Hiện trạng (chốt 2026-06-09)

| Hạng mục | Trạng thái |
|---|---|
| **Luận án** (5 chương + phần đầu + TLTK) | ✅ Hoàn chỉnh, dist docx đã build, P9 đã tích hợp |
| **Chuyên đề CĐ1, CĐ2** | ✅ dist docx build; không khai báo AI (đúng yêu cầu) |
| **Đã công bố** | ICBEF meta 2024 (k=113); India book chapter (Do & Phan 2025); P1 (VEFR 2026); P2 (JFAR 2026) |
| **P3–P9** | ✅ Mỗi paper 3 hồ sơ nộp + 1 bản dịch VI; đã rà soát (pre-submission-reviewer) + đối chiếu số liệu với replication |
| **Liêm chính** | ✅ Lời cam đoan + khai báo kết hợp công trình; AI declaration khớp CTU; ICR P6 chuyển sang khung 2 tác giả |
| **Blinding** | ✅ Đã gỡ danh tính khỏi mọi bản blinded; self-citation ngôi thứ ba |
| **em-dash / AI-tone** | ✅ 0 trên tất cả manuscript + 8 bản dịch VI |

---

## PHA 1 — Cổng dữ liệu/phân tích — CẬP NHẬT 2026-06-09 (đã đóng phần lớn)

> Cập nhật sau vòng hoàn thiện P8 + P3/P4/P5/P9.

| # | Việc | Paper | Trạng thái |
|---|---|---|---|
| 1.1 | Mã hóa kép 20% (k=47) → κ/ICC | P6 | ⏳ **NCS/GVHD** (đường găng) |
| 1.2 | Đăng ký OSF → DOI | P6 | ⏳ **NCS** |
| 1.3 | Chạy lại Q_M cho 3 lệch off-by-one | P6 | ✅ **XONG** — đối chiếu `p6_study_database.csv`: là **lỗi gõ count** (Regime-III 90/78→91/79; cDAI-M 75→76; DPL-Span 107→108); tổng khớp 288/238. r̄ và Q_M vốn đã tính trên dữ liệu thật ⇒ **KHÔNG cần chạy lại Q_M**. Sửa cả 4 package |
| 1.4 | Bảng 1 thống kê theo nước (7 SIDS) | P8 | ✅ **XONG** — tính từ `data_wbes/p7/p7_pooled_clean.csv` (tái tạo N=959 chính xác), điền 3 package + clean_en + VI |
| 1.5 | Minh bạch estimation N=209 vs 959 | P8 | ✅ **XONG** — đã ghi rõ trong abstract + §4; sửa nhãn TCI; thêm ref Mahler |
| 1.6 | p exporter-only + ref World Bank 2025b/c | P3 | ✅ **Không cần sửa** — .660 nhất quán; WB 2025b/c đã có trong reflist (review over-flag) |
| 1.7 | Ref Leon (2004) + làm rõ 18%/N=84 | P4 | ⚠️ 18%/N=84 ✅ đã làm rõ (=complete-case của ~18% exporter); **Leon (2004) ⏳ NCS bổ sung** (không có trong repo) |
| 1.8 | Đối chiếu TP R↔Stata (47.6 vs 49.4) | P5 | ✅ **Không cần sửa** — 49.4% khớp pipeline chuẩn `results_coefs.csv` (FSTS 2.065/FSTS² −2.092 → 49.4%); file R turning_points là phụ/lỗi |
| 1.9 | Ref Hutzschenreuter & Voll (2008) | P9 | ✅ **XONG** — thêm entry JIBS 39(1), 53–70 (3 manuscript + clean_en) |

**Pha 1 còn lại = chỉ P6 (1.1–1.3) + P4 Leon ref (1.7).** P8 đã hoàn thiện hoàn toàn.

---

## PHA 1 (gốc) — Cổng dữ liệu/phân tích (chỉ NCS/GVHD; CHẶN nộp paper liên quan)

> Đây là các việc tôi **không thể** làm vì cần dữ liệu gốc/coder thứ hai/đăng ký bên ngoài. Hoàn thành trước khi nộp paper tương ứng.

| # | Việc | Paper | Chủ thể | "Hoàn thành" = |
|---|---|---|---|---|
| 1.1 | **Mã hóa kép 20% (k=47)**: thầy Tú mã hóa mù → tính κ/ICC | P6 | GVHD + NCS | Điền 6 ô `[insert after dual-coding]` ở 4 package + bản dịch VI; κ≥0.70, ICC≥0.80 |
| 1.2 | **Đăng ký OSF** protocol → lấy DOI | P6 | NCS | Thay `[insert OSF DOI at submission]` ở 4 package + file OSF |
| 1.3 | **Chạy lại Q_M** cho 3 lệch off-by-one (Regime-III 90/78↔91/79; cDAI-M 75/76; DPL-Span 107/108) | P6 | NCS | Bảng composition = bảng kết quả = CSV; Q_M cập nhật |
| 1.4 | **Sinh Bảng 1** thống kê mô tả theo từng nước (7 SIDS) | P8 | NCS | Bảng 1 đầy đủ số liệu, không để trống |
| 1.5 | Xác nhận **estimation N=209 vs full 959** (cân nhắc re-impute hoặc giữ minh bạch) | P8 | NCS | Quyết định cách trình bày; cập nhật abstract/§4 nếu đổi hướng |
| 1.6 | Xác nhận p exporter-only (.660 vs .730) + chi tiết ref World Bank 2025b/c | P3 | NCS | Số nhất quán; 2 ref đầy đủ |
| 1.7 | Thêm ref **Leon (2004)**; làm rõ "18% vs N=84 exporter" | P4 | NCS | Ref có entry; mâu thuẫn N được giải |
| 1.8 | Đối chiếu pipeline R↔Stata turning point (47.6 vs 49.4) | P5 | NCS | Một con số chuẩn duy nhất |
| 1.9 | Quyết định ref **Hutzschenreuter & Voll (2008)** (thêm entry hoặc bỏ in-text) | P9 | NCS | Không còn cite gãy |

---

## PHA 2 — Việc Claude làm được an toàn — ✅ HOÀN THÀNH 2026-06-09

| # | Việc | Trạng thái |
|---|---|---|
| 2.1 | Xóa header draft ("Version/Status" P7×3; footer line-477 P9×3) + sửa P6 jwb ghi nhầm tạp chí (IBR→JWB) | ✅ |
| 2.2 | Abstract **7 mục Emerald** ≤250 từ cho P9 IJOEM + JABS (MIR giữ 4 mục) | ✅ (250 từ, đủ số liệu) |
| 2.3 | Spaced-thousands trên TẤT CẢ package (180 chỗ) + em-dash/AI-tone = 0 toàn bộ | ✅ |
| 2.4 | **Bổ sung title/cover còn thiếu cho hồ sơ nộp đầu**: P4-MIR (title+cover), P5-IJOEM (title) | ✅ (đã tạo) |
| 2.5 | Citation↔reference 2 chiều: gỡ orphan đã verify (P4×4, P6×3, P9×13), flag missing | ✅ (per-paper fix agents) |
| 2.6 | Harvard "and" (Emerald) / APA "&" (Elsevier) đúng house style | ✅ |
| 2.7 | Dọn em-dash bản dịch VI P3 (184→0) | ✅ |
| 2.8 | `dist/SUBMISSION_FINAL/UPLOAD_INDEX.md` — manifest nộp đầu/ paper (file, VI, house style, cổng) | ✅ |

**Còn lại trong Pha 2 (tùy chọn, thấp ưu tiên):** dựng hồ sơ P3-jabs (stub) nếu muốn dùng tùy chọn 4; bổ sung title/cover cho P6-ibr legacy (đã rời IBR, không cần).

---

## PHA 3 — Tiền nộp tạp chí (mỗi paper, sau khi xong Pha 1+2)

| # | Việc | Chủ thể |
|---|---|---|
| 3.1 | **iThenticate / CTU similarity check** từng paper; loại 2 chuyên đề của NCS khỏi nguồn so trùng | NCS |
| 3.2 | Kiểm tra hình độ phân giải cao khi upload (300dpi/vector) | NCS (tôi kiểm path/format) |
| 3.3 | Điền ngày cover letter; xác nhận corresponding author = Phan Anh Tú | NCS |
| 3.4 | Khai báo prior work trong cover (P9 ↔ book chapter DOI) | ✅ đã có |
| 3.5 | Xác nhận tên tạp chí mục tiêu (chỉ nêu chính thức sau khi chấp nhận) | NCS |

---

## PHA 4 — Chiến lược nộp (staggered, theo `reviews/JOURNAL_TARGETING_PLAN.md`)

> Nguyên tắc Đ.15: **không nộp đồng thời cùng 1 bài tới nhiều tạp chí**. Mỗi paper đi thang Reach → Target → Safe.

| Paper | Thứ tự nộp (Reach → … → Safe) |
|---|---|
| P3 VN | MBR (Q1) → JABS (Q2) → Thunderbird (Q2) → JED (Q3) |
| P4 SG | MIR (Q1) → MBR (Q1) → APBR (Q2) |
| P5 CN | IJOEM (Q1) → Chinese Mgmt Studies (Q2) → APBR (Q2) |
| P6 Meta | JWB (Q1) → JIM (Q1) → RIBS (Q2) |
| P7 Capstone | JIBS (Q1) → IBR (Q1) → APJM (Q1) → IJOEM |
| P8 SIDS | World Development (Q1) → JID (Q2) → EJDR (Q2) |
| P9 India | MIR (Q1) → IJOEM (Q1/Q2) → JABS (Q2) |

**Trình tự khuyến nghị theo độ sẵn sàng:** P3/P5/P7 (sạch, ít cổng) nộp trước → P9 (sau Pha 1.9) → P4/P8 (sau cổng dữ liệu) → **P6 nộp cuối** (phụ thuộc κ/ICC + OSF DOI).

---

## PHA 5 — Hoàn thiện & bảo vệ luận án

| # | Việc | Chủ thể |
|---|---|---|
| 5.1 | **CTU similarity check toàn luận án** (loại 2 chuyên đề NCS khỏi nguồn) | NCS |
| 5.2 | Cập nhật **Danh mục công trình** khi có chấp nhận/đăng (P3–P9) | NCS (tôi cập nhật file) |
| 5.3 | Rebuild **dist docx** cuối cùng (luận án + chuyên đề) sau mọi chỉnh sửa | tôi tự động |
| 5.4 | **Slide bảo vệ** + tóm tắt 24 trang + bản tóm tắt tiếng Anh | NCS (tôi hỗ trợ nội dung/skill) |
| 5.5 | Kiểm tra lần cuối **AI declaration** (luận án có; chuyên đề không) khớp quy định CTU | ✅ đã khớp; rà lại trước in |
| 5.6 | Chuẩn bị trả lời hội đồng: tính độc lập, kết hợp công trình, đóng góp mới CDCM/ICRV/FIP | NCS (tôi soạn Q&A) |

---

## Phụ thuộc & đường găng (critical path)

```
P6 κ/ICC (1.1) ─┐
P6 OSF DOI (1.2)─┼─→ P6 nộp được (muộn nhất)
P6 Q_M (1.3) ───┘
P8 Bảng 1 (1.4) + estimation-N (1.5) ─→ P8 nộp được
[Pha 2 — tôi làm song song, không chặn]
Tất cả paper → CTU similarity (3.1) → nộp (Pha 4)
Luận án → similarity (5.1) → bảo vệ (5.4–5.6)
```

**Đường găng = P6** (cần coder thứ hai + OSF + chạy lại Q_M). Khuyến nghị khởi động 1.1–1.3 sớm.

---

## Đề xuất bước kế tiếp (tôi có thể làm ngay trong Pha 2)
1. **2.1 + 2.3 + 2.5** — quét toàn bộ package (kể cả Reach/Safe) cho draft-header, spaced-thousands, citation↔reference; sửa an toàn, flag phần cần NCS.
2. **2.2** — dựng abstract 7 mục Emerald cho P9 IJOEM/JABS.
3. **2.8** — đóng gói `dist/SUBMISSION_FINAL/` cho các paper đã sạch (P3/P5/P7).

> Nói cho tôi biết ưu tiên (1, 2, 3, hay tất cả) — tôi sẽ triển khai và cập nhật kế hoạch này.
