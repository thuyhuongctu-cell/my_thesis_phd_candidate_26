# =============================================================================
# Paper 8: Pacific & Indian Ocean SIDS — Robustness battery (R)
# Script: 02_p8_robustness_R.R
# Date:   2026-06-03
#
# Purpose: Re-run in authentic R (mirroring 01_p8_run_models_R.R methodology)
# the 4 robustness items previously prototyped in Python and documented in
# the Stata .do files (02/03/04). This produces the authoritative R-based
# coefficient set that the P8 manuscript §4 robustness panels cite.
#
# Items addressed (RECONCILIATION #7, #8, #9, #10):
#   #7  Comoros exclusion (Pacific-only sub-sample)
#   #8  Wild-cluster Rademacher bootstrap (Cameron-Gelbach-Miller 2008)
#   #9  Leave-one-country-out (LOO) sensitivity
#   #10 foreign_own_pct attrition — M1 without that control recovers all 9 SIDS
#
# Inputs:
#   - data_wbes/p7/p7_pooled_clean.csv
#
# Outputs:
#   - p8/replication/results/p8_R_robustness_coefs.csv
#   - p8/replication/results/p8_R_robustness_summary.csv
#   - p8/replication/results/p8_R_robustness.log
#
# Required packages: sandwich, lmtest, clubSandwich
#   (fwildclusterboot not available for R 4.3.3; WCB implemented manually
#    with Rademacher weights — equivalent to the canonical Cameron-Gelbach-
#    Miller 2008 procedure)
# =============================================================================

suppressPackageStartupMessages({
  library(sandwich)
  library(lmtest)
  library(clubSandwich)
})

set.seed(20260603)

DATA_PATH   <- "data_wbes/p7/p7_pooled_clean.csv"
RESULTS_DIR <- "p8/replication/results"
dir.create(RESULTS_DIR, showWarnings = FALSE, recursive = TRUE)

# Open log file for tee-style output
log_file <- file(file.path(RESULTS_DIR, "p8_R_robustness.log"), open = "wt")
tee <- function(...) {
  cat(..., file = log_file, sep = "")
  cat(..., sep = "")
}

tee("=============================================================================\n")
tee("Paper 8: Pacific & Indian Ocean SIDS — Robustness battery (R)\n")
tee("Run date: ", format(Sys.time(), "%Y-%m-%d %H:%M:%S"), "\n")
tee("=============================================================================\n\n")

# ── 1. Load and define SIDS analysis sample ─────────────────────────────────
df_raw <- read.csv(DATA_PATH, stringsAsFactors = FALSE)
df_sids <- df_raw[df_raw$icrv_label == "SIDS_small", ]
df_sids <- df_sids[!is.na(df_sids$ln_labor_prod) & !is.na(df_sids$fsts), ]

n_full <- nrow(df_sids)
n_comoros <- sum(df_sids$country == "Comoros")
tee(sprintf("Full SIDS analysis sample: %d\n", n_full))
tee(sprintf("Comoros share: %d (%.1f%%)\n\n", n_comoros, 100 * n_comoros / n_full))

# Helper: build sample-specific centred FSTS
build_centred <- function(d) {
  d$fsts_c  <- d$fsts - mean(d$fsts, na.rm = TRUE)
  d$fsts_c2 <- d$fsts_c^2
  d$country <- factor(d$country)
  d$year    <- factor(d$year)
  d
}

# Helper: extract coefficient row from coeftest output
get_coef <- function(ct, term) {
  if (!term %in% rownames(ct)) {
    return(list(beta = NA_real_, se = NA_real_, t = NA_real_, p = NA_real_))
  }
  list(beta = ct[term, 1], se = ct[term, 2], t = ct[term, 3], p = ct[term, 4])
}

# Results collector
all_results <- list()
add_result <- function(spec, term, info, n_obs, g = NA) {
  all_results[[length(all_results) + 1]] <<- data.frame(
    spec = spec, term = term, beta = info$beta, se = info$se,
    t_stat = info$t, p_value = info$p, n = n_obs, g = g,
    stringsAsFactors = FALSE
  )
}

# ── 2. ITEM #7: Comoros exclusion ───────────────────────────────────────────
tee("=============================================================================\n")
tee("ITEM #7: Comoros exclusion — Full SIDS vs Pacific-only\n")
tee("=============================================================================\n\n")

