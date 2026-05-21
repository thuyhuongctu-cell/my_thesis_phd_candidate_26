# BẰNG CHỨNG QUYỀN TÁC GIẢ — MẪU MÃ NGUỒN
# (Evidence of Authorship — Source Code Samples)
# COV Copyright Registration: M-AIDA v7.0.0

---

> **Hướng dẫn**: Tài liệu này cung cấp mẫu mã nguồn (10–15 trang đầu của file chính) kèm
> copyright header theo yêu cầu của Cục Bản quyền Tác giả Việt Nam (COV).
> In và đóng kèm theo hồ sơ đăng ký bản quyền (1 bộ gốc).

---

## FILE 1: backend/main.py (FastAPI Application Entry Point)

```python
# =============================================================================
# M-AIDA: Meta-Analysis Intelligent Data Assistant
#         Internationalization & Performance Research Pipeline
# =============================================================================
# Version   : 7.0.0
# Copyright : © [Năm] [Tên tác giả đầy đủ]. All rights reserved.
# Author    : [Tên tác giả]
# Created   : [DD/MM/YYYY]
# Modified  : [DD/MM/YYYY]
# License   : Proprietary — Research Use Only
#
# Protected by copyright law. Unauthorized reproduction, distribution,
# or modification is strictly prohibited.
# =============================================================================
"""
M-AIDA v7.0 — FastAPI application entry point.

Routes
------
POST   /api/extract               Upload PDF → ExtractedEffect
GET    /api/studies               List all studies (filterable)
GET    /api/studies/{id}          Single study detail
PATCH  /api/studies/{id}/verify   PI verification + field overrides
POST   /api/studies/{id}/lock     PI permanent data lock (irreversible)
GET    /api/studies/export/csv    Export verified+locked studies as CSV
GET    /api/health                Health check
POST   /api/notion/sync           Push all locked studies to Notion

Data persistence
----------------
Studies are stored in an in-memory dict keyed by study_id (UUID string).
TODO: Replace with SQLite persistence using aiosqlite + SQLAlchemy Core so
      data survives process restarts.  The StudyDatabaseEntry model already
      has all required fields; only main.py needs to change.
"""

from __future__ import annotations

import base64
import csv
import io
import logging
from datetime import datetime
from typing import Any

import fitz  # PyMuPDF
from fastapi import FastAPI, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from extractor import StatisticalExtractor
from models import ExtractedEffect, ExtractionRequest, StudyDatabaseEntry, VerificationDecision
from notion_sync import NotionSync
from settings import get_settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="M-AIDA v7.0",
    description="Meta-Analysis Intelligent Data Assistant — I→P research pipeline",
    version="7.0.0",
)

settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_studies: dict[str, StudyDatabaseEntry] = {}


def _get_extractor() -> StatisticalExtractor:
    if not settings.anthropic_api_key:
        raise HTTPException(
            status_code=503,
            detail="ANTHROPIC_API_KEY not configured; extraction unavailable.",
        )
    return StatisticalExtractor(api_key=settings.anthropic_api_key)


def _get_notion() -> NotionSync:
    if not settings.notion_token or not settings.notion_database_id:
        raise HTTPException(
            status_code=503,
            detail="NOTION_TOKEN or NOTION_DATABASE_ID not configured.",
        )
    return NotionSync(
        token=settings.notion_token, database_id=settings.notion_database_id
    )


@app.get("/api/health", tags=["system"])
def health_check() -> dict[str, Any]:
    return {
        "status": "ok",
        "version": "7.0.0",
        "study_count": len(_studies),
        "anthropic_configured": bool(settings.anthropic_api_key),
        "notion_configured": bool(settings.notion_token and settings.notion_database_id),
    }


@app.post("/api/extract", response_model=StudyDatabaseEntry, tags=["extraction"])
def extract_pdf(request: ExtractionRequest) -> StudyDatabaseEntry:
    """Accept a Base64-encoded PDF and return an extracted effect-size record."""
    try:
        pdf_bytes = base64.b64decode(request.pdf_content)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid Base64 PDF content: {exc}") from exc

    try:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        pages_text: list[str] = [page.get_text() for page in doc]
        full_text = "\n".join(pages_text)
        doc.close()
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"PDF text extraction failed: {exc}") from exc

    extractor = _get_extractor()
    try:
        effect: ExtractedEffect = extractor.extract_from_text(full_text, request.paper_metadata)
    except Exception as exc:
        logger.exception("Extraction failed")
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    entry = StudyDatabaseEntry(**effect.model_dump())
    _studies[entry.study_id] = entry
    return entry


@app.post("/api/extract/upload", response_model=StudyDatabaseEntry, tags=["extraction"])
async def extract_pdf_upload(
    file: UploadFile,
    title: str = Query(""),
    authors: str = Query(""),
    year: int = Query(0),
    country: str = Query(""),
) -> StudyDatabaseEntry:
    """Multipart file upload alternative to the Base64 POST /api/extract route."""
    pdf_bytes = await file.read()
    if not pdf_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")
    encoded = base64.b64encode(pdf_bytes).decode()
    metadata = {"title": title, "authors": authors, "year": year,
                 "country": country, "filename": file.filename or ""}
    req = ExtractionRequest(pdf_content=encoded, paper_metadata=metadata)
    return extract_pdf(req)


@app.get("/api/studies", response_model=list[StudyDatabaseEntry], tags=["studies"])
def list_studies(
    icrv: str | None = Query(None),
    dpl: str | None = Query(None),
    verified: bool | None = Query(None),
    locked: bool | None = Query(None),
) -> list[StudyDatabaseEntry]:
    results = list(_studies.values())
    if icrv is not None:
        results = [s for s in results if s.icrv_regime == icrv]
    if dpl is not None:
        results = [s for s in results if s.dpl_phase == dpl]
    if verified is not None:
        results = [s for s in results if (not s.requires_verification) == verified]
    if locked is not None:
        results = [s for s in results if s.pi_locked == locked]
    return results


@app.get("/api/studies/export/csv", response_class=StreamingResponse, tags=["studies"])
def export_csv() -> StreamingResponse:
    """Stream a CSV of all PI-verified and locked studies."""
    locked = [s for s in _studies.values() if s.pi_locked]
    if not locked:
        raise HTTPException(status_code=404, detail="No locked studies available for export.")
    buf = io.StringIO()
    fieldnames = [
        "study_id", "paper_title", "authors", "year", "country", "sample_n",
        "effect_r", "effect_t", "effect_beta", "effect_df", "p_value",
        "ci_lower", "ci_upper", "doi_measure", "performance_measure",
        "icrv_regime", "dpl_phase", "cdai_score", "extraction_confidence",
        "pi_notes", "locked_at",
    ]
    writer = csv.DictWriter(buf, fieldnames=fieldnames, extrasaction="ignore")
    writer.writeheader()
    for study in locked:
        writer.writerow(study.model_dump())
    buf.seek(0)
    return StreamingResponse(
        content=iter([buf.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="maida_locked_studies.csv"'},
    )
```

