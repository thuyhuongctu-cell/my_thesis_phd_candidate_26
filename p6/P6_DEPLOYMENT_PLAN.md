# P6 Meta-Analysis — Hiện trạng và Kế hoạch Triển khai

**Ngày báo cáo**: 2026-05-21
**Branch P6 hiện tại**: `origin/claude/edit-vietnamese-academic-standards-xcAmn`
**Target journal**: International Business Review (IBR, Elsevier · Scopus Q1 · IF ~5.5 · ABS-3)
**Trạng thái tổng thể**: 🟡 **~65% hoàn thành** — Manuscript + pipeline sẵn sàng; còn extraction + MARA cuối cùng

---

## 1. Hiện trạng tài sản

### 1.1 Đã có (ready)

| Tài sản | Vị trí | Trạng thái |
|---|---|---|
| **Manuscript draft v1.0** | `p6/p6_meta_manuscript_en.md` | ✅ 14,466 từ EN; cấu trúc IBR sẵn sàng |
| **OSF pre-registration template** | `p6/osf/P6_OSF_Preregistration_Template.md` | ✅ Sẵn để pre-register trước final extraction |
| **PRISMA 2020 flow + checklist** | `p6/p6_prisma_flow.md`, `p6/p6_prisma_checklist.md` | ✅ Sẵn |
| **WoS search guide** | `p6/p6_wos_search_guide.md` | ✅ 28 queries trong `search_queries.json` |
| **5 figures (forest, funnel, sensitivity, DPL phase, conceptual)** | `p6/figures/figure{1-5}*.{png,pdf}` | ✅ Sẵn (generated từ sim data; cần regenerate sau MARA cuối) |
| **Vietnamese translation** | `p6/21_p6_meta_vi.md` | ✅ |
| **GitHub Actions pipeline** | `.github/workflows/{p6_full_search,wos_api,scopus_api,unpaywall,pdf_download_extract}.yml` | ✅ 8 workflows hoạt động |
| **Tools 01-45** (parse, screen, dedup, extract) | `p6/tools/*.py` | ✅ 50+ scripts hoàn chỉnh |
| **R MARA scripts** | `p6/scripts/p6_three_level_mara.R`, `p6_real_mara.R`, `run_mara.sh` | ✅ Sẵn |

### 1.2 Đang xử lý (in progress)

| Tài sản | Trạng thái | Còn lại |
|---|---|---|
| **L1 title screening** | 2,123 candidates → 332 Y / 248 N / **1,543 UNSURE** | 1,543 UNSURE cần đi sang L2 abstract screening |
| **L2 abstract screening** | 2,467 tracker rows, 0 blank | ✅ Done |
| **Extraction queue** | 652 Y papers cần PDF extraction | ~430 papers chưa extract |
| **PDF effect-size extraction** | 224/652 rows có `converted_r` (35%) | **428 papers cần extract effect size** |

### 1.3 Số liệu PROVISIONAL trong manuscript v1.0 (cần update sau extraction)

| Metric | Provisional (v1.0) | Source |
|---|---|---|
| k studies | **238** | Baseline (k=113 ICBEF 2025) + projected ~125 từ extraction queue |
| K effect sizes | **288** | k × ~1.2 effect sizes/study |
| Pooled r | **0.074** (CI [0.060, 0.088]) | Extrapolation từ ICBEF 2025 r=0.07 |
| I² | **62.4%** | Mock từ three-level decomposition |
| ICRV Q_M | **17.35** (p=.002) | Mock test |
| Begg–Mazumdar τ | **-0.134** (p=.0007) | Mock |
| Trim-and-fill imputed k | **58** | Mock |
| r_adj | **0.035** | Mock |

**⚠ Tất cả số trên là theoretical extrapolation — cần MARA thực với 652+ studies sau khi extraction xong.**

---

## 2. Kế hoạch triển khai 3 giai đoạn

### Giai đoạn 1 — Hoàn tất extraction (1-2 tuần)

**Mục tiêu**: Extract effect sizes từ 428 PDFs còn lại → tracker v3 đạt 652 rows có `converted_r`.

