# ── R STARTER CODE — Three-Level MARA ──────────────────────────────
# Run after extraction is complete and converted_r filled in tracker

library(metafor)
library(clubSandwich)

# Load data (filter to ready_for_r=1)
dat <- read.csv("p6/tools/results/fulltext_to_extraction_tracker_v3.csv",
                stringsAsFactors = FALSE)
dat <- subset(dat, ready_for_r == "1" & converted_r != "")

# Prepare effect sizes
dat$r   <- as.numeric(dat$converted_r)
dat$n   <- as.numeric(dat$sample_size_n)
dat     <- subset(dat, !is.na(r) & !is.na(n) & n > 10)

# Fisher z transformation
dat$yi  <- 0.5 * log((1 + dat$r) / (1 - dat$r))  # or use escalc
dat$vi  <- 1 / (dat$n - 3)

# Study ID + effect ID
dat$study_id <- paste0(dat$authors, "_", dat$year)
dat$es_id    <- seq_len(nrow(dat))

# ── M0: Three-level baseline (Cheung 2014 single nested term) ────────
m0 <- rma.mv(yi, vi,
             random = ~ 1 | study_id/es_id,
             data = dat, method = "REML")

cat("k =", length(unique(dat$study_id)),
    "| K =", nrow(dat),
    "| r =", round(tanh(coef(m0)), 3), "\n")

# I² decomposition (Cheung 2014)
W  <- diag(1 / dat$vi)
X  <- model.matrix(m0)
P  <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
I2 <- 100 * sum(m0$sigma2) / (sum(m0$sigma2) + (m0$k - m0$p) / sum(diag(P)))

# ── M1–M4: Moderators ───────────────────────────────────────────────
m1_icrv <- rma.mv(yi, vi, mods = ~ factor(icrv),
                  random = ~ 1 | study_id/es_id,
                  data = dat, method = "REML")

m2_dpl  <- rma.mv(yi, vi, mods = ~ factor(dpl),
                  random = ~ 1 | study_id/es_id,
                  data = dat, method = "REML")

# ── Publication bias ────────────────────────────────────────────────
m0_2level <- rma(yi, vi, data = dat, method = "REML")  # 2-level for Egger/trim-fill
egger_rt  <- regtest(m0_2level, predictor = "sei")     # manuscript-comparable
cat("Egger regtest: z =", round(egger_rt$zval, 3), "p =", round(egger_rt$pval, 3), "\n")
taf <- trimfill(m0_2level, estimator = "L0")
cat("Trim-fill: k0 =", taf$k0, "adj_r =", round(tanh(coef(taf)), 4), "\n")

# ── Cluster-robust variance estimation ─────────────────────────────
vcov_rve <- vcovCR(m0, cluster = dat$study_id, type = "CR2")
coef_test(m0, vcov = vcov_rve)
