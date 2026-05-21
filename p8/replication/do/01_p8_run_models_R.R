# =============================================================================
# Paper 8: Pacific SIDS Forced Internationalization Penalty
# Script: 01_p8_run_models_R.R
# Date:   2026-05-14
#
# HYPOTHESIS: beta(fsts_c) should be NEGATIVE and significant in Pacific SIDS,
#   i.e., greater export-sales share is associated with LOWER labor productivity
#   (Forced Internationalization Penalty) — reversed sign vs mainland Asia's
#   positive coefficient.
# =============================================================================

suppressPackageStartupMessages({
  library(sandwich)   # vcovHC robust SEs
  library(lmtest)     # coeftest
})

cat("=============================================================================\n")
cat("PAPER 8: Pacific SIDS Forced Internationalization Penalty\n")
cat("=============================================================================\n\n")

# ── Paths ─────────────────────────────────────────────────────────────────────
DATA_PATH   <- "/home/user/PAPERS_IN_PHD_2026/data_wbes/p7/p7_pooled_clean.csv"
RESULTS_DIR <- "/home/user/PAPERS_IN_PHD_2026/p8/replication/results"
dir.create(RESULTS_DIR, showWarnings = FALSE, recursive = TRUE)

# =============================================================================
# 1. LOAD & FILTER DATA
# =============================================================================
cat("--- 1. DATA LOADING & FILTERING ---\n")

df_raw <- read.csv(DATA_PATH, stringsAsFactors = FALSE)
cat(sprintf("Full dataset rows: %d\n", nrow(df_raw)))

# Filter to SIDS_small only
df_sids <- df_raw[df_raw$icrv_label == "SIDS_small", ]
cat(sprintf("SIDS_small rows (icrv_label == 'SIDS_small'): %d\n\n", nrow(df_sids)))

# Country × Year breakdown
cat("Country x Year breakdown (all SIDS_small):\n")
tab_cy <- table(df_sids$country, df_sids$year)
print(tab_cy)

cat("\nRow totals by country:\n")
print(sort(table(df_sids$country), decreasing = TRUE))
cat("\nRow totals by year:\n")
print(sort(table(df_sids$year)))

# Apply analysis filters
df <- df_sids[!is.na(df_sids$ln_labor_prod) & !is.na(df_sids$fsts), ]
cat(sprintf("\nAfter !is.na(ln_labor_prod) & !is.na(fsts): n = %d\n", nrow(df)))

# Centred export-intensity variables
fsts_mean <- mean(df$fsts, na.rm = TRUE)
cat(sprintf("Mean fsts (SIDS analysis sample): %.6f\n", fsts_mean))

df$fsts_c  <- df$fsts - fsts_mean
df$fsts_c2 <- df$fsts_c^2

# Exporter-only flag
df$exporter_only <- (df$fsts > 0)
n_exporters <- sum(df$exporter_only, na.rm = TRUE)
cat(sprintf("Exporters (fsts > 0): n = %d (%.1f%% of analysis sample)\n\n",
            n_exporters, 100 * n_exporters / nrow(df)))

# Ensure factor variables for FE
df$country <- factor(df$country)
df$year    <- factor(df$year)

# =============================================================================
# Helper functions
# =============================================================================
robust_se <- function(model) {
  coeftest(model, vcov = vcovHC(model, type = "HC1"))
}

extract_coef <- function(ct, term) {
  idx <- which(rownames(ct) == term)
  if (length(idx) == 0) return(list(beta = NA_real_, se = NA_real_, t = NA_real_, p = NA_real_))
  list(beta = ct[idx, 1], se = ct[idx, 2], t = ct[idx, 3], p = ct[idx, 4])
}

sig_star <- function(p) {
  if (is.na(p)) return("")
  if (p < 0.001) return("***")
  if (p < 0.01)  return("**")
  if (p < 0.05)  return("*")
  if (p < 0.10)  return(".")
  return("")
}

print_coefs <- function(label, model, ct, terms) {
  n   <- length(model$residuals)
  r2  <- summary(model)$r.squared
  ar2 <- summary(model)$adj.r.squared
  cat(sprintf("\n  %s\n", label))
  cat(sprintf("  N = %d  |  R2 = %.4f  |  Adj-R2 = %.4f\n", n, r2, ar2))
  for (trm in terms) {
    info <- extract_coef(ct, trm)
    if (!is.na(info$beta)) {
      cat(sprintf("    %-22s: beta = %+.4f  SE = %.4f  t = %+.3f  p = %.4f  %s\n",
                  trm, info$beta, info$se, info$t, info$p, sig_star(info$p)))
    } else {
      cat(sprintf("    %-22s: [not in model or collinear]\n", trm))
    }
  }
}