| # | Task | Owner | Tool | Time |
|---|---|---|---|---:|
| 1.1 | Download PDFs cho 428 papers còn lại (sau Unpaywall + S2 fallback) | GH Actions | `pdf_download_extract.yml` | 2-3 ngày (rate-limited) |
| 1.2 | Auto-extract via pdfplumber → pre-fill tracker | Local Python | `p6/tools/41_auto_extract_from_pdfs.py` | 1 ngày |
| 1.3 | Manual review + verify auto-extract (target precision ~85%) | NCS | Excel/CSV review | 3-4 ngày |
| 1.4 | Handle "extraction_status=PARTIAL/AMBIGUOUS" cases manually | NCS | `HOW_TO_EXTRACT_DATA.md` | 2-3 ngày |
| 1.5 | Compute inter-coder reliability κ trên 20% subsample | NCS + AsstNCS | `09_select_reliability_subsample.py` + κ formula | 2 ngày |
| 1.6 | Resolve UNSURE titles 1,543 → Y/N sau abstract screening | Auto + manual | `12_screen_l2_with_abstracts.py` | 2-3 ngày |

**Deliverable**: `p6/data/p6_study_database_FINAL.csv` với ~k=270-320 studies, K=320-380 effect sizes, tất cả 6 columns coding (icrv, cdai_country, dpl_phase, sample_size, converted_r, fisher_z, variance_z).

### Giai đoạn 2 — MARA + Sensitivity analysis (3-5 ngày)

**Mục tiêu**: Chạy three-level MARA + tất cả robustness checks → có FINAL numbers cho manuscript.

| # | Task | Tool | Time |
|---|---|---|---:|
| 2.1 | Pre-register protocol cập nhật trên OSF | `p6/osf/P6_OSF_Preregistration_Template.md` | 1 ngày |
| 2.2 | Run baseline three-level MARA (random-effects) | `p6/scripts/p6_three_level_mara.R` | 1h |
| 2.3 | Heterogeneity decomposition (Level 2 vs 3) | `metafor::rma.mv()` | 1h |
| 2.4 | Moderator tests: ICRV (5-regime), cDAI, DPL phase | `metafor::rma.mv(mods=~icrv+cdai+dpl)` | 2h |
| 2.5 | Publication bias: Egger, Begg, trim-and-fill, PET-PEESE | `metafor::regtest`, `ranktest`, `trimfill` | 2h |
| 2.6 | Sensitivity: outlier removal, leave-one-out, year subsamples | Custom R script | 1 ngày |
| 2.7 | Cross-check với ICBEF 2025 baseline (k=113) | Direct comparison | 0.5 ngày |
| 2.8 | Generate FINAL figures (forest, funnel, sensitivity, ICRV) | `p6/scripts/generate_p6_figures.py` | 1 ngày |

**Deliverable**: `p6/results/p6_final_mara_results.{json,csv,html}` + 5 figures cập nhật.

### Giai đoạn 3 — Manuscript finalize + submission (1 tuần)

**Mục tiêu**: Update manuscript v1.0 với FINAL numbers + nộp IBR.

| # | Task | Time |
|---|---|---:|
| 3.1 | Update `p6/p6_meta_manuscript_en.md` thay 8 placeholder numbers (k, K, r, I², Q_M, τ, r_adj, etc.) | 0.5 ngày |
| 3.2 | Update CD2 §2.4.3 Hướng 1 PENDING blockquote → final numbers | 30 min |
| 3.3 | Update Luận án 5 chương §4.2 (Chương 4 P6 section) | 1 ngày |
| 3.4 | Apply 3 skills (chinh-sua-van-ban-hoc-thuat-scopus-wos + humanizer + variable-formatter) | 1 ngày |
| 3.5 | Build IBR submission package (DOCX + PDF + TEX + cover letter) | 0.5 ngày |
| 3.6 | Final internal review (NCS + supervisor) | 2 ngày |
| 3.7 | Submit to IBR portal | 30 min |

**Deliverable**: `dist/final_packages/P6_Meta_IBR_YYYYMMDD.zip` + portal submission confirmation.

---

## 3. Critical dependencies & risks

### 3.1 Dependencies

```
Giai đoạn 1 (extraction) → Giai đoạn 2 (MARA) → Giai đoạn 3 (manuscript) → CD2 + Luận án final
```

Không thể skip GĐ1: số liệu MARA phải dựa trên thực data, không thể extrapolate.

### 3.2 Risk register

