# PR review checklist — `claude/vietnamese-academic-standards-QuiLM` → `main`

Targeted at **PR #12** (long-running finalization branch, currently 362 commits / 933 files ahead of `main`). Use this checklist before clicking "Ready for review" / un-drafting / merging.

Last updated: 2026-06-03 after commit `6f716b4` (CIMT–ICRV–CDCM hierarchy installed).

---

## 0. Pre-merge sanity (mechanical, must all be green)

| Check | Command | Expected | Status |
|---|---|---|---|
| Numerical consistency | `python3 scripts/check-consistency.py` | 0 inconsistencies across 65 files | ☐ |
| APA7 reference formatting | `python3 scripts/format-apa7.py --paper p3/p3_vietnam_en_clean.md` (and p4–p8) | clean for all 7 papers | ☐ |
| Blinded-DOCX scan — author-identifier leaks | `python3 scripts/scan_blind_compliance.py dist/SUBMISSION_FINAL/P*/01_manuscript_blinded.docx` (or equivalent) | 0 hits on `thuyhuongctu`, `huongctu`, `Do Thuy Huong`, `Đỗ Thùy`, `Phan Anh Tú`, `Phan Anh Tu`, `patu@ctu`, `Can Tho University`, `VLUTE`, `huongdt@vlute` | ☐ |
| Em-dash / en-dash scan in newly-added §2.5 | `awk 'NR>=196 && NR<=246' thesis/chuong_2_tong_quan_tai_lieu_vi.md \| grep -c "—"` | 0 em dashes (en dashes acceptable inside compound proper nouns only) | ☐ |
| Word-count caps respected per journal | manual count per paper file | P3 ≤ 12 000 (APJM/JED), P4 ≤ 12 500 (JABES), P5 ≤ 10 000 (IJOEM), P6 ≤ 12 000 (APJM), P7 ≤ 14 000 (JIBS), P8 ≤ 9 000 (JED), P9' ≤ 9 000 (MIR) | ☐ |
| Submission bundles structurally complete | `ls dist/SUBMISSION_FINAL/P*_*/` | each folder has 01_manuscript_blinded.docx + 02_title_page.docx + 03_cover_letter.docx + figures/ + README.md | ☐ |

---

## 1. Theoretical-framework integrity (post-CIMT restoration)

Following the CIMT-restoration cycle (commits `374e443` → `a3cae9f` → `32315c5` → `3f23b1d`), verify the layered hierarchy is consistent across all artifacts.

| Artifact | Expected framing | Verify |
|---|---|---|
| `thesis/chuong_2_tong_quan_tai_lieu_vi.md` §2.5.1–2.5.4 | CIMT umbrella · ICRV taxonomy · CDCM signature | grep `2.5.1 CIMT`, `2.5.2 ICRV`, `2.5.3 CDCM`, `2.5.4 Cấu trúc phân tầng` |
| `thesis/chuong_5_ket_luan_de_xuat_vi.md` §5.1 + §5.3 | layered framework named in chapter intro; §5.3 leads with CIMT as Contribution #1 | grep `CIMT–ICRV–CDCM` |
| `thesis/tom_tat_noi_dung_vi.md` "Các lý thuyết nền" section | retitled to layered framework with 3-layer block | grep `khung lý thuyết phân tầng CIMT` |
| `thesis/cumulative_argument_summary.md` Predictions 1–2 | CDCM positioned as observable signature of CIMT | grep `CDCM signature of CIMT` |
| `thesis/defense_qa_preparation.md` Q2.1 | Merton 1968 + Whetten 1989 + Corley & Gioia 2011 cited; layered hierarchy spelled out | manual read |
| `p6/p6_meta_manuscript_en.md` §2.2 | section title = "Capability–Institution Mismatch Theory (CIMT): A Middle-Range Integrative Framework" | grep `Capability–Institution Mismatch Theory (CIMT)` |
| `p7/p7_capstone_en_clean.md` §2.1 + abstract + keywords + §5.1 | CIMT named in all four locations | grep `Capability–Institution Mismatch Theory (CIMT)` |
| `p6/submission/apjm_package/03_cover_letter.md` | Contribution #1 = "first three-level meta-analytic test of CIMT" | grep `Capability–Institution Mismatch Theory (CIMT)` |
| `thesis/04_references_apa7.md` | Merton (1968), Whetten (1989), Corley & Gioia (2011) present in Section A | grep `Merton, R\.` + `Whetten, D\.` + `Corley, K\.` |
| `dist/SUBMISSION_FINAL/README.md` | P6+P7 description references CIMT layered hierarchy | grep `CIMT = mechanism` |

