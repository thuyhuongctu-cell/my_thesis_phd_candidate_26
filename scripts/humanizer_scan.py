#!/usr/bin/env python3
"""humanizer_scan.py — Detect AI-writing patterns across EN + VI documents.

Scans for the high-signal AI tells documented in .claude/skills/humanizer/
plus phd-academic-writing-humanizer (em-dash focus).

Outputs:
  reports/humanizer_audit.md  — per-file ranked pattern counts
  reports/humanizer_audit.json — machine-readable

Usage:
  python3 scripts/humanizer_scan.py
"""
import re
import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
REPORTS.mkdir(exist_ok=True)

FILES = {
    # EN papers
    'P3 Vietnam (EN)': 'manuscripts/p3_vietnam_en_clean.md',
    'P4 Singapore (EN)': 'manuscripts/p4_singapore_en_clean.md',
    'P5 China (EN)': 'manuscripts/p5_china_en_clean.md',
    'P6 Meta (EN)': 'p6/p6_meta_manuscript_en.md',
    'P7 Capstone (EN)': 'p7/p7_capstone_en_clean.md',
    'P8 SIDS (EN)': 'p8/p8_pacific_sids_en_clean.md',
    # VI papers
    'P3 Vietnam (VI)': 'manuscripts/p3_vietnam_vi_clean.md',
    'P4 Singapore (VI)': 'manuscripts/p4_singapore_vi_clean.md',
    'P5 China (VI)': 'manuscripts/p5_china_vi_clean.md',
    'P6 Meta (VI)': 'p6/p6_meta_manuscript_vi.md',
    # Chuyen de + chapters (VI)
    'CĐ1': 'chuyen_de/cd1/00_cd1_ctu_final_vi.md',
    'CĐ2': 'chuyen_de/cd2/00_cd2_ctu_final_vi.md',
    'Ch1 Giới thiệu': 'thesis/chuong_1_gioi_thieu_vi.md',
    'Ch2 Tổng quan tài liệu': 'thesis/chuong_2_tong_quan_tai_lieu_vi.md',
    'Ch3 Phương pháp': 'thesis/chuong_3_phuong_phap_vi.md',
    'Ch4 Kết quả': 'thesis/chuong_4_ket_qua_vi.md',
    'Ch5 Kết luận': 'thesis/chuong_5_ket_luan_de_xuat_vi.md',
}

# EN AI-vocabulary (humanizer skill §7)
EN_AI_VOCAB = [
    r'\bdelve\w*\b', r'\bintricate\w*\b', r'\btapestry\b', r'\bmultifaceted\b',
    r'\bunderscore\w*\b', r'\bpivotal\b', r'\bfoster(?:s|ing|ed)?\b',
    r'\benduring\b', r'\bgarner\w*\b', r'\binterplay\b',
    r'\bshowcase\w*\b', r'\btestament\b', r'\bvibrant\b',
    r'\bcrucial\b', r'\bvital\b',
    # NOTE: 'significantly' excluded — it's standard statistical language
    # ("statistically significantly different") not an AI tell in academic context.
    r'\bin\s+conclusion\b', r'\bin\s+summary\b',
    r'\bnavigat\w+\s+the\s+(?:complex|complexit|landscape)',
    r'\bevolving\s+landscape\b', r'\bever[\s-]changing\b',
]

# EN forced -ing endings (§3) — only fronted/tail participial phrases, not normal
EN_ING_TELLS = [
    r',\s+(?:highlighting|underscoring|emphasizing|reflecting|symbolizing|contributing|cultivating|fostering|ensuring|showcasing|encompassing)\b',
    r'^(?:Highlighting|Underscoring|Emphasizing|Reflecting|Symbolizing|Contributing|Cultivating|Fostering|Ensuring|Showcasing|Encompassing)\b',
]

# EN copula avoidance (§8)
EN_COPULA_AVOID = [
    r'\bserves?\s+as\s+a\b', r'\bstands?\s+as\s+a\b',
    r'\bmarks?\s+a\s+pivotal\b', r'\brepresents?\s+a\s+pivotal\b',
    r'\bboasts?\s+(?:a\s+)?(?:rich|vibrant|impressive|stunning)',
]

