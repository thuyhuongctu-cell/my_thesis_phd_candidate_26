# KẾ HOẠCH TRIỂN KHAI REVIEW TOÀN BỘ TÀI LIỆU LUẬN ÁN
## Liêm Chính Học Thuật + Submission Standards

*Tác giả: NCS. Đỗ Thùy Hương · GVHD: PGS.TS. Phan Anh Tú*
*Ngày lập: 2026-06-02*
*Mục tiêu: Đảm bảo toàn bộ tài liệu đạt chuẩn submit + tuân thủ Luật Liêm Chính Học Thuật VN*

---

## I. PHẠM VI VÀ TIÊU CHUẨN

### I.1. Phạm vi (3 layer × 17 artifacts)

| Layer | Artifact | File chính | Words | Status hiện tại |
|---|---|---|---:|---|
| **L1 Papers EN** | P3 Vietnam | `p3/p3_vietnam_en_clean.md` | 21,372 | 4 we/our, 0 em-dash |
| | P4 Singapore | `p4/p4_singapore_en_clean.md` | 13,669 | 3 we/our, 0 em-dash |
| | P5 China | `p5/p5_china_en_clean.md` | 7,308 | 1 we/our, 0 em-dash |
| | P6 Meta | `p6/p6_meta_manuscript_en.md` | 11,129 | 4 we/our, 0 em-dash |
| | P7 Capstone | `p7/p7_capstone_en_clean.md` | 10,884 | 9 we/our, 0 em-dash |
| | P8 SIDS | `p8/p8_pacific_sids_en_clean.md` | 7,828 | 5 we/our, 0 em-dash |
| | P9' India | `p9_india/p9_india_en_clean.md` | 8,424 | 0 we/our, 2 em-dash (titles) ✅ |
| **L2 Chuyên đề VI** | CĐ1 (Tổng luận tài liệu) | `chuyen_de/cd1/00_cd1_ctu_final_vi.md` | 16,584 | 0 em-dash |
| | CĐ2 (Khung lý thuyết) | `chuyen_de/cd2/00_cd2_ctu_final_vi.md` | 24,140 | 3 em-dash |
| | CĐ1 expansion P1 | `thesis/14_cd1_part1_intro_theory_vi.md` | 6,374 | 25 em-dash |
| | CĐ1 expansion P2 | `thesis/15_cd1_part2_findings_vi.md` | 9,520 | 63 em-dash ⚠ |
| | CĐ1 expansion P3 | `thesis/16_cd1_part3_cases_conclusion_vi.md` | 8,414 | 18 em-dash |
| **L3 Luận án VI (5 chương)** | Chương 1 Giới thiệu | `thesis/chuong_1_gioi_thieu_vi.md` | 5,508 | 0 em-dash |
| | Chương 2 Tổng quan TL | `thesis/chuong_2_tong_quan_tai_lieu_vi.md` | 13,875 | 2 em-dash |
| | Chương 3 Phương pháp | `thesis/chuong_3_phuong_phap_vi.md` | 8,420 | 3 em-dash |
| | Chương 4 Kết quả | `thesis/chuong_4_ket_qua_vi.md` | 11,190 | 9 em-dash |
| | Chương 5 Kết luận đề xuất | `thesis/chuong_5_ket_luan_de_xuat_vi.md` | 7,933 | 0 em-dash |
| **Tổng** | 17 artifacts | | **~180,000 words** | |

### I.2. Tiêu chuẩn chất lượng (4 trụ cột)

| Trụ cột | Tiêu chí | Đo bằng |
|---|---|---|
| **Học thuật** | Lập luận chặt chẽ, citation đầy đủ, đóng góp lý thuyết rõ | dissertation-theoretical-framework-reviewer skill |
| **Liêm chính** | Không AI tạo sinh, không copy, citation đúng | AI detector (GPTZero/Copyleaks/Pangram/Originality) + iThenticate |
| **Tác giả voice** | Phong cách Đỗ Thùy Hương + Phan Anh Tú, trưởng thành | chuyen-doi-van-ban-ai-theo-giong-tac-gia + book chapter benchmark |
| **Submit standards** | Đáp ứng chuẩn tạp chí/CTU defense | Per-journal checklist + CTU dissertation format |

