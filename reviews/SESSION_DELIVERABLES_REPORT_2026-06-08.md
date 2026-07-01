# Báo cáo chi tiết — Các tài liệu đã triển khai

**Nhánh:** `claude/phd-thesis-review-L9Gml` · **PR:** #17 (draft) · **Ngày:** 2026-06-08
**Phạm vi phiên:** 15 commit (`5cc13b4` đến `9c80bf8`); **95 file thay đổi** (+2.091 / −4.192 dòng — giảm ròng do cô đọng).
**Mục tiêu:** chuẩn hoá 6 hồ sơ nộp tạp chí (P3–P8), rà soát liêm chính & nhất quán toàn dự án, hoàn thiện nội dung chưa đạt.

---

## 1. Liêm chính học thuật (Integrity)

| Hạng mục | Việc đã làm | File |
|---|---|---|
| **Khai báo AI — chuyên đề** | Gỡ đoạn khai báo AI/Grammarly bị chèn nhầm ở bản dist CĐ1/CĐ2 (bản gốc & file nộp vốn không có) — đúng chuẩn ĐHCT | `dist/chuyen_de_1/source_md/00_cd1,cd2…md` |
| **Khai báo AI — luận án** | Đối chiếu *Hướng dẫn trình bày LATS ĐHCT* (63 tr.): chuẩn dùng **Lời cam đoan**, không có mục khai báo AI dẫn đến gỡ mục AI, giữ Lời cam đoan | `thesis/00_phan_dau_vi.md`, `dist/luan_an_ctu/…` |
| **Tự‑trích‑dẫn/kết hợp công trình** | Bổ sung khai báo: luận án phát triển từ **2 chuyên đề của chính NCS** (Quyết định giao chuyên đề) đến trùng lặp hợp lệ, không phải đạo văn | `thesis/00_phan_dau_vi.md` (Lời cam đoan) |
| **Khai báo AI — P6 (NGHIÊM TRỌNG)** | Bằng chứng (extractor dùng Claude + log auto-extract) dẫn đến sửa câu sai "extracted manually / no GenAI" thành **khai báo M‑AIDA (LLM) có PI kiểm chứng 100% + khóa dữ liệu** ở cả 4 package | `p6/submission/{jim,ibr,jwb,apjm}/01_manuscript_blinded.md` |
| **OSF — sửa tuyên bố sai** | Bỏ "OSF pre-registration *preceded* extraction / registered *prior to database access*" đến **transparency registration** (corpus đã thu thập), chèn `[insert OSF DOI]` | 4 package P6 |
| Báo cáo compliance | Cập nhật `LIEM_CHINH_KHOA_HOC_compliance.md` (Đ.2.3, Đ.16, Đ.18) | `reviews/LIEM_CHINH_KHOA_HOC_compliance.md` |

## 2. Reviewer audit & nhất quán số liệu xuyên tài liệu

| Phát hiện | Kết quả | File |
|---|---|---|
| **P6 cỡ mẫu lệch** (237/287 vs 238/288) | Đối chiếu dữ liệu gốc (`p6_study_database.csv`=288 effects/238 study; workbook "r=0.074") đến chuẩn hoá toàn repo về **k=238/K=288** | JIM+APJM manuscripts, cover letter, README |
| 47 vs 49 nền KT; 91.982/101.185/102.332 DN | Xác nhận **phân biệt hợp lệ** (WBES final vs pool vs CD-era) — không lỗi | `reviews/REVIEWER_AUDIT_2026-06.md` |
| Hình ảnh 6 package | Đủ file; P7/P8 cố ý chỉ bảng | audit |
| Báo cáo phản biện đa góc | 6 mục (A–F): lỗi đã sửa, việc NCS phải làm, mối lo khoa học từng paper | `reviews/REVIEWER_AUDIT_2026-06.md` |

## 3. P8 — Tái phân tích về 7 Pacific SIDS (validated)

