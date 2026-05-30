# Kế hoạch phản biện toàn bộ tài liệu — góc nhìn học giả IB top 1%

**Mục đích:** Phản biện adversarial toàn bộ portfolio nghiên cứu (luận án + 6 papers + 2 chuyên đề + book chapter) dưới góc độ một reviewer cấp tạp chí top IB (JIBS, GSJ, JWB, MIR, SMJ, JoM). Xác định critical gaps trước defense và journal submission.

---

## 1. Calibration: "Top 1% IB scholar review" có nghĩa là gì?

### Reviewer profile
- 15+ năm kinh nghiệm publish ở JIBS/SMJ/AMJ
- Editor hoặc Associate Editor ở 1 trong: JIBS, GSJ, JWB
- Specialty area: internationalization, emerging markets, institutions, digital transformation
- Reading speed: ~30 phút/paper cho first-pass triage; 2-3 giờ cho deep review
- Decision pattern: ~85% reject ở first round; 10% R&R; 5% accept

### Reviewer evaluation criteria (NOT "is it good enough", but "is this in top 1% of submissions?")

| Lens | Top 1% bar | Failure mode |
|---|---|---|
| **Theory** | Genuinely novel construct OR refines existing theory với boundary condition | Cite-cluster repackaging; framework collage |
| **Methodology** | Identification strategy addresses obvious endogeneity; assumptions tested | "We use OLS with HC1" without identification argument |
| **Empirics** | Effect sizes meaningful; nulls interpreted honestly; robustness across many specs | p-hacking signals; selective reporting; null spin |
| **Positioning** | Clear differentiation vs 3-5 closest prior works; not just "no one has done X in country Y" | Marginal contribution claims; geographic novelty as only hook |
| **Coherence** | Hypotheses follow from theory; results map to hypotheses; conclusion bounded by results | Theory predicts X, results show ~X, conclusion claims X |
| **Honesty** | Limitations acknowledged; failed hypotheses not reinterpreted as confirmed | Post-hoc theorizing; HARKing patterns |

---

## 2. Materials inventory (scope)

| Tier | Artifact | Lines | Priority | Status |
|---|---|---|---|---|
| **T1** | `p6/p6_meta_manuscript_en.md` (MIR submission, trimmed 11.5k word-equiv) | 490 | 🔴 P0 | Submission-ready |
| **T1** | `thesis/chuong_3_phuong_phap_vi.md` | 555 | 🔴 P0 | Defense Q3-Q4 2026 |
| **T1** | `thesis/chuong_2_tong_quan_tai_lieu_vi.md` | 270 | 🔴 P0 | Theoretical foundation |
| **T1** | `thesis/chuong_4_ket_qua_vi.md` | 312 | 🔴 P0 | Empirical results |
| **T2** | `thesis/chuong_1_gioi_thieu_vi.md` | 115 | 🟡 P1 | Sets up framing |
| **T2** | `thesis/chuong_5_ket_luan_de_xuat_vi.md` | 219 | 🟡 P1 | Synthesis claims |
| **T2** | `p3/p3_vietnam_en_clean.md` (companion paper) | 1,258 | 🟡 P1 | Primary empirics 1 |
| **T2** | `p4/p4_singapore_en_clean.md` | 373 | 🟡 P1 | Primary empirics 2 |
| **T2** | `p5/05_p5_china_design_vi.md` | 203 | 🟡 P1 | Primary empirics 3 |
| **T3** | `p7/07_p7_capstone_design_vi.md` (Đa quốc gia châu Á N=82k) | 305 | 🟢 P2 | Largest sample |
| **T3** | `p8/10_p8_pacific_sids_design_vi.md` (FIP finding) | 332 | 🟢 P2 | Boundary condition |
| **T3** | `chuyen_de/cd1/00_cd1_ctu_final_vi.md` | 1,038 | 🟢 P2 | Foundational background |
| **T3** | `chuyen_de/cd2/00_cd2_ctu_final_vi.md` | 1,162 | 🟢 P2 | Foundational background |
| **T3** | `p6/osf/P6_OSF_Preregistration_Template.md` | — | 🟢 P2 | Cross-check vs MS |
| **T4** | Book chapter (InTechOpen 2025, already published) | — | 🔵 P3 | Historical record |

