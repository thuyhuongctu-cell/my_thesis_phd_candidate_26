# Adversarial Review: P6 Manuscript (MIR submission, v1.2)

> **Reviewer perspective:** Senior IB scholar, JIBS/GSJ Associate Editor calibration. ~150 prior reviews at top-3 IB outlets. Methodological strength: meta-analysis + multilevel models.
>
> **Working calibration for decision:** What would I write to the action editor at MIR?
>
> **Estimated decision at top-tier outlet:** **Reject (Major) → R&R at MIR (Q2) IF specific issues addressed**

---

## Summary in one sentence

A pre-registered three-level meta-analysis of the 40-year I-P literature that fails to confirm its three hypothesized moderators (ICRV regime, cDAI, DPL phase) but documents a 53% publication-bias attenuation of the pooled effect (r = .074 → .035); the paper's central finding ends up being one it did not set out to test.

---

## Three biggest issues

### Issue 1: The headline contribution undermines the research question — Grade A

**Where:** Sections 4.6, 5.2 Contribution 3, 6 Conclusion.

**What's wrong:** The most novel empirical finding is that the I-P literature has substantial publication-bias inflation: trim-and-fill imputes *k* = 58 missing studies, dropping the pooled effect from *r* = .074 to *r* = .035 — a 53% attenuation. The paper presents this as a "corrective contribution". But this finding implies that **the literature on which the paper's theory rests (Lu & Beamish, Marano et al., Wu et al.) is materially inflated**, which means the entire theoretical motivation for testing institutional/digital moderators (which assumes a real, sizeable I-P effect that contexts modulate) is on shakier ground than the paper admits. If the population effect is *r* = .035 (Cohen's small floor = .10), is "the I-P relationship" even a meaningful object to moderate? The discussion sidesteps this by treating publication bias as a separable finding.

**Why it matters:** A top-tier reviewer will not let this paradox stand. The paper either (i) defends the moderator project as still meaningful at *r* = .035, OR (ii) reframes itself as primarily a publication-bias audit, OR (iii) raises the question and disclaims it. The current draft does (iii) tacitly but never explicitly.

**Fix:** Add a paragraph in §5 (probably end of §5.2) explicitly addressing the tension: "The publication-bias correction raises a methodological question about the scale of the underlying effect that this paper's moderator project assumes. If the population effect is closer to *r* = .035, between-study moderator detection requires substantially larger *k* than presented here to achieve adequate power. We interpret our moderator nulls in light of both this power constraint and the bias-correction; future replications should pre-specify minimum-detectable-effect-size targets calibrated to the *r* ≈ .035 anchor rather than the inflated *r* ≈ .07 anchor." This admission strengthens, rather than weakens, the paper.

### Issue 2: "Capability–Context Mismatch" is presented as a contribution but is post-hoc — Grade A

**Where:** Introduction §47 ("Capability–Context Mismatch interpretation"), §2.4 cDAI as Amplifier, Conclusion §364.

**What's wrong:** The Introduction frames Capability–Context Mismatch (CCM) as a theoretical interpretation that the moderator nulls *motivate*: "a macro digital context is inert for I-P unless matched by firm-level digital capability." This is **introduced after observing the nulls**. CCM was not in the OSF pre-registration (verify against z37kn); it is not derived in §2 before the hypotheses; it is offered to rescue the null cDAI result.

This is the textbook HARKing pattern: Hypothesizing After Results Known. A JIBS reviewer will flag it instantly. The fact that the introduction openly states CCM emerges from the non-confirmation of H3 makes it worse, not better — it acknowledges the post-hoc nature rather than concealing it.

**Why it matters:** Top journals (JIBS, SMJ, AMJ) have explicit anti-HARKing policies. Even MIR/GSJ reviewers will flag it. The paper currently *announces* HARKing as if it were a feature.

**Fix:** Three options, in order of editorial cost:
- **Cheapest:** Reframe CCM as a *Discussion-section interpretive proposition* rather than a "theoretical interpretation" introduced in §1. Move all CCM mentions out of Introduction and into §5.2 as a "future-research-worthy proposition consistent with the observed nulls". State explicitly: "This proposition was developed post-hoc and requires confirmatory testing."
- **Middle:** Drop CCM entirely; let the nulls stand on their own as informative bounds.
- **Most ambitious:** Pre-register CCM as a separate study and run a confirmatory test on Path B's expansion corpus before submitting this paper.

### Issue 3: cDAI temporal validity — construct invalid for half the corpus — Grade A

**Where:** §2.4, §3.4 Moderator coding protocol (item 6), §4.4.

**What's wrong:** cDAI is assigned to each study via "country-year following the dominant data period of each study". Source: World Bank DAI (2016 vintage, single year) extended via ITU Digital Development Index (2017+). The corpus spans **1977–2026**. For studies with data periods before 2010 (and Table 4.1 shows DPL Precede *K* = 100; 35% of corpus), cDAI is being assigned scores from a construct that did not meaningfully exist at the time of the data. A 1995 Indonesian SME sample is assigned a 2016 DAI score, projected backwards through 21 years of digital transformation. This is **construct anachronism**.

The paper never confronts this. The cDAI null result (Q_M = 1.23, p = .541) may be entirely attributable to noise from this back-projection. Worse, the paper then uses the null to motivate CCM (Issue 2) — building theory on a construct that does not validly apply to a large fraction of the data.

**Why it matters:** Construct validity threats this large are first-round-reject territory at top journals. Even at MIR, a reviewer with digital-transformation expertise will catch this.

**Fix:** Two-part:
- **Methodological:** Restrict cDAI moderation analysis to Span + Follow studies (DPL > 2008; *K* ≈ 188) where cDAI's construct domain is at least temporally co-located. Report the restricted analysis as the primary cDAI test; report full-sample as sensitivity. The Q_M may remain non-significant — but the inference will be on construct-valid data.
- **Discursive:** Add a Limitation explicitly recognizing that cDAI back-projection introduces measurement error proportional to the gap between data-year and 2016 vintage; cite this as a reason cDAI moderation may be detectable only in post-2010 sub-samples.

---

## Detailed critique by lens

### Theory

**Adequacies.**
- Foundation theories (RBV, institutional, learning, coordination cost, digital transformation hierarchy) appropriately invoked.
- ICRV taxonomy linked to WGI Rule of Law with explicit cutoffs — operationally precise.
- DPL anchored at 2009 with three concrete empirical anchors (smartphone diffusion; B2B platform launches; 2009 crisis SME adoption) — defensible cut.

**Concerns.**
- **CIMT vs Khanna-Palepu vs Zaheer:** The three CIMT mechanisms (rent protection, LOF attenuation, void amplification) are direct restatements of Kogut-Zander 1993, Zaheer 1995, Khanna-Palepu 2010. The paper says CIMT "explains the ICRV gradient" but the gradient prediction is already in Marano et al. (2016). What CIMT adds is unclear; reviewer will ask: "What does CIMT predict that the parent theories don't?" Recommend: drop CIMT label OR add a CIMT-specific testable prediction that parent theories don't make.
- **"Globally representative" framing:** §1 claims "globally representative corpus". Table 4.1 shows ICRV-I = 139/288 (48%); Frontier = 3 (1%); SIDS = 0. This is Advanced-economy-dominated, not globally representative. Top reviewer will spot this. Reframe as "geographically diverse with skew toward Advanced-economy literature".
- **Three-level model interpretation overreach:** §4.2 ("Most unexplained heterogeneity therefore arises from analytic choices within primary studies, not from stable cross-country contextual differences") is a sharp interpretation. But within-study variance (76.1%) >> between-study (11.8%) could equally mean (a) primary studies are heterogeneous in design, OR (b) the included studies in the same paper actually reflect different populations/sub-samples that the meta-analyst is treating as nested. The paper picks (a) without considering (b).

### Method

**Adequacies.**
- Pre-registration on OSF z37kn before extraction — strong practice.
- 4 disclosed deviations from pre-registration in §3.1 — also strong.
- Three-level model with REML in `metafor` v4 — appropriate tool choice.
- Independent Python cross-check (`verify_moderator_qm.py`) for moderator Q_M — exemplary.
- Drop-Frontier sensitivity is the right diagnostic.

**Concerns.**
- **Independence assumption:** Three-level MARA assumes effects within studies are exchangeable. But multi-effect studies typically share country, year, sample frame, controls — the residual independence between within-study effects is weaker than the model assumes. **Robust Variance Estimation (RVE)** is the standard remedy (Hedges, Tipton, Johnson 2010); the paper doesn't use it. Recommend: add RVE as a sensitivity check; report cluster-robust SEs alongside three-level estimates.
- **Compound-symmetric within-study covariance:** §3.5 states this but doesn't justify against alternatives (autoregressive, unstructured). For studies reporting effects across different DOI measures (FSTS + entropy) on the same sample, exchangeability is a strong assumption. Add 1-2 sentences justifying.
- **Single-coder design:** Disclosed honestly. But "pilot calibration + double-entry verification" defenses are weak. Pilot calibration on 10 studies does not substitute for inter-coder κ on the analysed corpus. Double-entry by the same coder is not independent re-extraction. Recommend: acknowledge the limitation more directly OR (much better) commission a 20-30 paper inter-coder check before final submission. *(See thesis Supplement S-MAIDA workspace for execution scaffold.)*
- **PET-PEESE mentioned but not reported (§3.6, §4.6):** PET-PEESE is mentioned as "additionally applied" but no PET-PEESE results appear. Either drop the mention or add the table. Selective application of bias-correction tests is itself a publication-bias smell.
- **Trim-and-fill over-correction risk:** Trim-and-fill is known to over-correct in high-heterogeneity settings (Terrin et al. 2003; Duval 2005). I² = 87.8% here. The 53% attenuation may be an upper bound, not the central estimate. Add Vevea-Woods weight-function model or selection model as a second bias-correction.

### Empirics

**Adequacies.**
- ICRV regime forest plot (Figure 2) clear; CIs honest.
- Drop-Frontier sensitivity (Q_M = 1.49 vs 17.35) reported transparently.
- Leave-one-out range [0.071, 0.075] tight and reported.
- Funnel plot (Figure 4) shows the asymmetry honestly.
- Year-distribution figure (Figure 6) added per prior review — good response.

**Concerns.**
- **The Frontier-cell carrying H1 framing:** §4.3 leads with Q_M = 17.35, p = .002; only after the table reveals the FR anomaly does the drop-Frontier test appear. Reverse the order: lead with drop-Frontier Q_M = 1.49 as the primary interpretation, present full-sample Q_M = 17.35 as artifact-of-FR-cell. This frames the honest finding first.
- **Effect-size practical magnitude:** *r* = .074 raw, *r* = .035 corrected. Cohen's (1988) "small" floor = .10. Both estimates are below Cohen's small. The paper treats them as "small but consistent positive". A reviewer with effect-size literacy will note that this is sub-Cohen-small territory and ask whether substantive conclusions about "the I-P relationship" are warranted at this scale.
- **Self-citation in Discussion §5.1:** "Do & Phan (2025) document a negative aggregate DOI coefficient on 380 Indian WBES firms" — the paper uses its own author's separate primary study to corroborate CIMT. This is circular: same author tests same theory in two outlets and cross-confirms. Top reviewer will require disclosure that Do & Phan (2025) is the same author group testing a related question; preferably remove this passage or note circularity.
- **The "Forced-penalty hypothesis" reference (§5.4(a)(1)):** Cited as if external literature, but it appears to be P8's contribution (per `p8/10_p8_pacific_sids_design_vi.md`). If the same author group is anchoring P6's SIDS Limitation on P8's finding, disclose. Top reviewer can trace this through co-authorship.

### Positioning

**Adequacies.**
- Anchor MA citations (Bausch & Krist; Kirca et al.; Marano et al.; Schwens et al.; Wu et al.; Arte & Larimo) cover the field.
- Bustamante et al. (2022) cited as closest prior — appropriate.
- Three "first to" methodological claims (three-level MARA, PRISMA + OSF, within/between decomposition) — defensible if narrowly scoped.

**Concerns.**
- **Vs Marano et al. (2016):** Marano had k=359 and reported significant institutional moderation. Current paper has k=238 and reports non-robust ICRV moderation. The paper frames this as "Marano's classification was coarse"; reviewer asks: "Did your finer classification produce more or less informative inference?" The honest answer is less. Reframe: ICRV taxonomy is *qualitatively* finer (six regimes resolve frontier/SIDS); finding non-robust moderation does not falsify Marano's finding because the samples differ.
- **Vs Bustamante et al. (2022):** Cited as cross-country firm-level cDAI × institution interaction. Current paper tests cDAI × ICRV at *meta-analytic* level. These are different analytic levels — firm-level interaction does not necessarily aggregate to study-level interaction. The paper's claim that it "tests the meta-analytic extension" of Bustamante elides the level-of-analysis problem. Reframe as "different question at different level".
- **Multiple "first to" claims:** Three methodological + three theoretical = six "firsts" for one paper. Top reviewer will trim to 2-3 substantive firsts and ask for the rest as incremental refinements.

### Honesty about nulls

**Strengths:** The paper does NOT spin the moderator nulls as confirmed. The Conclusion explicitly states H1 (fragile), H2 (not supported), H3 (not supported). This is to the paper's credit and unusual in the literature.

**Weakness:** The CCM rescue (Issue 2) partially undoes this honesty. Pure null reporting + CCM as Discussion proposition (not Introduction theory) would be cleaner.

---

## Reproducibility check

- **OSF z37kn deposit cited.** Tested: as of audit, the deposit contains the pre-registration but the data + code may not yet be uploaded. **Reviewer will click the link**; must be populated BEFORE submission.
- **PRISMA 2020 trace claimed in Supp-A.** Two-path design is now clearly documented; this is good.
- **Replication script `verify_moderator_qm.py`** referenced. Should be deposited in `03_code/` on OSF along with metafor R scripts.
- **`p6_study_database.csv`** is the canonical analyzed corpus. Currently in repo; must be on OSF.
- **Gold-standard validation report** referenced in thesis Supp-S-MAIDA but not in the MS itself. If the MS cites OSF reproducibility, a reviewer will expect to see validation evidence at the link.

**Action:** OSF deposit must be complete and populated before MIR submission. Per existing `prisma_extraction_pipeline_status.md`, this is in the user's queue.

---

## AI-generation indicators

Lower than Chapter 3 of the thesis (where the M-AIDA section was a clear AI-tell). Specific signals:

- **Medium-confidence:** Discussion §5.2 contribution claims (Contribution 1/2/3) follow a tight AI-template: "first to X | result | bound by Y". Real reviewers expect more synthesis between contributions.
- **Low-confidence:** The "globally representative corpus" framing repeated in Introduction, Theory, Discussion, Conclusion — AI-tells repeat keywords across sections; human authors vary.
- **Low-confidence:** "informative bounds" appears 3+ times — boilerplate hedging.
- **Negative evidence (against AI):** Real numerical results, real WBES integration, real ICRV codings, real pre-registration deviations. The empirical scaffolding is human.

Bottom line: the manuscript was likely AI-assisted in *drafting* (especially Discussion/Conclusion) but human-driven in *empirics and structure*. This is not disqualifying — most top journals tolerate AI-assisted drafting if (a) the empirical work is human and (b) the AI use is disclosed (per Emerald and Springer policy). The MS already discloses this in the title page (`Use of Generative AI in the Writing Process`). Adequate.

---

## Pre-registration alignment audit (preliminary)

The MS discloses 4 deviations from z37kn pre-registration (§3.1):
1. ICRV re-specified to WGI Rule of Law + MX category — ✅ disclosed
2. DPL re-specified to data-period bins — ✅ disclosed
3. Publication bias upgraded to labeled hypothesis H4 — ✅ disclosed
4. Inter-coder reliability protocol not executed — ✅ disclosed

**Possible undisclosed deviations** (will require user to audit by reading z37kn document):
- Was CIMT (capability-institution mismatch) pre-registered as a theoretical lens? If introduced post-hoc, this is a 5th deviation requiring disclosure.
- Was Capability–Context Mismatch (CCM) interpretation pre-registered? Same question.
- Drop-Frontier sensitivity test: pre-registered or post-hoc reaction to FR anomaly?
- 32-paper gold-standard evaluation plan: pre-registered or added later?

**Action:** Read z37kn carefully; either confirm CIMT/CCM/drop-FR were registered, or add them to §3.1 as additional deviations.

---

## Recommendation

**At MIR (target):** **Major Revision** addressable in 3-6 months. The three Grade-A issues (publication-bias paradox, CCM HARKing, cDAI temporal validity) require substantial rewriting but not new data collection. The Grade-B issues (RVE robustness, PET-PEESE, Marano positioning, drop-FR reordering, Frontier cell honesty) are tractable. The empirics + transparency are above field median; the framing needs editorial discipline.

**At JIBS / SMJ / AMJ (aspirational):** **Reject (without revision)** unless the three Grade-A issues are fully resolved and the paper is recast as either (i) a publication-bias audit paper with moderator analysis as secondary, OR (ii) a moderator-power-bounded paper with CCM dropped entirely. The current framing — confirmatory moderator test + post-hoc CCM rescue + publication-bias headline — is too unfocused for top-3 IB.

**At MBR / IBR / JIM (backup):** **Minor-to-Major revision**, likely accept after revisions. The pubication-bias finding is novel-enough; CIMT framing is tolerable at Q2 outlets if explicitly post-hoc; cDAI temporal validity will still need a Limitation note.

---

## Priority fix list (for submission)

| # | Issue | Grade | Effort | Where |
|---|---|---|---|---|
| 1 | Resolve publication-bias paradox in Discussion | A | 1 day | §5.2 |
| 2 | Reframe CCM as post-hoc Discussion proposition | A | 1 day | §1, §2.4, §5 |
| 3 | Restrict cDAI to Span+Follow as primary; full-sample as sensitivity | A | 1 day analysis + write-up | §4.4 + Supp |
| 4 | Add RVE robustness check | B | 1 day | §4.7 |
| 5 | Run + report PET-PEESE; OR drop the mention | B | 0.5 day | §4.6 |
| 6 | Reorder §4.3 to lead with drop-FR | B | 0.5 day | §4.3 |
| 7 | Drop or qualify Vs Marano positioning | B | 1 day | §1, §5 |
| 8 | Disclose Do-Phan 2025 self-citation circularity | B | 0.5 day | §5.1 |
| 9 | Audit pre-registration alignment; disclose CIMT/CCM deviations | B | 1 day | §3.1 |
| 10 | Trim "first to" claims from 6 to 3 substantive | C | 0.5 day | §1, §5 |
| 11 | Reframe "globally representative" to "geographically diverse with Advanced skew" | C | 0.25 day | throughout |
| 12 | Complete OSF z37kn deposit before submission | A | (separate workstream) | external |

**Total revision effort:** ~8-10 focused days for Grade A+B fixes. Grade A items are non-negotiable.

---

*End of P6 manuscript review.*
