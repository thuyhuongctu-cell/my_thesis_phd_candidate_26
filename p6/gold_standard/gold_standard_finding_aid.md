# Gold-Standard Sample (P6 v1.3) — Finding Aid

**30 studies** chọn stratified random theo ICRV (seed=42, tái lập được).
Mục tiêu: trích xuất thủ công 6 trường (r, n, country, sample_start, sample_end, icrv) từ PDF gốc để kiểm chứng pipeline.

**Tóm tắt:**
- 30 nghiên cứu, 32 effect-rows
- 27/30 có DOI → ưu tiên tìm qua DOI
- 14/30 Open Access → có thể tải miễn phí

## Danh sách 30 nghiên cứu

| # | study_id | Tác giả (Năm) | Quốc gia | ICRV | n_eff | DOI | OA |
|---|---|---|---|---|---|---|---|
| 1 | S04 | McDougall & Oviatt (1996) | USA | I | 1 | 10.1016/0883-9026(95)00081-x | — |
| 2 | S05 | Tallman & Li (1996) | USA | I | 2 | 10.2307/256635 | — |
| 3 | S107 | Song & Lee (2021) | Korea | I | 1 | 10.7275/x78z-g422 | ✓ |
| 4 | S14 | Majocchi & Zucchella (2003) | Italy | II | 1 | 10.1177/0266242603021003001 | — |
| 5 | S153 | Wan & Hoskisson (2003) | Multi | I | 1 | — | — |
| 6 | S157 | Boehe & Cruz (2010) | Brazil | III | 1 | — | ✓ |
| 7 | S164 | Gao, Murray, Kotabe & Lu (2010) | China | III | 1 | — | ✓ |
| 8 | S188 | Do & Phan (2025) | India mfg | III | 1 | 10.5772/intechopen.1011012 | ✓ |
| 9 | S190 | Phan, Ninh & Do (2021) | Turkey mfg | II | 1 | 10.5267/j.dsl.2020.7.001 | ✓ |
| 10 | S194 | Godbole (2024) | India listed family | III | 1 | 10.1002/bsd2.365 | ✓ |
| 11 | S20 | Elango (2006) | USA | I | 2 | 10.1108/1525383x200600015 | — |
| 12 | S206 | Espinosa-Méndez & Jara (2021) | Chile | III | 1 | 10.1080/02102412.2021.1886453 | — |
| 13 | S211 | Olmos & Díez-Vial (2015) | Spain | II | 1 | 10.1108/ejm-06-2012-0365 | ✓ |
| 14 | S212 | Phan, Tran & Lu (2020) | Cameroon | FR | 1 | 10.5267/j.dsl.2020.7.001 | ✓ |
| 15 | S221 | Vithessonthi & Racela (2016) | Thailand | III | 1 | 10.1016/j.mulfin.2015.12.001 | — |
| 16 | S229 | Azman et al. (2022) | Malaysia | III | 1 | 10.1061/(asce)me.1943-5479.0000985 | — |
| 17 | S23 | Chari et al. (2007) | USA | I | 1 | 10.1016/j.jwb.2007.02.007 | — |
| 18 | S230 | Bhandari et al. (2023) | Multi | MX | 1 | 10.1016/j.ibusrev.2023.102135 | ✓ |
| 19 | S234 | Yip et al. (2000) | Multi | MX | 1 | 10.1509/jimk.8.3.10.19635 | — |
| 20 | S27 | Richter (2007) | Germany | I | 1 | 10.1016/s1064-4857(07)13015-1 | — |
| 21 | S34 | Garbe & Richter (2009) | Germany | I | 1 | 10.1016/j.intman.2009.01.003 | — |
| 22 | S61 | Graves & Shan (2014) | Australia | I | 1 | 10.1177/0894486513510534 | — |
| 23 | S68 | Benito-Osorio et al. (2015) | Spain | II | 1 | 10.1016/j.ibusrev.2015.03.003 | ✓ |
| 24 | S69 | Altaf & Shah (2016) | Pakistan | FR | 1 | 10.1016/j.psrb.2016.05.002 | ✓ |
| 25 | S72 | Brida et al. (2016) | Italy | II | 1 | 10.1108/ijchm-10-2014-0517 | — |
| 26 | S75 | Mohr & Batsakis (2016) | Multi | MX | 1 | 10.1007/s11575-016-0284-7 | ✓ |
| 27 | S82 | Purkayastha et al. (2017) | India | III | 1 | 10.1016/j.jwb.2018.03.006 | — |
| 28 | S86 | Pouresmaeili et al. (2018) | Iran | FR | 1 | 10.1504/ijbg.2018.095267 | ✓ |
| 29 | S87 | Hojnik et al. (2018) | Slovenia | I | 1 | 10.1080/1331677x.2018.1504673 | ✓ |
| 30 | S89 | Velez-Calle et al. (2018) | Latin America | III | 1 | 10.1108/ijoem-11-2016-0298 | — |

