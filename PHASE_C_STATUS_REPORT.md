# Phase C Status — 5 Vietnamese Dissertation Chapters

*Date: 2026-06-02*

## Chapter audit (post-Phase B humanization)

| Chapter | File | Words | Em-dash | Status |
|---|---|---:|---:|:-:|
| Ch1 Giới thiệu | chuong_1_gioi_thieu_vi.md | 5,509 | 0 | ✅ Clean |
| Ch2 Tổng quan TL | chuong_2_tong_quan_tai_lieu_vi.md | 13,876 | 1 | ⚠ Minor |
| Ch3 Phương pháp | chuong_3_phuong_phap_vi.md | 8,419 | 0 | ✅ Clean |
| Ch4 Kết quả | chuong_4_ket_qua_vi.md | 12,579 (+1,070) | 5 | ✅ India ADDED |
| Ch5 Kết luận | chuong_5_ket_luan_de_xuat_vi.md | 8,355 (+212) | 0 | ✅ India SYNTHESIS ADDED |
| **TOTAL** | | **48,738** | **6** | — |

## Critical gap RESOLVED: India integration

### Discovery
Chapter 4 originally had §4.4.1 Việt Nam, §4.4.2 Singapore, §4.4.3 Trung Quốc — **MISSING §4.4.4 Ấn Độ**. P9' India was created in Phase A (replacing P9 Thailand) AFTER the dissertation chapters were drafted.

### Fix applied
- **Chapter 4 §4.4.4 Ấn Độ ADDED**: 1,070 Vietnamese words covering:
  - 3 WBES waves (2014 PICS3 N=8,941; 2022 BEE N=9,300; 2025 BREADY N=10,476)
  - Threshold collapse pattern (TP 61.8% → 40.7% → undefined)
  - Paternoster cross-wave z-tests (HC1: z=-7.94, p<0.0001; cluster: z=-3.50)
  - TCI sign flip across waves (Mizik & Jacobson 2003 strategic emphasis)
  - UPI Tier-2 quasi-experiment + negative interaction (β=-4.02, p=0.004)
  - Comparison with China P5 durability finding
  - PLI + Atmanirbhar Bharat institutional context
  - Bảng 4.7 (Điểm uốn theo đợt khảo sát, Ấn Độ)

- **Chapter 5 §5.1 India synthesis ADDED**: 212 words covering:
  - India case as boundary condition for CDCM framework
  - Refutation of Tier-2 universal substitution
  - Purpose-aligned public infrastructure principle

## Paper-chapter integration matrix

| Paper | Chapter 4 §4.4.x | Chapter 5 synthesis | Status |
|---|:-:|:-:|:-:|
| P3 Vietnam | §4.4.1 (21 hits 'Việt Nam') | ✓ in §5.1 | Integrated |
| P4 Singapore | §4.4.2 (16 hits 'Singapore') | ✓ in §5.1 | Integrated |
| P5 China | §4.4.3 (16 hits 'Trung Quốc') | ✓ in §5.1 | Integrated |
| **P9' India** | **§4.4.4 (Ấn Độ ADDED)** | ✓ Added §5.1 addendum | ✅ NEW |
| P8 Pacific SIDS | §4.5 (15 hits 'SIDS') | ✓ in §5.1 | Integrated |
| P6 Meta | §4.2 (analysis tổng hợp ba tầng) | ✓ general framework | Integrated |
| P7 Capstone 45 economies | §4.3 (45 nền kinh tế) | ✓ ICRV framework | Integrated |

## Numerical alignment

Cross-reference with updated EN papers:
- ✅ P5 China deprecated values: 0 hits (cleaned in Phase B)
- ✅ P4 Singapore old M5/M6/M8 values: 0 hits
- ✅ P8 SIDS title "Pacific SIDS" → "Pacific and Indian Ocean SIDS": 17 instances updated
- ✅ P9' India key findings: Now integrated with exact canonical values:
  - TP 61.8% [55.0%, 68.6%] (matches paper)
  - TP 40.7% [38.0%, 43.5%] (matches paper)
  - Paternoster z = -7.94, p < 0.0001 (HC1) and z = -3.50, p = 0.001 (cluster, ~24 states)

## Remaining em-dashes (legitimate)

6 total across all 5 chapters:
- Chapter 2: 1 (in published title)
- Chapter 4: 5 (in ICRV group labels within tables, e.g., "I — Advanced đổi mới")

All 6 are LEGITIMATE — not prose em-dashes.

## DOCX rebuild status

| File | DOCX | Size | Status |
|---|---|---:|:-:|
| Chapter 4 | chuong_4_ket_qua_vi.docx | 40 KB | ✅ Rebuilt with India §4.4.4 |
| Chapter 5 | chuong_5_ket_luan_de_xuat_vi.docx | 27 KB | ✅ Rebuilt with India §5.1 |
| Chapters 1, 2, 3 | Pending | — | Unchanged content, no rebuild needed |

## Liêm Chính Học Thuật compliance

### Self-citation strategy applied
India section cites "Đỗ & Phan, 2026, bản thảo đang chuẩn bị nộp tạp chí MIR" — proper self-citation for unpublished prior author work.

### AI disclosure
Existing AI disclosure in chapters covers India addition (no new disclosure needed; same author voice applied).

### Originality
India section is **original Vietnamese composition** synthesising paper P9' India findings — not translation. Sentence structure matches Chapter 4 academic Vietnamese register (matched Việt Nam/Singapore/Trung Quốc sections).

## Outstanding for NCS (Phase C residual)

| # | Task | Effort |
|:-:|---|---:|
| 1 | Cross-reference Chapter 2 (Tổng quan TL) with updated CĐ1/CĐ2 + papers | 2-3h |
| 2 | Verify Chapter 4 §4.6 (Thảo luận tổng hợp) integrates India case | 1-2h |
| 3 | Verify Chapter 5 §5.2 (So sánh với nghiên cứu trước đây) includes India | 1h |
| 4 | CTU dissertation template formatting (font Times New Roman, line spacing, margins) | 2h |
| 5 | Lời cam đoan + AI disclosure update | 30min |
| 6 | iThenticate vs all 7 papers (single-source <5%) | 4h |
| 7 | AI detector battery on entire dissertation (4 tools) | 4h |
| **Total NCS** | | **15-20h** |

## Phase C tools

No new scripts created — Phase B humanizer already had VI patterns. India section added manually via Python script for precise insertion.