for (sample_name in c("Full_incl_Comoros", "Pacific_only")) {
  d <- if (sample_name == "Full_incl_Comoros") df_sids else df_sids[df_sids$country != "Comoros", ]
  d <- d[!is.na(d$ln_size) & !is.na(d$firm_age) & !is.na(d$foreign_own_pct), ]
  d <- build_centred(d)
  d$country <- droplevels(d$country)
  d$year    <- droplevels(d$year)
  g <- length(unique(d$country))

  tee(sprintf("\n[%s] N = %d, G = %d\n", sample_name, nrow(d), g))

  # M1: + fsts_c (key FIP test)
  m1 <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + foreign_own_pct + country + year, data = d)
  ct1 <- coeftest(m1, vcov = vcovHC(m1, type = "HC1"))
  info_m1 <- get_coef(ct1, "fsts_c")
  tee(sprintf("  M1 β(fsts_c) = %+.4f  SE = %.4f  t = %+.3f  p = %.4f\n",
              info_m1$beta, info_m1$se, info_m1$t, info_m1$p))
  add_result(paste0("M1_", sample_name), "fsts_c", info_m1, nrow(d), g)

  # M2: + quadratic
  m2 <- lm(ln_labor_prod ~ fsts_c + fsts_c2 + ln_size + firm_age + foreign_own_pct + country + year, data = d)
  ct2 <- coeftest(m2, vcov = vcovHC(m2, type = "HC1"))
  info_m2l <- get_coef(ct2, "fsts_c")
  info_m2q <- get_coef(ct2, "fsts_c2")
  tee(sprintf("  M2 β(fsts_c)  = %+.4f  SE = %.4f  p = %.4f\n",
              info_m2l$beta, info_m2l$se, info_m2l$p))
  tee(sprintf("  M2 β(fsts_c²) = %+.4f  SE = %.4f  p = %.4f\n",
              info_m2q$beta, info_m2q$se, info_m2q$p))
  add_result(paste0("M2_", sample_name), "fsts_c", info_m2l, nrow(d), g)
  add_result(paste0("M2_", sample_name), "fsts_c2", info_m2q, nrow(d), g)

  # M3: + capability moderators
  d3 <- d[!is.na(d$tci_z) & !is.na(d$dai_z), ]
  m3 <- lm(ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z + ln_size + firm_age + foreign_own_pct + country + year, data = d3)
  ct3 <- coeftest(m3, vcov = vcovHC(m3, type = "HC1"))
  info_m3l <- get_coef(ct3, "fsts_c")
  info_m3_tci <- get_coef(ct3, "tci_z")
  info_m3_dai <- get_coef(ct3, "dai_z")
  tee(sprintf("  M3 β(fsts_c) = %+.4f  p = %.4f  (N = %d after capability filter)\n",
              info_m3l$beta, info_m3l$p, nrow(d3)))
  tee(sprintf("  M3 β(tci_z)  = %+.4f  p = %.4f\n",
              info_m3_tci$beta, info_m3_tci$p))
  tee(sprintf("  M3 β(dai_z)  = %+.4f  p = %.4f\n",
              info_m3_dai$beta, info_m3_dai$p))
  add_result(paste0("M3_", sample_name), "fsts_c", info_m3l, nrow(d3), g)
  add_result(paste0("M3_", sample_name), "tci_z",  info_m3_tci, nrow(d3), g)
  add_result(paste0("M3_", sample_name), "dai_z",  info_m3_dai, nrow(d3), g)
}

# ── 3. ITEM #8: Wild-cluster Rademacher bootstrap ───────────────────────────
tee("\n=============================================================================\n")
tee("ITEM #8: Wild-cluster Rademacher bootstrap (B = 999)\n")
tee("=============================================================================\n\n")