## Chi tiết từng nghiên cứu (kèm metadata OpenAlex)

### 1. S04 — McDougall & Oviatt (1996)

- **Quốc gia:** USA (ICRV I)
- **Số effect:** 1 (r = -0.03; n = 62)
- **Title (OpenAlex):** New venture internationalization, strategic change, and performance: A follow-up study
- **Journal:** Journal of Business Venturing
- **DOI:** `10.1016/0883-9026(95)00081-x` (confidence: high)
  - Tìm: https://doi.org/10.1016/0883-9026(95)00081-x
- **Cited by:** 711
- **Notes:** New ventures

### 2. S05 — Tallman & Li (1996)

- **Quốc gia:** USA (ICRV I)
- **Số effect:** 2 (r = 0.19; 0.01; n = 192; 192)
- **Title (OpenAlex):** Timing of Breeding by Antbirds (Formicariidae) in an Aseasonal Environment in Amazonian Ecuador
- **Journal:** Ornithological Monographs
- **DOI:** `10.2307/256635` (confidence: high)
  - Tìm: https://doi.org/10.2307/256635
- **Cited by:** 21
- **Notes:** AMJ

### 3. S107 — Song & Lee (2021)

- **Quốc gia:** Korea (ICRV I)
- **Số effect:** 1 (r = 0.05; n = 44)
- **Title (OpenAlex):** Acoustic regularities in infant-directed speech and song across cultures
- **Journal:** Nature Human Behaviour
- **DOI:** `10.7275/x78z-g422` (confidence: suggested)
  - Tìm: https://doi.org/10.7275/x78z-g422
- **OA URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10101735/pdf/nihms-1882109.pdf
- **Cited by:** 170

### 4. S14 — Majocchi & Zucchella (2003)

- **Quốc gia:** Italy (ICRV II)
- **Số effect:** 1 (r = 0.06; n = 220)
- **Journal:** International Small Business Journal
- **DOI:** `10.1177/0266242603021003001` (confidence: review)
  - Tìm: https://doi.org/10.1177/0266242603021003001
- **Notes:** Italian SMEs

### 5. S153 — Wan & Hoskisson (2003)

- **Quốc gia:** Multi (ICRV I)
- **Số effect:** 1 (r = 0.13; n = 244)
- **Title (OpenAlex):** A Chinese herbal medicine Ermiao wan reduces serum uric acid level and inhibits liver xanthine dehydrogenase and xanthin
- **Journal:** Journal of Ethnopharmacology
- **DOI:** *Không có sẵn — phải tìm Google Scholar bằng "Wan & Hoskisson 2003"*
- **Cited by:** 103
- **Notes:** AMJ; home country institutions

### 6. S157 — Boehe & Cruz (2010)