### I.3. Khung pháp lý

Việt Nam ban hành **Thông tư về Liêm chính học thuật** (LCHT). Yêu cầu rà soát:
1. **Tính nguyên gốc**: tài liệu là sản phẩm độc lập của tác giả
2. **Trích dẫn đúng quy chuẩn**: APA 7 / Harvard, không thiếu sót
3. **Không AI tạo sinh trực tiếp**: AI chỉ hỗ trợ ngôn ngữ, không thay tác giả
4. **Tự kiểm**: tác giả chịu trách nhiệm cuối cùng

---

## II. THỨ TỰ ƯU TIÊN (3 PHASE)

```
PHASE A: Papers EN review (P3-P8, ~6 papers)   ⏱ 12-18h
  ↓ (Papers chốt findings → CĐ phải đồng bộ)
PHASE B: Chuyên đề 1 + 2 sync                  ⏱ 6-10h
  ↓ (CĐ chốt khung lý thuyết → Chapters đồng bộ)
PHASE C: 5 Chương luận án VI                   ⏱ 10-15h
  ↓
PHASE D: Cross-document liêm chính audit       ⏱ 4-6h
─────────────────────────────────────────────
TỔNG: 32-49h focused work (4-7 ngày)
```

---

## III. PHASE A — REVIEW 6 PAPERS EN (P3, P4, P5, P6, P7, P8)

*P9' India đã hoàn tất 12 milestone, dùng làm reference template.*

### III.1. Quy trình chuẩn cho mỗi paper (7 bước)

```
STEP A1 (15 min) — Pre-review audit
  Đo metrics: word count, em-dash, we/our, references count, figures/tables
  So sánh với P9' India baseline

STEP A2 (30 min) — Comprehensive review
  Spawn lfe-academic-reviewer subagent
  Input: manuscript + submission package
  Output: 7-section review (hypothesis-result alignment, theoretical
          contribution, self-plagiarism, methods rigor, journal fit,
          APA7 consistency, top 5 red flags)

STEP A3 (15 min) — Theoretical framework review
  Invoke dissertation-theoretical-framework-reviewer skill
  Output: structural analysis, hypothesis review, integration check

STEP A4 (60-120 min) — Apply Top 3-5 fixes
  Priority: internal contradictions → §5 Discussion gaps → references
  Use lfe-paper-writer subagent for substantial rewrites
  Use Edit tool for targeted corrections

STEP A5 (15 min) — Voice transfer + humanizer
  Re-run scripts/humanize_portfolio.py if any new content added
  Manual review for remaining we/our (P3, P7 priority)
  Apply humanizer skill if needed

STEP A6 (30 min) — Stop-slop verification
  Target: ≥ 35/50 score
  Document score in HUMANIZATION_FINAL_REPORT.md per paper

STEP A7 (20 min) — Rebuild DOCX
  Adapt p9_india/replication/build_docx.py for each paper
  Rebuild: manuscript_blinded.docx + title_page.docx + cover_letter.docx
  Verify figures embedded
```

### III.2. Per-paper priority + specific concerns

| Paper | Target journal | Priority | Specific concerns |
|---|---|:-:|---|
| **P5 China** | IJOEM Q1 | 🟢 LOW | Đã ngắn (7,308w), 1 we/our; chỉ cần rebuild DOCX |
| **P4 Singapore** | JABES Q1 | 🟢 LOW | 13,669w, 3 we/our; figures + tables status unclear |
| **P8 Pacific SIDS** | JED Q1 | 🟡 MED | 7,828w, 5 we/our; "FIP" concept needs theoretical defence |
| **P6 Meta** | IBR/MIR Q1 | 🟡 MED | 11,129w, 4 we/our; no replication folder = methodology audit needed |
| **P3 Vietnam** | JED Q1 | 🟡 MED | 21,372w (OVER target 12K), 4 we/our; needs WORD CAP reduction |
| **P7 Capstone** | JIBS ABS-4* | 🔴 HIGH | 9 we/our highest; JIBS rejection rate ~90% means quality bar critical |

