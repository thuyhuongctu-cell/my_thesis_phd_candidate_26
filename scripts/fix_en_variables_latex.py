#!/usr/bin/env python3
"""Convert bare Unicode statistical notation in the English manuscripts to
LaTeX inline math (Scopus/WoS standard), per the academic-variable-formatter
skill. Protects any existing $...$ / $$...$$ math. Ordered most-specific first
so compound expressions wrap as a single math span, e.g.
  FSTS_c² × DAI_z   ->  $\\text{FSTS}_c^2 \\times \\text{DAI}_z$
  β₁ > 0            ->  $\\beta_1$ > 0
  R²                ->  $R^2$
Usage: python3 scripts/fix_en_variables_latex.py FILE [FILE ...]
"""
import re, sys

VARS = r"FSTS|DAI|TCI|DDXK|ICRV|DOI|WGI"
SUP = {"²": "2", "³": "3"}

def term_latex(t):
    m = re.match(rf"^({VARS})(?:_([a-z]))?([²³])?$", t)
    var, sub, sup = m.group(1), m.group(2), m.group(3)
    s = r"\text{" + var + "}"
    if sub:
        s += "_" + sub
    if sup:
        s += "^" + SUP[sup]
    return s

TERM = rf"(?:{VARS})(?:_[a-z])?[²³]?"
CHAIN = re.compile(rf"({TERM})((?:\s*×\s*{TERM})+)")          # 2+ terms with ×
DECOR = re.compile(rf"(?<![A-Za-z\\])({VARS})(?:_([a-z]))([²³]?)")  # VAR_sub(sup)
SUPSTAT = [("FSTSc²", r"$\text{FSTS}_c^2$"), ("FSTSc", r"$\text{FSTS}_c$"),
           ("ΔR²", r"$\Delta R^2$"), ("R²", r"$R^2$"), ("I²", r"$I^2$"),
           ("f²", r"$f^2$"), ("χ²", r"$\chi^2$"), ("η²", r"$\eta^2$"),
           ("ω²", r"$\omega^2$"), ("s²", r"$s^2$"), ("FSTS²", r"$\text{FSTS}^2$"),
           ("FSTS³", r"$\text{FSTS}^3$")]
BETASUB = [(f"β{u}", rf"$\beta_{d}$") for u, d in
           zip("₀₁₂₃₄₅₆₇₈₉", "0123456789")]
GREEK = {"β": r"\beta", "ρ": r"\rho", "σ": r"\sigma", "χ": r"\chi",
         "τ": r"\tau", "η": r"\eta", "λ": r"\lambda", "μ": r"\mu",
         "Δ": r"\Delta", "α": r"\alpha", "γ": r"\gamma", "θ": r"\theta",
         "π": r"\pi", "φ": r"\phi", "ω": r"\omega", "ε": r"\epsilon"}
OPS = {"≈": r"$\approx$", "≤": r"$\leq$", "≥": r"$\geq$", "±": r"$\pm$",
       "≠": r"$\neq$"}
MATH = re.compile(r"(\$\$.*?\$\$|\$[^$\n]*\$|\\begin\{[^}]*\}.*?\\end\{[^}]*\})", re.S)

def chain_repl(m):
    terms = re.split(r"\s*×\s*", m.group(0))
    return "$" + r" \times ".join(term_latex(t) for t in terms) + "$"

def decor_repl(m):
    var, sub, sup = m.group(1), m.group(2), m.group(3)
    s = r"$\text{" + var + "}_" + sub
    if sup:
        s += "^" + SUP[sup]
    return s + "$"

def conv(seg):
    # Skip Markdown table rows: their cells hold identifier tokens
    # (e.g. joint_F_DAI_rich_interactions) that must not be mathified.
    return "\n".join(ln if ln.lstrip().startswith("|") else conv_line(ln)
                     for ln in seg.split("\n"))

def conv_line(seg):
    seg = CHAIN.sub(chain_repl, seg)          # 1) compound × chains
    seg = DECOR.sub(decor_repl, seg)          # 2) standalone VAR_sub(sup)
    for u, t in SUPSTAT:                        # 3) stat superscripts
        seg = seg.replace(u, t)
    for u, t in BETASUB:                        # 4) β with unicode subscript
        seg = seg.replace(u, t)
    # 4b) meta-analysis prose notation: σ²_(2), *I*²_(2), *I*²_total, *t*², *f*²
    seg = re.sub(r"σ²_\((\d)\)", r"$\\sigma^2_{(\1)}$", seg)
    seg = re.sub(r"σ²", r"$\\sigma^2$", seg)
    seg = re.sub(r"\*([A-Za-z])\*²_\((\d)\)", r"$\1^2_{(\2)}$", seg)
    seg = re.sub(r"\*([A-Za-z])\*²_total", r"$\1^2_{\\text{total}}$", seg)
    seg = re.sub(r"\*([A-Za-z])\*²", r"$\1^2$", seg)
    seg = re.sub(r"\*([A-Za-z])\*³", r"$\1^3$", seg)
    seg = seg.replace("fsts_c²", r"$\text{FSTS}_c^2$").replace("fsts_c", r"$\text{FSTS}_c$")
    for u, t in GREEK.items():                 # 5) bare greek letters
        seg = re.sub(rf"(?<![\\A-Za-z]){u}", lambda m, t=t: f"${t}$", seg)
    for u, t in OPS.items():                    # 6) operators
        seg = seg.replace(u, t)
    seg = seg.replace("×", r"$\times$")        # 7) remaining bare multiply
    return seg

CUR = re.compile(r"(?<!\\)\$(?=\d)")   # currency: $ before a digit (not math)

def main():
    for path in sys.argv[1:]:
        text = open(path, encoding="utf-8").read()
        # Protect literal currency ($20.17) so it never pairs with math $.
        text = CUR.sub("\x00CUR\x00", text)
        parts = MATH.split(text)            # protect existing $...$ / $$...$$
        new = "".join(p if i % 2 else conv(p) for i, p in enumerate(parts))
        new = new.replace("\x00CUR\x00", r"\$")   # restore as escaped currency
        bal = new.count("$") - new.count(r"\$")   # math $ must be even
        open(path, "w", encoding="utf-8").write(new)
        left = len(re.findall(r"[βρσχτηλμΔαγθπφωε²³≈≤≥±≠×]", new))
        flag = "OK" if bal % 2 == 0 else "‼ ODD-$ (unbalanced!)"
        print(f"{path}: residual unicode={left} | math-$ balance={bal} {flag}")

if __name__ == "__main__":
    main()
