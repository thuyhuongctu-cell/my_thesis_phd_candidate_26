#!/usr/bin/env Rscript
# =============================================================================
# P6 Three-Level MARA — Updated for merged database (k = 287 + new studies)
# =============================================================================
# Script:  p6_mara_updated.R
# Input:   ../data/p6_study_database_updated.csv  (from 10_merge_new_studies.py)
# Output:  ../results/updated/                     (tables + forest data)
#
# Changes from p6_real_mara.R (legacy):
#   - Uses *_std columns (icrv_std, dpl_std, cdai_std) — standardized codes
#   - icrv_std: integer 1–6 (1=Advanced, 2=Emerging, 3=Transition,
#                             4=Resource-rich/GCC, 5=SIDS, 6=Frontier, 0=Multi)
#   - dpl_std:  integer 1/2/3 (1=pre-2000, 2=2000-2009, 3=2010+)
#   - cdai_std: continuous 0–1 (World Bank DAI proxy; legacy L→0.25/M→0.50/H→0.75)
#   - doi_type_std, fp_type_std: full descriptive names
#
# Usage (local R ≥ 4.3):
#   Rscript p6/scripts/p6_mara_updated.R
#
# Usage (Docker):
#   docker run --rm -v $(pwd):/analysis rocker/tidyverse:4.3.2 \
#     Rscript /analysis/p6/scripts/p6_mara_updated.R
# =============================================================================

suppressPackageStartupMessages({
  library(metafor)
  library(dplyr)
  library(readr)
})

# ── Paths ─────────────────────────────────────────────────────────────────────
script_dir  <- tryCatch(dirname(normalizePath(sys.frame(1)$ofile)),
                        error = function(e) getwd())
# Try updated first, fall back to original
updated_file  <- file.path(script_dir, "..", "data", "p6_study_database_updated.csv")
original_file <- file.path(script_dir, "..", "data", "p6_study_database.csv")
data_file     <- if (file.exists(updated_file)) updated_file else original_file
results_dir   <- file.path(script_dir, "..", "results", "updated")
dir.create(results_dir, showWarnings = FALSE, recursive = TRUE)

cat("=============================================================\n")
cat("P6 Three-Level MARA — Updated Database\n")
cat("=============================================================\n\n")
cat("Input:", data_file, "\n\n")

# ── Load & Prepare Data ───────────────────────────────────────────────────────
raw <- read_csv(data_file, show_col_types = FALSE)

# Main sample: include_flag == 1 (legacy) or "Y" (new)
dat <- raw %>%
  filter(include_flag == 1 | toupper(include_flag) == "Y") %>%
  # Ensure *_std columns exist (script can run on either old or new database)
  mutate(
    icrv_std = coalesce(as.character(icrv_std), as.character(icrv)),
    dpl_std  = coalesce(as.character(dpl_std),  as.character(dpl)),
    cdai_std = coalesce(suppressWarnings(as.numeric(cdai_std)),
                        case_when(cdai == "H" ~ 0.75,
                                  cdai == "M" ~ 0.50,
                                  cdai == "L" ~ 0.25,
                                  TRUE ~ as.numeric(cdai))),
    doi_type_std = coalesce(doi_type_std, doi_type),
    fp_type_std  = coalesce(fp_type_std,  fp_type),
    # Numeric r must be present
    r = suppressWarnings(as.numeric(r)),
    n = suppressWarnings(as.numeric(n))
  ) %>%
  filter(!is.na(r), !is.na(n), n > 0)

cat(sprintf("Sample: K = %d effects, k = %d unique studies\n\n",
            nrow(dat), n_distinct(dat$study_id)))

# Fisher's z transformation
dat <- escalc(measure = "ZCOR", ri = r, ni = n, data = as.data.frame(dat),
              var.names = c("yi", "vi"))

# Factor encoding — standardized codes
# ICRV: exclude multi (0) and regimes with k < 3
icrv_regime_labels <- c(
  "1" = "Advanced", "2" = "Emerging", "3" = "Transition",
  "4" = "Resource-rich", "5" = "SIDS", "6" = "Frontier", "0" = "Multi"
)
dat$icrv_f   <- factor(dat$icrv_std,
                        levels = c("1", "2", "3", "4", "5", "6", "0"))
dat$dpl_f    <- factor(dat$dpl_std, levels = c("1", "2", "3"))
dat$cdai_num <- suppressWarnings(as.numeric(dat$cdai_std))

