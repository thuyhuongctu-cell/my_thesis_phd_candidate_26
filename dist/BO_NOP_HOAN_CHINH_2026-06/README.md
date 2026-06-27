# Bộ nộp hoàn chỉnh — NCS Đỗ Thùy Hương (VLUTE / CTU)

> Cập nhật **2026-06-26** (dựng lại toàn bộ; bổ sung S238 đóng khe k=238 ở Phụ lục D, và các sửa CĐ1/CĐ2: số nội bộ, trích dẫn Wu Fan & Chen, Unicode→math). Trước đó 2026-06-23 (dựng lại toàn bộ từ nguồn đã hiệu chỉnh bằng
> `scripts/build_bo_nop_package.sh`). Tất cả số liệu **của các gói LIVE** đã đồng bộ về **khung canonical 50 nền**; các bản nháp thế-hệ-trước (P7 APJM/JIBS khung 49 nền; P8 EJDR/JID/World Development khung −1.339) được **giữ lại có gắn nhãn SUPERSEDED — không nộp**.
> Phân cấp khung (đã tái lập được): pool phân loại **96.415 DN / 52 nhãn** ⊇ khung phân tích
> **88.869 DN / 50 nền** ⊇ khung mô tả LP hợp lệ **84.998 DN / 50 nền / 107 cặp nền-năm**
> (cơ sở của Bảng 4.1/4.2 và bảng tương quan) ⊇ hồi quy P7 M2 **81.022** (master-locked).
> Khung mô tả giữ Timor-Leste trong Nhóm VI; nghiên cứu SIDS P8 loại Timor (7 nền Pacific).
> Thuật ngữ thống nhất: quan hệ I–P "mất cấu trúc" (Nhóm V/VI); "phổ thể chế" (ICRV).

Thư mục gồm 3 phần: (1) papers đủ điều kiện nộp, (2) hai chuyên đề, (3) năm chương luận án + phụ lục.

---

## 0. Tóm tắt đóng góp cốt lõi (Executive Summary of Contributions)

Năm đóng góp định hướng toàn bộ công trình; hội đồng nên đọc README này trước, rồi tra
ngược về chương/paper tương ứng:

1. **Khung CDCM (Country–Digital–Capability Moderation).** Tái khái niệm hóa quan hệ
   quốc tế hóa–hiệu quả (I–P) thành một quan hệ *được điều tiết bởi thể chế*: thể chế chi
   phối **độ lớn, dấu, và hình dạng** đường cong (luận điểm apex, nêu ở thì thăm dò/có điều
   kiện). → Chương 2–3; CĐ1/CĐ2.
2. **Phân loại sáu tiểu chế độ ICRV** (I Advanced_innovation … VI SIDS_small) cho 50 nền
   châu Á–Thái Bình Dương, dựng trên khung canonical WBES 88.869 DN. → Chương 3–4; P7.
3. **Cấu trúc ba vùng giải mâu thuẫn văn liệu I–P châu Á.** Đường cong chữ U ngược *sắc nét*
   ở chế độ chuyển đổi (Nhóm IV, TP ≈ 43%), *gần tuyến tính* ở chế độ thể chế mạnh nhất
   (Nhóm I, đỉnh ngoài tầm quan sát), *tan biến* ở chế độ yếu nhất (Nhóm V/VI) — hòa giải
   các phát hiện tuyến-tính-dương vs null/âm trước đây. → P7; Chương 4.
4. **FIP (Forced Internationalization Penalty)** như điều kiện biên: ở nhóm Pacific SIDS,
   quan hệ đảo dấu (không có cực đại nội vi). → P8; Chương 4–5.
5. **Tổng hợp meta-analysis ba cấp k=238 (K=288 cỡ hiệu ứng, MARA/metafor)** kết nối tám
   nghiên cứu thành phần P3–P10 thành một luận điểm thống nhất (kappa synthesis essay). → P6;
   essay kappa.

## 0b. Đạo đức nghiên cứu & minh bạch dữ liệu (Research Ethics & Data Transparency)

- **Nguồn dữ liệu thứ cấp, ẩn danh:** phân tích dùng vi dữ liệu **World Bank Enterprise
  Survey (WBES)** đã ẩn danh ở cấp doanh nghiệp; không thu thập dữ liệu người tham gia mới,
  không có thông tin định danh cá nhân (PII). Không yêu cầu phê duyệt IRB cho dữ liệu thứ cấp
  công khai này.
- **Tái lập (reproducibility):** mỗi paper kèm replication package (`p*/replication/`);
  kết quả đã đối chiếu chéo Python↔Stata (xem `reviews/REPLICATION_CROSSCHECK_2026-06-23.md`).
  Các số liệu công bố khóa theo `data_wbes/analysis/CANONICAL_NUMBERS.md` (master-lock).
