# Estructura del manuscrito PRISMA 2020 (journal format)

> Plantilla autoritativa para `compile_docx.py`. Cada sección mapea a items PRISMA específicos.

## Estructura

```
TITLE PAGE
  - Title (Item 1)  ← debe contener "systematic review"
  - Authors, affiliations
  - Corresponding author + ORCID
  - Word count, # tables, # figures

ABSTRACT (Item 2 — PRISMA Abstracts checklist)
  - Background
  - Objectives
  - Data Sources
  - Study Eligibility Criteria
  - Participants and Interventions
  - Study Appraisal and Synthesis Methods
  - Results
  - Limitations
  - Conclusions
  - Registration (PROSPERO CRD)
  - Keywords (4–6)

1. INTRODUCTION
   1.1 Rationale (Item 3)
   1.2 Objectives (Item 4)

2. METHODS
   2.1 Protocol and registration (Item 24)
   2.2 Eligibility criteria (Item 5)
   2.3 Information sources (Item 6)
   2.4 Search strategy (Item 7)
   2.5 Selection process (Item 8)
   2.6 Data collection process (Item 9)
   2.7 Data items (Items 10a, 10b)
   2.8 Study risk of bias assessment (Item 11)
   2.9 Effect measures (Item 12)
   2.10 Synthesis methods (Items 13a–f)
   2.11 Reporting bias assessment (Item 14)
   2.12 Certainty assessment (Item 15)

3. RESULTS
   3.1 Study selection (Items 16a, 16b) ← incluye PRISMA flow diagram (Figura 1)
   3.2 Study characteristics (Item 17) ← Tabla 1
   3.3 Risk of bias in studies (Item 18) ← Figura 2 (traffic light) o Tabla 2
   3.4 Results of individual studies (Item 19)
   3.5 Results of syntheses (Items 20a–d)
   3.6 Reporting biases (Item 21)
   3.7 Certainty of evidence (Item 22) ← Tabla SoF

4. DISCUSSION
   4.1 Summary of evidence (Item 23a)
   4.2 Limitations of the evidence (Item 23b)
   4.3 Limitations of the review process (Item 23c)
   4.4 Implications (Item 23d)

5. CONCLUSIONS

DECLARATIONS
  - Funding (Item 25)
  - Competing interests (Item 26)
  - Data availability (Item 27)
  - AI tools used (PRISMA-trAIce reference)
  - Author contributions
  - Acknowledgements

REFERENCES (rellenas por Zotero RTF/ODF Scan)

TABLES (en páginas separadas)
  Tabla 1 — Características de estudios incluidos
  Tabla 2 — RoB por estudio
  Tabla SoF — Summary of Findings (GRADE)

FIGURES (en páginas separadas)
  Figura 1 — PRISMA 2020 flow diagram
  Figura 2 — Forest plot (si MA)
  Figura 3 — Funnel plot (si MA con ≥10 estudios)
  Figura 4 — Risk of bias summary

APPENDICES
  Apéndice A — Estrategias completas de búsqueda por base
  Apéndice B — Lista de estudios excluidos en full-text con razón
  Apéndice C — Checklist PRISMA 2020 completa
  Apéndice D — Checklist PRISMA-trAIce (si IA usada)
  Apéndice E — Data extraction form
```

## Convenciones de redacción

- **Registro académico**: sin coloquialismos. "Studies were screened" mejor que "We screened".
- **Tiempos verbales**: pasado para métodos y resultados; presente para conocimiento establecido y discusión.
- **Toda afirmación lleva cita**: marcadores `{|Author Year|}` que Zotero convertirá.
- **Tablas**: título encima; "Tabla 1\n*Título en cursiva*".
- **Figuras**: caption debajo.
- **No bullet points en el cuerpo**: prosa continua. Excepciones: tabla de elegibilidad y PRISMA flow.

## Antes de inyectar prosa larga

**Invoca skill `humanizer`** sobre cualquier sección de Introduction, Discussion o Conclusions
de >2 párrafos. Es regla del usuario y mejora claramente la naturalidad.

## Después de generar el .docx

1. Abrir en Word con Zotero plugin.
2. Edit → RTF/ODF Scan.
3. Mapear `{|Author Year|}` a la colección Zotero "SR — <slug>".
4. Zotero genera References automáticamente al final.
