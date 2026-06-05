# M-AIDA System + SHTT Registration Dossier

**Hệ thống M-AIDA v7.0** *(Meta-Analysis Intelligent Data Assistant)* và **hồ sơ đăng ký bản quyền tác giả** kèm theo.

**Tác giả PI:** Đỗ Thùy Hương · **Đồng tác giả:** PGS.TS. Phan Anh Tú
**Đơn vị:** Trường Kinh tế, Trường Đại học Cần Thơ
**Cấp dữ liệu nguồn:** Web Bank Enterprise Surveys (WBES); P6 meta-analysis 238 studies (OSF z37kn)
**Trạng thái:** ✅ READY (NCS điền personal data trước nộp Cục Bản quyền)

---

## 📁 Cấu trúc

```
10_MAIDA_SHTT/
├── README.md                              ← File này
├── system/                                ⭐ HỆ THỐNG M-AIDA (artifact chính)
│   ├── MAIDA_intake.html                  → Web app single-file (23 KB)
│   ├── CITATION.cff                       → Citation metadata (zenodo-style)
│   └── README.md                          → Hướng dẫn dùng + technical doc
│
├── 00_mo_ta_tac_pham_vi.{md,docx}         → Mô tả tác phẩm (theo form Cục Bản quyền)
├── 01_source_code_samples.{md,docx}       → Mẫu source code đại diện
├── 02_checklist_nop_ho_so.md              → Checklist hồ sơ nộp
├── 03_huong_dan_toi_uu.md                 → Hướng dẫn tối ưu cho NCS
├── 04_phan_tich_chu_so_huu_va_ctu.{md,docx} → Phân tích chủ sở hữu (NCS vs CTU)
├── 05_evidence_quyet_dinh_CTU.{md,docx}   → Evidence các quyết định CTU
├── 06_cam_doan_nguon_luc_ca_nhan.{md,docx} → Cam đoan nguồn lực cá nhân (NCS)
└── evidence_ctu/                          → 3 quyết định CTU làm bằng chứng quyền sở hữu
    ├── 3010_qd_cong_nhan_ncs.md           → Công nhận NCS
    ├── 4768_qd_giao_chuyen_de.md          → Giao chuyên đề
    └── 4769_qd_dieu_chinh_ten_lats.md     → Điều chỉnh tên LATS
```

---

## ⚙️ Hệ thống M-AIDA v7.0 (`system/`)

### Phạm vi (scope statement — quan trọng)

> **M-AIDA là công cụ TRÍCH XUẤT tham số thống kê + QUY ĐỔI sang Pearson *r* / Fisher *z*; KHÔNG phải công cụ TÍNH TOÁN phân tích tổng hợp.**

| M-AIDA LÀM | M-AIDA KHÔNG LÀM |
|---|---|
| ✅ Đọc PDF → text (PDF.js) | ❌ Pooled effect size (random/fixed effects) |
| ✅ Trích xuất `N, r, t, F, β, df, p` từ văn bản học thuật | ❌ Heterogeneity statistics (`Q`, `τ²`, `I²`) |
| ✅ Quy đổi `t/β/F → r` theo Cohen (1988), Peterson & Brown (2005), Rosenthal (1994) | ❌ Forest plot, funnel plot |
| ✅ Fisher-z transform `z = ½·ln[(1+r)/(1−r)]` | ❌ Publication bias tests (Egger, trim-and-fill, Vevea-Hedges) |
| ✅ Human-in-the-loop PI verification + irreversible lock + audit trail | ❌ Moderator regression / meta-regression |
| ✅ Export CSV/JSON sẵn sàng nạp vào metafor (R) / CMA | ❌ Sensitivity analysis (leave-one-out, drop-frontier) |

Tính toán meta-analysis cho P6 (k=238) được thực hiện bằng **R `metafor` package** (random-effects REML estimator + Knapp-Hartung adjustment + Vevea-Hedges 3-parameter selection model + RVE), KHÔNG bằng M-AIDA. M-AIDA chỉ cung cấp **input dataset** cho pipeline R.