- **Công bố dùng AI:** quy trình trích xuất M-AIDA và mức độ hỗ trợ của công cụ AI được khai
  báo minh bạch tại **Phụ lục B** (`phu_luc_B_maida_vi`).
- **Liêm chính trích dẫn:** không bịa trích dẫn/DOI; các mục chờ xác minh online được gắn
  nhãn rõ ràng và để NCS xác minh trên máy có mạng (Crossref bị chặn 403 trong môi trường
  dựng bộ nộp — xem mục 4 và `reviews/P6_PHASE_B_HANDOFF.md`).

---

## 1. Papers đủ điều kiện submit (`1_papers/`)

Mỗi gói gồm 4 file: `01_manuscript_blinded.docx` (bản tiếng Anh ẩn danh để nộp tạp chí),
`02_title_page.docx`, `03_cover_letter.docx`, và **`04_ban_dich_vi.docx`** (bản dịch tiếng Việt
đầy đủ cho hồ sơ luận án/hội đồng CTU — kèm hình minh họa với P3/P4/P5).
Đích tạp chí là **gói live** (đã loại các gói DEPRECATED), theo `DEPRECATED.md` trong từng paper.

| Thư mục | Paper | Tạp chí đích (live) | Hạng | Cổng nộp |
|---|---|---|---|---|
| `P3_JED/` | P3 Việt Nam | Journal of Economics and Development (Emerald) | Scopus/WoS, Diamond OA | emeraldgrouppublishing.com/journal/jed |
| `P4_MIR/` | P4 Singapore | Management International Review (Springer) | ABS-3 | mc.manuscriptcentral.com/mir |
| `P5_IJOEM/` | P5 Trung Quốc | International Journal of Emerging Markets (Emerald) | ABS-1 | mc.manuscriptcentral.com/ijoem |
| `P6_JWB/` | P6 Meta-analysis | Journal of World Business (Elsevier) | ABS-4* | editorialmanager.com/jwb |
| `P7_IBR/` | P7 Đa quốc gia | International Business Review (Elsevier) | ABS-3 | editorialmanager.com/ibr |
| `P8_World_Development/` | P8 Pacific SIDS | World Development (Elsevier) | ABS-4* | editorialmanager.com/worlddev |
| `P9_MIR/` | P9 Ấn Độ | Management International Review (Springer) — primary; IJOEM thay thế | ABS-3 | mc.manuscriptcentral.com/mir |
| `P10_ABM/` | P10 Nhật Bản | Asian Business & Management (Palgrave) | ABS-2 | — |

**Lưu ý định tuyến (đã sửa khỏi số liệu/đích cũ):**
- P3 → **JED** (không phải JABS — JABS/MBR/Thunderbird đã DEPRECATED).
- P6 → **JWB** đầu ladder (JWB → JIM → APJM); IBR đã chuyển cho P7.
- P7 → **IBR** (JIBS bị loại: pooled cross-section không đạt kỳ vọng nhận dạng nhân quả của JIBS).
  Bản IBR dùng khung 50 nền: M2 N=81.022 (TP 51,5%), M5 N=79.080 (TP 43,6%).
- P8 → bản **redesign 2026-06-19** (7 nền Pacific, loại Timor-Leste).
- P9 → **MIR** (primary; IJOEM thay thế). Bản India đã hòa giải: N gộp phân tích 28.717
  (3 đợt 2014/2022/2025); phát hiện "tan biến điểm uốn" theo thập kỷ chuyển đổi thể chế.
- P10 → **ABM** (Asian Business & Management); Nhật Bản 2025 (N=2.168, đợt WBES khai mở).

**Ghi chú độ sẵn sàng nộp (2026-06-20):**
- P3 trong bundle là **bản 8.500 từ** (`_8500`) đúng giới hạn JED (bản đầy đủ vượt cap, không nộp JED).
- Tự-trích-dẫn của P5/P6/P7/P9 đã **ẩn danh** ("Authors, năm") cho double-blind; OSF DOI của P6 đã điền (10.17605/OSF.IO/Z37KN).
- Cover letter P9 đã điền ngày (20 June 2026).
- LaTeX: primary non-Emerald kèm `04_manuscript_latex.pdf` (P4/P6/P7/P8/P9/P10). Mỗi paper có ≥3 hồ sơ/3 tạp chí với LaTeX cho đích non-Emerald; xem `reviews/JOURNAL_FORMAT_MATRIX.md`. Abstract theo house-style (Emerald structured / khác unstructured); tự-trích-dẫn đã ẩn danh ở mọi gói.
- Còn lại lúc nộp (không chặn): giá trị κ mã hóa ICRV của P6 chờ dual-coding thật.

## 2. Hai chuyên đề (`2_chuyen_de/`)

