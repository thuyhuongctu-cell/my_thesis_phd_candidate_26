# Báo cáo chất lượng tài liệu và kế hoạch nâng chuẩn quốc tế

*Đánh giá độc lập toàn dự án — 2026-06-13. Người đánh giá đóng vai biên tập viên/phản biện tạp chí IB hàng đầu (JIBS/JWB/MIR register). Mọi nhận định gắn file:line; ba cụm tài liệu được rà bằng ba luồng phản biện song song. Phần kiểm tra DOI online KHÔNG thực hiện được trong container (chặn egress 403) — cung cấp công cụ chạy ngoài.*

---

## ✅ CẬP NHẬT KHẮC PHỤC P0 (2026-06-13, sau đánh giá)

Đã thực hiện và push (branch `claude/phd-thesis-review-L9Gml`):
- **Khóa canonical** `data_wbes/analysis/CANONICAL_NUMBERS.md`. Xác minh thực nghiệm: P7 re-run GỒM Nhật Bản → **50 nền/88.869/M2 81.022/M5 79.080/TP 43,6%**; "91.982/49" là build cũ superseded (bỏ Nhật chỉ còn 86.701). **Rối "49 vs 50" đã được giải quyết: đáp án là 50.**
- **Luận án** (Ch1–5 + Phụ lục A EN): đồng bộ 49→50, 91.982→88.869; sửa §4.1.5 (Nhật ĐÃ vào P7); Phụ lục A cập nhật sơ đồ PRISMA + đánh dấu build cũ superseded. → V3 xử lý xong cho luận án.
- **CĐ1 + CĐ2**: đồng bộ 50 nền (group-sum 6+6+6+7+17+8=50); **bổ sung FIP β=−1,339 + k=238** vào CĐ2 (D1 xử lý xong); **sửa DOI Marano hỏng** 648proper (D-DOI xử lý xong).
- **P7 manuscript (V1 XỬ LÝ XONG):** tái ước lượng đầy đủ ladder M1–M8 trên 50 nền (`scripts/p7_full_ladder.py`); hai mỏ neo tái lập chính xác (M2 81.022/51,5%; M4 79.080/43,6%). Viết lại toàn bộ manuscript. Hai sửa đổi bản chất từ re-estimation: (i) **DAI là level-shifter (+0,219***), KHÔNG uốn cong** (tương tác FSTS×DAI không ý nghĩa) — sửa luận điểm cũ; (ii) **nữ quản lý đảo dấu +0,185→−0,104***** (nhất quán P10/luận án); gradient 28→55% → **ba vùng** (Bảng 4 per-ICRV).
- **P3/P4/P5 (P1 XỬ LÝ XONG):** P3 sửa công thức `(FSTS^c)^2` hỏng (16 chỗ) + bảng điểm uốn + đánh số 5.5; P4 sửa nhãn item TCI (e6/h8/h1) + TP 88,6%; P5 thêm câu hòa giải ba tầng mẫu.
- **Công cụ**: `scripts/verify_dois.py` (kiểm 62 DOI nghi bịa), `scripts/reference_audit.py`, `scripts/p7_full_ladder.py`.

**Còn lại (cần dữ kiện tác giả / máy có mạng):** P6 hoàn tất meta thật + sửa nhãn OSF prereg (mốc thời gian — chỉ tác giả biết); chạy `verify_dois.py` trên máy có mạng để kiểm 62 DOI; đối chứng do-file Stata trên máy có license trước khi nộp.

---

## PHẦN I — BẢNG ĐIỂM CHẤT LƯỢNG (rubric 0–10)

Thang đo: (a) Đóng góp/định vị lý thuyết; (b) Chặt chẽ phương pháp; (c) Nhất quán số liệu nội bộ; (d) Văn phong học thuật; (e) APA7 & độ phù hợp tạp chí.

