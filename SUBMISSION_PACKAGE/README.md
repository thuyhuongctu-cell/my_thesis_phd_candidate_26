# SUBMISSION_PACKAGE — Bộ hồ sơ submission-ready

**Cập nhật:** 2026-06-05
**Tác giả:** NCS Đỗ Thùy Hương (P1323001) · NHD PGS.TS. Phan Anh Tú
**Đơn vị:** Trường Kinh tế, Trường Đại học Cần Thơ
**Branch:** `claude/vietnamese-academic-standards-QuiLM`
**Trạng thái:** ✅ **11/11 deliverables submission-ready** — đã pass blind compliance + APA7 cross-reference + numerical consistency + CTU QĐ 1799 format + lfe-academic-reviewer 2 vòng.

Thư mục này gom toàn bộ tài liệu đủ chuẩn nộp (papers, chuyên đề, luận án, M-AIDA) vào một nơi duy nhất ở repo root để tiện tra cứu trên GitHub. Bản đồng bộ với `dist/SUBMISSION_FINAL/` (build artifact) nhưng đã được dọn dẹp các file legacy pre-restructure.

---

## 📁 Cấu trúc thư mục

```
SUBMISSION_PACKAGE/
├── README.md                          ← File này (master index)
├── STATA_REPLICATION_GUIDE.md         ← Replication Stata + R cho cả portfolio
│
├── 00_LUAN_AN/                        → 5 chương luận án + tóm tắt + supporting
├── 01_CHUYEN_DE_1/                    → CĐ1 thực trạng FP (post 2-pass review)
├── 02_CHUYEN_DE_2/                    → CĐ2 mô hình NC (post 2-pass review)
│
├── 03_Paper_P3_Vietnam_JED/           → Journal of Economics and Development (Emerald, NEU)
├── 04_Paper_P4_Singapore_JABES/       → Journal of Asian Business and Economic Studies
├── 05_Paper_P5_China_IJOEM/           → International Journal of Emerging Markets
├── 06_Paper_P6_Meta_APJM/             → Asia Pacific Journal of Management
├── 07_Paper_P7_Capstone_JIBS/         → Journal of International Business Studies
├── 08_Paper_P8_SIDS_JED/              → Journal of Economics and Development
├── 09_Paper_P9_India_MIR/             → Management International Review (or IJOEM)
│
└── 10_MAIDA_SHTT/                     → Hệ thống M-AIDA v7.0 (artifact) + Hồ sơ SHTT
    ├── system/                        → MAIDA_intake.html (web app 23 KB) + CITATION.cff
    └── (00–06) + evidence_ctu/        → Hồ sơ đăng ký bản quyền tác giả
```

---

## 📋 Trạng thái 11 deliverables

### Luận án + 2 chuyên đề (CTU dossier)

| # | Folder | Loại | Trạng thái |
|---|---|---|:-:|
| 00 | `00_LUAN_AN/` | 5 chương luận án + tóm tắt + supporting | ✅ READY |
| 01 | `01_CHUYEN_DE_1/` | CĐ1 Thực trạng FP (26.302 từ, single-file) | ✅ READY |
| 02 | `02_CHUYEN_DE_2/` | CĐ2 Mô hình NC (6.916 từ, single-file) | ✅ READY |

### 7 papers quốc tế

| # | Folder | Tạp chí | Quartile | Words | Trạng thái |
|---|---|---|:-:|---:|:-:|
| 03 | `03_Paper_P3_Vietnam_JED` | Journal of Economics and Development (Emerald, NEU) | Q1 | 11.597 | ✅ READY |
| 04 | `04_Paper_P4_Singapore_JABES` | Journal of Asian Business and Economic Studies | Q1 | 12.096 | ✅ READY |
| 05 | `05_Paper_P5_China_IJOEM` | International Journal of Emerging Markets | Q1 | 7.331 | ✅ READY |
| 06 | `06_Paper_P6_Meta_APJM` | Asia Pacific Journal of Management (Springer) | Q1/ABS-3 | 11.167 | ✅ READY |
| 07 | `07_Paper_P7_Capstone_JIBS` | Journal of International Business Studies | ABS-4* | 13.140 | ✅ READY |
| 08 | `08_Paper_P8_SIDS_JED` | Journal of Economics and Development | Q1 | 8.683 | ✅ READY |
| 09 | `09_Paper_P9_India_MIR` | Management International Review (or IJOEM) | Q1 | 8.424 | ✅ READY |

### Hồ sơ M-AIDA SHTT

| # | Folder | Loại | Trạng thái |
|---|---|---|:-:|
| 10 | `10_MAIDA_SHTT/` | **Hệ thống M-AIDA v7.0** (`system/MAIDA_intake.html`) + hồ sơ đăng ký bản quyền | ✅ READY (cần personal data NCS điền local) |

---

## 🎯 Thứ tự nộp đề xuất