> Định dạng chuẩn CTU (QĐ 1799/SH): TeX Gyre Termes 13pt, lề trái 3cm / phải-trên-dưới 2cm,
> giãn dòng 1,2. PDF biên dịch bằng XeLaTeX; docx dùng template `ctu_thesis_reference.docx`.

| File | Nội dung |
|---|---|
| `CD1_CTU.pdf` / `.docx` | Chuyên đề 1 — định dạng CTU (36 trang) |
| `CD2_CTU.pdf` / `.docx` | Chuyên đề 2 — mô hình khái niệm & thiết kế thực nghiệm (34 trang) |

## 3. Năm chương luận án + phụ lục (`3_luan_an_chuong_phu_luc/`)

> Mỗi chương có **cả PDF (CTU XeLaTeX) lẫn docx (template CTU luận án)**, đúng chuẩn QĐ 1799/SH.

| File | Nội dung |
|---|---|
| `LUAN_AN_CTU_full.pdf` | **Luận án đầy đủ** đã biên dịch (154 trang, định dạng CTU) |
| `chuong_1_gioi_thieu_vi.pdf` / `.docx` | Chương 1 — Giới thiệu (9 tr) |
| `chuong_2_tong_quan_tai_lieu_vi.pdf` / `.docx` | Chương 2 — Tổng quan tài liệu (23 tr) |
| `chuong_3_phuong_phap_vi.pdf` / `.docx` | Chương 3 — Phương pháp (24 tr) |
| `chuong_4_ket_qua_vi.pdf` / `.docx` | Chương 4 — Kết quả (39 tr) |
| `chuong_5_ket_luan_de_xuat_vi.pdf` / `.docx` | Chương 5 — Kết luận & đề xuất (20 tr) |
| `00_phan_dau_vi.docx` | Phần đầu (bìa, mục lục, tóm tắt) |
| `04_references_apa7.docx` | Danh mục tài liệu tham khảo (APA 7) |
| `phu_luc_A_hop_nhat_du_lieu_vi.docx` | Phụ lục A — Hợp nhất dữ liệu |
| `phu_luc_B_maida_vi.docx` | Phụ lục B — Công cụ trích xuất M-AIDA & công bố dùng AI |
| `kappa_synthesis_en.pdf` / `.docx` | **Tổng luận tích hợp (kappa) tiếng Anh** — bản synthesis essay hợp nhất 8 nghiên cứu thành phần thành một luận điểm, chuẩn compilation-thesis quốc tế (kèm bảng golden-thread); luận án chính vẫn tiếng Việt theo CTU |

---

## 4. Việc còn lại — CHỈ NCS / máy có mạng + license làm được (không chặn đóng gói)

Các mục dưới đây **không thể chạy trong môi trường dựng bộ nộp** (container chặn outbound,
không có Stata license, nội dung cá nhân). Bộ nộp đã hoàn chỉnh về nội dung; đây là các bước
xác minh/điền cuối NCS thực hiện trước khi bấm nộp:

| # | Việc | Vì sao chỉ NCS làm được | Cách làm |
|---|------|--------------------------|----------|
| A2 | **Verify DOI** (~62 DOI cũ + 4 mục mới: Contractor–Kundu–Hsu 2003, Hitt 2006, Hunter–Schmidt 2004 [sách, không DOI — hợp lệ], Peng 2001) | Container trả HTTP 403 từ CrossRef | Chạy `python3 scripts/verify_dois.py` trên máy có mạng |
| A1 | **Cross-validation bằng Stata** (P3–P10) | Cần Stata license | Chạy lại `.do` trong `p*/replication/do/`; Python đã đối chiếu chéo P4–P10 ✅ (xem `reviews/REPLICATION_CROSSCHECK_2026-06-23.md`) |
| P3 | **Khóa reproducibility sóng 2009** (β₁ = 1,045) | Cần `.dta` build Stata gốc của NCS | Export `vietnam_2009_analytic.dta`; raw chính thức cho β₁ = 0,634, chênh do harmonize per-wave (đã chẩn đoán xong, xem `data_wbes/analysis/p3_paternoster_zflag_2026-06.md`) |
| P6 | **κ inter-coder** (Bảng 3.1 ICRV) + nhánh PRISMA Scopus | Cần dual-coding thật của 2 người mã hóa | Điền κ sau khi mã hóa độc lập |
| LA | **"Lời cảm ơn"** (`thesis/00_phan_dau_vi.md`) | Nội dung cá nhân | NCS viết, build lại bằng `scripts/build_bo_nop_package.sh` |

> Sau khi điền bất kỳ mục nào ở trên vào nguồn Markdown, **dựng lại toàn bộ bộ nộp** bằng:
> ```bash
> bash scripts/build_bo_nop_package.sh
> ```
> Script biên dịch lại PDF (XeLaTeX) + DOCX cho luận án, 5 chương, 2 chuyên đề và phụ lục,
> đồng bộ tự động về đúng khung canonical 50 nền.
