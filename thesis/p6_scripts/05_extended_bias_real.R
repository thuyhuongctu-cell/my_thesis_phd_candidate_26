#!/usr/bin/env Rscript
# 05_extended_bias_real.R — Run PET-PEESE + Vevea-Hedges on the real k=238 corpus
# (not the simulated data). Outputs numbers that can be quoted in §4.6 of P6.
#
# Usage:  Rscript 05_extended_bias_real.R
# Reads:  ../../p6/data/p6_study_database.csv

suppressMessages(library(metafor))

dat_raw <- read.csv("../../p6/data/p6_study_database.csv", stringsAsFactors = FALSE)
# Keep only rows with usable r and n
dat <- subset(dat_raw, !is.na(r) & !is.na(n) & n > 3 &
              r > -0.999 & r < 0.999 & !is.na(include_flag) & include_flag == 1)
cat(sprintf("Loaded %d effect sizes from %d unique studies\n",
            nrow(dat), length(unique(dat$study_id))))

# Fisher-z transform
dat$yi <- 0.5 * log((1 + dat$r) / (1 - dat$r))   # Fisher z
dat$vi <- 1 / (dat$n - 3)                         # sampling variance of z
dat$sei <- sqrt(dat$vi)

# Three-level baseline (consistent with §4.2)
m0 <- rma.mv(yi, vi, random = list(~ 1 | study_id, ~ 1 | effect_id),
             data = dat, method = "REML")
pooled_z <- coef(m0)
pooled_r <- (exp(2*pooled_z) - 1) / (exp(2*pooled_z) + 1)
cat(sprintf("\nBaseline three-level pooled z=%.4f, r=%.4f [%.4f, %.4f]\n",
            pooled_z, pooled_r,
            (exp(2*m0$ci.lb)-1)/(exp(2*m0$ci.lb)+1),
            (exp(2*m0$ci.ub)-1)/(exp(2*m0$ci.ub)+1)))

# Study-level aggregation for funnel-based tests
study_agg <- aggregate(cbind(yi, vi) ~ study_id, data = dat, FUN = mean)
study_agg$sei <- sqrt(study_agg$vi)
m_study <- rma(yi, vi, data = study_agg, method = "REML")
cat(sprintf("\nStudy-aggregated baseline pooled r=%.4f [%.4f, %.4f]\n",
            (exp(2*coef(m_study))-1)/(exp(2*coef(m_study))+1),
            (exp(2*m_study$ci.lb)-1)/(exp(2*m_study$ci.lb)+1),
            (exp(2*m_study$ci.ub)-1)/(exp(2*m_study$ci.ub)+1)))

# Trim-and-fill (reference for §4.6)
tf <- trimfill(m_study, side = "left")
cat(sprintf("\nTrim-and-fill: k=%d imputed; adjusted pooled r=%.4f [%.4f, %.4f]\n",
            tf$k0, (exp(2*coef(tf))-1)/(exp(2*coef(tf))+1),
            (exp(2*tf$ci.lb)-1)/(exp(2*tf$ci.lb)+1),
            (exp(2*tf$ci.ub)-1)/(exp(2*tf$ci.ub)+1)))

# PET-PEESE
cat("\n=== PET-PEESE ===\n")
m_pet <- rma(yi, vi, mods = ~ sei, data = study_agg, method = "REML")
pet_b <- coef(m_pet)[1]
pet_p <- m_pet$pval[1]
cat(sprintf("PET intercept (z scale): %.4f [%.4f, %.4f], p=%.4f\n",
            pet_b, m_pet$ci.lb[1], m_pet$ci.ub[1], pet_p))
if (pet_p < 0.05) {
  m_peese <- rma(yi, vi, mods = ~ vi, data = study_agg, method = "REML")
  peese_b <- coef(m_peese)[1]
  cat(sprintf("PEESE intercept (z scale; bias-corrected): %.4f [%.4f, %.4f]\n",
              peese_b, m_peese$ci.lb[1], m_peese$ci.ub[1]))
  petp <- peese_b
  petp_lb <- m_peese$ci.lb[1]; petp_ub <- m_peese$ci.ub[1]
} else {
  petp <- pet_b; petp_lb <- m_pet$ci.lb[1]; petp_ub <- m_pet$ci.ub[1]
}
petp_r <- (exp(2*petp) - 1) / (exp(2*petp) + 1)
cat(sprintf("PET-PEESE bias-corrected r=%.4f [%.4f, %.4f]\n",
            petp_r, (exp(2*petp_lb)-1)/(exp(2*petp_lb)+1),
            (exp(2*petp_ub)-1)/(exp(2*petp_ub)+1)))

# Vevea-Hedges step-function selection model
cat("\n=== Vevea-Hedges 3-parameter step-function ===\n")
vh <- tryCatch(
  selmodel(m_study, type = "stepfun", alternative = "greater",
           steps = c(.025, .500)),
  error = function(e) { cat("[fail]", conditionMessage(e), "\n"); NULL }
)
if (!is.null(vh)) {
  vh_z <- coef(vh)$beta[1]
  vh_r <- (exp(2*vh_z) - 1) / (exp(2*vh_z) + 1)
  vh_lrt_p <- pchisq(vh$LRT, df = vh$LRTdf, lower.tail = FALSE)
  cat(sprintf("Vevea-Hedges adjusted r=%.4f [%.4f, %.4f]\n",
              vh_r, (exp(2*vh$ci.lb)-1)/(exp(2*vh$ci.lb)+1),
              (exp(2*vh$ci.ub)-1)/(exp(2*vh$ci.ub)+1)))
  cat(sprintf("Selection weights: w[(.025,.500]]=%.3f; w[(.500,1.0]]=%.3f\n",
              coef(vh)$delta[1], coef(vh)$delta[2]))
  cat(sprintf("LRT vs. no-selection model: chi2=%.3f, df=%d, p=%.4f\n",
              vh$LRT, vh$LRTdf, vh_lrt_p))
}

cat("\n--- Summary line for §4.6 ---\n")
cat(sprintf("Trim-and-fill r=%.3f; PET-PEESE r=%.3f; Vevea-Hedges r=%.3f\n",
            (exp(2*coef(tf))-1)/(exp(2*coef(tf))+1), petp_r,
            if (!is.null(vh)) vh_r else NA))