**Trigger:** if any of the 10 rows above fails, do **not** un-draft the PR — sync first.

---

## 2. Submission-readiness per paper

Each paper in `dist/SUBMISSION_FINAL/P{n}_*/` must independently pass.

### P3 Vietnam → JED (Q1, Emerald)
- [ ] 01_manuscript_blinded.docx ≤ 12 000 words
- [ ] 0 author-identifier hits in blinded DOCX
- [ ] Cover letter addresses JED EiC + journal name correctly
- [ ] Figures @ 300 DPI present
- [ ] Online appendix (panel robustness) linked

### P4 Singapore → JABES (Q1, Emerald)
- [ ] Word count ≤ 12 500
- [ ] Heckman §3.3 disclosure intact (no exclusion restriction → OLS primary, IMR sensitivity)
- [ ] Blinded ✓

### P5 China → IJOEM (Q1, Emerald)
- [ ] Word count ≤ 10 000 (currently 9 491 per PR body)
- [ ] **Zero `apjm` / `APJM` references** in p5 source/build/DOCX (per dedicated cleanup commits)
- [ ] Blinded ✓

### P6 Meta-analysis → APJM (Q1 ABS-3, Springer Nature)
- [ ] §2.2 names CIMT explicitly with Merton/Whetten/Corley-Gioia anchors
- [ ] OSF preregistration link present (https://osf.io/z37kn, DOI 10.17605/OSF.IO/Z37KN)
- [ ] PRISMA Item 9 single-coder deviation disclosed (Reconciliation Notes Issue #7)
- [ ] Schwens 2018 ref decision recorded (Reconciliation Notes Issue #8 — verify or remove from "5 anchor meta-analyses" list)
- [ ] Cover letter targets APJM EiC + journal name + ABS-3 framing

### P7 Capstone → JIBS (ABS-4*)
- [ ] §2.1 + abstract + keywords + §5.1 all CIMT-named
- [ ] DAI×ICRV β = +0.052 / p = .049 / SE = 0.0266 verified from `p7_coefs_all_models.csv` M11 row
- [ ] Sample-attrition diagnostic (§3.5) present
- [ ] Cluster-SE robustness (§4.9) present
- [ ] Conceptual figures 1 + 2 embedded (DOCX size > 500 KB confirms embedding)

### P8 SIDS → JED (Q1, parallel submission with P3)
- [ ] 4 robustness panels present (Comoros excl., wild cluster bootstrap, LOO, attrition)
- [ ] R authoritative scripts in `p8/replication/do/`
- [ ] Word count ≤ 9 000
- [ ] Blinded ✓

### P9' India → MIR or IJOEM
- [ ] UPI quasi-experiment §3 self-contained, no book-chapter cross-cite
- [ ] Sample-relationship to forthcoming book chapter disclosed in §3
- [ ] Blinded ✓

---

## 3. Dissertation chapters (Vietnamese, CTU dossier)

| File | DOCX rebuilt this session? | Manual read needed? |
|---|---|---|
| `chuong_1_gioi_thieu.docx` | No (untouched) | optional |
| `chuong_2_tong_quan_tai_lieu.docx` | ✅ commit `6f716b4` (486 KB, Hình 2.1 embedded, §2.5.1–2.5.4 new) | **Required** — committee read-through of §2.5 |
| `chuong_3_phuong_phap.docx` | No | optional |
| `chuong_4_ket_qua.docx` | ✅ commit `6f716b4` (cosmetic) | optional |
| `chuong_5_ket_luan_de_xuat.docx` | ✅ commit `6f716b4` (§5.1 + §5.3 retitled, CIMT-umbrella framing) | **Required** — verify §5.1 + §5.3 flow |
| `tom_tat_noi_dung_vi.docx` | ✅ commit `6f716b4` (new file) | **Required** — verify CIMT layered description |

---

## 4. Outstanding non-blocking items (acceptable to defer)

These are documented in `thesis/PROJECT_SELF_CRITIQUE.md` and `thesis/OUTSTANDING_ISSUES.md`. They do **not** block PR merge but **do** require disclosure to the dissertation committee:

- [ ] **P6 single-coder κ** (PROJECT_SELF_CRITIQUE Group A.2) — disclose as pre-reg deviation; recruit 2nd coder post-defense for replication
- [ ] **P7 Advanced_resource regime dropped from M11** (Group A.3) — already disclosed in §3.5 + §5.6; verify language consistent
- [ ] **OSF z37kn Path B (k ≈ 600–700 expansion)** (Group F) — pre-registered as follow-up, undelivered this session
- [ ] **P4 word overrun +96 / P7 overrun +795** (Group G) — verify against current files (`wc -w`)
- [ ] **CĐ1 / CĐ2 cross-reference to Ch.2 §2.5** (Group D) — chuyên đề are independent specialised contributions; cross-ref optional
- [ ] **Stata `.do` files for P7 cluster-SE + P8 robustness never executed** in this container (Group J) — NCS to run locally on actual Stata before submission

---

## 5. Merge-safety checks

| Risk gate | Verify | Status |
|---|---|---|
| **`mergeable_state` is `dirty`** (per PR #12 metadata) | resolve conflicts with `main` via `git merge main` on the branch, then re-push | ☐ |
| Force-push to `main` requested? | **No** — never force-push to main per `git push` rule | ☑ N/A |
| Hooks disabled? | **No** — no `--no-verify` flags used | ☑ N/A |
| Test artifacts present? | dist/SUBMISSION_FINAL/ + dist/HO_SO_NOP/ committed | ☐ |
| Sensitive data in branch? | `.env`, credentials, personal CCCD — none should be present | ☐ scan |
| Dependabot vulnerabilities | 25 high / 23 moderate / 2 low on `main` (per push output) — not introduced by this PR | ☑ pre-existing |

---

## 6. Sign-off

By checking all boxes above, the merger confirms:
- All mechanical checks (Section 0) are green
- Theoretical-framework integrity (Section 1) is intact across 10 named artifacts
- All 7 papers have submission packages in `dist/SUBMISSION_FINAL/`
- Dissertation chapters 2/4/5 DOCX rebuilt with CIMT framing
- Outstanding items (Section 4) are acknowledged and disclosed; not silent gaps
- Merge conflict with `main` resolved (Section 5)

**Reviewer:** _______________ · **Date:** _______________ · **Merged commit:** _______________

---

## Appendix — Useful one-liners

```bash
# Quick pre-merge audit
python3 scripts/check-consistency.py && \
grep -rcE "thuyhuongctu|huongdt@vlute|Phan Anh Tú|Can Tho University|VLUTE" dist/SUBMISSION_FINAL/P*/01_manuscript_blinded.docx 2>/dev/null

# Verify CIMT layered hierarchy is named in all 10 anchor files
for f in thesis/chuong_2_tong_quan_tai_lieu_vi.md thesis/chuong_5_ket_luan_de_xuat_vi.md \
         thesis/tom_tat_noi_dung_vi.md thesis/cumulative_argument_summary.md \
         thesis/defense_qa_preparation.md p6/p6_meta_manuscript_en.md \
         p7/p7_capstone_en_clean.md p6/submission/apjm_package/03_cover_letter.md \
         thesis/04_references_apa7.md dist/SUBMISSION_FINAL/README.md; do
  hit=$(grep -c "CIMT" "$f"); echo "${f}: ${hit} hits"; done

# Count em-dashes in newly-inserted §2.5 (must be 0)
awk 'NR>=196 && NR<=246' thesis/chuong_2_tong_quan_tai_lieu_vi.md | grep -c "—"

# Rebuild dissertation DOCX from .md
pandoc thesis/chuong_2_tong_quan_tai_lieu_vi.md \
  -o thesis/chuong_2_tong_quan_tai_lieu_vi.docx \
  --reference-doc=templates/ctu_thesis_reference.docx

# Resolve merge conflict with main before un-drafting
git fetch origin main
git merge origin/main   # resolve conflicts, commit
git push origin claude/vietnamese-academic-standards-QuiLM
```
