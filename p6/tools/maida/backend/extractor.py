"""
Statistical parameter extractor for M-AIDA v7.0.

Uses the Anthropic Claude SDK to locate and parse effect-size statistics from
academic PDF text, then converts them to Pearson's r following:

    Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients in
    meta-analysis. Journal of Applied Psychology, 90(1), 175–181.
    https://doi.org/10.1037/0021-9010.90.1.175
"""

from __future__ import annotations

import json
import logging
import math
import uuid
from datetime import datetime
from typing import Any

import anthropic

from models import (
    DoiMeasure,
    DplPhase,
    ExtractedEffect,
    IcrvRegime,
    PerformanceMeasure,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Confidence thresholds (Peterson & Brown, 2005)
# ---------------------------------------------------------------------------
CONFIDENCE_DIRECT_R: float = 1.0   # Pearson r reported directly
CONFIDENCE_FROM_T: float = 0.8     # Derived from t-statistic + df
CONFIDENCE_FROM_BETA: float = 0.6  # Derived from standardised β coefficient
CONFIDENCE_REVIEW_THRESHOLD: float = 0.7  # Flag for PI review if below this

# ---------------------------------------------------------------------------
# Extraction system prompt
# ---------------------------------------------------------------------------
_SYSTEM_PROMPT = """You are a precision meta-analysis data extraction assistant
specialised in international business research.  Your job is to identify and
extract statistical parameters that quantify the relationship between a firm's
degree of internationalisation (DOI) and firm performance.

Extract ONLY the following statistics:
- N  : total sample size
- r  : Pearson's product-moment correlation coefficient (PREFERRED)
- t  : t-statistic (report alongside df if both present)
- df : degrees of freedom
- β  : standardised regression coefficient (beta)
- F  : F-statistic (for context; not directly convertible)
- p  : reported p-value (exact or inequality, e.g. p < 0.05)
- CI : 95 % confidence interval for r if reported

Also classify the study on these moderators when determinable from the text:
- doi_measure    : one of FSTS | entropy | n_markets | TNI
- performance_measure : one of ROA | ROE | ROS | TobinsQ | composite | other
- icrv_regime    : one of I | II | III | SIDS | V | pooled
- dpl_phase      : one of Precede | Span | Follow
- cdai_score     : float 0–10 if Cultural Distance Asymmetry Index is mentioned

Return a single JSON object — no markdown, no prose — with exactly these keys:
{
  "sample_n": <int|null>,
  "effect_r": <float|null>,
  "effect_t": <float|null>,
  "effect_beta": <float|null>,
  "effect_df": <int|null>,
  "p_value": <float|null>,
  "ci_lower": <float|null>,
  "ci_upper": <float|null>,
  "doi_measure": <"FSTS"|"entropy"|"n_markets"|"TNI"|null>,
  "performance_measure": <"ROA"|"ROE"|"ROS"|"TobinsQ"|"composite"|"other"|null>,
  "icrv_regime": <"I"|"II"|"III"|"SIDS"|"V"|"pooled"|null>,
  "dpl_phase": <"Precede"|"Span"|"Follow"|null>,
  "cdai_score": <float|null>
}

Rules:
1. If multiple models are reported, prefer the main/fully-specified model.
2. Prefer Pearson r over t over β for the primary effect size.
3. If a p-value is given as an inequality (e.g. "p < .001"), encode as the
   boundary value (0.001).
4. If the paper reports a negative t or β, preserve the sign.
5. Never hallucinate statistics; return null for any field not found.
"""


class StatisticalExtractor:
    """Wraps an Anthropic client to extract effect sizes from PDF text.

    Usage::

        extractor = StatisticalExtractor(api_key="sk-ant-...")
        effect = await extractor.extract_from_text(pdf_text, metadata)
    """

    def __init__(self, api_key: str) -> None:
        self._client = anthropic.Anthropic(api_key=api_key)

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def extract_from_text(
        self, text: str, metadata: dict[str, Any]
    ) -> ExtractedEffect:
        """Run LLM extraction on plain text from a PDF and return an effect.

        Args:
            text: Full text content extracted from the PDF.
            metadata: Pre-known bibliographic fields (title, authors, year,
                country, doi, …).

        Returns:
            An ``ExtractedEffect`` with all parseable fields populated.
        """
        raw = self._call_llm(text, metadata)
        return self._build_effect(raw, metadata)

    # ------------------------------------------------------------------
    # Effect-size conversion formulas
    # ------------------------------------------------------------------

    @staticmethod
    def compute_r_from_t(t: float, df: int) -> float:
        """Convert a t-statistic to Pearson's r.

        Formula (Peterson & Brown, 2005):
            r = sqrt( t² / (t² + df) )

        The sign of t is preserved in the returned r.

        Args:
            t: t-statistic (may be negative).
            df: Degrees of freedom.

        Returns:
            Pearson's r in the range [-1, 1].
        """
        # Peterson & Brown (2005): r = sqrt(t² / (t² + df))
        t_sq = t * t
        r_unsigned = math.sqrt(t_sq / (t_sq + df))
        return r_unsigned if t >= 0 else -r_unsigned

    @staticmethod
    def convert_beta_to_r(beta: float) -> float:
        """Approximate Pearson's r from a standardised regression coefficient.

        Approximation (Peterson & Brown, 2005):
            r ≈ β × 0.98

        This linear correction adjusts for the attenuation typically observed
        when converting unstandardised path coefficients.  The approximation
        performs best when |β| < 0.5.

        Args:
            beta: Standardised regression coefficient (signed).

        Returns:
            Approximate Pearson's r.
        """
        # Peterson & Brown (2005): r ≈ β × 0.98
        return beta * 0.98

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _call_llm(self, text: str, metadata: dict[str, Any]) -> dict[str, Any]:
        """Send the extraction prompt to Claude and parse the JSON response."""
        user_content = (
            f"Paper metadata provided by the researcher:\n{json.dumps(metadata)}\n\n"
            f"---BEGIN PDF TEXT---\n{text[:40_000]}\n---END PDF TEXT---\n\n"
            "Extract the statistical parameters as described and return valid JSON."
        )

        try:
            message = self._client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1024,
                system=_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_content}],
            )
        except anthropic.APIError as exc:
            logger.error("Anthropic API call failed: %s", exc)
            raise

        raw_text = message.content[0].text.strip()

        # Strip accidental markdown fences that models sometimes emit
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]

        try:
            return json.loads(raw_text)
        except json.JSONDecodeError as exc:
            logger.error("Failed to parse LLM JSON output: %s\n%s", exc, raw_text)
            return {}

    def _build_effect(
        self, raw: dict[str, Any], metadata: dict[str, Any]
    ) -> ExtractedEffect:
        """Resolve the canonical Pearson r and compute confidence / verification flag."""
        effect_r: float | None = raw.get("effect_r")
        effect_t: float | None = raw.get("effect_t")
        effect_beta: float | None = raw.get("effect_beta")
        effect_df: int | None = raw.get("effect_df")

        confidence: float
        computed_r: float | None = None

        if effect_r is not None:
            # Direct Pearson r — highest confidence (Peterson & Brown, 2005)
            computed_r = effect_r
            confidence = CONFIDENCE_DIRECT_R
        elif effect_t is not None and effect_df is not None:
            # Convert from t-statistic (Peterson & Brown, 2005)
            computed_r = self.compute_r_from_t(effect_t, effect_df)
            confidence = CONFIDENCE_FROM_T
        elif effect_beta is not None:
            # Convert from standardised β (Peterson & Brown, 2005)
            computed_r = self.convert_beta_to_r(effect_beta)
            confidence = CONFIDENCE_FROM_BETA
        else:
            # Nothing convertible found
            computed_r = None
            confidence = 0.0

        requires_verification = confidence < CONFIDENCE_REVIEW_THRESHOLD

        # Parse moderator fields with safe casting
        doi_measure: DoiMeasure | None = _safe_literal(
            raw.get("doi_measure"), ("FSTS", "entropy", "n_markets", "TNI")
        )
        performance_measure: PerformanceMeasure | None = _safe_literal(
            raw.get("performance_measure"),
            ("ROA", "ROE", "ROS", "TobinsQ", "composite", "other"),
        )
        icrv_regime: IcrvRegime | None = _safe_literal(
            raw.get("icrv_regime"), ("I", "II", "III", "SIDS", "V", "pooled")
        )
        dpl_phase: DplPhase | None = _safe_literal(
            raw.get("dpl_phase"), ("Precede", "Span", "Follow")
        )

        cdai_raw = raw.get("cdai_score")
        cdai_score: float | None = (
            float(cdai_raw) if cdai_raw is not None else None
        )

        p_raw = raw.get("p_value")
        p_value: float | None = float(p_raw) if p_raw is not None else None

        sample_n_raw = raw.get("sample_n")
        sample_n: int | None = int(sample_n_raw) if sample_n_raw is not None else None

        ci_lower_raw = raw.get("ci_lower")
        ci_upper_raw = raw.get("ci_upper")

        return ExtractedEffect(
            study_id=str(uuid.uuid4()),
            paper_title=metadata.get("title", ""),
            authors=metadata.get("authors", ""),
            year=int(metadata.get("year", 0)),
            country=metadata.get("country", ""),
            sample_n=sample_n,
            effect_r=computed_r,
            effect_t=effect_t,
            effect_beta=effect_beta,
            effect_df=effect_df,
            p_value=p_value,
            ci_lower=float(ci_lower_raw) if ci_lower_raw is not None else None,
            ci_upper=float(ci_upper_raw) if ci_upper_raw is not None else None,
            doi_measure=doi_measure,
            performance_measure=performance_measure,
            icrv_regime=icrv_regime,
            cdai_score=cdai_score,
            dpl_phase=dpl_phase,
            extraction_confidence=confidence,
            requires_verification=requires_verification,
            pi_locked=False,
            extracted_at=datetime.utcnow(),
            locked_at=None,
        )


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def _safe_literal(value: Any, allowed: tuple[str, ...]) -> str | None:
    """Return ``value`` if it is one of ``allowed``, else ``None``."""
    if isinstance(value, str) and value in allowed:
        return value
    return None