run_wcb <- function(d, label) {
  d$country <- droplevels(d$country)
  d$year    <- droplevels(d$year)
  countries <- as.character(d$country)
  unique_countries <- unique(countries)
  G <- length(unique_countries)
  n <- nrow(d)
  tee(sprintf("[%s] N = %d, G = %d\n", label, n, G))

  # 1. HC1 baseline
  m_full <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + foreign_own_pct + country + year, data = d)
  ct_hc1 <- coeftest(m_full, vcov = vcovHC(m_full, type = "HC1"))
  beta_hat <- coef(m_full)["fsts_c"]
  info_hc1 <- get_coef(ct_hc1, "fsts_c")
  tee(sprintf("  HC1 baseline:        β = %+.4f, SE = %.4f, p = %.4f\n",
              info_hc1$beta, info_hc1$se, info_hc1$p))

  # 2. Cluster-robust (CR1)
  ct_cl <- coef_test(m_full, vcov = "CR1", cluster = d$country, test = "naive-t")
  cl_se <- ct_cl[ct_cl$Coef == "fsts_c", "SE"]
  cl_p <- ct_cl[ct_cl$Coef == "fsts_c", "p_t"]
  tee(sprintf("  Cluster CR1 (G=%d): β = %+.4f, SE = %.4f, p = %.4f\n", G, beta_hat, cl_se, cl_p))
  t_cluster <- as.numeric(beta_hat / cl_se)

  # 3. Wild-cluster Rademacher bootstrap, H0: β(fsts_c) = 0
  m_restrict <- lm(ln_labor_prod ~ ln_size + firm_age + foreign_own_pct + country + year, data = d)
  resid_r <- residuals(m_restrict)
  fitted_r <- fitted(m_restrict)

  B <- 999
  t_boot <- numeric(B)
  for (b in seq_len(B)) {
    eps_g <- sample(c(-1, 1), size = G, replace = TRUE)
    eps_i <- eps_g[match(countries, unique_countries)]
    y_star <- fitted_r + eps_i * resid_r
    d_b <- d
    d_b$y_star <- y_star
    m_b <- lm(y_star ~ fsts_c + ln_size + firm_age + foreign_own_pct + country + year, data = d_b)
    ct_b <- coef_test(m_b, vcov = "CR1", cluster = d_b$country, test = "naive-t")
    se_b <- ct_b[ct_b$Coef == "fsts_c", "SE"]
    t_b <- coef(m_b)["fsts_c"] / se_b
    t_boot[b] <- t_b
  }
  p_wcb <- mean(abs(t_boot) >= abs(t_cluster), na.rm = TRUE)
  tee(sprintf("  WCB Rademacher (B=999): p = %.4f\n", p_wcb))
  list(hc1_p = info_hc1$p, cr1_p = cl_p, wcb_p = p_wcb, beta = beta_hat, g = G, n = n)
}

# Run WCB on both samples
d_full <- df_sids[!is.na(df_sids$ln_size) & !is.na(df_sids$firm_age) & !is.na(df_sids$foreign_own_pct), ]
d_full <- build_centred(d_full)
res_wcb_full <- run_wcb(d_full, "Full_incl_Comoros")

d_pac <- df_sids[df_sids$country != "Comoros", ]
d_pac <- d_pac[!is.na(d_pac$ln_size) & !is.na(d_pac$firm_age) & !is.na(d_pac$foreign_own_pct), ]
d_pac <- build_centred(d_pac)
res_wcb_pac <- run_wcb(d_pac, "Pacific_only")

# ── 4. ITEM #9: Leave-one-country-out (LOO) ────────────────────────────────
tee("\n=============================================================================\n")
tee("ITEM #9: Leave-one-country-out (LOO) — M1 with sample-specific centring\n")
tee("=============================================================================\n\n")

# Baseline first
d_b <- df_sids[!is.na(df_sids$ln_size) & !is.na(df_sids$firm_age) & !is.na(df_sids$foreign_own_pct), ]
d_b <- build_centred(d_b)
m_b <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + foreign_own_pct + country + year, data = d_b)
ct_b <- coeftest(m_b, vcov = vcovHC(m_b, type = "HC1"))
info_b <- get_coef(ct_b, "fsts_c")
tee(sprintf("(NONE — baseline)         N = %d  G = %d  β = %+.4f  SE = %.4f  p = %.4f\n",
            nrow(d_b), length(unique(d_b$country)), info_b$beta, info_b$se, info_b$p))
add_result("M1_LOO_baseline", "fsts_c", info_b, nrow(d_b), length(unique(d_b$country)))

# LOO
for (c in sort(unique(df_sids$country))) {
  d_loo <- df_sids[df_sids$country != c, ]
  d_loo <- d_loo[!is.na(d_loo$ln_size) & !is.na(d_loo$firm_age) & !is.na(d_loo$foreign_own_pct), ]
  if (nrow(d_loo) < 50) {
    tee(sprintf("drop %-18s skipped (N too small)\n", c))
    next
  }
  d_loo <- build_centred(d_loo)
  m_loo <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + foreign_own_pct + country + year, data = d_loo)
  ct_loo <- coeftest(m_loo, vcov = vcovHC(m_loo, type = "HC1"))
  info_loo <- get_coef(ct_loo, "fsts_c")
  sig <- if (is.na(info_loo$p)) "?" else if (info_loo$p < .05) "*" else if (info_loo$p < .10) "." else "NS"
  tee(sprintf("drop %-18s N = %d  G = %d  β = %+.4f  SE = %.4f  p = %.4f %s\n",
              c, nrow(d_loo), length(unique(d_loo$country)),
              info_loo$beta, info_loo$se, info_loo$p, sig))
  add_result(paste0("M1_LOO_drop_", c), "fsts_c", info_loo, nrow(d_loo), length(unique(d_loo$country)))
}