---

## FILE 2: backend/extractor.py (Statistical Extraction Engine)

```python
# =============================================================================
# M-AIDA: Meta-Analysis Intelligent Data Assistant
# =============================================================================
# Version   : 7.0.0
# Copyright : © [Năm] [Tên tác giả đầy đủ]. All rights reserved.
# Author    : [Tên tác giả]
# License   : Proprietary — Research Use Only
# =============================================================================
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
    DoiMeasure, DplPhase, ExtractedEffect, IcrvRegime, PerformanceMeasure,
)

logger = logging.getLogger(__name__)

CONFIDENCE_DIRECT_R: float = 1.0
CONFIDENCE_FROM_T: float = 0.8
CONFIDENCE_FROM_BETA: float = 0.6
CONFIDENCE_REVIEW_THRESHOLD: float = 0.7

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
  "sample_n": <int|null>, "effect_r": <float|null>, "effect_t": <float|null>,
  "effect_beta": <float|null>, "effect_df": <int|null>, "p_value": <float|null>,
  "ci_lower": <float|null>, "ci_upper": <float|null>,
  "doi_measure": <"FSTS"|"entropy"|"n_markets"|"TNI"|null>,
  "performance_measure": <"ROA"|"ROE"|"ROS"|"TobinsQ"|"composite"|"other"|null>,
  "icrv_regime": <"I"|"II"|"III"|"SIDS"|"V"|"pooled"|null>,
  "dpl_phase": <"Precede"|"Span"|"Follow"|null>,
  "cdai_score": <float|null>
}

Rules:
1. Prefer the main/fully-specified model if multiple models are reported.
2. Prefer Pearson r over t over β for the primary effect size.
3. Encode p-value inequalities as boundary value (e.g. "p < .001" → 0.001).
4. Preserve sign for negative t or β.
5. Never hallucinate statistics; return null for any field not found.
"""


class StatisticalExtractor:
    """Wraps an Anthropic client to extract effect sizes from PDF text."""

    def __init__(self, api_key: str) -> None:
        self._client = anthropic.Anthropic(api_key=api_key)

    def extract_from_text(self, text: str, metadata: dict[str, Any]) -> ExtractedEffect:
        raw = self._call_llm(text, metadata)
        return self._build_effect(raw, metadata)

    @staticmethod
    def compute_r_from_t(t: float, df: int) -> float:
        """Convert t-statistic to Pearson's r (Peterson & Brown, 2005):
           r = sqrt(t² / (t² + df)), sign preserved from t."""
        t_sq = t * t
        r_unsigned = math.sqrt(t_sq / (t_sq + df))
        return r_unsigned if t >= 0 else -r_unsigned

    @staticmethod
    def convert_beta_to_r(beta: float) -> float:
        """Approximate r from standardised β (Peterson & Brown, 2005):
           r ≈ β × 0.98"""
        return beta * 0.98

    def _call_llm(self, text: str, metadata: dict[str, Any]) -> dict[str, Any]:
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
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]
        try:
            return json.loads(raw_text)
        except json.JSONDecodeError as exc:
            logger.error("Failed to parse LLM JSON output: %s\n%s", exc, raw_text)
            return {}

    def _build_effect(self, raw: dict[str, Any], metadata: dict[str, Any]) -> ExtractedEffect:
        effect_r = raw.get("effect_r")
        effect_t = raw.get("effect_t")
        effect_beta = raw.get("effect_beta")
        effect_df = raw.get("effect_df")
        if effect_r is not None:
            computed_r, confidence = effect_r, CONFIDENCE_DIRECT_R
        elif effect_t is not None and effect_df is not None:
            computed_r = self.compute_r_from_t(effect_t, effect_df)
            confidence = CONFIDENCE_FROM_T
        elif effect_beta is not None:
            computed_r = self.convert_beta_to_r(effect_beta)
            confidence = CONFIDENCE_FROM_BETA
        else:
            computed_r, confidence = None, 0.0
        requires_verification = confidence < CONFIDENCE_REVIEW_THRESHOLD
        return ExtractedEffect(
            study_id=str(uuid.uuid4()),
            paper_title=metadata.get("title", ""),
            authors=metadata.get("authors", ""),
            year=int(metadata.get("year", 0)),
            country=metadata.get("country", ""),
            sample_n=int(raw["sample_n"]) if raw.get("sample_n") is not None else None,
            effect_r=computed_r,
            effect_t=effect_t,
            effect_beta=effect_beta,
            effect_df=int(effect_df) if effect_df is not None else None,
            p_value=float(raw["p_value"]) if raw.get("p_value") is not None else None,
            ci_lower=float(raw["ci_lower"]) if raw.get("ci_lower") is not None else None,
            ci_upper=float(raw["ci_upper"]) if raw.get("ci_upper") is not None else None,
            doi_measure=_safe_literal(raw.get("doi_measure"), ("FSTS","entropy","n_markets","TNI")),
            performance_measure=_safe_literal(raw.get("performance_measure"),
                                              ("ROA","ROE","ROS","TobinsQ","composite","other")),
            icrv_regime=_safe_literal(raw.get("icrv_regime"), ("I","II","III","SIDS","V","pooled")),
            dpl_phase=_safe_literal(raw.get("dpl_phase"), ("Precede","Span","Follow")),
            cdai_score=float(raw["cdai_score"]) if raw.get("cdai_score") is not None else None,
            extraction_confidence=confidence,
            requires_verification=requires_verification,
            pi_locked=False,
            extracted_at=datetime.utcnow(),
            locked_at=None,
        )


def _safe_literal(value: Any, allowed: tuple[str, ...]) -> str | None:
    return value if isinstance(value, str) and value in allowed else None
```