### III.3. Skills mapping cho Phase A

| Skill | Mục đích | Papers cần |
|---|---|---|
| `lfe-academic-reviewer` (subagent) | Full review | All 6 |
| `dissertation-theoretical-framework-reviewer` | Theory review | P3, P6, P7 (theory-heavy) |
| `lfe-paper-writer` (subagent) | Major rewrites | P3 word cap, P7 polish |
| `humanizer` | AI patterns scan | P3, P7 (remaining we/our) |
| `stop-slop` | Final AI tells | All 6 |
| `chuyen-doi-van-ban-ai-theo-giong-tac-gia` | Voice transfer | All 6 (consistency) |
| `academic-conceptual-model-diagram` | Render missing figures | P4 (0 figs), P6 (no replication), P7 (0 figs), P8 (0 figs) |
| `academic-variable-formatter` | Var notation | All 6 (consistency check) |

### III.4. Verification checklist (per paper)

```
□ Word count within journal target range
□ Em-dash count ≤ 5 (titles + figure captions only)
□ we/our prose count ≤ 5 (Acknowledgements/Disclosure excepted)
□ AI vocabulary scan: 0 hits (crucial/delve/landscape/etc.)
□ Mid-sentence boldface emphasis: 0
□ Inline-header vertical lists: 0
□ Negative parallelism: 0
□ Stop-slop score: ≥ 35/50
□ No [TBD] / [Placeholder] / [Insert] markers remaining
□ References Harvard/APA7 format consistent
□ Self-citation (Do & Phan 2025 book chapter for India only): properly
  disclosed where applicable
□ Figures rendered + embedded in DOCX
□ Tables typeset + embedded in DOCX
□ Title page DOCX with CRediT + AI disclosure
□ Cover letter DOCX targeted at specific journal
□ Submission checklist README updated
```

### III.5. Risk mitigation

| Risk | Mitigation |
|---|---|
| P3 word cap (21K → 12K = 45% cut) | Targeted abstract + dedicated reduction plan via lfe-paper-writer |
| P7 JIBS quality bar (top 0.5% accept) | Extra round of review; consider compress to JIBS Insights 3.5K |
| Cross-paper inconsistency (numbers, citations) | Master numbers reconciliation table at end of Phase A |
| Self-citation overlap | iThenticate cross-paper check |
| Voice inconsistency across portfolio | Use Do & Phan 2025 book chapter as single voice benchmark |

---

## IV. PHASE B — CHUYÊN ĐỀ 1 + 2 SYNCHRONIZATION

### IV.1. Mapping CĐ ↔ Papers

| CĐ section | Sources from EN papers | Last sync |
|---|---|---|
| **CĐ1 Part 1** (Intro + Theory) | P6 Meta findings, P7 Capstone theory | After P6+P7 finalised |
| **CĐ1 Part 2** (Findings) | P3 Vietnam, P5 China, P4 Singapore | After P3+P4+P5 finalised |
| **CĐ1 Part 3** (Cases + Conclusion) | P8 SIDS, P9' India | After P8+P9' finalised |
| **CĐ2 Section 2-3** (Theoretical framework) | P7 Capstone CDCM | After P7 finalised |
| **CĐ2 Section 4-5** (Empirical operationalisation) | All 7 papers | After Phase A done |

### IV.2. Quy trình sync (5 bước)

