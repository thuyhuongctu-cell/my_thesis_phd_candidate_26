# ── R STARTER CODE — Three-Level MARA ──────────────────────────────
# Run after extraction is complete and converted_r filled in tracker
# MODE is patched at runtime by the mara_run.yml workflow via sed.

library(metafor)
library(clubSandwich)

MODE <- "database"   # patched by workflow: "database" or "tracker"

# ── Load data (mode-specific) ────────────────────────────────────────
if (MODE == "tracker") {
  cat("=== MODE: tracker (tracker_v3.csv, ready_for_r=1) ===\n")
  dat_raw <- read.csv("p6/tools/results/fulltext_to_extraction_tracker_v3.csv",
                      stringsAsFactors = FALSE)
  dat_raw <- subset(dat_raw, ready_for_r == "1" & converted_r != "")
  dat <- data.frame(
    study_id = paste0(dat_raw$authors, "_", dat_raw$year),
    es_id    = seq_len(nrow(dat_raw)),
    r        = as.numeric(dat_raw$converted_r),
    n        = as.numeric(dat_raw$sample_size_n),
    icrv     = dat_raw$icrv,
    dpl      = dat_raw$dpl,
    author   = dat_raw$authors,
    year     = dat_raw$year,
    stringsAsFactors = FALSE
  )
} else {
  # Prefer v2 if it exists (more coded studies)
  db_path <- if (file.exists("p6/data/p6_study_database_v2.csv")) {
    "p6/data/p6_study_database_v2.csv"
  } else {
    "p6/data/p6_study_database.csv"
  }
  cat(sprintf("=== MODE: database (%s) ===\n", db_path))
  dat_raw <- read.csv(db_path, stringsAsFactors = FALSE)
  dat_raw <- subset(dat_raw, include_flag == "1")
  dat <- data.frame(
    study_id = dat_raw$study_id,
    es_id    = dat_raw$effect_id,
    r        = as.numeric(dat_raw$r),
    n        = as.numeric(dat_raw$n),
    icrv     = dat_raw$icrv_std,
    dpl      = dat_raw$dpl,
    author   = dat_raw$author,
    year     = dat_raw$year,
    stringsAsFactors = FALSE
  )
}

# ── Clean & transform ────────────────────────────────────────────────
dat <- subset(dat, !is.na(r) & !is.na(n) & n > 10 & abs(r) < 1)

# Fisher z transformation
dat$yi <- 0.5 * log((1 + dat$r) / (1 - dat$r))
dat$vi <- 1 / (dat$n - 3)

cat("Rows after cleaning:", nrow(dat), "\n")
cat("Unique studies:", length(unique(dat$study_id)), "\n")

if (nrow(dat) < 5) {
  cat("ERROR: Too few rows for meta-analysis. Exiting.\n")
  quit(status = 1)
}

# ── M0: Three-level baseline ─────────────────────────────────────────
m0 <- rma.mv(yi, vi,
             random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
             data = dat, method = "REML")

cat("\n=== M0 Baseline ===\n")
print(summary(m0))
cat("k =", length(unique(dat$study_id)),
    "| K =", nrow(dat),
    "| r =", round(tanh(coef(m0)), 3),
    "| 95% CI [", round(tanh(m0$ci.lb), 3), ",", round(tanh(m0$ci.ub), 3), "]\n")

# ── I² decomposition (Cheung 2014) ───────────────────────────────────
W  <- diag(1 / dat$vi)
X  <- model.matrix(m0)
P  <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
denom <- sum(m0$sigma2) + (m0$k - m0$p) / sum(diag(P))
I2_total   <- 100 * sum(m0$sigma2) / denom
I2_between <- 100 * m0$sigma2[1] / denom
I2_within  <- 100 * m0$sigma2[2] / denom
cat(sprintf("I² total=%.1f%% | between=%.1f%% | within=%.1f%%\n",
            I2_total, I2_between, I2_within))

# ── M1: ICRV moderator ───────────────────────────────────────────────
if (length(unique(dat$icrv)) > 1) {
  cat("\n=== M1: ICRV moderator ===\n")
  m1_icrv <- rma.mv(yi, vi,
                    mods = ~ factor(icrv),
                    random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
                    data = dat, method = "REML")
  cat("QM(icrv) =", round(m1_icrv$QM, 2), "df =", m1_icrv$m,
      "p =", round(m1_icrv$QMp, 4), "\n")
  print(coef(summary(m1_icrv)))
} else {
  cat("ICRV moderator skipped: only one ICRV level in data\n")
}

# ── M2: DPL phase moderator ──────────────────────────────────────────
if (length(unique(dat$dpl)) > 1) {
  cat("\n=== M2: DPL moderator ===\n")
  m2_dpl <- rma.mv(yi, vi,
                   mods = ~ factor(dpl),
                   random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
                   data = dat, method = "REML")
  cat("QM(dpl)  =", round(m2_dpl$QM, 2), "df =", m2_dpl$m,
      "p =", round(m2_dpl$QMp, 4), "\n")
  print(coef(summary(m2_dpl)))
} else {
  cat("DPL moderator skipped: only one DPL level in data\n")
}

# ── Publication bias (Egger's regression test) ───────────────────────
cat("\n=== Publication Bias ===\n")
precision <- 1 / sqrt(dat$vi)
egger     <- lm(dat$yi ~ precision, weights = 1 / dat$vi)
p_egger   <- summary(egger)$coefficients[1, 4]
cat("Egger's test: b0 =",
    round(summary(egger)$coefficients[1, 1], 3),
    " p =", round(p_egger, 4),
    ifelse(p_egger < 0.05, " [ASYMMETRIC]", " [OK]"), "\n")

# ── Cluster-robust variance estimation ──────────────────────────────
cat("\n=== Cluster-Robust SEs (CR2) ===\n")
vcov_rve <- vcovCR(m0, cluster = dat$study_id, type = "CR2")
print(coef_test(m0, vcov = vcov_rve))

cat("\n=== MARA COMPLETE ===\n")
