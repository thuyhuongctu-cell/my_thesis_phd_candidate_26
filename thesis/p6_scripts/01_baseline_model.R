# P6 Meta-Analysis — Baseline Three-Level Model
# Model: rma.mv(yi, vi, random=list(~1|study_id, ~1|study_id/es_id))
# REML estimator; clubSandwich robust SE for cluster-robust inference
# Ref: Cheung (2014) MBR; Van den Noortgate et al. (2013); Assink & Wibbelink (2016)

library(metafor)
library(clubSandwich)

# --- Load data (real or simulated) ---
if (file.exists("data/p6_coded_effects.rds")) {
  dat <- readRDS("data/p6_coded_effects.rds")
  cat("Using real coded data\n")
} else if (file.exists("p6_sim_dat.rds")) {
  dat <- readRDS("p6_sim_dat.rds")
  cat("Using simulated data (run 00_simulate_data.R first)\n")
} else {
  stop("No data found. Run 00_simulate_data.R or place real data at data/p6_coded_effects.rds")
}

cat(sprintf("\nDataset: %d effect sizes from %d studies\n",
            nrow(dat), length(unique(dat$study_id))))

# ============================================================
# MODEL 0: Intercept-only three-level model (baseline)
# ============================================================
m0 <- rma.mv(
  yi, vi,
  random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
  data   = dat,
  method = "REML"
)
cat("\n=== M0: Three-level baseline ===\n")
print(summary(m0))

# --- Variance partitioning ---
I2_total <- sum(m0$sigma2) / (sum(m0$sigma2) + mean(dat$vi)) * 100
I2_L3    <- m0$sigma2[1] / (sum(m0$sigma2) + mean(dat$vi)) * 100
I2_L2    <- m0$sigma2[2] / (sum(m0$sigma2) + mean(dat$vi)) * 100

cat(sprintf("\nVariance partition:\n"))
cat(sprintf("  tau2 L3 (between-study):  %.4f  [I2_L3 = %.1f%%]\n", m0$sigma2[1], I2_L3))
cat(sprintf("  tau2 L2 (within-study):   %.4f  [I2_L2 = %.1f%%]\n", m0$sigma2[2], I2_L2))
cat(sprintf("  I2 total:  %.1f%%\n", I2_total))
cat(sprintf("  Ratio L3/(L3+L2): %.2f  [>0.5 suggests study-level heterogeneity dominates]\n",
            m0$sigma2[1] / sum(m0$sigma2)))

# --- Cluster-robust inference (clubSandwich) ---
# CR2 estimator — recommended for small clusters (< 40 studies)
if (length(unique(dat$study_id)) < 40) {
  cat("\n[WARNING] < 40 studies — use CR2 robust SE (clubSandwich)\n")
}
robust_m0 <- coef_test(m0, vcov = "CR2", cluster = dat$study_id)
cat("\n=== Cluster-robust SE (CR2, clustered by study_id) ===\n")
print(robust_m0)

# --- Likelihood ratio tests for variance components ---
m0_noL3 <- rma.mv(yi, vi,
                   random = list(~ 1 | study_id / es_id),
                   data = dat, method = "ML")
m0_ML   <- rma.mv(yi, vi,
                   random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
                   data = dat, method = "ML")
lrt_L3 <- anova(m0_noL3, m0_ML)
cat(sprintf("\nLRT H0: tau2_L3=0 — chi2=%.3f, df=%d, p=%.4f\n",
            lrt_L3$LRT, lrt_L3$p.LRT, lrt_L3$p.LRT))

# ============================================================
# MODEL 1: Two-level for comparison (no nesting)
# ============================================================
m1 <- rma.mv(yi, vi,
             random = ~ 1 | es_id,
             data = dat, method = "REML")
cat("\n=== M1: Two-level (no study nesting) for comparison ===\n")
cat(sprintf("  mu = %.3f [%.3f, %.3f]\n", m1$b, m1$ci.lb, m1$ci.ub))
cat(sprintf("  tau2 = %.4f\n", m1$sigma2))

cat(sprintf("\nPooled estimate (M0 three-level): %.3f [%.3f, %.3f]\n",
            m0$b, m0$ci.lb, m0$ci.ub))

# ============================================================
# Save results
# ============================================================
results_baseline <- list(
  m0           = m0,
  m1           = m1,
  robust_m0    = robust_m0,
  I2_total     = I2_total,
  I2_L3        = I2_L3,
  I2_L2        = I2_L2,
  lrt_L3       = lrt_L3
)
saveRDS(results_baseline, "p6_baseline_results.rds")
cat("\nResults saved to p6_baseline_results.rds\n")
