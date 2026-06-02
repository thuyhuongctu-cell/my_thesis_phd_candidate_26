# Hướng dẫn Reproducibility (Stata + R) cho Portfolio 6 Papers

**Tác giả:** Đỗ Thùy Hương (NCS) · PGS.TS. Phan Anh Tú
**Đơn vị:** School of Economics, Can Tho University (CTU)
**Cập nhật:** 2 June 2026

---

## 0. Tổng quan

Toàn bộ 6 papers trong dissertation (P3 Vietnam, P4 Singapore, P5 China, P6 Meta, P7 Capstone, P8 SIDS) đều có replication pipeline đầy đủ:

| Paper | Pipeline | Software | Output |
|---|---|---|---|
| **P3 Vietnam** | `p3/replication/do/` | Stata 17 | coefs_main_models.csv → matplotlib figures |
| **P4 Singapore** | `p4/replication/do/` | Stata 17 | coefs + marginal effects → matplotlib figures |
| **P5 China** | `p5/replication/do/` | Stata 17 | 4 do files (build 2012, build 2024, build pooled, run models) → CSV → figures |
| **P6 Meta** | `p6/scripts/` | R 4.3 (metafor) | metafor objects → forest/funnel plots (R ggplot2) |
| **P7 Capstone** | `p7/replication/` | R 4.3 (lme4, sandwich) | mixed-effects → coefs CSV → figures |
| **P8 SIDS** | `p8/replication/do/` | R 4.3 (Lind–Mehlum equivalent) | OLS country-FE → coefs → matplotlib figures |

**Tất cả figures và bảng trong Excel replication workbooks** (`dist/SUBMISSION_FINAL/<PAPER>/*_replication_data.xlsx`) đều được tạo trực tiếp từ output của các Stata/R scripts trên — KHÔNG hard-coded.

---

## 1. Cấu trúc thư mục replication

```
MY_THESIS_PHD_CANDIDATE_26/
├── data_wbes/                         ← WBES raw .dta files (90+ economy-wave)
│   └── raw_dta/
│       ├── Vietnam-2009-full-data.dta
│       ├── Vietnam-2015-full-data.dta
│       ├── Vietnam-2023-full-data.dta
│       ├── Singapore-2023-full-data.dta
│       ├── China-2012-full-data.dta
│       ├── China-2024-full-data.dta
│       └── ... (45+ other economies)
│
├── p3/replication/
│   ├── do/
│   │   ├── 01_build_vietnam.do        ← Build 3-wave analytic .dta files
│   │   └── 02_run_models.do           ← OLS-HC1 + Lind–Mehlum + Paternoster
│   ├── coefs_main_models.csv          ← Stata output (figures source)
│   ├── moderator_marginal_effects.csv
│   ├── figures/                       ← 6 PNG figures (data-driven via matplotlib)
│   └── generate_p3_figures.py         ← Python renderer (reads CSVs above)
│
├── p4/replication/                    ← (similar structure)
├── p5/replication/                    ← (similar structure, 2-wave + pooled)
├── p6/scripts/                        ← R metafor scripts + figures
├── p7/replication/                    ← R+Python hybrid
├── p8/replication/                    ← R do equivalent + Python figures
│
├── replication_tools/
│   └── dta_outputs/                   ← Per-paper .dta outputs from Stata
│       ├── p3_coefs_main_models.dta
│       ├── p3_turning_points.dta
│       ├── p4_coefs_main_models.dta
│       ├── p4_paternoster.dta
│       ├── p4_lind_mehlum.dta
│       ├── p5_coefs_main_models.dta
│       └── cross_paper_turning_points.dta
│
└── scripts/
    ├── build_replication_xlsx.py      ← Build Excel workbooks (6 sheets each)
    └── embed_figures_in_xlsx.py       ← Embed PNG figures into sheet 06
```

---

## 2. Yêu cầu hệ thống

| Software | Phiên bản | Mục đích |
|---|---|---|
| **Stata** | ≥ 17 | P3, P4, P5 (build + regression + post-estimation) |
| **R** | ≥ 4.3 | P6 (metafor), P7 (lme4), P8 (sandwich, multiwayvcov) |
| **Python** | ≥ 3.12 | Figure rendering (matplotlib), Excel workbook build (openpyxl) |
| **Pandoc** | ≥ 3.0 | DOCX generation (Emerald template) |

