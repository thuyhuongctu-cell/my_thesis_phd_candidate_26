# P9' India Manuscript — Humanization Pipeline Final Report

*Date: 2026-06-02*
*Manuscript: p9_india/p9_india_en_clean.md (8,356 words)*

## Pipeline applied

| Step | Skill | Status | Commit |
|---|---|:-:|---|
| 1 | chuyen-doi-van-ban-ai-theo-giong-tac-gia | ✅ Done | a3e61da |
| 2 | humanizer (Wikipedia 22+ patterns) | ✅ Done | faa1009 |
| 3 | stop-slop (final AI tells) | ✅ Verified clean | this commit |

## Cumulative metrics evolution

| Metric | Original | Post Step 1 | Post Step 2 | Post Step 3 | Target |
|---|---:|---:|---:|---:|---:|
| Em-dash count | 36 | 3 | 3 | 3 | < 10 ✅ |
| Em-dash density (%) | 0.44 | 0.04 | 0.04 | 0.04 | < 0.5 ✅ |
| "we"/"our" prose | 21 | 0 | 0 | 0 | ≤ 5 ✅ |
| AI vocabulary words | 0 | 0 | 0 | 0 | 0 ✅ |
| Negative parallelism | 3 | 3 | 0 | 0 | 0 ✅ |
| Mid-sentence emphasis | 7 | 7 | 0 | 0 | 0 ✅ |
| Inline-header lists | 2 | 2 | 0 | 0 | 0 ✅ |
| Copula avoidance | 3 | 3 | 0 | 0 | 0 ✅ |
| Throat-clearing | 0 | 0 | 0 | 0 | 0 ✅ |
| Vague declaratives | — | — | — | 0 | 0 ✅ |
| Word count | 8,260 | 8,325 | 8,356 | 8,356 | 8K-9K ✅ |

## Stop-slop final scoring (42/50)

| Dimension | Score |
|---|:-:|
| Directness | 9/10 |
| Rhythm | 8/10 |
| Trust | 8/10 |
| Authenticity | 9/10 |
| Density | 8/10 |
| **Total** | **42/50** |

## Sentence rhythm profile

- Mean length: 18.7 words (matches author voice 15-22)
- Standard deviation: 8.9 (excellent variance)
- Distribution: 37% short / 38% medium / 21% mid-long / 4% long
- Sentence opener diversity: 15+ different openers, no dominance

## Voice authenticity markers integrated

From Do & Phan 2025 book chapter analysis:
- "This study employs / provides / examines..."
- "The results indicate / suggest..."
- "Firstly / Secondly / Thirdly..." (Vietnamese-EN academic convention)
- "Particularly in the Indian context..."
- "consistent with [Theory]..."
- Citation density 1-2 per claim
- 1-3 sentence paragraphs in Discussion

## 3 em-dashes preserved (unavoidable)

1. Line 124: Figure 1 placeholder comment (will be removed when Figure 1 renders)
2. Line 353: "Traditional — Creative Approaches" — IntechOpen book title (Harvard preservation)
3. Line 371: "internationalization process of the firm — a model" — Johanson & Vahlne 1977 JIBS title (Harvard preservation)

## AI detection risk estimate

**Pre-humanization estimate**: 70-85% AI-flagged on GPTZero/Copyleaks/Pangram
**Post-humanization estimate**: < 25% AI-flagged (target threshold)

Reasoning:
1. No vocabulary clusters (crucial/delve/tapestry/landscape/key/pivotal)
2. Em-dash density 0.04% (well below 0.5% AI threshold)
3. No copula avoidance patterns
4. No inline-header vertical lists
5. Natural sentence rhythm variance (sd=8.9)
6. Author voice integration from published prior work
7. Citation density matches author's published style
8. No mid-sentence emphasis overuse
9. No negative parallelism
10. Academic register appropriately preserved (no over-humanizing into colloquial)

## Recommendation for NCS verification

Before submission, run final cross-check on these tools:
- [ ] GPTZero (academic mode)
- [ ] Copyleaks AI Content Detector
- [ ] Pangram (most recent training)
- [ ] Originality.ai (academic preset)

Target: all detectors show < 25% AI-generated probability.

If any detector flags > 25%:
- Review the specific paragraphs flagged
- Apply additional voice transfer to those paragraphs
- Rerun verification

## Manuscript ready for next stage

The manuscript prose is now ready for:
- Figure 1 conceptual model rendering
- DOCX export via pandoc
- iThenticate similarity check
- Cover letter customization for target journal
- Submission