---

## FILE 3: frontend/src/App.tsx (React 18 Root Component)

```typescript
// =============================================================================
// M-AIDA: Meta-Analysis Intelligent Data Assistant
// =============================================================================
// Version   : 7.0.0
// Copyright : © [Năm] [Tên tác giả đầy đủ]. All rights reserved.
// Author    : [Tên tác giả]
// License   : Proprietary — Research Use Only
// =============================================================================
/**
 * M-AIDA v7.0 — Root application component.
 *
 * Two-tab layout:
 *   1. Extract       — PDF upload and LLM extraction (ExtractionPanel)
 *   2. Verify & Lock — PI verification dashboard (VerificationDashboard + ExportPanel)
 */

import React, { useCallback, useState } from "react";
import ExportPanel from "./components/ExportPanel";
import ExtractionPanel from "./components/ExtractionPanel";
import VerificationDashboard from "./components/VerificationDashboard";
import { StudyDatabaseEntry } from "./types";
import "./index.css";

type Tab = "extract" | "verify";

export default function App() {
  const [activeTab, setActiveTab] = useState<Tab>("extract");
  const [extractionCount, setExtractionCount] = useState(0);

  const handleExtracted = useCallback((_entry: StudyDatabaseEntry) => {
    setExtractionCount((c) => c + 1);
  }, []);

  const switchToVerify = useCallback(() => {
    setActiveTab("verify");
  }, []);

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-brand">
          <h1 className="app-title">M-AIDA</h1>
          <span className="app-version">v7.0</span>
        </div>
        <p className="app-subtitle">
          Meta-Analysis Intelligent Data Assistant — Internationalization &amp; Performance
        </p>
      </header>

      <nav className="tab-nav" role="tablist">
        <button
          role="tab"
          aria-selected={activeTab === "extract"}
          className={`tab-btn ${activeTab === "extract" ? "active" : ""}`}
          onClick={() => setActiveTab("extract")}
        >
          Extract
        </button>
        <button
          role="tab"
          aria-selected={activeTab === "verify"}
          className={`tab-btn ${activeTab === "verify" ? "active" : ""}`}
          onClick={() => setActiveTab("verify")}
        >
          Verify &amp; Lock
          {extractionCount > 0 && (
            <span className="tab-badge">{extractionCount}</span>
          )}
        </button>
      </nav>

      <main className="app-main">
        {activeTab === "extract" && (
          <div className="tab-content">
            <ExtractionPanel onExtracted={handleExtracted} />
            {extractionCount > 0 && (
              <div className="extraction-prompt">
                <p>
                  {extractionCount} paper{extractionCount !== 1 ? "s" : ""} extracted
                  this session.
                </p>
                <button className="btn btn-link" onClick={switchToVerify}>
                  Go to Verify &amp; Lock
                </button>
              </div>
            )}
          </div>
        )}
        {activeTab === "verify" && (
          <div className="tab-content verify-tab">
            <VerificationDashboard />
            <ExportPanel />
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>
          M-AIDA v7.0 · PhD Dissertation Research Tool · Asia-Pacific I→P Meta-Analysis
        </p>
      </footer>
    </div>
  );
}
```