# ── Helpers ───────────────────────────────────────────────────────────────────
z2r <- function(z) tanh(z)

print_r <- function(beta, cilb, ciub, pval = NA) {
  r   <- round(z2r(beta), 3)
  lo  <- round(z2r(cilb),  3)
  hi  <- round(z2r(ciub),  3)
  p_s <- if (!is.na(pval)) sprintf(", p = %.4f", pval) else ""
  sprintf("r = %.3f [%.3f, %.3f]%s", r, lo, hi, p_s)
}

i2_threelevel <- function(mod) {
  v_bar <- mean(mod$vi, na.rm = TRUE)
  s2    <- sum(mod$sigma2)
  list(
    I2_total   = round(100 * s2 / (s2 + v_bar), 1),
    I2_between = round(100 * mod$sigma2[1] / (s2 + v_bar), 1),
    I2_within  = round(100 * mod$sigma2[2] / (s2 + v_bar), 1),
    tau2_total = round(s2, 5)
  )
}

# =============================================================================
# MODEL 0 — Baseline Three-Level Random-Effects MARA
# =============================================================================
cat("─────────────────────────────────────────────────────────────\n")
cat("MODEL 0: Baseline Three-Level MARA\n")
cat("─────────────────────────────────────────────────────────────\n")

m0 <- rma.mv(
  yi = yi, V = vi,
  random = ~ 1 | study_id / effect_id,
  data   = dat,
  method = "REML",
  slab   = paste(dat$author, dat$year)
)

i2 <- i2_threelevel(m0)
cat(sprintf("Pooled effect : %s\n",
            print_r(m0$beta[1], m0$ci.lb[1], m0$ci.ub[1], m0$pval[1])))
cat(sprintf("sigma²(study) : %.5f  |  sigma²(effect): %.5f\n",
            m0$sigma2[1], m0$sigma2[2]))
cat(sprintf("I² total      : %.1f%%  (between: %.1f%%, within: %.1f%%)\n",
            i2$I2_total, i2$I2_between, i2$I2_within))
cat(sprintf("tau²          : %.5f\n",  i2$tau2_total))
cat(sprintf("Q_E(%d)       : %.2f, p = %.4f\n\n",
            m0$QEdf, m0$QE, m0$QEp))

# Two-level fallback for trim-and-fill / leave-one-out
m0_2L <- rma(yi = yi, vi = vi, data = dat, method = "REML")

# =============================================================================
# MODERATOR ANALYSES
# =============================================================================

# ── MODEL 1: ICRV Regime (H1) ─────────────────────────────────────────────────
cat("─────────────────────────────────────────────────────────────\n")
cat("MODEL 1: ICRV Regime Moderation (H1)\n")
cat("─────────────────────────────────────────────────────────────\n")

icrv_counts <- table(dat$icrv_std)
cat("Effect rows per ICRV regime (standardized codes):\n")
for (code in names(icrv_regime_labels)) {
  n_k <- icrv_counts[code]
  if (!is.na(n_k) && n_k > 0)
    cat(sprintf("  %s (%s): k = %d\n", code, icrv_regime_labels[code], n_k))
}

# Only include regimes with k >= 3 for stable estimates
valid_regimes <- names(icrv_counts[icrv_counts >= 3])
dat_icrv <- dat %>% filter(icrv_std %in% valid_regimes)
dat_icrv$icrv_f <- factor(dat_icrv$icrv_std, levels = valid_regimes)

m1 <- rma.mv(
  yi = yi, V = vi,
  mods   = ~ icrv_f - 1,
  random = ~ 1 | study_id / effect_id,
  data   = dat_icrv, method = "REML"
)

cat("\nICRV regime effects (r scale):\n")
for (i in seq_len(nrow(m1$beta))) {
  code <- sub("icrv_f", "", rownames(m1$beta)[i])
  k_i  <- sum(dat_icrv$icrv_std == code)
  lbl  <- icrv_regime_labels[code]
  cat(sprintf("  ICRV %s (%s)  k=%d  %s\n",
              code, lbl, k_i,
              print_r(m1$beta[i], m1$ci.lb[i], m1$ci.ub[i], m1$pval[i])))
}
cat(sprintf("\nOmnibus Q_M(%d) = %.2f, p = %.4f\n\n",
            m1$QMdf[1], m1$QM, m1$QMp))

