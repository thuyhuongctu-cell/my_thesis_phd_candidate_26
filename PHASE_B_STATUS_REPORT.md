# Phase B Status — CĐ1/CĐ2 Sync

*Date: 2026-06-02*

## Phase B objectives (per implementation plan)

| Step | Task | Status |
|---|---|:-:|
| B1 | Cross-reference scan (CĐ vs source papers) | ✅ Complete |
| B2 | Theoretical framework reconcile | ⏳ NCS workflow |
| B3 | Vietnamese humanization | ✅ Complete |
| B4 | Update numbers + references | ✅ P8 title propagated (17 instances) |
| B5 | Rebuild CĐ DOCX | ✅ Complete |

## B1: Cross-reference scan results

### CĐ vs updated EN papers — alignment check

| Updated paper | Change in Phase A | CĐ impact | Status |
|---|---|---|:-:|
| P5 China | Table 2 +1.28 → +2.065 etc. | 0 hits of old values in CĐ | ✅ No drift |
| P4 Singapore | M5/M6/M8 FSTS values updated | 0 hits in CĐ | ✅ No drift |
| P8 Pacific SIDS | Title relabeled | 17 instances "Pacific SIDS" updated | ✅ Synced |
| P3 Vietnam | §2 Theory compressed | No numerical change in CĐ | ✅ No action needed |
| P9' India | Threshold collapse finding | 1 hit in CĐ1 (line 472) | ✅ Aligned |

## B3: Vietnamese humanization results

### Em-dash removal across portfolio

| File | Before | After | Removed |
|---|---:|---:|---:|
| chuyen_de/cd1/00_cd1_ctu_final_vi.md | 0 | 0 | 0 |
| chuyen_de/cd2/00_cd2_ctu_final_vi.md | 3 | 1 | 2 |
| thesis/14_cd1_part1_intro_theory_vi.md | 25 | 8 | 17 |
| thesis/15_cd1_part2_findings_vi.md | 63 | 45 | 18 |
| thesis/16_cd1_part3_cases_conclusion_vi.md | 18 | 14 | 4 |
| thesis/chuong_2_tong_quan_tai_lieu_vi.md | 2 | 1 | 1 |
| thesis/chuong_3_phuong_phap_vi.md | 5 | 0 | 5 |
| thesis/chuong_4_ket_qua_vi.md | 12 | 5 | 7 |
| thesis/chuong_1, chuong_5_vi.md | 0 | 0 | 0 |
| **Total** | **128** | **74** | **54** |

Remaining 74 em-dashes are LEGITIMATE — in:
- Section headings (e.g., "Chương 4 — Thực trạng...")
- Figure/table captions (preserved by `Hình`/`Bảng`/`Source:` line detection)
- Table cells (preserved by `|` pipe line detection)
- Bibliography titles (preserved in References section)

### "Chúng tôi" status
Already cleaned in prior pass — 0 instances in all 10 files. No action this pass.

### Vietnamese AI-tell patterns
- "then chốt" / "đáng chú ý" / "sâu sắc" / "phong phú" / "toàn diện" — 4 instances fixed
- "trong bối cảnh hiện nay" → "hiện nay" — applied
- "có thể nói rằng" / "điều quan trọng cần lưu ý là" filler removed

## B4: Stale reference updates

**17 instances** propagated:
- "Pacific SIDS" → "Pacific and Indian Ocean SIDS" (per P8 title change Phase A1)
  - CĐ1: 5 instances
  - thesis/14: 9 instances
  - thesis/chuong_1: 1 instance
  - thesis/chuong_2: 1 instance
  - thesis/chuong_3: 1 instance

## B5: DOCX rebuild results

| File | DOCX size | Word count (extracted) | Status |
|---|---:|---:|:-:|
| chuyen_de/cd1/00_cd1_ctu_final_vi.docx | 56 KB | ~16,000 | ✅ |
| chuyen_de/cd2/00_cd2_ctu_final_vi.docx | 935 KB | ~24,000 | ✅ |

CĐ2 larger due to embedded figures (conceptual model + others).

## Outstanding for NCS (B2 work)

### Theoretical framework reconciliation

Following P5/P7 updates need cross-check in CĐ2:

1. **CDCM framework (Conditional Digital Capability Moderation)**
   - Updated in P9' India paper (added Tier-1 vs Tier-2 distinction)
   - CĐ2 §2.3 should reference Tier-2 (UPI public infrastructure)
   - Estimated work: 1h

2. **Institutional Context Regime Variation (ICRV)**
   - 6-group taxonomy used in P7 Capstone
   - CĐ2 §2.4 ICRV definition should match P7 audit (45 economies, not 49)
   - Already standardised in P7; verify CĐ2 matches

3. **CIMT (Capability-Institution Mismatch Theory)**
   - P7 reviewer flagged: manuscript has 0 hits for CIMT
   - CĐ2 may still claim CIMT as theoretical anchor
   - NCS decision: retire CIMT label or restore to P7

### Number cross-reference

Manual review needed for:
- CĐ1 §2.3 (Vietnam) — confirm matches P3 Vietnam paper
- CĐ1 §3.1 (China) — confirm matches P5 canonical values
- CĐ1 §3.2 (India) — confirm matches P9' India threshold collapse finding

Estimated effort: 4-6h focused review.

## Phase B → Phase C transition

Phase B has cleared the major em-dash + stale reference issues. CĐ1/CĐ2 prose is now humanized. The remaining theoretical reconciliation work (B2) is best done by NCS with deep familiarity with the framework.

Phase C (5 Vietnamese chapters) can begin in parallel because:
1. ✅ Chapters already include the P8 title update (propagated via humanizer)
2. ✅ Chapter 4 em-dashes cleaned (12 → 5)
3. ✅ Chapter 1/3/5 are clean
4. ⏳ Chapter 2 + 4 may need cross-reference review for paper findings

## Tools deployed in Phase B

- `scripts/humanize_vietnamese.py` — VI portfolio humanizer (reusable)
  - Idempotent: safe to re-run
  - Preserves titles, captions, tables, bibliography
  - Handles "chúng tôi" verb-specific patterns

## Commits this Phase B

- `4b63be7` — VI humanizer applied + stale refs updated
- (This commit) — CĐ DOCX rebuild + status report