Total in scope: ~6,500 lines / ~50,000 VN+EN words. Realistic deep-review effort: **40-60 hours**.

---

## 3. Review architecture (4 lenses × 4 severity grades)

### Lens 1: Theoretical contribution
- Is CIMT (Capability-Institution Mismatch Theory) genuinely new or repackaging of Khanna-Palepu + Zaheer?
- Does DPL (Digital Paradox Lifecycle) add anything beyond Brynjolfsson J-curve?
- Is "Capability-Context Mismatch" interpretation of null results post-hoc rationalization?
- Are H1-H6 systematically derived from theory or retrofitted to available moderators?

### Lens 2: Methodological rigor
- **Meta-analysis (P6):** Three-level model justification; sample independence assumption; single-coder validity threat
- **Empirics (P3-P8):** Identification strategy; selection bias (only exporters report FSTS?); panel structure exploitation
- **Variable measurement:** TCI vs DAI conceptual purity (verify no overlap); ICRV classifier choice (Rule of Law vs composite); cDAI temporal mismatch (study data-year vs DAI vintage)
- **Pre-registration alignment:** Compare actual analyses vs OSF z37kn registered protocol

### Lens 3: Empirical interpretation
- The headline finding (publication bias trim-and-fill r=.035 vs raw .074): does this undermine the entire research question?
- Frontier cell anomaly (K=3, r̄=.349): is "small-sample artifact" framing honest?
- Single-coder + no inter-coder κ: how does this affect inferential weight?
- Non-confirmation of H2, H3: is the "informative null" framing defensible or rationalization?

### Lens 4: Positioning + coherence
- Vs Marano et al. (2016): institutional moderator; what's actually new in ICRV 6-regime?
- Vs Bustamante et al. (2022): digital × institution interaction; positioning?
- Vs Wu et al. (2022): EMNE I-P meta-analysis; differentiation?
- Cumulative story across P3 (Vietnam) + P4 (Singapore) + P5 (China) + P7 (47-country) + P8 (SIDS): does it add to one coherent thesis?
- Does the dissertation answer ONE question well, or 6 questions partially?

### Severity grading

| Grade | Label | Meaning | Action |
|---|---|---|---|
| 🔴 **A** | Fatal | Reviewer at top journal will REJECT for this | MUST fix before submission |
| 🟠 **B** | Major | Major revision required at top journal | Fix before submission (high priority) |
| 🟡 **C** | Minor | Reviewer comment; not deal-breaking | Fix at revision stage |
| 🟢 **D** | Polish | Style/clarity; tonal | Optional; defense should still pass |

---

## 4. Review execution plan (4 phases)

### Phase A: Triage scan (~3-5 hours)
**All T1+T2 artifacts.** Identify top-3 fatal/major issues per artifact. Produce a 2-page triage memo per artifact:
- 1-sentence summary
- Top theoretical/methodological/empirical/positioning concerns
- Grade A-D issues identified
- Cross-reference to other artifacts where same issue appears

### Phase B: Deep review of T1 (~12-16 hours)
**P6 manuscript + 4 thesis chapters.** Full adversarial review with reviewer-style memo:
- Line-by-line critique
- Reproducibility check (where claims are testable)
- Suggested rewordings for problematic passages
- Comparison vs 3-5 closest prior works

### Phase C: Deep review of T2 (~12-16 hours)
**Thesis Ch1, Ch5 + P3, P4, P5.** Same format as Phase B.

### Phase D: Cross-cutting synthesis (~6-10 hours)
**One synthesis memo** covering:
- Theoretical coherence across the dissertation (does the umbrella theory hold?)
- Methodological consistency (do moderator coding rules match across papers?)
- Empirical narrative arc (does the cumulative story work?)
- Pre-registration alignment audit (P6 vs z37kn protocol)
- AI-generation audit (extend Chapter 3 audit to all materials)
- 3-tier recommendations: must-fix (A), should-fix (B), nice-to-have (C+D)

---

## 5. Deliverable format (per-artifact review memo)

