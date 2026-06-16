# P5 Pre-Submission Review

**Paper:** "The Export Intensity–Performance Relationship in Chinese Private Firms: A Threshold-Stability Perspective"
**Target:** International Journal of Emerging Markets (IJOEM), Emerald
**Source reviewed:** `p5/submission/ijoem_package/01_manuscript_blinded.md` (full), `03_cover_letter.md`, `README.md`
**Date:** 2026-06-09

## Summary

A competent, well-structured threshold-stability study with a clean two-wave (2012/2024) WBES China design, correctly stated throughout the manuscript (no 4-wave remnants survive in the body; only a benign reference in the replication note to a six-part build directory). The core statistics (turning points 49.4 / 47.2 / 48.8 %, Paternoster z = +0.82 / −0.61, all β/p) are internally consistent across abstract, highlights, body, Tables 2–3, and conclusion. The Emerald structured abstract, Harvard "and" referencing, and AI-use disclosure are all present and house-style compliant. No em-dashes; no genuine AI-tone vocabulary; the lone "superior" (line 206) is legitimate comparative usage.

The blocking problems are not in the statistics but in (1) an internal logical contradiction about whether firms can be matched across waves ("panel core" vs anonymisation limitation), and (2) a cluster of cover-letter/README metadata that contradicts the manuscript (manufacturing-only framing, sample scope, table count, word count, JEL codes). These are fixable but several would embarrass the authors if a desk editor cross-checks the package.

## Severity counts

| Severity | Count |
|----------|-------|
| CRITICAL | 0 |
| MAJOR | 5 |
| MINOR | 9 |

## Top-3 fixes

1. **Resolve the "panel core" vs anonymisation contradiction (MAJOR).** Section 3.3 claims 217 firms appear in both waves enabling "within-firm variation estimates"; Section 5.4 says cross-wave panel matching "is not possible due to WBES anonymisation." Pick one: WBES China 2012 and 2024 are independent cross-sections, so delete the 217-firm panel-core claim.
2. **Fix cover letter "manufacturing firms" framing (MAJOR).** The letter twice calls the sample "Chinese private manufacturing firms," but the manuscript's identification strategy explicitly uses the *full private-firm frame* (services, retail, IT, construction included), with manufacturing only as a robustness subsample. Align the letter to the full-frame design.
3. **Reconcile package metadata (MAJOR).** Word count (manuscript 7,200 / cover letter 6,600 / README 6,500), table count (manuscript 3 / README 4 twice), and JEL codes (manuscript F23,O33,D22,L25,O53 / cover letter F23,O33,L25,O53,P31) all disagree. Make all three documents match the manuscript.

---

## Dimension 1 — Macro logic

| ID | Sev | Location | Issue | Fix |
|----|-----|----------|-------|-----|
| M1 | MAJOR | Section 3.3 (l.336–339) vs Section 5.4 (l.657–661) | "217 firms appear in both the 2012 and 2024 waves (the 'panel core'), enabling within-firm variation estimates" directly contradicts "panel matching across 2012 and 2024 is not possible due to WBES anonymisation." | Delete the panel-core sentences in Section 3.3; WBES waves are unmatched cross-sections. The cluster-robust SE justification can stay without the within-firm-matching claim. |
| M2 | MINOR | Section 2.3 (l.199, 201) vs hypothesis block | Prose introduces "(H3)" and "(H4)", but the formal hypotheses are labelled H3, H4a, H4b. The bare "H4" referent is ambiguous. | Change "attenuating the curvature (H4)" to "(H4a/H4b)" or rename for one-to-one prose↔label mapping. |
| M3 | MINOR | Abstract vs body | Abstract tests only H2a/H2b and H1 by implication; H3/H4a/H4b are never named in the abstract though they are central to Section 4.4. | Add one clause to Findings naming the capability-moderation hypotheses (H4b supported) for abstract↔body completeness. |
| M4 | MINOR | Section 4.4 / Section 5.2 | F2 (p=.039) is described as "marginal, not surviving Bonferroni" and mapped to "H4b" support, but H4a is the within-wave curvature-moderation hypothesis the F2 test actually targets. The verdict (H4b over H4a) is defensible but the H4a/F2 linkage in Table 3 note ("F2 to H4a") and the discussion's "marginally consistent with H4a" should be stated as a single consistent reading. | State explicitly: F2 marginal leads to weak/no support for H4a leads to H4b retained. |