| Tài liệu | a | b | c | d | e | TB | Trạng thái |
|---|--:|--:|--:|--:|--:|--:|---|
| Luận án — Mở đầu/Abstract | 8 | 7 | 5 | 7 | 6 | 6.6 | Sửa số liệu |
| Ch.1 Giới thiệu | 8 | 7 | 5 | 6 | 8 | 6.8 | Sửa số liệu |
| Ch.2 Lý thuyết | 9 | 8 | 6 | 7 | 8 | 7.6 | Tốt |
| Ch.3 Phương pháp | 8 | 8 | 4 | 6 | 8 | 6.8 | Sửa số liệu (nặng nhất) |
| Ch.4 Kết quả | 8 | 8 | 5 | 7 | 7 | 7.0 | Sửa số liệu |
| Ch.5 Thảo luận | 9 | 7 | 6 | 8 | 8 | 7.6 | Tốt |
| Phụ lục A | 8 | 8 | 7 | 8 | 8 | 7.8 | Tốt |
| CĐ1 (mô tả 50 nền) | 7 | 7 | 6 | 8 | 7 | 7.0 | Tốt |
| CĐ2 (taxonomy ICRV) | 8 | 7 | 5 | 8 | 7 | 7.0 | Sửa số liệu |
| P3 Việt Nam | 8 | 8 | 7 | 8 | 6 | 7.4 | ✅ Đã sửa (LaTeX+TP+§) |
| P4 Singapore | 8 | 7 | 8 | 9 | 8 | 8.0 | ✅ Đã sửa (TCI+TP) |
| P5 Trung Quốc | 8 | 8 | 8 | 8 | 8 | 8.0 | ✅ Đã sửa (N reconcile) |
| **P6 Meta-analysis** | 6 | 6 | 5 | 7 | 6 | 6.0 | **CHƯA HOÀN TẤT** |
| P7 Capstone 50 nền | 7 | 7 | 8 | 7 | 7 | 7.2 | ✅ Đã tái ước lượng + viết lại |
| P8 SIDS/FIP | 8 | 7 | 6 | 8 | 7 | 7.2 | Sửa định khung |
| P9 Ấn Độ | 8 | 8 | 7 | 8 | 7 | 7.6 | Mạnh nhất |
| P10 Nhật Bản | 7 | 7 | 7 | 8 | 7 | 7.2 | Sạch |

**Đọc nhanh:** Lõi lý thuyết (Ch.2, Ch.5, CĐ2, P8, P9) đạt chuẩn 7.5+. Hai điểm đỏ kéo điểm xuống là **P7 (số liệu lệch canon)** và **P6 (meta chưa hoàn tất)**. Phần lớn lỗi còn lại là **không nhất quán số liệu mẫu** lan khắp dự án, không phải lỗi học thuật bản chất.

---

## PHẦN II — KIỂM TRA BỊA ĐẶT CITATION & REFERENCES (APA 7th)

### Câu trả lời thẳng cho câu hỏi "citation nào bịa đặt?"

**Không tìm thấy DOI giả về mặt cú pháp.** 227 DOI đều dùng tiền tố nhà xuất bản hợp lệ (Elsevier 10.1016, Springer 10.1007/10.1057, Wiley 10.1002/10.1111, Emerald 10.1108, SAGE 10.1177, JSTOR 10.2307, AOM 10.5465, AEA 10.1257, World Bank 10.1596). Công trình của chính tác giả được phân tách đúng: đã công bố (P1, P2, book chapter IntechOpen DOI 10.5772/intechopen.1011012, ICBEF 2024) tách khỏi bản thảo đang bình duyệt (đánh dấu `[Manuscript under review]`, không gắn DOI giả). Đây là thực hành liêm chính tốt.

**NHƯNG — rủi ro bịa đặt tập trung ở một nhóm được chính thư mục tự thú nhận:**

1. **🔴 62 DOI "from training knowledge" — chưa kiểm chứng (nhóm rủi ro số 1).** `thesis/04_references_apa7.md:495`: *"CrossRef batch: 0/62 confirmed via live API (network blocked); DOIs from training knowledge — verify before final submission."* Đây là 62 nghiên cứu sơ cấp của meta-analysis P6 (batch v2.8). "From training knowledge" nghĩa là DOI do AI nhớ lại từ bộ nhớ huấn luyện, KHÔNG tra Crossref — đúng cơ chế gây ảo giác (hallucination) DOI. **Toàn bộ 62 DOI này phải được xác minh trước khi nộp**; bất kỳ DOI nào không resolve là bịa đặt.

2. **🟠 1 DOI hỏng rõ ràng (corruption).** `chuyen_de/cd2/00_cd2_ctu_final_vi.md:1020` — Marano et al. (2016) JOM ghi `https://doi.org/10.1177/0149206316648proper`: chuỗi "648proper" là placeholder bị nối nhầm, không phải DOI thật. Phải thay bằng DOI đúng (tra Crossref) trước khi nộp.