# =============================================================================
# 2. BASELINE MODELS — FULL SIDS SAMPLE (HC1 ROBUST SEs)
# =============================================================================
cat("=============================================================================\n")
cat("SECTION 2: Baseline models (full SIDS sample, HC1 robust SEs)\n")
cat("=============================================================================\n")

# M0: Controls + FE only (baseline, no fsts)
m0 <- lm(ln_labor_prod ~ ln_size + firm_age + foreign_own_pct +
            factor(country) + factor(year),
          data = df)
ct_m0 <- robust_se(m0)
print_coefs("M0: Controls + Country FE + Year FE (baseline)", m0, ct_m0,
            c("ln_size", "firm_age", "foreign_own_pct"))

# M1: + fsts_c  [KEY: Forced Penalty test]
m1 <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + foreign_own_pct +
            factor(country) + factor(year),
          data = df)
ct_m1 <- robust_se(m1)
print_coefs("M1: + fsts_c  [KEY: beta(fsts_c) should be NEGATIVE — Forced Penalty]",
            m1, ct_m1,
            c("fsts_c", "ln_size", "firm_age", "foreign_own_pct"))

m1_fsts <- extract_coef(ct_m1, "fsts_c")
cat(sprintf("\n  >>> M1 Forced Penalty test:\n"))
cat(sprintf("      beta(fsts_c) = %+.4f  p = %.4f  %s\n",
            m1_fsts$beta, m1_fsts$p, sig_star(m1_fsts$p)))
cat(sprintf("      Direction: %s\n",
            if (!is.na(m1_fsts$beta) && m1_fsts$beta < 0)
              "NEGATIVE — consistent with Forced Penalty"
            else
              "POSITIVE or NA — penalty NOT confirmed"))

# M2: + fsts_c + fsts_c2 (quadratic)
m2 <- lm(ln_labor_prod ~ fsts_c + fsts_c2 + ln_size + firm_age + foreign_own_pct +
            factor(country) + factor(year),
          data = df)
ct_m2 <- robust_se(m2)
print_coefs("M2: + fsts_c + fsts_c2  [Quadratic — test for U-shape]",
            m2, ct_m2,
            c("fsts_c", "fsts_c2", "ln_size", "firm_age", "foreign_own_pct"))

# M3: + tci_z + dai_z (capability controls)
df_m3 <- df[!is.na(df$tci_z) & !is.na(df$dai_z), ]
m3 <- lm(ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z +
            ln_size + firm_age + foreign_own_pct +
            factor(country) + factor(year),
          data = df_m3)
ct_m3 <- robust_se(m3)
print_coefs("M3: + tci_z + dai_z  [Capability controls]",
            m3, ct_m3,
            c("fsts_c", "fsts_c2", "tci_z", "dai_z",
              "ln_size", "firm_age", "foreign_own_pct"))

cat("\n")

# =============================================================================
# 3. EXPORTERS-ONLY SUBSAMPLE (fsts > 0)
# =============================================================================
cat("=============================================================================\n")
cat("SECTION 3: Exporters-only subsample (fsts > 0)\n")
cat("=============================================================================\n")

df_exp <- df[df$exporter_only == TRUE, ]
cat(sprintf("  n_exporters (analysis sample): %d\n", nrow(df_exp)))
cat(sprintf("  Countries: %d  |  Years: %d\n",
            length(unique(df_exp$country)), length(unique(df_exp$year))))

