# Gold-Standard Evaluation & OSF Deposit Plan (z37kn)

**Mục tiêu:** Hoàn thành 2 việc bắt buộc trước defense / submission MIR:
1. Đánh giá chất lượng quy trình trích xuất LLM (điền `[TO FILL]` trong `thesis/supplement_s_maida_vi.md` §S-MAIDA.4 và §S-MAIDA.5).
2. Upload package validation + reproducibility lên OSF project z37kn.

**Tổng effort dự kiến:** 15–25 giờ (1 tuần làm part-time) — chi tiết theo phase bên dưới.

---

## Phase 1: Sample selection (✅ ĐÃ XONG, ~1 phút)

```bash
python3 p6/gold_standard/01_select_sample.py
```

Kết quả: `p6/gold_standard/gold_standard_sample.csv` — 32 effect-rows / 30 nghiên cứu duy nhất, stratified random theo ICRV (seed=42, tái lập được).

Phân bố mẫu:
- ICRV: I=12 / II=5 / III=9 / FR=3 (census) / MX=3
- DPL: PRE=11 / SPN=15 / FOL=6
- DOI: FSTS=16 / EXP=8 / COMP=4 / GEO=4
- FP: ACC=26 / MIX=4 / LAB=1 / MKT=1

---

## Phase 2: Manual extraction (👤 BẠN PHẢI LÀM, ~12–20 giờ)

### Bước 2.1: Chuẩn bị
```bash
cp p6/gold_standard/gold_standard_manual_template.csv \
   p6/gold_standard/gold_standard_manual_filled.csv
```

Mở `gold_standard_manual_filled.csv` (Excel hoặc text editor).

### Bước 2.2: Trích xuất thủ công 30 nghiên cứu

Với mỗi dòng (đã pre-fill `study_id`, `effect_id`, `author`, `year`):
1. **Tìm PDF** của nghiên cứu (DOI lookup, library, Google Scholar)
2. **Đọc methods + results section** để xác định:
   - `manual_r`: hệ số tương quan focal I-P (đã chuyển đổi nếu paper báo cáo $\beta$/$t$/$F$)
   - `manual_n`: cỡ mẫu của ước lượng focal
   - `manual_country`: ISO-3 (multi-country = "pooled")
   - `manual_sample_start` / `manual_sample_end`: năm dữ liệu min/max
   - `manual_icrv`: I/II/III/FR/SIDS/MX theo bảng WGI 2023
   - `manual_dpl`: PRE (median year ≤ 2008) / SPN (2009–2013) / FOL (≥ 2014)
   - `manual_doi_type`: FSTS / GEO / EXP / COMP / FDI / OTH
   - `manual_fp_type`: ACC / MKT / LAB / MIX
   - `manual_notes`: bất kỳ ghi chú nào (ví dụ paper báo cáo nhiều specs; chọn spec đầy đủ kiểm soát nhất)

> **⚠️ Quan trọng:** Trích xuất "mù" — KHÔNG nhìn vào `gold_standard_sample.csv` trong khi điền. Chỉ nhìn PDF nguồn. Đây là điều kiện cần để Cohen's $\kappa$ có giá trị scientific.

> **💡 Tip thực tế:**
> - Effort trung bình: 30–40 phút/paper với HITL workflow đã quen; 40–60 phút/paper nếu thủ công từ đầu.
> - Chia 5 ngày × 6 papers/ngày = ~4 giờ/ngày trong 1 tuần.
> - Nếu có 1 colleague làm phần subset, làm thêm inter-coder reliability check cho ICRV/DOI/FP — Phase 4 optional bên dưới.

### Bước 2.3: Validation lỗi cơ học
Trước khi chạy metrics, đảm bảo:
- [ ] Mọi `manual_r` đều có giá trị numeric trong khoảng (−1, +1)
- [ ] Mọi `manual_n` đều là số nguyên dương
- [ ] `manual_icrv`/`manual_dpl`/`manual_doi_type`/`manual_fp_type` đều thuộc bảng codes
- [ ] 32/32 rows đã điền (không có blank)

---

## Phase 3: Compute metrics (✅ TỰ ĐỘNG, ~1 phút)

```bash
python3 p6/gold_standard/02_compute_metrics.py
```

Kết quả:
- `p6/gold_standard/validation_report.json` (machine-readable)
- `p6/gold_standard/validation_report.md` (human-readable, dùng để paste vào Supp-S-MAIDA §S-MAIDA.4)

Metrics tính:
| Quantity | Metric | Pre-registered threshold |
|---|---|---|
| `r` | % within $\|\Delta\| \leq 0.005$ + mean/max $\|\Delta\|$ | $\geq$ 90% |
| `N` | % exact | $\geq$ 90% |
| `year` | % exact | $\geq$ 90% |
| `icrv` / `dpl` / `doi_type` / `fp_type` / `country` | Cohen's $\kappa$ + % agreement | $\kappa \geq$ 0.70 |

### Diễn giải kết quả

**Nếu PASS toàn bộ:** Quy trình đạt ngưỡng tiền đăng ký. Paste `validation_report.md` content vào §S-MAIDA.4 (thay `[TO FILL]`). Workflow validated; primary analysis được sử dụng nguyên trạng.