# ── MODEL 2: cDAI Continuous (H3) ─────────────────────────────────────────────
cat("─────────────────────────────────────────────────────────────\n")
cat("MODEL 2: cDAI Digital Adoption Moderation (H3, continuous)\n")
cat("─────────────────────────────────────────────────────────────\n")

dat_cdai <- dat %>% filter(!is.na(cdai_num))
m2_lin <- rma.mv(
  yi = yi, V = vi,
  mods   = ~ cdai_num,
  random = ~ 1 | study_id / effect_id,
  data   = dat_cdai, method = "REML"
)
cat(sprintf("cDAI linear trend: b = %.4f, SE = %.4f, p = %.4f  (K=%d)\n",
            m2_lin$beta[2], m2_lin$se[2], m2_lin$pval[2], nrow(dat_cdai)))
cat(sprintf("Intercept (cDAI=0): r = %.3f\n",
            z2r(m2_lin$beta[1])))
cat(sprintf("Omnibus Q_M(%d) = %.2f, p = %.4f\n\n",
            m2_lin$QMdf[1], m2_lin$QM, m2_lin$QMp))

# ── MODEL 3: DPL Phase (H2) ───────────────────────────────────────────────────
cat("─────────────────────────────────────────────────────────────\n")
cat("MODEL 3: DPL Phase Moderation (H2)\n")
cat("─────────────────────────────────────────────────────────────\n")

dpl_labels <- c("1" = "pre-2000", "2" = "2000-2009", "3" = "2010+")
dpl_counts <- table(dat$dpl_std)
cat("Effect rows per DPL phase:\n")
for (code in c("1","2","3")) {
  n_k <- if(!is.na(dpl_counts[code])) dpl_counts[code] else 0
  cat(sprintf("  DPL %s (%s): k = %d\n", code, dpl_labels[code], n_k))
}

m3 <- rma.mv(
  yi = yi, V = vi,
  mods   = ~ dpl_f - 1,
  random = ~ 1 | study_id / effect_id,
  data   = dat, method = "REML"
)

cat("\nDPL phase effects (r scale):\n")
for (i in seq_len(nrow(m3$beta))) {
  code <- sub("dpl_f", "", rownames(m3$beta)[i])
  k_i  <- sum(dat$dpl_std == code, na.rm = TRUE)
  cat(sprintf("  DPL %s (%s)  k=%d  %s\n",
              code, dpl_labels[code], k_i,
              print_r(m3$beta[i], m3$ci.lb[i], m3$ci.ub[i], m3$pval[i])))
}
cat(sprintf("\nOmnibus Q_M(%d) = %.2f, p = %.4f\n\n",
            m3$QMdf[1], m3$QM, m3$QMp))

# ── MODEL 4: Combined Moderators ──────────────────────────────────────────────
cat("─────────────────────────────────────────────────────────────\n")
cat("MODEL 4: Combined Moderators (ICRV + cDAI + DPL)\n")
cat("─────────────────────────────────────────────────────────────\n")

dat_comb <- dat %>%
  filter(icrv_std %in% valid_regimes, !is.na(cdai_num))
dat_comb$icrv_f <- factor(dat_comb$icrv_std, levels = valid_regimes)

m4 <- rma.mv(
  yi = yi, V = vi,
  mods   = ~ icrv_f + cdai_num + dpl_f,
  random = ~ 1 | study_id / effect_id,
  data   = dat_comb, method = "REML"
)
cat(sprintf("Combined model: Q_M(%d) = %.2f, p = %.4f  (K=%d)\n",
            m4$QMdf[1], m4$QM, m4$QMp, nrow(dat_comb)))
R2 <- max(0, (m0$sigma2[1] - m4$sigma2[1]) / m0$sigma2[1])
cat(sprintf("R² analog (sigma²_study reduction): %.1f%%\n\n", R2 * 100))

# =============================================================================
# PUBLICATION BIAS
# =============================================================================
cat("─────────────────────────────────────────────────────────────\n")
cat("PUBLICATION BIAS\n")
cat("─────────────────────────────────────────────────────────────\n")

dat$se_yi <- sqrt(dat$vi)
m_egger <- rma.mv(
  yi = yi, V = vi,
  mods   = ~ se_yi,
  random = ~ 1 | study_id / effect_id,
  data   = dat, method = "REML"
)
cat(sprintf("Egger's (multilevel): b = %.4f, SE = %.4f, p = %.4f\n",
            m_egger$beta[2], m_egger$se[2], m_egger$pval[2]))
