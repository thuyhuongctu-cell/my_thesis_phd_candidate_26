#!/usr/bin/env python3
"""
Audit Vietnamese translations against the WBES/IB glossary.

For each (en, vn) glossary term pair, scan the 3 VN translations and
report:
  - terms that should appear (because the EN source uses them) but
    are missing in the VN translation;
  - terms that are translated incorrectly (e.g., a non-glossary
    Vietnamese rendering of an English construct);
  - first-mention pattern compliance (VN term followed by EN in parens
    on first use).

Run from project root:
    python3 scripts/audit_vn_glossary.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


GLOSSARY: list[tuple[str, str, str]] = [
    # (English term, expected VN, optional alternative-VN to flag as wrong)
    # VN terms follow the canonical bilingual glossary v1.4
    # (writing_guides/09b_vn_term_glossary.md); modern orthography (hóa).
    ("internationalisation",  "quốc tế hóa",                            ""),
    ("internationalization",  "quốc tế hóa",                            ""),
    ("firm performance",      "hiệu quả doanh nghiệp",                  ""),
    ("labour productivity",   "năng suất lao động",                     ""),
    ("export intensity",      "cường độ xuất khẩu",                     ""),
    ("technological capability", "năng lực công nghệ",                  ""),
    ("digital adoption",      "áp dụng số",                             ""),
    ("structural durability", "tính bền vững cấu trúc",                 ""),
    ("environmental shift",   "dịch chuyển môi trường",                 ""),
    ("inverted U-shape",      "hình chữ U ngược",                       ""),
    ("turning point",         "điểm ngoặt",                             ""),
    ("moderation",            "tác động điều tiết",                     ""),
    ("absorptive capacity",   "năng lực hấp thụ",                       ""),
    ("coordination cost",     "chi phí phối hợp",                       ""),
    ("working capital",       "vốn lưu động",                           ""),
    ("trade finance",         "tài trợ thương mại",                     ""),
    ("level shift",           "dịch chuyển mức",                        ""),
    ("curvature moderation",  "điều tiết độ cong",                      ""),
    ("Lind & Mehlum",         "kiểm định Lind–Mehlum",                  ""),
    ("Paternoster",           "kiểm định z Paternoster",                ""),
    ("Heckman two-step",      "mô hình Heckman hai bước",               ""),
    ("propensity-score matching", "đối sánh điểm xu hướng",             ""),
    ("listwise deletion",     "loại bỏ theo dòng",                      ""),
    ("z-standardisation",     "chuẩn hóa theo z",                       ""),
    ("formative composite",   "chỉ số hợp thành cấu thành",             ""),
]

SECTION_HEADINGS = [
    ("Abstract",                 "Tóm tắt"),
    ("Highlights",               "Điểm nhấn"),
    ("Introduction",             "Giới thiệu"),
    ("Theory and Hypotheses",    "Cơ sở lý thuyết và giả thuyết"),
    ("Data and Methods",         "Dữ liệu và phương pháp"),
    ("Results",                  "Kết quả"),
    ("Discussion",               "Thảo luận"),
    ("Limitations",              "Hạn chế"),
    ("References",               "References"),         # kept in EN
    ("Acknowledgements",         "Lời cảm ơn"),
    ("Purpose",                  "Mục đích"),
    ("Design/methodology/approach", "Thiết kế / phương pháp luận / cách tiếp cận"),
    ("Findings",                 "Kết quả nghiên cứu"),
    ("Originality/value",        "Tính mới"),
]

PROTECTED_TOKENS = [
    # Should appear unchanged in VN: variable names, item codes,
    # statistical notation, journal acronyms.
    "TCI", "DAI", "FSTS", "WBES", "APJM", "MIR", "JIBS", "JFAR",
    "VEFR", "ICBEF", "OLS", "HC1", "2SLS", "IV", "PSM", "IMR",
    "c22b", "k33", "k38", "b8", "e6", "h1", "h8", "l1", "d2", "d3c",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# Vietnamese tone-placement variants: "old style" puts the tone mark on the
# second vowel of oa/oe/uy (hoá, thuỷ); modern standard puts it on the main
# vowel (hóa, thủy). Normalise both directions to one canonical form so the
# glossary matches regardless of which convention a document uses.
_VN_ORTHO = {
    "oà": "òa", "oá": "óa", "oả": "ỏa", "oã": "õa", "oạ": "ọa",
    "oè": "òe", "oé": "óe", "oẻ": "ỏe", "oẽ": "õe", "oẹ": "ọe",
    "uỳ": "ùy", "uý": "úy", "uỷ": "ủy", "uỹ": "ũy", "uỵ": "ụy",
}


def _vn_norm(s: str) -> str:
    for old, new in _VN_ORTHO.items():
        s = s.replace(old, new)
    return s


def _en_spelling_tolerant(en_term: str) -> str:
    """Escape an English glossary term and allow British/American -is/-iz
    spelling variants (internationalisation == internationalization)."""
    pat = re.escape(en_term)
    pat = pat.replace("isation", "i[sz]ation").replace("ization", "i[sz]ation")
    pat = pat.replace("ise", "i[sz]e").replace("ize", "i[sz]e")
    return pat


def find_pairs(text: str, en_term: str, vn_term: str) -> dict:
    """Count VN term occurrences and whether at least one first-mention
    bilingual pattern 'VN (EN)' or 'VN (EN, ABBR)' appears."""
    text_n = _vn_norm(text)
    vn_n = _vn_norm(vn_term)
    vn_count = len(re.findall(re.escape(vn_n), text_n))
    # First-mention bilingual: VN term followed by ( ... en_term ... ).
    # EN matching tolerates British/American spelling so the same gloss
    # satisfies both -isation and -ization glossary rows; VN is orthography-
    # normalised so hoá/hóa etc. match.
    fm_pat = re.compile(
        re.escape(vn_n) + r"\s*\([^)]*" + _en_spelling_tolerant(en_term) + r"[^)]*\)",
        re.IGNORECASE,
    )
    has_first_mention = bool(fm_pat.search(text_n))
    return {"vn_count": vn_count, "has_first_mention": has_first_mention}


def audit_file(path: Path) -> dict:
    text = _read(path)
    n_words = len(text.split())
    n_lines = text.count("\n") + 1

    # ── Glossary compliance ────────────────────────────────────────────
    missing_term: list[str] = []
    wrong_term: list[tuple[str, int]] = []
    no_first_mention: list[str] = []
    for en, vn, alt_wrong in GLOSSARY:
        info = find_pairs(text, en, vn)
        if info["vn_count"] == 0:
            # Term might legitimately not be used; only flag major
            # focal constructs.
            if en in (
                "internationalisation", "internationalization",
                "firm performance", "labour productivity",
                "export intensity", "technological capability",
                "digital adoption", "inverted U-shape",
            ):
                missing_term.append(f"{en} → {vn}")
        if alt_wrong:
            alt_n = len(re.findall(re.escape(alt_wrong), text))
            if alt_n > 0:
                wrong_term.append((alt_wrong, alt_n))
        if info["vn_count"] > 0 and not info["has_first_mention"]:
            no_first_mention.append(f"{en} → {vn}")

    # ── Section headings ───────────────────────────────────────────────
    missing_sections: list[str] = []
    for en, vn in SECTION_HEADINGS:
        if not re.search(r"^##\s+[\d\.\s]*" + re.escape(vn), text, re.MULTILINE):
            # Only flag if EN heading appears in the source paper at all
            # (some files don't have Highlights, etc.)
            missing_sections.append(f"{en} → ## {vn}")

    # ── Protected tokens ───────────────────────────────────────────────
    protected_status = {tok: text.count(tok) for tok in PROTECTED_TOKENS}

    return {
        "path": path,
        "n_words": n_words,
        "n_lines": n_lines,
        "missing_term": missing_term,
        "wrong_term": wrong_term,
        "no_first_mention": no_first_mention,
        "missing_sections": missing_sections,
        "protected_status": protected_status,
    }


def render(report: dict) -> str:
    p = report["path"]
    out = [f"\n=== {p.name} ({report['n_words']:,} words, {report['n_lines']:,} lines) ==="]
    if report["wrong_term"]:
        out.append(f"  ✗ WRONG TERMS ({len(report['wrong_term'])} — these should be replaced):")
        for term, n in report["wrong_term"]:
            out.append(f"    - '{term}' appears {n}× (should use authoritative glossary form)")
    if report["missing_term"]:
        out.append(f"  ⚠ MISSING focal-construct VN terms ({len(report['missing_term'])}):")
        for t in report["missing_term"]:
            out.append(f"    - {t}")
    if report["no_first_mention"]:
        out.append(f"  ⚠ Terms used but no bilingual first-mention ({len(report['no_first_mention'])}):")
        for t in report["no_first_mention"][:6]:
            out.append(f"    - {t}")
        if len(report["no_first_mention"]) > 6:
            out.append(f"    ...and {len(report['no_first_mention']) - 6} more")
    missing_present = report["missing_sections"]
    if missing_present:
        out.append(f"  ⚠ Section headings not found ({len(missing_present)} — may be legit omissions):")
        for s in missing_present[:5]:
            out.append(f"    - {s}")

    # Protected tokens summary
    zero_tokens = [t for t, n in report["protected_status"].items() if n == 0]
    if zero_tokens:
        out.append(f"  ℹ Protected tokens not present (legit omissions ok): {', '.join(zero_tokens[:10])}")

    if not (report["wrong_term"] or report["missing_term"]
            or report["no_first_mention"][:1] or report["missing_sections"]):
        out.append("  ✓ All glossary checks pass")
    return "\n".join(out)


def main() -> int:
    # The deliverable VI sources that build into the submission bundle
    # (build_ctu_docx.sh [3]). Earlier this pointed at the stale
    # manuscripts/*_vi_clean.md set, which is not in the bundle.
    files = [
        Path("p3/submission/p3_vietnam_vi.md"),
        Path("p4/submission/p4_singapore_vi.md"),
        Path("p5/submission/p5_china_vi.md"),
        Path("p6/21_p6_meta_vi.md"),
        Path("p7/submission/jibs_package/p7_capstone_vi.md"),
        Path("p8/submission/world_development_package/p8_pacific_sids_vi.md"),
    ]
    n_fail = 0
    for f in files:
        if not f.is_file():
            print(f"\n=== {f.name} ===\n  ✗ FILE NOT FOUND")
            n_fail += 1
            continue
        report = audit_file(f)
        print(render(report))
        if report["wrong_term"]:
            n_fail += 1
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