- **Quốc gia:** Brazil (ICRV III)
- **Số effect:** 1 (r = 0.18; n = 168)
- **Title (OpenAlex):** Papel das relações interorganizacionais e da capacidade de inovação na propensão para exportar
- **Journal:** REAd Revista Eletrônica de Administração (Porto Alegre)
- **DOI:** *Không có sẵn — phải tìm Google Scholar bằng "Boehe & Cruz 2010"*
- **OA URL:** https://www.scielo.br/j/read/a/9DKYw6XQzjPsQ5HBmDQWmrS/?lang=pt&format=pdf
- **Cited by:** 10
- **Notes:** JBE; CSR differentiation

### 7. S164 — Gao, Murray, Kotabe & Lu (2010)

- **Quốc gia:** China (ICRV III)
- **Số effect:** 1 (r = 0.13; n = 105)
- **Title (OpenAlex):** Graphene chiral liquid crystals and macroscopic assembled fibres
- **Journal:** Nature Communications
- **DOI:** *Không có sẵn — phải tìm Google Scholar bằng "Gao, Murray, Kotabe & Lu 2010"*
- **OA URL:** https://www.nature.com/articles/ncomms1583.pdf
- **Cited by:** 1096
- **Notes:** JIBS; strategy tripod China

### 8. S188 — Do & Phan (2025)

- **Quốc gia:** India mfg (ICRV III)
- **Số effect:** 1 (r = -0.045; n = 380)
- **Title (OpenAlex):** The emergence of artemisinin partial resistance in Africa: how do we respond?
- **Journal:** The Lancet Infectious Diseases
- **DOI:** `10.5772/intechopen.1011012` (confidence: suggested)
  - Tìm: https://doi.org/10.5772/intechopen.1011012
- **OA URL:** http://www.thelancet.com/article/S1473309924001415/pdf
- **Cited by:** 154
- **Notes:** IntechOpen; India WBES; FGLS; ROS; manager moderator; r confirmed Table 3

### 9. S190 — Phan, Ninh & Do (2021)

- **Quốc gia:** Turkey mfg (ICRV II)
- **Số effect:** 1 (r = -0.04; n = 263)
- **Title (OpenAlex):** The role of Indigenous peoples and local communities in effective and equitable conservation
- **Journal:** Ecology and Society
- **DOI:** `10.5267/j.dsl.2020.7.001` (confidence: medium)
  - Tìm: https://doi.org/10.5267/j.dsl.2020.7.001
- **OA URL:** http://www.ecologyandsociety.org/vol26/iss3/art19/ES-2021-12625.pdf
- **Cited by:** 817
- **Notes:** IntechOpen; WBES Turkey; FGLS; manager experience moderator

### 10. S194 — Godbole (2024)

- **Quốc gia:** India listed family (ICRV III)
- **Số effect:** 1 (r = 0.08; n = 120)
- **Title (OpenAlex):** Deciphering the mechanisms of action of progesterone in breast cancer
- **Journal:** Oncotarget
- **DOI:** `10.1002/bsd2.365` (confidence: medium)
  - Tìm: https://doi.org/10.1002/bsd2.365
- **OA URL:** https://www.oncotarget.com/article/28455/pdf/
- **Cited by:** 10
- **Notes:** BSD 7(3); NIFTY500 family firms; GMM; financial+innovation

### 11. S20 — Elango (2006)

- **Quốc gia:** USA (ICRV I)
- **Số effect:** 2 (r = 0.125; 0.226; n = 326; 393)
- **Title (OpenAlex):** International Channels of Distribution: A Classification System for Analyzing Research Studies
- **Journal:** Multinational Business Review
- **DOI:** `10.1108/1525383x200600015` (confidence: medium)
  - Tìm: https://doi.org/10.1108/1525383x200600015
- **Cited by:** 9
- **Notes:** MBR 2 subsamples

### 12. S206 — Espinosa-Méndez & Jara (2021)

- **Quốc gia:** Chile (ICRV III)
- **Số effect:** 1 (r = 0.04; n = 150)
- **DOI:** `10.1080/02102412.2021.1886453` (confidence: review)
  - Tìm: https://doi.org/10.1080/02102412.2021.1886453
