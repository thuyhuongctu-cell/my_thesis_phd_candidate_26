# PRISMA-trAIce — Checklist para reportar uso de IA en revisiones sistemáticas (17 items)

> Fuente: Holst D, et al. Transparent Reporting of AI in Systematic Literature Reviews:
> Development of the PRISMA-trAIce Checklist. JMIR AI. 2025. doi:[10.2196/80247](https://doi.org/10.2196/80247).
>
> Es un **estándar emergente** ("foundational proposal", no consenso Delphi formal).
> Cada vez más revistas (BMJ AI, Lancet Digital Health, JMIR AI) lo piden o lo recomiendan.

Aplicar cuando la skill ha ejecutado cribado o extracción asistida por IA.

## Tiers
- **M** (Mandatory): bloquea aceptación si falla.
- **HR** (Highly Recommended).
- **R** (Recommended).
- **O** (Optional).

## TITLE / ABSTRACT / INTRODUCTION

| # | Item | Tier | Qué reportar |
|---|------|------|--------------|
| T1 | Title | O | Indicar uso de IA en el título o subtítulo si jugó un rol sustancial. |
| A1 | Abstract | O | Resumir tool(s) de IA usadas y las etapas de la review en las que se aplicaron. |
| I1 | Introduction | R | Justificación de por qué se usó IA para tareas específicas. |

## METHODS

| # | Item | Tier | Qué reportar |
|---|------|------|--------------|
| M1 | Protocol registration | **M** | Si el uso de IA estaba pre-especificado en el protocolo, y documentar desviaciones. |
| M2 | Tool identification | **M** | Nombre, versión, proveedor/desarrollador de cada tool; URL del repositorio o DOI si es open-source. |
| M3 | Purpose and stage | **M** | Etapa específica de la RS y tarea precisa que realizó la IA. |
| M4 | Input data | **M** | Datos proporcionados a la IA (training, fine-tuning); o declarar explícitamente que no hubo fine-tuning. |
| M5 | Output data | **M** | Formato de salida (JSON, scores) y cualquier post-procesado automatizado. |
| M6 | Prompt engineering | **M** | Proceso, prompts completos y parámetros clave (model, temperature, top_p, max tokens) para LLMs. |
| M7 | Operational details | HR | Algoritmos y hyperparameters para ML clásico (ASReview, Abstrackr, etc.). |
| M8 | Human-AI interaction | **M** | Número de revisores, sus cualificaciones, mecanismo de supervisión (e.g. doble revisión independiente, adjudicación). |
| M9 | AI performance evaluation methods | **M** | Métricas usadas (sensibilidad, agreement, Cohen's κ) y reference standard. |
| M10 | Data management | R | Almacenamiento, privacidad, GDPR/IRB. |

## RESULTS

| # | Item | Tier | Qué reportar |
|---|------|------|--------------|
| R1 | Study selection (AI-assisted) | **M** | En PRISMA flow diagram o texto, **distinguir** entre records gestionados por IA vs. revisores humanos. |
| R2 | AI performance metrics | **M** | Resultados numéricos de las evaluaciones (referenciar M9). |

## DISCUSSION

| # | Item | Tier | Qué reportar |
|---|------|------|--------------|
| D1 | Limitations of AI use | R | ≥1 párrafo dedicado a limitaciones de la IA (técnicas, sesgos, hallucinations) y su impacto. |
| D2 | Implications of AI use | O | Reflexión forward-looking sobre la utilidad de la IA para futuras revisiones. |

## Plantilla rellena para esta skill (copia y edita)

```
Tool: Claude (model claude-opus-4-7), Anthropic.
Version: opus-4-7 (1M context), via Claude Code CLI.
Stage applied:
  - Search query optimization (Phase 2)
  - First-pass screening by keyword rules (Phase 6)
  - Second-pass title/abstract screening (IA proposes, human confirms, Phase 7)
Prompt: see https://github.com/<este SKILL.md> for full instructions.
Parameters: temperature default (Claude Code), no fine-tuning.
Human oversight: dual review of every Pass 2 decision by [autor X] and [autor Y].
Discrepancies: resolved by consensus with senior reviewer [Z].
Performance evaluation: random sample of N=50 decisions audited by [autor], agreement κ=[?].
Output: master_corpus.xlsx + screening_pass1_log.csv + screening_pass2_log.csv (auditables).
Limitations: keyword rules pueden excluir estudios con terminología no canónica;
  abstract-only screening puede fallar con papers cuyo abstract subreporta el design.
```