cat(if (m_egger$pval[2] < 0.05) "  *** Asymmetry detected ***\n"
    else "  No significant asymmetry\n")

rkt <- ranktest(m0_2L)
cat(sprintf("Rank correlation (Begg): tau = %.3f, p = %.4f\n", rkt$tau, rkt$pval))

taf <- trimfill(m0_2L)
cat(sprintf("Trim-and-fill: k_imputed = %d, adj. r = %.3f [%.3f, %.3f]\n\n",
            taf$k0, z2r(taf$beta[1]), z2r(taf$ci.lb[1]), z2r(taf$ci.ub[1])))

# Vevea-Hedges selection model
tryCatch({
  sel <- selmodel(m0_2L, type = "stepfun", steps = c(0.025, 0.5))
  cat(sprintf("Selection model (Vevea-Hedges): adj. r ≈ %.3f\n\n", z2r(sel$beta[1])))
}, error = function(e) cat("Selection model: not available\n\n"))

fsn_val <- fsn(dat$yi, dat$vi)
cat(sprintf("Fail-safe N (Rosenthal): %d\n\n", fsn_val$fsnum))

# =============================================================================
# SENSITIVITY ANALYSES
# =============================================================================
cat("─────────────────────────────────────────────────────────────\n")
cat("SENSITIVITY ANALYSES\n")
cat("─────────────────────────────────────────────────────────────\n")

loo <- leave1out(m0_2L)
r_loo <- z2r(loo$estimate)
cat(sprintf("Leave-one-out: range r = [%.3f, %.3f]; sign changes = %d / %d\n",
            min(r_loo, na.rm=TRUE), max(r_loo, na.rm=TRUE),
            sum(r_loo < 0, na.rm=TRUE), length(r_loo)))

run_sensitivity <- function(label, filter_expr, note = "") {
  d <- tryCatch(filter(dat, !!rlang::parse_expr(filter_expr)), error = function(e) NULL)
  if (is.null(d) || nrow(d) < 10) {
    cat(sprintf("  %-30s  K < 10 — skipped\n", label))
    return(invisible(NULL))
  }
  m <- tryCatch(
    rma.mv(yi, vi, random = ~ 1 | study_id/effect_id, data = d, method = "REML"),
    error = function(e) NULL
  )
  if (is.null(m)) { cat(sprintf("  %-30s  ERROR\n", label)); return(invisible(NULL)) }
  cat(sprintf("  %-30s  K=%3d  %s\n", label, nrow(d),
              print_r(m$beta[1], m$ci.lb[1], m$ci.ub[1], m$pval[1])))
}

run_sensitivity("Confirmed r (not estimated)", "is_estimated == 0 | is_estimated == '0'")
run_sensitivity("n >= 30",                      "n >= 30")
run_sensitivity("Financial performance only",   "fp_type_std %in% c('financial_perf','ROA','ROE','ROS')")
run_sensitivity("FSTS measure only",            "doi_type_std == 'FSTS'")
run_sensitivity("Panel data only",              "is_panel == 1 | is_panel == '1'")
run_sensitivity("No endogeneity correction",    "endogeneity_corrected == 0 | endogeneity_corrected == '0'")
run_sensitivity("Advanced regime only",         "icrv_std == '1'")
run_sensitivity("Emerging regime only",         "icrv_std == '2'")

m0_dl <- rma(yi = yi, vi = vi, data = dat, method = "DL")
cat(sprintf("  %-30s  K=%3d  %s\n", "DL estimator (two-level)", nrow(dat),
            print_r(m0_dl$beta[1], m0_dl$ci.lb[1], m0_dl$ci.ub[1], m0_dl$pval[1])))

# =============================================================================
# EXPORT RESULTS
# =============================================================================
cat("\n─────────────────────────────────────────────────────────────\n")
cat("EXPORTING RESULTS\n")
cat("─────────────────────────────────────────────────────────────\n")

