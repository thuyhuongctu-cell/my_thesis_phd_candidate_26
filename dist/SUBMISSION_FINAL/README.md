# SUBMISSION_FINAL — Portfolio Hoàn Chỉnh 7 Bài Báo + Hồ Sơ Luận Án

**Cập nhật:** 2026-06-03 (session-final state)
**Tác giả:** Đỗ Thùy Hương (NCS, mã số P1323001) · PGS.TS. Phan Anh Tú
**Đơn vị:** Trường Kinh tế, Trường Đại học Cần Thơ (CTU)
**Branch:** `claude/vietnamese-academic-standards-QuiLM`
**Trạng thái:** ✅ **7/7 papers submission-ready** — đã pass toàn bộ kiểm định blind compliance + APA7 cross-reference + numerical consistency.

---

## 📦 Cấu trúc thư mục

```
dist/SUBMISSION_FINAL/
├── README.md                     ← Master index (file này)
├── STATA_REPLICATION_GUIDE.md    ← Hướng dẫn replication Stata + R cho cả portfolio
│
├── P3_Vietnam_JED/               → Journal of Economics and Development (Emerald, NEU)
├── P4_Singapore_JABES/           → Journal of Asian Business and Economic Studies (Emerald, UEH)
├── P5_China_IJOEM/               → International Journal of Emerging Markets (Emerald)
├── P6_Meta_APJM/                 → Asia Pacific Journal of Management (Springer Nature) ★ NEW retarget
├── P7_Capstone_JIBS/             → Journal of International Business Studies (Wiley/Palgrave Macmillan)
├── P8_SIDS_JED/                  → Journal of Economics and Development (Emerald, NEU)
├── P9_India_MIR/                 → Management International Review (Springer) hoặc IJOEM
│
├── CD1_ChuyenDe_1/               → Chuyên đề Tiến sĩ số 1
├── CD2_ChuyenDe_2/               → Chuyên đề Tiến sĩ số 2
│
├── Thesis_LuanAn/                → 5 chương luận án
│   ├── chuong_1_gioi_thieu.docx
│   ├── chuong_2_tong_quan_tai_lieu.docx
│   ├── chuong_3_phuong_phap.docx
│   ├── chuong_4_ket_qua.docx
│   └── chuong_5_ket_luan_de_xuat.docx
│
└── M-AIDA_SHTT_Registration/     → Hồ sơ đăng ký bản quyền M-AIDA (NCS-side, cần personal data)
```

---

## 📋 Trạng thái từng paper

| # | Folder | Tạp chí | Quartile | Word count | Status |
|---|---|---|:-:|---:|:-:|
| 1 | **P3_Vietnam_JED** | Journal of Economics and Development (Emerald, NEU) | Q1 | 11,597 | ✅ READY |
| 2 | **P4_Singapore_JABES** | Journal of Asian Business and Economic Studies (Emerald, UEH) | Q1 | 12,096 | ✅ READY |
| 3 | **P5_China_IJOEM** | International Journal of Emerging Markets (Emerald) | Q1 | 7,331 | ✅ READY |
| 4 | **P6_Meta_APJM** | Asia Pacific Journal of Management (Springer Nature) | Q1 ABS-3 | 11,167 | ✅ READY ★ |
| 5 | **P7_Capstone_JIBS** | Journal of International Business Studies | ABS-4* | 13,140 | ✅ READY |
| 6 | **P8_SIDS_JED** | Journal of Economics and Development (Emerald, NEU) | Q1 | 8,683 | ✅ READY |
| 7 | **P9_India_MIR** | Management International Review (Springer) hoặc IJOEM | Q1 | 8,424 | ✅ READY |

★ P6 retargeted từ MIR → APJM trong commit `1061efa` per stronger geographic + theoretical fit; CIMT (Capability-Institution Mismatch) là central theoretical contribution của cả P6 (meta-test) và P7 (firm-level multi-country test).

---

## 🎯 Thứ tự nộp đề xuất

| Priority | Paper | Lý do |
|:-:|---|---|
| 1 | P5 China → IJOEM | Cleanest manuscript, fastest review (~4-6 months) |
| 2 | P9' India → MIR (or IJOEM alt) | Self-contained, novel UPI quasi-experiment |
| 3 | P3 Vietnam → JED | NEU partnership, faster local review |
| 4 | P8 SIDS → JED | Parallel submission to JED (different paper, same journal); 4 robustness panels resolved (Comoros + WCB + LOO + attrition) |
| 5 | P4 Singapore → JABES | Emerald portal (NCS familiar) |
| 6 | P6 Meta → APJM | Springer EM portal; CIMT theoretical contribution + OSF z37kn pre-registration |
| 7 | P7 Capstone → JIBS | Most ambitious — leverage other submissions' acceptance signals |