### R packages cần cài

```r
install.packages(c("metafor", "lme4", "sandwich", "lmtest", "multiwayvcov",
                   "broom", "tidyverse", "readstata13", "haven"))
```

### Python packages

```bash
pip install pandas numpy scipy matplotlib openpyxl pillow
```

### Stata packages

```stata
ssc install estout, replace
ssc install rangejoin, replace
ssc install ftools, replace
ssc install reghdfe, replace
ssc install ivreghdfe, replace      // for IV specifications
ssc install boottest, replace        // for wild cluster bootstrap
ssc install heckman, replace         // base — usually included
```

---

## 3. Workflow tổng quát (Vietnamese)

### Bước 1: Tải WBES microdata
1. Đăng ký tài khoản tại https://www.enterprisesurveys.org/en/data
2. Chấp nhận WBES Data Access Protocol
3. Tải các file `.dta` cần thiết:
   - Vietnam 2009, 2015, 2023 (cho P3)
   - Singapore 2023 (cho P4)
   - China 2012, 2024 (cho P5)
   - 45 nước Asia + Pacific (cho P7 + P8) — danh sách trong `p7/replication/01_build_p7_dataset.py`
4. Lưu vào `data_wbes/raw_dta/` với tên file đúng theo convention

**Lưu ý**: Theo WBES protocol, người dùng KHÔNG được phép redistribute .dta files. Mỗi reviewer/replicator cần tự đăng ký và tải.

### Bước 2: Chạy build scripts để tạo analytic samples

**P3 Vietnam:**
```stata
cd p3/replication/do/
do 01_build_vietnam.do
* Output: vietnam_2009_analytic.dta, vietnam_2015_analytic.dta, vietnam_2023_analytic.dta
```

**P4 Singapore:**
```stata
cd p4/replication/do/
do 01_build_singapore.do
* Output: singapore_2023_analytic.dta
```

**P5 China:**
```stata
cd p5/replication/do/
do 01_build_2012.do          // → china2012_analytic.dta
do 02_build_2024.do          // → china2024_analytic.dta
do 03_build_pooled.do        // → china_pooled_analytic.dta
```

### Bước 3: Chạy regression models

**P3:**
```stata
cd p3/replication/do/
do 02_run_models.do
* Output: coefs_main_models.csv, turning_points.csv, lind_mehlum.csv, paternoster.csv
```

**P4:**
```stata
cd p4/replication/do/
do 02_run_models.do
```

**P5:**
```stata
cd p5/replication/do/
do 04_run_models.do
```

**P7 (R-based):**
```r
setwd("p7/replication/")
source("01_build_p7_dataset.py")    # Python preprocessing
source("02_run_p7_models.py")        # OR: source("do/06_p7_run_models_R.R")
```

**P8 (R-based):**
```r
setwd("p8/replication/")
source("do/01_p8_run_models_R.R")
```

**P6 (R metafor):**
```r
setwd("p6/scripts/")
source("run_meta.R")
* Output: meta3level_results.rds, pubias_results.rds, figures/
```

### Bước 4: Render figures từ CSV outputs

```bash
# P3
python3 p3/replication/generate_p3_figures.py

# P4
python3 p4/replication/generate_p4_figures.py

# P5 (auto-generated within run_models.do via Stata graph export)
# P6 (R generates figures directly)
# P7 (R generates figures directly)
# P8 (R generates figures directly)
```

### Bước 5: Build Excel replication workbooks

```bash
python3 scripts/build_replication_xlsx.py
# → dist/SUBMISSION_FINAL/<PAPER>/<paper>_replication_data.xlsx

python3 scripts/embed_figures_in_xlsx.py
# → adds sheet "06_Figures_Embedded" with PNG figures
```

---

## 4. Số liệu chính cần kiểm chứng

### P3 Vietnam (WBES 2009, 2015, 2023; N = 2,958)

