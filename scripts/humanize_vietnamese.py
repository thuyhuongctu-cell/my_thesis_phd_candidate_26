#!/usr/bin/env python3
"""
Vietnamese humanizer for portfolio CĐ + dissertation chapters.

Applies the same patterns as scripts/humanize_portfolio.py (EN) but for
Vietnamese academic prose:
- Em-dash removal (preserve in published titles)
- "chúng tôi" / "của chúng tôi" → "tác giả" / "nghiên cứu này"
- Vietnamese AI-tell words (then chốt, đáng chú ý, sâu sắc, phong phú) → context-sensitive
- Filler phrases (cần phải, có thể nói rằng) → tighter
- Inline-header vertical lists → prose

Usage:
    python3 scripts/humanize_vietnamese.py --file cd1
    python3 scripts/humanize_vietnamese.py --file all
    python3 scripts/humanize_vietnamese.py --file all --dry-run
"""

from __future__ import annotations
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "cd1": "chuyen_de/cd1/00_cd1_ctu_final_vi.md",
    "cd2": "chuyen_de/cd2/00_cd2_ctu_final_vi.md",
    "cd1_p1": "thesis/14_cd1_part1_intro_theory_vi.md",
    "cd1_p2": "thesis/15_cd1_part2_findings_vi.md",
    "cd1_p3": "thesis/16_cd1_part3_cases_conclusion_vi.md",
    "ch1": "thesis/chuong_1_gioi_thieu_vi.md",
    "ch2": "thesis/chuong_2_tong_quan_tai_lieu_vi.md",
    "ch3": "thesis/chuong_3_phuong_phap_vi.md",
    "ch4": "thesis/chuong_4_ket_qua_vi.md",
    "ch5": "thesis/chuong_5_ket_luan_de_xuat_vi.md",
}

CHUNG_TOI_REPLACEMENTS = [
    (r'\bChúng tôi đề xuất\b', 'Tác giả đề xuất'),
    (r'\bchúng tôi đề xuất\b', 'tác giả đề xuất'),
    (r'\bChúng tôi xem xét\b', 'Nghiên cứu này xem xét'),
    (r'\bchúng tôi xem xét\b', 'nghiên cứu này xem xét'),
    (r'\bChúng tôi đánh giá\b', 'Tác giả đánh giá'),
    (r'\bchúng tôi đánh giá\b', 'tác giả đánh giá'),
    (r'\bChúng tôi thực hiện\b', 'Tác giả thực hiện'),
    (r'\bchúng tôi thực hiện\b', 'tác giả thực hiện'),
    (r'\bChúng tôi nhận thấy\b', 'Nghiên cứu này nhận thấy'),
    (r'\bchúng tôi nhận thấy\b', 'nghiên cứu này nhận thấy'),
    (r'\bChúng tôi cho rằng\b', 'Tác giả cho rằng'),
    (r'\bchúng tôi cho rằng\b', 'tác giả cho rằng'),
    (r'\bChúng tôi phát hiện\b', 'Nghiên cứu này phát hiện'),
    (r'\bchúng tôi phát hiện\b', 'nghiên cứu này phát hiện'),
    (r'\bcủa chúng tôi\b', 'của tác giả'),
    (r'\bCủa chúng tôi\b', 'Của tác giả'),
    (r'\bnghiên cứu chúng tôi\b', 'nghiên cứu của tác giả'),
    (r'\bNghiên cứu chúng tôi\b', 'Nghiên cứu của tác giả'),
    # Generic: any remaining "chúng tôi" → "tác giả"
    (r'\bChúng tôi\b', 'Tác giả'),
    (r'\bchúng tôi\b', 'tác giả'),
]

VIETNAMESE_AI_TELL = [
    # "Then chốt" / "đáng chú ý" overuse
    (r'\bvai trò then chốt\b', 'vai trò quan trọng'),
    (r'\bVai trò then chốt\b', 'Vai trò quan trọng'),
    (r'\bđóng vai trò then chốt\b', 'đóng vai trò quan trọng'),
    # "Sâu sắc" / "phong phú" / "toàn diện" overuse
    (r'\bsâu sắc và toàn diện\b', 'thấu đáo'),
    (r'\bphong phú và đa dạng\b', 'đa dạng'),
    (r'\bphân tích sâu sắc\b', 'phân tích'),
    (r'\bnghiên cứu sâu sắc\b', 'nghiên cứu'),
    # "Đáng chú ý" overuse
    (r'\bĐáng chú ý là\b', 'Cụ thể'),
    (r'\bđáng chú ý là\b', 'cụ thể'),
    # "Trong bối cảnh" overuse
    (r'\bTrong bối cảnh hiện nay\b', 'Hiện nay'),
    (r'\btrong bối cảnh hiện nay\b', 'hiện nay'),
    # Em-dash like patterns
    (r'\bnổi bật trong\b', 'trong'),
    (r'\bNổi bật là\b', 'Cụ thể'),
    (r'\bnổi bật là\b', 'cụ thể'),
]

FILLER_VI = [
    (r'\bCó thể nói rằng\b', ''),
    (r'\bcó thể nói rằng\b', ''),
    (r'\bĐiều quan trọng cần lưu ý là\b', ''),
    (r'\bđiều quan trọng cần lưu ý là\b', ''),
    (r'\bTrong thời điểm hiện tại\b', 'Hiện nay'),
    (r'\btrong thời điểm hiện tại\b', 'hiện nay'),
    (r'\bcần phải lưu ý rằng\b', 'lưu ý:'),
    (r'\bCần phải lưu ý rằng\b', 'Lưu ý:'),
]

