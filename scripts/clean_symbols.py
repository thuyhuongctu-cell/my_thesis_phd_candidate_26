#!/usr/bin/env python3
"""Normalise non-standard symbols in Markdown docs (Scopus/WoS hygiene).

Protects: fenced code blocks, inline code spans, math/stats symbols, em-dash.
Language-aware (VI default, EN for /en/ or _en files / mostly-ASCII content).
"""
import re, subprocess, os, sys

# Exclude vendored third-party trees only (top-level tools/ holds cloned repos);
# author sub-tools like p6/tools/ are NOT excluded.
def excluded(f):
    return (f.startswith((".claude/", "tools/", "replication_tools/"))
            or "node_modules" in f)
files = subprocess.run(["git", "ls-files", "*.md"], capture_output=True, text=True).stdout.split()
files = [f for f in files if not excluded(f) and os.path.isfile(f)]

VI_DIAC = re.compile(r"[ăâđêôơưáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ]", re.I)
ROMAN = re.compile(r"\b([IVX]+)\s*→\s*([IVX]+)\b")
TARGET = re.compile(r"[§→←↑↓⇒⟹✓✔✅❌•▪★➔]")
stats = {k: 0 for k in ["§", "→", "←", "↑↓", "⇒⟹", "bullet", "check", "cross"]}

def file_is_en(path, text):
    if "/en/" in path or re.search(r"_en(_clean)?\.md$", path):
        return True
    return len(VI_DIAC.findall(text)) < 8  # mostly non-Vietnamese

def clean_segment(t, en):
    sec = "Section " if en else "Mục "
    if "§" in t:
        stats["§"] += t.count("§")
        t = t.replace("§§", sec).replace("§", sec).replace(sec + " ", sec)
    t = ROMAN.sub(r"\1–\2", t)
    t = re.sub(r"I\s*→\s*P", "I–P", t)  # thesis abbreviation

    for a in "⇒⟹":
        stats["⇒⟹"] += t.count(a)
    # clause-initial connector (after sentence end, or segment start) -> Thus/Do đó
    t = re.sub(r"([.:;]\s+)[⇒⟹]\s*", r"\1" + ("Thus, " if en else "Do đó, "), t)
    t = re.sub(r"^\s*[⇒⟹]\s*", ("Thus, " if en else "Do đó, "), t)
    # inline implication
    t = re.sub(r"\s*[⇒⟹]\s*", " leads to " if en else " dẫn đến ", t)
    stats["→"] += len(re.findall(r"[→➔]", t))
    t = re.sub(r"\s*[→➔]\s*", " to " if en else " đến ", t)
    stats["←"] += t.count("←")
    t = re.sub(r"\s*←\s*", " from " if en else " từ ", t)
    stats["↑↓"] += t.count("↑") + t.count("↓")
    t = re.sub(r"\s*↑", " increases" if en else " tăng", t)
    t = re.sub(r"\s*↓", " decreases" if en else " giảm", t)
    stats["bullet"] += len(re.findall(r"[•▪★]", t))
    t = re.sub(r"\s*[•▪★]\s*", " ", t)
    return t

def process_line(line, en):
    # protect inline code spans
    segs = re.split(r"(`[^`]*`)", line)
    for i in range(0, len(segs), 2):
        segs[i] = clean_segment(segs[i], en)
    line = "".join(segs)
    # status marks: table cells -> word; prose -> strip symbol
    if line.lstrip().startswith("|"):
        for c in "✓✔✅":
            stats["check"] += line.count(c)
        stats["cross"] += line.count("❌")
        line = (line.replace("✅", "Có").replace("✔", "Có")
                    .replace("✓", "Có").replace("❌", "Không"))
    else:
        stats["check"] += len(re.findall(r"[✓✔✅]", line))
        stats["cross"] += line.count("❌")
        line = re.sub(r"[✓✔✅]️?\s*", "", line)
        line = re.sub(r"❌️?\s*", "", line)
    # collapse interior double spaces created by replacements (leading indent safe)
    line = re.sub(r"(?<=\S)  +(?=\S)", " ", line)
    return line

changed = 0
for f in files:
    s = open(f, encoding="utf-8").read()
    if not TARGET.search(s):
        continue
    en = file_is_en(f, s)
    out, in_code = [], False
    for ln in s.split("\n"):
        if ln.lstrip().startswith("```"):
            in_code = not in_code
            out.append(ln); continue
        out.append(ln if in_code else process_line(ln, en))
    s2 = "\n".join(out)
    if s2 != s:
        open(f, "w", encoding="utf-8").write(s2)
        changed += 1

print(f"Files changed: {changed}")
for k, v in stats.items():
    print(f"  {k}: {v}")