Contributions↔results align; conclusions are supported by the reported tests. H1, H2a/H2b, H3, H4a/H4b are all tested and reported.

## Dimension 2 — Writing details / structured abstract

| ID | Sev | Location | Issue | Fix |
|----|-----|----------|-------|-----|
| W1 | PASS | Abstract (l.20–64) | Emerald structured abstract complete: Purpose / Design / Findings / Originality-value, plus keywords, JEL, paper type. | None. |
| W2 | MINOR | Section 5.2 (l.629–639) | Paragraph references sibling papers "P4 Singapore", "P3 Vietnam", and "ICRV-contingency" framework without introducing them; in a blinded single-paper submission these read as dangling cross-references to unpublished companion work. | Either cite Đỗ and Phan (2026)-style companion references explicitly or soften to "in a parallel advanced-economy setting" without the internal P-codes. |
| W3 | MINOR | l.249–251 | "This attrition is not random in direction, WBES 2024 overshoots private manufacturing SMEs" — comma splice joining two independent clauses. | Replace first comma with a colon or "because": "...not random in direction: WBES 2024 overshoots...". |

## Dimension 3 — Grammar

| ID | Sev | Location | Issue | Fix |
|----|-----|----------|-------|-----|
| G1 | MINOR | Section 2.3 H4a (l.213–214) | Stray line break places the comma at the start of a line: "moderates the I–P curvature cross-sectionally / , because..." | Join: "...cross-sectionally, because...". |
| G2 | MINOR | l.249 | "This attrition is not random in direction" — comma-splice (see W3). | As W3. |
| G3 | MINOR | l.83–85 highlight | "recasts from a sample artifact to a durable structural regularity" — verb "recast" used intransitively; reads awkwardly. | "is recast from a sample artefact to..." (and standardise artifact/artefact spelling vs l.593 "artifact"). |

S-V agreement, tense, which/that usage otherwise clean. No Chinglish detected.

## Dimension 4 — Numbers / stats / citation consistency

| ID | Sev | Location | Issue | Fix |
|----|-----|----------|-------|-----|
| N1 | PASS | abstract / Table 2 / Section 4.2 / conclusion | Turning points (49.4 / 47.2 / 48.8 %), Paternoster z (+0.82, p=.412; −0.61, p=.545), all β and p values are mutually consistent. | None. |
| N2 | PASS | throughout | Two-wave (2012, 2024) design stated consistently; no 4-wave remnant in body. README footnote correctly flags legacy 4-wave drafts as superseded. | None. |
| N3 | MINOR | Table 3 (l.517–519) vs note (l.521) | F-test denominator df is 3,558 while sample_full N = 3,559. With 11 estimated parameters the residual df would be far below 3,558; the "F(2, 3,558)" denominator df appears to just echo N−1 rather than N−k. | Verify and report correct residual df (N − parameters), or clarify the cluster-robust df convention used. |
| N4 | MINOR | Section 3.1 (l.239–240) vs Section 3.1 (l.243–244) | Raw frame "2,700 firms (2012)" and "2,189 (2024)" vs focal-set "2,619 / 1,940". This is internally explained, but the abstract/Tables use the regression sample (2,610 / 1,934 / 4,544). The two N families (focal-set 2,619/1,940/4,559 vs regression 2,610/1,934/4,544) are correctly distinguished in the replication note — confirm the body never mixes them. They are consistent as written; flagging only because the closeness invites copy-edit error. | No change required; keep the replication note that disambiguates them. |
| N5 | MAJOR | Cover letter l.35 vs manuscript l.59–62 | JEL codes differ: manuscript F23, O33, D22, L25, O53; cover letter F23, O33, L25, O53, P31. | Align JEL sets across documents. |
| N6 | PASS | references | Citation↔reference bidirectional check: all in-text cites (Hitt et al. 1997; Lu and Beamish 2004; Bausch and Krist 2007; Schwens et al. 2018; Marano et al. 2016; Kirca et al. 2012; Teece 2007; Lall 1992; Avenyo et al. 2021; Haans et al. 2016; Lind and Mehlum 2010; Paternoster et al. 1998; Pierce and Aguinis 2013; Wagner 2007; Manova 2013; Niepmann and Schmidt-Eisenlohr 2017; Kano et al. 2020; Nambisan et al. 2019; Vial 2019; Verhoef et al. 2021; Volberda et al. 2021; Antonakis et al. 2010; Shaver 2020; Xiao et al. 2013; Johanson and Vahlne 1977; Helpman et al. 2004; MacKinnon and White 1985; World Bank 2013/2025; Đỗ/Do and Phan 2026) resolve to the reference list. | See N7, N8 for the exceptions. |
| N7 | MINOR | l.139, l.140 | "Johanson and Vahlne, 1977" and "Helpman, Melitz and Yeaple, 2004" are cited in text but have NO entry in the reference list. | Add both references, or remove the citations. |
| N8 | MINOR | references l.814–817 (Meyer et al. 2017) | Meyer, van Witteloostuijn and Beugelsdijk (2017) appears in the reference list but is never cited in the text (orphan reference). | Cite it (e.g., in the p-value/inference discussion) or delete it. |
| N9 | MINOR | references l.837 (Schwens), l.862 (Volberda) | These two entries use an ampersand "&" before the final author, whereas every other entry uses Harvard "and". | Replace "&" with "and" for Harvard consistency. |