```markdown
# Review of [artifact name]

**Reviewer perspective:** Senior IB scholar (JIBS Associate Editor calibration)
**Estimated decision at top journal:** [Reject / R&R / Accept]

## Summary in one sentence
[What the artifact claims to contribute]

## Three biggest issues

### Issue 1: [Title] — Grade A/B/C/D
**Where:** [Section / page]
**What's wrong:** [Specific gap]
**Why it matters:** [Reviewer logic]
**Fix:** [Concrete suggestion]

### Issue 2: ...
### Issue 3: ...

## By lens

### Theory
- ...

### Method
- ...

### Empirics
- ...

### Positioning
- ...

## Reproducibility check
- Are central claims testable from the deposited data/code? [yes/no/partial]
- Specific failures: ...

## AI-generation indicators
- High-confidence: [evidence]
- Medium-confidence: ...

## Recommendation
[Reject / Major revision / Minor revision / Accept] at top-tier IB journal under reviewer's working calibration.
```

---

## 6. Cross-cutting concerns (preview)

These will surface in EVERY artifact and deserve dedicated treatment in Phase D:

1. **The publication-bias headline paradox:** The trim-and-fill estimate r=.035 (vs raw .074) is the dissertation's most novel empirical finding, but it ALSO suggests that 40 years of I-P evidence (which the dissertation's theory rests on) may be inflated. Does the dissertation acknowledge this tension or talk past it?

2. **CIMT as ex-post rationalization:** "Capability-Context Mismatch" was introduced AFTER null results emerged. Reviewer Q: was this framework in the OSF pre-registration, or HARKed in?

3. **Multi-paper coherence vs salami slicing:** P3-P8 each have a "first to X" claim. A senior reviewer will ask: is this 6 contributions or 1 contribution sliced 6 ways?

4. **Frontier/SIDS underpower → "FIP" finding (P8):** P8 reports the Forced Internationalization Penalty as a major contribution on N=1,469 / 187 exporters. Top reviewer will ask: is this 187-firm finding generalizable to "SIDS as a regime", or specific to 9 surveyed Pacific countries with overlapping economic structure?

5. **Single-coder design extended through P3-P8:** Limitation acknowledged in P6 but does it propagate consistently to other papers' methodology sections?

6. **AI-tell pattern from Chapter 3:** "Cơ sở kế thừa / Đóng góp mới" template appears verbatim in CĐ2 sections — is this consistent author template or repeated AI-prompt structure?

7. **WBES item-code mismatches across papers:** Vietnam uses c22b only (Tier-1); Singapore uses c22b+k33+k38 (Tier-1+2); China uses c22b only. Same construct (DAI) measured differently across papers. Is this disclosed honestly or framed as adaptation?

8. **Pre-registration alignment (OSF z37kn):** What % of reported analyses are AS-REGISTERED vs deviations? Are deviations explicit (Section 3.1 of MS does have 4 deviations) — but are there UNDISCLOSED deviations?

---

## 7. Effort + timing options

| Option | Scope | Effort | Deliverable |
|---|---|---|---|
| **Lite** | T1 triage only (Phase A on 4 artifacts) | ~4 hours | 4 triage memos |
| **Standard** | T1 deep (Phase B) | ~16 hours | 4 deep memos |
| **Comprehensive** | T1+T2 deep + synthesis (B+C+D) | ~30-40 hours | 9 deep memos + synthesis |
| **Exhaustive** | All T1-T4 + cross-cutting + AI audit | ~50-60 hours | 12 deep memos + synthesis + AI report |

Note on effort: tôi (Claude) làm song song hơn so với 1 human reviewer, nên realistic clock time là **1/4 effort** ước tính (e.g., "Standard" = ~4 hours session). Mức effort trên là "reviewer-hour equivalent" cho calibration.

---

## 8. Khuyến nghị

Đề xuất bắt đầu bằng **Option "Standard"** (T1 deep review = P6 MS + 4 thesis chapters), vì:
- T1 là các materials có stakes cao nhất (MIR submission + dissertation defense)
- 4 deep memos cho cảm nhận đầy đủ về depth of critique
- Sau Standard, có thể quyết định mở rộng sang T2 hoặc dừng

Trong phần tiếp theo, tôi sẽ **thực hiện 1 sample review** (P6 manuscript hoặc Chapter 2 — bạn chọn) để bạn xem format thực tế trước khi commit Option nào.
