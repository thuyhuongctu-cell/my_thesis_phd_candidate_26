# Đánh giá học thuật độc lập — Luận án tiến sĩ (Kinh doanh quốc tế, CTU)

> Người đánh giá: Inspector học thuật độc lập (LFE Academic Reviewer)
> Ngày: 2026-06-11
> Phạm vi: thesis/chuong_1..5_vi.md; thesis/04_references_apa7.md; chuyen_de/cd1 & cd2 (00_…_final_vi.md)
> Ground truth số liệu: `data_wbes/analysis/CANONICAL_RECONCILIATION.md` + `FP_DESCRIPTIVES_RESULTS.md`
> Nguyên tắc: grounded trên file thật, phân biệt rõ "đã đúng" vs "cần sửa", không sửa manuscript.

---

## 0. Tóm tắt điều hành

Luận án có chất lượng học thuật cao, mạch lập luận gap đến câu hỏi đến giả thuyết đến phương pháp đến kết quả đến kết luận chặt chẽ và nhất quán xuyên năm chương. Việc xử lý các nghiên cứu thành phần P1–P9 bằng nhãn "(P-label)/nghiên cứu thành phần" thay vì cite như nguồn ngoài đã xuất bản **về cơ bản là ĐÚNG** (xác nhận lại theo yêu cầu). Cảnh báo "artifact tiền tệ" trong CANONICAL **đã được xử lý đúng**: Chương 4 dùng phân tán (sd/CV của log LP đã winsorize/PPP theo country-year) và gradient ROS-tương đương, KHÔNG khẳng định mức năng suất thô tăng đơn điệu I–VI.

Tuy nhiên còn **một số lỗi số liệu nội bộ-mâu thuẫn mức MAJOR/CRITICAL** cần sửa trước bảo vệ, chủ yếu liên quan đến: (i) hệ số FIP của P8 trong Chương 5 mâu thuẫn với Chương 3/4; (ii) N exporters-only SIDS không nhất quán (26 vs 187 vs 132); (iii) số nền/pool trong CĐ1 chưa re-lock (101.185/47 nền/108 cặp) lệch bản canonical (91.982 analytic / 96.415 phân loại / 49 nền); (iv) một khẳng định "tăng đơn điệu" độ phân tán không khớp chính bảng số liệu của luận án.

**Kết luận: ĐẠT chuẩn bảo vệ CÓ ĐIỀU KIỆN** — phải sửa toàn bộ nhóm CRITICAL + MAJOR (đa số là sửa số/đồng bộ, không phải làm lại phân tích).

---

## 1. Scorecard từng tiêu chí

| Tiêu chí | Điểm | Mức cao nhất của lỗi | Nhận định |
|---|---|---|---|
| **Logic học thuật & mạch lập luận** | 8,5/10 | MINOR (một chỗ MAJOR) | Mạch gap đến RQ đến H đến method đến result đến conclusion rất chặt; H1–H6 + H1b + (H1c Ấn Độ) ánh xạ rõ. Lỗi: H1c (P9) xuất hiện ở Bảng 4.9 nhưng KHÔNG được phát biểu trong hệ giả thuyết Chương 2; "tăng đơn điệu" phân tán không khớp bảng. |
| **Nhất quán số liệu** | 6,5/10 | CRITICAL | Pool luận án (49 nền/91.982/96.415/102 cặp) nhất quán nội bộ trong 5 chương. Nhưng: FIP β mâu thuẫn (−1,339 vs −0,404); N exporters-only SIDS 3 giá trị khác nhau; CĐ1 chưa re-lock (101.185/47/108); P5 N (4.544 vs canonical 4.559). |
| **APA7 (in-text + ref list + P3–P9)** | 8,5/10 | MINOR | Xử lý P1–P9 bằng nhãn thành phần — ĐÚNG. Ref list phong phú, có DOI. Lỗi nhỏ: một số mục thiếu DOI; ghi "k=238" vs "hàng trăm cặp effect-size" mơ hồ; cite "Do & Phan (2025, IntechOpen)" đúng vì đã xuất bản thật. |
| **Thuật ngữ nhất quán (FSTS/LP/TCI/DAI/ICRV)** | 9/10 | MINOR | Rất nhất quán; glossary tốt. Lỗi nhỏ: crosswalk nhãn ICRV 5-regime (P6) vs 6-nhóm; tên cũ "Đang nổi/Cận biên" trong CĐ vs nhãn dữ liệu — đã có ghi chú nhưng dễ gây nhầm. |
| **Luận điểm rủi ro (artifact tiền tệ)** | 9/10 | đã xử lý đúng | KHÔNG có khẳng định mức năng suất thô tăng đơn điệu I–VI. Dùng phân tán + neo vào suy diễn P6/P7. Còn 1 lỗi câu chữ "tăng đơn điệu". |

