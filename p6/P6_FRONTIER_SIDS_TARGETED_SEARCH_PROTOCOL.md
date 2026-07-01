# P6 — Targeted Frontier/SIDS Search Protocol (future work / revision lever)

**Status:** documented contingency — **not** a pre-submission requirement.
**Purpose:** a pre-specified plan to raise the Frontier-regime cell (currently
*k* = 3) and the SIDS cell (currently *k* = 0) so the exploratory CIMT gradient
(E1a: Advanced largest; E1b: Frontier smallest) can be *tested* rather than only
*bounded*. Deploy this if a reviewer requires a confirmatory E1a/E1b test, or as
a planned extension after first submission.

> The locked submission corpus stays **k = 238 / K = 288**. This protocol is
> additive: any studies it yields enter a *new* coding round and trigger a
> re-estimation of the three-level MARA on a machine with R (`metafor`).

---

## 1. Rationale
- ICRV significance (Q_M = 17.35, p = .002) is driven by a single **k = 3 Frontier cell** (r̄ = 0.349, dominated by Pouresmaeili et al., 2018); **SIDS k = 0**.
- The directional gradient E1a/E1b therefore cannot be confirmed — the manuscripts honestly report this as an *informative bound* and flag a targeted search as the remedy.
- Closing this gap converts the main reviewer risk into a strength ("we have a pre-specified plan / executed extension").

## 2. Target frame (ICRV-FR scope)
Restrict to firm-level I→P primary studies whose **sample economy** is:
- **Frontier** (WGI Rule of Law 2023 ≤ −0.50): e.g., Bangladesh, Pakistan, Myanmar, Cambodia, Lao PDR, Nigeria, Kenya, Ghana, Ethiopia, Tanzania, Uganda, Zimbabwe, Venezuela, Bolivia, Iraq, Afghanistan; **and/or**
- **SIDS** (UN-OHRLLS small-island developing states): e.g., Fiji, Papua New Guinea, Solomon Islands, Vanuatu, Samoa, Tonga, Mauritius, Seychelles, Maldives, Cape Verde, Jamaica, Trinidad & Tobago, Barbados, Bahamas, Belize, Guyana, Suriname.

## 3. Search strings
Base I→P string = OSF preregistration §6 (reused verbatim), **AND**-ed with a
geographic constraint.

**WoS Topic field (append to the OSF §6 base):**
```
AND TS=("frontier market*" OR "frontier econom*" OR "least developed countr*"
    OR "small island developing state*" OR SIDS OR "Pacific island*" OR "Caribbean"
    OR Bangladesh OR Pakistan OR Myanmar OR Cambodia OR "Lao PDR" OR Laos
    OR Nigeria OR Kenya OR Ghana OR Ethiopia OR Tanzania OR Uganda OR Zimbabwe
    OR Venezuela OR Bolivia OR Iraq OR Afghanistan
    OR Fiji OR "Papua New Guinea" OR "Solomon Islands" OR Vanuatu OR Samoa OR Tonga
    OR Mauritius OR Seychelles OR Maldives OR "Cape Verde" OR "Cabo Verde"
    OR Jamaica OR "Trinidad" OR Barbados OR Bahamas OR Belize OR Guyana OR Suriname)
```
**Scopus** = equivalent `TITLE-ABS-KEY( ... )` with
`AND DOCTYPE(ar) AND LANGUAGE(english) AND PUBYEAR AFT 1976`.

**Specialist supplements:** AfricaJOL, AJOL, ABI/INFORM, OpenAlex (filter by
country/region), plus backward/forward citation from any frontier/SIDS hit.

## 4. Eligibility (same as main protocol, FR-scoped)
Include if: (i) firm-level empirical I→P study; (ii) reports a usable effect
size (r, or convertible β/t/F/χ²/OR); (iii) sample is majority frontier/SIDS
economy; (iv) English; (v) published/working paper 1977–present.
Exclude: country-level only, no extractable effect, pure conceptual, duplicate
of an in-corpus effect.

## 5. Screening, extraction, ICR
1. Deduplicate against the locked `p6/data/p6_study_database.csv` (by DOI + title fuzzy match).
2. Two-stage screening (title/abstract → full text), log counts for a PRISMA *update* diagram.
3. Extract via the standard codebook (`p6/tools/p6_extraction_codebook.md`); all values PI-verified and locked.
4. Code ICRV (FR vs. — keep frontier vs. SIDS as a sub-flag), DPL phase, cDAI, industry, DOI, performance type.
5. Run the 20% second-coder ICR pass on the *new* studies; report κ/ICC alongside the main-corpus values.

## 6. Re-estimation
- Append new effects to the canonical input; re-run `p6/scripts/p6_real_mara.R` (`metafor::rma.mv`) — **requires R, not available in this container**.
- Regenerate `table1_baseline.csv … table5_sensitivity.csv`; update `CANONICAL_NUMBERS_P6.md` and all live manuscripts in lockstep.
- Re-test E1a/E1b with the enlarged Frontier (+ now-nonzero SIDS) cells; report whether the gradient emerges.

## 7. Expected yield & decision rule
- Realistic yield: **~10–40 additional frontier/SIDS effects** (frontier I→P literature is thin; SIDS thinner). Even a modest gain moves Frontier from k = 3 toward a testable cell and makes SIDS k > 0.
- **Deploy when:** (a) a reviewer demands a confirmatory E1a/E1b test, or (b) as a planned post-submission extension. **Do not** hold the first submission for it — pool size is an estimate, not a deliverable; P6's value is the three new moderators + three-level MARA.

## 8. Cross-reference fix (paired with this protocol)
The manuscripts cite "Appendix B" for *targeted search strings*, but Appendix B
is the **Coding Protocol**. When this protocol is adopted, point those
cross-references (Method note; Limitations a; Frontier expansion sentence) to
**this file / OSF §6** instead, so the citation is accurate.
