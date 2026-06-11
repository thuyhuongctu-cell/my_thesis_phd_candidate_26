# Python Cho Econometrics (Thay Thế Stata)

## Core Libraries

### pandas (Data Manipulation)

```python
import pandas as pd

# Đọc Stata file
df = pd.read_stata("data.dta")

# Basic operations
df.describe()
df.head()

# Filter
df_clean = df[df['outcome'].notna()]

# Create variables
df['log_y'] = np.log(df['outcome'])

# Group operations
df.groupby('state')['outcome'].mean()
```

### statsmodels (Statistical Models)

```python
import statsmodels.api as sm
import statsmodels.formula.api as smf

# OLS
model = smf.ols('outcome ~ x1 + x2', data=df).fit()
print(model.summary())

# Robust standard errors
model_robust = smf.ols('outcome ~ x1 + x2', data=df).fit(
    cov_type='HC1'  # Stata default
)

# Clustered SE
model_cluster = smf.ols('outcome ~ x1 + x2', data=df).fit(
    cov_type='cluster',
    cov_kwds={'groups': df['cluster_id']}
)
```

## Panel Data

### linearmodels (Panel Econometrics)

```python
from linearmodels.panel import PanelOLS, RandomEffects

# Setup panel data
df_panel = df.set_index(['id', 'year'])

# Fixed effects
fe = PanelOLS(
    df_panel['outcome'],
    df_panel[['x1', 'x2']],
    entity_effects=True
).fit(cov_type='clustered', cluster_entity=True)

print(fe.summary)

# Random effects
re = RandomEffects(
    df_panel['outcome'],
    df_panel[['x1', 'x2']]
).fit()
```

**Stata equivalent:**
```stata
xtset id year
xtreg outcome x1 x2, fe vce(cluster id)
xtreg outcome x1 x2, re
```

## Instrumental Variables

### linearmodels.iv

```python
from linearmodels.iv import IV2SLS

# 2SLS
model_iv = IV2SLS(
    dependent=df['log_wage'],
    exog=df[['experience']],
    endog=df[['education']],
    instruments=df[['father_education']]
).fit(cov_type='robust')

print(model_iv.summary)

# Diagnostics
print(f"First stage F-stat: {model_iv.first_stage.diagnostics['f.stat']}")
print(f"Sargan test: {model_iv.sargan}")
```

## Time Series

### statsmodels.tsa

```python
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, grangercausalitytests
from statsmodels.tsa.vector_ar.var_model import VAR

# ARIMA
model = ARIMA(ts_data, order=(1, 1, 1)).fit()
print(model.summary())
forecast = model.forecast(steps=12)

# Unit root test
adf_result = adfuller(ts_data)
print(f"ADF statistic: {adf_result[0]}")
print(f"p-value: {adf_result[1]}")

# VAR
var_model = VAR(df[['y', 'x']])
var_fit = var_model.fit(maxlags=2)
print(var_fit.summary())

# Impulse response
irf = var_fit.irf(10)
irf.plot()

# Granger causality
granger = grangercausalitytests(df[['y', 'x']], maxlag=4)
```

## Difference-in-Differences

### Manual Implementation

```python
import statsmodels.formula.api as smf

# Create treatment indicator
df['post'] = (df['year'] >= treatment_year).astype(int)
df['treated'] = df['group'].isin(treatment_groups).astype(int)
df['did'] = df['post'] * df['treated']

# DID regression
did_model = smf.ols(
    'outcome ~ treated + post + did + controls',
    data=df
).fit(cov_type='cluster', cov_kwds={'groups': df['id']})

print(f"DID estimate: {did_model.params['did']}")
print(f"SE: {did_model.bse['did']}")
```

### pydid (Advanced)

```python
# For Callaway & Sant'Anna estimator
# pip install pydid
from pydid import ATT

att = ATT(
    data=df,
    outcome='outcome',
    time='year',
    id='id',
    cohort='treatment_year'
)

results = att.estimate()
```

## Regression Discontinuity

### rdrobust (Port from R)

