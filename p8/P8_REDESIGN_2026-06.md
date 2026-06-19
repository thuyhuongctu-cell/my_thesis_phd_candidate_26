# P8 — Redesign for scientific soundness and a clear contribution (2026-06-19)

## Why redesign

The current P8 claims a **robust Forced Internationalization Penalty (FIP)** — a strong, significant
*negative* I–P slope across "seven Pacific SIDS" (β = −1.339, p < .001). Reproduction shows this
estimate rests on **three economies / three clusters** (Fiji 2009, PNG 2015, Vanuatu 2009; N = 209),
is **data-version-sensitive**, and **does not survive** on the fuller sample (β turns positive/null;
3-cluster inference is invalid). The strong-FIP empirical claim is therefore not defensible for a Q1
submission. The redesign converts the weakness into a **robust, honest, and theoretically valuable**
contribution.

## Verified empirical core (full 8-economy SIDS sample, raw .dta, FE, cluster by economy)

| Quantity | Estimate | p | Reading |
|---|--:|--:|---|
| FSTS² (curvature) | +0.553 | 0.154 | **No inverted-U** (curvature null) |
| FSTS linear slope | −0.161 | 0.338 | **I–P slope null** (faint negative lean) |
| N / economies / exporters | 1,916 / 8 / 13.9% | — | thin, forced-export profile |
| Contrast: mainland transition (P7 Lower-mid) | β₂ = −1.012 | <.001 | inverted-U **present** on the mainland |

**Robust finding:** in Pacific SIDS the canonical inverted-U **dissolves** — neither the curvature nor
the slope is statistically distinguishable from zero — in sharp contrast to mainland Asia, where the
inverted-U is sharp. This holds on the full 8-economy sample (8 clusters), is not data-version-fragile,
and is the empirically honest core.

## Redesigned positioning

**Working title:** *When the Inverted-U Dissolves: Structural Boundary Conditions of the
Internationalization–Performance Relationship in Pacific Microstates.*

**Research question.** Does the dominant inverted-U I–P relationship extend to extreme-periphery
micro-economies, or does it dissolve where its implicit structural prerequisites are absent?

**Core argument (scope conditions).** The inverted-U cost–benefit logic implicitly assumes three
structural prerequisites: (i) a viable domestic market, (ii) manageable trade costs, and (iii)
functional institutional support. Pacific SIDS violate all three simultaneously — firms export under
*compulsion*, not strategic selection. Where the prerequisites fail, the mechanism that generates the
curve (early scale/learning gains, later coordination costs around an interior optimum) breaks down,
so the relationship **dissolves** (no curvature, null slope) rather than following the curve. The
**Forced Internationalization Penalty (FIP)** is then defined as the *theoretical limiting case* of
this dissolution — the direction the relationship tends toward when forced internationalization fully
dominates — for which the SIDS evidence shows a non-significant negative lean rather than a robust
effect (stated transparently).

## Reframed propositions (no over-claiming)

- **P1 (dissolution, supported):** In Pacific SIDS the inverted-U is absent — both FSTS² and the FSTS
  slope are statistically indistinguishable from zero, unlike mainland Asian regimes.
- **P2 (capability does not rescue, supported):** Technological capability raises the productivity
  *level* (β_TCI > 0) but neither TCI nor DAI restores a positive I–P slope or an interior optimum.
- **P3 (FIP as limiting case, theoretical + suggestive):** Under the three-prerequisite-violation
  account, the relationship tends negative; the SIDS estimate is directionally negative but
  non-significant on the full sample, consistent with FIP as a boundary concept rather than a
  measured effect.

## Empirical strategy (valid this time)

1. **Full sample, all 7–8 Pacific (+ Timor-Leste) economies and all available waves** — maximises
   clusters (8) and avoids the 3-economy artifact.
2. **Honest few-cluster inference:** report the cluster count prominently; use wild-cluster bootstrap
   (Webb weights) for all key tests; never present a clustered p-value as decisive with <10 clusters.
3. **The headline is the dissolution (null curvature + null slope) contrasted with the mainland
   inverted-U** — a null *as a finding*, which is publishable when it bounds a dominant theory.
4. **Descriptive pillar:** the forced-export profile (13.9% exporters, mean FSTS 0.062, high
   productivity dispersion) documents *why* selection-into-exporting breaks down.
5. **Capability models** (M3) show level-shift without slope rescue.
6. **Transparency appendix:** the data-version sensitivity and the 3-economy fragility of any strong
   negative estimate are reported openly (turns the reproducibility problem into a credibility asset).

## Contributions (clear, defensible)

1. **First firm-level test of the inverted-U's *scope conditions* in Pacific microstates**, showing
   the paradigm does not extend to the extreme periphery.
2. **Makes explicit the three structural prerequisites** the inverted-U literature has left implicit —
   a theoretical clarification with broad applicability (any micro/periphery economy).
3. **Names the theoretical limiting case (FIP)** and distinguishes it from phase-1 S-curve costs and
   liability of foreignness — kept as a *concept*, not an over-stated empirical effect.
4. **Policy:** export-led-growth prescriptions are misaligned with SIDS structural realities; the
   binding constraints are domestic-market viability, trade costs, and institutions, not export
   intensity per se.

## Target journal

- **World Development** still fits (development + boundary condition + policy; null-as-boundary is
  acceptable there), now on a defensible footing.
- Alternatives if a stronger theory framing is wanted: *Journal of World Business* (boundary
  conditions / context), *Asia Pacific Journal of Management* (regional), or a *Global Strategy
  Journal* "scope conditions" piece.

## What changes vs the current manuscript

- Title, abstract, RQ, and hypotheses move from "we find a strong FIP" → "the inverted-U dissolves;
  FIP is the theoretical limiting case."
- Headline estimates move from the 3-economy −1.339 to the **full-sample null** (curvature +0.55 n.s.,
  slope −0.16 n.s.), with the mainland contrast.
- Add the wild-bootstrap few-cluster inference and the transparency appendix.
- Keep: the theory section, the three-prerequisite mechanism, the descriptive SIDS profile, the policy
  section.

## Implementation status

The empirical core above is **already verified** from the raw `.dta` (this document). On approval, the
next step is to rewrite the manuscript Sections 1–6 to the new framing and regenerate the tables; the
thesis §4.7 has already been reframed consistently (FIP as concept + exploratory evidence).