| Priority | Paper | Lý do |
|:-:|---|---|
| 1 | P5 China → IJOEM | Cleanest manuscript, fastest review (~4–6 tháng) |
| 2 | P9 India → MIR | Self-contained, novel UPI quasi-experiment |
| 3 | P3 Vietnam → JED | NEU partnership, local review nhanh |
| 4 | P8 SIDS → JED | Parallel submission JED (paper khác, cùng tạp chí) |
| 5 | P4 Singapore → JABES | Emerald portal (NCS quen) |
| 6 | P6 Meta → APJM | Springer EM portal + OSF z37kn preregistration |
| 7 | P7 Capstone → JIBS | Ambitious — leverage 6 paper trước đã accept |

---

## 📂 Mỗi paper folder chứa

| File | Mục đích | Submission slot |
|---|---|---|
| `01_manuscript_blinded.docx` | Bản blind cho reviewers | Main manuscript upload |
| `01_manuscript_blinded_vi.docx` *(nếu có)* | Bản tiếng Việt cho CTU dossier | KHÔNG upload journal |
| `02_title_page.docx` (+ `.md`) | Title page + author info + ORCID + CRediT | Separate "Title page" upload |
| `03_cover_letter.docx` (+ `.md`) | Cover letter journal-specific | Cover letter upload |
| `figures/` | Figures @ 300 DPI | Figure uploads (theo journal format) |
| `*_replication_data.xlsx` | Bảng dữ liệu replication kèm | Supplementary materials |
| `README.md` | Pre-submission checklist + format notes | Internal reference |

---

## ✅ Integrity verification (final state 2026-06-05)

| Check | Status | Commit |
|---|:-:|---|
| `check-consistency.py` — 0 numerical inconsistencies (67 files) | ✅ | `63ba590` |
| `format-apa7.py` — toàn bộ 7 papers tiếng Anh clean | ✅ | `9dd6d01` |
| Blind-DOCX scan — 0 author-identifier hits (9 patterns × 7 papers) | ✅ | `9dd6d01` |
| Humanizer pass — em-dash AI-tells removed | ✅ | `9dd6d01` |
| **CĐ1 + CĐ2 restructure** (Chương → §2.1–§2.4 per CTU QĐ 1799) | ✅ | `2e7f645` |
| **CĐ1 + CĐ2 review** — 7/7 blockers + 11/11 minor resolved | ✅ | `2b56800` + `63ba590` |
| **CĐ1 + CĐ2 et al.→ctv.** — VN narrative chuẩn CTU §1.2 | ✅ | `63ba590` |
| **CĐ1 APJM tag** — zero stale APJM citation (P3 retargeted JED) | ✅ | `63ba590` |
| **P5 IJOEM cleanup** — zero APJM residual trong P5 scope | ✅ | `0c823c9`, `58ee98b` |
| **CTU format** — template chuẩn QĐ 1799 (1.2 spacing, 14pt H1, TNR 13pt) | ✅ | `927b30c` |

---

## 🔬 Replication packages

- **Stata + R replication guide:** `STATA_REPLICATION_GUIDE.md` (ở thư mục này)
- **OSF Pre-registration (P6 meta-analysis):** https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN) · journal-agnostic
- **Per-paper replication code:** trong `../p[3-9]/replication/` (ở repo root, ngoài SUBMISSION_PACKAGE)
- **P8 R authoritative scripts:** `../p8/replication/do/01_p8_run_models_R.R` + `02_p8_robustness_R.R`

---

## 📝 Notes cho NCS

1. **Title pages** chứa author identity → upload **separately** từ blinded manuscript theo journal convention.
2. **Cover letters** cũng chứa author identity (signed by corresponding author).
3. **Vietnamese versions** (`*_vi.docx`) là cho CTU dossier / supervisor review — KHÔNG upload journal.
4. **Thesis chapters + chuyên đề** giữ author identity theo CTU dissertation regulations.
5. **M-AIDA hồ sơ** cần personal data (CCCD, DOB, etc.) — NCS điền local trước nộp Cục Bản quyền.
6. **OSF DOI z37kn** giữ nguyên cho mọi journal target.
7. **PR #12** trên GitHub là long-running finalization branch — sẵn sàng merge xuống main khi NCS quyết định.
8. Thư mục `SUBMISSION_PACKAGE/` này là **canonical view** cho NCS download/upload nhanh; `dist/SUBMISSION_FINAL/` là build artifact location (do scripts ghi vào, có thể chứa staging files).

---

## 📞 Liên hệ

- **Corresponding author:** PGS.TS. Phan Anh Tú · patu@ctu.edu.vn
- **First author:** Đỗ Thùy Hương · huongdt@vlute.edu.vn
- **OSF preregistration:** https://osf.io/z37kn (P6 meta-analysis)
- **GitHub repo:** `thuyhuongctu-cell/MY_THESIS_PHD_CANDIDATE_26`
- **PR #12:** https://github.com/thuyhuongctu-cell/MY_THESIS_PHD_CANDIDATE_26/pull/12

---

*Cập nhật cuối: 2026-06-05 sau 2-pass review cycle của lfe-academic-reviewer. Toàn bộ thay đổi nằm trong branch `claude/vietnamese-academic-standards-QuiLM`.*