### Architecture

Single-file web app, client-side only, no server, no API key.

```
MAIDA_intake.html  (HTML5 + JavaScript ES2017+)
    ├── PDF.js 3.11 (CDN)         → readPdf: extract text from PDF
    ├── ruleExtract (offline)      → regex extract N, r, t(df), F(1,df2), β
    ├── aiExtract (window.claude)  → Claude artifact API (claude.ai)
    ├── conversion: t2r / beta2r / f2r / clampR / z (Fisher z)
    ├── renderCands / accept       → PI verify → LOCK (audit trail)
    └── exportCSV / JSON           → locked records only
```

**Quick start:** Mở `system/MAIDA_intake.html` trong trình duyệt bất kỳ. Không cần cài đặt, không cần server.

**Pipeline:**
1. Nạp PDF / .txt hoặc paste văn bản → textarea
2. **Trích xuất (AI)** dùng Claude trong artifact claude.ai (no API key) — ngoài claude.ai tự fallback sang **Trích xuất theo quy tắc** (offline regex)
3. Verify từng candidate (chỉnh N / df / r / p / measure)
4. **Kiểm chứng ✓** → LOCK record (audit trail)
5. **Kết xuất CSV / JSON** → chỉ verified-and-locked records

**Hierarchy chuyển đổi effect-size** (luận án §3.3.1):
1. `r` từ `t`: `r = √(t² / (t² + df))` (Cohen, 1988) — sign preserved
2. `r_partial` từ standardized `β`: `r = 0.98 × β` (Peterson & Brown, 2005)
3. `r` từ `F` (df₁ = 1): `r = √(F / (F + df₂))` (Rosenthal, 1994)

Tất cả `r` được Fisher-transform `z = ½·ln[(1+r)/(1−r)]`; bất kỳ `|r| ≥ 1` đều bị reject.

**Export schema (CSV):**
`study_id, effect_id, author, year, country, r, n, fisher_z, measure, moderator, p, source`

---

## 📜 Hồ sơ SHTT (`00`–`06` + `evidence_ctu/`)

Đây là bộ hồ sơ đăng ký **bản quyền tác giả** cho hệ thống M-AIDA tại **Cục Bản quyền tác giả, Bộ Văn hóa, Thể thao và Du lịch**.

### Bước nộp:
1. NCS điền personal data (CCCD, DOB, địa chỉ thường trú) vào các form `00_mo_ta_tac_pham_vi.docx` + `06_cam_doan_nguon_luc_ca_nhan.docx`
2. In + ký các form `00`, `01`, `06` + đính kèm `evidence_ctu/`
3. Nộp tại Cục Bản quyền (số 33 Ngọc Hà, Ba Đình, Hà Nội) hoặc nộp online qua https://cov.gov.vn

### Lưu ý chủ sở hữu (`04_phan_tich_chu_so_huu_va_ctu.docx`):
- **PI**: Đỗ Thùy Hương (đồng sở hữu 70%)
- **Đồng tác giả**: PGS.TS. Phan Anh Tú (đồng sở hữu 30%)
- **CTU**: KHÔNG đồng sở hữu (nguồn lực cá nhân, đã có cam đoan tại `06`)

### Trích dẫn (CITATION.cff):

```
Đỗ, T. H., & Phan, A. T. (2026). M-AIDA v7.0: Meta-Analysis Intelligent Data
Assistant [Computer software]. Can Tho University.
```

---

## 🔬 Quan hệ với portfolio

- **P6 meta-analysis** (Asia Pacific Journal of Management) dùng M-AIDA để extract 238 effect sizes từ ~150 PDFs
- **OSF preregistration z37kn** chỉ rõ "data extraction tool: M-AIDA v7.0"
- **Luận án §3.3.1** (Methodology) mô tả full conversion hierarchy
- **Supplement S** (`00_LUAN_AN/supporting/supplement_s_maida_vi.md`) là tài liệu kỹ thuật bổ trợ cho thesis defense
