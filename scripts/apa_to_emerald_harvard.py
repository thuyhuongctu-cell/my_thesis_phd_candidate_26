#!/usr/bin/env python3
"""Convert the References section of a manuscript markdown file from APA-7 style
to Emerald-Harvard style (the house style for Emerald journals).

Emerald-Harvard conventions applied:
  - Year in parentheses followed by a comma:            (2020),
  - Article/chapter titles in double quotation marks:   "Title of article",
  - Journal name italic; volume/issue OUTSIDE italics:  *Journal*, Vol. X No. Y, pp. aa-bb.
  - Book/data titles italic, comma before publisher:    *Title*, Publisher.
  - Authors joined with " and " (no serial comma, no &); initials closed up: A.A.
  - DOI rendered as:                                    doi: 10.xxxx/....
  - En-dashes in page ranges normalised to hyphens.

Only the block from the "## References" heading to end-of-file is touched. The
block is collapsed to one stream and re-split on entry boundaries, so it works
whether or not the source separates entries with blank lines.

Usage:
  python3 scripts/apa_to_emerald_harvard.py <file.md> [--write] [--expect N]
Without --write it prints the converted entries and writes nothing.
"""
import re
import sys

YEAR = r"\((\d{4}[a-z]?)\)"

# --- Entry splitting by year-anchor + backward author-list matching ----------
# Each reference has exactly one author-year head "(YYYY)." So we anchor on year
# markers and, in the text between two markers, locate where the *next* entry's
# author list begins. An author list is structurally distinct from prose: it is
# only capitalised surnames + initials + connectors, with no ordinary lowercase
# words, so the true split is the terminal after which the suffix is a clean
# author list.
_SURNAME = r"(?:(?:van |de |der |von |del |di |la |Mc|Mac|O['’]|Al-)?[A-Z][A-Za-z'’\-]+)"
_INITIALS = r"[A-Z]\.(?:[ -]?[A-Z]\.)*"
_NAME = _SURNAME + r",\s" + _INITIALS
_CONN = r"(?:,\s&\s|,\sand\s|\sand\s|\s&\s|,\s)"
_PERSON_LIST = _NAME + r"(?:" + _CONN + _NAME + r")*"
_ORG = r"[A-Z][A-Za-z]+(?:\s[A-Z&][A-Za-z]+)*"
AUTHORS_FULL = re.compile(r"^(?:" + _PERSON_LIST + r"|" + _ORG + r")\.?\s*$")
YEAR_MARKER = re.compile(r"\(\d{4}[a-z]?\)[.,]")
# A terminal that can end an entry: lowercase/digit/star/paren/bracket + '.', or '>'.
TERMINAL = re.compile(r"(?:[a-z0-9\)\]\*]\.|>)\s+")


def split_entries(stream: str) -> list[str]:
    markers = list(YEAR_MARKER.finditer(stream))
    if not markers:
        return [stream.strip()] if stream.strip() else []
    starts = [0]
    for i in range(len(markers) - 1):
        seg = stream[markers[i].end(): markers[i + 1].start()]
        cand = None
        for t in TERMINAL.finditer(seg):
            if AUTHORS_FULL.match(seg[t.end():].strip()):
                cand = t.end()  # earliest terminal with clean author-list suffix
                break
        if cand is None:
            ts = list(TERMINAL.finditer(seg))
            cand = ts[-1].end() if ts else len(seg)
        starts.append(markers[i].end() + cand)
    starts.append(len(stream))
    return [stream[starts[i]:starts[i + 1]].strip()
            for i in range(len(markers)) if stream[starts[i]:starts[i + 1]].strip()]


def normalize_authors(seg: str) -> str:
    seg = seg.replace(", &", " and").replace(", and", " and")
    seg = re.sub(r"\s&\s", " and ", seg)
    return seg


def close_initials(s: str) -> str:
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\b([A-Z])\.\s([A-Z])\.", r"\1.\2.", s)
    return s


def extract_doi(s: str):
    m = re.search(r"<?https?://doi\.org/([^>\s]+)>?", s)
    if not m:
        return s, None
    doi = m.group(1).strip().rstrip(".")
    s = s[: m.start()] + s[m.end():]
    return s, doi


def extract_url(s: str):
    """Pull a non-DOI <http...> token; return (clean, url)."""
    m = re.search(r"<(https?://[^>\s]+)>", s)
    if not m:
        return s, None
    url = m.group(1).strip()
    s = s[: m.start()] + s[m.end():]
    return s, url


def clean_org_head(s: str) -> str:
    """Drop the APA period an organisation author carries before the year:
    'World Bank. (2024),' -> 'World Bank (2024),' (leaves 'Smith, J.A. (2024)')."""
    return re.sub(r"\b([A-Za-z]{3,})\.\s+\((\d{4}[a-z]?)\)", r"\1 (\2)", s)


def dashes(s: str) -> str:
    return s.replace("–", "-").replace("—", "-")


