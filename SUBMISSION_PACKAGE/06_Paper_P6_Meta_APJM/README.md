# P6 Meta-Analysis — APJM Submission Package

**Target journal:** Asia Pacific Journal of Management (APJM, Springer Nature)
**Quartile:** Scopus Q1 · ABS-3
**Submission target:** Q3 2026
**Submission portal:** Springer Editorial Manager

## Package contents

| File | Purpose | Submission slot |
|---|---|---|
| `01_manuscript_blinded.docx` | Blinded manuscript (no author identifiers) | Main manuscript upload |
| `01_manuscript_blinded_vi.docx` | Vietnamese parallel version (CTU dossier / supervisor review) | NOT for journal portal |
| `02_title_page.md` (+ `.docx` after build) | Author title page, CRediT, ORCID, conflict-of-interest | Separate "Title page" upload |
| `03_cover_letter.md` (+ `.docx` after build) | APJM-specific cover letter (fit, contributions, OSF pre-registration disclosure) | Cover letter upload |
| `figures/` | 6 figures @ 300 DPI | Figure uploads |
| `osf_supplementary_materials.md` | Pointer to OSF Supp-A through Supp-M | OSF link in cover letter |
| `prisma_extraction_pipeline_status.md` | Path B (formal WoS+Scopus search) status | OSF deposit |

## Pre-submission checklist

- [ ] Read APJM "Instructions for Authors" current at time of submission (Springer Nature portal)
- [ ] Confirm word count meets APJM cap (~12,000 words total; current ≈ 11,167 ✓)
- [ ] Confirm format-specific requirements:
  - [ ] Running header (APJM)
  - [ ] Title page submitted separately from manuscript
  - [ ] Structured abstract (Purpose / Design / Findings / Originality / Implications)
  - [ ] APA 7 references (verified by `scripts/format-apa7.py`)
- [ ] Verify blinded manuscript has no author identifiers (already verified — commit `f1f5d38`)
- [ ] Verify cover letter discloses OSF pre-registration (https://osf.io/z37kn) and single-coder limitation transparently
- [ ] Confirm Replication Data Statement complies with APJM policy (link to OSF deposit)
- [ ] PRISMA 2020 27-item checklist accompanies the manuscript (in OSF Supp materials)

## Related materials

- Master submission README: `../README.md` (if exists in parent)
- Source manuscript: `../../p6_meta_manuscript_en.md`
- Source replication: `../../scripts/` (R `metafor` + Python cross-check)
- OSF pre-registration: https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN; registered May 18, 2026)

## OSF DOI note

The OSF pre-registration DOI **10.17605/OSF.IO/Z37KN** is journal-agnostic and remains the same across the MIR/APJM/MBR/MRQ target-journal exploration. The preregistration body does not name a specific target journal; the target-journal choice is a manuscript-level decision documented in the cover letter and title page only. No retro-edit to the OSF preregistration is required for the MIR → APJM retargeting.

## Why APJM (not MIR / IBR / MRQ)

- **Geographic fit:** APJM's scope ("management research in the Asia-Pacific") matches P6's 45-economy Asian and Pacific corpus and the ICRV institutional taxonomy directly.
- **Theoretical fit:** APJM has published institutional-view research (Peng 2003) and welcomes the integrated capability–institution mechanism (synthesising rent protection, LoF attenuation, and institutional-void amplification under the ICRV gradient) as an Asian-Pacific institutional-contingency advance.
- **Methodological tolerance:** APJM accepts pre-registered single-coder meta-analyses when the single-coder limitation is transparently disclosed and mitigated (P6 has 5 documented mitigations).
- **Submission velocity:** APJM review timeline (~6–8 months) is materially faster than MIR (~8–12 months) at similar Q1 / ABS-3 status.
- **NCS exclusion:** IBR was explicitly excluded by the corresponding author.
- **Quartile:** APJM Q1 Scopus is in the user-specified Q1–Q2 range; MRQ (Q3–Q4) was outside this range.