**Nếu FAIL ở 1+ quantity:** Theo tiền đăng ký, đại lượng dưới ngưỡng phải **trích xuất hoàn toàn thủ công** cho toàn corpus (k=238/K=288). Ví dụ nếu Cohen's $\kappa$ cho `doi_type` = 0.55 < 0.70 → trích xuất lại `doi_type` cho toàn corpus, các đại lượng khác giữ nguyên. Thay đổi phải re-run MARA và update results.

---

## Phase 4 (optional): Inter-coder reliability check (⏱ +4–6 giờ)

Nếu có colleague hoặc supervisor sẵn sàng:

```bash
cp p6/gold_standard/gold_standard_manual_template.csv \
   p6/gold_standard/gold_standard_coder2_filled.csv
```

Coder thứ 2 điền độc lập (không xem `gold_standard_manual_filled.csv`). Sau đó modify `02_compute_metrics.py` để so coder1 vs coder2 (inter-coder reliability) thay vì manual vs system. Báo cáo cả hai số trong §S-MAIDA.4: (a) system-vs-manual, (b) coder1-vs-coder2.

**Khuyến nghị:** Có inter-coder reliability sẽ giải quyết Limitation 5 trong §5.4 (currently single-coder design). Reviewer Q1 sẽ khen.

---

## Phase 5: OSF z37kn deposit (✅ TỰ ĐỘNG kê manifest, ~30 phút upload thủ công)

### Bước 5.1: Truy cập OSF z37kn
URL: https://osf.io/z37kn

Đăng nhập với account của bạn (Phan Anh Tú hoặc Đỗ Thị Thúy Hương — bất kỳ ai là project administrator).

### Bước 5.2: Tạo folder structure trên OSF

```
z37kn/
├── 01_manuscript/
│   ├── p6_meta_manuscript_en_v1.2.pdf       (MIR EN, blinded, with Figure 7)
│   ├── p6_meta_manuscript_vi_v1.2.pdf       (VI version)
│   └── README_manuscript.md                  (version log; current = v1.2 MIR-target)
├── 02_data/
│   ├── p6_study_database.csv                 (k=238 / K=288 analyzed corpus)
│   ├── p6_study_database_codebook.md         (schema + coding rules)
│   └── fulltext_to_extraction_tracker_v3.csv (full Path-B screening tracker, 2510 rows)
├── 03_code/
│   ├── meta_analysis_R/                      (metafor scripts)
│   ├── verify_moderator_qm.py                (Python cross-check)
│   └── README_replication.md
├── 04_supplementary/
│   ├── osf_supplementary_materials.md        (Supp-A through Supp-T6)
│   ├── prisma_extraction_pipeline_status.md  (Path B status report)
│   ├── prisma_status_report.json             (machine-readable)
│   ├── figure_prisma_2020_flow.png           (Figure 7)
│   └── supplement_s_maida_vi.md              (S-MAIDA, filled-in version)
├── 05_validation/
│   ├── gold_standard_sample.csv              (32 stratified-random sample rows)
│   ├── gold_standard_manual_filled.csv       (your manual extractions)
│   ├── validation_report.md                  (Cohen kappa + % agreement)
│   ├── validation_report.json
│   ├── 01_select_sample.py                   (reproducible sample script)
│   └── 02_compute_metrics.py                 (reproducible metrics script)
├── 06_prereg/
│   └── (already deposited; preregistration document untouched)
└── README.md                                  (top-level index)
```

### Bước 5.3: Upload checklist

Per-file upload (drag-and-drop on OSF web UI):

#### Folder 01_manuscript
- [ ] `p6_meta_manuscript_en_v1.2.pdf` — convert from `p6/submission/mir_package/01_manuscript_blinded.docx`
- [ ] `p6_meta_manuscript_vi_v1.2.pdf` — convert from `p6/submission/mir_package/01_manuscript_blinded_vi.docx`
- [ ] `README_manuscript.md` — short note: "Current target = MIR; backup = MRQ, MBR"

#### Folder 02_data
- [ ] `p6/data/p6_study_database.csv`
- [ ] `p6/data/p6_study_database_codebook.md` (create if not exists: schema + coding rules used for ICRV/DPL/cDAI)
- [ ] `p6/tools/results/fulltext_to_extraction_tracker_v3.csv`

#### Folder 03_code
- [ ] All R scripts from `p6/scripts/`
- [ ] `p6/scripts/verify_moderator_qm.py`
- [ ] Create `README_replication.md` with step-by-step run instructions

#### Folder 04_supplementary
- [ ] `p6/submission/mir_package/osf_supplementary_materials.md`
- [ ] `p6/submission/mir_package/prisma_extraction_pipeline_status.md`
- [ ] `p6/submission/mir_package/prisma_status_report.json`
- [ ] `p6/figures/figure_prisma_2020_flow.png`
- [ ] `thesis/supplement_s_maida_vi.md` (AFTER filling all `[TO FILL]`)