def convert_entry(entry: str) -> tuple[str, str]:
    entry = re.sub(r"\s+", " ", entry).strip()

    # Blinded self-citation.
    if "omitted for" in entry.lower() and "review" in entry.lower():
        m = re.match(r"^(.*?)\s*\(\d{4}[a-z]?\)", entry)
        head = (m.group(1).rstrip(".") if m else "Authors")
        yr = re.search(r"\((\d{4}[a-z]?)\)", entry)
        yr = yr.group(1) if yr else "2026"
        return f"{head} ({yr}), details omitted for double-blind review.", "blinded"

    entry, doi = extract_doi(entry)
    entry, url = extract_url(entry)
    entry = re.sub(r"\s+", " ", entry).strip()
    entry = re.sub(YEAR + r"\.", r"(\1),", entry)  # year period -> comma

    # --- Journal article ---
    art = re.match(
        r"^(?P<head>.*?\(\d{4}[a-z]?\)),\s+"
        r"(?P<title>.+?)\.\s+"
        r"\*(?P<jvol>[^*]+?),\s*(?P<vol>\d+)\*"
        r"(?:\((?P<issue>[^)]+)\))?"
        r",\s*(?P<pages>[^.]+?)\.?\s*$",
        entry,
    )
    if art:
        head = normalize_authors(art.group("head"))
        title = art.group("title").strip().rstrip(".")
        journal = art.group("jvol").strip()
        vol = art.group("vol")
        issue = art.group("issue")
        pages = dashes(art.group("pages").strip())
        out = f'{head}, "{title}", *{journal}*, Vol. {vol}'
        if issue:
            out += f" No. {dashes(issue)}"
        out += f", pp. {pages}"
        if doi:
            out += f", doi: {dashes(doi)}"
        out += "."
        return clean_org_head(close_initials(out)), "article"

    # --- Book chapter:  ... Title. In <eds> (Eds.), *Book* (Vol. X, pp. y-z). Pub. ---
    chap = re.match(
        r"^(?P<head>.*?\(\d{4}[a-z]?\)),\s+"
        r"(?P<title>.+?)\.\s+In\s+(?P<eds>.+?)\s+\(Eds?\.\),\s+"
        r"\*(?P<book>[^*]+)\*\s*"
        r"(?:\((?:Vol\.\s*(?P<vol>[^,)]+))?(?:,\s*)?(?:pp?\.\s*(?P<pages>[^)]+))?\))?"
        r"\.\s*(?P<pub>.+?)\.?\s*$",
        entry,
    )
    if chap:
        head = normalize_authors(chap.group("head"))
        title = chap.group("title").strip().rstrip(".")
        eds = normalize_authors(chap.group("eds").strip())
        book = chap.group("book").strip()
        vol = chap.group("vol")
        pages = chap.group("pages")
        pub = chap.group("pub").strip().rstrip(".")
        out = f'{head}, "{title}", in {eds} (Eds), *{book}*'
        if vol:
            out += f", Vol. {vol.strip()}"
        out += f", {pub}"
        if pages:
            out += f", pp. {dashes(pages.strip())}"
        out += "."
        return close_initials(out), "chapter"

    # --- Book / report / data set:  ... *Title*[ optional bracket]. Publisher. ---
    book = re.match(
        r"^(?P<head>.*?\(\d{4}[a-z]?\)),\s+"
        r"\*(?P<title>[^*]+)\*(?P<extra>\s*\((?:[^)]*ed\.)\)|\s*\[[^\]]+\])?"
        r"\.\s+(?P<pub>.+?)\.?\s*$",
        entry,
    )
    if book:
        head = normalize_authors(book.group("head"))
        title = book.group("title").strip()
        extra = book.group("extra") or ""
        pub = book.group("pub").strip().rstrip(".")
        out = f"{head}, *{title}*{extra}, {pub}"
        if doi:
            out += f", doi: {dashes(doi)}"
        if url:
            out += f", available at: {url}"
        out += "."
        return clean_org_head(close_initials(out)), "book"

    # --- Fallback: shared transforms only ---
    entry = normalize_authors(dashes(entry))
    if doi:
        entry = entry.rstrip().rstrip(".") + f", doi: {dashes(doi)}."
    elif url:
        entry = entry.rstrip().rstrip(".") + f", available at: {url}."
    return clean_org_head(close_initials(entry)), "other"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    write = "--write" in sys.argv
    expect = None
    if "--expect" in sys.argv:
        expect = int(sys.argv[sys.argv.index("--expect") + 1])

    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    m = re.search(r"(?m)^#+\s*References\s*$", text)
    if not m:
        print(f"!! No '## References' heading in {path}")
        sys.exit(2)

    head = text[: m.end()]
    body = text[m.end():]

    # Preserve special non-reference tails (contextual web sources, replication
    # notes) verbatim — they are handled by hand, not by the auto-converter.
    SENTINELS = [r"\*Additional contextual sources", r"\*Replication package"]
    tail = ""
    cut = len(body)
    for s in SENTINELS:
        sm = re.search(s, body)
        if sm and sm.start() < cut:
            cut = sm.start()
    if cut < len(body):
        tail = body[cut:].strip()
        body = body[:cut]

    # Strip pandoc-escaped brackets, collapse to one stream, re-split into entries.
    body = body.replace("\\[", "[").replace("\\]", "]")
    stream = re.sub(r"\s+", " ", body).strip()
    entries = split_entries(stream)

    out, counts = [], {}
    for e in entries:
        conv, kind = convert_entry(e)
        counts[kind] = counts.get(kind, 0) + 1
        out.append(conv)

    new_text = head + "\n\n" + "\n\n".join(out) + "\n"
    if tail:
        new_text += "\n" + tail + "\n"
    summary = ", ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
    total = len(out)

    flag = ""
    if expect is not None and total != expect:
        flag = f"  <<< COUNT MISMATCH expected {expect}, got {total}"

    if write:
        if expect is not None and total != expect:
            print(f"!! refusing to write {path}: {flag.strip()}")
            sys.exit(3)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_text)
        print(f"[written] {path}  ({total} entries: {summary})")
    else:
        print(f"=== DRY-RUN {path}  ({total} entries: {summary}){flag} ===\n")
        print("\n\n".join(out))


if __name__ == "__main__":
    main()
