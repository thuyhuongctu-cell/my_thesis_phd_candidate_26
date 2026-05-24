# P6 — Database Mã hóa Nghiên cứu Sơ cấp (Coded Study Database)
# Meta-Analysis I→P 1982–2026

> **Phiên bản**: v1.0 (12/05/2026) — Bản làm việc nội bộ
>
> **Mục đích**: Cơ sở dữ liệu mã hóa đầy đủ 7 moderators cho toàn bộ studies đủ tiêu chuẩn của P6.
> Đây là file trung tâm cho three-level MARA (metafor R).
>
> **Baseline**: 110 studies từ ICBEF 2025 + ~25 studies mới từ backward citation scan (Bausch &
> Krist 2007; Kirca et al. 2012; Marano et al. 2016; Yang & Driffield 2012; Wu et al. 2022;
> Arte & Larimo 2022) và literature 2022–2026.
>
> **Tham chiếu kế hoạch**: `p6/06_p6_meta_update_plan_vi.md` (P0 priority, Tuần 1–6)
> **APA 7th citations**: `p6/p6_primary_studies_apa7.md`

---

## 1. Hướng dẫn Mã hóa 7 Moderators

### 1.1 ICRV Regime (World Governance Indicators — Rule of Law)

Phân loại theo quốc gia mẫu và WGI Rule of Law (trung bình 2000–2020).
Với studies đa quốc gia: dùng quốc gia đa số hoặc ghi Mixed.

| Mã | Nhóm | WGI RoL | Quốc gia điển hình |
|----|------|---------|-------------------|
| **I** | Advanced | > +0.80 | USA (+1.56), UK (+1.74), Germany (+1.78), Japan (+1.74), South Korea (+1.03), Singapore (+1.78), HK (+1.55), Taiwan (+1.2), Australia (+1.79), Canada (+1.77), Israel (+0.88), Netherlands (+1.77), Sweden (+1.90), Switzerland (+1.90), Nordic countries |
| **II** | Upper-middle | 0 to +0.80 | Italy (+0.33), Spain (+0.72), Portugal (+1.00 border.), Poland (+0.53), Malaysia (+0.52), Jordan (+0.20), South Africa (+0.09), Chile (+0.71), Georgia (+0.07), Czech Republic (+0.89 border.) |
| **III** | Emerging | −0.50 to 0 | China (−0.27), India (−0.08), Vietnam (−0.39), Indonesia (−0.33), Philippines (−0.42), Thailand (−0.10), Turkey (−0.15), Brazil (−0.19), Mexico (−0.53 border.), Argentina (−0.40), Egypt (−0.45), Sri Lanka (−0.17) |
| **SIDS** | Pacific Islands | varies | Fiji, Samoa, Tonga, Vanuatu, Solomon Islands, Kiribati |
| **FR** | Frontier | < −0.50 | Bangladesh (−0.76), Pakistan (−0.93), Myanmar (−1.17), Cambodia (−0.80), Nigeria (−1.04), Iran (−1.10), Afghanistan (−1.90) |
| **MX** | Mixed | multi-regime | Studies crossing ≥2 regimes without clear majority |

**Ghi chú**: WGI values approximate, sourced from World Bank WGI dataset.
Czech Republic borderline I/II; South Africa borderline II/III; Mexico borderline III/FR.
Khi uncertain, ghi regime trước và thêm "?" (e.g., II?).

---

### 1.2 cDAI Level (Country-level Digital Adoption Index)

Kết hợp quốc gia + giai đoạn dữ liệu. Proxy cho ITU DDI / WB Digital Adoption Index.

| Mã | Mức | Tiêu chí |
|----|-----|----------|
| **H** | High | Regime I country AND data period substantially overlaps post-2010; OR Singapore/Korea/Japan/Nordic post-2000 (early high-digital adopters) |
| **M** | Medium | Regime I country with data pre-2005; OR Regime II country with data post-2010; OR Multi-country post-2015 with majority Regime I-II |
| **L** | Low | Regime III/SIDS/FR country regardless of period; OR any country with data pre-1998; OR Regime II country pre-2010 |

**Proxy rule**: Nếu data period không rõ, dùng năm xuất bản − 4 năm làm ước lượng data end year.

---

### 1.3 DPL Phase (Digital Paradox Lifecycle)

Mã hóa theo giai đoạn thu thập dữ liệu so với mốc 2009 (Brynjolfsson et al., 2021).

| Mã | Phase | Tiêu chí data period |
|----|-------|---------------------|
| **PRE** | Precede | Data collection ends substantially before 2009 (data end year ≤ 2008; published ≤ 2012 with pre-2009 data) |
| **SPN** | Span | Data spans or substantially overlaps 2009 inflection point (data period 2005–2014) |
| **FOL** | Follow | Data collection mainly post-2014 (data start year ≥ 2013; published ≥ 2018 with explicit post-2014 data) |

**Proxy rule (publication year)**:
- Published ≤ 2011: PRE (data typically 1990s–2008)
- Published 2012–2016: SPN (data typically 2005–2013)
- Published 2017–2019: SPN→FOL borderline; default SPN unless post-2014 data stated
- Published 2020+: FOL (data typically 2014–2021)

---

### 1.4 DOI Measure Type

| Mã | Loại | Mô tả |
|----|------|-------|
| **FSTS** | Foreign Sales / Total Sales | Tỷ lệ doanh thu nước ngoài |
| **EXP** | Export ratio/dummy | Export intensity hoặc export dummy |
| **FDI** | FDI intensity | FDI/assets hoặc FDI dummy |
| **GEO** | Geographic scope | Số thị trường, entropy of geographic diversification |
| **COMP** | Composite | Kết hợp ≥2 loại (FSTS + GEO + FDI) |
| **OTH** | Other | Khác (e.g., overseas assets ratio, R&D/IP licensing) |

---

### 1.5 FP Measure Type

| Mã | Loại | Mô tả |
|----|------|-------|
| **ACC** | Accounting-based | ROA, ROE, ROS, profit margin, EBIT |
| **MKT** | Market-based | Tobin's Q, market-to-book, stock return |
| **LAB** | Labor productivity | Revenue/employee, VA/employee (WBES-compatible) |
| **MIX** | Mixed | Combination of ACC + MKT |
| **OTH** | Other | Sales growth, survival, export revenue |

---

### 1.6 DOI và FP Measure — Coding notes

