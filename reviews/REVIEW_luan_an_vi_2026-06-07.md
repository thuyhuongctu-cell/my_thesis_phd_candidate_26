# BÁO CÁO PHẢN BIỆN LUẬN ÁN (NHÁNH TIẾNG VIỆT)

**Đối tượng review:** Luận án tiến sĩ — `dist/luan_an_ctu/` (5 chương) + Bộ hồ sơ nộp `dist/submission_packages/` (CD1, CD2)
**Chuyên ngành:** Quản trị Kinh doanh Quốc tế (International Business Administration)
**Tiêu chuẩn đối chiếu:** Luận án tiến sĩ (chuẩn cơ sở đào tạo) + chuẩn công bố Scopus/WoS (Q1–Q2)
**Ngày review:** 2026-06-07
**Phương pháp review:** Khung 5 phản biện đa góc nhìn (Tổng biên tập + Phương pháp + Chuyên ngành + Liên ngành + Phản biện đối kháng), áp dụng từ skill `academic-paper-reviewer`.

---

## 0. TÓM TẮT ĐIỀU HÀNH (Executive Summary)

Luận án nghiên cứu mối quan hệ **Quốc tế hóa – Hiệu quả doanh nghiệp (I–P)** tại châu Á qua khung điều tiết đa tầng **CDCM** (thể chế ICRV × năng lực số TCI/DAI × đặc điểm nhà quản trị), thiết kế **mixed synthesis-empirical** (meta-analysis 1982–2026 + phân tích WBES đa quốc gia). Đây là một luận án **trình độ cao, có độ chín học thuật rõ rệt**: khung lý thuyết tích hợp chặt chẽ, dữ liệu quy mô lớn (≈101.185 doanh nghiệp), có **hai đóng góp gốc đáng giá** (construct **FIP — Forced Internationalization Penalty** và taxonomy **ICRV 6 nhóm**), và sự phân tách khái niệm **TCI vs DAI** có nền tảng lý thuyết vững.

**Kết luận điều hành:**

| Hạng mục | Đánh giá |
|---|---|
| Chất lượng học thuật cốt lõi (lý thuyết, đóng góp) | **Mạnh** — đạt ngưỡng tiến sĩ và có tiềm năng Scopus/WoS Q1–Q2 |
| Tính chặt chẽ phương pháp | **Khá–Mạnh**, còn một số điểm cần củng cố (endogeneity, power, selection) |
| **Tính nhất quán nội tại (consistency)** | **YẾU — cần sửa bắt buộc** (số liệu mâu thuẫn giữa các chương) |
| **Hoàn chỉnh cấu trúc luận án (front matter)** | **THIẾU NGHIÊM TRỌNG** ở bản 5 chương |
| Chuẩn trình bày Scopus/WoS (hình, bảng, APA7) | **Chưa đạt** — thiếu hình mô hình khái niệm, danh mục TLTK hợp nhất chưa đầy đủ |
| Văn phong học thuật tiếng Việt | **Khá**, nhưng lạm dụng thuật ngữ tiếng Anh chưa Việt hóa |

**Quyết định đề xuất (editorial decision): MAJOR REVISION (Chỉnh sửa lớn) — không phải reject.** Phần lõi khoa học đã đạt; các vấn đề chủ yếu là **nhất quán, hoàn chỉnh cấu trúc, và chuẩn trình bày** — đều khắc phục được mà không phải làm lại nghiên cứu.

---

## 0b. TRẠNG THÁI TRIỂN KHAI SỬA CHỮA (cập nhật 2026-06-07)

Các mục bắt buộc đã được triển khai trên **cả** nguồn build `thesis/` và bản `dist/luan_an_ctu/source_md/`:

