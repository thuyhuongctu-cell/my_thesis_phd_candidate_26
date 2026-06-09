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

## PHA 1 — Cổng dữ liệu/phân tích (chỉ NCS/GVHD; CHẶN nộp paper liên quan)

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

## PHA 2 — Việc tôi (Claude) làm được an toàn NGAY (không cần dữ liệu mới)

> Có thể thực hiện bất cứ lúc nào bạn đồng ý; không chặn bởi Pha 1.

| # | Việc | Paper | Ghi chú |
|---|---|---|---|
| 2.1 | Xóa header "Version: Working manuscript / under revision" trong bản blinded | P7 (+ rà các paper khác) | Lộ trạng thái draft, không phù hợp nộp |
| 2.2 | Dựng abstract **7 mục Emerald** (Purpose/Design/Findings/Research limitations/Practical/Social/Originality) trong ≤250 từ cho IJOEM + JABS | P9 | Hiện dùng bản 4 mục 258 từ (đúng MIR); Emerald muốn 7 mục |
| 2.3 | Rà **spaced-thousands** + em-dash + AI-tone trên TẤT CẢ package phụ (Reach/Safe), không chỉ first-target | P3–P9 | Mới rà first-target; đồng bộ các package còn lại |
| 2.4 | Đồng bộ **metadata README/title-page** với manuscript (số bảng, word count, JEL, keywords) cho mọi package | P3–P9 | P5 đã làm; nhân rộng |
| 2.5 | Rà **citation↔reference 2 chiều** trên mọi package (orphan + missing) bằng script đối chiếu | P3–P9 | Tự động liệt kê; chỉ xóa orphan đã verify, missing thì flag |
| 2.6 | Chuẩn hóa Harvard "and" (Emerald) / APA "&" (Elsevier) đồng nhất từng package | P3–P9 | Theo đúng house style mỗi tạp chí |
| 2.7 | Dọn em-dash bản dịch VI P3 còn lại (nếu phát sinh) + rebuild docx | P3 | Đã làm 1 lần; kiểm lại |
| 2.8 | Build **bộ nộp cuối** `dist/SUBMISSION_FINAL/` gọn cho từng paper (manuscript+title+cover+figures+VI) | P3–P9 | 1 thư mục/ paper, sẵn upload |

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
