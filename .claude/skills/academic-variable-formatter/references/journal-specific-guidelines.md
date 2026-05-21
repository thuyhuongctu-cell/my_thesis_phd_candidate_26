# Journal-Specific Formatting Guidelines

## Elsevier Journals (Scopus-indexed)

### Variable Notation
- Vectors: bold lowercase `$\mathbf{x}$`
- Matrices: bold uppercase `$\mathbf{X}$`
- Scalars: italic `$x$`
- Use `\mathrm{}` for non-variable text in equations

### Statistical Reporting
- Always include effect sizes
- Report exact p-values to 3 decimal places
- Use `$N$` for total sample, `$n$` for subgroups

**Example:**
```latex
A significant difference was found between groups, 
$t(148) = 3.45, p = .001, d = 0.56$.
```

## Springer Journals (WOS-indexed)

### Mathematical Notation
- Use `\text{}` for text within equations
- Number all equations that are referenced
- Use `\label{}` and `\ref{}` for cross-references

**Example:**
```latex
\begin{equation}\label{eq:regression}
y_i = \beta_0 + \sum_{j=1}^{k} \beta_j x_{ij} + \epsilon_i
\end{equation}

Equation~\ref{eq:regression} shows the linear model.
```

### Statistical Tables
- Align decimal points
- Use consistent decimal places within columns
- Include footnotes for significance levels: $^*p < .05$, $^{**}p < .01$

## Nature/Science Journals

### Concise Notation
- Prefer compact notation: `mean ± s.e.m.` in figures
- In text: `$(M = 45.2, \text{s.e.m.} = 2.3)$`
- Always report confidence intervals for main findings

**Example:**
```latex
The treatment effect was significant 
(difference = 12.3 units, 95\% CI [8.1, 16.5], $p < .001$).
```

### Figure Legends
- Define all error bars: "Error bars represent s.e.m."
- State sample sizes: `$n = 15$ per group`
- Include statistical test information

## IEEE Journals (Engineering)

### Signal Processing Variables
- Time domain: lowercase `$x(t)$, $y(t)$`
- Frequency domain: uppercase `$X(f)$, $Y(f)$`
- Discrete: use brackets `$x[n]$, $X[k]$`

**Example:**
```latex
The discrete Fourier transform is given by
\begin{equation}
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j2\pi kn/N}
\end{equation}
```

### Matrix Operations
- Transpose: `$\mathbf{A}^\mathrm{T}$`
- Inverse: `$\mathbf{A}^{-1}$`
- Hermitian: `$\mathbf{A}^\mathrm{H}$`

## APA Style (Psychology/Social Sciences)

### Statistical Reporting Order
1. Descriptive statistics first
2. Test statistic with degrees of freedom
3. Exact p-value
4. Effect size
5. Confidence interval (when applicable)

**Template:**
```latex
Participants in the treatment group ($M = 23.4, SD = 4.2$) 
scored significantly higher than controls ($M = 19.1, SD = 3.8$), 
$t(78) = 4.23, p < .001, d = 1.09, 95\% CI [2.1, 6.5]$.
```

### Common Mistakes to Avoid
- ❌ `p = .000` → ✓ `p < .001`
- ❌ `r = 0.45` → ✓ `r = .45` (drop leading zero)
- ❌ `M=23.4,SD=4.2` → ✓ `M = 23.4, SD = 4.2` (spacing)
- ❌ Starting sentence with lowercase symbol → ✓ Rephrase or write out "The correlation coefficient"

## Medical Journals (NEJM, Lancet, BMJ)

### Clinical Trial Reporting
- Always report absolute numbers with percentages
- Include confidence intervals for all effect estimates
- Report hazard ratios with CI

**Example:**
```latex
The primary outcome occurred in 45 of 150 patients (30.0\%) 
in the treatment group vs. 67 of 150 (44.7\%) in the control group 
($\text{RR} = 0.67, 95\% \text{CI} [0.49, 0.92], p = .014$).
```

### Survival Analysis
```latex
The hazard ratio for death was $\text{HR} = 0.73$ 
(95\% CI [0.58, 0.91], $p = .005$).
```

## Economics/Finance Journals

### Econometric Models
- Use hat notation for estimates: `$\hat{\beta}$`
- Standard errors in parentheses below coefficients
- Stars for significance in tables

**Regression Table Format:**
```latex
\begin{table}
\caption{Regression Results}
\begin{tabular}{lcc}
\hline
 & Model 1 & Model 2 \\
\hline
Intercept & $2.34^{**}$ & $1.89^*$ \\
 & $(0.45)$ & $(0.52)$ \\
$x_1$ & $0.67^{***}$ & $0.71^{***}$ \\
 & $(0.12)$ & $(0.13)$ \\
\hline
$R^2$ & 0.45 & 0.52 \\
$N$ & 250 & 250 \\
\hline
\multicolumn{3}{l}{\footnotesize Notes: Standard errors in parentheses.} \\
\multicolumn{3}{l}{\footnotesize $^*p<.05$, $^{**}p<.01$, $^{***}p<.001$}
\end{tabular}
\end{table}
```

## Field-Specific Greek Letters

### Physics
- `$\hbar$` (reduced Planck constant)
- `$\lambda$` (wavelength)
- `$\nu$` (frequency)
- `$\Psi$` (wavefunction)

### Chemistry
- `$\Delta$` (change)
- `$\mu$` (chemical potential, dipole moment)
- `$\lambda_{\text{max}}$` (maximum wavelength)

### Biology/Medicine
- `$\alpha$` (significance level, alpha diversity)
- `$\beta$` (beta diversity)
- `$\rho$` (correlation, density)

---

**When to consult this reference:**
- Submitting to a specific journal
- Unsure about field-specific conventions
- Formatting complex tables or equations
- Need examples of complete statistical reporting