| Mục | Nội dung | Trạng thái |
|---|---|---|
| **M1** | Đồng bộ số liệu: **49** nền kinh tế · **102** cặp quốc gia-năm · **91.982** DN · **9 "SIDS"**; chuẩn hóa k=studies; Bảng 4.1 tính lại theo dataset (96.415 phân loại ICRV) + chú thích N | Có Hoàn tất (đối chiếu `p7_pooled_clean.csv` + P7 capstone EN; con số chốt theo NCS xác nhận) |
| **M2** | Thêm phần đầu luận án `00_phan_dau_vi.md` (bìa, cam đoan, tóm tắt VN/EN, danh mục từ viết tắt, danh mục bảng/hình, danh mục công trình) + nối vào build | Có Hoàn tất (một số mục để placeholder: tên HD, tiêu đề chính thức — NCS xác nhận) |
| **M3** | Hình 2.1 (mô hình khái niệm CDCM) + Hình 4.x (họ đường cong I–P theo ICRV + FIP), 300 DPI, nhúng vào Ch2/Ch4 | Có Hoàn tất |
| **M4** | Bổ sung Combs (2005, 2011) & Richard et al. (2009) vào danh mục | Có Một phần (còn: hợp nhất TLTK cho luận án + citation-check hai chiều) |
| **M5** | Bảng 2.1 ánh xạ P3–P8 ↔ chương ↔ H; ghi chú giả thuyết con; làm rõ "H7-P7"; xác nhận "P9" là dương tính giả | Có Hoàn tất |

### Cập nhật vòng 2 (theo chỉ đạo NCS)
- **Bỏ toàn bộ self-citation chưa công bố trong LUẬN ÁN:** mọi `Do/Đỗ & Phan (2026a–g)` và `Mar et al. (2026)` (= P4) được thay bằng nhãn nội bộ **P1–P8** (đây là nội dung nghiên cứu của chính luận án, không trích dẫn tác giả–năm). Gỡ 9 entry tự thân khỏi danh mục TLTK; chuyển hồ sơ công bố sang phần đầu, **tách rõ Đã công bố (ICBEF 2024, P1-VEFR, P2-JFAR) vs Đang bình duyệt (P3–P8)** + ghi chú liêm chính.
- **Bỏ Mục 5.4.4 (ĐBSCL)** — nội dung suy luận chưa chắc chắn.
- **Chốt một nguồn chuẩn:** `dist/luan_an_ctu/source_md/` đã đồng bộ **byte-identical** với `thesis/`. đến **M6 ĐÃ XỬ LÝ.**
- **Build DOCX:** cài `pandoc 3.1.3`, dựng lại `dist/luan_an_ctu/*.docx` (gồm `00_phan_dau_vi.docx` + 2 hình nhúng) bằng `bash build_ctu_docx.sh --no-templates`.
- **Kiểm tra papers (P3–P8):** các manuscript nộp **KHÔNG** trích dẫn bài chưa công bố; mọi self-citation đều trỏ tới công trình đã công bố (ICBEF 2024; chương sách IntechOpen 2025 có DOI; JFAR 2026 advance-online) đến **hợp lệ, không cần sửa.**

### M6 (đã xử lý — trước đây Major): Hai nguồn luận án phân kỳ
`thesis/chuong_*.md` (nguồn build) và `dist/luan_an_ctu/source_md/chuong_*.md` (bản sinh) **đã phân kỳ về nội dung**: bản `thesis/` mới hơn (có thêm Mục 5.4.4 — hàm ý chính sách ĐBSCL; dùng trích dẫn APA dạng "Do & Phan, 2026e"; romanize "Do"), bản `dist/` dùng "Đỗ & Phan (2026 — JABS under review)". đến **Cần NCS chọn một nguồn chuẩn duy nhất** (khuyến nghị: `thesis/` vì là nguồn build) và **tái sinh `dist/` bằng `build_ctu_docx.sh`** (cần cài `pandoc`). Hiện các sửa M1–M5 đã áp **đồng thời lên cả hai** để không mất đồng bộ.

### Còn lại (chưa làm — cần quyết định/định hướng của NCS):
- **N-items (N1–N13):** endogeneity/IV mô hình chính; sửa diễn giải TP Singapore (CI vượt 100%) & publication bias (Egger NS); Việt hóa thuật ngữ; ký hiệu mũi tên "I–P"; disclosure thesis-by-publication. 
- **M4 đầy đủ:** hợp nhất một danh mục TLTK cho luận án 5 chương + chạy citation-check hai chiều.
- **Đồng bộ hồ sơ nộp:** CD2 Phụ lục A đang ghi "47 nền kinh tế" đến cập nhật về 49 cho khớp luận án.
- **Năm dữ liệu 2003 vs 2009:** P7 capstone EN ghi 2003–2025 (có Oman 2003) nhưng luận án ghi 2009–2025 — cần thống nhất hoặc chú thích.
- **Nhãn nhóm ICRV:** dataset gán Nhóm IV="Lower_mid_transition", V="Emerging"; luận án dùng IV="Emerging", V="Frontier" — đã giữ theo luận án (thành viên khớp), nhưng nên thống nhất nhãn một lần.

