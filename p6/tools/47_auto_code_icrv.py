#!/usr/bin/env python3
"""
47_auto_code_icrv.py — Auto-code ICRV for Y papers missing it.

Uses country names in title + abstract to infer ICRV regime:
  1 = Advanced (OECD high-income: USA, UK, Germany, Japan, Korea, Singapore, ...)
  2 = Upper-middle (China, Malaysia, Thailand, Brazil, Turkey, Mexico, ...)
  3 = Emerging (Vietnam, India, Indonesia, Philippines, Pakistan, ...)
  4 = Resource-rich/GCC (Saudi Arabia, UAE, Qatar, Nigeria, Kazakhstan, ...)
  5 = SIDS (Fiji, Malta, Mauritius, Caribbean)
  6 = Frontier/LDC (Cambodia, Myanmar, Ethiopia, Bangladesh, ...)
  0 = Multi-country (mixed sample, no single dominant context)

Conservative: only auto-code when single country is clearly dominant.
If ≥2 different ICRV groups detected → ICRV=0 (multi).
If no country detected → leave blank (TO_EXTRACT).
"""
import csv, re, os
from pathlib import Path
from datetime import date

TRACKER   = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
ABSTRACTS = "p6/tools/results/abstracts_20260520.csv"
LOG_OUT   = f"p6/tools/results/icrv_auto_log_{date.today().strftime('%Y%m%d')}.csv"