---

## FILE 4: backend/models.py (Pydantic Data Models)

```python
# =============================================================================
# M-AIDA: Meta-Analysis Intelligent Data Assistant
# =============================================================================
# Version   : 7.0.0
# Copyright : © [Năm] [Tên tác giả đầy đủ]. All rights reserved.
# Author    : [Tên tác giả]
# License   : Proprietary — Research Use Only
# =============================================================================
"""Pydantic data models for M-AIDA v7.0."""

from __future__ import annotations
from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

DoiMeasure = Literal["FSTS", "entropy", "n_markets", "TNI"]
PerformanceMeasure = Literal["ROA", "ROE", "ROS", "TobinsQ", "composite", "other"]
IcrvRegime = Literal["I", "II", "III", "SIDS", "V", "pooled"]
DplPhase = Literal["Precede", "Span", "Follow"]


class ExtractedEffect(BaseModel):
    study_id: str = Field(..., description="UUID assigned at extraction time")
    paper_title: str
    authors: str
    year: int
    country: str
    sample_n: int | None = None
    effect_r: float | None = None
    effect_t: float | None = None
    effect_beta: float | None = None
    effect_df: int | None = None
    p_value: float | None = None
    ci_lower: float | None = None
    ci_upper: float | None = None
    doi_measure: DoiMeasure | None = None
    performance_measure: PerformanceMeasure | None = None
    icrv_regime: IcrvRegime | None = None
    cdai_score: float | None = Field(None, ge=0.0, le=10.0)
    dpl_phase: DplPhase | None = None
    extraction_confidence: float = Field(..., ge=0.0, le=1.0)
    requires_verification: bool
    pi_locked: bool = False
    extracted_at: datetime = Field(default_factory=datetime.utcnow)
    locked_at: datetime | None = None


class ExtractionRequest(BaseModel):
    pdf_content: str = Field(..., description="Base64-encoded PDF binary content")
    paper_metadata: dict = Field(default_factory=dict)


class VerificationDecision(BaseModel):
    study_id: str
    field_overrides: dict = Field(default_factory=dict)
    pi_approved: bool = False
    pi_notes: str = ""


class StudyDatabaseEntry(ExtractedEffect):
    notion_page_id: str | None = None
    pi_notes: str = ""
```

---

*Ghi chú: Mã nguồn trên đây bao gồm các file chính của M-AIDA v7.0.0. Trước khi nộp hồ sơ:*
*1. Điền [Năm], [Tên tác giả đầy đủ] vào tất cả copyright headers*
*2. In tài liệu này (4–6 trang) kèm theo hồ sơ đăng ký*
*3. Giữ bản điện tử làm backup*