# Negative parallelism (§9)
EN_NEG_PARALLEL = [
    r'\bnot\s+(?:just|only|merely)\s+(?:a|an|about)\b',
    r"\bit['’]s\s+not\s+(?:just|only|merely)\b",
    r'\bis\s+not\s+(?:whether|just|only|merely)\b',
]

# Persuasive authority (§27)
EN_PERSUASIVE = [
    r'\bat\s+(?:its|the)\s+(?:core|heart)\b',
    r'\bthe\s+real\s+question\b', r'\bthe\s+deeper\s+issue\b',
    r'\bin\s+reality,\b', r'\bfundamentally,\b',
    r'\bwhat\s+(?:really\s+matters|truly\s+counts)\b',
]

# Filler phrases (§23)
EN_FILLER = [
    r'\bin\s+order\s+to\b',
    r'\bdue\s+to\s+the\s+fact\s+that\b',
    r'\bat\s+this\s+point\s+in\s+time\b',
    r'\bit\s+is\s+important\s+to\s+note\s+that\b',
    r'\bhas\s+the\s+ability\s+to\b',
    r'\bin\s+the\s+event\s+that\b',
]

# Promotional language (§4)
EN_PROMO = [
    r'\bnestled\s+(?:in|within)\b', r'\bin\s+the\s+heart\s+of\b',
    r'\bbreathtaking\b', r'\bgroundbreaking\b', r'\brenowned\b',
    r'\bcommitment\s+to\s+(?:excellence|quality|innovation)\b',
    r'\bcutting[\s-]edge\b',
]

# Em-dash ONLY (en-dash `–` is legitimate in compound terms like I–P, Levinsohn–Petrin,
# number ranges 5–10, etc. — not an AI tell in academic writing).
EM_DASH = [r'—', r'\s--\s']  # em-dash + ASCII double-hyphen-as-em

# VI patterns — only strong AI tells, NOT legitimate academic vocabulary.
# "đáng kể", "đáng chú ý", "đáng quan tâm" are normal Vietnamese academic
# qualifiers (≈ "substantial", "notable") and routinely appear in published
# articles; they are NOT AI tells in isolation.
VI_AI_VOCAB = [
    r'\b(?:đa\s+chiều|nhiều\s+chiều)\s+và\s+phức\s+tạp\b',
    r'\b(?:bức\s+tranh|tấm\s+thảm)\s+(?:phong\s+phú|đa\s+sắc|đa\s+chiều)\b',
    r'\b(?:bối\s+cảnh|phong\s+cảnh)\s+(?:không\s+ngừng\s+)?(?:thay\s+đổi|biến\s+đổi)\b',
    r'\bđóng\s+vai\s+trò\s+(?:then\s+chốt|chủ\s+chốt|không\s+thể\s+thiếu|không\s+thể\s+phủ\s+nhận)\b',
    r'\b(?:vai\s+trò|ý\s+nghĩa)\s+(?:không\s+thể\s+thiếu|không\s+thể\s+phủ\s+nhận|sống\s+còn)\b',
    r'\bminh\s+chứng\s+(?:rõ\s+ràng|đáng\s+kể|sống\s+động)\s+cho\b',
    r'\btrong\s+bối\s+cảnh\s+(?:ngày\s+nay|hiện\s+nay)\s+(?:đầy|với\s+nhiều)',
    r'\b(?:hài\s+hoà|hài\s+hòa)\s+với\s+(?:thiên\s+nhiên|bản\s+sắc)\b',
    r'\bkhông\s+ngừng\s+(?:tiến\s+hoá|phát\s+triển|đổi\s+mới)\b',
    r'\b(?:sâu\s+sắc|sâu\s+đậm)\s+và\s+(?:bền\s+vững|lâu\s+dài)\b',
]