---

## 1. ĐIỂM MẠNH (cần giữ và phát huy)

1. **Đóng góp lý thuyết gốc, có thể đặt tên (nameable contribution).** FIP (gánh nặng quốc tế hóa bắt buộc) tại Pacific SIDS là một *boundary condition* mới, có biện minh lý thuyết 3 điều kiện cấu trúc và bằng chứng thực nghiệm nhất quán qua 4 specification (β từ −0,404 đến −1,596). Đây là loại đóng góp mà reviewer Q1 (JIBS, JWB, World Development) đánh giá cao.
2. **Khung tích hợp đa tầng mạch lạc.** Việc gắn mỗi tầng điều tiết với một lý thuyết nền (Uppsala đến chi phí học hỏi; RBV đến TCI; Institutional Theory đến ICRV; Upper Echelons đến nhà quản trị) và phân vai TCI = *foundational/level-shifter* vs DAI = *situational/curvature* là logic chặt, không phải "ghép nối cơ học".
3. **Tam giác hóa bằng chứng (triangulation).** Cùng một kết luận gradient thể chế đến từ hai nguồn độc lập: meta-analysis (P6, Q_M = 17,35; p = ,002) và primary data (P7, gradient turning point 28% đến 55%). Đây là điểm cộng phương pháp lớn.
4. **Quy mô và phạm vi dữ liệu vượt trội** so với literature khu vực (mở rộng từ pool 17 nước đến 47/49 nền kinh tế), bao gồm cả các trường hợp biên (Frontier, SIDS) vốn thiếu vắng trong literature.
5. **Tính trung thực khoa học cao.** Luận án tự khai báo giới hạn (power ≈ 16% ở Singapore; "consistent but underpowered"; null kết quả được báo cáo trung thực; trim-and-fill điều chỉnh r = 0,074 đến 0,035). Sự khiêm tốn trong suy luận là dấu hiệu chín muồi.

---

## 2. VẤN ĐỀ BẮT BUỘC SỬA (Major — chặn thông qua / chặn nộp tạp chí)

### M1. Mâu thuẫn số liệu hệ thống giữa các chương (CRITICAL)
Bằng chứng kiểm đếm tự động trên `dist/luan_an_ctu/source_md/`:

| Đại lượng | Các giá trị xuất hiện | Vị trí |
|---|---|---|
| Số nền kinh tế | **"47 nền kinh tế" (11 lần)** vs **"49 nền kinh tế" (16 lần)** vs "47–49" | Ch1 dùng "47–49"; Ch3 Mục 3.1 "47"; Ch3 Mục 3.4.5.4 & Ch4/Ch5 "49" |
| Số Pacific SIDS | **6** / **8** / **9** ("chín") | Ch1 Mục 1.5.2 = 6; Ch1 Mục 1.2 = "6–8"; Ch3/Ch4/Ch5 = 9 |
| Cỡ mẫu SIDS | bảng 4.1 ghi **~1.371**; Mục 4.7 & Ch3 ghi **N = 1.469** | Ch4 |
| Tổng mẫu | Bảng 4.1 cộng 6 nhóm = **100.697** ≠ tiêu đề **101.185** (lệch ~488) | Ch4 Mục 4.1.1 |
| `k = 113` (baseline ICBEF) | mô tả vừa là **"effect-size units"** vừa là **"nghiên cứu"** | Ch2 Mục 2.3.2 vs Ch4 Mục 4.2.1 vs Ch5 |
| Pool P6 | Ch3 ghi **K=288 effect sizes / k=238 studies**; Ch4 ghi "hàng trăm cặp effect-size", k=238 | Ch3 Mục 3.2.2 vs Ch4 Mục 4.2 |

 đến **Hành động:** Chốt một "bảng số liệu chuẩn" (single source of truth) và áp dụng đồng bộ. Lưu ý **CD2 Phụ lục A** đã chốt **"47 nền kinh tế"** — cần thống nhất luận án với hồ sơ nộp (hoặc giải thích rõ: 47 nền kinh tế châu Á + 2 đơn vị bổ sung = 49; hay 47 gồm 6 SIDS vs 49 gồm 9 SIDS). Đây là loại lỗi mà phản biện hội đồng và reviewer tạp chí phát hiện ngay và làm mất niềm tin vào toàn bộ phần định lượng.

