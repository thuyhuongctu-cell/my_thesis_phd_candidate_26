# P6 Meta-Analysis — Sensitivity Analyses (SA1–SA6)
# Implements sensitivity checks from PRISMA protocol §6.3:
# SA1: Exclude grey literature
# SA2: High-quality studies only (NOS >= 7)
# SA3: Outlier-robust (Winsorize 2.5%/97.5%)
# SA4: Temporal subgroups (pre-2015 vs 2015-2025)
# SA5: Leave-one-study-out (LOSO) influence analysis
# SA6: WBES-only subsample

library(metafor)
library(clubSandwich)

# --- Load data & baseline ---
if (file.exists("p6_sim_dat.rds")) {
  dat <- readRDS("p6_sim_dat.rds")
} else {
  stop("Run 00_simulate_data.R first")
}

baseline <- readRDS("p6_baseline_results.rds")
mu_base  <- baseline$m0$b
ci_base  <- c(baseline$m0$ci.lb, baseline$m0$ci.ub)

cat(sprintf("Baseline: mu=%.3f [%.3f, %.3f]\n\n", mu_base, ci_base[1], ci_base[2]))

run_3level <- function(d) {
  rma.mv(yi, vi,
         random = list(~ 1 | study_id, ~ 1 | study_id / es_id),
         data = d, method = "REML")
}

results_sa <- list()

# SA1: Published studies only
cat("=== SA1: Published studies only ===\n")
dat_sa1 <- dat[dat$published == 1, ]
m_sa1   <- run_3level(dat_sa1)
cat(sprintf("n_ES=%d, mu=%.3f [%.3f, %.3f]\n",
            nrow(dat_sa1), m_sa1$b, m_sa1$ci.lb, m_sa1$ci.ub))
results_sa$SA1 <- m_sa1

# SA2: High-quality studies (NOS >= 7)
cat("\n=== SA2: High-quality studies (NOS >= 7) ===\n")
set.seed(42)
nos_study <- sample(5:9, length(unique(dat$study_id)), replace = TRUE)
dat$nos   <- nos_study[dat$study_id]
dat_sa2   <- dat[dat$nos >= 7, ]
m_sa2     <- run_3level(dat_sa2)
cat(sprintf("n_ES=%d (%.0f%%), mu=%.3f [%.3f, %.3f]\n",
            nrow(dat_sa2), nrow(dat_sa2)/nrow(dat)*100,
            m_sa2$b, m_sa2$ci.lb, m_sa2$ci.ub))
results_sa$SA2 <- m_sa2

# SA3: Outlier-robust (winsorize yi at 2.5th/97.5th percentile)
cat("\n=== SA3: Outlier-robust (winsorized ES) ===\n")
q_low  <- quantile(dat$yi, 0.025)
q_high <- quantile(dat$yi, 0.975)
dat_sa3    <- dat
dat_sa3$yi <- pmin(pmax(dat_sa3$yi, q_low), q_high)
m_sa3      <- run_3level(dat_sa3)
cat(sprintf("Winsorize range: [%.3f, %.3f]\n", q_low, q_high))
cat(sprintf("n_ES=%d, mu=%.3f [%.3f, %.3f]\n",
            nrow(dat_sa3), m_sa3$b, m_sa3$ci.lb, m_sa3$ci.ub))
results_sa$SA3 <- m_sa3

# SA4: Temporal — pre-2015 vs 2015-2025
# Tests whether I->P relationship shifted post-GVC restructuring
cat("\n=== SA4: Temporal subgroups ===\n")
dat_pre  <- dat[dat$pub_year < 2015, ]
dat_post <- dat[dat$pub_year >= 2015, ]
m_pre    <- run_3level(dat_pre)
m_post   <- run_3level(dat_post)
cat(sprintf("Pre-2015:  n_ES=%d, mu=%.3f [%.3f, %.3f]\n",
            nrow(dat_pre),  m_pre$b,  m_pre$ci.lb,  m_pre$ci.ub))