- **Notes:** SJFC; Chile family firm

### 13. S211 — Olmos & Díez-Vial (2015)

- **Quốc gia:** Spain (ICRV II)
- **Số effect:** 1 (r = 0.07; n = 200)
- **Title (OpenAlex):** Monolayer protected gold nanoparticles: the effect of the headgroup–Au interaction
- **Journal:** Physical Chemistry Chemical Physics
- **DOI:** `10.1108/ejm-06-2012-0365` (confidence: medium)
  - Tìm: https://doi.org/10.1108/ejm-06-2012-0365
- **OA URL:** https://pubs.rsc.org/en/content/articlepdf/2014/cp/c4cp01963f
- **Cited by:** 34
- **Notes:** EJM; SME intl paths Spain

### 14. S212 — Phan, Tran & Lu (2020)

- **Quốc gia:** Cameroon (ICRV FR)
- **Số effect:** 1 (r = 0.03; n = 90)
- **Title (OpenAlex):** The role of Indigenous peoples and local communities in effective and equitable conservation
- **Journal:** Ecology and Society
- **DOI:** `10.5267/j.dsl.2020.7.001` (confidence: medium)
  - Tìm: https://doi.org/10.5267/j.dsl.2020.7.001
- **OA URL:** http://www.ecologyandsociety.org/vol26/iss3/art19/ES-2021-12625.pdf
- **Cited by:** 817
- **Notes:** DSL; W-shaped Cameroon

### 15. S221 — Vithessonthi & Racela (2016)

- **Quốc gia:** Thailand (ICRV III)
- **Số effect:** 1 (r = 0.05; n = 400)
- **DOI:** `10.1016/j.mulfin.2015.12.001` (confidence: medium)
  - Tìm: https://doi.org/10.1016/j.mulfin.2015.12.001
- **Notes:** JMFM; short/long-run Thailand

### 16. S229 — Azman et al. (2022)

- **Quốc gia:** Malaysia (ICRV III)
- **Số effect:** 1 (r = 0.09; n = 200)
- **Title (OpenAlex):** The Effectiveness of a Design Thinking Tool for the Development of Creativity in Teaching STEM Subjects among Special Ne
- **Journal:** The International Journal of Science Mathematics and Technology Learning
- **DOI:** `10.1061/(asce)me.1943-5479.0000985` (confidence: medium)
  - Tìm: https://doi.org/10.1061/(asce)me.1943-5479.0000985
- **Cited by:** 4
- **Notes:** JMgmtEng; Malaysia construction

### 17. S23 — Chari et al. (2007)

- **Quốc gia:** USA (ICRV I)
- **Số effect:** 1 (r = 0.37; n = 131)
- **Title (OpenAlex):** International diversification and firm performance: Role of information technology investments
- **Journal:** Journal of World Business
- **DOI:** `10.1016/j.jwb.2007.02.007` (confidence: review)
  - Tìm: https://doi.org/10.1016/j.jwb.2007.02.007
- **Cited by:** 67
- **Notes:** JWB 2 effects

### 18. S230 — Bhandari et al. (2023)

- **Quốc gia:** Multi (ICRV MX)
- **Số effect:** 1 (r = 0.1; n = 300)
- **Title (OpenAlex):** Book Review on Medani P. Bhandari (2023). Live and Let Others Live – In Reference to Sustainability and Environment Cons
- **Journal:** Health Economics and Management Review
- **DOI:** `10.1016/j.ibusrev.2023.102135` (confidence: medium)
  - Tìm: https://doi.org/10.1016/j.ibusrev.2023.102135
- **OA URL:** https://armgpublishing.com/wp-content/uploads/2024/07/HEM_5_2_2024_10.pdf
- **Cited by:** 3
- **Notes:** IBR; digitalization OLI

### 19. S234 — Yip et al. (2000)