if (nrow(df_exp) > 20) {
  tryCatch({
    m_exp <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + foreign_own_pct +
                  factor(country) + factor(year),
                data = df_exp)
    ct_exp <- robust_se(m_exp)
    print_coefs("M_exp: Exporters only — fsts_c + controls + FE",
                m_exp, ct_exp,
                c("fsts_c", "ln_size", "firm_age", "foreign_own_pct"))
    exp_fsts <- extract_coef(ct_exp, "fsts_c")
    cat(sprintf("\n  >>> Exporter-only beta(fsts_c) = %+.4f  p = %.4f  %s\n",
                exp_fsts$beta, exp_fsts$p, sig_star(exp_fsts$p)))
  }, error = function(e) {
    cat(sprintf("  WARNING: Exporter FE model failed (%s). Falling back to no-FE.\n", e$message))
    m_exp_nfe <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + foreign_own_pct,
                    data = df_exp)
    ct_exp_nfe <- robust_se(m_exp_nfe)
    print_coefs("M_exp (no FE fallback)", m_exp_nfe, ct_exp_nfe,
                c("fsts_c", "ln_size", "firm_age", "foreign_own_pct"))
    exp_fsts <- extract_coef(ct_exp_nfe, "fsts_c")
    cat(sprintf("\n  >>> Exporter-only (no FE) beta(fsts_c) = %+.4f  p = %.4f\n",
                exp_fsts$beta, exp_fsts$p))
  })
} else {
  cat("  WARNING: Too few exporters for regression.\n")
}

cat("\n")

# =============================================================================
# 4. COUNTRY-LEVEL OLS (no country FE — replicate design-doc β=-0.028, p=.012)
# =============================================================================
cat("=============================================================================\n")
cat("SECTION 4: Country-level OLS (no country FE)\n")
cat("  Design-doc target: beta(fsts) ~ -0.028, p ~ .012\n")
cat("=============================================================================\n")

# 4a. Year FE only (no country FE)
m_nfe <- lm(ln_labor_prod ~ fsts + ln_size + firm_age + foreign_own_pct +
               factor(year),
             data = df)
ct_nfe <- robust_se(m_nfe)
print_coefs("4a. Year-FE only (no country FE): ln_labor_prod ~ fsts + controls",
            m_nfe, ct_nfe,
            c("fsts", "ln_size", "firm_age", "foreign_own_pct"))

nfe_fsts <- extract_coef(ct_nfe, "fsts")
cat(sprintf("\n  >>> Year-FE only beta(fsts) = %+.4f  p = %.4f  [target: -0.028, p=.012]\n",
            nfe_fsts$beta, nfe_fsts$p))

# 4b. Bivariate OLS (no FE)
m_biv <- lm(ln_labor_prod ~ fsts, data = df)
ct_biv <- robust_se(m_biv)
print_coefs("4b. Bivariate OLS (no FE): ln_labor_prod ~ fsts",
            m_biv, ct_biv,
            c("fsts"))
biv_fsts <- extract_coef(ct_biv, "fsts")
cat(sprintf("\n  >>> Bivariate beta(fsts) = %+.4f  p = %.4f\n",
            biv_fsts$beta, biv_fsts$p))

cat("\n")

# =============================================================================
# 5. CAPABILITY EFFECTS (tci_z, dai_z from M3)
# =============================================================================
cat("=============================================================================\n")
cat("SECTION 5: Capability effects (tci_z, dai_z) from M3\n")
cat("=============================================================================\n")

tci_info <- extract_coef(ct_m3, "tci_z")
dai_info  <- extract_coef(ct_m3, "dai_z")

if (!is.na(tci_info$beta)) {
  cat(sprintf("  tci_z (tech/cert capability index): beta = %+.4f  SE = %.4f  p = %.4f  %s\n",
              tci_info$beta, tci_info$se, tci_info$p, sig_star(tci_info$p)))
  cat(sprintf("  Interpretation: Higher tech/cert capability -> %s labor productivity\n",
              ifelse(tci_info$beta > 0, "HIGHER", "LOWER")))
} else {
  cat("  tci_z: not available in M3\n")
}

if (!is.na(dai_info$beta)) {
  cat(sprintf("  dai_z (digital adoption index/website): beta = %+.4f  SE = %.4f  p = %.4f  %s\n",
              dai_info$beta, dai_info$se, dai_info$p, sig_star(dai_info$p)))
  cat(sprintf("  Interpretation: Higher digital adoption -> %s labor productivity\n",
              ifelse(dai_info$beta > 0, "HIGHER", "LOWER")))
} else {
  cat("  dai_z: not available in M3\n")
}

