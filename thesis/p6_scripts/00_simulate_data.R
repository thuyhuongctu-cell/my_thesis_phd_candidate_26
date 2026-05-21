# P6 Meta-Analysis — Simulate synthetic data for framework testing
# Three-level MARA: study level (L3) + effect size level within study (L2) + sampling error (L1)
# Framework: rma.mv(yi, vi, random=list(~1|study_id, ~1|study_id/es_id))

library(metafor)
set.seed(2026)

simulate_meta_data <- function(
  n_studies    = 80,
  mean_es_per_study = 2.5,
  mu           = 0.15,   # overall pooled effect (FSTS->performance)
  tau2_L3      = 0.04,   # between-study variance
  tau2_L2      = 0.02,   # within-study (between-ES) variance
  n_min        = 50,
  n_max        = 800
) {
  # --- Study-level heterogeneity ---
  n_es <- rpois(n_studies, mean_es_per_study - 1) + 1  # at least 1 ES per study
  total_es <- sum(n_es)

  study_id <- rep(seq_len(n_studies), times = n_es)
  es_id    <- seq_len(total_es)

  # True effects: study-level + ES-level deviations
  u_study <- rnorm(n_studies, 0, sqrt(tau2_L3))
  u_es    <- rnorm(total_es, 0, sqrt(tau2_L2))
  theta   <- mu + u_study[study_id] + u_es

  # Sample sizes & sampling variances
  ni <- sample(n_min:n_max, total_es, replace = TRUE)
  vi <- 4 / ni  # approximate variance for r-based effect sizes

  # Observed ES (adds sampling error)
  yi <- theta + rnorm(total_es, 0, sqrt(vi))

  # --- Moderators (coded per PRISMA protocol §4) ---
  # I-measure type: FSTS / export dummy / entropy
  i_type_study <- sample(c("FSTS", "export_dummy", "entropy"), n_studies, replace = TRUE,
                         prob = c(0.55, 0.30, 0.15))
  i_type <- i_type_study[study_id]

  # P-measure type: labor productivity / ROA / sales growth
  p_type_study <- sample(c("labor_productivity", "ROA", "sales_growth"), n_studies, replace = TRUE,
                         prob = c(0.45, 0.35, 0.20))
  p_type <- p_type_study[study_id]

  # ICRV regime: Advanced / Upper-middle / Emerging / Frontier / SIDS
  icrv_study <- sample(c("Advanced", "Upper_middle", "Emerging", "Frontier", "SIDS"),
                       n_studies, replace = TRUE, prob = c(0.15, 0.15, 0.35, 0.30, 0.05))
  icrv <- icrv_study[study_id]

  # Publication year: 2000-2025
  pub_year_study <- sample(2000:2025, n_studies, replace = TRUE)
  pub_year <- pub_year_study[study_id]

  # Publication status: journal vs working paper (for publication bias)
  published_study <- rbinom(n_studies, 1, 0.75)
  published <- published_study[study_id]

  data.frame(
    study_id = study_id,
    es_id    = es_id,
    yi       = yi,
    vi       = vi,
    ni       = ni,
    i_type   = i_type,
    p_type   = p_type,
    icrv     = icrv,
    pub_year = pub_year,
    published = published,
    stringsAsFactors = FALSE
  )
}

# Generate dataset
dat <- simulate_meta_data()

cat("=== Simulated meta-analysis dataset ===\n")
cat(sprintf("Studies (L3): %d\n", length(unique(dat$study_id))))
cat(sprintf("Effect sizes (L2): %d\n", nrow(dat)))
cat(sprintf("Mean ES per study: %.1f\n", mean(table(dat$study_id))))
cat(sprintf("yi range: [%.3f, %.3f]\n", min(dat$yi), max(dat$yi)))
cat(sprintf("vi range: [%.5f, %.5f]\n", min(dat$vi), max(dat$vi)))
cat("\nI-type distribution:\n")
print(table(dat$i_type))
cat("\nICRV distribution:\n")
print(table(dat$icrv))
cat("\nP-type distribution:\n")
print(table(dat$p_type))

# Quick sanity: run baseline model
m_sanity <- rma.mv(yi, vi,
                   random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
                   data = dat, method = "REML", verbose = FALSE)
cat(sprintf("\nSanity check — pooled estimate: %.3f [%.3f, %.3f], p=%.4f\n",
            m_sanity$b, m_sanity$ci.lb, m_sanity$ci.ub, m_sanity$pval))
cat(sprintf("tau2 L3=%.4f, L2=%.4f\n", m_sanity$sigma2[1], m_sanity$sigma2[2]))

# Save for downstream scripts
saveRDS(dat, "p6_sim_dat.rds")
cat("\nData saved to p6_sim_dat.rds\n")