#### Folder 05_validation
- [ ] `p6/gold_standard/gold_standard_sample.csv`
- [ ] `p6/gold_standard/gold_standard_manual_filled.csv` (AFTER Phase 2)
- [ ] `p6/gold_standard/validation_report.md` (AFTER Phase 3)
- [ ] `p6/gold_standard/validation_report.json` (AFTER Phase 3)
- [ ] `p6/gold_standard/01_select_sample.py`
- [ ] `p6/gold_standard/02_compute_metrics.py`

#### Top-level
- [ ] Update OSF project README with link to all 6 folders + brief description

### Bước 5.4: OSF visibility + DOI

- [ ] Đảm bảo project visibility = **Public**
- [ ] Tạo Persistent Identifier (DOI) qua "Add a DOI" trên OSF
- [ ] Confirm DOI = `10.17605/OSF.IO/Z37KN` (đã có theo manuscript reference)

---

## Phase 6: Update manuscript với validation evidence (✅ AUTOMATIC, ~5 phút)

Sau khi `validation_report.md` có data thực:

1. Mở `thesis/supplement_s_maida_vi.md`
2. §S-MAIDA.1: Điền tên LLM + version (ví dụ "Claude 3.5 Sonnet (claude-3-5-sonnet-20241022)")
3. §S-MAIDA.2: Dán prompt template thực tế
4. §S-MAIDA.4: Paste table content từ `validation_report.md`
5. §S-MAIDA.5: Paste mismatch breakdown từ `validation_report.json`
6. §S-MAIDA.6 và §S-MAIDA.7: Đã có sẵn nội dung, chỉ cần verify

Sau đó:
```bash
pandoc -f markdown-yaml_metadata_block -t docx \
  --reference-doc=templates/ctu_thesis_reference.docx \
  thesis/supplement_s_maida_vi.md \
  -o dist/luan_an_ctu/supplement_s_maida_vi.docx
```

Commit + push:
```bash
git add thesis/supplement_s_maida_vi.md dist/luan_an_ctu/supplement_s_maida_vi.docx p6/gold_standard/
git commit -m "feat(thesis): complete S-MAIDA validation (gold-standard k=30)"
git push origin claude/vietnamese-academic-standards-QuiLM
```

---

## Tổng kết timeline

| Phase | Effort | Owner | Status |
|---|---|---|---|
| 1. Sample selection | 1 phút | Auto (script) | ✅ DONE |
| 2. Manual extraction (30 papers) | 12–20 giờ | 👤 YOU | ⏳ pending |
| 3. Compute metrics | 1 phút | Auto (script) | ⏳ blocked by Phase 2 |
| 4. Inter-coder check (optional) | +4–6 giờ | 👤 YOU + colleague | ⏳ optional |
| 5. OSF deposit | ~30 phút | 👤 YOU (web UI) | ⏳ blocked by Phase 2-3 |
| 6. Update manuscript | ~5 phút | Auto + manual fill | ⏳ blocked by Phase 3 |
| **Total realistic** | **~15–25 giờ over 1 week** | | |

---

## Files trong workspace

```
p6/gold_standard/
├── 01_select_sample.py                  ✅ ready to use
├── 02_compute_metrics.py                ✅ ready to use
├── gold_standard_sample.csv             ✅ generated (32 rows)
├── gold_standard_manual_template.csv    ✅ generated (32 blank rows)
├── gold_standard_manual_filled.csv      ⏳ YOU fill from PDFs
├── validation_report.md                 ⏳ auto-generated after Phase 3
├── validation_report.json               ⏳ auto-generated after Phase 3
└── README_execution_plan.md             ← this file
```

---

## Questions / contingencies

**Q: Nếu không tìm được PDF của 1-2 papers?**
A: Replace từ pool tương đương trong cùng stratum. Modify `01_select_sample.py` để skip những `study_id` không có PDF, re-run. Document trong `validation_report.md` notes.

**Q: Nếu nhiều papers có specs ambiguous (e.g., không rõ DOI type)?**
A: Đó chính là điểm gold-standard cần phát hiện. Code conservatively (default sang loại phổ biến nhất khi mơ hồ); note trong `manual_notes`. Mismatch sẽ xuất hiện trong report — đó là tín hiệu hợp lệ.

**Q: Nếu Cohen kappa thấp (e.g., 0.55 cho ICRV) — có nghĩa fail submission?**
A: Không. Nghĩa là quantity đó phải trích xuất lại thủ công cho toàn corpus. Add: re-run primary MARA với data đã update + report change trong manuscript Limitations. Đây cũng là evidence of methodological rigor.

**Q: Có cần làm Phase 4 inter-coder?**
A: Không bắt buộc cho submission MIR, nhưng RẤT khuyến nghị cho dissertation defense. Single-coder design là explicit Limitation §5.4 — inter-coder check giải quyết hoàn toàn limitation này.

**Q: OSF deposit có thể defer sau MIR submission?**
A: Cover letter và §3.2.4 đã cite OSF z37kn. Reviewer có thể click link bất cứ lúc nào. Tốt nhất là deposit TRƯỚC khi submit MIR để link có nội dung khi reviewer mở.