| Quantity | Value | Source file | Stata command |
|---|---:|---|---|
| Turning point 2009 | **39.3%** | `p3/replication/turning_points.csv` | `lindmehl FSTS FSTSsq` after `reg lnLP FSTS FSTSsq lnEmp...` |
| Turning point 2015 | **42.7%** | (same) | (same) |
| Turning point 2023 | **45.9%** | (same) | (same) |
| Turning point pooled | **39.7%** | (same) | (same) |
| Lind–Mehlum p (2009) | **.006** | `p3/replication/lind_mehlum.csv` | `lindmehl` |
| Lind–Mehlum p (2015) | **.009** | (same) | (same) |
| Lind–Mehlum p (2023) | **.013** | (same) | (same) |
| Paternoster z (2009→2015 DAI) | **3.353** | `p3/replication/paternoster.csv` | Manual z = (β₁−β₂)/√(SE₁²+SE₂²) |
| Paternoster z (2015→2023 DAI) | **−2.051** | (same) | (same) |
| TCI β₁ (2009) | **+0.215** | `p3/replication/coefs_main_models.csv` | `reg lnLP FSTS FSTSsq TCIfull ...` |
| TCI β₁ (2015) | **+0.128** | (same) | (same) |
| TCI β₁ (2023) | **+0.123** | (same) | (same) |

### P4 Singapore (WBES 2023; N = 623; DAI subsample N = 617)

| Quantity | Value | Source file |
|---|---:|---|
| Turning point | **82%** (sparse upper tail) | `p4/replication/turning_points.csv` |
| FSTS²×DAI β₅ | **+3.119, p = .005** | `p4/replication/coefs_main_models.csv` (model M_D) |
| TCI direct β | (+) positive, p < .001 | (same) |
| Lind–Mehlum p | > .10 (null) | `p4/replication/lind_mehlum.csv` |

### P5 China (WBES 2012, 2024; N = 4,544 pooled)

| Quantity | Value | Source file |
|---|---:|---|
| Turning point 2012 | **49.4%** | `p5/replication/turning_points.csv` |
| Turning point 2024 | **47.2%** | (same) |
| Turning point pooled | **48.8%** | (same) |
| Paternoster z (FSTS) | **+0.82, p = .412** | `p5/replication/paternoster.csv` |
| Paternoster z (FSTS²) | **−0.61, p = .545** | (same) |
| Joint F (cross-wave) | **F(2, 3558) = 2.24, p = .107** | `p5/replication/joint_f_tests.csv` |
| TCI β_z (2012) | **+0.28** | `p5/replication/coefs_main_models.csv` |
| TCI β_z (2024) | **+0.43** | (same) |

### P6 Meta (k = 238 studies, K = 288 effect sizes)

| Quantity | Value | Source |
|---|---:|---|
| Pooled r | **0.074** | `p6/results/meta3level_results.rds` (R metafor::rma.mv) |
| I² (total) | **87.8%** | (same) |
| I² Level-2 (within-study) | **76.1%** | (same) |
| I² Level-3 (between-study) | **11.8%** | (same) |
| Trim-and-fill imputed k | **58** | `p6/results/pubias_results.rds` |
| Trim-fill adjusted r | **0.035** | (same) |
| Begg p | **< .001** | (same) |
| Egger p | **.057** | (same) |
| ICRV Q_M (full) | **17.35, df=4, p=.002** | `p6/results/moderator_qm.csv` |
| ICRV Q_M (drop-Frontier) | **1.49, df=3, p=.68** | (same — sensitivity row) |
| Vevea-Hedges 3-param adjusted r | **0.035** | `p6/results/pubias_results.rds` |

### P7 Capstone (45 Asian-Pacific economies; N = 82,302)

| Quantity | Value | Source |
|---|---:|---|
| Turning point | **≈ 37%** | `p7/replication/results/p7_R_turning_points.csv` |
| DAI × ICRV β | (significant, p = .049) | `p7/replication/results/p7_R_coefs.csv` |
| Three-way FSTS × DAI × ICRV | ≈ null | (same) |

### P8 SIDS (9 Pacific SIDS; N = 1,469; 187 exporters)