**Điểm tổng hợp định tính: ĐẠT có điều kiện.** Không phát hiện lỗi học thuật nền tảng (fabrication, sai phương pháp, đạo văn, cite sai loại nguồn cho bài under-review).

---

## 2. Bảng issue chi tiết

Ký hiệu mức độ: **CRITICAL** = phải sửa trước bảo vệ (mâu thuẫn số/sai sự thật trong chính văn bản); **MAJOR** = nên sửa, ảnh hưởng độ tin cậy; **MINOR** = chau chuốt.

| # | File:line | Vấn đề | Đề xuất sửa | Mức độ |
|---|---|---|---|---|
| I-01 | chuong_5_…_vi.md:51 | **Hệ số FIP P8 mâu thuẫn nội bộ**: Mục 5.1.5 ghi `β = −0,404, p = ,032` trong khi Chương 3 (Mục 3.4.5.5, dòng 455), Chương 4 (Mục 4.7.2, dòng 223) và Mục 5.6.1 (dòng 191) đều ghi `β(FSTS_c) = −1,339, p < ,001` (M1 country+year FE). −0,404 không xuất hiện ở bất kỳ bảng nào. | Thay `β = −0,404, p = ,032` bằng giá trị canonical `β = −1,339, p < ,001 (M1, country+year FE)` hoặc nêu rõ đây là spec nào (không có spec nào cho ra −0,404 trong Bảng độ vững Mục 3.4.5.5). | **CRITICAL** |
| I-02 | chuong_5_…_vi.md:151 vs chuong_4_…_vi.md:225,217 | **N exporters-only SIDS không nhất quán**: Mục 5.5.2 ghi "SIDS exporters-only N = 187"; Mục 4.7.2 ghi "exporters-only, N = 26"; Mục 4.7.1 ghi "N_exporters = 132 (13,8%)"; Bảng Mục 3.4.5.5 ghi "Exporters-only (N = 26)". Ba con số 26/132/187 cho cùng một subset. | Thống nhất một định nghĩa: tổng số DN có FSTS>0 (=132) vs N đưa vào hồi quy exporters-only sau lọc missing (=26). Sửa Mục 5.5.2 "187" đến "26" (hoặc 132 nếu là nghĩa khác) và chú thích rõ chênh lệch do listwise deletion. | **CRITICAL** |
| I-03 | chuong_1_…_vi.md:57 vs 37,45,83,97; chuong_2:111 | **Số nền SIDS mâu thuẫn trong cùng Chương 1**: Mục 1.5.2 (dòng 57) ghi SIDS gồm "**9 nền** kinh tế đảo nhỏ Thái Bình Dương"; nhưng Mục 1.3, Mục 1.4, Mục 1.8.1, Mục 1.9 (dòng 37,45,83,97) và P8 đều ghi "**7 nền** Pacific SIDS". Chương 2 (dòng 111) lại ghi "9 nền". | Chuẩn hóa: mẫu CHÍNH P8 = **7 nền Pacific**; robustness mở rộng = **9 nền** (thêm Comoros + Timor-Leste). Sửa Mục 1.5.2 và Mục 2.3.3 (dòng 111) thành "7 nền (mẫu chính); 9 nền (robustness)" để khớp Bảng 2.1 (dòng 208) đã ghi đúng. | **MAJOR** |
| I-04 | chuong_2_…_vi.md:137 | **Danh sách nước SIDS trong P8 thiếu/khác**: liệt kê "(Fiji, Tonga, Solomon Islands, Vanuatu, Samoa)" = 5 nước, trong khi Mục 3.4.5.5 (dòng 424) liệt kê 7 nước (thêm Kiribati, Papua New Guinea). | Bổ sung đủ 7 nước Pacific cho khớp Chương 3, hoặc ghi rõ "ví dụ" nếu chỉ minh họa. Tránh liệt kê 5 nước khi mẫu là 7. | **MAJOR** |
| I-05 | chuong_3_…_vi.md:283 | **P5 China N lệch canonical**: ghi `pooled N = 4.544` (2.610 + 1.934). CANONICAL/anchor xác nhận N = **4.559**. Chênh 15 DN. | Đối chiếu lại dữ liệu thô; sửa về 4.559 nếu đúng canonical, hoặc giải trình listwise. Đồng bộ luôn 2012/2024 sub-N. | **MAJOR** |
| I-06 | chuong_4_…_vi.md:19 | **Khẳng định "tăng đơn điệu" không khớp chính Bảng 4.1**: dòng 19 nói sd log LP "tăng đơn điệu" từ thể chế cao đến thấp; nhưng Bảng 4.1 cho I=1,03 < III=1,29 > IV=1,24 < V=1,36 > VI=1,32 — KHÔNG đơn điệu (III>IV, V>VI). Đây cũng là rủi ro "artifact" prompt cảnh báo: gradient phân tán không trơn. | Đổi "tăng đơn điệu" đến "có xu hướng tăng (gần đơn điệu, với dao động giữa Nhóm III–IV và V–VI)". Tránh từ "đơn điệu" cho dữ liệu không đơn điệu. Lưu ý canonical: lp_z within-country-year sd ~đồng đều (0,92–1,00) đến khi z-chuẩn hóa, gradient phân tán BIẾN MẤT; cần nói rõ Bảng 4.1 là sd của log LP đã winsorize/PPP (chưa z-within), nên gradient một phần phản ánh khác biệt mức giữa nước. | **MAJOR** |
| I-07 | chuong_4_…_vi.md:276 vs chuong_2 Mục 2.5 | **H1c (Ấn Độ — tan biến ngưỡng) chưa có trong hệ giả thuyết Chương 2**: Bảng 4.9 (dòng 276) và Mục 5.6.1 báo cáo "H1c" như một giả thuyết được xác nhận, nhưng Chương 2 chỉ phát biểu H1–H6 + H1b (không có H1c). Chương 1 (dòng 105) mô tả P9 là "phát hiện" chứ không phải giả thuyết tiền nghiệm. | Hoặc (a) bổ sung phát biểu H1c vào Mục 2.5 như giả thuyết điều kiện biên thời gian; hoặc (b) đổi nhãn "H1c" thành "Phát hiện bổ sung P9 (post-hoc)" trong Bảng 4.9 để không tạo giả thuyết "ma" chưa khai báo. | **MAJOR** |
| I-08 | cd1/00_cd1_…_vi.md:99,113,122–126,205,210,274,377,843,859,1037,1047 | **CĐ1 chưa re-lock — dùng 101.185 DN / 47 nền / 108 cặp** xuyên suốt (abstract, mục tiêu, bảng, phụ lục), lệch canonical (analytic 91.982/49 nền; phân loại 96.415/52 nền). CANONICAL Mục 2 liệt kê đây là số "lỗi cần chuẩn hóa". | Re-lock CĐ1 về bản canonical: pool phân loại 96.415/52 nền đến khung phân tích 49 nền/91.982 (91.864). Ghi chú dòng 1049 đã thừa nhận "bản khóa CĐ1 = 101.185/47" — cần thực thi re-lock, không chỉ chú thích. | **CRITICAL** (cho CĐ1; nếu CĐ1 nộp riêng) / **MAJOR** (nếu chỉ là phụ lục lịch sử) |
| I-09 | cd2/00_cd2_…_vi.md:182,727,787,789 | **CĐ2 Nhóm VI = 8 nền (gồm Timor-Leste)** trong khi luận án/P8 mẫu chính = 7 Pacific. Tổng "5+6+6+7+17+8=49" — nhưng Bảng canonical đếm Nhóm VI `SIDS_small` n=1.885. Có ghi chú crosswalk nhưng con số "8 nền" dễ mâu thuẫn với "7 nền" ở luận án. | Giữ logic: phân loại 8 nền Nhóm VI (gồm Timor-Leste) là OK cho khung 49; nhưng nêu rõ P8 phân tích 7 Pacific. Đảm bảo tổng nhóm khớp 91.864 và nhãn nhất quán giữa CĐ2 ↔ Chương 4 Bảng 4.1 (VI=2.038 phân loại vs 1.885 analytic). | MINOR (đã có ghi chú) |
| I-10 | chuong_3_…_vi.md:539 | **Bảng 3.6 ghi "47 châu Á + Pacific economies"** trong khi toàn bộ Chương 3 và luận án dùng "49 nền". Sót số cũ. | Sửa "47" đến "49" ở dòng 539 (Mixed design row). | **MAJOR** (sai số rõ trong bảng tóm tắt) |
| I-11 | chuong_4_…_vi.md:138,303(ch3) | **Paternoster p-value gán nhầm vế**: Mục 4.4.2 (dòng 138) chỉ báo cáo `z = +0,82, p = ,412` (vế FSTS) cho "điểm turning point ổn định". Anchor canonical cho P5 ghi `p = ,545` (đó là vế FSTS², z = −0,61, theo Mục 3.4.5.3 dòng 303). Không sai, nhưng Chương 4 nên báo cáo CẢ HAI vế (FSTS p=,412 và FSTS² p=,545) để khớp anchor và đầy đủ. | Bổ sung vào Mục 4.4.2: "z(FSTS²) = −0,61, p = ,545" bên cạnh z(FSTS). Hiện chỉ có ở Chương 3. | MINOR |
| I-12 | chuong_4_…_vi.md:30 vs chuong_1:57 | **Bảng 4.1 Nhóm VI phân loại n = 2.038**, nhưng canonical phân loại VI = 2.038 Có và analytic VI = 1.885. Nhất quán. Tuy nhiên SIDS trong Bảng 4.1 liệt kê "FJI, PNG, SLB…" (Pacific) trong khi nhóm phân loại 96.415 có thể gồm cả Timor/Comoros. | Thêm chú thích Bảng 4.1: nhóm VI phân loại gồm 8 nền (Pacific 7 + Timor-Leste); P8 phân tích 7 Pacific. (Liên kết I-09.) | MINOR |
| I-13 | chuong_2_…_vi.md:103,135; chuong_3:33 | **P6 mô tả "K=288 effect sizes / k=238" nhưng Mục 4.2.1 (ch4:81) ghi "hàng trăm cặp effect-size đa dạng"** — mơ hồ, mất con số K=288. | Thay "hàng trăm cặp effect-size" bằng "K = 288 effect sizes" để nhất quán Chương 2/3. | MINOR |
| I-14 | chuong_1_…_vi.md:105 | **Roadmap ghi P7 = "JIBS, under revision"; P8 = "World Development, under revision"; P9 = "MIR/IJOEM, đang bình duyệt"** — trạng thái tạp chí đích. Cần đảm bảo KHÔNG cite các bài này như nguồn ngoài đã xuất bản ở chính văn. | Đã kiểm tra: chính văn dùng nhãn "(P7)/(P8)/(P9)/nghiên cứu thành phần" — ĐÚNG. Chỉ cần đảm bảo trang bìa/lời cam đoan công bố trạng thái under-review minh bạch. | MINOR (đã đúng, xác nhận) |
| I-15 | chuong_4_…_vi.md:202,158; figures | **Nhãn hình "Hình 4.x"** (placeholder) chưa đánh số chính thức (xuất hiện 2 lần: dòng 112 "Hình 4.x", dòng 202–204). | Đổi "Hình 4.x" đến số thứ tự chính thức (vd Hình 4.1, 4.2) trước bản nộp. | MINOR |
| I-16 | chuong_3_…_vi.md:193 | **Ghi chú M4 P3 ghi "(H4 thăm dò)"** nhưng M4 là điều tiết CSS/DAI (thuộc H3, không phải H4). Nhãn giả thuyết sai. | Sửa "(H4 thăm dò)" đến "(H3 thăm dò)" cho M4 Việt Nam (DAI/CSS là H3). Kiểm tra dòng 219 cũng ghi "H4 thăm dò" cho CSS_z. | **MAJOR** (gán sai giả thuyết) |