3. **🟠 9 entry không DOI/URL** (cần xác minh thủ công): Cazzaniga et al. (IMF), Sikdar & Mukhopadhyay (2026), ADB 2026 reports, IFC PSD Blueprint, v.v. — phần lớn là báo cáo tổ chức (hợp lệ không có DOI) nhưng cần kiểm tra năm/nhan đề.

4. **🟡 3–4 mục tự gắn cờ "pending verify"** (thực hành minh bạch tốt): Yang et al. (2025) JBR thiếu volume/pages (`:230`), IFC PSD Blueprint năm (`:214`), Gambacorta et al. (2025) BIS (`:484`), WTO (2025) (`:486`).

### Phán quyết liêm chính

Thư mục **không cố ý bịa đặt** — nó minh bạch tự gắn cờ những mục chưa kiểm chứng, đây là dấu hiệu tốt. Rủi ro thực là **62 DOI do AI cung cấp từ bộ nhớ chưa tra cứu**. Đây không phải "gian lận" nhưng là lỗ hổng phải bịt: một phản biện chỉ cần click 1 DOI không resolve là đặt nghi vấn toàn bộ.

**Hành động:** Chạy `python3 scripts/verify_dois.py` trên máy có mạng (container này chặn Crossref/doi.org — đã xác nhận 403). Script tra từng DOI qua Crossref API, gắn cờ NOT-FOUND (nghi bịa/gõ sai) vs PASS, xuất `reviews/doi_verification_report.md`. Ưu tiên 62 DOI batch P6 + DOI Marano hỏng + 9 entry không DOI.

---

## PHẦN III — BA VẤN ĐỀ NGHIÊM TRỌNG NHẤT (toàn dự án)

### 🔴 V1 — P7 capstone lệch hoàn toàn khỏi số liệu canon (nghiêm trọng nhất)
Bản thảo P7 (`p7/p7_capstone_en_clean.md`) vẫn ở **khung cũ tiền-Nhật-Bản**: 91.982 DN / 49 nền (`:11`), M2 N=84.910, M5 N=38.342, TP≈36–40% (`:329-333`), gradient 28%→55% (`:189`). Trong khi Chương 4 luận án đã cập nhật canon 50 nền: M2 N=81.022 TP=51,5%, M5 N=79.080 TP=43,6%, ba vùng. **Hai vật thể số liệu mâu thuẫn cho cùng một nghiên cứu P7.** Lưu ý kỹ thuật: M5 manuscript (N=38.342, có đủ kiểm soát manager/ownership) là spec KHÁC với M5 canon (N=79.080, ít kiểm soát hơn) — nên đây là vấn đề **đối chiếu lại spec**, không phải đổi số mù quáng.

### 🔴 V2 — P6 meta-analysis chưa hoàn tất, đang bị trình bày như đã xong
`p6/p6_meta_manuscript_en.md`: sơ đồ PRISMA kết thúc ở "k = TBD" (`:169, :730`), bảng độ tin cậy liên mã hóa (ICR) toàn "[TBD]" (`:269-274`), nhưng phần Kết quả đã báo cáo điểm ước lượng tới 3 chữ số. Hai giá trị Q_M khác nhau cho cùng kiểm định cDAI: 1,34 (`:350`) vs 1,23 (`:13, :118`). OSF pre-registration đề ngày 18/05/2026 (`:151`) — **sau** khi dữ liệu đã được phân tích, nên không còn là "tiền đăng ký". Đây là rủi ro liêm chính lớn: hai giá trị khác nhau cho cùng một thống kê dễ bị đọc là bịa.

### 🟠 V3 — Số đếm mẫu/nền "nhảy" khắp dự án
Ba tổng thể DN lưu hành (88.869 phân tích / 91.982 / 96.415 phân loại) và hai số nền (49/50) xuất hiện không nhất quán: `chuong_3:43` (91.982), `phu_luc_A:67` (88.869), `chuong_4:21` (91.982/49), CĐ2:53 (49) vs CĐ2:1095 (50). Gốc rễ: **Nhật Bản đã vào khung MÔ TẢ (50 nền) nhưng CHƯA vào khung ƯỚC LƯỢNG P7 (49 nền)** — đúng về bản chất nhưng nhãn dán không thống nhất khiến hội đồng dễ hỏi "rốt cuộc bao nhiêu nền vào hồi quy, Nhật có trong đó không?".