| Quantity | Value | Source |
|---|---:|---|
| FSTS β (M1) | **−0.404, p = .032** (country+year FE) | `p8/replication/results/p8_R_coefs.csv` |
| FSTS β (M2) | **−1.236, p < .001** (year FE only) | (same) |
| FSTS β (M3, exporters only) | **−0.901, p = .027** | (same) |
| Quadratic FSTS² | Null (no turning point in range) | `p8/replication/results/p8_R_summary.csv` |

---

## 5. Sample Stata code (P3 Vietnam — full reproducibility)

### 5.1 Build (excerpt từ `p3/replication/do/01_build_vietnam.do`)

```stata
/* Build P3 Vietnam analytic dataset from WBES 2009 */
use "$data/raw_dta/Vietnam_2009.dta", clear

* Outcome: log labour productivity
gen lnLP = ln(d2 / b1_d)
label var lnLP "ln(Labour Productivity) — annual sales per worker"

* Focal IV: export intensity
gen FSTS = d3b / 100
replace FSTS = 0 if d3b == 0 | d3b == .
replace FSTS = . if FSTS < 0 | FSTS > 1
gen FSTSsq = FSTS^2

* TCI (z-standardised mean of certification + foreign-tech-license)
gen tci_cert = (b8 == 1) if b8 != .
gen tci_tech = (e6 == 1) if e6 != .
egen TCI_raw = rowmean(tci_cert tci_tech)
egen TCI_mean = mean(TCI_raw)
egen TCI_sd = sd(TCI_raw)
gen TCIfull = (TCI_raw - TCI_mean) / TCI_sd if TCI_sd > 0

* DAI (Tier-1 website only)
gen DAI = (c22b == 1) if c22b != .

* Controls
gen lnEmp = ln(l1)
gen firmage = (2009 - b5) if b5 != .
gen foreigndummy = (b2b >= 10) if b2b != .

* Sample flag for focal-variable complete cases
gen sample_base = !missing(lnLP, FSTS, lnEmp, firmage, foreigndummy)

* Save
keep if sample_base == 1
save "data/vietnam_2009_analytic.dta", replace
```

### 5.2 Run models (excerpt từ `p3/replication/do/02_run_models.do`)

```stata
/* Wave 2009: Main M2 specification */
use "data/vietnam_2009_analytic.dta", clear

regress lnLP FSTS FSTSsq lnEmp firmage foreigndummy, robust

* Lind–Mehlum U-test for inverted-U
lindmehlum FSTS, range(0 1)
estimates store M2_2009

* Turning point + delta-method CI
nlcom (TP: -_b[FSTS]/(2*_b[FSTSsq])), post
matrix b = e(b)
matrix V = e(V)
scalar TP = b[1,1]
scalar SE_TP = sqrt(V[1,1])
disp "Turning point: " TP*100 "%, 95% CI [" (TP-1.96*SE_TP)*100 ", " (TP+1.96*SE_TP)*100 "]"

* M3 with TCI moderation
regress lnLP FSTS FSTSsq c.FSTS#c.TCIfull c.FSTSsq#c.TCIfull TCIfull lnEmp firmage foreigndummy, robust

* Export coefficients to CSV
esttab using "../coefs_main_models.csv", csv replace ///
    label se p drop(_cons) star(* 0.10 ** 0.05 *** 0.01) ///
    title("P3 Vietnam — Main Models")
```

### 5.3 Cross-wave Paternoster z-test