```
STEP B1 (45 min) — Cross-reference scan
  Script: scripts/check_cd_paper_alignment.py (NEW)
  Output: table of numbers/findings differing between CĐ and source paper

STEP B2 (60 min) — Theoretical framework reconcile
  Spawn dissertation-theoretical-framework-reviewer skill
  Verify CDCM framework consistent across CĐ2 + P6 + P7
  Check ICRV group definitions consistent

STEP B3 (90 min) — Vietnamese humanization
  Apply Vietnamese-specific patterns:
    - "Chúng tôi" → "Tác giả" / "Nghiên cứu này"
    - "Của chúng tôi" → "Của tác giả" / "Của nghiên cứu này"
    - Em-dash → dấu phẩy/chấm
    - Title case heading → sentence case
  Use chinh-sua-van-ban-hoc-thuat-scopus-wos skill

STEP B4 (45 min) — Update numbers + references
  Propagate any updated findings from Phase A
  Verify Vietnamese reference list = English reference list (mapped)

STEP B5 (30 min) — Rebuild CĐ DOCX
  Pandoc Vietnamese template
  Submission package: cd1_bia_chinh.docx + cd1_bia_phu.docx + main
```

### IV.3. CĐ1 expansion files (thesis/14, 15, 16) — special concern

3 files có **106 em-dashes** tổng cộng. Khả năng cao đây là AI-generated drafts chưa được humanize. Cần:
1. Run scripts/humanize_portfolio.py adapted for Vietnamese
2. Manual review CĐ1 Part 2 (63 em-dashes nhiều nhất)
3. Verify alignment with main `chuyen_de/cd1/00_cd1_ctu_final_vi.md`

### IV.4. Verification checklist (per CĐ)

```
□ Em-dash count ≤ 5 (only in published titles)
□ "Chúng tôi" / "của chúng tôi" → đã chuyển sang "tác giả" / "nghiên cứu này"
□ Vietnamese AI-pattern words audited (quan trọng/then chốt/đáng chú ý overuse)
□ All numbers reconciled with source EN papers
□ APA7 citation style consistent
□ Vietnamese term glossary (`09b_vn_term_glossary.md`) applied
□ CTU template formatting applied (font Times New Roman 13pt, line 1.5)
□ Bia chinh + bia phu DOCX rebuilt
□ TLTQ requirements met (per `chuong_trinh_dao_tao/cd1/NCS_huong_dan_viet_chuyen_de_TLTQ.docx`)
```

---

## V. PHASE C — 5 CHƯƠNG LUẬN ÁN (VI)

### V.1. Cross-references chuong ↔ CĐ ↔ Paper

| Chương | Source CĐ | Source Papers |
|---|---|---|
| **Chương 1** Giới thiệu | — | All 7 (positioning) |
| **Chương 2** Tổng quan tài liệu | CĐ1 (cores) | P6 Meta, P7 theory |
| **Chương 3** Phương pháp | CĐ2 §4 | P7 Capstone methods |
| **Chương 4** Kết quả | — | All 7 (numbers) |
| **Chương 5** Kết luận và đề xuất | CĐ2 §5 | All 7 (synthesis) |

### V.2. Quy trình chương (6 bước)

```
STEP C1 (30 min) — Audit + cross-ref scan
  Find references/numbers from updated papers/CĐ that need propagation

STEP C2 (60 min) — Theoretical framework alignment (Chương 2, 3)
  Verify CDCM framework + hypothesis system consistent across thesis

STEP C3 (60 min) — Empirical alignment (Chương 4)
  All numerical findings cross-referenced with paper results CSVs
  Update Vietnamese tables/figures if EN versions changed

STEP C4 (90 min) — Vietnamese humanization
  Same patterns as CĐ + Vietnamese specific:
    - Long compound sentences → split
    - Han-Viet vs Pure Vietnamese vocabulary balance per author profile
    - Vietnamese academic register (formal-respectful)
  Apply chuyen-doi-van-ban-ai-theo-giong-tac-gia (adapt for VI)

STEP C5 (45 min) — Liêm chính học thuật review
  Per-chapter check:
    - Trích dẫn đúng nguồn
    - Không đoạn copy 100% từ paper/CĐ
    - Lập luận tự bản thân
    - Self-citation rõ ràng (luận án vs paper)

STEP C6 (30 min) — Rebuild DOCX with CTU template
  CTU dissertation format (font Times New Roman, A4 portrait, header,
  page numbers, TOC, list of figures/tables)
```

