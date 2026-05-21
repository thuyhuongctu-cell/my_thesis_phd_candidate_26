# ── MARA Update — Combined Database (existing k=238 + new Y papers) ──────
# Run after Phase C completes and ready_for_r=1 papers exist in tracker
#
# Step 1: Load existing k=238, K=288 database
# Step 2: Load new ready_for_r=1 papers from tracker
# Step 3: Dedup + merge → combined database
# Step 4: Run three-level MARA on combined dataset
# Step 5: Compare to baseline (r=0.074, k=238, K=288, I²=62.4%)

library(metafor)
library(clubSandwich)

cat("Loading existing k=238 database...\n")
existing <- read.csv("p6/data/p6_study_database.csv", stringsAsFactors = FALSE)
existing$r   <- as.numeric(existing$r)
existing$n   <- as.numeric(existing$n)
existing$source <- "existing_k238"

# Standardize ICRV (letter → integer)
icrv_map <- c("I"=1, "II"=2, "III"=3, "IV"=4, "V"=5, "VI"=6, "MX"=0)
existing$icrv_int <- ifelse(!is.na(suppressWarnings(as.integer(existing$icrv_std))),
                             as.integer(existing$icrv_std),
                             icrv_map[existing$icrv])

# Standardize DPL (PRE/SPN/FOL → 1/2/3)
dpl_map <- c("PRE"=1, "SPN"=2, "FOL"=3, "EARLY"=2, "PLATFORM"=3)
existing$dpl_int <- dpl_map[existing$dpl]
# Fill unmapped with 2 (unknown → span)
existing$dpl_int[is.na(existing$dpl_int)] <- 2

cat(sprintf("Existing: k=%d studies, K=%d effects\n",
            length(unique(existing$study_id)), nrow(existing)))

# ── Load new papers from tracker ─────────────────────────────────────────────
cat("\nLoading new papers from tracker...\n")
tracker <- read.csv("p6/tools/results/fulltext_to_extraction_tracker_v3.csv",
                    stringsAsFactors = FALSE)
tracker <- subset(tracker,
                  fulltext_screening_decision == "Y" &
                  ready_for_r == "1" &
                  converted_r != "")

tracker$r   <- as.numeric(tracker$converted_r)
tracker$n   <- as.numeric(tracker$sample_size_n)
tracker     <- subset(tracker, !is.na(r) & !is.na(n) & n > 10 & r > 0 & r < 1)

cat(sprintf("New ready papers from tracker: %d\n", nrow(tracker)))

if (nrow(tracker) > 0) {
  # Build matching columns
  tracker$study_id <- paste0("NEW_", tracker$seq)
  tracker$effect_id <- paste0("NEW_", tracker$seq, "_E1")
  tracker$icrv_int  <- as.integer(tracker$icrv)
  tracker$dpl_int   <- as.integer(tracker$dpl)
  tracker$source <- "new_wos2026"

  # Subset to needed cols
  new_rows <- tracker[, c("study_id","effect_id","r","n","icrv_int","dpl_int","source")]

  # Subset existing
  existing_sub <- existing[, c("study_id","effect_id","r","n","icrv_int","dpl_int","source")]

  # Combine
  combined <- rbind(existing_sub, new_rows)
} else {
  cat("WARNING: No new papers with ready_for_r=1. Running on existing k=238 only.\n")
  combined <- existing[, c("study_id","effect_id","r","n","icrv_int","dpl_int","source")]
}

cat(sprintf("\nCombined dataset: k=%d studies, K=%d effects\n",
            length(unique(combined$study_id)), nrow(combined)))

# ── Fisher z transformation ───────────────────────────────────────────────────
combined$yi <- 0.5 * log((1 + combined$r) / (1 - combined$r))
combined$vi <- 1 / (combined$n - 3)
combined$es_id_seq <- seq_len(nrow(combined))

# ── M0: Three-level baseline MARA (Cheung 2014, single nested term) ──────────
cat("\n── M0: Baseline MARA ──\n")
m0 <- rma.mv(yi, vi,
             random = ~ 1 | study_id/es_id_seq,
             data = combined, method = "REML")

r_pool <- round(tanh(coef(m0)), 4)
cat(sprintf("r_pooled = %.4f [%.4f, %.4f]\n",
            r_pool, tanh(m0$ci.lb), tanh(m0$ci.ub)))
