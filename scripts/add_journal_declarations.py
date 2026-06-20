#!/usr/bin/env python3
"""Ensure each live submission package's blinded manuscript carries the
declaration sections required by its target publisher, with publisher-correct
headings and double-blind-safe (name-free) wording. Only MISSING sections are
inserted (immediately before the References heading); existing sections are left
untouched.

Usage:
  python3 scripts/add_journal_declarations.py [--write]
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# package path -> (publisher, paper_key)
PKG_PUB = {
    "p3/submission/jed_package": ("Emerald", "p3"),
    "p4/submission/apbr_package": ("TaylorFrancis", "p4"),
    "p4/submission/mbr_package": ("Emerald", "p4"),
    "p4/submission/mir_package": ("Springer", "p4"),
    "p5/submission/ijoem_package": ("Emerald", "p5"),
    "p6/submission/apjm_package": ("Springer", "p6"),
    "p6/submission/jim_package": ("Elsevier", "p6"),
    "p6/submission/jwb_package": ("Elsevier", "p6"),
    "p7/submission/ibr_package": ("Elsevier", "p7"),
    "p8/submission/ejdr_package": ("Springer", "p8"),
    "p8/submission/jid_package": ("Wiley", "p8"),
    "p8/submission/world_development_package": ("Elsevier", "p8"),
    "p8/submission/world_development_redesign": ("Elsevier", "p8"),
    "p9_india/submission/ijoem_package": ("Emerald", "p9"),
    "p9_india/submission/jabs_package": ("Emerald", "p9"),
    "p9_india/submission/mir_package": ("Springer", "p9"),
    "p10_japan/submission/abm_package": ("Springer", "p10"),
    "p10_japan/submission/apjm_package": ("Springer", "p10"),
    "p10_japan/submission/ijoem_package": ("Emerald", "p10"),
}

# paper_key -> (data-acknowledgement coverage, data-availability coverage)
PAPER = {
    "p3": ("WBES Vietnam 2009, 2015, and 2023",
           "The World Bank Enterprise Survey (WBES) microdata for Vietnam (2009, 2015, and 2023) analysed in this study are publicly available at https://www.enterprisesurveys.org subject to World Bank registration. Replication materials are available from the authors upon reasonable request, to the extent permitted by the WBES Data Access Protocol."),
    "p4": ("WBES Singapore 2023 (B-READY)",
           "The World Bank Enterprise Survey (WBES) microdata for Singapore (2023) analysed in this study are publicly available at https://www.enterprisesurveys.org subject to World Bank registration. Replication materials are available from the authors upon reasonable request, to the extent permitted by the WBES Data Access Protocol."),
    "p5": ("WBES China 2012 and 2024",
           "The World Bank Enterprise Survey (WBES) microdata for China (2012 and 2024) analysed in this study are publicly available at https://www.enterprisesurveys.org subject to World Bank registration. Replication materials are available from the authors upon reasonable request, to the extent permitted by the WBES Data Access Protocol."),
    "p6": (None,  # meta-analysis: handled specially
           "All data supporting the findings of this meta-analysis — the coded effect-size database, the PRISMA records, and the analysis scripts — are available from the authors upon reasonable request. The primary studies underlying the synthesis are listed in the references and the supplementary material."),
    "p7": ("WBES microdata for the Asian and Pacific economies analysed (including Japan 2025)",
           "The World Bank Enterprise Survey (WBES) microdata for the Asian and Pacific economies analysed in this study (including Japan 2025) are publicly available at https://www.enterprisesurveys.org subject to World Bank registration. Replication materials are available from the authors upon reasonable request, to the extent permitted by the WBES Data Access Protocol."),
    "p8": ("WBES microdata for the Pacific Small Island Developing States analysed",
           "The World Bank Enterprise Survey (WBES) microdata for the Pacific Small Island Developing States analysed in this study are publicly available at https://www.enterprisesurveys.org subject to World Bank registration. Replication materials are available from the authors upon reasonable request, to the extent permitted by the WBES Data Access Protocol."),
    "p9": ("WBES India 2014, 2022, and 2025",
           "The World Bank Enterprise Survey (WBES) microdata for India (2014, 2022, and 2025) analysed in this study are publicly available at https://www.enterprisesurveys.org subject to World Bank registration. Replication materials are available from the authors upon reasonable request, to the extent permitted by the WBES Data Access Protocol."),
    "p10": ("WBES Japan 2025 (first survey wave)",
            "The World Bank Enterprise Survey (WBES) microdata for Japan (2025) analysed in this study are publicly available at https://www.enterprisesurveys.org subject to World Bank registration. Replication materials are available from the authors upon reasonable request, to the extent permitted by the WBES Data Access Protocol."),
}

FUNDING = ("This research received no specific grant from any funding agency in "
           "the public, commercial, or not-for-profit sectors.")
ETHICS = ("This study analyses secondary, de-identified, publicly available "
          "firm-level survey data (World Bank Enterprise Surveys) and did not "
          "involve human participants or animals; ethics approval was not required.")
AI_DISCLOSURE = ("During the preparation of this work the authors used generative AI "
                 "tools to assist with language editing and formatting. The authors "
                 "reviewed and edited the content as needed and take full "
                 "responsibility for the content of the publication.")

COMPETING = {
    "Elsevier": "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.",
    "Springer": "The authors have no relevant financial or non-financial competing interests to declare.",
    "Emerald": "The authors declare no conflict of interest.",
    "Wiley": "The authors declare no conflict of interest.",
    "TaylorFrancis": "No potential conflict of interest was reported by the authors.",
}

def ack_text(paper_key):
    if paper_key == "p6":
        return ("The authors thank the authors of the primary studies synthesised in "
                "this meta-analysis. Where World Bank Enterprise Survey data informed "
                "primary estimates, the original collectors, the authorised distributor, "
                "and the relevant funding agencies bear no responsibility for the use of "
                "the data or for interpretations based upon such uses.")
    cov = PAPER[paper_key][0]
    return (f"The authors thank the Enterprise Analysis Unit of the Development "
            f"Economics Global Indicators Group of the World Bank for the {cov} data. "
            f"The original collector of the data, the authorised distributor, and the "
            f"relevant funding agency bear no responsibility for the use of the data or "
            f"for interpretations or inferences based upon such uses.")

# publisher -> ordered list of concept keys
ORDER = {
    "Emerald": ["funding", "conflict", "data", "ai"],
    "Springer": ["ack", "funding", "competing", "ethics", "data", "ai"],
    "Elsevier": ["ack", "funding", "competing", "data", "ai"],
    "Wiley": ["ack", "funding", "conflict", "ethics", "data", "ai"],
    "TaylorFrancis": ["ack", "funding", "disclosure", "data", "ai"],
}

# concept -> (heading text by publisher, detection regex, body builder)
def heading_for(concept, pub):
    H = {
        "ack": "Acknowledgements",
        "funding": "Funding",
        "ethics": {"Wiley": "Ethics Statement"}.get(pub, "Ethics approval"),
        "data": {"Wiley": "Data Availability Statement", "Elsevier": "Data availability"}.get(pub, "Data availability statement"),
        "ai": "Declaration of Generative AI in the Writing Process",
        "conflict": "Conflict of Interest",
        "competing": "Competing interests" if pub == "Springer" else "Declaration of competing interest",
        "disclosure": "Disclosure statement",
    }
    return H[concept]

DETECT = {
    "ack": r"acknowledg",
    "funding": r"\bfunding\b",
    "ethics": r"ethic",
    "data": r"data availability|data access",
    "ai": r"generative ai|use of ai|ai[ -]assisted",
    "conflict": r"conflict of interest|competing interest",
    "competing": r"competing interest|conflict of interest|declaration of competing",
    "disclosure": r"disclosure statement|conflict of interest|competing interest",
}

def body_for(concept, pub, paper_key):
    if concept == "ack":
        return ack_text(paper_key)
    if concept == "funding":
        return FUNDING
    if concept == "ethics":
        return ETHICS
    if concept == "data":
        return PAPER[paper_key][1]
    if concept == "ai":
        return AI_DISCLOSURE
    return COMPETING[pub]


def process(path: pathlib.Path, pub: str, paper_key: str):
    text = path.read_text(encoding="utf-8")
    low = text.lower()
    added = []
    blocks = []
    for concept in ORDER[pub]:
        if re.search(DETECT[concept], low):
            continue
        h = heading_for(concept, pub)
        b = body_for(concept, pub, paper_key)
        blocks.append(f"## {h}\n\n{b}\n")
        added.append(h)
    if not blocks:
        return text, []
    insertion = "\n".join(blocks) + "\n"
    m = re.search(r"(?m)^#+\s*References\s*$", text)
    if m:
        new_text = text[: m.start()] + insertion + text[m.start():]
    else:
        new_text = text.rstrip() + "\n\n" + insertion
    return new_text, added


def main():
    write = "--write" in sys.argv
    for rel, (pub, pk) in PKG_PUB.items():
        pkg = ROOT / rel
        md = sorted(pkg.glob("01_manuscript*blind*.md")) or sorted(pkg.glob("01_manuscript*.md"))
        if not md:
            print(f"!! {rel}: no manuscript md"); continue
        md = md[0]
        new_text, added = process(md, pub, pk)
        tag = f"[{pub}]"
        if added:
            print(f"{tag:14} {rel}/{md.name}  +ADD: {', '.join(added)}")
            if write:
                md.write_text(new_text, encoding="utf-8")
        else:
            print(f"{tag:14} {rel}/{md.name}  (complete)")


if __name__ == "__main__":
    main()