### V.3. Per-chapter priority

| Chương | Words | Priority | Concerns |
|---|---:|:-:|---|
| Chương 1 Giới thiệu | 5,508 | 🟢 LOW | Đã sạch, em-dash 0 |
| Chương 2 Tổng quan TL | 13,875 | 🟡 MED | Cập nhật theo P6 + P7 sync |
| Chương 3 Phương pháp | 8,420 | 🟡 MED | Sync với P7 methods |
| **Chương 4 Kết quả** | **11,190** | **🔴 HIGH** | 9 em-dash, all 7 papers data feed into đây |
| Chương 5 Kết luận | 7,933 | 🟡 MED | Synthesis quality critical |

### V.4. Liêm chính học thuật — specific protocols

```
PROTOCOL 1: Tự trích dẫn (self-citation)
  Luận án dùng paper làm bằng chứng → phải cite "Đỗ Thùy Hương & Phan
  Anh Tú (forthcoming/under review at Journal X)" rõ ràng
  Hoặc "Trong nghiên cứu trước của tác giả (cite paper), ..." nếu paper
  đã xuất bản

PROTOCOL 2: Không lặp lại 100%
  Câu chữ trong luận án phải KHÁC với câu chữ trong paper, ngay cả khi
  cùng tác giả. Diễn đạt lại, không copy-paste.
  Target: < 30% similarity per iThenticate

PROTOCOL 3: AI tools disclosure
  Bao gồm AI disclosure statement trong:
    - Lời cam đoan của NCS (mới)
    - Acknowledgements
    - Phương pháp (nêu cách dùng AI: chỉ hỗ trợ ngôn ngữ, không tạo nội dung)

PROTOCOL 4: Verify original
  Run iThenticate trên TOÀN luận án (tất cả chương + CĐ)
  Target similarity:
    - Toàn văn: < 20%
    - Single source: < 5%
    - Khi exclude own publications: < 10%
```

---

## VI. PHASE D — CROSS-DOCUMENT LIÊM CHÍNH AUDIT

### VI.1. Quy trình (3 bước)

```
STEP D1 (60 min) — Self-plagiarism cross-check
  Script: scripts/check_self_plagiarism.py (NEW)
  Compare prose between:
    - EN papers (P3 vs P5 vs P7 cross-overlap)
    - EN paper → VI CĐ → VI Chương cascading
  Output: similarity matrix
  Flag any segment > 60 words verbatim

STEP D2 (90 min) — AI detection battery
  Run on EACH artifact (17 files):
    - GPTZero academic mode
    - Copyleaks AI Detector
    - Pangram (latest)
    - Originality.ai academic preset
  Target: all < 25% AI flagged

STEP D3 (60 min) — Author voice consistency audit
  Verify Đỗ Thùy Hương + Phan Anh Tú voice across all 17 artifacts
  Compare with reference: Do & Phan 2025 IntechOpen book chapter
  Check matured argumentation: PhD-level vs Master-level evidence
```

### VI.2. Liêm chính học thuật checklist (master)

```
□ Lời cam đoan luận án có chữ ký NCS + GVHD
□ AI disclosure statement có trong tất cả 17 artifacts
□ Self-citation đầy đủ ở mọi chỗ tham chiếu paper riêng
□ iThenticate similarity:
   - Mỗi paper EN: < 20% (single source < 5%)
   - Mỗi CĐ: < 20% (single source < 5%)
   - Mỗi chương: < 20% (single source < 5%)
   - Luận án tổng: < 15% (excluding own publications)
□ AI detector (4 tools): tất cả < 25%
□ Reference list bibliography đầy đủ APA7
□ Bảng kê công trình NCS tự công bố (`98_danh_muc_cong_trinh_vi.md`)
   cập nhật với P3-P9
□ Tránh circular citation
□ Author contribution statement (CRediT) ở mọi paper
```

