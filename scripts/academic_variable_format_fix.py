#!/usr/bin/env python3
"""academic_variable_format_fix.py — Apply academic-variable-formatter skill.

Per APA 7 / Scopus-WoS conventions:
1. Drop leading zero for p, r values (can't exceed 1):
   "p = 0.05" → "p = .05"
   "r = 0.07" → "r = .07"
2. Add space around = in statistical reporting:
   "p=0.05" → "p = .05"
3. Ensure χ² uses proper math mode in EN: "chi-square" → "$\chi^2$"
4. Add space in degrees of freedom: "F(2,87)" → "F(2, 87)"

Preserves: existing well-formatted statistics, math blocks, code blocks,
tables.

Usage: python3 scripts/academic_variable_format_fix.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    "manuscripts/p3_vietnam_en_clean.md",
    "manuscripts/p4_singapore_en_clean.md",
    "manuscripts/p5_china_en_clean.md",
    "p6/p6_meta_manuscript_en.md",
    "p7/p7_capstone_en_clean.md",
    "p8/p8_pacific_sids_en_clean.md",
]


def apply_fixes(text):
    """Apply variable formatting fixes, preserving math/code/tables."""
    lines = text.split('\n')
    out_lines = []
    in_fence = False
    changes = 0

    for line in lines:
        if line.strip().startswith('```'):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence or line.strip().startswith('|'):
            out_lines.append(line)
            continue

        new_line = line
        # Split by math markers; only fix outside
        parts = re.split(r'(\$[^\$\n]*\$|\$\$[^\$]*\$\$)', new_line)
        for i, part in enumerate(parts):
            if part.startswith('$'):
                continue
            original = part

            # 1. Drop leading zero for p values: "p = 0.05" → "p = .05"
            # Match: word boundary p (or P) followed by = or < or >, optional space, 0.XXX
            part = re.sub(
                r'(\b[pP])(\s*[<>=]\s*)0(\.\d+)',
                r'\1\2\3',
                part
            )

            # 2. Drop leading zero for r values: "r = 0.07" → "r = .07"
            # Be conservative: only standalone r (not "or", "for", etc.)
            part = re.sub(
                r'(\b[rR])(\s*=\s*)0(\.\d+\b)',
                r'\1\2\3',
                part
            )

            # 3. Drop leading zero for Pearson r in CI brackets:
            # "[0.060, 0.088]" → "[.060, .088]" when preceded by r
            # Pattern: r ... [0.XX, 0.YY] — only first occurrence
            def fix_ci(m):
                return f'[.{m.group(1)}, .{m.group(2)}]'
            # Only inside r = X.XX (95% CI [a, b])
            part = re.sub(
                r'(\b[rR]\s*[=<>≈]\s*\.\d+[^.]*?\[)0\.(\d+),\s*0\.(\d+)(\])',
                lambda m: f'{m.group(1)}.{m.group(2)}, .{m.group(3)}{m.group(4)}',
                part
            )

            # 4. Drop leading zero for Cohen's d / partial eta squared / phi:
            #    "d = 0.5" → "d = .5"
            part = re.sub(
                r'(\bCohen\'s\s+[dDfF])(\s*=\s*)0(\.\d+)',
                r'\1\2\3',
                part
            )

            # 5. Add space in degrees of freedom: "F(2,87)" → "F(2, 87)"
            part = re.sub(
                r'\b([tFFchi]\^?2?|F|t|χ)\((\d+),(\d+)\)',
                r'\1(\2, \3)',
                part
            )

            # 6. Add space around = in p-value reporting if missing:
            #    "p=.05" → "p = .05" (but only inline, not after $)
            part = re.sub(
                r'(\b[pPrtF])=([\.\d])',
                r'\1 = \2',
                part
            )

            if part != original:
                changes += 1
            parts[i] = part
        new_line = ''.join(parts)
        out_lines.append(new_line)
    return '\n'.join(out_lines), changes


def main():
    dry = '--dry-run' in sys.argv
    total_changes = 0
    files_changed = []
    for rel in TARGETS:
        path = ROOT / rel
        if not path.exists():
            print(f'  [skip] {rel}')
            continue
        text = path.read_text(encoding='utf-8')
        new_text, changes = apply_fixes(text)
        if changes:
            print(f'📄 {rel}: {changes} formatting fixes')
            # Show first 3 diff regions
            old_lines = text.split('\n')
            new_lines = new_text.split('\n')
            diffs_shown = 0
            for ln_idx, (o, n) in enumerate(zip(old_lines, new_lines)):
                if o != n and diffs_shown < 3:
                    print(f'  L{ln_idx+1}:')
                    print(f'    -: {o[:120]}')
                    print(f'    +: {n[:120]}')
                    diffs_shown += 1
            total_changes += changes
            if not dry:
                path.write_text(new_text, encoding='utf-8')
                files_changed.append(rel)
    print(f'\n=== Summary ===')
    print(f'Total formatting fixes: {total_changes}')
    print(f'Files modified: {len(files_changed)}')


if __name__ == '__main__':
    main()
