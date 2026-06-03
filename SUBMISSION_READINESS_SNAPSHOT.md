# Submission Readiness Snapshot — Portfolio 7 Papers + Dissertation

**Last refreshed:** 2026-06-03 (post commit `0e9a0e0`)
**Branch:** `claude/vietnamese-academic-standards-QuiLM` (PR #12)
**Triggering session:** finalization — 12+ commits resolving 6 strategic groups

This is the **one-page dashboard**. For details: `thesis/PROJECT_SELF_CRITIQUE.md` · `.github/PR_REVIEW_CHECKLIST.md` · `docs/adr/`.

---

## 1. 7-paper portfolio status

| # | Paper | Target | Words | Cap | Buffer | Blind | DOCX | Status |
|---|---|---|---:|---:|---:|:-:|:-:|:-:|
| P3 | Vietnam | JED (Emerald) | 11,597 | 12,000 | -403 | ✅ 0/11 | 1.6 MB | ✅ READY |
| P4 | Singapore | JABES (Emerald) | 12,096 | 12,500 | -404 | ✅ 0/11 | 0.6 MB | ✅ READY |
| P5 | China | IJOEM (Emerald) | 7,238 | 10,000 | -2,762 | ✅ 0/11 | 0.8 MB | ✅ READY |
| P6 | Meta-analysis | APJM (Springer) | 11,384 | 12,000 | -616 | ✅ 0/11 | 1.8 MB | ✅ READY |
| P7 | Capstone | JIBS | 12,085 | 13,000 | -915 | ✅ 0/11 | 0.6 MB | ✅ READY |
| P8 | SIDS | JED (Emerald) | 8,784 | 9,000 | -216 | ✅ 0/11 | 36 KB ¹ | ✅ READY |
| P9' | India | MIR (Springer) | 8,424 | 10,000 | -1,576 | ✅ 0/11 | 33 KB ² | ⚠ figs |

¹ P8 has no figures by design (4 robustness panels are text + tables only).
² P9' references Figures 1-4 as placeholders; NCS needs to render the 4 PNGs before submission.

**Recommended submission order:** P5 → P9' → P3 → P8 → P4 → P6 → P7 (cleanest/fastest first; JIBS last leveraging earlier acceptance signals).

---

## 2. Theoretical hierarchy integrity (CIMT–ICRV–CDCM)

| Artifact | CIMT mentions | Status |
|---|:-:|:-:|
| `thesis/chuong_2_tong_quan_tai_lieu_vi.md` §2.5 | 15 | ✅ umbrella defined here |
| `thesis/chuong_5_ket_luan_de_xuat_vi.md` §5.1/5.3 | 7 | ✅ discussion + contributions |
| `thesis/tom_tat_noi_dung_vi.md` | 9 | ✅ dissertation summary |
| `thesis/cumulative_argument_summary.md` | 2 | ✅ portfolio narrative |
| `thesis/defense_qa_preparation.md` Q2.1 | 4 | ✅ defense-ready answer |
| `thesis/02_theoretical_framework_vi.md` (CĐ2) | 4 | ✅ §1 + new §3.5 |
| `thesis/14_cd1_part1_intro_theory_vi.md` (CĐ1) | 1 | ✅ §2.7 cross-ref |
| `thesis/16_cd1_part3_cases_conclusion_vi.md` (CĐ1) | 1 | ✅ §7.3.1 cross-ref |
| `thesis/chuong_1_gioi_thieu_vi.md` §1.6.1 | 1 | ✅ contribution #1 |
| `p6/p6_meta_manuscript_en.md` §2.2 | 3 | ✅ middle-range framing |
| `p7/p7_capstone_en_clean.md` §2.1/abstract/keywords/§5.1 | 4 | ✅ CIMT named |
| `p6/submission/apjm_package/03_cover_letter.md` | 1 | ✅ contribution #1 |
| `thesis/04_references_apa7.md` Merton/Whetten/Corley-Gioia | 2 | ✅ anchors |
| M-AIDA description v2.1 | 4 | ✅ moderator schema mapped |
| `dist/SUBMISSION_FINAL/README.md` | 1 | ✅ portfolio framing |

**15/15 anchor artifacts consistently name the CIMT–ICRV–CDCM layered framework.**

---

## 3. PROJECT_SELF_CRITIQUE — 10-group status

| Group | Issue | Status | Resolved by |
|---|---|:-:|---|
| A | Foundational (associational design) | ⚪ | cannot fix in container; disclosed |
| B | Theoretical coherence | 🟢 | commit `32315c5` |
| C | Self-citation + dual-pub | 🟢 | commit `943e793` |
| D | Documentation drift | 🟢 | commit `b262f56` |
| E | Replication fragmentation (Stata) | ⚪ | NCS-side local exec |
| F | OSF Path B (k ≈ 600–700) | ⚪ | post-submission follow-up |
| G | Word-count overruns | 🟢 | commit `0bb9619` |
| H | Process critique | 🟢 | documented |
| I | Strategic positioning | 🟢 | commit `0e9a0e0` |
| J | What cannot be fixed remotely | ⚪ | NCS-side (κ + AI-detector) |

**6/10 RESOLVED · 4 NCS-side (genuine external dependencies).**

---

## 4. Quality gates — final verification

| Check | Command | Result |
|---|---|:-:|
| Numerical consistency (65 files) | `python3 scripts/check-consistency.py` | ✅ 0 issues |
| Em-dash count in new §2.5 inserts | `awk 'NR>=196 && NR<=246' \| grep -c "—"` | ✅ 0 |
| Em-dash count in P7 (post-trim) | `grep -c "—" p7/p7_capstone_en_clean.md` | ✅ 1 (figure caption only) |
| ICBEF 2025 leak in blinded P6 | `grep -c ICBEF p6/p6_meta_manuscript_en.md` | ✅ 0 |
| Blind-compliance scan (7 papers × 11 patterns) | python zipfile audit | ✅ 0/77 hits |
| Word-count buffers ≥ 200w per paper | per-paper `wc -w` vs cap | ✅ all pass |
| Submission bundle completeness (7 papers × 4 files) | bash file-existence | ✅ 28/28 present |
| Figures embedded in DOCX where applicable | DOCX size > 200 KB | ✅ 5/5 papers w/ figures |

---

## 5. NCS-side outstanding (cannot be done in container)

| Item | Required for | Estimated effort |
|---|---|---|
| Render P9' Figures 1–4 (PNG @ 300 DPI) | P9' MIR submission | 1–2 hours |
| Fill 6 `[TO FILL]` fields in `thesis/supplement_s_maida_vi.md` | P6 APJM submission + defense | 30 min (data already exists in log) |
| Run Stata `.do` files in `p7/replication/do/` + `p8/replication/do/` locally | replication-package audit-trail | 1 hour |
| Recruit 2nd coder + compute κ for P6 PRISMA Item 9 | P6 APJM revision (if requested) | post-submission |
| Submit OSF Path B (k ≈ 600–700) formal-search expansion | follow-up replication | post-defense |
| Run AI-detector battery (Originality.ai / GPTZero) on all 7 papers | due-diligence | 1 hour |
| Fill personal CCCD/DOB/address in M-AIDA copyright forms | M-AIDA submission to COV | 15 min |
| Resolve PR #12 `mergeable_state=dirty` (git merge main) | merge to main | 30 min |

---

## 6. Recommended next action

1. **NCS local verification (1 day):** Open P9' MIR package + render Figures 1–4. Fill supplement_s_maida [TO FILL] from M-AIDA log. Run Stata `.do` files locally.
2. **Run AI-detector battery (1 hour):** Sanity-check all 7 papers against Originality.ai or equivalent before submission.
3. **Submit cleanest paper first (P5 → IJOEM, ~3–4 month cycle).** Wait for desk-not-rejected signal before submitting P7 to JIBS.
4. **PR #12 merge:** After 1-3 done, resolve `mergeable_state=dirty` via `git merge main`, un-draft PR, merge to main.

---

*Auto-generated from repo state at commit `0e9a0e0`. Re-run on each finalization session.*