### M2. Thiếu toàn bộ phần đầu luận án (front matter) ở bản 5 chương (CRITICAL)
`dist/luan_an_ctu/source_md/` **chỉ có 5 file chương**, không có:
- Trang bìa chính/bìa phụ, Lời cam đoan, Lời cảm ơn
- **Tóm tắt tiếng Việt + Abstract tiếng Anh** (bắt buộc cho luận án + bắt buộc cho Scopus/WoS)
- Mục lục, Danh mục bảng, Danh mục hình, **Danh mục từ viết tắt**
- **Danh mục công trình đã công bố của NCS** liên quan luận án
- Danh mục tài liệu tham khảo hợp nhất (xem M4)

> Nghịch lý: **CD1 và CD2 trong SUBMISSION_PACKAGE đã có đầy đủ** các mục này (Lời cam đoan, Tóm tắt, Abstract, Mục lục, Danh mục bảng/hình/từ viết tắt, TLTK, Phụ lục). Cần "nâng" chuẩn cấu trúc của chuyên đề lên cho bản luận án.

 đến **Hành động:** Bổ sung front matter đầy đủ. Danh mục từ viết tắt đặc biệt cấp thiết vì luận án dày đặc acronym (I–P, FSTS, TCI, DAI, ICRV, CDCM, FIP, WBES, WGI, MARA, LM-test…).

### M3. Thiếu HÌNH MÔ HÌNH KHÁI NIỆM (conceptual framework figure) (CRITICAL cho Scopus/WoS)
Mục 2.5.1 "Mô hình khái niệm" **chỉ mô tả bằng lời**, không có sơ đồ. Một luận án QTKD Quốc tế và mọi bài Scopus/WoS Q1–Q2 trong IB **bắt buộc** có hình khung khái niệm (biến độc lập FSTS đến phụ thuộc LP, với 3 tầng điều tiết ICRV/TCI-DAI/manager, quan hệ phi tuyến + boundary condition FIP). Thư mục `thesis/figures/` hiện chỉ có hình mô tả (pool, mật độ năng suất…), **không có** hình mô hình.

 đến **Hành động:** Dùng skill `conceptual-model-international-business` hoặc `academic-conceptual-model-diagram` để dựng Hình 2.1 (khung CDCM) + Hình minh họa họ đường cong I–P theo ICRV (turning point 28% đến 55%) cho Chương 4/5.

### M4. Danh mục tài liệu tham khảo (APA7) chưa hợp nhất & còn thiếu mục (Major)
- Bản 5 chương **không có** danh mục TLTK hợp nhất; chỉ Chương 4 có danh mục cục bộ ("trích dẫn trong Chương 4").
- File `dist/luan_an/source_md/04_references_apa7.md` (≈325 mục) **thiếu ít nhất**: **Combs et al. (2005, 2011)** và **Richard et al. (2009)** — đều được trích trong Ch2 Mục 2.1.2 và Ch3 Mục 3.3.2 làm căn cứ chọn thước đo hiệu quả. (Đã kiểm tra: 28/30 trích dẫn chủ chốt khác có mặt.)
- Cần kiểm tra đối chiếu **toàn bộ** in-text ↔ reference list (two-way check) bằng skill `chinh-sua-van-ban-hoc-thuat-scopus-wos` / `/ars-citation-check`.

 đến **Hành động:** Hợp nhất 1 danh mục TLTK cuối luận án, chuẩn APA7, bổ sung mục thiếu, chạy citation-check hai chiều.