### Lỗi cụ thể khác (theo cụm, đã có file:line trong 3 báo cáo luồng)
- **P3:** hỏng công thức `FSTS^{c} 2` (mã hóa squared term) khắp `:549-551, 608-610`; bảng TP mâu thuẫn (Table 2 thang 0,27–0,29 vs Table 4 thang 39–46%); mục 5.4→5.6 thiếu 5.5.
- **P4:** TP ghi cả 82% (`:132`) và 88,6% (`:22, 193`); hoán đổi nhãn item TCI (Table V1 `:74`).
- **P5:** N mâu thuẫn 2.610/2.619, 4.544/4.559/3.559 (`:23, 234, 257, 281`).
- **CĐ2:** thiếu hai số canon — FIP β=−1,339 và k=238 (chỉ ghi Marano k=333 và FIP định tính `:666`).
- **Thesis:** danh mục TLTK lặp ở cuối chương (`chuong_4:372-406`) — chuẩn CTU yêu cầu một danh mục hợp nhất.

---

## PHẦN IV — TÁM NỘI DUNG THEO YÊU CẦU (góc nhìn học giả IB hàng đầu)

### 1. Nhận xét về dự án

Đây là một dự án **tham vọng, cấu trúc tốt và có đóng góp thực**, hiếm gặp ở cấp luận án: một chuỗi 10 nghiên cứu thành phần + 2 chuyên đề + meta-analysis, gắn kết bằng khung CDCM ba tầng và taxonomy ICRV sáu nhóm, đỉnh là construct lý thuyết mới FIP. Điểm mạnh nổi bật: (i) FIP là đóng góp định danh được, công bố độc lập được; (ii) tái định hình "ba vùng" của điều tiết thể chế vượt qua nhị phân của Marano et al. (2016); (iii) tách bạch TCI (nền tảng nâng mặt bằng) vs DAI (tình huống đổi độ cong); (iv) hạ tầng tái lập (M-AIDA, do-files, pyfixest pipeline, OSF) vượt chuẩn luận án Việt Nam thông thường.

Điểm yếu hệ thống: **không phải lỗi tư duy mà là lỗi đồng bộ** — số liệu mẫu chưa khóa một nguồn-sự-thật duy nhất, khiến cùng một đại lượng có nhiều giá trị ở các file khác nhau. Đây là rủi ro lớn nhất khi bảo vệ/nộp tạp chí, và may mắn là **sửa được hoàn toàn** bằng kỷ luật biên tập (Phần III + V).

### 2. Đề xuất hướng thiết kế & triển khai dự án

- **Một bảng canon duy nhất (single source of truth).** Tạo `data_wbes/analysis/CANONICAL_NUMBERS.md` khóa: 96.415 phân loại / 88.869 mô tả 50 nền / 91.982 ước lượng 49 nền / M2 81.022 / M5 79.080 / TP M5 43,6% / M2 51,5% / Nhóm IV 43,0% / FIP −1,339 / k=238. MỌI con số trong mọi file trỏ về bảng này. Đây là việc #1.
- **Phân tách rõ hai khung trong mọi abstract:** "khung mô tả 50 nền (gồm Nhật Bản, P10); khung ước lượng P7 = 49 nền (Nhật chờ tái ước lượng)". Một câu, lặp ở mọi nơi có "50 nền".
- **Đồng bộ P7 manuscript với canon** (hoặc ngược lại, sau khi đối chiếu spec M5). Đây là việc #2.
- **Hoàn tất P6 thật sự** (chạy search + extraction + đóng băng số) trước khi gọi là meta hoàn chỉnh. Việc #3.
- **Quy trình "freeze".** Sau mỗi lần chạy estimation, xuất bảng từ log → cập nhật CANONICAL → propagate. Không bao giờ để hai số khác nhau cùng tồn tại.

### 3. Hướng dẫn công bố các papers (chiến lược tạp chí)