# ── 5. ITEM #10: M1 without foreign_own_pct (recovers all 9 SIDS) ──────────
tee("\n=============================================================================\n")
tee("ITEM #10: M1 without foreign_own_pct (recovers all 9 SIDS)\n")
tee("=============================================================================\n\n")

d_nf <- df_sids[!is.na(df_sids$ln_size) & !is.na(df_sids$firm_age), ]
d_nf <- build_centred(d_nf)
tee(sprintf("Analysis sample (no foreign_own_pct control): N = %d, G = %d\n",
            nrow(d_nf), length(unique(d_nf$country))))

m_nf <- lm(ln_labor_prod ~ fsts_c + ln_size + firm_age + country + year, data = d_nf)
ct_nf <- coeftest(m_nf, vcov = vcovHC(m_nf, type = "HC1"))
info_nf <- get_coef(ct_nf, "fsts_c")
tee(sprintf("  M1 (no foreign_own_pct) β(fsts_c) = %+.4f  SE = %.4f  p = %.4f\n",
            info_nf$beta, info_nf$se, info_nf$p))
add_result("M1_no_foreign_control", "fsts_c", info_nf, nrow(d_nf), length(unique(d_nf$country)))

# ── 6. Save consolidated results ───────────────────────────────────────────
all_df <- do.call(rbind, all_results)
write.csv(all_df, file.path(RESULTS_DIR, "p8_R_robustness_coefs.csv"), row.names = FALSE)

# Summary tied to each manuscript panel
summary_df <- data.frame(
  panel = c("M_comoros_excluded_M1", "M_comoros_excluded_M2_q", "M_comoros_excluded_M3",
            "M_wild_cluster_full_HC1", "M_wild_cluster_full_CR1", "M_wild_cluster_full_WCB",
            "M_wild_cluster_pac_HC1", "M_wild_cluster_pac_CR1", "M_wild_cluster_pac_WCB",
            "M_LOO_drop_TimorLeste_M1", "M_LOO_drop_Fiji_M1",
            "M_no_foreign_control_M1"),
  description = c("M1 β(fsts_c) Pacific-only sample",
                  "M2 β(fsts_c²) Pacific-only sample",
                  "M3 β(fsts_c) Pacific-only + capability controls",
                  "WCB full sample HC1 p", "WCB full sample CR1 p (G=5)", "WCB full sample bootstrap p",
                  "WCB Pacific-only HC1 p", "WCB Pacific-only CR1 p (G=4)", "WCB Pacific-only bootstrap p",
                  "LOO drop Timor-Leste β(fsts_c) — should STRENGTHEN",
                  "LOO drop Fiji β(fsts_c) — single influential country",
                  "M1 without foreign_own_pct (all 9 SIDS) β(fsts_c)"),
  value = NA_real_,
  stringsAsFactors = FALSE
)

# Fill summary values from the results collected
get_r <- function(spec, term) {
  hit <- all_df[all_df$spec == spec & all_df$term == term, ]
  if (nrow(hit) > 0) hit[1, c("beta", "p_value")] else c(NA, NA)
}
summary_df$value[1]  <- as.numeric(get_r("M1_Pacific_only", "fsts_c")[1])
summary_df$value[2]  <- as.numeric(get_r("M2_Pacific_only", "fsts_c2")[1])
summary_df$value[3]  <- as.numeric(get_r("M3_Pacific_only", "fsts_c")[1])
summary_df$value[4]  <- res_wcb_full$hc1_p
summary_df$value[5]  <- res_wcb_full$cr1_p
summary_df$value[6]  <- res_wcb_full$wcb_p
summary_df$value[7]  <- res_wcb_pac$hc1_p
summary_df$value[8]  <- res_wcb_pac$cr1_p
summary_df$value[9]  <- res_wcb_pac$wcb_p
summary_df$value[10] <- as.numeric(get_r("M1_LOO_drop_TimorLeste", "fsts_c")[1])
summary_df$value[11] <- as.numeric(get_r("M1_LOO_drop_Fiji", "fsts_c")[1])
summary_df$value[12] <- as.numeric(get_r("M1_no_foreign_control", "fsts_c")[1])

write.csv(summary_df, file.path(RESULTS_DIR, "p8_R_robustness_summary.csv"), row.names = FALSE)

tee("\n=============================================================================\n")
tee("Done — results saved to:\n")
tee(paste0("  - p8/replication/results/p8_R_robustness_coefs.csv (", nrow(all_df), " rows)\n"))
tee("  - p8/replication/results/p8_R_robustness_summary.csv (12 panel summaries)\n")
tee("  - p8/replication/results/p8_R_robustness.log\n")
tee("=============================================================================\n")

close(log_file)