- **Quốc gia:** Multi (ICRV MX)
- **Số effect:** 1 (r = 0.06; n = 150)
- **Title (OpenAlex):** Total Global Strategy
- **DOI:** `10.1509/jimk.8.3.10.19635` (confidence: medium)
  - Tìm: https://doi.org/10.1509/jimk.8.3.10.19635
- **Cited by:** 219
- **Notes:** JIM; newly internationalizing firms

### 20. S27 — Richter (2007)

- **Quốc gia:** Germany (ICRV I)
- **Số effect:** 1 (r = -0.058; n = 85)
- **DOI:** `10.1016/s1064-4857(07)13015-1` (confidence: medium)
  - Tìm: https://doi.org/10.1016/s1064-4857(07)13015-1

### 21. S34 — Garbe & Richter (2009)

- **Quốc gia:** Germany (ICRV I)
- **Số effect:** 1 (r = -0.085; n = 85)
- **Title (OpenAlex):** Embracing risk as a core competence: The case of CEMEX
- **Journal:** Journal of International Management
- **DOI:** `10.1016/j.intman.2009.01.003` (confidence: medium)
  - Tìm: https://doi.org/10.1016/j.intman.2009.01.003
- **Cited by:** 33
- **Notes:** 3 effects

### 22. S61 — Graves & Shan (2014)

- **Quốc gia:** Australia (ICRV I)
- **Số effect:** 1 (r = -0.07; n = 4217)
- **Title (OpenAlex):** An Empirical Analysis of the Effect of Internationalization on the Performance of Unlisted Family and Nonfamily Firms in
- **Journal:** Family Business Review
- **DOI:** `10.1177/0894486513510534` (confidence: review)
  - Tìm: https://doi.org/10.1177/0894486513510534
- **Cited by:** 91
- **Notes:** Large sample

### 23. S68 — Benito-Osorio et al. (2015)

- **Quốc gia:** Spain (ICRV II)
- **Số effect:** 1 (r = -0.09; n = 2748)
- **Title (OpenAlex):** Context, law and reinvestment decisions: Why the transitional periphery differs from other post-state socialist economie
- **Journal:** International Business Review
- **DOI:** `10.1016/j.ibusrev.2015.03.003` (confidence: review)
  - Tìm: https://doi.org/10.1016/j.ibusrev.2015.03.003
- **OA URL:** https://strathprints.strath.ac.uk/52151/1/Demirbag_etal_IBR_2015_The_law_corruption_and_reinvestment_decisions_the_transitional_periphery_in_comparative.pdf
- **Cited by:** 24
- **Notes:** Spanish mfg large

### 24. S69 — Altaf & Shah (2016)

- **Quốc gia:** Pakistan (ICRV FR)
- **Số effect:** 1 (r = 0.08; n = 180)
- **Title (OpenAlex):** Tumor suppressor role of microRNA-1296 in triple-negative breast cancer
- **Journal:** Oncotarget
- **DOI:** `10.1016/j.psrb.2016.05.002` (confidence: suggested)
  - Tìm: https://doi.org/10.1016/j.psrb.2016.05.002
- **OA URL:** https://www.oncotarget.com/article/6961/pdf/
- **Cited by:** 64
- **Notes:** Pakistan firms

### 25. S72 — Brida et al. (2016)

- **Quốc gia:** Italy (ICRV II)
- **Số effect:** 1 (r = -0.032; n = 82)
- **Title (OpenAlex):** Dynamic relationship between tourism and economic growth in MERCOSUR countries: a nonlinear approach based on asymmetric
- **Journal:** Economics bulletin
- **DOI:** `10.1108/ijchm-10-2014-0517` (confidence: review)
  - Tìm: https://doi.org/10.1108/ijchm-10-2014-0517
- **Cited by:** 42
- **Notes:** Italy hotels

### 26. S75 — Mohr & Batsakis (2016)