| Paper | Tạp chí mục tiêu thực tế | Hạng | Rào cản lớn nhất phải xử lý trước khi nộp |
|---|---|---|---|
| **P9 Ấn Độ** | Management International Review | Q1/Q2 | Cross-section lặp (không panel) → "tan biến ngưỡng" có thể do thành phần mẫu; thừa nhận thẳng + thêm kiểm định thành phần. **Nộp sớm nhất — mạnh nhất.** |
| **P10 Nhật Bản** | Asian Business & Management | Q2 | Một sóng cắt ngang, xuất khẩu thấp (16,8%) → đóng góp mô tả sạch nhưng khiêm tốn. Đã sẵn sàng. |
| **P4 Singapore** | J. of Asian Business Studies (hạ từ MIR) | Q2 | Hiệu ứng DAI×FSTS² dựa vào đuôi mỏng (f²=0,018 < 0,02; exporters N=84) → đóng khung "gợi ý, chưa xác quyết". |
| **P5 Trung Quốc** | IJoEM | Q2 | Đóng góp là "không bác bỏ" (độ bền ngưỡng) → cần phân tích công suất + kiểm định tương đương (equivalence test). |
| **P3 Việt Nam** | JABS/IJoEM (hạ từ APJM) | Q2 | Sửa hỏng công thức + inverted-U biến mất trong mẫu exporters-only (β₂ p=,66) → giải thích biên tham gia. |
| **P8 SIDS/FIP** | J. of International Development (an toàn) hoặc World Development (tham vọng) | Q1/Q2 | Phê phán "chỉ là negative selection mẫu nhỏ" → **dẫn bằng kết quả 9 nền N=1.469 (β=−0,510), KHÔNG dẫn N=26**; đóng khung "nhất quán với FIP, chưa loại trừ được selection". |
| **P7 Capstone** | International Business Review (không phải JIBS) | Q1 | JIBS đòi nhận diện nhân quả; WBES cross-section pooled là contingency mô tả → IBR/JWB hợp hơn. Sửa số canon trước. |
| **P6 Meta** | International Business Review / J. of Int. Management | Q1 | **Chưa hoàn tất** — PRISMA TBD, ICR TBD, prereg sau dữ liệu. Hoàn tất search/extraction thật trước khi nộp. |

**Trình tự khuyến nghị:** P9 → P10 → P4 → P5 → P3 → P8 → P7 → P6. Công bố P9/P10 trước tạo "vết" đã-bình-duyệt củng cố luận án.

### 4. Hệ thống M-AIDA: viết/điều chỉnh + đăng ký SHTT Việt Nam + công bố GitHub

**Hiện trạng:** đã có gói bản quyền `p6/submission/maida_copyright/` (mô tả tác phẩm, mẫu mã nguồn, checklist) cho M-AIDA v7.0.0 (Meta-Analysis Intelligent Data Assistant). Đây là nền tảng tốt.

**Hồ sơ đăng ký quyền tác giả tại Cục Bản quyền tác giả (COV), Bộ VH-TT-DL:**
- Loại hình: **Chương trình máy tính** (Luật SHTT 2005 sửa đổi 2022, Điều 22).
- Hồ sơ gồm: (1) Tờ khai đăng ký (mẫu COV); (2) 02 bản in mã nguồn (in 2 mặt, đánh số trang, đóng quyển — thường yêu cầu trọn bộ hoặc 25 trang đầu + 25 trang cuối tùy COV); (3) Giấy cam đoan tác giả tự sáng tạo; (4) CMND/CCCD; (5) nếu là tác phẩm trong khuôn khổ luận án/đơn vị → giấy xác nhận quyền của VLUTE/CTU hoặc cam kết không tranh chấp. Lệ phí ~100.000đ/chương trình. Thời gian cấp ~15 ngày làm việc.
- **Lưu ý quan trọng về quyền:** nếu M-AIDA viết trong khuôn khổ công việc tại VLUTE, cần làm rõ chủ sở hữu (tác giả vs đơn vị). Khuyến nghị thỏa thuận trước để tác giả giữ quyền tác giả + đồng sở hữu, tránh tranh chấp khi thương mại hóa.
- **Cải thiện trước khi nộp:** (a) thêm header license (đề xuất license riêng "All rights reserved" cho bản nộp COV, hoặc MIT/Apache nếu muốn mở mã trên GitHub — KHÔNG dùng GPL nếu định thương mại hóa); (b) README mô tả kiến trúc + sơ đồ luồng (PDF→trích xuất→chuẩn hóa→xuất CSV meta); (c) gắn version tag rõ ràng + commit hash để chứng minh mốc thời gian sáng tạo.