# ── Country → ICRV mapping ──────────────────────────────────────────────────
# Each entry: (regex_pattern, icrv_code, label)
COUNTRY_ICRV = [
    # ICRV 1 — Advanced
    (r'\b(US|U\.S\.|USA|United States|American)\b',           1, "USA"),
    (r'\b(UK|U\.K\.|United Kingdom|British|England)\b',       1, "UK"),
    (r'\bGerman(y|s)?\b',                                      1, "Germany"),
    (r'\bJapan(ese)?\b',                                       1, "Japan"),
    (r'\b(Korea[n]?|South Korea)\b',                           1, "Korea"),
    (r'\bSingapore(an)?\b',                                    1, "Singapore"),
    (r'\bAustralia[n]?\b',                                     1, "Australia"),
    (r'\bCanada(ian)?\b',                                      1, "Canada"),
    (r'\bFrance|French\b',                                     1, "France"),
    (r'\bItal(y|ian)\b',                                       1, "Italy"),
    (r'\bSpain|Spanish\b',                                     1, "Spain"),
    (r'\bPortugal(ese)?\b',                                    1, "Portugal"),
    (r'\bSweden|Swedish\b',                                    1, "Sweden"),
    (r'\bNorway|Norwegian\b',                                  1, "Norway"),
    (r'\bDenmark|Danish\b',                                    1, "Denmark"),
    (r'\bFinland|Finnish\b',                                   1, "Finland"),
    (r'\bNetherlands|Dutch\b',                                 1, "Netherlands"),
    (r'\bBelgium|Belgian\b',                                   1, "Belgium"),
    (r'\bSwitzerland|Swiss\b',                                 1, "Switzerland"),
    (r'\bAustria[n]?\b',                                       1, "Austria"),
    (r'\bNew Zealand(er)?\b',                                  1, "NZ"),
    (r'\bIsrael(i)?\b',                                        1, "Israel"),
    (r'\bTaiwan(ese)?\b',                                      1, "Taiwan"),
    (r'\bHong Kong\b',                                         1, "HongKong"),
    (r'\bGreece|Greek\b',                                      1, "Greece"),
    (r'\bIreland|Irish\b',                                     1, "Ireland"),
    (r'\bCzech\b',                                             1, "Czech"),
    (r'\bPoland|Polish\b',                                     1, "Poland"),
    (r'\bHungary|Hungarian\b',                                 1, "Hungary"),

    # ICRV 2 — Upper-middle
    (r'\bChina|Chinese\b',                                     2, "China"),
    (r'\bMalaysia[n]?\b',                                      2, "Malaysia"),
    (r'\bThailand|Thai\b',                                     2, "Thailand"),
    (r'\bBrazil(ian)?\b',                                      2, "Brazil"),
    (r'\bTurkey|Turkish\b',                                    2, "Turkey"),
    (r'\bMexico|Mexican\b',                                    2, "Mexico"),
    (r'\bSouth Africa[n]?\b',                                  2, "SouthAfrica"),
    (r'\bArgentina[n]?\b',                                     2, "Argentina"),
    (r'\bColombia[n]?\b',                                      2, "Colombia"),
    (r'\bPeru(vian)?\b',                                       2, "Peru"),
    (r'\bEcuador(ian)?\b',                                     2, "Ecuador"),
    (r'\bJordan(ian)?\b',                                      2, "Jordan"),
    (r'\bMorocco|Moroccan\b',                                  2, "Morocco"),
    (r'\bTunisia[n]?\b',                                       2, "Tunisia"),
    (r'\bEgypt(ian)?\b',                                       2, "Egypt"),
    (r'\bIran(ian)?\b',                                        2, "Iran"),
    (r'\bRomania[n]?\b',                                       2, "Romania"),
    (r'\bBulgaria[n]?\b',                                      2, "Bulgaria"),
    (r'\bSerbia[n]?\b',                                        2, "Serbia"),

    # ICRV 3 — Emerging
    (r'\bVietnam(ese)?\b',                                     3, "Vietnam"),
    (r'\bIndia[n]?\b',                                         3, "India"),
    (r'\bIndonesia[n]?\b',                                     3, "Indonesia"),
    (r'\bPhilippines|Filipino|Philippine\b',                   3, "Philippines"),
    (r'\bPakistan(i)?\b',                                      3, "Pakistan"),
    (r'\bBangladesh(i)?\b',                                    3, "Bangladesh"),
    (r'\bSri Lanka[n]?\b',                                     3, "SriLanka"),
    (r'\bGhana(ian)?\b',                                       3, "Ghana"),
    (r'\bKenya[n]?\b',                                         3, "Kenya"),
    (r'\bTanzania[n]?\b',                                      3, "Tanzania"),
    (r'\bUganda[n]?\b',                                        3, "Uganda"),
    (r'\bEthiopia[n]?\b',                                      3, "Ethiopia"),
    (r'\bSenegal(ese)?\b',                                     3, "Senegal"),
    (r'\bCambodia[n]?\b',                                      3, "Cambodia"),
    (r'\bMyanmar|Burmese\b',                                   3, "Myanmar"),
    (r'\bNepal(ese)?\b',                                       3, "Nepal"),
    (r'\bBolivia[n]?\b',                                       3, "Bolivia"),
    (r'\bHonduras|Honduran\b',                                 3, "Honduras"),
    (r'\bNicaragua[n]?\b',                                     3, "Nicaragua"),
    (r'\bGuatemala[n]?\b',                                     3, "Guatemala"),

    # ICRV 4 — Resource-rich / GCC
    (r'\bSaudi Arabia[n]?|KSA\b',                              4, "SaudiArabia"),
    (r'\bUAE|United Arab Emirates\b',                          4, "UAE"),
    (r'\bQatar(i)?\b',                                         4, "Qatar"),
    (r'\bKuwait(i)?\b',                                        4, "Kuwait"),
    (r'\bBahrain(i)?\b',                                       4, "Bahrain"),
    (r'\bOman(i)?\b',                                          4, "Oman"),
    (r'\bNigeria[n]?\b',                                       4, "Nigeria"),
    (r'\bAngola[n]?\b',                                        4, "Angola"),
    (r'\bKazakhstan\b',                                        4, "Kazakhstan"),
    (r'\bAzerbaijan\b',                                        4, "Azerbaijan"),
    (r'\bTurkmenistan\b',                                      4, "Turkmenistan"),
    (r'\bLibya[n]?\b',                                         4, "Libya"),
    (r'\bAlgeria[n]?\b',                                       4, "Algeria"),
    (r'\bIraq(i)?\b',                                          4, "Iraq"),
    (r'\bGabon(ese)?\b',                                       4, "Gabon"),

    # ICRV 5 — SIDS
    (r'\bMalta\b',                                             5, "Malta"),
    (r'\bMauritius\b',                                         5, "Mauritius"),
    (r'\bFiji(an)?\b',                                         5, "Fiji"),
    (r'\bSamoa[n]?\b',                                         5, "Samoa"),
    (r'\bBarbados\b',                                          5, "Barbados"),
    (r'\bJamaica[n]?\b',                                       5, "Jamaica"),
    (r'\bTrinidad\b',                                          5, "Trinidad"),
    (r'\bCyprus\b',                                            5, "Cyprus"),
    (r'\bMaldives\b',                                          5, "Maldives"),
    (r'\bCape Verde\b',                                        5, "CapeVerde"),

    # ICRV 6 — Frontier/LDC
    (r'\bMali(an)?\b',                                         6, "Mali"),
    (r'\bBurkina Faso\b',                                      6, "BurkinaFaso"),
    (r'\bNiger\b(?!ia)',                                       6, "Niger"),
    (r'\bChad(ian)?\b',                                        6, "Chad"),
    (r'\bSierra Leone\b',                                      6, "SierraLeone"),
    (r'\bLiberia[n]?\b',                                       6, "Liberia"),
    (r'\bMozambique[an]?\b',                                   6, "Mozambique"),
    (r'\bMadagascar\b',                                        6, "Madagascar"),
    (r'\bZambia[n]?\b',                                        6, "Zambia"),
    (r'\bZimbabwe[an]?\b',                                     6, "Zimbabwe"),
    (r'\bRwanda[n]?\b',                                        6, "Rwanda"),
    (r'\bBurundi\b',                                           6, "Burundi"),
    (r'\bSomalia[n]?\b',                                       6, "Somalia"),
    (r'\bAfghanistan\b',                                       6, "Afghanistan"),
    (r'\bYemen(i)?\b',                                         6, "Yemen"),
    (r'\bHaiti(an)?\b',                                        6, "Haiti"),

    # Multi-country signals (if found alongside single-country → ICRV=0)
    (r'\bmulti.countr(y|ies)\b',                               0, "multi_country"),
    (r'\bcross.countr(y|ies)\b',                               0, "cross_country"),
    (r'\b\d{2,3} (countries|economies|nations)\b',            0, "N_countries"),
    (r'\b(emerging|developing) (market|econom)',               0, "emerging_markets"),
    (r'\bASEAN\b',                                             0, "ASEAN"),
    (r'\bBRICS?\b',                                            0, "BRICS"),
    (r'\bG20\b',                                               0, "G20"),
    (r'\bOECD (countries|economies|members)\b',               0, "OECD"),
    (r'\bEuropean (Union|firms?|countries)\b',                 0, "EU"),
    (r'\bAsia.Pacific\b',                                      0, "AsiaPacific"),
    (r'\bworld.?wide|global (sample|survey|data)\b',           0, "global"),
]