# tci_cert direct proxy (quality_cert)
if ("tci_cert" %in% names(df)) {
  df_cert <- df[!is.na(df$tci_cert), ]
  if (nrow(df_cert) > 50) {
    m_cert <- lm(ln_labor_prod ~ fsts_c + tci_cert + ln_size + firm_age + foreign_own_pct +
                   factor(country) + factor(year),
                 data = df_cert)
    ct_cert <- robust_se(m_cert)
    cert_info <- extract_coef(ct_cert, "tci_cert")
    if (!is.na(cert_info$beta)) {
      cat(sprintf("\n  tci_cert (quality_cert proxy, M_cert):\n"))
      cat(sprintf("    N = %d | beta = %+.4f  SE = %.4f  p = %.4f  %s\n",
                  length(m_cert$residuals),
                  cert_info$beta, cert_info$se, cert_info$p, sig_star(cert_info$p)))
    }
  } else {
    cat("\n  tci_cert: too few non-missing observations\n")
  }
}

cat("\n")

# =============================================================================
# 6. EXPORT RESULTS
# =============================================================================
cat("=============================================================================\n")
cat("SECTION 6: Exporting results\n")
cat("=============================================================================\n")

# -- 6a. Coefficient table --
coef_rows <- list()

add_row <- function(model_name, term, ct) {
  info <- extract_coef(ct, term)
  if (!is.na(info$beta)) {
    coef_rows[[length(coef_rows) + 1]] <<- data.frame(
      model   = model_name,
      term    = term,
      beta    = round(info$beta, 6),
      se      = round(info$se,   6),
      t_stat  = round(info$t,    4),
      p_value = round(info$p,    6),
      signif  = sig_star(info$p),
      stringsAsFactors = FALSE
    )
  }
}

# M0
for (trm in c("ln_size", "firm_age", "foreign_own_pct"))
  add_row("M0_controls_FE", trm, ct_m0)
# M1
for (trm in c("fsts_c", "ln_size", "firm_age", "foreign_own_pct"))
  add_row("M1_fsts_c", trm, ct_m1)
# M2
for (trm in c("fsts_c", "fsts_c2", "ln_size", "firm_age", "foreign_own_pct"))
  add_row("M2_quadratic", trm, ct_m2)
# M3
for (trm in c("fsts_c", "fsts_c2", "tci_z", "dai_z", "ln_size", "firm_age", "foreign_own_pct"))
  add_row("M3_capability", trm, ct_m3)
# Year-FE only
for (trm in c("fsts", "ln_size", "firm_age", "foreign_own_pct"))
  add_row("M_yearFE_only", trm, ct_nfe)
# Bivariate
add_row("M_bivariate", "fsts", ct_biv)

df_coefs <- do.call(rbind, coef_rows)
coef_path <- file.path(RESULTS_DIR, "p8_R_coefs.csv")
write.csv(df_coefs, coef_path, row.names = FALSE)
cat(sprintf("  Saved: %s  (%d rows)\n", coef_path, nrow(df_coefs)))
print(df_coefs)

# -- 6b. Summary table --
m1_f  <- extract_coef(ct_m1, "fsts_c")
m2_f  <- extract_coef(ct_m2, "fsts_c")
m2_f2 <- extract_coef(ct_m2, "fsts_c2")
m3_f  <- extract_coef(ct_m3, "fsts_c")
nfe_f <- extract_coef(ct_nfe, "fsts")
biv_f <- extract_coef(ct_biv, "fsts")

penalty_confirmed <- !is.na(m1_f$beta) && (m1_f$beta < 0) && (m1_f$p < 0.10)

summary_rows <- data.frame(
  metric = c(
    "N_total_analysis", "N_exporters", "N_M3", "fsts_mean",
    "M1_beta_fsts_c", "M1_se_fsts_c", "M1_p_fsts_c", "M1_R2",
    "M2_beta_fsts_c", "M2_beta_fsts_c2", "M2_p_fsts_c",
    "M3_beta_fsts_c", "M3_p_fsts_c",
    "M3_beta_tci_z", "M3_p_tci_z",
    "M3_beta_dai_z", "M3_p_dai_z",
    "M_yearFE_beta_fsts", "M_yearFE_p_fsts",
    "M_biv_beta_fsts", "M_biv_p_fsts",
    "penalty_confirmed"
  ),
  value = c(
    nrow(df), n_exporters, length(m3$residuals), round(fsts_mean, 6),
    round(m1_f$beta, 6), round(m1_f$se, 6), round(m1_f$p, 6),
    round(summary(m1)$r.squared, 4),
    round(m2_f$beta, 6), round(m2_f2$beta, 6), round(m2_f$p, 6),
    round(m3_f$beta, 6), round(m3_f$p, 6),
    round(tci_info$beta, 6), round(tci_info$p, 6),
    round(dai_info$beta, 6), round(dai_info$p, 6),
    round(nfe_f$beta, 6), round(nfe_f$p, 6),
    round(biv_f$beta, 6), round(biv_f$p, 6),
    ifelse(penalty_confirmed, "YES", "NO")
  ),
  stringsAsFactors = FALSE
)