| Việc | Chi tiết |
|---|---|
| **Cơ sở** | Loại **Comoros** (Ấn Độ Dương) + **Timor-Leste** (ĐNÁ) đến 7 đảo nhỏ TBD thật, khớp định nghĩa chuyên đề (không theo p-value) |
| **Phương pháp** | Chạy **chính pipeline R của tác giả** với bộ lọc 2 nước; **validated** tái tạo bản 9 nước *chính xác* (M1 β=−0.4038) |
| **Kết quả** | FIP mạnh hơn: M1 β=**−1.339, p<.001**; TCI nay có ý nghĩa (+0.299, p=.003); N=959 |
| **Viết lại** | 3 package P8 (jid/world_development/ejdr): abstract, mẫu, **Table 1/2/3**, mọi hệ số in-text; khung lại trung thực (bivariate/exporters yếu đến dựa FE) |
| **Đồng bộ** | Abstract luận án + positioning (chín đến bảy); footnote "dữ liệu cập nhật" ở CĐ1 |
| **Lưu** | Script + CSV kết quả 7 nước | `p8/replication/reanalysis_7pacific/` (5 file) |

## 4. Chuẩn hoá 6 hồ sơ nộp đầu (P3 đến JED, P4 đến MBR, P5 đến IJOEM, P6 đến JIM, P7 đến IBR, P8 đến JID)

| Việc | Chi tiết |
|---|---|
| **Abstract theo NXB** | Emerald (JED/MBR/IJOEM) đến **cấu trúc** Purpose/Design/Findings/Originality; Elsevier (JIM/IBR) + Wiley (JID) đến **1 đoạn** |
| **Cover letter — sửa lệch dữ liệu** | P5: bản cũ 4 đợt (2003–2024) đến **2 đợt (2012/2024)** khớp manuscript; P6: 288/238 |
| **Em dash** | Gỡ sạch (0) toàn bộ 6 package (manuscript, cover, title, tables, supplementary, README) |
| **README** | Đồng bộ tiêu đề/số từ/checklist (vd P5 tiêu đề sai, P7 "structured" đến 1 đoạn) |
| **Harvard (Emerald)** | `, &` đến `, and` trong TLTK; `&` đến `and` trong trích dẫn có năm (giữ "&" tên tạp chí/R&D) — JED/MBR×2/CMS/IJOEM |

## 5. Cô đọng độ dài (đạt trần tạp chí)

| Paper | Trước đến Sau | Giữ nguyên |
|---|---|---|
| **P6/APJM** | 13.467 đến **8.351 từ** (≤10k); Phụ lục A–C đến supplement | Results/Discussion/References |
| **P4/MBR** | 12.704 đến **10.616 từ** (main ~9.100) | Mọi hệ số, bảng M0–M8, H1–H3 |

## 6. Hoàn thiện P6 cho nộp tạp chí

| Tài liệu | Nội dung |
|---|---|
| **Checklist sẵn sàng** | 6 mục: tìm kiếm PRISMA chính thức, ICR (κ/ICC), đăng ký OSF, khai báo AI, tái định khung đóng góp, items chuẩn | `p6/P6_SUBMISSION_READINESS_CHECKLIST.md` |
| **OSF pre-registration** | Soạn lại hoàn chỉnh, khớp manuscript: ICRV 5-regime, DPL Paradox (Precede/Span/Follow), H1–H4, k=238/K=288, transparency registration + hướng dẫn đăng ký | `p6/osf/P6_OSF_Preregistration_Template.md` (+ `.docx`) |

## 7. Tích hợp tài liệu & trích dẫn

| Việc | Chi tiết | File |
|---|---|---|
| **Tự‑trích‑dẫn P7 Mục 2.5** | Thêm **Phan, Đỗ & Phan (2020)** — bài của nhóm về kinh nghiệm/giới tính nhà quản trị điều tiết I–P (củng cố H4 + Đ.2.3) + **Nielsen (2010)** | P7 ibr/apjm/jibs |
| Luận án Mục 2.5.5 | Thêm Phan (2020) vào H4 + nạp 2 reference vào danh mục | `thesis/chuong_2…`, `thesis/04_references_apa7.md` |
| **Bản đồ tích hợp** | Map 6 nguồn học thuật + báo cáo kinh tế (IMF Asia-Pacific, WB China/Indonesia/Mekong, Schulze meta…) đến section đích, reference sẵn dán | `reviews/INTEGRATION_ATTACHED_SOURCES.md` |