- **Quốc gia:** Multi (ICRV MX)
- **Số effect:** 1 (r = 0.05; n = 110)
- **Title (OpenAlex):** Internationalization Speed and Firm Performance: A Study of the Market-Seeking Expansion of Retail MNEs
- **Journal:** Management International Review
- **DOI:** `10.1007/s11575-016-0284-7` (confidence: review)
  - Tìm: https://doi.org/10.1007/s11575-016-0284-7
- **OA URL:** http://bura.brunel.ac.uk/handle/2438/12228
- **Cited by:** 92
- **Notes:** Internation speed

### 27. S82 — Purkayastha et al. (2017)

- **Quốc gia:** India (ICRV III)
- **Số effect:** 1 (r = 0.029; n = 185)
- **Title (OpenAlex):** Business group effects on the R&amp;D intensity-internationalization relationship: Empirical evidence from India
- **Journal:** Journal of World Business
- **DOI:** `10.1016/j.jwb.2018.03.006` (confidence: review)
  - Tìm: https://doi.org/10.1016/j.jwb.2018.03.006
- **Cited by:** 91
- **Notes:** India conglomerates

### 28. S86 — Pouresmaeili et al. (2018)

- **Quốc gia:** Iran (ICRV FR)
- **Số effect:** 1 (r = 0.69; n = 226)
- **Title (OpenAlex):** A comprehensive overview on osteoporosis and its risk factors
- **Journal:** Therapeutics and Clinical Risk Management
- **DOI:** `10.1504/ijbg.2018.095267` (confidence: medium)
  - Tìm: https://doi.org/10.1504/ijbg.2018.095267
- **OA URL:** https://www.dovepress.com/getfile.php?fileID=45951
- **Cited by:** 570
- **Notes:** Iran SMEs high r

### 29. S87 — Hojnik et al. (2018)

- **Quốc gia:** Slovenia (ICRV I)
- **Số effect:** 1 (r = 0.035; n = 267)
- **Title (OpenAlex):** Eco-Innovation and Firm Efficiency: Empirical Evidence from Slovenia
- **Journal:** Foresight-Russia
- **DOI:** `10.1080/1331677x.2018.1504673` (confidence: review)
  - Tìm: https://doi.org/10.1080/1331677x.2018.1504673
- **OA URL:** https://foresight-journal.hse.ru/data/2017/09/28/1159178022/Manolova 103-111.pdf
- **Cited by:** 43
- **Notes:** Slovenia; 7 eff

### 30. S89 — Velez-Calle et al. (2018)

- **Quốc gia:** Latin America (ICRV III)
- **Số effect:** 1 (r = 0.05; n = 147)
- **Title (OpenAlex):** The influence of political risk, inertia and imitative behavior on the location choice of Chinese multinational enterpri
- **Journal:** International Journal of Emerging Markets
- **DOI:** `10.1108/ijoem-11-2016-0298` (confidence: review)
  - Tìm: https://doi.org/10.1108/ijoem-11-2016-0298
- **Cited by:** 33
- **Notes:** Latin Am. MNEs

---

## Hướng dẫn tìm PDF

**Ưu tiên 1 — Open Access (14 studies):** click trực tiếp `OA URL` ở mỗi mục.

**Ưu tiên 2 — DOI có sẵn (27 studies):** mở `https://doi.org/{DOI}`. Nếu paywall:
- Thử CTU library proxy (https://login.proxy.ctu.edu.vn/...)
- Thử ResearchGate (search by DOI)
- Thử Sci-Hub mirror (rủi ro pháp lý, dùng theo quy định trường)
- Email tác giả trực tiếp (tỷ lệ phản hồi ~60% trong 1-2 tuần)

**Ưu tiên 3 — Không DOI (3 studies):** Google Scholar full title; nếu vẫn không có → thay từ stratum tương đương (xem `01_select_sample.py` để re-draw seed).

## File template điền

Sau khi mở từng PDF, điền 6 trường vào `gold_standard_manual_template.csv` (đã pre-fill `study_id`, `effect_id`, `author`, `year`). Sau đó chạy `python3 02_compute_metrics.py` để so sánh với pipeline.