summary_path <- file.path(RESULTS_DIR, "p8_R_summary.csv")
write.csv(summary_rows, summary_path, row.names = FALSE)
cat(sprintf("\n  Saved: %s  (%d rows)\n", summary_path, nrow(summary_rows)))

cat("\n")

# =============================================================================
# 7. FINAL SUMMARY
# =============================================================================
cat("=============================================================================\n")
cat(" PAPER 8 — FINAL SUMMARY\n")
cat("=============================================================================\n")
cat(sprintf("  N total (analysis sample)  : %d\n", nrow(df)))
cat(sprintf("  N exporters (fsts > 0)     : %d\n", n_exporters))
cat(sprintf("  N M3 (tci_z & dai_z obs)   : %d\n", length(m3$residuals)))
cat(sprintf("  Mean fsts (SIDS sample)    : %.6f\n\n", fsts_mean))

cat(sprintf("  M1  beta(fsts_c)           : %+.4f\n", m1_f$beta))
cat(sprintf("      SE                     : %.4f\n",  m1_f$se))
cat(sprintf("      p-value                : %.4f  %s\n", m1_f$p, sig_star(m1_f$p)))
cat(sprintf("      Sign                   : %s\n",
            if (!is.na(m1_f$beta) && m1_f$beta < 0) "NEGATIVE" else "POSITIVE or NA"))
cat(sprintf("      Significant p<.10      : %s\n", ifelse(m1_f$p < 0.10, "YES", "NO")))
cat(sprintf("      Significant p<.05      : %s\n\n", ifelse(m1_f$p < 0.05, "YES", "NO")))

cat(sprintf("  M2  beta(fsts_c)           : %+.4f\n", m2_f$beta))
cat(sprintf("      beta(fsts_c^2)         : %+.4f\n\n", m2_f2$beta))

cat(sprintf("  M3  beta(fsts_c)           : %+.4f  p = %.4f\n", m3_f$beta, m3_f$p))
cat(sprintf("      beta(tci_z)            : %+.4f  p = %.4f\n", tci_info$beta, tci_info$p))
cat(sprintf("      beta(dai_z)            : %+.4f  p = %.4f\n\n", dai_info$beta, dai_info$p))

cat(sprintf("  M_yearFE beta(fsts)        : %+.4f  p = %.4f  [design-doc target: -0.028, p=.012]\n",
            nfe_f$beta, nfe_f$p))
cat(sprintf("  M_biv    beta(fsts)        : %+.4f  p = %.4f\n\n", biv_f$beta, biv_f$p))

cat("─────────────────────────────────────────────────────────────────────────────\n")
if (penalty_confirmed) {
  cat("  CONCLUSION: Forced Penalty CONFIRMED\n")
  cat(sprintf("  beta(fsts_c) = %+.4f (p = %.4f) — NEGATIVE and significant (p < .10)\n",
              m1_f$beta, m1_f$p))
  cat("  Pacific SIDS firms with higher export-sales ratio show LOWER\n")
  cat("  labor productivity, supporting the Forced Internationalization Penalty.\n")
} else if (!is.na(m1_f$beta) && m1_f$beta < 0) {
  cat("  CONCLUSION: Forced Penalty — DIRECTIONALLY CONSISTENT but NOT significant\n")
  cat(sprintf("  beta(fsts_c) = %+.4f (p = %.4f) — NEGATIVE direction but p >= .10\n",
              m1_f$beta, m1_f$p))
  cat("  Penalty directionally consistent; check M_yearFE and M_biv for robustness.\n")
} else {
  cat("  CONCLUSION: Forced Penalty NOT confirmed in M1\n")
  cat(sprintf("  beta(fsts_c) = %+.4f (p = %.4f) — POSITIVE direction\n",
              m1_f$beta, m1_f$p))
  cat("  Consider heterogeneity across countries or quadratic (M2) specification.\n")
}
cat("─────────────────────────────────────────────────────────────────────────────\n")
cat("\nScript complete.\n")