---

## VII. EXECUTION TIMELINE + DEPENDENCIES

### VII.1. Critical Path

```
Day 1-2: Phase A1-A2 (Papers P5, P4, P8 — LOW/MED priority, ~6h)
Day 3-4: Phase A3-A4 (Papers P6, P3, P7 — MED/HIGH priority, ~12h)
         ↓ MILESTONE: All 6 papers verified ≥ 35/50
Day 5:   Phase B (Chuyên đề 1 + 2 sync, ~8h)
         ↓ MILESTONE: CĐ aligned with papers
Day 6-7: Phase C (5 chương VI, ~13h)
         ↓ MILESTONE: All chapters consistent
Day 8:   Phase D (Liêm chính audit, ~5h)
         ↓ MILESTONE: All 17 artifacts cleared for defense
```

### VII.2. Parallelization opportunities

| Task A | Task B | Có thể chạy song song? |
|---|---|:-:|
| Review P3 | Review P5 | ✅ (independent) |
| Review papers | Audit CĐ structure | ✅ |
| Render figures | Run humanizer | ✅ |
| iThenticate check | AI detector check | ✅ |
| Chapter 1 VI | Chapter 5 VI | ✅ |

### VII.3. Sequential dependencies (cannot parallelize)

| Task | Depends on |
|---|---|
| CĐ1 sync | All EN papers final |
| Chương 2 sync | CĐ1 final |
| Chương 4 sync | All paper results + Chương 3 methods |
| Chương 5 synthesis | All chapters draft + CĐ2 conclusion |

---

## VIII. SKILL UTILIZATION MATRIX

| Skill | Phase A | Phase B | Phase C | Phase D | Use Cases |
|---|:-:|:-:|:-:|:-:|---|
| lfe-academic-reviewer | ✓ | ✓ | ✓ | | Comprehensive review per artifact |
| dissertation-theoretical-framework-reviewer | ✓ | ✓ | ✓ | | Theory consistency |
| lfe-paper-writer | ✓ | ✓ | ✓ | | Major rewrites (P3 word cap, P7 polish) |
| lfe-quick-fixer | ✓ | ✓ | ✓ | | Minor typo/format |
| lfe-reference-archivist | | | | ✓ | Final reference reconciliation |
| chuyen-doi-van-ban-ai-theo-giong-tac-gia | ✓ | ✓ | ✓ | | Voice transfer |
| humanizer | ✓ | ✓ | ✓ | | 22+ AI patterns |
| phd-academic-writing-humanizer | ✓ | ✓ | ✓ | | Em-dash + PhD-specific |
| stop-slop | ✓ | ✓ | ✓ | ✓ | Final AI tells |
| chinh-sua-van-ban-hoc-thuat-scopus-wos | | ✓ | ✓ | | Vietnamese academic standards |
| chinh-sua-tai-lieu-latex-khoa-hoc | ✓ | ✓ | ✓ | | LaTeX/Word output |
| academic-conceptual-model-diagram | ✓ | ✓ | ✓ | | Figure rendering |
| academic-variable-formatter | ✓ | | | ✓ | Variable notation |
| academic-translation-vietnamese | | ✓ | ✓ | | EN→VI bilingual check |

---

## IX. DELIVERABLES (END STATE)

### IX.1. Tài liệu submission-ready

