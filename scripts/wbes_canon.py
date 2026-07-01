"""Shared WBES filename canonicalization for raw .dta archive + CD1 pipeline.

Parses heterogeneous WBES file names (zip-extracted "Country-YYYY-full-data.dta"
and loose "CountryYYYYfulldata.dta") into a canonical (country, year, instrument)
key so the archive can be deduplicated by economy-year and the pipeline can map
every file to the master country name regardless of naming style.
"""
from __future__ import annotations
import os
import re

# normalized-key (lowercase, alpha-only) -> master canonical country name
_CANON = {
    "afghanistan": "Afghanistan", "armenia": "Armenia", "azerbaijan": "Azerbaijan",
    "bahrain": "Bahrain", "bangladesh": "Bangladesh", "bhutan": "Bhutan",
    "brunei": "Brunei", "bruneidarussalam": "Brunei", "cambodia": "Cambodia",
    "china": "China", "comoros": "Comoros", "cyprus": "Cyprus",
    "republicofcyprus": "Cyprus", "fiji": "Fiji", "georgia": "Georgia",
    "hongkong": "HongKong", "hongkongsarchina": "HongKong", "india": "India",
    "indonesia": "Indonesia", "iraq": "Iraq", "israel": "Israel", "japan": "Japan",
    "jordan": "Jordan", "kazakhstan": "Kazakhstan", "kenya": "Kenya",
    "kiribati": "Kiribati", "korea": "Korea", "korearep": "Korea",
    "korearepublic": "Korea", "kosovo": "Kosovo", "kuwait": "Kuwait",
    "kyrgyzrepublic": "KyrgyzRepublic", "kyrgyzrep": "KyrgyzRepublic",
    "lao": "Laos", "laos": "Laos", "laopdr": "Laos", "lebanon": "Lebanon",
    "malaysia": "Malaysia", "maldives": "Maldives", "mongolia": "Mongolia",
    "myanmar": "Myanmar", "nepal": "Nepal", "oman": "Oman", "pakistan": "Pakistan",
    "papuanewguinea": "PapuaNewGuinea", "philippines": "Philippines",
    "qatar": "Qatar", "samoa": "Samoa", "saudi": "SaudiArabia",
    "saudiarabia": "SaudiArabia", "singapore": "Singapore",
    "solomonislands": "SolomonIslands", "srilanka": "SriLanka",
    "taiwan": "Taiwan", "taiwanchina": "Taiwan", "tajikistan": "Tajikistan",
    "thailand": "Thailand", "timorleste": "TimorLeste", "tonga": "Tonga",
    "turkey": "Turkey", "turkiye": "Turkey", "turkmenistan": "Turkmenistan",
    "uzbekistan": "Uzbekistan", "vanuatu": "Vanuatu", "vietnam": "Vietnam",
    "viet": "Vietnam", "vietname": "Vietnam", "westbankandgaza": "WestBankGaza",
    "westbankgaza": "WestBankGaza", "yemen": "Yemen",
}

# Economies retained in the dissertation's Asia-Pacific universe (master 52-frame
# minus the three out-of-region drops). NON_ASIA are archived-out on request.
NON_ASIA = {"Kenya", "Kosovo", "Cyprus", "Turkey", "WestBankGaza"}
MIN_YEAR = 2006  # pre-2006 WBES waves use a non-comparable instrument — excluded
# Comoros (African SIDS) is retained ONLY for the P8 9-economy robustness set.

# instrument tags that are NOT the standard private-firm cross-section
_NONSTANDARD = ("informal", "isbs", "ises", "micro", "expansion", "longform",
                "esn", "esis", "panel", "tgs", "followup")


def canon_country(raw: str) -> str | None:
    key = re.sub(r"[^a-z]", "", raw.lower())
    return _CANON.get(key)


def parse(path: str):
    """Return dict(country, year, standard, panel) or None if unparseable."""
    name = re.sub(r"\.dta$", "", os.path.basename(path), flags=re.I)
    name = re.sub(r"^[0-9a-f]{6,}-", "", name)            # strip upload hash prefix
    years = re.findall(r"(?:19|20)\d{2}", name)
    if not years:
        return None
    m = re.search(r"(?:19|20)\d{2}", name)
    country = canon_country(name[:m.start()])
    if country is None:
        return None
    # Drop the sample-size annotation (e.g. "-N2700" in "...full-ES-N2700-data")
    # before tokenising; otherwise "ES-N####" collapses to "esn", which both
    # breaks the contiguous "fulldata" test and spuriously matches the
    # _NONSTANDARD "esn" instrument tag, dropping a valid full cross-section.
    tail = re.sub(r"[-_]n\d+", "", name[m.start():].lower())
    suffix = re.sub(r"[^a-z]", "", tail)
    panel = len(years) > 1                                # multi-wave panel file
    year = int(years[0])
    # pre-2006 WBES used a non-comparable questionnaire; excluded by scope rule
    standard = ("full" in suffix and "data" in suffix) and year >= MIN_YEAR \
        and not any(t in suffix for t in _NONSTANDARD)
    return {"country": country, "year": year,
            "standard": standard, "panel": panel}