def detect_icrv(title: str, abstract: str) -> tuple[str, str]:
    """
    Returns (icrv_code_str, reason).
    icrv_code_str: '0'-'6' or '' (cannot determine).
    """
    text = f"{title} {abstract}"
    hits: dict[int, list[str]] = {}

    for pattern, code, label in COUNTRY_ICRV:
        if re.search(pattern, text, re.IGNORECASE):
            hits.setdefault(code, []).append(label)

    if not hits:
        return "", "no_country_detected"

    # Multi-country signal present
    if 0 in hits:
        return "0", f"multi:{','.join(hits[0][:3])}"

    # Single ICRV group detected
    if len(hits) == 1:
        code = list(hits.keys())[0]
        return str(code), f"single:{','.join(hits[code][:3])}"

    # Multiple different ICRV groups → multi-country
    all_labels = [l for lbls in hits.values() for l in lbls]
    return "0", f"multi_inferred:{','.join(all_labels[:4])}"


def main():
    # Load abstracts
    abs_map: dict[str, str] = {}
    if Path(ABSTRACTS).exists():
        with open(ABSTRACTS, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                seq = r.get("seq", "").strip()
                ab  = r.get("abstract", "").strip()
                if seq and ab:
                    abs_map[seq] = ab

    with open(TRACKER, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    cols = list(rows[0].keys())

    target = [r for r in rows
              if r.get("fulltext_screening_decision", "") == "Y"
              and not r.get("icrv", "").strip()]

    print(f"Y papers missing ICRV: {len(target)}")

    log_rows = []
    coded, skipped = 0, 0

    for row in target:
        seq      = row.get("seq", "").strip()
        title    = row.get("title", "")
        abstract = abs_map.get(seq, "")

        icrv_code, reason = detect_icrv(title, abstract)

        log_rows.append({
            "seq": seq, "title": title[:70],
            "icrv_auto": icrv_code, "reason": reason,
            "has_abstract": "Y" if abstract else "N",
        })

        if icrv_code:
            row["icrv"] = icrv_code
            coded += 1
        else:
            skipped += 1

    print(f"Auto-coded:  {coded}")
    print(f"Still blank: {skipped}")

    # Distribution
    from collections import Counter
    dist = Counter(l["icrv_auto"] for l in log_rows if l["icrv_auto"])
    print("\nICRV distribution (auto-coded):")
    for k in sorted(dist, key=lambda x: (x == "", int(x) if x else -1)):
        label = {
            "0": "Multi-country", "1": "Advanced", "2": "Upper-middle",
            "3": "Emerging", "4": "Resource-rich/GCC", "5": "SIDS", "6": "Frontier"
        }.get(k, k)
        print(f"  ICRV {k} ({label}): {dist[k]}")

    # Atomic write
    tmp = TRACKER + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, TRACKER)

    # Write log
    with open(LOG_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["seq","title","icrv_auto","reason","has_abstract"])
        w.writeheader()
        w.writerows(log_rows)

    print(f"\nTracker updated: {TRACKER}")
    print(f"Log: {LOG_OUT}")


if __name__ == "__main__":
    main()
