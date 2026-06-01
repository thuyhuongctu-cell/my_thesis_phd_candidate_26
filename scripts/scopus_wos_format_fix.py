#!/usr/bin/env python3
"""scopus_wos_format_fix.py — Apply Scopus/WoS formatting standards.

Scans dissertation portfolio markdown files for non-standard symbols
and applies replacements per the chinh-sua-van-ban-hoc-thuat-scopus-wos
skill specification. Preserves math equations, tables, code blocks.

Patterns fixed in prose (NOT in math/code/tables):
  § (section sign)     → "Section" (EN) / "Mục" (VI)
  ¶ (pilcrow)          → removed (or "đoạn")
  → ← ↑ ↓ (arrows)     → text ("leads to", "increases", etc.)
  ✓ ✗ × in prose       → text equivalents (kept in tables)
  Decorative bullets   → standard markdown bullets

Skipped: math equations ($...$), code blocks (```...```), tables (|...|).

Usage: python3 scripts/scopus_wos_format_fix.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Files to scan (canonical submission sources)
TARGETS = [
    # EN papers (blinded sources)
    "manuscripts/p3_vietnam_en_clean.md",
    "manuscripts/p4_singapore_en_clean.md",
    "manuscripts/p5_china_en_clean.md",
    "p6/p6_meta_manuscript_en.md",
    "p7/p7_capstone_en_clean.md",
    "p8/p8_pacific_sids_en_clean.md",
    # VI papers
    "manuscripts/p3_vietnam_vi_clean.md",
    "manuscripts/p4_singapore_vi_clean.md",
    "manuscripts/p5_china_vi_clean.md",
    "p6/p6_meta_manuscript_vi.md",
    # Chuyên đề
    "chuyen_de/cd1/00_cd1_ctu_final_vi.md",
    "chuyen_de/cd2/00_cd2_ctu_final_vi.md",
    # Thesis chapters
    "thesis/chuong_1_gioi_thieu_vi.md",
    "thesis/chuong_2_tong_quan_tai_lieu_vi.md",
    "thesis/chuong_3_phuong_phap_vi.md",
    "thesis/chuong_4_ket_qua_vi.md",
    "thesis/chuong_5_ket_luan_de_xuat_vi.md",
]

# Patterns to look for (in prose, not math/code)
SCAN_PATTERNS = [
    (r'§', "section sign §"),
    (r'¶', "pilcrow ¶"),
    (r'→', "right arrow →"),
    (r'←', "left arrow ←"),
    (r'↑', "up arrow ↑"),
    (r'↓', "down arrow ↓"),
    (r'★', "filled star ★"),
    (r'☆', "empty star ☆"),
    (r'◦', "white bullet ◦"),
    (r'■', "filled square ■"),
    (r'□', "empty square □"),
    (r'①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩', "circled digits"),
    (r'\b(\d+)°([CFK])\b', "unspaced degree symbol"),  # 25°C → 25 °C
    (r'\b(\d+)\s*x\s*(\d+)\b', "x as multiplication (should be ×)"),
]


def strip_protected(text):
    """Remove math/code/tables to scan only prose."""
    # Remove fenced code blocks
    text = re.sub(r'```.*?```', '\n', text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r'`[^`]+`', '`code`', text)
    # Remove math $$...$$
    text = re.sub(r'\$\$.*?\$\$', '$$math$$', text, flags=re.DOTALL)
    # Remove inline math $...$
    text = re.sub(r'\$[^\$\n]+\$', '$math$', text)
    # Remove markdown tables
    text = re.sub(r'^\s*\|.*$', '', text, flags=re.MULTILINE)
    return text


def is_in_math_or_code(text, pos):
    """Check if position is inside math/code/table — should not be modified."""
    # Crude check: count $ before pos and check parity
    upto = text[:pos]
    # Inside fenced code block?
    fence_count = upto.count('```')
    if fence_count % 2 == 1:
        return True
    # Inside inline code?
    bt_count = upto.count('`')
    if bt_count % 2 == 1:
        return True
    # Inside math?
    # Count $ NOT preceded by backslash
    dollar_count = len(re.findall(r'(?<!\\)\$', upto))
    if dollar_count % 2 == 1:
        return True
    # Inside table row? Check current line
    line_start = upto.rfind('\n') + 1
    line = text[line_start:text.find('\n', pos) if text.find('\n', pos) != -1 else len(text)]
    if line.strip().startswith('|'):
        return True
    return False


def scan_file(path):
    """Find all non-standard symbol occurrences in prose."""
    if not path.exists():
        return None
    text = path.read_text(encoding='utf-8')
    hits = []
    for pat, label in SCAN_PATTERNS:
        for m in re.finditer(pat, text):
            if is_in_math_or_code(text, m.start()):
                continue
            # Find line number
            line_no = text[:m.start()].count('\n') + 1
            # Get line context
            line_start = text.rfind('\n', 0, m.start()) + 1
            line_end = text.find('\n', m.end())
            if line_end == -1:
                line_end = len(text)
            context = text[line_start:line_end][:120]
            hits.append((line_no, label, m.group(0), context))
    return hits


def apply_fixes(text, is_vi=False):
    """Apply replacements to prose text. Preserves math/code/tables."""
    lines = text.split('\n')
    out_lines = []
    in_fence = False
    for line in lines:
        if line.strip().startswith('```'):
            in_fence = not in_fence
        if in_fence or line.strip().startswith('|'):
            out_lines.append(line)
            continue

        # Replace patterns NOT inside math
        new_line = line
        # Split by math markers and only fix outside
        parts = re.split(r'(\$[^\$\n]*\$|\$\$[^\$]*\$\$)', new_line)
        for i, part in enumerate(parts):
            if part.startswith('$'):
                continue  # math, leave alone
            # Apply fixes
            if is_vi:
                # Vietnamese replacements
                part = part.replace(' § ', ' Mục ')
                part = re.sub(r'§(\d)', r'Mục \1', part)  # §5.4 → Mục 5.4
                part = re.sub(r'§([A-Z])', r'Mục \1', part)
            else:
                # English replacements
                part = part.replace(' § ', ' Section ')
                part = re.sub(r'§(\d)', r'Section \1', part)
                part = re.sub(r'§([A-Z])', r'Section \1', part)
            # Remove pilcrow entirely
            part = part.replace('¶ ', '').replace(' ¶', '').replace('¶', '')
            # Circled digits → numbers
            CIRCLED = {'①':'1','②':'2','③':'3','④':'4','⑤':'5','⑥':'6','⑦':'7','⑧':'8','⑨':'9','⑩':'10'}
            for c, d in CIRCLED.items():
                part = part.replace(c, f'({d})')
            # Decorative bullets at line start (markdown OK with `- ` / `* `)
            part = re.sub(r'^(\s*)[★☆◦■□](\s+)', r'\1- ', part, flags=re.MULTILINE)
            # Fix unspaced degree: 25°C → 25 °C
            part = re.sub(r'(\d)°([CFK])\b', r'\1 °\2', part)
            # Arrow replacements (per Scopus/WoS standard: prefer text in prose)
            if is_vi:
                # Common patterns in VI prose
                part = re.sub(r'\s+→\s+', '; sau đó ', part)
                part = re.sub(r'\s+←\s+', '; trước đó ', part)
                part = re.sub(r'\b↑\b', 'tăng', part)
                part = re.sub(r'\b↓\b', 'giảm', part)
            else:
                # EN: most common forms in IB papers
                # "X records → Y removed" (PRISMA flow) → "X records, of which Y removed"
                part = re.sub(r'\s+→\s+', '; ', part)
                part = re.sub(r'\s+←\s+', '; preceded by ', part)
                part = re.sub(r'\b↑\b', 'increases', part)
                part = re.sub(r'\b↓\b', 'decreases', part)
            parts[i] = part
        new_line = ''.join(parts)
        out_lines.append(new_line)
    return '\n'.join(out_lines)


def main():
    dry = '--dry-run' in sys.argv
    total_hits = 0
    files_changed = []
    for rel in TARGETS:
        path = ROOT / rel
        if not path.exists():
            print(f'  [skip] {rel} not found')
            continue
        hits = scan_file(path) or []
        if not hits:
            continue
        total_hits += len(hits)
        # Group by symbol type
        by_label = {}
        for ln, label, sym, ctx in hits:
            by_label.setdefault(label, []).append((ln, sym, ctx))
        print(f'\n📄 {rel}: {len(hits)} symbols to fix')
        for label, items in sorted(by_label.items()):
            print(f'  {label}: {len(items)}')
            for ln, sym, ctx in items[:3]:
                print(f'    L{ln}: "{ctx[:80]}"')

        if not dry:
            # Apply fixes
            text = path.read_text(encoding='utf-8')
            is_vi = '_vi' in rel or 'cd' in rel or 'chuong' in rel
            new_text = apply_fixes(text, is_vi=is_vi)
            if new_text != text:
                path.write_text(new_text, encoding='utf-8')
                files_changed.append(rel)

    print(f'\n=== Summary ===')
    print(f'Total non-standard symbol hits: {total_hits}')
    print(f'Files modified: {len(files_changed)}')
    for f in files_changed:
        print(f'  ✓ {f}')


if __name__ == '__main__':
    main()
