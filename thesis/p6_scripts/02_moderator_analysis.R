# P6 Meta-Analysis — Moderator Analysis
# Tests three sets of moderators from PRISMA protocol §4:
#   (1) ICRV regime (institutional context)
#   (2) I-measure type (FSTS / export dummy / entropy)
#   (3) P-measure type (labor productivity / ROA / sales growth)
# Method: rma.mv with moderator in mods argument (meta-regression)

library(metafor)
library(clubSandwich)

# --- Load data ---
if (file.exists("p6_sim_dat.rds")) {
  dat <- readRDS("p6_sim_dat.rds")
} else {
  stop("Run 00_simulate_data.R first")
}

# Recode categorical moderators as factors
dat$icrv    <- factor(dat$icrv,
                      levels = c("Emerging", "Advanced", "Upper_middle", "Frontier", "SIDS"))
dat$i_type  <- factor(dat$i_type, levels = c("FSTS", "export_dummy", "entropy"))
dat$p_type  <- factor(dat$p_type, levels = c("labor_productivity", "ROA", "sales_growth"))

# ============================================================
# MODERATOR SET 1: ICRV institutional regime
# Ref: CĐ2 H4 — "phân nhóm con thể chế"
# Prediction: effects differ across regimes (institutional moderation)
# ============================================================
m_icrv <- rma.mv(
  yi, vi,
  mods   = ~ icrv,
  random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
  data   = dat, method = "REML"
)
cat("=== M_ICRV: Institutional regime moderator ===\n")
cat(sprintf("Omnibus test (ICRV): QM(df=%d) = %.2f, p = %.4f\n",
            m_icrv$m - 1, m_icrv$QM, m_icrv$QMp))
print(coef(summary(m_icrv)))

# Cluster-robust test
robust_icrv <- coef_test(m_icrv, vcov = "CR2", cluster = dat$study_id)
cat("\nCluster-robust (CR2):\n")
print(robust_icrv)

# ============================================================
# MODERATOR SET 2: I-measure type
# Ref: PRISMA protocol §4.2 — moderator coding M2
# Prediction: FSTS > export_dummy > entropy (fine-grained > coarse)
# ============================================================
m_itype <- rma.mv(
  yi, vi,
  mods   = ~ i_type,
  random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
  data   = dat, method = "REML"
)
cat("\n=== M_ITYPE: I-measure type moderator ===\n")
cat(sprintf("Omnibus test (I-type): QM(df=%d) = %.2f, p = %.4f\n",
            m_itype$m - 1, m_itype$QM, m_itype$QMp))
print(coef(summary(m_itype)))

# ============================================================
# MODERATOR SET 3: P-measure type
# Ref: PRISMA protocol §4.3 — moderator coding M3
# ============================================================
m_ptype <- rma.mv(
  yi, vi,
  mods   = ~ p_type,
  random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
  data   = dat, method = "REML"
)
cat("\n=== M_PTYPE: P-measure type moderator ===\n")
cat(sprintf("Omnibus test (P-type): QM(df=%d) = %.2f, p = %.4f\n",
            m_ptype$m - 1, m_ptype$QM, m_ptype$QMp))
print(coef(summary(m_ptype)))

# ============================================================
# COMBINED MODEL: ICRV + I-type + P-type
# ============================================================
m_combined <- rma.mv(
  yi, vi,
  mods   = ~ icrv + i_type + p_type,
  random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
  data   = dat, method = "REML"
)
cat("\n=== M_COMBINED: ICRV + I-type + P-type ===\n")
cat(sprintf("Omnibus test (all mods): QM(df=%d) = %.2f, p = %.4f\n",
            m_combined$m - 1, m_combined$QM, m_combined$QMp))
cat(sprintf("Residual heterogeneity: tau2_L3=%.4f, tau2_L2=%.4f\n",
            m_combined$sigma2[1], m_combined$sigma2[2]))
R2 <- 1 - sum(m_combined$sigma2) / sum(m_icrv$sigma2)
cat(sprintf("Pseudo-R2 vs intercept-only (approx): %.1f%%\n", max(0, R2) * 100))
print(coef(summary(m_combined)))

# ============================================================
# INTERACTION: ICRV × I-type (theory test for H2-H3)
# ============================================================
m_interact <- rma.mv(
  yi, vi,
  mods   = ~ icrv * i_type,
  random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
  data   = dat, method = "REML"
)
cat(sprintf("\nICRV × I-type interaction omnibus: QM(df=%d) = %.2f, p = %.4f\n",
            m_interact$m - 1, m_interact$QM, m_interact$QMp))

# Save
saveRDS(list(m_icrv = m_icrv, m_itype = m_itype, m_ptype = m_ptype,
             m_combined = m_combined, m_interact = m_interact),
        "p6_moderator_results.rds")
cat("\nModerator results saved to p6_moderator_results.rds\n")
