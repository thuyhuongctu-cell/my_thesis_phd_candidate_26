#!/usr/bin/env python3
"""Strip invisible / problematic whitespace from project Markdown.

Removes soft hyphen (U+00AD), zero-width space (U+200B), BOM (U+FEFF);
normalises NBSP (U+00A0), narrow-NBSP (U+202F), thin space (U+2009) to a
regular space. Copy-paste artifacts that corrupt search/diff and submission
text. Vendored trees and .claude/ are excluded.
"""
import subprocess, os

def excluded(f):
    return (f.startswith((".claude/", "tools/", "replication_tools/"))
            or "node_modules" in f)

files = [f for f in subprocess.run(["git", "ls-files", "*.md"],
                                   capture_output=True, text=True).stdout.split()
         if not excluded(f) and os.path.isfile(f)]

REMOVE = [chr(0x00AD), chr(0x200B), chr(0xFEFF)]
TO_SPACE = [chr(0x00A0), chr(0x202F), chr(0x2009)]

ch = rem = sp = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    o = s
    for c in REMOVE:
        rem += s.count(c); s = s.replace(c, "")
    for c in TO_SPACE:
        sp += s.count(c); s = s.replace(c, " ")
    if s != o:
        open(f, "w", encoding="utf-8").write(s); ch += 1
print(f"files changed: {ch} | removed(shy/zwsp/bom): {rem} | normalised-to-space: {sp}")