### M5. Hệ thống giả thuyết không nhất quán giữa cấp luận án và cấp bài báo (Major)
Chương 2 định nghĩa **H1–H6 + H1b**. Nhưng các chương sau xuất hiện **H7 (1 lần), H2b, H4a, H4b, E1a, E1b, và P9 (1 lần)** — không được giới thiệu/định nghĩa trong hệ giả thuyết của luận án (đây là các giả thuyết con từ các bài P3–P8 "rò" vào).

 đến **Hành động:** (a) Thêm **một bảng ánh xạ** P3–P8 ↔ chương luận án ↔ giả thuyết H; (b) hoặc Việt hóa/định nghĩa các giả thuyết con khi xuất hiện, hoặc loại bỏ mã không thuộc hệ H1–H6/H1b. Riêng **"P9"** và **"H7"** xuất hiện đơn lẻ — gần như chắc là lỗi sót, cần truy vết và sửa.

---

## 3. VẤN ĐỀ NÊN SỬA (Minor–Moderate — nâng chất lượng lên ngưỡng Q1)

### Phương pháp & suy luận
- **N1. Nội sinh (endogeneity)/nhân quả ngược.** Luận án đã thành thật nêu hạn chế (Mục 5.5.3) nhưng nên *chủ động* hơn: bổ sung ít nhất một kiểm định IV/Heckman ở **mô hình chính** (hiện Heckman/IMR mới chỉ ở P4 Singapore như robustness). Reviewer JIBS sẽ yêu cầu điều này.
- **N2. Turning point Singapore ≈ 88,6% với CI [53%, 253%].** Cận trên 253% **không khả diễn** vì FSTS bị chặn ở 100%. Cần ghi rõ TP nằm ngoài miền dữ liệu quan sát và diễn giải như "không có bằng chứng đảo chiều trong miền [0,100%]" thay vì điểm ước lượng 88,6%.
- **N3. Diễn giải publication bias.** Mục 4.2.4 viết "publication bias xác nhận" trong khi **Egger p = ,057 (không có ý nghĩa)**; chỉ Begg–Mazumdar có ý nghĩa. Nên phát biểu thận trọng: "bằng chứng hỗn hợp, nghiêng về có lệch nhẹ; ước lượng bảo thủ r = 0,035".
- **N4. Mâu thuẫn I² của chính nghiên cứu vs literature.** Ch1/Ch2 nhấn mạnh "I² > 80%" (từ literature trước), nhưng meta của luận án (P6) cho **I² = 62,4%**. Cần một câu giải thích vì sao thấp hơn (cấu trúc 3 tầng, pool châu Á cụ thể) để tránh người đọc tưởng mâu thuẫn.
- **N5. Phân cực FSTS (trung vị = 0).** Mục 4.1.2 nêu đa số doanh nghiệp không xuất khẩu đến hồi quy toàn mẫu bị kéo bởi thiểu số. Nên trình bày rõ chiến lược xử lý (mô hình toàn mẫu vs exporters-only) và đối chiếu kết quả ở mỗi nơi để minh bạch.

### Phạm vi & định nghĩa
- **N6. Định nghĩa "châu Á" của phạm vi.** Việc đưa **GCC (Advanced Resource)** và **Israel (ISR, xuất hiện ở bảng 4.1)** vào "châu Á" cần một câu biện minh phạm vi địa lý/thể chế minh bạch (nếu không reviewer sẽ chất vấn). Nhật Bản bị loại đã giải thích (do WBES) — tốt.
- **N7. Nhãn nhóm ICRV không đồng nhất.** Nhóm IV gọi là "Emerging" (Ch1, bảng 4.1) nhưng "Lower-middle transition" (Ch2 Mục 2.1.4); Nhóm I liệt kê khác nhau giữa các chương (có/không Hong Kong, Israel). Chuẩn hóa nhãn + danh sách thành viên trong **một bảng định nghĩa ICRV** (đặt ở Ch2, tham chiếu lại ở Ch3/Ch4).

