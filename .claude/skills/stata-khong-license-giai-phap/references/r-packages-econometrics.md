# R Packages Cho Econometrics (Thay Thế Stata)

## Panel Data Analysis

### plm (Core Package)

**Cài đặt:**
```r
install.packages("plm")
library(plm)
```

**Chức năng chính:**
- Fixed effects, random effects, first differences
- Between estimator, pooled OLS
- Tests: Hausman, F-test for fixed effects
- Robust standard errors

**Ví dụ đầy đủ:**
```r
# Tạo panel data object
data("Produc", package = "plm")
pdata <- pdata.frame(Produc, index = c("state", "year"))

# Fixed effects
fe <- plm(gsp ~ pcap + pc + emp + unemp, 
          data = pdata, 
          model = "within")

# Random effects
re <- plm(gsp ~ pcap + pc + emp + unemp, 
          data = pdata, 
          model = "random")

# Hausman test
phtest(fe, re)

# Clustered SE
library(lmtest)
library(sandwich)
coeftest(fe, vcov = vcovHC(fe, cluster = "group"))
```

**Stata equivalent:**
```stata
xtset state year
xtreg gsp pcap pc emp unemp, fe
xtreg gsp pcap pc emp unemp, re
hausman fe re
xtreg gsp pcap pc emp unemp, fe vce(cluster state)
```

### panelView (Visualization)

```r
install.packages("panelView")
library(panelView)

# Visualize panel structure
panelView(Y ~ X, data = pdata, index = c("id", "time"))
```

## Instrumental Variables

### ivreg (Recommended)

```r
install.packages("ivreg")
library(ivreg)

# 2SLS
model_iv <- ivreg(log(wage) ~ education + experience | 
                          father_education + experience,
                  data = wage_data)

summary(model_iv, diagnostics = TRUE)
```

**Diagnostics tự động:**
- Weak instruments test
- Wu-Hausman test
- Sargan test (overidentification)

### AER (Alternative)

```r
library(AER)

# 2SLS
model_iv <- ivreg(log(wage) ~ education + experience | 
                          father_education + experience,
                  data = wage_data)

# GMM
library(gmm)
model_gmm <- gmm(g ~ x, x = instruments, data = data)
```

**Stata equivalent:**
```stata
ivregress 2sls log_wage experience (education = father_education)
estat firststage
estat overid
```

## Time Series

### forecast (ARIMA)

```r
install.packages("forecast")
library(forecast)

# Auto ARIMA
model <- auto.arima(ts_data)
summary(model)

# Forecast
forecast(model, h = 12)

# Manual ARIMA
model <- arima(ts_data, order = c(1, 1, 1))
```

### vars (Vector Autoregression)

```r
install.packages("vars")
library(vars)

# VAR model
var_model <- VAR(data, p = 2, type = "const")
summary(var_model)

# Impulse response
irf <- irf(var_model, n.ahead = 10)
plot(irf)

# Granger causality
causality(var_model, cause = "x")
```

**Stata equivalent:**
```stata
var y x, lags(1/2)
irf create var1, set(myirf) step(10)
irf graph irf
vargranger
```

### urca (Unit Root Tests)

```r
install.packages("urca")
library(urca)

# ADF test
adf_test <- ur.df(ts_data, type = "trend", lags = 4)
summary(adf_test)

# Phillips-Perron
pp_test <- ur.pp(ts_data)
summary(pp_test)

# KPSS test
kpss_test <- ur.kpss(ts_data)
summary(kpss_test)
```

## Robust Standard Errors

### sandwich + lmtest

```r
library(sandwich)
library(lmtest)

model <- lm(y ~ x1 + x2, data = data)

# Heteroskedasticity-robust (HC1 = Stata default)
coeftest(model, vcov = vcovHC(model, type = "HC1"))

# Clustered SE
coeftest(model, vcov = vcovCL(model, cluster = ~ cluster_var))

# HAC (Newey-West)
coeftest(model, vcov = vcovHAC(model))
```

**Type options:**
- `HC0`: White's original
- `HC1`: Stata default (n/(n-k) adjustment)
- `HC2`, `HC3`: More conservative