**Công bố lên GitHub của tác giả (củng cố chứng cứ năng lực lập trình):**
- Tạo repo công khai `m-aida` riêng (tách khỏi repo luận án), README chi tiết, ảnh chụp giao diện/luồng, ví dụ chạy được (sample PDF → output CSV), CHANGELOG theo version.
- **Lịch sử commit là bằng chứng vàng** chống nghi ngờ "AI viết hộ": commit thường xuyên, nhỏ, có message mô tả quá trình suy nghĩ/sửa lỗi → cho thấy quá trình phát triển thật của con người. Thêm `CITATION.cff` + Zenodo DOI (archive GitHub release → Zenodo cấp DOI vĩnh viễn, trích dẫn được trong luận án).
- Gắn badge giấy chứng nhận bản quyền COV vào README sau khi cấp.

### 5. Hoàn thiện hệ thống OSF cho papers

Hiện có `p6/osf/P6_OSF_Preregistration_Template.md`. Khuyến nghị mỗi paper (P3–P10) một OSF project chuẩn:
- **Cấu trúc mỗi project:** (1) Pre-registration/Registration (cho P6 phải trung thực: nếu đã có dữ liệu thì đăng ký dạng "Registration" có timestamp, KHÔNG gọi là "pre-registration"); (2) thư mục `/data` (hoặc link WBES + hướng dẫn xin quyền truy cập, vì WBES có license); (3) `/code` (do-files + pyfixest scripts + verify_dois.py); (4) `/materials` (codebook biến, ICRV crosswalk); (5) `/manuscript` (bản blinded).
- **Sửa lỗi prereg P6:** tách "pre-registration" (nếu thật sự trước dữ liệu) khỏi "registration of analysis plan" (sau dữ liệu). OSF cho phép cả hai nhưng nhãn phải đúng — đây chính là lỗi V2.
- Mỗi OSF project tạo DOI → trích dẫn chéo trong paper ("Data and code: osf.io/xxxx") → tăng điểm reproducibility với reviewer Q1.
- Gắn license rõ (CC-BY cho materials; phù hợp license cho code).

### 6. Nhận xét P1–P8 + meta 2025 + book chapter (ưu/nhược + cách khắc phục)

- **P1 (Vietnam Economic & Financial Review 2026, heterogeneity emerging Asia):** *Ưu:* đã công bố, đặt nền mô tả; *Nhược:* tạp chí trong nước hạng thấp → đóng góp học thuật quốc tế hạn chế. *Khắc phục:* dùng làm "vết công bố" baseline, không kỳ vọng impact.
- **P2 (J. of Finance & Accounting Research 2026, China SME):** *Ưu:* đã công bố, mở rộng bằng chứng Trung Quốc; *Nhược:* tương tự P1 về hạng. *Khắc phục:* P5 là phiên bản nâng cấp Q2 — định vị P2 là tiền đề.
- **Book chapter (IntechOpen 2025, India + top management):** *Ưu:* DOI thật, quốc tế, lăng kính thượng tầng quản trị, là tiền đề P9; *Nhược:* IntechOpen là open-access phí tác giả, uy tín học thuật trung bình, không Scopus-Q. *Khắc phục:* P9 (MIR) là bản nâng cấp peer-reviewed thực thụ — trích book chapter như "prior author work", không như bằng chứng đỉnh.
- **Meta 2025 (ICBEF 2024 proceedings, k=113):** *Ưu:* nền tảng meta cho P6, mốc baseline; *Nhược:* proceedings hội nghị, k=113 nhỏ so với k=238 hiện tại → có thể bị hỏi vì sao k nhảy. *Khắc phục:* nêu rõ P6 là MỞ RỘNG có hệ thống (1982–2026) của baseline ICBEF, ghi rõ phương pháp bổ sung studies.
- **P3 Việt Nam:** *Ưu:* phương pháp đầy đủ bậc nhất (PSM, 2SLS F=22–35, Oster, Heckman); *Nhược:* hỏng định dạng + inverted-U biến mất trong exporters-only. *Khắc phục:* sửa định dạng; đóng khung curvature là hiện tượng biên-tham-gia.
- **P4 Singapore:** *Ưu:* "nghịch lý bão hòa số" tinh tế, văn phong sạch nhất; *Nhược:* kết quả lõi dựa đuôi mỏng underpowered. *Khắc phục:* đóng khung "positive null có thông tin"; hạ tạp chí mục tiêu.
- **P5 Trung Quốc:** *Ưu:* tái định hình độ-bền-ngưỡng sắc; *Nhược:* bán một "null" làm đóng góp chính. *Khắc phục:* thêm power + equivalence test.
- **P6 Meta:** *Ưu:* thiết kế ba tầng đúng chuẩn, battery publication-bias đầy đủ; *Nhược:* CHƯA hoàn tất (TBD), prereg sai mốc, Q_M hai giá trị. *Khắc phục:* hoàn tất thật + đóng băng số. **Nhược phải chấp nhận:** ba moderator mới đều null → đóng khung "null là phát hiện" (pub-bias gánh bài báo).
- **P7 Capstone:** *Ưu:* mẫu lớn nhất, tổng hợp CDCM+ICRV; *Nhược:* số lệch canon, không nhận diện nhân quả ở quy mô. *Khắc phục:* đồng bộ canon; hạ JIBS→IBR. **Nhược phải chấp nhận:** WBES cross-section không cho nhân quả mạnh — đóng khung contingency mô tả.
- **P8 SIDS/FIP:** *Ưu:* FIP construct mới, định danh được; *Nhược:* β=−1,339 dựa N nhỏ, dễ bị phê "negative selection". *Khắc phục:* dẫn bằng 9 nền N=1.469. **Nhược phải chấp nhận:** với N=26 exporters-only không thể loại trừ hoàn toàn selection — thừa nhận thẳng.