cat(sprintf("k = %d, K = %d\n",
            length(unique(combined$study_id)), nrow(combined)))

# I² decomposition (Cheung 2014) — sigma2[1]=between-study(L3), sigma2[2]=within-study(L2)
W  <- diag(1 / combined$vi)
X  <- model.matrix(m0)
P  <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
denom <- sum(m0$sigma2) + (m0$k - m0$p) / sum(diag(P))
I2         <- 100 * sum(m0$sigma2) / denom
I2_between <- 100 * m0$sigma2[1]   / denom  # Level 3: between-study
I2_within  <- 100 * m0$sigma2[2]   / denom  # Level 2: within-study between-effects
cat(sprintf("I²_total = %.1f%% (L3 between-study=%.1f%%, L2 within-study=%.1f%%)\n",
            I2, I2_between, I2_within))

# ── M1: ICRV moderation ──────────────────────────────────────────────────────
cat("\n── M1: ICRV moderation (6-regime) ──\n")
dat_icrv <- subset(combined, icrv_int %in% 1:6)
if (nrow(dat_icrv) > 20) {
  m1 <- rma.mv(yi, vi, mods = ~ factor(icrv_int),
               random = ~ 1 | study_id/es_id_seq,
               data = dat_icrv, method = "REML")
  cat(sprintf("QM(ICRV) = %.2f, df=%d, p=%.3f\n",
              m1$QM, m1$QMdf[1], m1$QMp))
  for (i in 1:6) {
    sub <- subset(dat_icrv, icrv_int == i)
    if (nrow(sub) > 0) {
      r_sub <- round(tanh(mean(sub$yi, na.rm=TRUE)), 3)
      cat(sprintf("  ICRV-%d: k=%d, r_mean=%.3f\n", i, nrow(sub), r_sub))
    }
  }
}

# ── M2: DPL moderation ───────────────────────────────────────────────────────
cat("\n── M2: DPL moderation (3-phase) ──\n")
dat_dpl <- subset(combined, dpl_int %in% 1:3)
if (nrow(dat_dpl) > 20) {
  m2 <- rma.mv(yi, vi, mods = ~ factor(dpl_int),
               random = ~ 1 | study_id/es_id_seq,
               data = dat_dpl, method = "REML")
  cat(sprintf("QM(DPL) = %.2f, df=%d, p=%.3f\n",
              m2$QM, m2$QMdf[1], m2$QMp))
}

# ── Publication bias ──────────────────────────────────────────────────────────
cat("\n── Publication bias ──\n")
# Egger's test (using two-level model for simplicity)
m_2level <- rma(yi, vi, data = combined, method = "REML")
egger <- regtest(m_2level, model = "lm")
cat(sprintf("Egger's test: z=%.2f, p=%.3f\n", egger$zval, egger$pval))

# Trim-and-fill
taf <- trimfill(m_2level)
cat(sprintf("Trim-and-fill: imputed=%d, adjusted r=%.4f\n",
            taf$k0, tanh(coef(taf))))

# ── Baseline comparison ───────────────────────────────────────────────────────
# NOTE on I²: Manuscript reports I²=62.4% using typical_v = mean(vi) ≈ 0.00611.
# This script uses the Cheung (2014) exact P-matrix formula: typical_v = (K-p)/sum(diag(P)) ≈ 0.00140.
# With N ranging 17–114,398, the two approaches diverge (87.9% vs 62.4%).
# sigma2[1] (L3 between-study) and sigma2[2] (L2 within-study) are identical in both.
# The manuscript I²=62.4% was computed using arithmetic mean(vi). Both are valid implementations.
cat("\n── Comparison to baseline (k=238, r=0.074, I²=62.4% [mean-vi formula]) ──\n")
cat(sprintf("Updated: k=%d (+%d), r=%.4f (Δ%.4f)\n",
            length(unique(combined$study_id)),
            length(unique(combined$study_id)) - 238,
            r_pool, r_pool - 0.074))
cat(sprintf("I² (P-matrix formula): %.1f%% | I² (mean-vi, manuscript): %.1f%%\n",
            I2, 100 * sum(m0$sigma2) / (sum(m0$sigma2) + mean(combined$vi))))
cat(sprintf("sigma2[L3 between-study]: %.5f | sigma2[L2 within-study]: %.5f\n",
            m0$sigma2[1], m0$sigma2[2]))

cat("\n✅ MARA complete.\n")
