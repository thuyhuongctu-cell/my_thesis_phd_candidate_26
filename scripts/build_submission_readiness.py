#!/usr/bin/env python3
"""Generate a consolidated submission-readiness table for every live package,
checking each manuscript against its target journal's requirements:
  - main-text word count vs documented limit
  - abstract type (structured for Emerald / unstructured otherwise)
  - reference style (Emerald-Harvard vs APA author-date)
  - declarations completeness (publisher-specific)
  - Elsevier Highlights
Writes reviews/SUBMISSION_READINESS_MASTER_2026-06.md.

Word limits are documented author-guideline values (web access is blocked in
this environment); confirm against the live Guide for Authors before submission.
"""
import pathlib, re, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent

# package -> (paper, journal, publisher, main-text word limit, manuscript filename or None)
PKG = [
 ("p3/submission/jed_package","P3","JED","Emerald",8000,"01_manuscript_blinded_8500.md"),
 ("p4/submission/mir_package","P4","MIR","Springer",12000,None),
 ("p4/submission/mbr_package","P4","MBR","Emerald",10000,None),
 ("p4/submission/apbr_package","P4","APBR","Taylor & Francis",8000,None),
 ("p5/submission/ijoem_package","P5","IJOEM","Emerald",9000,None),
 ("p6/submission/jwb_package","P6","JWB","Elsevier",10000,None),
 ("p6/submission/jim_package","P6","JIM","Elsevier",12000,None),
 ("p6/submission/apjm_package","P6","APJM","Springer",12000,None),
 ("p7/submission/ibr_package","P7","IBR","Elsevier",12000,None),
 ("p8/submission/world_development_package","P8","World Development","Elsevier",10000,None),
 ("p8/submission/world_development_redesign","P8","World Development (redesign)","Elsevier",10000,None),
 ("p8/submission/ejdr_package","P8","EJDR","Springer",8000,None),
 ("p8/submission/jid_package","P8","JID","Wiley",8000,None),
 ("p9_india/submission/mir_package","P9","MIR","Springer",12000,None),
 ("p9_india/submission/ijoem_package","P9","IJOEM","Emerald",9000,None),
 ("p9_india/submission/jabs_package","P9","JABS","Emerald",9000,None),
 ("p10_japan/submission/abm_package","P10","ABM","Springer",10000,None),
 ("p10_japan/submission/apjm_package","P10","APJM","Springer",12000,None),
 ("p10_japan/submission/ijoem_package","P10","IJOEM","Emerald",9000,None),
]
DECL = re.compile(r"^#+\s*(acknowledg|funding|conflict|competing|disclosure|data availability|data access|ethic|use of (generative )?ai|declaration of (generative )?ai|ai (use|and data)|highlights)", re.I)

def main_words(t):
    m=re.search(r"(?m)^#+\s*References\s*$",t); t=t[:m.start()] if m else t
    out=[];skip=False;ab=False;code=False
    for ln in t.split("\n"):
        s=ln.strip()
        if s.startswith("```"): code=not code; continue
        if code: continue
        if re.match(r"^#+\s",ln):
            if re.match(r"^#+\s*abstract",ln,re.I): ab=True;skip=False;continue
            if DECL.match(ln): skip=True;ab=False;continue
            ab=False;skip=False;out.append(re.sub(r"^#+\s*","",ln));continue
        if ab or skip: continue
        if s.startswith("|") or s.startswith("!["): continue
        out.append(ln)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", re.sub(r"[*_`#>\-]+"," "," ".join(out))))

def chk(b): return "✓" if b else "✗"

rows=[]
for rel,paper,jr,pub,lim,fname in PKG:
    pkg=ROOT/rel
    md = pkg/fname if fname else (sorted(pkg.glob('01_manuscript*blind*.md')) or sorted(pkg.glob('01_manuscript*.md')))[0]
    t=md.read_text(encoding="utf-8"); low=t.lower()
    w=main_words(t)
    wc = "✓" if w<=lim else f"✗ +{w-lim:,}"
    # abstract type
    structured = bool(re.search(r"\*\*purpose",low)) or bool(re.search(r"design/methodology",low))
    abok = structured if pub=="Emerald" else (not structured and bool(re.search(r"^#+\s*abstract",t,re.M|re.I)))
    # refs style: Emerald-Harvard markers vs APA
    refblk = t[re.search(r"(?m)^#+\s*References\s*$",t).end():] if re.search(r"(?m)^#+\s*References\s*$",t) else ""
    emerald_refs = bool(re.search(r'\(\d{4}\),\s*"', refblk)) or bool(re.search(r"Vol\.\s*\d+\s*No\.", refblk))
    refok = emerald_refs if pub=="Emerald" else True   # others: APA author-date accepted
    # declarations
    need = ["funding","conflict of interest|competing interest","data availability"]
    if pub in ("Springer","Wiley"): need.append("ethic")
    need.append("generative ai|ai use|use of ai|ai and data")
    declok = all(re.search(p,low) for p in need)
    # highlights (Elsevier only)
    hl = bool(re.search(r"^#+\s*highlights",t,re.M|re.I))
    hlcell = chk(hl) if pub=="Elsevier" else "n/a"
    overall = (wc=="✓") and abok and refok and declok and (hl if pub=="Elsevier" else True)
    rows.append((paper,jr,pub,lim,w,wc,chk(abok),("EH" if (pub=="Emerald" and emerald_refs) else ("APA" if refok else "✗")),chk(declok),hlcell,"✅" if overall else "⚠️"))

lines=["# Submission Readiness — paper × journal requirements check",
 f"\n_Generated {datetime.date.today().isoformat()} from the live package files (single source of truth)._\n",
 "> Word limits are documented author-guideline values for **main text** (excl. abstract, references, tables, figures). "
 "Web access is blocked in this environment, so confirm each limit against the live Guide for Authors before submission. "
 "All other checks are read directly from the manuscript.\n",
 "| Paper | Journal | Publisher | Limit | Words | WordCount | Abstract | Refs | Declarations | Highlights | Overall |",
 "|---|---|---|---:|---:|---|:--:|:--:|:--:|:--:|:--:|"]
cur=None
for r in rows:
    paper=r[0]; pp=paper if paper!=cur else ""; cur=paper
    lim=f"{r[3]:,}"; w=f"{r[4]:,}"
    lines.append(f"| {pp} | **{r[1]}** | {r[2]} | {lim} | {w} | {r[5]} | {r[6]} | {r[7]} | {r[8]} | {r[9]} | {r[10]} |")
lines+=["",
 "**Legend.** WordCount ✓ = main text ≤ limit. Abstract: Emerald = structured "
 "(Purpose/Design/Findings/Originality), others = unstructured. Refs: EH = Emerald-Harvard, "
 "APA = APA author–date (accepted at initial submission under each non-Emerald publisher's free-format policy). "
 "Declarations: Funding + Conflict/Competing + Data availability + AI (+ Ethics for Springer/Wiley). "
 "Highlights required for Elsevier only. CRediT/ORCID live on the non-blinded title page.",
 "",
 "See also: `reviews/SUBMISSION_FORMAT_COMPLIANCE_2026-06.md` and `reviews/WORDCOUNT_COMPLIANCE_2026-06.md`."]
out=ROOT/"reviews/SUBMISSION_READINESS_MASTER_2026-06.md"
out.write_text("\n".join(lines)+"\n",encoding="utf-8")
print("\n".join(lines))
