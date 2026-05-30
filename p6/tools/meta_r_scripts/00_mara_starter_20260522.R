# ── R STARTER CODE — Three-Level MARA ──────────────────────────────
# Two modes:
#   MODE = "tracker"  — reads tracker_v3 (live extraction, ready_for_r=1)
#   MODE = "database" — reads p6_study_database_v2 (merged k=259, K=309)

library(metafor)
library(clubSandwich)

MODE <- "database"   # switch to "tracker" during active extraction

# ── Load data ────────────────────────────────────────────────────────
if (MODE == "tracker") {
  dat <- read.csv("p6/tools/results/fulltext_to_extraction_tracker_v3.csv",
                  stringsAsFactors = FALSE)
  dat <- subset(dat, ready_for_r == "1" & converted_r != "")
  dat$r   <- as.numeric(dat$converted_r)
  dat$n   <- as.numeric(dat$sample_size_n)
  dat     <- subset(dat, !is.na(r) & !is.na(n) & n > 10)
  dat$yi  <- 0.5 * log((1 + dat$r) / (1 - dat$r))
  dat$vi  <- 1 / (dat$n - 3)
  dat$study_id  <- paste0(dat$authors, "_", dat$year)
  dat$effect_id <- seq_len(nrow(dat))
  dat$icrv_var  <- dat$icrv
  dat$dpl_var   <- dat$dpl
} else {
  dat <- read.csv("p6/data/p6_study_database_v2.csv",
                  stringsAsFactors = FALSE)
  dat <- subset(dat, !is.na(fisher_z) & !is.na(vi) & vi > 0)
  dat$yi        <- dat$fisher_z
  dat$effect_id <- dat$effect_id
  dat$icrv_var  <- dat$icrv_std
  dat$dpl_var   <- dat$dpl_std
}

cat("Mode:", MODE, "| k =", length(unique(dat$study_id)),
    "| K =", nrow(dat), "\n")

# ── M0: Three-level baseline ─────────────────────────────────────────
m0 <- rma.mv(yi, vi,
             random = ~ 1 | study_id/effect_id,
             data = dat, method = "REML")

r_pooled <- tanh(as.numeric(coef(m0)))
ci_lo    <- tanh(m0$ci.lb)
ci_hi    <- tanh(m0$ci.ub)
cat(sprintf("r = %.4f [%.4f, %.4f]  p = %.4f\n",
            r_pooled, ci_lo, ci_hi, m0$pval))

# I² decomposition (Cheung 2014)
W  <- diag(1 / dat$vi)
X  <- model.matrix(m0)
P  <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
tv <- (m0$k - m0$p) / sum(diag(P))
I2_total   <- 100 * sum(m0$sigma2) / (sum(m0$sigma2) + tv)
I2_between <- 100 * m0$sigma2[1] / (sum(m0$sigma2) + tv)
I2_within  <- 100 * m0$sigma2[2] / (sum(m0$sigma2) + tv)
cat(sprintf("I2 = %.1f%%  (between=%.1f%%  within=%.1f%%)\n",
            I2_total, I2_between, I2_within))

# ── M1: ICRV moderation ──────────────────────────────────────────────
icrv_levels <- sort(unique(dat$icrv_var[!is.na(dat$icrv_var)]))
if (length(icrv_levels) >= 2) {
  dat_icrv <- subset(dat, !is.na(icrv_var))
  m1 <- rma.mv(yi, vi, mods = ~ factor(icrv_var),
               random = ~ 1 | study_id/effect_id,
               data = dat_icrv, method = "REML")
  cat(sprintf("ICRV  QM(%d) = %.3f  p = %.4f\n", m1$m, m1$QM, m1$QMp))
}

# ── M2: DPL phase ────────────────────────────────────────────────────
dpl_levels <- sort(unique(dat$dpl_var[!is.na(dat$dpl_var)]))
if (length(dpl_levels) >= 2) {
  dat_dpl <- subset(dat, !is.na(dpl_var))
  m2 <- rma.mv(yi, vi, mods = ~ factor(dpl_var),
               random = ~ 1 | study_id/effect_id,
               data = dat_dpl, method = "REML")
  cat(sprintf("DPL   QM(%d) = %.3f  p = %.4f\n", m2$m, m2$QM, m2$QMp))
}

# ── Publication bias (Egger regression) ──────────────────────────────
precision <- 1 / sqrt(dat$vi)
egger     <- lm(dat$yi ~ precision, weights = 1 / dat$vi)
egger_p   <- summary(egger)$coefficients[1, 4]
egger_b   <- summary(egger)$coefficients[1, 1]
cat(sprintf("Egger b = %.4f  p = %.4f\n", egger_b, egger_p))

# ── Cluster-robust variance estimation ───────────────────────────────
vcov_rve <- vcovCR(m0, cluster = dat$study_id, type = "CR2")
rve_res  <- coef_test(m0, vcov = vcov_rve)
cat("RVE intercept p =", round(rve_res$p_Satt[1], 4), "\n")