---

## 📂 Mỗi paper folder chứa

| File | Mục đích | Submission slot |
|---|---|---|
| `01_manuscript_blinded.docx` | Bản blind cho reviewers | Main manuscript upload |
| `01_manuscript_blinded_vi.docx` *(nếu có)* | Bản tiếng Việt cho CTU dossier | KHÔNG upload journal |
| `02_title_page.docx` (+ `.md`) | Title page + author info + ORCID + CRediT | Separate "Title page" upload |
| `03_cover_letter.docx` (+ `.md`) | Cover letter tạp chí-specific | Cover letter upload |
| `figures/` | Figures @ 300 DPI | Figure uploads (theo journal format) |
| `README.md` | Pre-submission checklist + format notes | Internal reference |

---

## ✅ Integrity verification (session-final 2026-06-03)

| Check | Status | Commit |
|---|:-:|---|
| `scripts/check-consistency.py` — 0 numerical inconsistencies across 60 files | ✅ | `9dd6d01` |
| `scripts/format-apa7.py` — all 7 English papers clean | ✅ | `9dd6d01` |
| Blind-DOCX scan — 0 author-identifier hits across 9 patterns × 7 papers | ✅ | `9dd6d01` |
| Em-dash AI-tells removed (humanizer pass) | ✅ | `9dd6d01` |
| P8 robustness backed by authoritative R analysis (commit 9dd6d01) | ✅ | `9dd6d01` |

**Patterns checked:** `thuyhuongctu`, `huongctu`, `Do Thuy Huong`, `Đỗ Thùy`, `Phan Anh Tú`, `Phan Anh Tu`, `patu@ctu`, `Can Tho University`, `VLUTE`, `huongdt@vlute`.

---

## 🔬 Replication packages

- **Stata + R replication guide**: `STATA_REPLICATION_GUIDE.md` ở thư mục này
- **OSF Pre-registration (P6 meta-analysis)**: https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN); journal-agnostic, dùng cho cả MIR/APJM/MBR/MRQ exploration
- **Per-paper replication code**: trong từng `../../p[3-9]/replication/` directory ở repo root
- **P8 R authoritative scripts**:
  - `p8/replication/do/01_p8_run_models_R.R` (baseline M0–M3 models)
  - `p8/replication/do/02_p8_robustness_R.R` (Comoros + WCB + LOO + attrition; commit `9dd6d01`)
- **P8 Stata `.do` companions** (cho NCS local Stata verification):
  - `p8/replication/do/02_p8_comoros_excluded.do`
  - `p8/replication/do/03_p8_wild_cluster_bootstrap.do`
  - `p8/replication/do/04_p8_loo_and_attrition.do`

---

## 📝 Notes cho NCS

1. **Title pages** chứa author identity và uploaded **separately** từ blinded manuscript theo journal convention
2. **Cover letters** cũng chứa author identity (signed by corresponding author)
3. **Vietnamese versions** (`*_vi.docx`) là cho CTU dossier / supervisor review — KHÔNG upload journal
4. **Thesis chapters + chuyên đề** giữ author identity theo CTU dissertation regulations
5. **M-AIDA hồ sơ** cần personal data (CCCD, DOB, etc.) — NCS điền local
6. **OSF DOI z37kn** giữ nguyên cho mọi journal target (preregistration body là journal-agnostic)
7. **PR #12** trên GitHub là long-running finalization branch — khi sẵn sàng có thể merge xuống main

---

## 📞 Liên hệ

- **Corresponding author:** PGS.TS. Phan Anh Tú · patu@ctu.edu.vn
- **First author:** Đỗ Thùy Hương · thuyhuongctu@gmail.com
- **OSF preregistration:** https://osf.io/z37kn (P6 meta-analysis)
- **GitHub repo:** `thuyhuongctu-cell/MY_THESIS_PHD_CANDIDATE_26`
- **PR #12** (long-running finalization): https://github.com/thuyhuongctu-cell/MY_THESIS_PHD_CANDIDATE_26/pull/12

---

*Tự động cập nhật cuối session 2026-06-03. Toàn bộ thay đổi nằm trong branch `claude/vietnamese-academic-standards-QuiLM`. Khi NCS sẵn sàng nộp, có thể download folder này về local hoặc clone branch trực tiếp.*