write_csv(data.frame(
  model         = "Baseline three-level (updated)",
  K_effects     = nrow(dat),
  k_studies     = n_distinct(dat$study_id),
  r_pooled      = round(z2r(m0$beta[1]), 3),
  r_ci_lo       = round(z2r(m0$ci.lb[1]), 3),
  r_ci_hi       = round(z2r(m0$ci.ub[1]), 3),
  pval          = round(m0$pval[1], 4),
  sigma2_study  = round(m0$sigma2[1], 5),
  sigma2_effect = round(m0$sigma2[2], 5),
  I2_total      = i2$I2_total,
  I2_between    = i2$I2_between,
  I2_within     = i2$I2_within,
  Q_total       = round(m0$QE, 2),
  Q_pval        = round(m0$QEp, 4),
  k_trimfill    = taf$k0,
  r_adj_trimfill = round(z2r(taf$beta[1]), 3)
), file.path(results_dir, "table1_baseline.csv"))

# Table 2: ICRV
icrv_out <- lapply(seq_len(nrow(m1$beta)), function(i) {
  code <- sub("icrv_f", "", rownames(m1$beta)[i])
  data.frame(
    icrv_std  = code,
    regime    = icrv_regime_labels[code],
    k         = sum(dat_icrv$icrv_std == code),
    r_est     = round(z2r(m1$beta[i]), 3),
    r_ci_lo   = round(z2r(m1$ci.lb[i]), 3),
    r_ci_hi   = round(z2r(m1$ci.ub[i]), 3),
    pval      = round(m1$pval[i], 4),
    QM        = round(m1$QM, 2),
    QM_pval   = round(m1$QMp, 4)
  )
})
write_csv(do.call(rbind, icrv_out), file.path(results_dir, "table2_icrv.csv"))

# Table 3: cDAI
write_csv(data.frame(
  predictor   = "cDAI (continuous)",
  b           = round(m2_lin$beta[2], 5),
  SE          = round(m2_lin$se[2], 5),
  pval        = round(m2_lin$pval[2], 4),
  QM          = round(m2_lin$QM, 2),
  QM_pval     = round(m2_lin$QMp, 4),
  K           = nrow(dat_cdai)
), file.path(results_dir, "table3_cdai.csv"))

# Table 4: DPL
dpl_out <- lapply(seq_len(nrow(m3$beta)), function(i) {
  code <- sub("dpl_f", "", rownames(m3$beta)[i])
  data.frame(
    dpl_std   = code,
    phase     = dpl_labels[code],
    k         = sum(dat$dpl_std == code, na.rm = TRUE),
    r_est     = round(z2r(m3$beta[i]), 3),
    r_ci_lo   = round(z2r(m3$ci.lb[i]), 3),
    r_ci_hi   = round(z2r(m3$ci.ub[i]), 3),
    pval      = round(m3$pval[i], 4),
    QM        = round(m3$QM, 2),
    QM_pval   = round(m3$QMp, 4)
  )
})
write_csv(do.call(rbind, dpl_out), file.path(results_dir, "table4_dpl.csv"))

# Forest data for Python figure
forest_dat <- dat %>%
  arrange(icrv_std, year) %>%
  mutate(
    r_i   = round(z2r(yi), 3),
    r_lo  = round(z2r(yi - 1.96 * sqrt(vi)), 3),
    r_hi  = round(z2r(yi + 1.96 * sqrt(vi)), 3),
    label = paste(author, year)
  ) %>%
  select(study_id, effect_id, label, r_i, r_lo, r_hi,
         icrv_std, cdai_std, dpl_std, n, doi_type_std, fp_type_std)
write_csv(forest_dat, file.path(results_dir, "forest_data.csv"))

cat("Saved: table1_baseline.csv, table2_icrv.csv, table3_cdai.csv,\n")
cat("       table4_dpl.csv, forest_data.csv\n\n")

cat("=============================================================\n")
cat("ANALYSIS COMPLETE\n")
cat("=============================================================\n")
cat(sprintf("Studies (k)      : %d\n", n_distinct(dat$study_id)))
cat(sprintf("Effects (K)      : %d\n", nrow(dat)))
cat(sprintf("Pooled r         : %.3f [%.3f, %.3f], p = %.4f\n",
            z2r(m0$beta[1]), z2r(m0$ci.lb[1]), z2r(m0$ci.ub[1]), m0$pval[1]))
cat(sprintf("I² total         : %.1f%%\n", i2$I2_total))
cat(sprintf("Pub. bias k_imp  : %d  adj. r = %.3f\n", taf$k0, z2r(taf$beta[1])))
cat(sprintf("Results saved to : %s/\n", results_dir))
