# P6 — Preregistration ↔ Manuscript ↔ Data ↔ Codebook Consistency Audit

> Date: 2026-05-27 · Scope: P6 three-level meta-analysis (OSF `z37kn`).
> Purpose: verify the registered preregistration against the final manuscript, the analysed
> dataset, and the extraction codebook before the OSF materials package is made public.
> **Principle:** a registered preregistration is a frozen, time-stamped record — deviations are
> *disclosed*, never retro-edited into the prereg.

## Verdict
- **Manuscript ↔ data: CONSISTENT.** ✅ No action.
- **Prereg ↔ final operationalisation: DEVIATIONS (legitimate, but need explicit disclosure).** ⚠️
- **Codebook ↔ data/manuscript: INCONSISTENT (stale).** ❌ Must reconcile before OSF upload.

---

## 1. What matches (no action)
- **Baseline numbers** identical across manuscript, dataset, results: k = 238 / K = 288,
  r̄ = 0.074 [0.060, 0.088], I² = 62.4% (L2 = 54.1%, L3 = 8.4%).
- **Hypothesis numbering** consistent: H1 = ICRV between-regime (confirmed, Q_M = 17.35, df = 4,
  p = .002); H2 = DPL phase (Q_M = 0.56, p = .755, ns); H3 = cDAI (Q_M = 1.23, p = .541, ns);
  H4 = publication bias (planned in prereg §9.3, elevated to a labelled hypothesis — acceptable).
- **Manuscript self-documents the final ICRV scheme** (§2, item 5) AND gives a crosswalk to the
  dissertation's canonical six-regime ICRV. Manuscript ICRV codes `I, II, III, FR, SIDS, MX`
  exactly match the dataset (`I`=139, `II`=25, `III`=91, `FR`=3, `MX`=30; `SIDS`=0/absent).
- Null/unconfirmed moderator results (E1a/E1b, H2, H3) are transparently reported.

---

## 2. DEVIATION A — ICRV operationalisation changed after registration
Four sources, three different schemes:

| Source | ICRV definition |
|---|---|
| **Prereg** §8.2 (registered) | numeric 1–6: 1 Advanced · 2 Upper-Middle · 3 Lower-Middle · 4 Frontier · 5 SIDS · 6 LDC |
| **Codebook** §4.1 (in OSF pkg) | numeric 1–6: 1 Advanced · 2 **Emerging** · 3 **Transition** · 4 **Resource/GCC** · 5 SIDS · 6 Frontier/LDC; *multi-country → code 2* |
| **Dataset** `p6_study_database.csv` | `I, II, III, MX, FR` (Roman + MX + FR) |
| **Manuscript** §2 (final, authoritative) | `I` Advanced-Innovation · `II` Upper-Middle · `III` Emerging · `FR` Frontier/LDC · `SIDS` Pacific (k=0) · **`MX` Multi-country (≥2 regimes)** |

Two substantive changes vs the registered plan:
1. The regime **labels/boundaries** were redefined (WGI Rule-of-Law thresholds; manuscript §2).
2. A **`MX` multi-country category was added** that exists in *neither* the prereg nor the
   codebook (the codebook had instead said "multi-country → code 2 (emerging)"). 30 effects (10%)
   sit in MX.

**Status:** This is a normal post-registration refinement, and the manuscript already (a) defines
the final scheme and (b) reports the null gradient. **What is missing is an explicit, labelled
"Deviations from preregistration" statement** (PRISMA 2020 Item 24c / OSF norm) that names the
ICRV redefinition + MX addition as a departure from the registered protocol.

## 3. DEVIATION B — DPL operationalisation changed after registration
| Source | DPL definition |
|---|---|
| **Prereg** §8.2 / **Codebook** | `dpl` = 1/2/3 by **publication-year bins** (1 = pre-2000, 2 = 2000–2009, 3 = 2010–2026) |
| **Dataset / Manuscript** | `PRE` / `SPN` / `FOL` = **Precede / Span / Follow** the digital-platform era (PRE=100, SPN=108, FOL=80); manuscript §3 uses `[d_Span, d_Follow]` with Precede as reference |

The final DPL is a Precede/Span/Follow construct, not the registered calendar-year bins. Same
treatment as Deviation A: disclose in the "Deviations from preregistration" statement; reconcile
the codebook.

---

## 4. DEFECT — Codebook is stale and contradicts the dataset (BLOCKS OSF upload)
`p6/tools/p6_extraction_codebook.md` (copied into `upload_package/3_Data/codebook.md`) still
documents the *pre-registration-era* ICRV (§4.1) and DPL coding. If uploaded next to
`p6_study_database_baseline.csv` (which uses `I/II/III/MX/FR` and `PRE/SPN/FOL`), an OSF reader or
IBR reviewer comparing the two would find a **direct contradiction** (e.g., codebook regime 4 =
"Resource/GCC" and "multi-country → code 2", but the data has no such coding and uses a standalone
`MX`). **Do not publish the package until the codebook is reconciled** to the manuscript §2 scheme
(the authoritative final definition).

---

## 5. Recommended actions
1. **Reconcile the codebook** (`p6/tools/p6_extraction_codebook.md` → re-copy into the package):
   replace §4.1 ICRV with the manuscript §2 scheme (`I/II/III/FR/SIDS/MX` + WGI thresholds +
   dissertation crosswalk) and the DPL section with Precede/Span/Follow. Bump to **v1.1
   (2026-05-27, reconciled to final coding)**, noting it supersedes the v1.0 prereg-era draft.
2. **Add a short "Deviations from preregistration" subsection** to the manuscript (and a one-line
   pointer on the OSF project) listing: ICRV regime redefinition + `MX` addition; DPL year-bins →
   Precede/Span/Follow; H4 (publication bias) promoted from planned analysis to labelled hypothesis.
3. **Do NOT edit** `P6_OSF_Preregistration_Template.md` substantively — it mirrors the frozen,
   registered record. (A non-substantive editor's note pointing to the deviations statement is OK.)
4. Re-run the OSF package assembly after the codebook fix so `upload_package/3_Data/codebook.md`
   carries v1.1.
