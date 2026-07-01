# Ma trận format theo tạp chí (house-style) — chuẩn nộp

> Áp cho mọi submission package. Abstract + tham chiếu + LaTeX theo từng nhà XB.

| Publisher | Tạp chí (paper) | Abstract | Tham chiếu | LaTeX class | Nộp |
|---|---|---|---|---|---|
| **Emerald** | JED(P3) · MBR(P3/P4) · JABS(P3/P9) · IJOEM(P5/P9) · CMS(P5) | **Structured** (Purpose/Design/Findings/Research limitations/Practical implications/Originality), ≤250 từ | Emerald Harvard | — (Word/ScholarOne) | DOCX |
| **Springer** | MIR(P4/P9) · APJM(P6/P7) · ABM(P10) · EJDR(P8) | Unstructured ≤250 từ | APA 7 | `svjour3` (article fallback) | DOCX + LaTeX |
| **Elsevier** | JWB(P6) · JIM(P6) · IBR(P7) · World Development(P8) | Unstructured | APA 7 | `elsarticle` (native) | DOCX + LaTeX |
| **Taylor & Francis** | APBR(P4/P5) | Unstructured ~200 từ | APA 7 (T&F) | `interact` (article fallback) | DOCX + LaTeX |
| **Wiley** | JID(P8) · Thunderbird(P3, deprecated) | Unstructured | APA 7 | `WileyNJD-v2` (article fallback) | DOCX + LaTeX |
| **Palgrave** | JIBS(P7, deprecated) | Unstructured | APA 7 | Springer Nature class | DOCX + LaTeX |

**LaTeX:** sinh bằng `scripts/build_journal_latex.py` từ `01_manuscript_blinded*.md` → `04_manuscript_latex.{tex,pdf}` trong package. Container chỉ có `elsarticle`; Springer/T&F/Wiley dùng article-fallback để xác minh PDF, kèm ghi chú swap class (.cls chính thức) cho bản nộp cuối.