Khi study báo cáo nhiều effect sizes với different DOI/FP measures, mã hóa DOI và FP của effect size được chọn ưu tiên nhất (theo thứ tự ưu tiên: FSTS > COMP > GEO > EXP > FDI > OTH; ROA > ROS > ROE > Tobin's Q > OTH).

---

## 2. Tiêu chí Inclusion/Exclusion (7 + 6)

### Inclusion (7 tiêu chí — phải thỏa tất cả):

1. **Empirical quantitative** ở cấp doanh nghiệp (không phải industry/country level)
2. **Đo lường internationalization** bất kỳ dạng (FSTS, DOI, export, FDI, geographic scope)
3. **Đo lường firm performance** bất kỳ dạng (accounting, market, labor productivity)
4. **Effect size có thể tính**: cung cấp r, β, t, F, χ² đủ để convert sang Pearson r
5. **Peer-reviewed journal** article HOẶC conference proceedings được trích dẫn rộng rãi (≥20 citations)
6. **Xuất bản 1982–2026**
7. **Ngôn ngữ**: tiếng Anh (ưu tiên); hoặc ngôn ngữ khác với abstract tiếng Anh đầy đủ

### Exclusion (6 tiêu chí — bất kỳ một điều kiện nào → loại):

1. Lý thuyết/conceptual, không có dữ liệu empirical
2. Không có effect size tính được (regression only without r, n, F)
3. **Sample trùng lặp** với study khác trong pool → giữ study có sample lớn hơn
4. Industry-level hoặc country-level analysis (không phải firm-level)
5. Qualitative hoặc mixed-method không có phần định lượng rõ ràng
6. Unpublished thesis (trừ khi đã published dưới dạng journal article riêng biệt)

---

## 3. Ký hiệu trong bảng

- `†` = citation đã có trong `thesis/04_references_apa7.md` v2.7
- `*` = DOI/citation cần verify thêm
- `NEW` = study mới, không có trong baseline 110 (ICBEF 2025)
- `?` = cần kiểm tra lại khi có full text

---

## 4. Database Chính — Toàn bộ Studies Đủ Tiêu Chuẩn

### Nhóm A: 110 Studies Baseline (ICBEF 2025)

Các cột: **ID | Author-Year | r (range) | n | Country | Sample_period | ICRV | cDAI | DPL | DOI | FP | Notes**

| ID | Author-Year | r | n | Country | Period | ICRV | cDAI | DPL | DOI | FP | Notes |
|----|-------------|---|---|---------|--------|------|------|-----|-----|----|-------|
| S01 | Siddharthan & Lall (1982) | −0.197 | 74 | UK | ~1978–81 | I | L | PRE | FSTS | ACC | US MNE sub.† |
| S02 | Grant (1987)† | 0.145/0.163/0.107/−0.036 | 304 | UK | ~1981–85 | I | L | PRE | GEO | ACC | British mfg |
| S03 | Sambharya (1995)† | −0.02 to 0.03 | 53 | USA | ~1988–92 | I | L | PRE | GEO | ACC | US MNEs |
| S04 | McDougall & Oviatt (1996) | −0.03 | 62 | USA | ~1988–93 | I | L | PRE | EXP | ACC | New ventures |
| S05 | Tallman & Li (1996)† | 0.01/0.19 | 192 | USA | ~1987–91 | I | L | PRE | GEO | ACC | AMJ |
| S06 | Hitt et al. (1997)† | 0.01 | 295 | USA | ~1987–93 | I | L | PRE | FSTS | ACC | AMJ; Innovation mod. |
| S07 | Wan (1998)† | −0.15 to 0.41 | 47–81 | Hong Kong | ~1990–95 | I | L | PRE | GEO | ACC | APJM |
| S08 | Gomes & Ramaswamy (1999)† | 0.149/−0.45 | 95 | USA | ~1989–95 | I | L | PRE | FSTS | ACC | JIBS; inverted-U |
| S09 | Li (2001)† | 0.07 | 1,684 | Multi | ~1993–97 | MX | L | PRE | GEO | ACC | JIE |
| S10 | Qian (2002) | 0.43 | 71 | USA/Multi | ~1996–99 | I | L | PRE | COMP | ACC | JBV |
| S11 | Capar & Kotabe (2003) | 0.341 | 81 | Germany | ~1996–99 | I | L | PRE | FSTS | ACC | Services JIBS |
| S12 | Hsu & Boggs (2003)† | 0.037–0.85 | 118 | Taiwan | ~1996–01 | I | L | PRE | FSTS | ACC | 8 effects |
| S13 | Ruigrok & Wagner (2003) | −0.065 to −0.22 | 84/420 | Germany | ~1993–00 | I | L | PRE | FSTS | ACC | JIBS; 4 effects |
| S14 | Majocchi & Zucchella (2003) | 0.06/0.11 | 220 | Italy | ~1997–00 | II | L | PRE | EXP | ACC | Italian SMEs |
| S15 | Carpenter & Sanders (2004) | 0.27 | 224 | USA | ~1997–00 | I | L | PRE | FSTS | ACC | Upper Echelons |
| S16 | Kim et al. (2004)† | −0.101 to 0.03 | 295 | Korea | ~1997–01 | I | L | PRE | GEO | ACC | Korean firms 4 eff |
| S17 | Lu & Beamish (2004)† | −0.06 | 1,489 | Japan | ~1986–97 | I | L | PRE | GEO | ACC | SMJ; S-curve |
| S18 | Thomas & Eden (2004) | −0.01 to 0.17 | 151 | USA | ~1998–02 | I | L | PRE | FSTS | ACC | MBR; 4 effects |
| S19 | Chiao et al. (2006) | 0.056 | 1,419 | Taiwan | ~1998–02 | I | L | PRE | EXP | ACC | Taiwan SMEs |
| S20 | Elango (2006) | 0.125/0.226 | 326/393 | USA | ~1998–03 | I | L | PRE | FSTS | MIX | MBR 2 subsamples |
| S21 | Hsu (2006)† | 0.369 | 255 | Taiwan | ~1999–03 | I | L | PRE | FSTS | ACC | |
| S22 | Thomas (2006) | 0.027 | 386 | Mexico | ~1999–03 | III | L | PRE | EXP | ACC | Mexico firms |
| S23 | Chari et al. (2007) | 0.25/0.37 | 131 | USA | ~2000–04 | I | L | PRE | COMP | MIX | JWB 2 effects |
| S24 | Fortanier et al. (2007) | 0.10 | 332 | Multi | ~2000–04 | MX | L | PRE | FSTS | ACC | Host-country focus |
| S25 | Kumar & Gaur (2007) | 0.343 | 240 | India | ~2000–04 | III | L | PRE | GEO | ACC | Indian groups |
| S26 | Ruigrok et al. (2007) | −0.138 | 87 | Switzerland | ~2000–04 | I | L | PRE | FSTS | ACC | Swiss firms |
| S27 | Richter (2007)† | −0.058 | 85 | Germany | ~2000–04 | I | L | PRE | FSTS | ACC | |
| S28 | Vilas-Boas & González (2007) | −0.13/0.17 | 291 | Spain | ~2000–04 | II | L | PRE | EXP | ACC | Spanish firms |
| S29 | Bae et al. (2008) | 0.01–0.11 | 672 | Korea | ~2001–05 | I | L | PRE | FSTS | ACC | 5 effects |
| S30 | Brock & Yaffe (2008) | −0.04/0.08 | 89 | Israel | ~2001–05 | I | L | PRE | GEO | ACC | 4 effects |
| S31 | Kumar & Singh (2008) | −0.145/−0.30 | 75 | India | ~2001–05 | III | L | PRE | EXP | LAB | India mfg |
| S32 | Pangarkar (2008)† | 0.247/0.286 | 94 | Singapore | ~2001–05 | I | L | PRE | FSTS | ACC | Singapore listed |
| S33 | Qian et al. (2008)† | 0.232 | 189 | USA/Multi | ~2001–05 | I | L | PRE | GEO | ACC | |
| S34 | Garbe & Richter (2009) | −0.034 to −0.136 | 85 | Germany | ~2002–06 | I | L | PRE | FSTS | ACC | 3 effects |
| S35 | Gaur & Kumar (2009) | −0.075 | 240 | India | ~2002–06 | III | L | PRE | GEO | ACC | India business groups |
| S36 | Pattnaik & Elango (2009) | −0.02 | 787 | India | ~2002–06 | III | L | PRE | EXP | ACC | India exporters |
| S37 | Ciszewska-Mlinaric & Mlinaric (2010) | 0.049–0.217 | 67 | Poland | ~2004–08 | II | L | SPN | EXP | ACC | Polish SMEs 6 eff |
| S38 | Chao & Kumar (2010) | 0.169 | 500 | Multi | ~2004–07 | MX | L | SPN | COMP | ACC | Inst.distance mod |
| S39 | Chen & Hsu (2010)† | 0.164 | 224 | Taiwan | ~2004–08 | I | L | SPN | FSTS | ACC | |
| S40 | Pan et al. (2010)† | 0.05/0.07 | 332 | China/Multi | ~2004–08 | III | L | SPN | FSTS | ACC | |
| S41 | Nielsen (2010)† | 0.09 | 165 | Denmark | ~2003–08 | I | L | SPN | FSTS | ACC | Danish firms |
| S42 | Chiao & Yang (2011) | −0.022 | 3,194 | Taiwan | ~2004–09 | I | L | SPN | FSTS | ACC | Large sample |
| S43 | Endo & Ozaki (2011) | −0.054 | 316 | Japan | ~2004–09 | I | L | SPN | FSTS | ACC | Japanese firms |
| S44 | Lin et al. (2011)† | −0.10 | 179 | Taiwan | ~2005–09 | I | L | SPN | FSTS | ACC | |
| S45 | Zhang & Toppinen (2011)† | 0.25/0.31 | 50 | China | ~2005–09 | III | L | SPN | EXP | ACC | Forestry sector |
| S46 | Assaf et al. (2012) | −0.29 | 43 | Multi/Hotels | ~2005–10 | MX | L | SPN | FSTS | ACC | Hotel industry |
| S47 | Almodóvar (2012) | 0.018 | 1,067 | Spain | ~2005–10 | II | L | SPN | EXP | ACC | Spanish mfg |
| S48 | Chang et al. (2012)† | 0.18 | 335 | Taiwan | ~2006–10 | I | L | SPN | FSTS | ACC | |
| S49 | Chen & Tan (2012)† | −0.011/0.171/0.24 | 887 | China | ~2006–10 | III | L | SPN | EXP | ACC | 3 effects |
| S50 | Li et al. (2012)† | 0.135 | 278 | China | ~2006–10 | III | L | SPN | GEO | ACC | |
| S51 | Pan & Tsai (2012)† | 0.05/0.07 | 281 | Taiwan | ~2006–10 | I | L | SPN | FSTS | ACC | Family firms |
| S52 | Polat & Mutlu (2012) | 0.266 | 103 | Turkey | ~2006–10 | III | L | SPN | EXP | ACC | Turkish firms |
| S53 | Tsao & Chen (2012) | 0.096/0.122 | 790 | Taiwan | ~2006–10 | I | L | SPN | FSTS | ACC | Family firm 2 eff |
| S54 | Fernhaber (2013) | −0.16/0.02 | 253 | USA | ~2005–10 | I | L | SPN | COMP | ACC | New ventures 2 eff |
| S55 | Hsu et al. (2013)† | 0.149/−0.247 | 187 | Taiwan | ~2006–11 | I | M | SPN | FSTS | ACC | |
| S56 | Lee (2013) | −0.03 to 0.15 | 814 | Korea | ~2006–11 | I | M | SPN | FSTS | ACC | 6 effects |
| S57 | Tsao & Lien (2013) | 0.033/0.068 | 776 | Taiwan | ~2007–11 | I | M | SPN | FSTS | ACC | Family firms 2 eff |
| S58 | Xiao et al. (2013)† | −0.034 | 114,398 | China | ~2004–08 | III | L | SPN | EXP | LAB | Large sample; WBES? |
| S59 | De Jong & van Houten (2014)† | 0.22 | 568 | Netherlands | ~2007–11 | I | M | SPN | GEO | ACC | |
| S60 | Hilmersson (2014) | 0.04/0.16/0.27 | 180 | Sweden/SME | ~2008–12 | I | M | SPN | COMP | ACC | 3 effects |
| S61 | Graves & Shan (2014) | −0.07 | 4,217 | Australia | ~2007–12 | I | M | SPN | FSTS | ACC | Large sample |
| S62 | Lee et al. (2014) | 0.383 | 279 | Korea SME | ~2008–12 | I | M | SPN | EXP | ACC | Korean SMEs |
| S63 | Zhou & Wu (2014) | 0.15 | 376 | China | ~2007–12 | III | L | SPN | EXP | ACC | China tech |
| S64 | Nguyen & Rugman (2015)† | 0.119–0.316 | 101 | Vietnam | ~2009–13 | III | L | SPN | FSTS | ACC | 4 effects |
| S65 | Ren et al. (2015)† | 0.09 | 176 | China | ~2009–13 | III | L | SPN | EXP | ACC | |
| S66 | Chen et al. (2015)† | −0.038 | 118 | Taiwan | ~2009–13 | I | M | SPN | FSTS | ACC | |
| S67 | Da Huo & Hung (2015)† | 0.01 | 316 | Taiwan | ~2009–13 | I | M | SPN | FSTS | ACC | |
| S68 | Benito-Osorio et al. (2015) | −0.09 | 2,748 | Spain | ~2007–12 | II | L | SPN | EXP | ACC | Spanish mfg large |
| S69 | Altaf & Shah (2016) | 0.08 | 180 | Pakistan | ~2009–14 | FR | L | SPN | EXP | ACC | Pakistan firms |
| S70 | Assaf et al. (2016) | 0.009 | 68 | Multi/Hotels | ~2009–14 | MX | L | SPN | FSTS | ACC | Hotels replication |
| S71 | Berry & Kaul (2016) | 0.04 | 2,023 | Multi | ~2005–12 | MX | M | SPN | FSTS | MIX | Replication study |
| S72 | Brida et al. (2016) | −0.032 | 82 | Italy | ~2009–14 | II | L | SPN | FSTS | ACC | Italy hotels |
| S73 | Cantele et al. (2016) | 0.04 | 1,231 | Italy | ~2009–14 | II | L | SPN | EXP | ACC | Italian SMEs |
| S74 | Miller et al. (2016) | −0.056 to −0.071 | 2,692 | Multi | ~2005–13 | MX | M | SPN | COMP | MIX | 3 effects |
| S75 | Mohr & Batsakis (2016) | 0.03/0.05 | 110 | Multi | ~2008–14 | MX | M | SPN | FSTS | ACC | Internation speed |
| S76 | Upadhyayula et al. (2016) | 0.354 | 98 | India | ~2009–14 | III | L | SPN | EXP | ACC | India board |
| S77 | Borda et al. (2017) | 0.04 | 103 | Latin America | ~2010–15 | III | L | SPN | FSTS | ACC | Latin Am. |
| S78 | Buckley & Tian (2017)† | −0.031 | 221 | China | ~2010–15 | III | L | SPN | FSTS | ACC | China MNEs |
| S79 | Ganvir & Dwivedi (2017) | 0.018–0.073 | 411 | India | ~2010–15 | III | L | SPN | EXP | ACC | India 3 effects |
| S80 | Jin et al. (2017)† | −0.02/−0.03 | 401 | China | ~2010–15 | III | L | SPN | EXP | ACC | |
| S81 | Nosi et al. (2017) | 0.305 | 169 | Italy SME | ~2010–15 | II | L | SPN | EXP | ACC | Niche exporters |
| S82 | Purkayastha et al. (2017) | 0.029 | 185 | India | ~2010–15 | III | L | SPN | FSTS | ACC | India conglomerates |
| S83 | Abdi & Aulakh (2018) | 0.09 | 2,620 | Multi/Emg | ~2010–15 | MX | M | SPN | FSTS | ACC | JIBS emerging mkt |
| S84 | Booltink & Saka-Helmhout (2018) | −0.048 | 947 | Multi | ~2010–15 | MX | M | SPN | OTH | ACC | R&D mod. |
| S85 | Cho & Lee (2018) | −0.029 | 232 | Korea | ~2010–15 | I | H | SPN | FSTS | ACC | Family firms Korea; cDAI=H (Korea advanced digital, post-2010; corrected from M) |
| S86 | Pouresmaeili et al. (2018) | 0.69 | 226 | Iran | ~2011–16 | FR | L | SPN | EXP | ACC | Iran SMEs high r |
| S87 | Hojnik et al. (2018) | −0.14 to 0.21 | 147–387 | Slovenia | ~2010–15 | I | M | SPN | EXP | ACC | Slovenia; 7 eff |
| S88 | Thi Ngoc Huynh et al. (2018)† | −0.051 | 12,704 | Vietnam | ~2009–15 | III | L | SPN | EXP | LAB | WBES-based |
| S89 | Velez-Calle et al. (2018) | −0.14/0.05 | 147 | Latin America | ~2011–16 | III | L | SPN | FSTS | ACC | Latin Am. MNEs |
| S90 | Zhou (2018) | −0.028 | 535 | China | ~2011–16 | III | L | SPN | EXP | ACC | China listed |
| S91 | Sun et al. (2018)† | −0.006 | 1,220 | Multi/China | ~2011–16 | III | L | SPN | FSTS | ACC | |
| S92 | Feng et al. (2019)† | 0.029 | 170 | China | ~2012–17 | III | L | FOL | EXP | ACC | |
| S93 | Juniati et al. (2019) | 0.37 | 300 | Indonesia | ~2012–17 | III | L | FOL | EXP | ACC | Indonesia firms |
| S94 | Lee et al. (2019) | −0.015/−0.09 | 91 | Korea | ~2013–17 | I | M | FOL | FSTS | ACC | 2 effects |
| S95 | Meyer et al. (2019)† | 0.52 | 18 | Multi | ~2013–17 | MX | M | FOL | COMP | ACC | Small n; caution |
| S96 | Tashman et al. (2019) | 0.41 | 17 | USA/CSR | ~2012–17 | I | H | FOL | FSTS | ACC | CSR mod.; small n |
| S97 | Woo et al. (2019)† | 0.19/0.19 | 107 | Korea | ~2013–17 | I | H | FOL | FSTS | ACC | |
| S98 | Kim et al. (2020) | 0.013/−0.29 | 236 | Korea | ~2013–18 | I | H | FOL | FSTS | ACC | 2 effects |
| S99 | Phan et al. (2020)† | −0.011/−0.152 | 114/285 | Vietnam | ~2013–18 | III | L | FOL | EXP | LAB | WBES-based |
| S100 | Tu et al. (2020)† | −0.021 | 263 | China/Taiwan | ~2013–18 | III | L | FOL | EXP | ACC | |
| S101 | Freixanet & Rialp (2021)† | 0.066/0.087 | 1,064 | Spain | ~2013–18 | II | M | FOL | EXP | ACC | Spain SMEs |
| S102 | Kongkaew et al. (2021) | 0.059 | 80 | Thailand | ~2014–18 | III | L | FOL | EXP | ACC | Thailand SMEs |
| S103 | Nath et al. (2021)† | 0.196 | 73 | India/Multi | ~2014–18 | III | L | FOL | EXP | ACC | |
| S104 | Tu et al. (2021)† | −0.093 | 131 | Vietnam | ~2014–19 | III | L | FOL | FSTS | ACC | |
| S105 | Tu (2021)† | −0.056 | 189 | Vietnam | ~2013–18 | III | L | FOL | EXP | LAB | WBES-based |
| S106 | Tu & Anh (2021)† | −0.051 | 90 | Vietnam | ~2014–18 | III | L | FOL | EXP | ACC | |
| S107 | Song & Lee (2021)† | 0.05/0.14 | 44/70 | Korea | ~2014–19 | I | H | FOL | FSTS | ACC | |
| S108 | Wei & Lin (2021)† | 0.04 | 2,175 | China | ~2014–19 | III | L | FOL | EXP | ACC | Large sample |
| S109 | Purkayastha & Gupta (2022) | 0.04 | 419 | India | ~2015–20 | III | L | FOL | FSTS | ACC | India family groups |
| S110 | Putri & Pan (2022) | 0.003/0.012 | 407 | Indonesia | ~2015–20 | III | L | FOL | EXP | ACC | Indonesia mfg |

---

### Nhóm B: Studies Mới từ Backward Citation Scan + 2022–2026 (NEW)

> **Nguồn:** Backward citation scan của 6 meta lớn (Bausch & Krist 2007; Kirca et al. 2012;
> Yang & Driffield 2012; Marano et al. 2016; Wu et al. 2022; Arte & Larimo 2022) và
> literature search 2022–2026. Tổng: **25 studies mới** → Pool tổng cộng **~135 studies**.

| ID | Author-Year | r | n | Country | Period | ICRV | cDAI | DPL | DOI | FP | Notes |
|----|-------------|---|---|---------|--------|------|------|-----|-----|----|-------|
| S111 | Daniels & Bracker (1989) **NEW** | 0.05 | 32 | USA | ~1980–86 | I | L | PRE | FSTS | ACC | MIR; profit vs. intl |
| S112 | Geringer, Beamish & daCosta (1989) **NEW** | 0.07–0.22 | 100 | USA/Canada | ~1980–86 | I | L | PRE | GEO | ACC | SMJ; diversification |
| S113 | Kim, Hwang & Burgers (1993) **NEW** | −0.05 to 0.12 | 85 | USA | ~1984–89 | I | L | PRE | COMP | ACC | SMJ; global strategy |
| S114 | Sullivan (1994) **NEW** | 0.09 | 74 | USA | ~1986–91 | I | L | PRE | COMP | ACC | JIBS; DOI measurement |
| S115 | Ramaswamy (1995) **NEW** | 0.07 | 180 | USA | ~1985–91 | I | L | PRE | GEO | ACC | JIBS; multinationality |
| S116 | Delios & Beamish (1999) **NEW** | 0.09 | 399 | Japan | ~1986–97 | I | L | PRE | GEO | ACC | SMJ; Japanese firms |
| S117 | Lu & Beamish (2001) **NEW** | 0.09 | 1,489 | Japan SMEs | ~1986–97 | I | L | PRE | GEO | ACC | SMJ; Japanese SMEs |
| S118 | Contractor, Kundu & Hsu (2003) **NEW** | −0.08 to 0.22 | 103 | Multi/Service | ~1993–99 | I | L | PRE | FSTS | ACC | JIBS; S-curve; 3 samples |
| S119 | Bloodgood, Sapienza & Almeida (1996) **NEW** | 0.05 | 61 | USA | ~1988–93 | I | L | PRE | EXP | ACC | EME; new ventures |
| S120 | Pangarkar & Yuan (2009) **NEW** | 0.12 | 150 | Singapore/Asia | ~2003–07 | I | L | PRE | FSTS | ACC | JIM; Singapore/HK |
| S121 | Gaur, Kumar & Singh (2014) **NEW** | 0.09 | 240 | India | ~2007–12 | III | L | SPN | GEO | ACC | JWB; India institutions |
| S122 | Luo & Tung (2015)* **NEW** | 0.11 | 285 | China | ~2008–13 | III | L | SPN | GEO | ACC | China EMNEs |
| S123 | García-García, García-Canal & Guillén (2017) **NEW** | 0.15 | 2,256 | Spain/Multi | ~2005–14 | II | M | SPN | GEO | ACC | BJM; rapid intl |
| S124 | Klier, Schwens, Zapkau & Dikova (2017)* **NEW** | 0.08 | ~350 | Multi | ~2005–14 | MX | M | SPN | COMP | ACC | JMS; resources meta-reg |
| S125 | Arte & Larimo (2022) **NEW** | 0.04–0.19 | ~1,200 | Multi/Europe | ~2005–18 | MX | M | FOL | COMP | MIX | JBR; product div mod |
| S126 | Schmuck, Lagerström & Sallis (2022) **NEW** | 0.06 | ~500 | Sweden/Multi | ~2010–18 | I | H | FOL | FSTS | ACC | MIR; reverse causality |
| S127 | Bhandari, Zámborský, Ranta & Salo (2023) **NEW** | 0.07–0.13 | ~1,500 | Multi | ~2014–21 | MX | H | FOL | COMP | MIX | IBR; digital × intl |
| S128 | Kafouros et al. (2023) **NEW** | 0.09 | ~800 | Multi | ~2014–21 | MX | H | FOL | GEO | ACC | GSJ; knowledge resources |
| S129 | Freixanet, Renart & Segarra-Blasco (2022) **NEW** | 0.08/0.11 | 892 | Spain | ~2010–17 | II | M | FOL | EXP | ACC | IBR; SME capabilities |
| S130 | Shin, Kim & Seol (2022) **NEW** | 0.12 | 314 | Korea | ~2014–19 | I | H | FOL | FSTS | ACC | IBR; Korea conglomerates |
| S131 | Dobbs & Hamilton (2007)* **NEW** | 0.03 | 220 | USA/Multi | ~1998–03 | I | L | PRE | FSTS | ACC | IJME; SME performance |
| S132 | Almodovar & Rugman (2014)* **NEW** | 0.09 | 342 | Spain/Multi | ~2004–11 | II | M | SPN | FSTS | ACC | MIR; regional strategy |
| S133 | Lin, Liu & Cheng (2011)* **NEW** | 0.07 | 246 | Taiwan | ~2004–09 | I | L | SPN | FSTS | ACC | IJBM; Taiwan |
| S134 | Pinheiro-Alves (2011)* **NEW** | 0.11 | 186 | Portugal | ~2004–09 | I | L | SPN | EXP | ACC | IJBM; Portuguese firms |
| S135 | Guo et al. (2020) **NEW** | 0.08 | 1,850 | China | ~2013–18 | III | L | FOL | EXP | ACC | IMR; Chinese exporter |
| S136 | Hitt, Hoskisson & Kim (1997) **NEW** | 0.14 | 295 | USA | ~1980–89 | I | L | PRE | COMP | ACC | AMJ; innovation + intl div |
| S137 | Gomes & Ramaswamy (1999) **NEW** | 0.08/−0.12 | 311 | Multi | ~1985–95 | I | L | PRE | FSTS | ACC | JIBS; curvilinear test |
| S138 | Tallman & Li (1996) **NEW** | 0.12 | 192 | USA | ~1980–88 | I | L | PRE | GEO | ACC | AMJ; international + product div |
| S139 | Aulakh, Kotabe & Teegen (2000) **NEW** | 0.09/0.17 | 163 | EME | ~1990–96 | III | L | PRE | EXP | ACC | AMJ; Brazil/Chile/Mexico |
| S140 | Kotabe, Srinivasan & Aulakh (2002) **NEW** | 0.07 | 167 | USA | ~1985–93 | I | L | PRE | GEO | ACC | JIBS; R&D moderates |
| S141 | Denis, Denis & Yost (2002) **NEW** | −0.06 | 3,659 | USA | ~1984–97 | I | L | PRE | GEO | MKT | JF; global vs industrial div |
| S142 | Gomez-Mejia & Palich (1997) **NEW** | −0.08 | 356 | Multi | ~1985–94 | I | L | PRE | COMP | ACC | JIBS; cultural distance negative |
| S143 | Chang & Wang (2007) **NEW** | 0.05/0.18 | 150 | Taiwan | ~1996–03 | I | L | PRE | FSTS | ACC | JWB; product × intl div |
| S144 | Pangarkar (2008) **NEW** | 0.08 | 150 | Singapore | ~2001–04 | I | M | SPN | GEO | ACC | JWB; SME Singapore |
| S145 | Zahra, Ireland & Hitt (2000) **NEW** | 0.22/0.31 | 321 | USA | ~1991–94 | I | L | PRE | GEO | ACC | AMJ; new ventures INV |
| S146 | Oh & Contractor (2012) **NEW** | −0.04/0.16 | 144 | Global | ~2003–07 | I | M | FOL | FSTS | ACC | JIBS; territorial + product mod |
| S147 | Qian, Li, Li & Qian (2008) **NEW** | 0.11 | 1,462 | USA | ~1985–02 | I | M | SPN | GEO | ACC | JIBS; regional diversification |
| S148 | Elango & Pattnaik (2007) **NEW** | 0.09 | 794 | India | ~1998–02 | III | L | PRE | FSTS | ACC | JIBS; networks → capabilities |
| S149 | Filatotchev & Piesse (2009) **NEW** | 0.15 | 254 | Europe | ~1996–03 | I | M | SPN | FSTS | MKT | JIBS; IPO firms R&D |
| S150 | Geringer, Tallman & Olsen (2000) **NEW** | 0.07/−0.08 | 172 | Japan | ~1980–89 | I | L | PRE | FSTS | ACC | SMJ; Japan MNE div |
| S151 | Michel & Shaked (1986) **NEW** | 0.08 | 60 | USA | ~1975–83 | I | L | PRE | GEO | ACC | JIBS; MNC vs domestic |
| S152 | Morck & Yeung (1991) **NEW** | 0.04 | 1,644 | USA | ~1978–88 | I | L | PRE | GEO | MKT | JB; Tobin's Q intangibles |
| S153 | Wan & Hoskisson (2003) **NEW** | 0.09/0.13 | 244 | Multi | ~1988–97 | I | L | PRE | GEO | ACC | AMJ; home country institutions |
| S154 | Yiu, Lau & Bruton (2007) **NEW** | 0.14 | 83 | China | ~1998–03 | III | L | PRE | GEO | MIX | JIBS; EMNEs capabilities |
| S155 | Luo, Zhao & Du (2005) **NEW** | 0.22 | 207 | China | ~1998–03 | III | L | PRE | FSTS | ACC | IMR; e-commerce speed |
| S156 | Bobillo, López-Iturriaga & Tejerina-Gaite (2010) **NEW** | 0.06/0.09 | 1,096 | Europe | ~1993–03 | I | M | SPN | FSTS | ACC | IBR; competitive advantages |
| S157 | Boehe & Cruz (2010) **NEW** | 0.18 | 168 | Brazil | ~2000–06 | III | L | SPN | EXP | ACC | JBE; CSR differentiation |
| S158 | Singh & Gaur (2009) **NEW** | 0.11 | 1,247 | Asia | ~2000–06 | III | L | SPN | GEO | MIX | CGR; BG affiliation India/China |
| S159 | Fernández-Olmos & Díez-Vial (2015) **NEW** | 0.12/0.19 | 261 | Spain | ~2004–11 | I | H | FOL | FSTS | ACC | EMJ; Iberian ham sector |
| S160 | Lu & Beamish (2006) **NEW** | −0.09/0.09 | 1,489 | Japan SMEs | ~1986–99 | I | L | PRE | FSTS | ACC | JIE; SME growth vs profitability |
| S161 | Contractor, Kumar & Kundu (2007) **NEW** | −0.33/0.44 | 103 | India | ~1998–02 | III | L | PRE | FSTS | ACC | JWB; EME S-curve services |
| S162 | Oh & Sohl (2017) **NEW** | 0.08 | 139 | USA | ~2003–10 | I | H | FOL | FSTS | ACC | MIR; turbulence moderates |
| S163 | Ogasavara & Hoshino (2007) **NEW** | 0.09 | 88 | Japan | ~1995–02 | I | L | PRE | FDI | ACC | IBR; Japan subs in Brazil |
| S164 | Gao, Murray, Kotabe & Lu (2010) **NEW** | 0.13 | 105 | China | ~2000–05 | III | M | SPN | FSTS | ACC | JIBS; strategy tripod China |
| S165 | Doukas & Kan (2006) **NEW** | −0.07 | 816 | USA | ~1988–01 | I | L | PRE | GEO | MKT | JMFM; global diversification discount |
| S166 | Castellacci (2015) **NEW** | 0.10/0.16 | 3,498 | LatAm | ~2006–11 | III | M | FOL | EXP | LAB | IBR; institutional voids |
| S167 | Reuber & Fischer (1997) **NEW** | 0.14/0.28 | 49 | Canada | ~1989–93 | I | L | PRE | GEO | ACC | JIBS; management intl exp SME |
| S168 | Zhou, Wu & Luo (2007) **NEW** | 0.19 | 195 | China | ~2000–04 | III | L | PRE | FSTS | ACC | JIBS; born-global social network |
| S169 | Isobe, Makino & Montgomery (2000) **NEW** | 0.09/0.15 | 164 | Japan/China | ~1989–96 | I | L | PRE | FDI | ACC | AMJ; JV resource commitment |
| S170 | Shan & Song (1997) **NEW** | 0.22 | 176 | USA | ~1985–91 | I | L | PRE | GEO | MKT | JIBS; biotech FDI technology |
| S171 | Buckley, Dunning & Pearce (1978) **NEW** | 0.08 | 370 | Multi | ~1962–72 | I | L | PRE | GEO | ACC | WA; earliest study in pool |
| S172 | Oesterle, Richta & Fisch (2013) **NEW** | 0.06 | 312 | Germany | ~2000–08 | I | M | SPN | GEO | ACC | IBR; ownership structure |
| S173 | Nguyen, Almodóvar & Martínez-Noya (2018) **NEW** | 0.13/0.21 | 187 | Multi | ~2005–12 | I | H | FOL | FSTS | ACC | IBR; intra-regional sales |
| S174 | Ogasavara, Hoshino & Alberton (2016) **NEW** | 0.11 | 148 | Brazil | ~2006–12 | III | M | FOL | GEO | ACC | MBR; intl experience Brazil |
| S175 | Jo & Roth (2015) **NEW** | 0.17 | 198 | Korea | ~2005–12 | I | M | FOL | FSTS | MIX | JIM; tech capability Korea |
| S176 | Khattak & Shah (2022) **NEW** | 0.07 | 168 | Pakistan | ~2014–19 | III | L | FOL | FSTS | ACC | IJOEM; org learning mediates |
| S177 | Lee & Yoon (2022) **NEW** | 0.11 | 312 | Korea | ~2013–18 | I | H | FOL | GEO | ACC | APJM; env uncertainty mod |
| S178 | Lin & Liu (2022) **NEW** | 0.09/−0.06 | 452 | Multi | ~2010–17 | MX | M | FOL | GEO | ACC | JIM; institutional env mod |
| S179 | Chen, Zhang & Li (2022) **NEW** | 0.10 | 534 | China | ~2014–19 | III | H | FOL | FSTS | ACC | EMFT; absorptive capacity mod |
| S180 | Wang & Xiang (2022) **NEW** | 0.11 | 385 | China SME | ~2015–20 | III | H | FOL | FSTS | ACC | IBR; sustainability orientation |
| S181 | Nguyen & Dinh (2022) **NEW** | 0.07 | 428 | Vietnam WBES | ~2015–16 | III | M | FOL | EXP | ACC | JABES; WBES wave |
| S182 | Vo & Nguyen (2021) **NEW** | 0.06 | 212 | Vietnam non-state | ~2015–19 | III | M | FOL | EXP | ACC | Cogent B&M; non-state firms |
| S183 | Kim & Kim (2023) **NEW** | 0.12 | 276 | Korea conglomerate | ~2015–20 | I | H | FOL | FSTS | MIX | JWB; digital transformation mod |
| S184 | Borkakoti & Dua (2023) **NEW** | 0.09 | 421 | India mfg | ~2015–20 | III | M | FOL | FSTS | ACC | JQE; manufacturing sector |
| S185 | Li & Li (2023) **NEW** | 0.13 | 1243 | China digital | ~2016–21 | III | H | FOL | FSTS | MKT | PBFJ; digital economy listed |
| S186 | Torres, Kunc & O'Shannassy (2022) **NEW** | 0.13 | 198 | Multi SME | ~2014–20 | MX | H | FOL | COMP | ACC | IBR; dynamic capability SME |
| S187 | Cho & Lee (2023) **NEW** | 0.14 | 204 | Korea SME digital | ~2016–21 | I | H | FOL | FSTS | ACC | APJM; digital capability SME |
| S188 | Do & Phan (2025) **AUTHOR** | −0.045 | 380 | India mfg | ~2013–18 | III | M | FOL | FSTS | ACC | IntechOpen; India WBES; FGLS; ROS; manager moderator; r confirmed Table 3 |
| S189 | Do & Phan (2026) **AUTHOR** | +0.07 (est.) | 4290 | China mfg SME | ~2012–24 | III | H | FOL | FSTS | LAB | JFAR; WBES China 2012+2024; inverted-U TP=47.8%; β₁=+1.704 |
| S190 | Phan, Ninh & Do (2021) **AUTHOR** | −0.04 (est.) | 263 | Turkey mfg | ~2013–16 | II | M | SPN | FSTS | ACC | IntechOpen; WBES Turkey; FGLS; manager experience moderator |
| S191 | Phan et al. (2021) **AUTHOR** | +0.05 (est.) | 131 | Poland mfg-svc | ~2013–16 | I | M | SPN | FSTS | ACC | IntechOpen; WBES Poland; inverted-U; female manager + fin.obstacles mods |
| S192 | Tu & Huynh (2021) **AUTHOR** | +0.03 (est.) | 90 | Ecuador mfg | 2003–17 | MX | L | SPN | FSTS | ACC | RWE 12(1); panel; inverse S-curve; LatAm context |
| S193 | García-Sánchez & Rama (2024) **NEW** | +0.09 (est.) | 267 | Spain mfg | 2010–17 | II | H | SPN | FSTS | ACC | EBR 14(4); Bayesian; heterogeneous firm-level effects |
| S194 | Godbole (2024) **NEW** | +0.08 (est.) | ~120 | India listed family | ~2015–22 | III | M | FOL | COMP | MIX | BSD 7(3); NIFTY500 family firms; GMM; financial+innovation |
| S195 | Barłożewski & Trąpczyński (2021a) | +0.06 (est.) | 200 | Poland | ~2014–19 | I | M | FOL | FSTS | ACC | EBER 9; full-sample n=200; see S236 for exporter-subsample (n=97, confirmed r) |
| S196 | Barłożewski & Trąpczyński (2021b) | +0.04 (est.) | 200 | Poland | ~2014–19 | I | M | FOL | FSTS | ACC | OC 12; full-sample n=200; see S237 for larger-sample (n=304, confirmed r) |
| S197 | Calabrese & Manello (2018) | +0.08 (est.) | 300 | Italy | ~2005–15 | II | M | SPN | FSTS | ACC | JPM; Italy policy evidence |
| S198 | Cao et al. (2022) | +0.07 (est.) | 400 | China | ~2010–20 | III | H | FOL | FSTS | ACC | PLoS ONE; social networks China |
| S199 | Carr et al. (2010) | +0.05 (est.) | 150 | Multi | ~2000–07 | MX | L | PRE | FSTS | ACC | SEJ; firm age at intl |
| S200 | Chen & Hsu (2010) | +0.09 (est.) | 200 | Taiwan | ~2001–07 | I | L | PRE | FSTS | MKT | IMM; resource allocation Taiwan |
| S201 | Cuervo-Cazurra et al. (2017) | +0.05 (est.) | 500 | Multi | ~2006–14 | MX | M | SPN | FSTS | ACC | JWB; uncertainty management |
| S202 | Da Cunha et al. (2023) | +0.06 (est.) | 250 | Multi-LatAm | ~2010–20 | III | M | FOL | FSTS | ACC | IJOEM; formal institutions |
| S203 | Debicki et al. (2020) | +0.05 (est.) | 300 | Multi | ~2005–15 | MX | M | SPN | FSTS | ACC | CCSM; family firm I→P |
| S204 | Dikova & Veselova (2020) | −0.04 (est.) | 200 | Russia | ~2008–16 | III | M | SPN | COMP | ACC | MOR; Russia contingency |
| S205 | Elango (2012) | +0.10 (est.) | 250 | USA/Multi | ~2000–08 | I | M | PRE | COMP | MKT | TIBR; tech-intensive industry |
| S206 | Espinosa-Méndez & Jara (2021) | +0.04 (est.) | 150 | Chile | ~2009–18 | III | M | FOL | GEO | ACC | SJFC; Chile family firm |
| S207 | Fu (2024) | +0.09 (est.) | 800 | China | ~2012–22 | III | H | FOL | FSTS | MKT | FRL; R&D investment China |
| S208 | Khatua et al. (2024) | +0.07 (est.) | 120 | India | ~2015–22 | III | H | FOL | FSTS | ACC | JIE; INVs India |
| S209 | Lin et al. (2011) | +0.06 (est.) | 180 | Taiwan | ~2001–08 | I | L | PRE | FSTS | MKT | JIM; firm behavior moderator |
| S210 | Manotas & Gonzalez-Perez (2020) | +0.05 (est.) | 150 | Multi-LatAm | ~2010–17 | III | L | SPN | EXP | ACC | CR; LatAm SMEs |
| S211 | Olmos & Díez-Vial (2015) | +0.07 (est.) | 200 | Spain | ~2004–10 | II | M | SPN | EXP | ACC | EJM; SME intl paths Spain |
| S212 | Phan, Tran & Lu (2020) | +0.03 (est.) | 90 | Cameroon | ~2013–18 | Frontier | L | SPN | FSTS | ACC | DSL; W-shaped Cameroon |
| S213 | Purkayastha et al. (2024) | +0.07 (est.) | 200 | India | ~2014–22 | III | H | FOL | COMP | ACC | JIM; resource management India |
| S214 | Purkayastha et al. (2021) | +0.06 (est.) | 185 | India | ~2010–18 | III | M | FOL | FSTS | ACC | JWB; EMNEs learning India |
| S215 | Rienda & Andreu (2021) | +0.04 (est.) | 200 | Spain | ~2005–18 | II | M | SPN | FSTS | ACC | EJFB; family firms Spain |
| S216 | Schmuck et al. (2022a) | +0.08 (est.) | 400 | Multi | ~2010–19 | MX | H | FOL | COMP | MKT | MIR; reverse P→M direction |
| S217 | Singla & George (2013) | +0.08 (est.) | 200 | India | ~2004–09 | III | L | SPN | FSTS | ACC | JBR; India contextual analysis |
| S218 | Sun et al. (2019) | +0.09 (est.) | 600 | USA | ~2003–15 | I | H | SPN | FSTS | MKT | JBR; longitudinal marketing cap |
| S219 | Tongurai & Vithessonthi (2022) | +0.06 (est.) | 350 | Thailand | ~2010–19 | III | H | FOL | FSTS | ACC | GFJ; Thailand learning |
| S220 | Tsionas & Tzeremes (2021) | +0.10 (est.) | 500 | Multi | ~2008–18 | MX | H | FOL | COMP | LAB | BJM; large MNEs productivity |
| S221 | Vithessonthi & Racela (2016) | +0.05 (est.) | 400 | Thailand | ~2000–13 | III | M | SPN | FSTS | ACC | JMFM; short/long-run Thailand |
| S222 | Wang et al. (2020) | +0.07 (est.) | 150 | China construction | ~2005–17 | III | M | SPN | COMP | ACC | JMgmtEng; ENR-listed Chinese |
| S223 | Wei & Lin (2021) | +0.05 (est.) | 800 | Taiwan | 1992–17 | I | M | SPN | FSTS | MKT | MPE; long panel Taiwan |
| S224 | Xiao et al. (2013) | +0.08 (est.) | 250 | China | ~2004–09 | III | L | SPN | FSTS | ACC | JIM; China governance |
| S225 | Xiong et al. (2024) | +0.09 (est.) | 600 | China | ~2010–20 | III | H | FOL | COMP | MKT | FRL; intl speed China |
| S226 | Zeng et al. (2009) | +0.06 (est.) | 200 | China | ~2003–07 | III | L | PRE | EXP | ACC | MD; China business factors |
| S227 | Ahsan & Sinha (2022) | +0.07 (est.) | 150 | India | ~2010–19 | III | M | FOL | COMP | ACC | CCSM; knowledge-intensive India |
| S228 | Ruzzier & Ruzzier (2014) | +0.06 (est.) | 180 | Slovenia | ~2005–10 | II | M | SPN | FSTS | ACC | JBEM; Slovenian SMEs |
| S229 | Azman et al. (2022) | +0.09 (est.) | 200 | Malaysia | ~2010–20 | III | H | FOL | COMP | LAB | JMgmtEng; Malaysia construction |
| S230 | Bhandari et al. (2023) | +0.10 (est.) | 300 | Multi | ~2014–22 | MX | H | FOL | FSTS | MKT | IBR; digitalization OLI |
| S231 | Hosseini et al. (2018) | +0.06 (est.) | 150 | Sweden | ~2005–15 | II | M | SPN | EXP | ACC | FPE; Swedish wood SMEs |
| S232 | Huang & Marciano (2020) | +0.05 (est.) | 200 | Multi | ~2010–18 | MX | M | SPN | FSTS | ACC | INSYMA conf.; Indonesia/China |
| S233 | Kayaci (2022) | +0.06 (est.) | 200 | Turkey | ~2015–20 | II | H | FOL | COMP | ACC | CumJourn; BIST-listed Turkey |
| S234 | Yip et al. (2000) | +0.06 (est.) | 150 | Multi | ~1992–98 | MX | L | PRE | COMP | ACC | JIM; newly internationalizing firms |
| S235 | Freixanet & Rialp (2021) GSJ | +0.08 (est.) | 1,500 | Spain | ~2008–16 | II | M | FOL | EXP | MIX | GSJ; I→P with innovation mediator (distinct from S101 EMJ) |
| S236 | Barłożewski & Trąpczyński (2021a) | −0.10 | 97 | Poland | ~2014–19 | MX | M | SPN | FSTS | ACC | EBER 9; exporter subsample n=97; r confirmed (see S195 for full-sample n=200 est.) |
| S237 | Barłożewski & Trąpczyński (2021b) | −0.04 | 304 | Poland | ~2014–19 | MX | M | FOL | FSTS | ACC | OC 12; larger-sample n=304; r confirmed (see S196 for n=200 est.) |
| S238 | Srividhya et al. (2024) | +0.13 | 992 | India | ~2005–21 | III | M | SPN | FSTS | ACC | WoS-arm S0129; JEI 2024 v39(2); DOI-ROA corr experienced BGs; n≈992 firm-yr (72 firms, PROWESS 2005–2021); doi:10.11130/jei.2024033 |

---

## 5. Tóm tắt Phân phối Moderator (k = 238 studies S01–S238; K = 288 effects in MARA)

> *Cập nhật 16/05/2026: k=237. S236/S237 are distinct subsample analyses from same papers as S195/S196 (different n, different effect). Table rows S01–S237 documented below. Các bảng phân phối dưới đây là ước tính từ coding thủ công; xem `p6/results/forest_data.csv` để có số liệu chính xác theo effect.*
>
> *Cập nhật 19/05/2026: S238 (Srividhya et al. 2024 — India BG, FSTS→ROA, r=0.13, n=992, ICRV=III, cDAI=M, DPL=SPN) đã được thêm vào bảng coded ở trên (trước đây chỉ nằm trong `forest_data.csv` như effect E288 từ WoS arm search). Coded database hiện cover đầy đủ S01–S238 (k=238); `p6_parse_database.py` nay sinh ra đúng K=288 rows / k=238 unique study_ids, khớp với `forest_data.csv`.*
>
> **Ghi chú về chênh lệch K: MetaEssentials vs forest_data (16/05/2026)**
>
> MetaEssentials 1.5 (ICBEF 2025 baseline, k=113) báo cáo **K=200 effect sizes**, trong khi `forest_data.csv` chỉ có **K=146 effects cho cùng k=113 studies** (S01–S113). Chênh lệch 54 effects này là có chủ đích và không phải lỗi:
>
> - **MetaEssentials** thu thập *tất cả* bivariate correlations trong correlation matrix của từng bài (kể cả các cặp DOI khác nhau với cùng FP, hoặc cùng biến đo bằng nhiều cách).
> - **forest_data.csv** chỉ giữ effects đại diện cho *tổ hợp (DOI type × FP type) độc lập* — một study có tối đa 1 effect mỗi tổ hợp; loại bỏ correlations giữa cùng biến nhưng đo theo cách khác (raw vs. adjusted, khác subsample cùng nghiên cứu).
> - Nguyên tắc này nhất quán với Cheung (2014) three-level MARA: "effects should represent independent comparisons; redundant correlations inflate K và bias kết quả aggregation."
>
> **Kết luận**: K=288 trong forest_data là số đúng cho three-level MARA (K=287 từ S01–S237 + K=1 từ S238 Srividhya et al. 2024). 54 effects không được đưa vào là *intentional exclusions*, không phải missing data.

### 5.1 Phân phối ICRV Regime

| Regime | k | % | Quốc gia chính |
|--------|---|---|----------------|
| I — Advanced | 91 | 44% | USA (30), Japan (12), Korea (17), Taiwan (14), Singapore (4), UK/EU (8), Poland (2) |
| II — Upper-middle | 25 | 11% | Italy (5), Spain (10), Turkey (2), Malaysia (1), Slovenia (1), Sweden (1), others (5) |
| III — Emerging | 80 | 34% | China (26), India (17), Vietnam (9), Indonesia (3), Brazil (5), LatAm (4), Russia (1), Thailand (2), Malaysia (1) |
| SIDS | 0 | 0% | *No studies yet — target from P8 backward scan* |
| Frontier | 3 | 1% | Pakistan (1), Iran (1), Cameroon (1) |
| Mixed | 36 | 15% | Multi-country (36) |
| **Tổng** | **237** | **100%** | |

> **Ghi chú SIDS**: Chưa tìm được studies đủ tiêu chuẩn với mẫu thuần SIDS Pacific. Phần
> backward scan tiếp theo cần tìm kiếm riêng cho Fiji, Solomon Islands, Vanuatu.

### 5.2 Phân phối cDAI Level

| cDAI | k | % | Diễn giải |
|------|---|---|-----------|
| High | 57 | 24% | Advanced economies post-2010 với strong digital infrastructure |
| Medium | 81 | 34% | Advanced pre-2010 or upper-middle post-2010 |
| Low | 97 | 41% | Emerging/Frontier contexts or pre-1998 data |
| **Tổng** | **237** | **100%** | |

### 5.3 Phân phối DPL Phase

| Phase | k | % | Data period |
|-------|---|---|-------------|
| Precede | 74 | 32% | Data ends ≤ 2008 |
| Span | 90 | 38% | Data 2005–2014 |
| Follow | 71 | 30% | Data starts ≥ 2013 |
| **Tổng** | **237** | **100%** | |

### 5.4 Phân phối DOI Measure Type

| DOI | k | % |
|-----|---|---|
| FSTS | 64 | 37% |
| Export (EXP) | 44 | 25% |
| Geographic scope (GEO) | 38 | 22% |
| Composite (COMP) | 20 | 11% |
| FDI intensity | 7 | 4% |
| Other | 2 | 1% |

### 5.5 Phân phối FP Measure Type

| FP | k | % |
|----|---|---|
| Accounting (ACC) | 145 | 83% |
| Mixed ACC+MKT | 16 | 9% |
| Labor productivity (LAB) | 9 | 5% |
| Market-based (MKT) | 5 | 3% |

---

## 6. Studies Cần Xác Minh Thêm (Flagged for Full-Text Check)

Các studies được đánh dấu `*` cần full-text access để xác nhận effect size và sample details
trước khi đưa vào analysis chính thức.

| ID | Author-Year | Vấn đề cần kiểm tra |
|----|-------------|---------------------|
| S95 | Meyer et al. (2019) | n=18 — quá nhỏ, xem xét loại khỏi main analysis |
| S96 | Tashman et al. (2019) | n=17 — quá nhỏ, xem xét loại khỏi main analysis |
| S86 | Pouresmaeili et al. (2018) | r=0.69 quá cao, kiểm tra outlier/coding error |
| S122 | Luo & Tung (2015) | Kiểm tra xem có effect size r hay chỉ có qualitative |
| S124 | Klier et al. (2017) | Meta-regression study — verify có primary effect size |
| S131 | Dobbs & Hamilton (2007) | Citation cần xác minh; journal tên đầy đủ |
| S132 | Almodovar & Rugman (2014) | Verify sample period |
| S133–S134 | Lin et al. (2011); Pinheiro-Alves (2011) | Ít được trích dẫn — verify đủ tiêu chuẩn inclusion |

> **Quy trình**: Nếu study bị loại, renumber lại từ S111+ và update bảng tóm tắt.
> Target: giữ ≥130 studies sau khi loại bỏ studies không đủ tiêu chuẩn.

---

## 7. Studies Đã Xét và Loại (Excluded Studies Log)

Ghi lại các studies được xem xét nhưng không đủ tiêu chuẩn để tránh double-checking.

| Author-Year | Lý do loại | Exclusion criterion |
|-------------|-----------|---------------------|
| Bausch & Krist (2007) | Meta-analysis — not primary study | Exclusion #1 |
| Kirca et al. (2012) | Meta-analysis — not primary study | Exclusion #1 |
| Yang & Driffield (2012) | Meta-analysis — not primary study | Exclusion #1 |
| Marano et al. (2016) | Meta-analysis — not primary study | Exclusion #1 |
| Wu et al. (2022) | Meta-analysis — not primary study | Exclusion #1 |
| Arte & Larimo (2022) | Meta-regression (được giữ lại S125 vì có primary effect sizes) | → INCLUDED |
| Luo & Tung (2007) | Conceptual/framework — no primary empirical data | Exclusion #1 |
| Klier et al. (2017) | Meta-regression — xem xét thêm (S124) | → PENDING |
| Banalieva & Dhanaraj (2019) | Theoretical paper | Exclusion #1 |
| Schmuck et al. (2022) | Primary empirical with r | → INCLUDED (S126) |
| Hitt et al. (2001)* | Not primarily I→P study (professional services HR) | Exclusion #1 |
| Sullivan (1994) measurement | Second sample in paper has r | → INCLUDED (S114) |
| Various PhD theses | Unpublished thesis | Exclusion #6 |
| Country-level FDI studies | Country-level not firm-level | Exclusion #4 |

---

## 8. Lộ trình Mở rộng Pool (Backward Citation Scan còn lại)

### 8.1 Nguồn chưa khai thác đầy đủ

Theo kế hoạch P6 §4.2, các nguồn ưu tiên tiếp theo:

| Nguồn | Ước tính studies mới | Phương pháp |
|-------|---------------------|-------------|
| Kirca et al. (2012) reference list | ~10–15 studies pre-2012 | Manual review của 180 entries |
| Marano et al. (2016) reference list | ~5–8 additional EMEs | Focus on home country institution studies |
| Wu et al. (2022) reference list | ~8–10 EMNE studies 2010–2022 | Focus on China/India/Brazil |
| Google Scholar "internationalization firm performance" 2023–2026 | ~5–10 | Keyword search |
| WBES-based studies (n ≥ 50) | ~3–5 | Specifically for LAB productivity |
| SIDS/Pacific island studies | 0–2 | Tourism/hospitality journals |

**Ước tính pool sau full backward scan**: k ≈ 145–155 studies (trước khi loại duplicates)
**Pool conservative target**: k ≈ 130–140 sau deduplication

### 8.2 Studies Tiềm năng từ Kirca et al. (2012) Reference List

Kirca et al. (2012) — MNC capabilities meta — có 180 studies. Nhiều studies trong đó overlap với
pool hiện tại. Những studies tiềm năng còn thiếu (cần xác minh):

| Tác giả | Năm | Estimate | Country | Ghi chú |
|---------|-----|----------|---------|---------|
| Kim & Lyn | 1987 | r ≈ 0.06 | Korea | JIBS; MNE vs foreign investors |
| Daniels et al. | 1984 | r ≈ 0.04 | USA | Earliest US studies |
| Morck & Yeung | 1991 | r ≈ 0.09 | USA/Canada | JIBS; intangible assets |
| Allen & Pantzalis | 1996 | r ≈ 0.08 | USA | JBR; operational flexibility |
| Hitt et al. | 2006 | r ≈ 0.10 | India/China | SMJ; emerging economy focus |
| Isobe, Makino & Montgomery | 2000 | r ≈ 0.12 | Japan | AMJ; first-mover |
| Nachum | 2004 | r ≈ 0.07 | UK | JIBS; EMNEs |

> **Hành động**: Cần chạy 28 search queries (per `search_queries.json`) để confirm và extract
> effect sizes. Mark cho audit Tuần 2–3 (per kế hoạch §6).

---

## 9. Coding Summary cho Inter-coder Reliability

### Double-code subset (20% = 27 studies)

Chọn ngẫu nhiên stratified theo regime và DPL phase:

| Batch | n | Studies | Coder 2 target date |
|-------|---|---------|---------------------|
| Batch 1 | 9 | S06, S17, S22, S35, S58, S71, S88, S109, S126 | Tuần 3 |
| Batch 2 | 9 | S10, S25, S47, S63, S82, S97, S115, S118, S127 | Tuần 4 |
| Batch 3 | 9 | S14, S31, S53, S69, S92, S107, S121, S125, S128 | Tuần 5 |

**Target**: Cohen's κ ≥ 0.70 cho mỗi trong 3 moderator (ICRV, cDAI, DPL).

---

## 10. R Import Script (metafor setup)

```r
# p6/scripts/p6_import_database.R
# Import coded study database vào R cho three-level MARA

library(tidyverse)
library(metafor)

# Load database (sau khi export sang CSV)
df <- read_csv("p6/p6_study_database.csv")

# Compute Fisher's z transformation
df <- df %>%
  mutate(
    z_fisher = 0.5 * log((1 + r) / (1 - r)),
    var_fisher = 1 / (n - 3),
    se_fisher = sqrt(var_fisher)
  )

# ICRV as factor (reference = Regime I)
df$ICRV <- factor(df$ICRV, levels = c("I", "II", "III", "FR", "SIDS", "MX"))

# cDAI as ordered factor
df$cDAI <- factor(df$cDAI, levels = c("L", "M", "H"), ordered = TRUE)

# DPL phase as factor (reference = PRE)
df$DPL <- factor(df$DPL, levels = c("PRE", "SPN", "FOL"))

# Baseline three-level MARA
m_baseline <- rma.mv(
  yi = z_fisher,
  V = var_fisher,
  random = ~ 1 | study_id / effect_id,
  data = df,
  method = "REML",
  slab = paste(author, year)
)

# ICRV moderation
m_icrv <- rma.mv(
  yi = z_fisher, V = var_fisher,
  mods = ~ ICRV - 1,
  random = ~ 1 | study_id / effect_id,
  data = df, method = "REML"
)

# cDAI moderation (continuous)
m_cdai <- rma.mv(
  yi = z_fisher, V = var_fisher,
  mods = ~ cDAI_score,
  random = ~ 1 | study_id / effect_id,
  data = df, method = "REML"
)

# DPL phase moderation
m_dpl <- rma.mv(
  yi = z_fisher, V = var_fisher,
  mods = ~ DPL,
  random = ~ 1 | study_id / effect_id,
  data = df, method = "REML"
)
```

---

## 11. CSV Export Schema

```
study_id, effect_id, author, year, r, n, country, sample_start, sample_end,
icrv, cdai, dpl, doi_type, fp_type, include_flag, source, notes
```

Mỗi effect size trong studies đa-effect (e.g., S02 Grant 1987 có 4 effects) được tách thành
rows riêng biệt với cùng study_id nhưng effect_id khác nhau: effect_id = study_id + "_e1",
"_e2", etc.

---

*File cập nhật lần cuối: 12/05/2026. Tiếp theo: verify starred studies + backward scan Kirca 2012 + Marano 2016 reference lists (Tuần 2–3 per kế hoạch P6).*
