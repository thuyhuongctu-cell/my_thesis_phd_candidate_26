#!/usr/bin/env python3
"""Genera diagrama PRISMA 2020 (Template B: database + other sources) en PNG.

Usa matplotlib. Lee contadores de project_state.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def make_box(ax, x, y, w, h, text, color="#e8eef5"):
    rect = mpatches.FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.02", linewidth=1.2,
        edgecolor="#2c5777", facecolor=color,
    )
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=9, wrap=True)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("project_dir")
    args = p.parse_args()

    proj = Path(args.project_dir)
    state = json.loads((proj / "project_state.json").read_text())
    c = state.get("counts", {})

    n_pubmed = c.get("identificados_pubmed", 0)
    n_s2 = c.get("identificados_semantic_scholar", 0)
    n_oa = c.get("identificados_openalex", 0)
    n_wos = c.get("identificados_wos", 0)
    n_em = c.get("identificados_embase", 0)
    n_consensus = c.get("identificados_consensus", 0)
    n_other = n_consensus  # grey lit / consensus

    n_db_total = n_pubmed + n_s2 + n_oa + n_wos + n_em
    n_dup = c.get("duplicados", 0)
    n_unique = c.get("unicos", n_db_total - n_dup)
    n_screened = n_unique
    n_excl_p1 = c.get("pass1_exclude", 0)
    n_excl_p2 = c.get("pass2_exclude", 0)
    n_ft_obtained = c.get("full_text_obtained", 0)
    n_ft_excluded = c.get("full_text_excluded", 0)
    n_included = c.get("incluidos_final", 0)

    fig, ax = plt.subplots(figsize=(14, 11))
    ax.set_xlim(0, 14); ax.set_ylim(0, 14)
    ax.axis("off")

    # Identification
    ax.text(7, 13.5, "Identification", fontsize=12, fontweight="bold", ha="center", color="#2c5777")
    make_box(ax, 1, 11.5, 5.5, 1.5,
             f"Records identified from databases (n={n_db_total})\n"
             f"  PubMed (n={n_pubmed})\n"
             f"  Semantic Scholar (n={n_s2})\n"
             f"  OpenAlex (n={n_oa})\n"
             f"  WoS (n={n_wos})  Embase (n={n_em})", color="#dfeaf3")
    make_box(ax, 7.5, 11.5, 5.5, 1.5,
             f"Records identified from other sources (n={n_other})\n  Consensus (n={n_consensus})", color="#dfeaf3")
    make_box(ax, 1, 9.8, 5.5, 1.0, f"Duplicates removed (n={n_dup})", color="#fef0d9")

    # Screening
    ax.text(7, 9.2, "Screening", fontsize=12, fontweight="bold", ha="center", color="#2c5777")
    make_box(ax, 1, 7.5, 5.5, 1.0, f"Records screened (n={n_screened})", color="#e8eef5")
    make_box(ax, 7.5, 7.5, 5.5, 1.0, f"Records excluded by automation/rules (n={n_excl_p1})", color="#fadbd8")

    make_box(ax, 1, 5.7, 5.5, 1.0, f"Reports sought for retrieval (n={n_ft_obtained + n_ft_excluded})", color="#e8eef5")
    make_box(ax, 7.5, 5.7, 5.5, 1.0, f"Reports not retrieved (n={(n_ft_obtained + n_ft_excluded) - n_ft_obtained})", color="#fadbd8")

    make_box(ax, 1, 3.9, 5.5, 1.0, f"Reports assessed for eligibility (n={n_ft_obtained})", color="#e8eef5")
    make_box(ax, 7.5, 3.9, 5.5, 1.0, f"Reports excluded (n={n_ft_excluded})\n  with documented reasons", color="#fadbd8")

    # Included
    ax.text(7, 3.3, "Included", fontsize=12, fontweight="bold", ha="center", color="#2c5777")
    make_box(ax, 3.5, 1.5, 7, 1.2, f"Studies included in review (n={n_included})", color="#d4edda")

    # Arrows
    def arrow(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", lw=1.4, color="#2c5777"))

    arrow(3.75, 11.5, 3.75, 10.8)   # to dedup
    arrow(3.75, 9.8, 3.75, 8.5)     # to screened
    arrow(6.5, 8, 7.5, 8)           # excl p1
    arrow(3.75, 7.5, 3.75, 6.7)     # to sought
    arrow(6.5, 6.2, 7.5, 6.2)       # not retrieved
    arrow(3.75, 5.7, 3.75, 4.9)     # to assessed
    arrow(6.5, 4.4, 7.5, 4.4)       # ft excluded
    arrow(3.75, 3.9, 7, 2.7)        # to included

    plt.title("PRISMA 2020 Flow Diagram", fontsize=14, color="#2c5777", pad=12)
    out_png = proj / "prisma_flow.png"
    plt.savefig(out_png, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    flow_data = {
        "identified_db": n_db_total,
        "identified_other": n_other,
        "duplicates_removed": n_dup,
        "screened": n_screened,
        "excluded_screening": n_excl_p1,
        "full_text_assessed": n_ft_obtained,
        "full_text_excluded": n_ft_excluded,
        "included_final": n_included,
        "by_source": {
            "pubmed": n_pubmed, "semantic_scholar": n_s2, "openalex": n_oa,
            "wos": n_wos, "embase": n_em, "consensus": n_consensus,
        },
    }
    (proj / "prisma_flow.json").write_text(json.dumps(flow_data, indent=2))

    print(json.dumps({"ok": True, "png": str(out_png), "json": str(proj / 'prisma_flow.json')}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