cat(sprintf("2015-2025: n_ES=%d, mu=%.3f [%.3f, %.3f]\n",
            nrow(dat_post), m_post$b, m_post$ci.lb, m_post$ci.ub))
cat(sprintf("ES shift: %.3f (post - pre)\n", m_post$b - m_pre$b))
results_sa$SA4_pre  <- m_pre
results_sa$SA4_post <- m_post

# SA5: Leave-one-study-out (LOSO) influence analysis
cat("\n=== SA5: Leave-one-study-out influence analysis ===\n")
study_ids  <- unique(dat$study_id)
loso_ests  <- numeric(length(study_ids))
loso_ci.lb <- numeric(length(study_ids))
loso_ci.ub <- numeric(length(study_ids))

for (i in seq_along(study_ids)) {
  d_i           <- dat[dat$study_id != study_ids[i], ]
  m_i           <- suppressMessages(run_3level(d_i))
  loso_ests[i]  <- m_i$b
  loso_ci.lb[i] <- m_i$ci.lb
  loso_ci.ub[i] <- m_i$ci.ub
}

loso_range  <- range(loso_ests)
influential <- study_ids[abs(loso_ests - mu_base) > 0.05]
cat(sprintf("LOSO range: [%.3f, %.3f]\n", loso_range[1], loso_range[2]))
cat(sprintf("Baseline: %.3f; max LOSO deviation: %.3f\n",
            mu_base, max(abs(loso_ests - mu_base))))
if (length(influential) > 0) {
  cat(sprintf("Influential studies (|delta| > 0.05): %s\n",
              paste(influential, collapse = ", ")))
} else {
  cat("No highly influential studies detected\n")
}

loso_df <- data.frame(study_id = study_ids, est = loso_ests,
                      ci.lb = loso_ci.lb, ci.ub = loso_ci.ub,
                      delta = loso_ests - mu_base)
results_sa$SA5_loso <- loso_df

# SA6: WBES-only subsample
cat("\n=== SA6: WBES-only subsample ===\n")
set.seed(99)
wbes_study  <- rbinom(length(unique(dat$study_id)), 1, 0.35)
dat$is_wbes <- wbes_study[dat$study_id]
dat_sa6     <- dat[dat$is_wbes == 1, ]

if (length(unique(dat_sa6$study_id)) >= 5) {
  m_sa6 <- run_3level(dat_sa6)
  cat(sprintf("WBES-only: n_studies=%d, n_ES=%d, mu=%.3f [%.3f, %.3f]\n",
              length(unique(dat_sa6$study_id)), nrow(dat_sa6),
              m_sa6$b, m_sa6$ci.lb, m_sa6$ci.ub))
  results_sa$SA6 <- m_sa6
} else {
  cat("Insufficient WBES-only studies — will populate with real data\n")
}

# Summary table
cat("\n=== Sensitivity Analysis Summary ===\n")
sa_names <- c("Baseline", "SA1: Published only", "SA2: NOS>=7",
              "SA3: Winsorized", "SA4: Pre-2015", "SA4: 2015-2025",
              "SA5: LOSO range", "SA6: WBES only")
sa_ests <- c(sprintf("%.3f", mu_base),
             sprintf("%.3f", m_sa1$b), sprintf("%.3f", m_sa2$b),
             sprintf("%.3f", m_sa3$b), sprintf("%.3f", m_pre$b),
             sprintf("%.3f", m_post$b),
             sprintf("[%.3f, %.3f]", loso_range[1], loso_range[2]),
             if (!is.null(results_sa$SA6)) sprintf("%.3f", results_sa$SA6$b) else "N/A")
for (i in seq_along(sa_names)) {
  cat(sprintf("  %-28s %s\n", sa_names[i], sa_ests[i]))
}

saveRDS(results_sa, "p6_sensitivity_results.rds")
cat("\nSensitivity results saved to p6_sensitivity_results.rds\n")