```python
# pip install rdrobust
from rdrobust import rdrobust, rdplot

# RD estimate
rd = rdrobust(
    y=df['outcome'],
    x=df['running_var'],
    c=cutoff
)

print(rd.summary())

# Plot
rdplot(
    y=df['outcome'],
    x=df['running_var'],
    c=cutoff
)
```

## Export Results

### stargazer (Python Port)

```python
from stargazer.stargazer import Stargazer

# Multiple models
stargazer = Stargazer([model1, model2, model3])
stargazer.title('Regression Results')
stargazer.show_degrees_of_freedom(False)

# LaTeX
with open('table.tex', 'w') as f:
    f.write(stargazer.render_latex())

# HTML
with open('table.html', 'w') as f:
    f.write(stargazer.render_html())
```

### regression_tables (Alternative)

```python
import regression_tables as rt

rt.summary(
    [model1, model2, model3],
    stars=True,
    output='table.tex'
)
```

## Complete Workflow Template

```python
# === Setup ===
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS
from stargazer.stargazer import Stargazer

# === Import ===
df = pd.read_stata("data.dta")

# === Clean ===
df_clean = df.dropna(subset=['outcome'])
df_clean['log_y'] = np.log(df_clean['outcome'])

# === Analyze ===

# 1. OLS với robust SE
ols = smf.ols('log_y ~ x1 + x2', data=df_clean).fit(cov_type='HC1')
print(ols.summary())

# 2. Panel FE
df_panel = df_clean.set_index(['id', 'year'])
fe = PanelOLS(
    df_panel['log_y'],
    df_panel[['x1', 'x2']],
    entity_effects=True
).fit(cov_type='clustered', cluster_entity=True)

print(fe.summary)

# 3. IV
iv = IV2SLS(
    dependent=df_clean['log_y'],
    exog=df_clean[['x2']],
    endog=df_clean[['x1']],
    instruments=df_clean[['z1']]
).fit(cov_type='robust')

print(iv.summary)

# === Export ===
stargazer = Stargazer([ols, fe, iv])
stargazer.title('Main Results')
stargazer.covariate_order(['x1', 'x2'])

with open('results.tex', 'w') as f:
    f.write(stargazer.render_latex())
```

## Key Packages Summary

| Package | Purpose | Install |
|---------|---------|----------|
| `pandas` | Data manipulation | `pip install pandas` |
| `statsmodels` | Statistical models | `pip install statsmodels` |
| `linearmodels` | Panel/IV econometrics | `pip install linearmodels` |
| `rdrobust` | RD design | `pip install rdrobust` |
| `stargazer` | Export tables | `pip install stargazer` |

## Stata vs Python Quick Reference

| Task | Stata | Python |
|------|-------|--------|
| Read .dta | `use data.dta` | `pd.read_stata("data.dta")` |
| Summary stats | `summarize` | `df.describe()` |
| OLS | `reg y x1 x2` | `smf.ols('y ~ x1 + x2', data=df).fit()` |
| Robust SE | `reg y x, robust` | `.fit(cov_type='HC1')` |
| Cluster SE | `reg y x, vce(cluster id)` | `.fit(cov_type='cluster', cov_kwds={'groups': df['id']})` |
| Panel FE | `xtreg y x, fe` | `PanelOLS(..., entity_effects=True)` |
| 2SLS | `ivregress 2sls` | `IV2SLS(...)` |
| Gen variable | `gen log_y = log(y)` | `df['log_y'] = np.log(df['y'])` |
| Keep if | `keep if x > 10` | `df = df[df['x'] > 10]` |

## Advantages of Python

- **Machine learning:** scikit-learn, TensorFlow, PyTorch
- **Big data:** Dask, PySpark
- **Web scraping:** BeautifulSoup, Scrapy
- **General purpose:** Automation, APIs, deployment

## When to Use Python vs R

**Use Python if:**
- You need ML/deep learning
- Working with big data pipelines
- Building production systems
- Already know Python

**Use R if:**
- Pure econometrics/statistics
- Need cutting-edge statistical methods
- Academic research workflow
- Better documentation for econ packages

**Reality:** Both work well. R has slight edge for pure econometrics, Python for everything else.