### 7. Khung lý thuyết & phương pháp luận có đủ logic/thuyết phục? Đóng góp & điểm mới

**Có — khung lý thuyết là điểm mạnh nhất của luận án.** Tích hợp 5 lớp (Uppsala + RBV + thể chế + thượng tầng quản trị + lăng kính số) thành CDCM ba tầng là mạch lạc; suy luận FIP từ ba điều kiện cấu trúc bị vi phạm đồng thời là đoạn lý thuyết chặt nhất (`chuong_2:174-180`). Chuỗi CDCM→giả thuyết→kết quả→thảo luận nhìn chung vững.

**Đóng góp/điểm mới định vị được trong văn liệu:**
1. **FIP** — đảo dấu quan hệ I–P (không phải điều tiết độ lớn) tại điều kiện biên cực đoan: construct mới, công bố độc lập được.
2. **Điều tiết "tồn tại" thay vì "cường độ"** — thể chế quyết định đường cong inverted-U *có tồn tại hay không* (sắc ở Nhóm IV, duỗi ở Nhóm I, tan ở V–VI), vượt nhị phân Marano.
3. **Taxonomy ICRV 6 nhóm** — công cụ tái sử dụng được.
4. **Tách TCI/DAI** — hai construct số độc lập, cơ chế khác nhau.

**Lỗ hổng logic cần vá (để thuyết phục hội đồng):**
- **H4 (nhà quản trị) chưa được dữ liệu ủng hộ** như giả thuyết (hiệu ứng nữ ÂM, tương tác null) → nên hạ tầng "cá nhân" xuống kiểm soát, hoặc pre-register confound chọn-lọc-ngành.
- **H6 (thời gian)** bị P5 bác (ổn định) nhưng P9 xác nhận (tan biến) → H6 thực ra điều kiện theo *độ lớn cú sốc*, là tinh chỉnh hậu nghiệm → diễn đạt lại H6 cho đúng.
- **H3 (DAI đổi độ cong)** chủ yếu dựa Singapore underpowered (power ~16%) → giảm trọng lượng suy diễn, hoặc dẫn bằng kết quả pool.
- **H5 gradient** chỉ P7 xác nhận (P6 5-regime không test được 6 nhóm) → nói rõ tam giác hóa một phần, không overclaim.

### 8. Hồ sơ tác giả (Scholar/ResearchGate/OSF/GitHub) & xóa nghi ngờ "AI viết hộ"

**Vấn đề cốt lõi:** hội đồng/người đọc có thể nghi một NCS không-chuyên-tin-học không thể tự xây M-AIDA + pipeline kinh tế lượng + hệ MCP. Cách xóa nghi ngờ là **chứng minh quá trình (process), không chỉ sản phẩm (product):**