### Trình bày & văn phong
- **N8. Định nghĩa acronym tại nơi xuất hiện đầu.** **CDCM** được dùng ở Ch1 Mục 1.8.1 nhưng chỉ định nghĩa ở Ch2 Mục 2.4 (forward reference). Quy tắc: viết đầy đủ + (viết tắt) ở lần đầu trong thân bài, và đưa vào Danh mục từ viết tắt.
- **N9. Việt hóa thuật ngữ.** Lạm dụng thuật ngữ tiếng Anh không dịch: *heterogeneity, moderator, turning point, level shifter, boundary condition, composite, robustness, power…* Chuẩn luận án tiếng Việt: dùng thuật ngữ Việt + (tiếng Anh) ở lần đầu, sau đó nhất quán. Dùng skill `academic-translation-vietnamese` + glossary `writing_guides/09b_vn_term_glossary.md`.
- **N10. Dấu mũi tên & ký hiệu phi chuẩn.** Văn bản dùng "I–P", " đến " nhiều nơi — với bản nộp Scopus/WoS cần thay bằng diễn đạt chữ hoặc "I–P". Dùng skill `chinh-sua-van-ban-hoc-thuat-scopus-wos`.
- **N11. Chuẩn hóa ký hiệu biến thống kê** (in nghiêng biến, chuẩn APA/LaTeX) bằng skill `academic-variable-formatter` (vd: *r*, *p*, *I²*, *Q_M*, β, *N*, *k*).
- **N12. Dấu hiệu văn phong AI.** Rà bằng skill `phd-academic-writing-humanizer` (lạm dụng em-dash "—", cấu trúc câu công thức) để giảm rủi ro nghi ngờ AI khi nộp.

### Tự trích dẫn & minh bạch nguồn
- **N13. Tự trích dẫn chùm bài đồng hành.** Luận án dựa nhiều vào **Đỗ & Phan (2026 — VEFR/JFAR/JABS/MIR/IJOEM/IBR/JIBS/World Development)** và **Đỗ & Phan (2024 — ICBEF)** — phần lớn đang *under review/under revision*. Cần: (a) một mục **"Quan hệ giữa luận án và các công trình đã/đang công bố của NCS"** (thesis-by-publication disclosure); (b) ghi rõ trạng thái (under review ≠ published) và **không suy luận như bằng chứng đã bình duyệt** ở những chỗ then chốt; (c) cảnh báo: nếu các bài chưa được chấp nhận tại thời điểm bảo vệ, hội đồng có thể yêu cầu hạ cấp độ khẳng định.

---

## 4. ĐÁNH GIÁ BỘ HỒ SƠ NỘP (SUBMISSION_PACKAGE: CD1, CD2)

`dist/submission_packages/{cd1,cd2}` — mỗi chuyên đề có `*_submission_final.docx` + bìa chính + bìa phụ.

**Điểm mạnh:** Cấu trúc **đạt chuẩn** (Lời cam đoan đến Tóm tắt đến Abstract đến Mục lục đến Danh mục bảng/hình/từ viết tắt đến Nội dung đến Kết luận đến TLTK đến Phụ lục). CD2 có Phụ lục đầy đủ (danh sách 47 nền kinh tế, tóm tắt bản thảo đồng hành, quy ước thống kê, đặc tả Stata cluster SE) — rất tốt cho khả năng tái lập.

**Cần đồng bộ với luận án:**
1. **Con số nền kinh tế:** CD2 Phụ lục A = **47**; luận án dùng lẫn 47/49 đến thống nhất (xem M1).
2. **Bộ từ viết tắt & glossary** giữa CD1, CD2 và luận án phải trùng khớp (TCI/DAI/ICRV/CDCM/FIP).
3. **Danh mục TLTK** giữa CD1/CD2 (mỗi file riêng) và luận án nên dùng cùng một thư viện trích dẫn để tránh lệch định dạng/lệch năm.

 đến **Khuyến nghị:** Dùng `scripts/build_submission_package.sh` + `build_ctu_docx.sh` để tái sinh docx **sau khi** sửa nhất quán, đảm bảo bản .docx nộp = bản .md nguồn (hiện cần kiểm tra đồng bộ md↔docx).

---

## 5. ĐỐI CHIẾU CHUẨN (Rubric)

| Tiêu chí | Luận án tiến sĩ QTKD QT | Scopus/WoS Q1–Q2 | Hiện trạng |
|---|---|---|---|
| Khoảng trống & câu hỏi NC rõ ràng | Có | Có | **Đạt** (3 gap mạch lạc) |
| Khung lý thuyết & giả thuyết | Có | Có | Đạt; cần hình + nhất quán mã H (M3, M5) |
| Đóng góp mới có thể đặt tên | Có | CóCó | **Vượt** (FIP, ICRV) |
| Phương pháp tái lập được | Có | Có | Khá; cần endogeneity (N1) |
| Nhất quán số liệu | Có (bắt buộc) | Có (bắt buộc) | **Chưa đạt** (M1) |
| Cấu trúc/front matter | Có (bắt buộc) | Có (abstract) | **Chưa đạt** (M2) |
| Hình/bảng chuẩn xuất bản | Có | Có | **Chưa đạt** (M3) |
| TLTK APA7 đầy đủ, hai chiều | Có | Có | **Chưa đạt** (M4) |
| Văn phong học thuật | Có | Có | Khá (N9–N12) |
| Đạo đức/minh bạch nguồn | Có | Có | Cần disclosure (N13) |