---

## 3. Phân biệt rõ "ĐÃ ĐÚNG" vs "CẦN SỬA"

### 3.1 ĐÃ ĐÚNG (xác nhận, không cần sửa)

1. **Xử lý P1–P9 theo chuẩn liêm chính học thuật**: toàn bộ chính văn dùng "(P3)…(P9)" / "nghiên cứu thành phần" — KHÔNG cite bài under-review như nguồn ngoài đã xuất bản. Đây là điểm prompt yêu cầu xác nhận: **ĐÚNG**. Ngoại lệ hợp lệ duy nhất là `Do & Phan (2025, IntechOpen)` được cite như nguồn ngoài — hợp lệ vì đã xuất bản thật (có DOI 10.5772/intechopen.1011012) và được nêu rõ là "công trình tiền đề" mà P9 mở rộng.

2. **Luận điểm artifact tiền tệ ĐÃ được xử lý đúng** (mục rủi ro #4 của prompt): Mục 4.1.1 KHÔNG khẳng định mức năng suất thô tăng đơn điệu I–VI. Thay vào đó dùng **độ phân tán** (sd log LP winsorize/PPP theo country-year) + neo vào suy diễn P6 (Q_M=17,35) và gradient TP của P7. Mục 4.1.1 còn tự hạ tông ("proxy gián tiếp cho TFPR", "mang bản chất mô tả"). Đây là cách xử lý đúng theo khuyến nghị canonical (option a/c). **Chỉ còn lỗi câu chữ "tăng đơn điệu" (I-06).**

3. **Pool số liệu cốt lõi của LUẬN ÁN (5 chương) nhất quán nội bộ**: 49 nền / 91.982 analytic / 96.415 phân loại / 102 cặp / nhóm ICRV (I=4.222/4.708, IV=50.926, V=18.569…) khớp canonical. KHÔNG tìm thấy "101.185 / 84.910-as-pool / 47 nền" trong 5 chương luận án (các số đó chỉ tồn tại ở CĐ1 chưa re-lock — I-08, và CĐ1 đã tự thừa nhận).

4. **N = 84.910 của P7 dùng ĐÚNG ngữ cảnh**: luôn được mô tả là "N hồi quy M2/mô hình đầy đủ sau listwise", KHÔNG nhầm là pool (canonical Mục 2 cảnh báo đúng điều này). Mục 4.6.1 và Mục 2.4 (dòng 135) đều ghi rõ "mẫu phân tích 91.982; N hồi quy mô hình đầy đủ = 84.910". Đúng.

5. **Mạch logic chương**: gap (Mục 2.4) đến RQ (Mục 1.4) đến H1–H6/H1b (Mục 2.5) đến method/model M0–M11 (Mục 3.4) đến results theo gradient ICRV (Mục 4) đến discussion CDCM (Mục 5). Ánh xạ Bảng 2.1 (P↔chương↔H) rõ ràng. Thuật ngữ FSTS/LP/TCI/DAI/ICRV nhất quán.

6. **Thận trọng thống kê tốt**: Singapore TP=88,6% được hạ tông đúng (CI vượt 100%, power ~16%, "consistent but underpowered"); SIDS exporters-only NS được thừa nhận thiếu power; trim-and-fill r=0,074 đến 0,035 báo cáo minh bạch.

### 3.2 CẦN SỬA (theo thứ tự ưu tiên)

- **CRITICAL (chặn bảo vệ)**: I-01 (FIP β=−0,404 sai), I-02 (N exporters-only 26/132/187), I-08 (CĐ1 re-lock 101.185/47 đến 91.982/49) nếu CĐ1 nộp như phần độc lập.
- **MAJOR (độ tin cậy)**: I-03, I-04 (SIDS 7/9/5 nước), I-05 (P5 N=4.544 vs 4.559), I-06 ("đơn điệu"), I-07 (H1c chưa khai báo), I-10 ("47" sót trong Bảng 3.6), I-16 (M4 gán "H4" thay vì "H3").
- **MINOR (chau chuốt)**: I-09, I-11, I-12, I-13, I-14, I-15.

---

## 4. Đánh giá theo từng chương (logic & lập luận)

- **Chương 1**: Bối cảnh đến vấn đề đến 3 khoảng trống đến mục tiêu đến RQ đến phạm vi đến giả thuyết tóm tắt đến đóng góp đến tính mới đến cấu trúc. Logic mạnh. Lỗi: SIDS 9 vs 7 nền (I-03); "Điểm mới thứ năm/thứ sáu" — đánh số "năm điểm mới" nhưng liệt kê SÁU (dòng 97: "năm điểm mới" rồi có "Điểm mới thứ sáu"). đến MINOR đếm sai.
- **Chương 2**: Khái niệm đến 4 lý thuyết + digital lens đến thực nghiệm 3 giai đoạn đến meta đến châu Á đến gap đến CDCM đến H1–H6/H1b đến Bảng ánh xạ. Rất chắc. Lỗi: danh sách SIDS 5 nước (I-04); thiếu H1c (I-07).
- **Chương 3**: Thiết kế mixed; PRISMA; đo lường biến (TCI/DAI non-overlapping — tốt); M0–M11 chi tiết cho từng P3/P4/P5/P7/P8/P9. Rất minh bạch. Lỗi: "47" sót (I-10); M4 gán H4 (I-16); P5 N (I-05).
- **Chương 4**: Mục 4.1 mô tả (xử lý artifact đúng) đến Mục 4.2 P6 meta đến Mục 4.3 SG đến Mục 4.4 CN đến Mục 4.5 VN đến Mục 4.6 P7 đến Mục 4.7 SIDS đến Mục 4.8 Ấn Độ đến Mục 4.9 tổng hợp H. Lỗi: "đơn điệu" (I-06); N exporters (I-02); H1c (I-07); "Hình 4.x" (I-15).
- **Chương 5**: Bàn luận CDCM đến so sánh tiền nhân đến đóng góp đến chính sách đến hạn chế đến kết luận. Lỗi nghiêm trọng nhất: FIP β=−0,404 (I-01) và N=187 (I-02). Hai số này phá nhất quán với Chương 3/4. Ngoài ra Mục 5.1.5 bị đánh số trùng (hai mục "5.1.5": FIP và Ấn Độ) — MINOR.

---

## 5. Kết luận đánh giá

**Luận án ĐẠT chuẩn bảo vệ CÓ ĐIỀU KIỆN.** Nền tảng học thuật (khung CDCM, ICRV, phân tách TCI/DAI, FIP, gradient turning point) vững; phương pháp minh bạch; liêm chính trích dẫn P-label đúng; cảnh báo artifact tiền tệ đã được xử lý đúng. Các lỗi còn lại **không phải lỗi phân tích gốc** mà là **mâu thuẫn số nội bộ và đồng bộ chưa hoàn tất**, sửa được bằng biên tập số học + re-lock, không cần chạy lại mô hình.

**Cần sửa TRƯỚC bảo vệ (bắt buộc):**
1. I-01: Sửa FIP β trong Mục 5.1.5 về −1,339 (p<,001) — hoặc nêu rõ spec.
2. I-02: Thống nhất N exporters-only SIDS (26 vs 132 vs 187) với định nghĩa rõ.
3. I-08: Re-lock CĐ1 (101.185/47/108 đến 96.415·52 / 91.982·49 / theo canonical).
4. I-03 & I-04: Chuẩn hóa SIDS = 7 nền Pacific (mẫu chính) / 9 nền (robustness); sửa danh sách 5-nước ở Mục 2.3.3.
5. I-10: Sửa "47" đến "49" trong Bảng 3.6.
6. I-16: Sửa nhãn M4 Việt Nam "H4" đến "H3".
7. I-07: Khai báo H1c trong Mục 2.5 hoặc đổi thành "phát hiện post-hoc P9".
8. I-05: Đối chiếu P5 N (4.544 vs 4.559).
9. I-06: Bỏ từ "đơn điệu" cho gradient phân tán không đơn điệu; làm rõ Bảng 4.1 là sd của log LP (chưa z-within) đến tránh hiểu lầm artifact.

**Nên sửa (chau chuốt):** I-09, I-11..I-15 + đếm "năm/sáu điểm mới" (Ch1) + mục "5.1.5" trùng số (Ch5) + "Hình 4.x".

So với bản review tự động của Copilot (vốn có báo động sai), đánh giá này grounded trên file thật: xác nhận luận án KHÔNG mắc các lỗi nền tảng (sai loại nguồn P-label, artifact tiền tệ chưa xử lý, pool sai trong chính luận án), và khoanh vùng chính xác các mâu thuẫn số có thật cần sửa.