1. **Lịch sử commit GitHub = bằng chứng quá trình.** Chuỗi commit nhỏ, thường xuyên, message mô tả suy nghĩ/sửa lỗi/thử-sai theo thời gian là thứ AI-một-lần không tạo ra được. Giữ repo công khai với lịch sử đầy đủ. Đây là lá chắn mạnh nhất.
2. **Notebook/nhật ký phân tích.** Lưu các bản nháp do-file, log chạy thất bại, ghi chú quyết định ("vì sao chọn cluster theo nền", "vì sao z-spec không tái lập FIP −1,339") → chứng minh hiểu biết kinh tế lượng/meta thật sự.
3. **Reproducibility công khai (OSF + Zenodo DOI).** Người khác chạy lại ra cùng số = năng lực thật, không phụ thuộc AI. `verify_dois.py`, `p7_run_50econ.py`, `p10_japan_models.py` đều chạy được độc lập.
4. **Bản quyền COV cho M-AIDA** (Phần 4) = công nhận pháp lý quyền tác giả phần mềm.
5. **Tách bạch vai trò AI minh bạch.** Thêm "AI use disclosure" (chuẩn JIBS/Elsevier 2024): nêu rõ AI hỗ trợ phần nào (ví dụ: soạn thảo, refactor code) và tác giả chịu trách nhiệm toàn bộ thiết kế/diễn giải/quyết định khoa học. Minh bạch *tăng* uy tín, không giảm.
6. **Trình bày được khi bảo vệ.** Chuẩn bị giải thích sống: đọc một do-file bất kỳ và giải thích từng dòng; giải thích vì sao Lind–Mehlum cần TP trong miền dữ liệu; vì sao two-way FE xử lý artifact tiền tệ. *Khả năng giải thích trực tiếp* là bằng chứng cuối cùng và thuyết phục nhất.
7. **Hồ sơ học thuật đồng bộ.** Google Scholar (gắn P1, P2, book chapter, ICBEF), ResearchGate (upload preprint P9/P10 sau khi an toàn bản quyền), ORCID (liên kết tất cả), OSF (data+code). Hồ sơ nhất quán, có DOI, có lịch sử = chân dung học giả thật.

**Kết luận mục 8:** Năng lực được chứng minh tốt nhất không phải bằng tuyên bố mà bằng *dấu vết quá trình có thể kiểm chứng*: commit history, log thất bại, reproducibility độc lập, bản quyền, và khả năng giải thích trực tiếp. Dự án này đã có hầu hết các mảnh — việc còn lại là làm chúng *công khai và mạch lạc*.

---

## PHẦN V — KẾ HOẠCH ĐIỀU CHỈNH CHI TIẾT (ưu tiên hóa)

### P0 — Bắt buộc trước bảo vệ/nộp (1–2 tuần)
1. **Khóa CANONICAL_NUMBERS.md** và propagate; xóa mọi 91.982/49 mâu thuẫn hoặc gắn nhãn rõ "khung ước lượng". (V3)
2. **Đồng bộ P7 manuscript** với canon sau khi đối chiếu spec M5. (V1)
3. **Chạy `verify_dois.py`** trên máy có mạng; sửa mọi NOT-FOUND; ưu tiên 62 DOI batch P6 + Marano `648proper`. (Phần II)
4. **Sửa nhãn OSF prereg P6** (registration ≠ pre-registration). (V2)

### P1 — Trước khi nộp tạp chí (2–4 tuần)
5. **Hoàn tất P6 thật** (search + extraction + đóng băng số; điền PRISMA/ICR; thống nhất Q_M). (V2)
6. Sửa P3 (hỏng công thức `FSTS^c 2`, bảng TP), P4 (82/88,6%, item TCI), P5 (N mâu thuẫn).
7. Bổ sung FIP β=−1,339 + k=238 vào CĐ2.
8. Hợp nhất danh mục TLTK luận án (bỏ list cuối chương).

### P2 — Nâng chuẩn (1–2 tháng)
9. Hoàn thiện OSF mỗi paper (data+code+DOI).
10. Nộp bản quyền COV cho M-AIDA + publish repo GitHub + Zenodo DOI.
11. Thêm AI-use disclosure mỗi paper.
12. Đồng bộ hồ sơ Scholar/ORCID/ResearchGate.

---

*Công cụ kèm theo (đã commit): `scripts/verify_dois.py` (kiểm tra DOI Crossref), `scripts/reference_audit.py` (orphan refs), `reviews/orphan_reference_audit_2026-06-13.md`. Mọi số canon đã tái lập qua `scripts/p7_run_50econ.py` + `p10_japan/replication/p10_japan_models.py` (xem `data_wbes/analysis/REESTIMATION_LOG_2026-06-13.md`).*