VI_FILLER = [
    r'\bnhằm\s+mục\s+đích\b',
    r'\bcần\s+phải\s+lưu\s+ý\s+rằng\b',
    r'\bđiều\s+quan\s+trọng\s+cần\s+lưu\s+ý\s+là\b',
    r'\btrong\s+thời\s+điểm\s+hiện\s+tại\b',
    r'\bcó\s+khả\s+năng\s+sẽ\b',
    r'\bvới\s+vai\s+trò\s+(?:là|như)\b',
]

VI_PROMO = [
    r'\bnằm\s+ẩn\s+mình\s+(?:trong|giữa)\b',
    r'\bgiữa\s+lòng\b', r'\bcảnh\s+sắc\s+(?:hùng\s+vĩ|tuyệt\s+đẹp)\b',
    r'\bmang\s+đậm\s+(?:bản\s+sắc|dấu\s+ấn)\b',
]

# Generic patterns (apply to both EN + VI as raw characters)
EM_DASH_PAT = re.compile(r'—|\s--\s')  # em-dash + ASCII double-hyphen-as-em (NOT en-dash `–`)

PATTERN_GROUPS = {
    'em_dash': (EM_DASH_PAT, 'Em-dash (—) decorative use (§14 — cut)'),
}

EN_GROUPS = {
    'ai_vocab': (re.compile('|'.join(EN_AI_VOCAB), re.IGNORECASE), 'AI vocab (delve/intricate/tapestry/pivotal/foster/etc.)'),
    'ing_tells': (re.compile('|'.join(EN_ING_TELLS), re.IGNORECASE | re.MULTILINE), 'Forced -ing participle (§3)'),
    'copula_avoid': (re.compile('|'.join(EN_COPULA_AVOID), re.IGNORECASE), 'Copula avoidance "serves as/stands as" (§8)'),
    'neg_parallel': (re.compile('|'.join(EN_NEG_PARALLEL), re.IGNORECASE), 'Negative parallelism "not just X but Y" (§9)'),
    'persuasive': (re.compile('|'.join(EN_PERSUASIVE), re.IGNORECASE), 'Persuasive authority "at its core / the real question" (§27)'),
    'filler': (re.compile('|'.join(EN_FILLER), re.IGNORECASE), 'Filler phrases "in order to / it is important to note" (§23)'),
    'promo': (re.compile('|'.join(EN_PROMO), re.IGNORECASE), 'Promotional language "nestled/breathtaking/groundbreaking" (§4)'),
}

VI_GROUPS = {
    'vi_ai_vocab': (re.compile('|'.join(VI_AI_VOCAB), re.IGNORECASE), 'VI AI vocab (đa chiều phức tạp / bức tranh phong phú / đóng vai trò then chốt / etc.)'),
    'vi_filler': (re.compile('|'.join(VI_FILLER), re.IGNORECASE), 'VI filler (nhằm mục đích / cần phải lưu ý / với vai trò là)'),
    'vi_promo': (re.compile('|'.join(VI_PROMO), re.IGNORECASE), 'VI promotional (nằm ẩn mình / giữa lòng / cảnh sắc hùng vĩ)'),
}


def strip_code_blocks(text):
    """Remove fenced code blocks + inline code + markdown tables so we don't
    count them as prose. Tables use `|` as cell separator and `—` as 'no data'
    placeholder, which would otherwise inflate em-dash counts."""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    # Drop markdown table lines (rows + separator + header-row both pipe-delimited)
    text = re.sub(r'^\s*\|.*$', '', text, flags=re.MULTILINE)
    return text


def strip_references(text):
    """Skip the References section — citations cause many false positives."""
    m = re.search(r'\n##\s+(?:References|Tài\s+liệu\s+tham\s+khảo)\b', text, re.IGNORECASE)
    if m:
        return text[:m.start()]
    return text