---

## 6. LỘ TRÌNH CHỈNH SỬA THEO ƯU TIÊN (Revision Roadmap)

**Đợt 1 — Bắt buộc trước bảo vệ/nộp (1–2 tuần):**
1. [M1] Lập "bảng số liệu chuẩn" và rà-thay đồng bộ 47/49, SIDS 6/8/9, N SIDS, tổng mẫu, k/effect-size.
2. [M2] Bổ sung front matter đầy đủ cho bản 5 chương (mượn khung CD1/CD2).
3. [M5] Bảng ánh xạ P3–P8 ↔ chương ↔ H; sửa H7/P9 sót.
4. [M4] Hợp nhất TLTK APA7, bổ sung Combs/Richard, chạy citation-check hai chiều.

**Đợt 2 — Nâng chuẩn xuất bản (2–3 tuần):**
5. [M3] Dựng Hình mô hình khái niệm CDCM + Hình họ đường cong I–P theo ICRV.
6. [N1, N2, N3] Củng cố suy luận: thêm IV/Heckman ở mô hình chính; sửa diễn giải TP Singapore & publication bias.
7. [N13] Mục disclosure thesis-by-publication + chuẩn hóa trạng thái các bài đồng hành.

**Đợt 3 — Hoàn thiện văn phong/định dạng (1 tuần):**
8. [N7, N8] Chuẩn hóa nhãn/danh sách ICRV + định nghĩa acronym tại lần đầu.
9. [N9–N12] Việt hóa thuật ngữ; bỏ ký hiệu mũi tên; chuẩn hóa biến thống kê; rà văn phong AI.
10. Tái sinh docx hồ sơ nộp; đối chiếu md↔docx.

---

## 7. CÔNG CỤ (SKILLS) ĐỀ XUẤT CHO TỪNG BƯỚC

| Bước | Skill |
|---|---|
| M3 — hình khung khái niệm | `conceptual-model-international-business`, `academic-conceptual-model-diagram`, `conceptual-model-scopus-wos` |
| M4 — kiểm tra trích dẫn | `chinh-sua-van-ban-hoc-thuat-scopus-wos`, lệnh `/ars-citation-check` (academic-paper) |
| N9 — Việt hóa thuật ngữ | `academic-translation-vietnamese` (+ `writing_guides/09b_vn_term_glossary.md`) |
| N10 — ký hiệu phi chuẩn | `chinh-sua-van-ban-hoc-thuat-scopus-wos` |
| N11 — biến thống kê | `academic-variable-formatter` |
| N12 — văn phong AI | `phd-academic-writing-humanizer` |
| Re-review sau sửa | `academic-paper-reviewer` (chế độ `re-review` / verification) |
| Toàn pipeline | `academic-pipeline` |

---

## 8. KẾT LUẬN PHẢN BIỆN

Đây là một luận án **có nội lực khoa học thật**, với đóng góp lý thuyết gốc đủ sức công bố Q1–Q2 nếu được hoàn thiện về hình thức và nhất quán. Các vấn đề phát hiện **không nằm ở chất lượng nghiên cứu** mà ở **tính nhất quán, hoàn chỉnh cấu trúc và chuẩn trình bày** — tất cả đều khắc phục được trong 4–6 tuần theo lộ trình trên.

**Quyết định: MAJOR REVISION đến có triển vọng cao đạt chuẩn sau khi sửa.**

> *Lưu ý: Báo cáo này là phản biện tài liệu (không chỉnh sửa nội dung khoa học). Các quyết định mang tính học thuật (vd: chốt 47 hay 49 nền kinh tế, có/không thêm IV) thuộc thẩm quyền NCS và hội đồng; báo cáo chỉ nêu rõ mâu thuẫn và đề xuất hướng xử lý.*