## Dimension 5 — House style (IJOEM/Emerald)

| ID | Sev | Location | Issue | Fix |
|----|-----|----------|-------|-----|
| H1 | MAJOR | Cover letter l.11, l.11 ("manufacturing firms") | Letter frames the study as "Chinese private manufacturing firms" and "China's private manufacturing sector", contradicting the manuscript's full-private-firm frame (services, retail, IT, construction explicitly included; Section 3.1 l.253–261). | Rewrite to "Chinese private firms (full WBES private-firm frame)"; manufacturing is only the Section 4.6 robustness subsample. |
| H2 | MAJOR | README l.47, l.51 vs manuscript | README "Tables: 4" (two places) and "Word count ~6,500"; cover letter "~6,600"; manuscript "~7,200" and "Tables: 3". | Set all package files to the manuscript's true counts (3 tables; one agreed word count). |
| H3 | MINOR | AI Use Disclosure (l.739–743) | Present and Emerald-compliant (Grammarly, language only). Cover letter mirrors it. | None — confirmed compliant. |
| H4 | MINOR | Keywords | Manuscript keywords (l.55–57) vs README checklist keywords (l.33) vs cover letter keywords (l.34) are three different lists. | Standardise the 5–6 keyword set across documents. |

## Dimension 6 — Banned vocab / em-dash scan

- **Em-dashes:** none found (`—` returns no matches). All dashes are en-dashes ("I–P", "intensity–performance") or hyphens. PASS.
- **"superior" (l.206):** confirmed legitimate comparative usage ("superior internal competencies reduce the coordination costs..."). NOT flagged.
- **AI-tone vocabulary:** "robust/robustly" (multiple) is standard statistical usage; "leverage" (l.340) is a noun ("identification leverage"). No genuine AI-tone terms (no delve/tapestry/nuanced/pivotal/seamless/landscape). PASS.

---

## Score: 7.5 / 10

Methodologically sound, statistically self-consistent, house-style compliant, and free of the AI-tone and 4-wave-remnant problems the brief flagged. Held back by one genuine internal logical contradiction (panel-core vs anonymisation) and a cluster of package-metadata inconsistencies (manufacturing framing, table/word counts, JEL, keywords) that a desk editor will notice on cross-check.

## Recommendation: **Minor revision before submission**

No CRITICAL issues. Fix the 5 MAJOR items (panel-core contradiction, cover-letter manufacturing framing, table count, word count, JEL codes) and the citation gaps (N7/N8/N9) before uploading to ScholarOne. The science and core numbers are submission-ready.
