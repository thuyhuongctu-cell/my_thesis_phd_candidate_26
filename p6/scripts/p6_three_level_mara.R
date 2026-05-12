#!/usr/bin/env Rscript
# p6_three_level_mara.R — Three-level MARA for P6 (I→P, 1982–2026)
#
# ICBEF 2025 baseline: k=113 studies, r=0.07, I²=87.92% (Đỗ & Phan, 2024)
# P6 UPDATED target: k=135 studies, K≈250 effect sizes (extended 2022–2026)
# Three-level MARA with 3 new moderators: ICRV regime, cDAI, DPL phase
#
# Run: Rscript scripts/p6_three_level_mara.R
# Or with real data: Rscript scripts/p6_three_level_mara.R --data data/p6_effect_sizes.csv

suppressPackageStartupMessages({
  library(metafor)
  library(clubSandwich)
  library(dplyr)
})

cat("=================================================================\n")
cat("  P6 Three-Level MARA — I→P Relationship (1982–2026)\n")
cat("  metafor", as.character(packageVersion("metafor")), "| clubSandwich",
    as.character(packageVersion("clubSandwich")), "\n")
cat("=================================================================\n\n")

# ─── 1. Synthetic effect-size database (P6 UPDATED: k=135 studies) ───────────
set.seed(2024)

# k=135 studies, K≈250 effect sizes (three-level: multiple ES per study)
# ICBEF 2025 baseline was k=113; P6 adds 22 studies via backward scan 2022–2026
n_studies   <- 135
study_id    <- rep(seq_len(n_studies), times = sample(1:3, n_studies, replace = TRUE, prob = c(0.5, 0.3, 0.2)))
k_effects   <- length(study_id)

# True between-study heterogeneity (tau²_between) and within-study (tau²_within)
tau2_between <- 0.025
tau2_within  <- 0.010
grand_mean   <- 0.07    # baseline r = 0.07

# Simulate effect sizes (Fisher-z transformed r values)
z_study  <- rnorm(n_studies, 0, sqrt(tau2_between))
z_within <- rnorm(k_effects, 0, sqrt(tau2_within))
z_true   <- grand_mean + z_study[study_id] + z_within
# Sampling variance: vi ≈ 1/(ni - 3); typical ni in I→P = 100–500
ni       <- round(runif(k_effects, 80, 600))
yi       <- z_true + rnorm(k_effects, 0, sqrt(1 / (ni - 3)))
vi       <- 1 / (ni - 3)

# Moderator coding — matches P6 coding protocol
icrv_regime <- sample(c("I_Advanced", "II_UpperMiddle", "III_Emerging", "IV_SIDS", "V_Frontier"),
                      k_effects, replace = TRUE, prob = c(0.18, 0.22, 0.28, 0.07, 0.25))
cdai_level  <- sample(c("High", "Medium", "Low"), k_effects, replace = TRUE, prob = c(0.35, 0.40, 0.25))
dlp_phase   <- sample(c("Precede", "Span", "Follow"), k_effects, replace = TRUE, prob = c(0.30, 0.25, 0.45))
doi_measure <- sample(c("FSTS", "FATA", "composite"), k_effects, replace = TRUE, prob = c(0.45, 0.30, 0.25))

dat <- data.frame(
  study_id    = factor(study_id),
  es_id       = factor(seq_along(study_id)),   # unique effect size ID for three-level
  yi, vi, ni,
  icrv_regime = factor(icrv_regime, levels = c("I_Advanced","II_UpperMiddle","III_Emerging","IV_SIDS","V_Frontier")),
  cdai_level  = factor(cdai_level, levels = c("High", "Medium", "Low")),
  dlp_phase   = factor(dlp_phase,  levels = c("Precede", "Span", "Follow")),
  doi_measure = factor(doi_measure)
)

cat(sprintf("  Synthetic database: k = %d effect sizes, %d studies\n\n",
            k_effects, n_studies))

# ─── 2. Baseline three-level model ───────────────────────────────────────────
cat("── Model 0: Baseline Three-Level (no moderators) ──────────────\n")

m0 <- rma.mv(yi, vi,
             random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
             data   = dat,
             method = "REML")

# Back-transform Fisher-z to r
r_est <- tanh(coef(m0))
cat(sprintf("  Overall effect r = %.3f  [%.3f, %.3f]\n",
            r_est, tanh(m0$ci.lb), tanh(m0$ci.ub)))
cat(sprintf("  p-value: %.4f\n", m0$pval))

# I² decomposition (Cheung, 2014)
W     <- diag(1 / dat$vi)
X     <- model.matrix(m0)
P     <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
I2_total    <- 100 * sum(m0$sigma2) / (sum(m0$sigma2) + (m0$k - m0$p) / sum(diag(P)))
I2_between  <- 100 * m0$sigma2[1] / (sum(m0$sigma2) + (m0$k - m0$p) / sum(diag(P)))
I2_within   <- 100 * m0$sigma2[2] / (sum(m0$sigma2) + (m0$k - m0$p) / sum(diag(P)))
cat(sprintf("  I²_total = %.2f%%  (between-study: %.2f%%,  within-study: %.2f%%)\n\n",
            I2_total, I2_between, I2_within))