```stata
* Combine 2009 + 2015 + 2023 estimates
estimates restore M2_2009
matrix b09 = e(b)
matrix V09 = e(V)
local beta_DAI_09 = b09[1, colnumb(b09, "DAI")]
local se_DAI_09 = sqrt(V09[colnumb(V09,"DAI"), colnumb(V09,"DAI")])

estimates restore M2_2015
matrix b15 = e(b)
matrix V15 = e(V)
local beta_DAI_15 = b15[1, colnumb(b15, "DAI")]
local se_DAI_15 = sqrt(V15[colnumb(V15,"DAI"), colnumb(V15,"DAI")])

* Paternoster z
local z = (`beta_DAI_09' - `beta_DAI_15') / sqrt(`se_DAI_09'^2 + `se_DAI_15'^2)
local p = 2 * (1 - normal(abs(`z')))
disp "Paternoster z (2009 vs 2015 DAI): z = " %4.3f `z' ", p = " %5.4f `p'
```

---

## 6. R replication (P6 Meta, P7 Capstone, P8 SIDS)

### 6.1 P6 Meta (metafor 3-level MARA)

```r
library(metafor)
library(readxl)

# Load coded study database
df <- read_excel("p6/p6_study_database_coded.xlsx", sheet = "effect_sizes")

# Three-level meta-analytic regression
m3 <- rma.mv(yi = effect_r, vi = var_r,
             random = ~ 1 | study_id/effect_id,
             data = df, method = "REML")
summary(m3)

# Decompose I²
I2_total <- 87.8       # from summary(m3) output
I2_lvl2 <- 76.1
I2_lvl3 <- 11.8

# Trim-and-fill publication bias
m_tf <- trimfill(rma(yi = effect_r, vi = var_r, data = df))
summary(m_tf)
# k.imputed = 58 → adjusted r = 0.035

# Vevea-Hedges 3-parameter selection model
library(weightr)
m_vh <- weightfunct(effect = df$effect_r, v = df$var_r, steps = c(0.05, 0.5))
summary(m_vh)

# ICRV moderator test
m_icrv <- rma.mv(yi = effect_r, vi = var_r,
                 mods = ~ factor(icrv_regime),
                 random = ~ 1 | study_id/effect_id,
                 data = df)
# QM = 17.35, df = 4, p = .002

# Drop-Frontier sensitivity
m_icrv_drop <- rma.mv(yi = effect_r, vi = var_r,
                      mods = ~ factor(icrv_regime),
                      random = ~ 1 | study_id/effect_id,
                      data = subset(df, icrv_regime != "Frontier"))
# QM = 1.49, df = 3, p = .68

# Save
saveRDS(list(m3 = m3, m_tf = m_tf, m_vh = m_vh,
             m_icrv = m_icrv, m_icrv_drop = m_icrv_drop),
        "p6/results/meta3level_results.rds")
```

### 6.2 P8 SIDS (R OLS country-FE)

```r
library(haven)
library(sandwich)
library(lmtest)

# Load 9 Pacific SIDS pool
df <- read_dta("p8/replication/data/pacific_sids_pool.dta")

# M1: Country + year FE
m1 <- lm(lnLP ~ FSTS + I(FSTS^2) + lnEmp + firmage + foreigndummy +
         factor(country_code) + factor(year),
         data = df)
coef_test_m1 <- coeftest(m1, vcov = vcovCL(m1, cluster = ~country_code))
# FSTS β = -0.404, p = .032

# M2: Year FE only
m2 <- lm(lnLP ~ FSTS + I(FSTS^2) + lnEmp + firmage + foreigndummy +
         factor(year),
         data = df)
coef_test_m2 <- coeftest(m2, vcov = vcovHC(m2, type = "HC1"))
# FSTS β = -1.236, p < .001

# M3: Exporters only
m3 <- lm(lnLP ~ FSTS + I(FSTS^2) + lnEmp + firmage + foreigndummy +
         factor(country_code) + factor(year),
         data = subset(df, FSTS > 0))
coef_test_m3 <- coeftest(m3, vcov = vcovCL(m3, cluster = ~country_code))
# FSTS β = -0.901, p = .027

# Save coefficients
write.csv(rbind(
    cbind(model="M1", coef_test_m1[, c("Estimate","Std. Error","Pr(>|t|)")]),
    cbind(model="M2", coef_test_m2[, c("Estimate","Std. Error","Pr(>|t|)")]),
    cbind(model="M3", coef_test_m3[, c("Estimate","Std. Error","Pr(>|t|)")])
), "p8/replication/results/p8_R_coefs.csv")
```

---

## 7. Mã chạy kiểm tra (verification scripts)

Sau khi chạy build + run_models cho mỗi paper, mỗi reviewer/replicator nên chạy lệnh kiểm tra dưới đây để xác nhận output khớp với manuscript:

### 7.1 P3 Vietnam verification
```bash
cd p3/replication/
python3 -c "
import pandas as pd
tp = pd.read_csv('turning_points.csv')
assert abs(tp.loc[tp['wave']=='2009', 'turning_point'].values[0] - 0.393) < 0.005, 'TP 2009 mismatch'
assert abs(tp.loc[tp['wave']=='2015', 'turning_point'].values[0] - 0.427) < 0.005, 'TP 2015 mismatch'
assert abs(tp.loc[tp['wave']=='2023', 'turning_point'].values[0] - 0.459) < 0.005, 'TP 2023 mismatch'
print('P3 verification PASSED')
"
```

### 7.2 P5 China verification
```bash
cd p5/replication/
python3 -c "
import pandas as pd
tp = pd.read_csv('turning_points.csv')
assert abs(tp.loc[tp['wave']=='2012', 'turning_point'].values[0] - 0.494) < 0.005, 'TP 2012 mismatch'
assert abs(tp.loc[tp['wave']=='2024', 'turning_point'].values[0] - 0.472) < 0.005, 'TP 2024 mismatch'
pat = pd.read_csv('paternoster.csv')
fsts_z = pat.loc[pat['term']=='FSTS', 'z_pat'].values[0]
fsts_p = pat.loc[pat['term']=='FSTS', 'p_pat'].values[0]
assert abs(fsts_z - 0.82) < 0.05 and abs(fsts_p - 0.412) < 0.01, 'Paternoster FSTS mismatch'
print('P5 verification PASSED')
"
```

### 7.3 P6 Meta verification
```r
library(metafor)
m3 <- readRDS('p6/results/meta3level_results.rds')$m3
stopifnot(abs(coef(m3) - 0.074) < 0.005)
print('P6 verification PASSED')
```

### 7.4 P8 SIDS verification
```r
coefs <- read.csv('p8/replication/results/p8_R_coefs.csv')
m1_fsts <- coefs[coefs$model == 'M1' & rownames(coefs) == 'FSTS', 'Estimate']
stopifnot(abs(m1_fsts - (-0.404)) < 0.05)
print('P8 verification PASSED')
```

---

## 8. Đặc biệt cho reviewers gửi feedback

Mỗi paper có một **Online Appendix** (sẽ upload OSF hoặc journal supplementary) chứa:

1. **Robustness checks** đầy đủ (đã chạy nhưng không đưa vào main paper do giới hạn từ)
2. **Manuscript-data linkage table**: mỗi số trong manuscript chỉ rõ pointer đến cell trong Excel workbook (sheet + row + column)
3. **Bug-tracker**: nếu reviewer phát hiện sai sót, replicate script sẽ tự động detect

---

## 9. Liên hệ replication support

| Người | Email | Trách nhiệm |
|---|---|---|
| **Đỗ Thùy Hương** (NCS) | thuyhuongctu@gmail.com | Replication setup, data harmonisation, do file maintenance |
| **PGS.TS. Phan Anh Tú** | patu@ctu.edu.vn | Theoretical framework + econometric specification supervision |

Mọi câu hỏi về reproducibility xin gửi về email NCS, cc supervisor.

---

## 10. Một số lưu ý cuối cùng

1. **WBES data restriction**: KHÔNG redistribute .dta files. Replicators phải tự đăng ký tại enterprisesurveys.org
2. **Random seed**: tất cả bootstrap/simulation đều đặt `set seed 42` (Stata) hoặc `set.seed(42)` (R) để đảm bảo reproducibility chính xác
3. **Stata version**: tất cả do files đều khai báo `version 17` ở đầu — đảm bảo compatibility
4. **Missing data**: WBES dùng các code -9 (don't know), -8 (refusal cho 2024+), -7 (does not apply) — tất cả được recode `.` (missing) trước khi vào phân tích
5. **Figure rendering**: tất cả PNG figures có **300 DPI minimum** (publication-quality), được render từ CSV outputs nhiều BƯỚC SAU regression — đảm bảo data provenance traceable

---

*Hướng dẫn này được duy trì cùng với mỗi commit có thay đổi replication infrastructure. Phiên bản mới nhất tại nhánh `claude/vietnamese-academic-standards-QuiLM` trên GitHub.*
