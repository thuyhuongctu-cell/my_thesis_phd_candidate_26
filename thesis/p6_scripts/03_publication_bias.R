# P6 Meta-Analysis — Publication Bias Assessment
# Three complementary approaches:
#   (1) Egger's test (funnel plot asymmetry via weighted regression)
#   (2) Trim-and-fill (Duval & Tweedie, 2000)
#   (3) PET-PEESE (Stanley & Doucouliagos, 2014)
# Note: For multilevel models use study-level aggregation for Egger/trim-fill
# Ref: Rodgers & Pustejovsky (2021) Psych Methods

library(metafor)

# --- Load data ---
if (file.exists("p6_sim_dat.rds")) {
  dat <- readRDS("p6_sim_dat.rds")
} else {
  stop("Run 00_simulate_data.R first")
}

# ============================================================
# APPROACH 1: Egger's test (multilevel extension)
# ============================================================
dat$sei <- sqrt(dat$vi)

m_egger <- rma.mv(
  yi, vi,
  mods   = ~ sei,
  random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
  data   = dat, method = "REML"
)
cat("=== Egger's test (multilevel) ===\n")
cat(sprintf("Intercept (bias-corrected pooled ES): %.3f [%.3f, %.3f]\n",
            coef(m_egger)[1], m_egger$ci.lb[1], m_egger$ci.ub[1]))
cat(sprintf("Slope (Egger): %.3f, SE=%.3f, p=%.4f\n",
            coef(m_egger)[2], sqrt(vcov(m_egger)[2,2]), m_egger$pval[2]))
if (m_egger$pval[2] < 0.10) {
  cat("  [WARNING] Funnel plot asymmetry detected (p < 0.10)\n")
} else {
  cat("  [OK] No significant funnel plot asymmetry\n")
}

# ============================================================
# APPROACH 2: Trim-and-fill (study-level aggregation)
# ============================================================
cat("\n=== Trim-and-fill (study-level aggregation) ===\n")

study_agg <- aggregate(
  cbind(yi = yi, vi = vi, ni = ni) ~ study_id,
  data = dat,
  FUN  = function(x) mean(x)
)

m_agg <- rma(yi, vi, data = study_agg, method = "REML")
cat(sprintf("Study-level pooled ES: %.3f [%.3f, %.3f]\n",
            m_agg$b, m_agg$ci.lb, m_agg$ci.ub))

tf_result <- trimfill(m_agg)
cat(sprintf("Trim-and-fill: %d studies trimmed\n", tf_result$k0))
cat(sprintf("Adjusted pooled ES: %.3f [%.3f, %.3f]\n",
            tf_result$b, tf_result$ci.lb, tf_result$ci.ub))
cat(sprintf("ES change after trim-and-fill: %.3f\n",
            tf_result$b - m_agg$b))

png("p6_funnel_plot.png", width = 800, height = 600)
funnel(tf_result, main = "P6 Funnel Plot (study-level aggregation)",
       xlab = "Fisher's Z (I->P effect size)")
dev.off()
cat("Funnel plot saved to p6_funnel_plot.png\n")

# ============================================================
# APPROACH 3: PET-PEESE (Stanley & Doucouliagos, 2014)
# ============================================================
cat("\n=== PET-PEESE ===\n")

# Define SE for study-level aggregated data
study_agg$sei <- sqrt(study_agg$vi)

m_pet <- rma(yi, vi, mods = ~ sei, data = study_agg, method = "REML")
pet_intercept <- coef(m_pet)[1]
pet_p         <- m_pet$pval[1]
cat(sprintf("PET intercept: %.3f [%.3f, %.3f], p=%.4f\n",
            pet_intercept, m_pet$ci.lb[1], m_pet$ci.ub[1], pet_p))