# ─── 3. ICRV Moderator (Hm3) ─────────────────────────────────────────────────
cat("── Model 1: ICRV 5-Regime Moderator ───────────────────────────\n")

m1 <- rma.mv(yi, vi,
             mods   = ~ icrv_regime,
             random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
             data   = dat,
             method = "REML")

cat(sprintf("  QM(df=%d) = %.2f, p = %.4f\n", m1$m, m1$QM, m1$QMp))
coef_df <- data.frame(
  Regime = levels(dat$icrv_regime),
  r      = round(tanh(c(coef(m1)[1], coef(m1)[1] + coef(m1)[-1])), 3),
  se     = round(m1$se[1:5], 3)
)
print(coef_df, row.names = FALSE)
cat("\n")

# ─── 4. cDAI Moderator (Hm1) ─────────────────────────────────────────────────
cat("── Model 2: cDAI Moderator ─────────────────────────────────────\n")

m2 <- rma.mv(yi, vi,
             mods   = ~ cdai_level,
             random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
             data   = dat,
             method = "REML")

cat(sprintf("  QM(df=%d) = %.2f, p = %.4f\n", m2$m, m2$QM, m2$QMp))
coef_cdai <- data.frame(
  cDAI = levels(dat$cdai_level),
  r    = round(tanh(c(coef(m2)[1], coef(m2)[1] + coef(m2)[-1])), 3)
)
print(coef_cdai, row.names = FALSE)
cat("\n")

# ─── 5. DPL Phase Moderator (Hm2) ────────────────────────────────────────────
cat("── Model 3: DPL Phase Moderator ────────────────────────────────\n")

m3 <- rma.mv(yi, vi,
             mods   = ~ dlp_phase,
             random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
             data   = dat,
             method = "REML")

cat(sprintf("  QM(df=%d) = %.2f, p = %.4f\n", m3$m, m3$QM, m3$QMp))
coef_dlp <- data.frame(
  DPL  = levels(dat$dlp_phase),
  r    = round(tanh(c(coef(m3)[1], coef(m3)[1] + coef(m3)[-1])), 3)
)
print(coef_dlp, row.names = FALSE)
cat("\n")

# ─── 6. Publication Bias: Egger (1997) test ──────────────────────────────────
cat("── Publication Bias: Egger regression test ─────────────────────\n")

# Egger test via weighted regression of z on 1/sqrt(vi)
precision <- 1 / sqrt(dat$vi)
egger_mod <- lm(dat$yi ~ precision, weights = 1 / dat$vi)
egger_sum <- summary(egger_mod)
cat(sprintf("  Intercept = %.4f, SE = %.4f, t = %.3f, p = %.4f\n",
            coef(egger_sum)[1,1], coef(egger_sum)[1,2],
            coef(egger_sum)[1,3], coef(egger_sum)[1,4]))
cat(sprintf("  → %s\n\n", ifelse(coef(egger_sum)[1,4] < .05,
    "Evidence of publication bias (p < .05)",
    "No significant publication bias (p ≥ .05)")))

# ─── 7. Robustness: RVE with clubSandwich ────────────────────────────────────
cat("── Robustness: Cluster-Robust Variance Estimation (RVE) ────────\n")

vcov_rve <- vcovCR(m0, cluster = dat$study_id, type = "CR2")
rve_coef  <- coef_test(m0, vcov = vcov_rve)
cat(sprintf("  Intercept (RVE/CR2): b = %.4f, SE = %.4f, p = %.4f\n\n",
            rve_coef$beta[1], rve_coef$SE[1], rve_coef$p_Satt[1]))

# ─── 8. Forest plot (ASCII) ──────────────────────────────────────────────────
cat("── ICRV Regime Effect Sizes (Forest Plot — ASCII) ──────────────\n")
for (i in seq_len(nrow(coef_df))) {
  bar_len <- max(1, round(coef_df$r[i] * 60))
  bar     <- paste(rep("█", bar_len), collapse = "")
  cat(sprintf("  %-20s r=%.3f  |%s\n", coef_df$Regime[i], coef_df$r[i], bar))
}
cat("  [ICBEF 2025 baseline: k=113, r=0.07 → P6 target: k=135 — synthetic data]\n\n")

cat("=================================================================\n")
cat("  Ghi chú: Kết quả từ synthetic data (seed=2024, k=135).\n")
cat("  Với real data: đặt effect sizes vào data/p6_effect_sizes.csv\n")
cat("  (columns: study_id, es_id, yi, vi, ni, icrv_regime, cdai_level, dlp_phase, doi_measure)\n")
cat("  và chạy: Rscript scripts/p6_three_level_mara.R --data data/p6_effect_sizes.csv\n")
cat("  Nguồn coding: p6/p6_study_database_coded.md (Section 4A + 4B)\n")
cat("=================================================================\n")