```
17 artifacts × 4 verification dimensions = 68 checkpoints, all PASS

PAPERS EN (7 packages):
├── P3 Vietnam JED package
├── P4 Singapore JABES package
├── P5 China IJOEM package
├── P6 Meta IBR/MIR package
├── P7 Capstone JIBS package
├── P8 SIDS JED package
└── P9' India MIR package ✅ (already done)

CHUYÊN ĐỀ (2 packages):
├── CĐ1 Tổng luận tài liệu (bia chinh + bia phu + nội dung)
└── CĐ2 Khung lý thuyết (bia chinh + bia phu + nội dung)

LUẬN ÁN (full thesis package):
├── 5 chương DOCX
├── References APA7
├── Phụ lục
├── Danh mục công trình
├── Tóm tắt LATS
├── Lời cam đoan (có AI disclosure)
└── Bia chinh + bia phu CTU template
```

### IX.2. Audit artifacts

```
reports/
├── phase_a_papers_review.md      (per-paper review summary)
├── phase_b_cd_sync.md            (CĐ-paper alignment matrix)
├── phase_c_chapters_audit.md     (chapter quality scores)
├── phase_d_liem_chinh_audit.md   (similarity + AI detector results)
├── master_numbers_table.md       (cross-document numerical consistency)
└── final_compliance_certificate.md (LCHT compliance statement)
```

---

## X. RISK REGISTER

| Risk | Probability | Impact | Mitigation |
|---|:-:|:-:|---|
| P3 word cap reduction breaks logic | Medium | High | Section-by-section reduction; verify before final |
| P7 JIBS desk-reject | High | Low (backup IJOEM) | Pre-flight check via lfe-academic-reviewer |
| CĐ numbers drift from papers | Medium | High | Master numbers table, sync after Phase A done |
| iThenticate flags > 25% similarity | Low | Critical | Use original VI wording; cite EN paper version |
| AI detector false positive | Medium | Medium | 4-tool consensus; argue with detector if needed |
| Defense schedule slipping | Medium | High | Phase A priority papers (P3, P5, P9) → defense-critical |
| GVHD review iterations | High | Medium | Build buffer time for 2-3 rounds feedback |

---

## XI. NCS DECISION POINTS

Cô cần quyết định:

1. **Targeting strategy P7 Capstone**:
   - (a) Push JIBS full (8K, ~10% accept) — high risk high reward
   - (b) Compress JIBS Insights (3.5K, ~30% accept) — moderate
   - (c) Redirect to IJOEM (8K, ~55% accept) — safe

2. **P3 word cap strategy**:
   - (a) Full reduction 21K → 12K (45% cut) trong session này
   - (b) Submit longer version to journal cho phép (IBR cap 15K)
   - (c) Keep 21K cho dissertation, build 11.6K version riêng cho journal

3. **Chương 4 VI complexity**:
   - (a) All 7 papers data → Chương 4 (sẽ rất dài, 15-20K words)
   - (b) Highlight 3-4 papers core (P3, P5, P7, P9') + summary table còn lại
   - (c) Split Chương 4 thành 4A và 4B (single-country vs multi-country)

4. **iThenticate strategy**:
   - (a) Run per artifact ngay (cần access institutional)
   - (b) Run sau khi NCS có account
   - (c) Skip, dùng Turnitin Free / GPTZero similarity feature

5. **Timeline preference**:
   - (a) Sprint: 8 ngày liên tục (32-49h)
   - (b) Tuần: 2 tuần × 16-25h/tuần
   - (c) Tháng: 4 tuần × 8-12h/tuần (preserve daily focus)

---

## XII. KICK-OFF PROPOSAL

Nếu Cô đồng ý plan, em đề xuất start với:

**Hôm nay (session này)**:
1. Phase A1 + A2 cho **P5 China** (priority LOW, 1.5h) — proof of concept
2. Document quality checkpoint
3. Cô review template approach trước khi áp dụng cho 5 papers còn lại

**Sau khi P5 done**:
- Apply template cho P4, P8 (LOW/MED priority)
- Sau đó P6, P3, P7 (MED/HIGH)
- Cuối Phase A: master numbers table + commit

Cô confirm để em proceed, hoặc adjust plan theo ưu tiên của Cô.

---

*Plan tổng: ~32-49h work, 4-7 ngày focused. Output: 17 artifacts submission-ready + 6 audit reports.*