## Difference-in-Differences

### fixest (Modern, Fast)

```r
install.packages("fixest")
library(fixest)

# DID với fixed effects
model <- feols(outcome ~ treatment | unit + time, 
               data = did_data,
               cluster = ~unit)

summary(model)
etable(model)
```

### did (Callaway & Sant'Anna)

```r
install.packages("did")
library(did)

# DID với staggered treatment
model <- att_gt(yname = "outcome",
                tname = "year",
                idname = "id",
                gname = "treatment_year",
                data = data)

summary(model)
```

## Regression Discontinuity

### rdrobust

```r
install.packages("rdrobust")
library(rdrobust)

# RD estimate
rd <- rdrobust(y = outcome, x = running_var, c = cutoff)
summary(rd)

# Plot
rdplot(y = outcome, x = running_var, c = cutoff)
```

## Export Results

### stargazer (LaTeX/HTML Tables)

```r
install.packages("stargazer")
library(stargazer)

# Multiple models
stargazer(model1, model2, model3,
          type = "latex",
          out = "table1.tex",
          title = "Regression Results",
          align = TRUE,
          no.space = TRUE)

# HTML for Word
stargazer(model1, type = "html", out = "table1.html")
```

### modelsummary (Modern Alternative)

```r
install.packages("modelsummary")
library(modelsummary)

# More flexible than stargazer
modelsummary(list(model1, model2),
             output = "table.docx",
             stars = TRUE,
             gof_omit = "IC|Log|F")
```

## Workflow Template

```r
# === Setup ===
library(haven)      # Read .dta
library(dplyr)      # Data manipulation
library(plm)        # Panel data
library(ivreg)      # IV
library(sandwich)   # Robust SE
library(lmtest)     # Coefficient tests
library(stargazer)  # Export tables

# === Import ===
data <- read_dta("data.dta")

# === Clean ===
data_clean <- data %>%
  filter(!is.na(outcome)) %>%
  mutate(log_y = log(outcome))

# === Analyze ===
# OLS với robust SE
ols <- lm(log_y ~ x1 + x2, data = data_clean)
coeftest(ols, vcov = vcovHC(ols, type = "HC1"))

# Panel FE
pdata <- pdata.frame(data_clean, index = c("id", "year"))
fe <- plm(log_y ~ x1 + x2, data = pdata, model = "within")
coeftest(fe, vcov = vcovHC(fe, cluster = "group"))

# IV
iv <- ivreg(log_y ~ x1 + x2 | z1 + z2, data = data_clean)
summary(iv, diagnostics = TRUE)

# === Export ===
stargazer(ols, fe, iv,
          type = "latex",
          out = "results.tex",
          se = list(
            sqrt(diag(vcovHC(ols, type = "HC1"))),
            sqrt(diag(vcovHC(fe, cluster = "group"))),
            NULL
          ))
```

## So Sánh Stata vs R

| Task | Stata | R |
|------|-------|---|
| Panel FE | `xtreg, fe` | `plm(..., model="within")` |
| Panel RE | `xtreg, re` | `plm(..., model="random")` |
| Robust SE | `reg, robust` | `coeftest(..., vcovHC)` |
| Cluster SE | `reg, vce(cluster id)` | `coeftest(..., vcovCL)` |
| 2SLS | `ivregress 2sls` | `ivreg(y ~ x1 \| z1)` |
| VAR | `var` | `VAR()` from `vars` |
| ARIMA | `arima` | `arima()` or `auto.arima()` |
| DID | Manual | `fixest::feols()` hoặc `did` |

## Learning Path

1. **Bắt đầu:** `plm` cho panel data, `lm` cho OLS
2. **Robust inference:** `sandwich` + `lmtest`
3. **Causal inference:** `ivreg`, `fixest`, `did`
4. **Time series:** `forecast`, `vars`
5. **Export:** `stargazer` hoặc `modelsummary`

Mỗi package đều có vignette chi tiết:
```r
vignette("plm")
vignette("ivreg")
```