# Stale references that need updating per Phase A1 changes
STALE_REFS = [
    # P8 title change
    (r'(?<!Pacific and Indian Ocean )\bPacific SIDS\b', 'Pacific and Indian Ocean SIDS'),
    # P9' India is paper #9 not paper #9 Thailand (paused)
    # (handled via context)
]


def remove_em_dashes_vi(text: str) -> tuple[str, int]:
    """Remove em-dashes in Vietnamese prose, preserve in titles."""
    count = 0
    lines = text.split('\n')
    in_refs = False
    in_code = False
    out = []

    for line in lines:
        # Detect references / bibliography sections
        if re.match(r'^##+\s*(Tài liệu|References|Bibliography|Danh mục)', line, re.IGNORECASE):
            in_refs = True
        elif re.match(r'^## ', line) and in_refs:
            in_refs = False

        if line.startswith('```'):
            in_code = not in_code
        if in_code or line.startswith('#') or line.startswith('|'):
            out.append(line)
            continue

        # Skip figure/table captions
        if re.match(r'^\s*(Hình|Bảng|Figure|Table|Nguồn:|Source:|\*Hình|\*Bảng)', line, re.IGNORECASE):
            out.append(line)
            continue

        # If in references, preserve em-dashes inside quoted titles
        if in_refs:
            new_line = ""
            in_q = False
            for c in line:
                if c == '"':
                    in_q = not in_q
                if c == '—' and not in_q:
                    new_line += ','
                    count += 1
                else:
                    new_line += c
            out.append(new_line)
            continue

        # Prose: spaced em-dash → comma
        n_spaced = line.count(' — ')
        line = line.replace(' — ', ', ')
        count += n_spaced
        # Unspaced em-dash → comma
        n_unspaced = line.count('—')
        line = line.replace('—', ', ')
        count += n_unspaced

        out.append(line)

    return '\n'.join(out), count


def apply_patterns(text: str, patterns: list) -> tuple[str, int]:
    count = 0
    for pat, repl in patterns:
        new_text, n = re.subn(pat, repl, text)
        if n > 0:
            count += n
            text = new_text
    return text, count


def humanize_file(path: Path, dry_run: bool = False) -> dict:
    text = path.read_text(encoding='utf-8')
    original = text
    stats = {
        "file": str(path.relative_to(ROOT)),
        "original_words": len(text.split()),
        "original_em": text.count(' — '),
        "original_chung_toi": len(re.findall(r"\b(chúng tôi|Chúng tôi)\b", text)),
    }

    # 1. Em-dash removal
    text, n_em = remove_em_dashes_vi(text)
    stats["em_removed"] = n_em

    # 2. "chúng tôi" replacements
    text, n_ct = apply_patterns(text, CHUNG_TOI_REPLACEMENTS)
    stats["chung_toi_replaced"] = n_ct

    # 3. Vietnamese AI tells
    text, n_ai = apply_patterns(text, VIETNAMESE_AI_TELL)
    stats["ai_tells_fixed"] = n_ai

    # 4. Filler phrases
    text, n_fp = apply_patterns(text, FILLER_VI)
    stats["filler_fixed"] = n_fp

    # 5. Stale refs (P8 title, etc.)
    text, n_sr = apply_patterns(text, STALE_REFS)
    stats["stale_refs_fixed"] = n_sr

    # Cleanup
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r' ,', ',', text)
    text = re.sub(r',,+', ',', text)
    text = re.sub(r' \.', '.', text)

    stats["final_words"] = len(text.split())
    stats["final_em"] = text.count(' — ')
    stats["text_changed"] = (text != original)

    if not dry_run and stats["text_changed"]:
        path.write_text(text, encoding='utf-8')

    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, choices=list(FILES.keys()) + ["all", "cd_only", "chapters_only"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.file == "all":
        targets = list(FILES.keys())
    elif args.file == "cd_only":
        targets = [k for k in FILES if k.startswith("cd")]
    elif args.file == "chapters_only":
        targets = [k for k in FILES if k.startswith("ch")]
    else:
        targets = [args.file]

    print(f"{'=' * 80}\n  Vietnamese humanization {'(DRY RUN)' if args.dry_run else ''}\n{'=' * 80}")

    all_stats = []
    for k in targets:
        path = ROOT / FILES[k]
        if not path.exists():
            print(f"  ⚠ {k}: not found at {path}")
            continue
        print(f"\n→ {k}: {FILES[k]}")
        s = humanize_file(path, args.dry_run)
        all_stats.append(s)
        print(f"   Words:  {s['original_words']:,} → {s['final_words']:,}")
        print(f"   Em-dash: {s['original_em']} → {s['final_em']}")
        print(f"   Replacements: em={s['em_removed']} chúng_tôi={s['chung_toi_replaced']} "
              f"ai={s['ai_tells_fixed']} filler={s['filler_fixed']} stale_refs={s['stale_refs_fixed']}")
        print(f"   Modified: {s['text_changed']}")

    print(f"\n{'=' * 80}\n  Total: {len(all_stats)} files\n{'=' * 80}")
    print(f"  Em-dashes removed: {sum(s['em_removed'] for s in all_stats)}")
    print(f"  Chúng tôi replaced: {sum(s['chung_toi_replaced'] for s in all_stats)}")
    print(f"  Stale refs updated: {sum(s['stale_refs_fixed'] for s in all_stats)}")


if __name__ == "__main__":
    main()