def scan_file(label, path):
    p = ROOT / path
    if not p.exists():
        return {'label': label, 'error': f'File not found: {path}'}

    raw = p.read_text(encoding='utf-8')
    text = strip_references(strip_code_blocks(raw))
    word_count = len(text.split())
    is_vi = '(VI)' in label or label in ('CĐ1', 'CĐ2') or label.startswith('Ch')

    groups = dict(PATTERN_GROUPS)
    if is_vi:
        groups.update(VI_GROUPS)
    else:
        groups.update(EN_GROUPS)

    findings = {}
    examples = {}
    for key, (pat, desc) in groups.items():
        matches = list(pat.finditer(text))
        findings[key] = {'count': len(matches), 'desc': desc}
        # Capture up to 3 example matches with line context
        if matches:
            lines = text.split('\n')
            line_starts = [0]
            for line in lines:
                line_starts.append(line_starts[-1] + len(line) + 1)
            ex_list = []
            for m in matches[:5]:
                # find line number
                pos = m.start()
                line_no = next((i for i, s in enumerate(line_starts) if s > pos), len(line_starts)) - 1
                snippet = lines[line_no][:200].strip() if line_no < len(lines) else ''
                ex_list.append({'match': m.group(0), 'line': line_no + 1, 'context': snippet})
            examples[key] = ex_list

    total = sum(f['count'] for f in findings.values())
    density = (total / word_count * 1000) if word_count else 0

    return {
        'label': label,
        'path': path,
        'word_count': word_count,
        'is_vi': is_vi,
        'total_hits': total,
        'density_per_1000w': round(density, 2),
        'findings': findings,
        'examples': examples,
    }


def main():
    results = [scan_file(label, path) for label, path in FILES.items()]

    # JSON output
    (REPORTS / 'humanizer_audit.json').write_text(
        json.dumps({'files': results}, indent=2, ensure_ascii=False),
        encoding='utf-8',
    )

    # Markdown report
    lines = ['# Humanizer Audit — Portfolio Pattern Scan', '']
    lines.append('_Generated by `scripts/humanizer_scan.py`. Patterns from `.claude/skills/humanizer/SKILL.md` + `phd-academic-writing-humanizer` skill._')
    lines.append('')
    lines.append('## Summary table (sorted by density per 1,000 words)')
    lines.append('')
    lines.append('| Document | Words | Total hits | Density/1000w | Worst pattern |')
    lines.append('|---|---:|---:|---:|---|')

    # Sort by density
    sorted_results = sorted(
        [r for r in results if 'error' not in r],
        key=lambda r: -r['density_per_1000w'],
    )
    for r in sorted_results:
        worst = max(r['findings'].items(), key=lambda kv: kv[1]['count'], default=(None, {'count': 0, 'desc': '—'}))
        worst_str = f"{worst[0]} ({worst[1]['count']})" if worst[1]['count'] > 0 else '—'
        lines.append(f"| {r['label']} | {r['word_count']:,} | {r['total_hits']} | {r['density_per_1000w']} | {worst_str} |")

    lines.append('')
    lines.append('## Per-file detail')
    for r in sorted_results:
        lines.append(f"\n### {r['label']}")
        lines.append(f"Path: `{r['path']}` · {r['word_count']:,} words · density {r['density_per_1000w']}/1000w · total {r['total_hits']}")
        lines.append('')
        # Pattern table
        pats = sorted(r['findings'].items(), key=lambda kv: -kv[1]['count'])
        for key, info in pats:
            if info['count'] == 0:
                continue
            lines.append(f"- **{key}** ({info['count']}): {info['desc']}")
            for ex in r['examples'].get(key, [])[:3]:
                ctx = ex['context'][:160].replace('|', '\\|')
                lines.append(f"  - L{ex['line']}: `{ex['match']}` — _{ctx}…_")

    (REPORTS / 'humanizer_audit.md').write_text('\n'.join(lines), encoding='utf-8')
    print(f"Wrote: {(REPORTS / 'humanizer_audit.md').relative_to(ROOT)}")
    print(f"Wrote: {(REPORTS / 'humanizer_audit.json').relative_to(ROOT)}")
    print()
    print('Top-5 files by AI-pattern density:')
    for r in sorted_results[:5]:
        print(f"  {r['label']:30s}  density={r['density_per_1000w']:6.2f}/1000w  hits={r['total_hits']:4d}  words={r['word_count']:6,}")


if __name__ == '__main__':
    main()