if (pet_p < 0.05) {
  m_peese <- rma(yi, vi, mods = ~ vi, data = study_agg, method = "REML")
  peese_intercept <- coef(m_peese)[1]
  cat(sprintf("PEESE intercept (bias-corrected): %.3f [%.3f, %.3f]\n",
              peese_intercept, m_peese$ci.lb[1], m_peese$ci.ub[1]))
  cat("  [Using PEESE estimate — PET significant]\n")
  pet_peese_estimate <- peese_intercept
} else {
  cat("  [Using PET estimate — PET not significant]\n")
  pet_peese_estimate <- pet_intercept
}
cat(sprintf("PET-PEESE bias-corrected pooled ES: %.3f\n", pet_peese_estimate))

# Caveat: with high heterogeneity (I^2 > 80%), PET-PEESE estimates can be
# biased toward null (Stanley & Doucouliagos, 2014). Report alongside
# trim-and-fill as a directional sensitivity, not a point estimate.

# ============================================================
# APPROACH 4: Vevea-Hedges 3-parameter step-function selection model
# (Vevea & Hedges 1995; Hedges & Vevea 1996; Vevea & Woods 2005)
# Model-based bias correction: estimates the publication selection function
# directly, complementing the non-parametric trim-and-fill.
# ============================================================
cat("\n=== Vevea-Hedges step-function selection model ===\n")

# Use metafor::selmodel with type="stepfun" and standard p-value cutpoints.
# Steps: (0, .025] one-tailed significant positive, (.025, .500] non-significant,
# (.500, 1.0] one-tailed significant negative.
# Weights are relative; w[1] = 1 (reference category for significant positives).
m_baseline_studyagg <- rma(yi, vi, data = study_agg, method = "REML")
vh_result <- tryCatch(
  selmodel(m_baseline_studyagg, type = "stepfun", alternative = "greater",
           steps = c(.025, .500)),
  error = function(e) { cat("  [warn] selmodel failed:", conditionMessage(e), "\n"); NULL }
)
if (!is.null(vh_result)) {
  vh_intercept <- coef(vh_result)$beta[1]
  vh_lb <- vh_result$ci.lb
  vh_ub <- vh_result$ci.ub
  cat(sprintf("Vevea-Hedges adjusted pooled ES: %.3f [%.3f, %.3f]\n",
              vh_intercept, vh_lb, vh_ub))
  cat(sprintf("Selection weights: w[<.025]=1.000 (ref); w[.025-.500]=%.3f; w[>.500]=%.3f\n",
              coef(vh_result)$delta[1], coef(vh_result)$delta[2]))
  vh_lrt_p <- pchisq(vh_result$LRT, df = vh_result$LRTdf, lower.tail = FALSE)
  cat(sprintf("Likelihood-ratio test vs. no-selection model: chi2=%.2f, df=%d, p=%.4f\n",
              vh_result$LRT, vh_result$LRTdf, vh_lrt_p))
} else {
  vh_intercept <- NA
}

# ============================================================
# SUMMARY TABLE
# ============================================================
cat("\n=== Publication Bias Summary ===\n")
cat(sprintf("%-32s %s\n", "Method", "Bias-corrected ES"))
cat(sprintf("%-32s %.3f\n", "Baseline (three-level)", readRDS("p6_baseline_results.rds")$m0$b))
cat(sprintf("%-32s %.3f\n", "Egger (intercept)", coef(m_egger)[1]))
cat(sprintf("%-32s %.3f\n", "Trim-and-fill", tf_result$b))
cat(sprintf("%-32s %.3f\n", "PET-PEESE", pet_peese_estimate))
if (!is.na(vh_intercept)) {
  cat(sprintf("%-32s %.3f\n", "Vevea-Hedges selection", vh_intercept))
}

saveRDS(list(m_egger = m_egger, tf_result = tf_result,
             m_pet = m_pet, pet_peese_estimate = pet_peese_estimate,
             vh_result = vh_result),
        "p6_pubias_results.rds")
cat("\nPublication bias results saved to p6_pubias_results.rds\n")