| Rủi ro | Mức độ | Mitigation |
|---|---|---|
| **PDFs không tìm được cho >30% papers** | 🟡 MEDIUM | (a) Unpaywall + S2 fallback đã có; (b) Manual library access cho 5% top studies; (c) Acceptable nếu coverage ≥70% với k_final ≥200 |
| **Q_M ICRV không sig khi extract đầy đủ** | 🟡 MEDIUM | Reframe: focus on heterogeneity decomposition (Level 2 vs 3) thay vì gradient claim |
| **cDAI / DPL không sig** | 🟢 LOW | Manuscript v1.0 đã thừa nhận "limited support" — không cần restructure |
| **Publication bias mạnh (τ very negative)** | 🟢 LOW | Trim-and-fill + PET-PEESE đã được pre-registered; mainstream meta-analysis practice |
| **Inter-coder κ < 0.70** | 🟡 MEDIUM | Re-train coders + re-extract problem rows; pre-registered as exclusion criterion |
| **Reviewer demand pre-registration trước submit** | 🟢 LOW | OSF template sẵn; chỉ cần update + submit OSF trước IBR |

---

## 4. Timeline tổng thể

```
Tuần 1-2: GĐ1 — Complete extraction (652 papers → tracker v4 final)
Tuần 3:   GĐ2 — Run MARA + sensitivity + figures
Tuần 4:   GĐ3 — Manuscript update + CD2/Luận án sync + IBR submit

Total:    4 tuần từ start
```

### Parallel tasks có thể làm song song

- GĐ1 step 1.5 (κ subsample) song song với 1.6 (UNSURE resolution)
- GĐ2 step 2.7 (cross-check ICBEF) song song với 2.8 (figures)
- GĐ3 step 3.2 (CD2 update) + 3.3 (Luận án update) sau khi 3.1 xong

---

## 5. Resource needs

| Tài nguyên | Yêu cầu |
|---|---|
| Compute | GitHub Actions free tier (60-100 min/tháng đủ); local Python + R |
| API keys | WoS Starter ✅, Scopus Elsevier ✅, OpenAlex ✅, Unpaywall (free) ✅ — **cần rotate sau security audit** |
| Storage | ~2 GB cho 652 PDFs; OSF account cho pre-registration (free) |
| Software | R 4.x + metafor + clubSandwich; Python 3.11 + pdfplumber + pandas |
| Human | NCS Đỗ Thúy Hương (primary coder); 1 AsstNCS cho 20% double-coding (κ check) |

---

## 6. Success metrics

| Metric | Mục tiêu | Min acceptable |
|---|---:|---:|
| k final studies | ≥250 | ≥200 |
| K effect sizes | ≥300 | ≥250 |
| Inter-coder κ | ≥0.80 | ≥0.70 |
| Country coverage | ≥45 economies | ≥35 |
| ICRV 5-regime coverage | Tất cả 5 nhóm có k≥5 | ≥3 nhóm có k≥10 |
| Manuscript word count | 7,000-10,000 (IBR limit) | <12,000 |
| Pre-registration | Done trước MARA | Done sau MARA (acceptable nếu OSF accept) |

---

## 7. Khi nào CD2 + Luận án được update?

CD2 §2.4.3 Hướng 1 + Luận án Chương 4 §4.2 đều có PENDING markers chờ P6 final numbers.

**Sequence**:
```
GĐ2 complete → final MARA results table có
GĐ3.1 update P6 manuscript với final numbers
GĐ3.2 update CD2 §2.4.3 (30 min, surgical edit)
GĐ3.3 update Luận án §4.2 (1 ngày, có thể có ripple đến Chương 5 conclusion)
Rebuild CD2 + Luận án packages
Refresh dist/final_packages/{CD2,LuanAn_5Chuong}_YYYYMMDD.zip
```

---

## 8. Đề xuất action ngay (24h tiếp theo)

1. **Pre-registration OSF** — submit hôm nay trước khi extract → defendable scientific practice
2. **Trigger pipeline PDF download** — start `pdf_download_extract.yml` cho ~430 papers còn lại
3. **Rotate 3 API keys** (PR #9 dependency) — Clarivate / Elsevier / OpenAlex
4. **Confirm timeline với supervisor** — 4 tuần có khớp với deadline hội đồng / IBR submission window không

Sau 24h, có thể commit GĐ1 task 1.1-1.2 (PDFs + auto-extract) chạy parallel với 1.6 (UNSURE resolution).