## 8. Công cụ M‑AIDA (chứng minh năng lực + bản quyền)

| Việc | File |
|---|---|
| `.gitignore` chặn `.env` (không có key thật bị lộ) | `p6/tools/maida/.gitignore` |
| Ghi chú tác giả + vai trò AI (human-in-the-loop) + bản quyền COV | `p6/tools/maida/README.md` |
| Sửa nhãn lỗi thời `cdai_score`: "Cultural Distance" đến "country Digital Adoption Index 0–1" | `p6/tools/maida/backend/extractor.py` |

---

## Tài liệu MỚI tạo trong phiên
- `reviews/REVIEWER_AUDIT_2026-06.md` — báo cáo phản biện toàn dự án
- `reviews/INTEGRATION_ATTACHED_SOURCES.md` — bản đồ tích hợp tài liệu đính kèm
- `p6/P6_SUBMISSION_READINESS_CHECKLIST.md` — checklist nộp P6
- `p6/osf/P6_OSF_Preregistration_Template.md` (viết lại) + `P6_OSF_Preregistration.docx`
- `p6/submission/apjm_package/supplementary_material.md` — Phụ lục A–C tách ra
- `p8/replication/reanalysis_7pacific/` — 5 file (script R/Python + CSV kết quả 7 nước)
- `p6/tools/maida/.gitignore`

## Việc còn lại — chỉ NCS làm được (không thể tự động / không bịa)
1. **P6:** chạy tìm kiếm WoS/Scopus chính thức (server không truy cập) đến điền 29 `[TBD]` PRISMA.
2. **P6:** ICR — cần **coder thứ hai** mã hoá 20% mẫu đến tính κ/ICC.
3. **OSF:** đăng ký thật đến lấy DOI đến dán vào 4 manuscript + file OSF.
4. **Kiểm tra trùng lặp ĐHCT** trước nộp.
5. **Xác nhận 1 dòng** phạm vi dùng MAIDA (giữ wording hiện tại hoặc biến thể (b)).
6. (Tuỳ chọn) Đặt các trích dẫn Schulze/Lundan/Park vào P6/P5 theo bản đồ tích hợp.

## Nhật ký commit (phiên này)
```
9c80bf8 fix(P6 integrity): correct false OSF pre-registration claims → transparency registration
ac1fe56 docs(P6/OSF): rewrite pre-registration aligned to final manuscript
fe3e8aa feat: propagate managerial-moderator citations; align MAIDA/OSF
72a1e3b feat(P7)+docs: cite Phan et al. 2020 + Nielsen 2010; integration map
8950a5e fix(P6 integrity)+docs: AI-use disclosure (M-AIDA), harden tool, submission checklist
cd599f3 refactor(P8): re-scope to 7 Pacific SIDS; full re-analysis
0b288f3 analysis(P8): validated 7-Pacific re-analysis script + coefs
d84de3e fix(P6)+audit: correct meta sample to k=238/K=288; add reviewer audit
4333839 refactor(P4/MBR): condense ~12,700 → ~10,600 words
f8091ef chore: strip em-dashes across 6 packages; sync READMEs
00fd404 feat: 6 first-target abstracts publisher-compliant + fix cover-letter drift
9b7d321 docs(integrity): dissertation built from candidate's own chuyên đề
415db2f fix(luan-an): align AI declaration with CTU LATS regulation
30ebdda fix(chuyen-de): remove orphan AI declaration from CD1/CD2
5cc13b4 feat(A+B): condense P6/APJM ≤10k; apply Emerald Harvard markers
```
