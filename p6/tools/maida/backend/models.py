"""
Pydantic data models for M-AIDA v7.0.

All models represent domain objects for the internationalization-performance
meta-analysis pipeline: extracted effect sizes, verification decisions, and
Notion-synchronized study database entries.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Domain Enums / Literal Types
# ---------------------------------------------------------------------------

DoiMeasure = Literal["FSTS", "entropy", "n_markets", "TNI"]
PerformanceMeasure = Literal["ROA", "ROE", "ROS", "TobinsQ", "composite", "other"]
# ICRV regimes follow the dissertation's classification schema:
#   I   = Domestic-only control
#   II  = Limited international (FSTS < 25 %)
#   III = Moderate international (25–75 %)
#   SIDS= Small Island Developing States sub-sample
#   V   = High internationalization (> 75 %)
#   pooled = Mixed / unclassified sample
IcrvRegime = Literal["I", "II", "III", "SIDS", "V", "pooled"]
DplPhase = Literal["Precede", "Span", "Follow"]


# ---------------------------------------------------------------------------
# Core Extracted Effect Model
# ---------------------------------------------------------------------------


class ExtractedEffect(BaseModel):
    """One study-level effect size record produced by the LLM extractor.

    Fields prefixed with ``effect_`` are the raw statistics as reported in the
    paper.  ``effect_r`` is the canonical Pearson r used in the meta-analysis;
    the other ``effect_*`` fields are intermediary values from which r may be
    computed when a direct correlation is not reported.
    """

    study_id: str = Field(..., description="UUID assigned at extraction time")
    paper_title: str
    authors: str
    year: int
    country: str = Field(..., description="Focal country / region of sample")

    # Sample information
    sample_n: int | None = Field(None, description="Total sample size (N)")

    # Raw reported statistics
    effect_r: float | None = Field(
        None,
        description="Pearson's r as directly reported (preferred); confidence = 1.0",
    )
    effect_t: float | None = Field(
        None, description="t-statistic; converted to r via Peterson & Brown (2005)"
    )
    effect_beta: float | None = Field(
        None,
        description="Standardised regression coefficient β; converted via P&B (2005)",
    )
    effect_df: int | None = Field(
        None, description="Degrees of freedom paired with t-statistic"
    )
    p_value: float | None = Field(None, description="Reported p-value")
    ci_lower: float | None = Field(
        None, description="Lower bound of 95 % confidence interval for r"
    )
    ci_upper: float | None = Field(
        None, description="Upper bound of 95 % confidence interval for r"
    )

    # Moderator coding variables (dissertation-specific)
    doi_measure: DoiMeasure | None = Field(
        None, description="Degree-of-internationalisation measure used"
    )
    performance_measure: PerformanceMeasure | None = Field(
        None, description="Firm-performance construct used"
    )
    icrv_regime: IcrvRegime | None = Field(
        None, description="ICRV internationalization regime classification"
    )
    cdai_score: float | None = Field(
        None,
        ge=0.0,
        le=10.0,
        description="Cultural Distance Asymmetry Index score (0–10)",
    )
    dpl_phase: DplPhase | None = Field(
        None, description="Dynamic Performance Lag phase (Precede/Span/Follow)"
    )

    # Extraction provenance
    extraction_confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description=(
            "Confidence score: 1.0 = direct r; 0.8 = converted from t; "
            "0.6 = converted from β (Peterson & Brown, 2005)"
        ),
    )
    requires_verification: bool = Field(
        ...,
        description="True when confidence < 0.7 or ambiguous statistics detected",
    )
    pi_locked: bool = Field(
        False, description="True after Principal Investigator permanently locks entry"
    )
    extracted_at: datetime = Field(default_factory=datetime.utcnow)
    locked_at: datetime | None = None


# ---------------------------------------------------------------------------
# API Request / Response Models
# ---------------------------------------------------------------------------


class ExtractionRequest(BaseModel):
    """Payload sent to POST /api/extract.

    ``pdf_content`` is a Base64-encoded PDF byte string.  ``paper_metadata``
    carries any bibliographic information already known (title, DOI, etc.)
    before LLM extraction so the extractor can cross-check against the PDF.
    """

    pdf_content: str = Field(
        ..., description="Base64-encoded PDF binary content"
    )
    paper_metadata: dict = Field(
        default_factory=dict,
        description="Pre-known bibliographic metadata (title, year, doi, …)",
    )


class VerificationDecision(BaseModel):
    """PI verification payload sent to PATCH /api/studies/{id}/verify.

    ``field_overrides`` maps ExtractedEffect field names to corrected values so
    the PI can adjust any LLM-extracted statistic without re-running extraction.
    """

    study_id: str
    field_overrides: dict = Field(
        default_factory=dict,
        description="Map of field_name → corrected_value supplied by the PI",
    )
    pi_approved: bool = Field(
        False, description="True when PI accepts the (possibly overridden) record"
    )
    pi_notes: str = Field(
        "",
        description="Free-text notes from the PI recorded alongside the decision",
    )


class StudyDatabaseEntry(ExtractedEffect):
    """Extends ExtractedEffect with Notion synchronization metadata."""

    notion_page_id: str | None = Field(
        None, description="Notion page ID after successful sync"
    )
    pi_notes: str = ""
