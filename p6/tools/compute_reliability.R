# compute_reliability.R — Inter-coder reliability for P6 meta-analysis
#
# NOT USED IN THE CURRENT STUDY: P6 is single-coder, so no inter-coder
# reliability is reported (disclosed as a pre-registration deviation in the
# manuscript). This script is dormant tooling, retained only for the planned
# formal-search expansion IF a second independent coder becomes available.
#
# Computes Cohen's kappa (categorical) and ICC (continuous) from the
# double-coded reliability subsample.
#
# Input:  reliability_subsample.csv (with coder1_* and coder2_* columns filled)
# Output: Printed results + reliability_report.txt
#
# Usage: Rscript compute_reliability.R [path_to_subsample.csv]
#
# Dependencies: install.packages(c("irr", "psych"))

suppressPackageStartupMessages({
  library(irr)
  library(psych)
})

args <- commandArgs(trailingOnly = TRUE)
input_file <- if (length(args) > 0) args[1] else
  "p6/tools/results/reliability_subsample.csv"

if (!file.exists(input_file)) {
  stop("Input file not found: ", input_file,
       "\nRun 09_select_reliability_subsample.py first.")
}

dat <- read.csv(input_file, stringsAsFactors = FALSE, na.strings = c("", "NA"))
cat("Loaded:", nrow(dat), "double-coded records\n\n")

# ---- Helper: safe kappa --------------------------------------------------
safe_kappa <- function(v1, v2, name) {
  mask <- !is.na(v1) & !is.na(v2)
  if (sum(mask) < 5) {
    cat(sprintf("  %-25s  SKIPPED (n < 5 complete pairs)\n", name))
    return(invisible(NULL))
  }
  mat <- cbind(v1[mask], v2[mask])
  res <- tryCatch(kappa2(mat), error = function(e) NULL)
  if (is.null(res)) {
    cat(sprintf("  %-25s  ERROR computing kappa\n", name))
  } else {
    flag <- if (res$value >= 0.70) "✓ PASS" else "✗ BELOW THRESHOLD"
    cat(sprintf("  %-25s  κ = %.3f  (z = %.2f, p = %.4f)  %s\n",
                name, res$value, res$statistic, res$p.value, flag))
  }
}

# ---- Helper: safe ICC ----------------------------------------------------
safe_icc <- function(v1, v2, name) {
  v1n <- suppressWarnings(as.numeric(v1))
  v2n <- suppressWarnings(as.numeric(v2))
  mask <- !is.na(v1n) & !is.na(v2n)
  if (sum(mask) < 5) {
    cat(sprintf("  %-25s  SKIPPED (n < 5 numeric pairs)\n", name))
    return(invisible(NULL))
  }
  mat <- cbind(v1n[mask], v2n[mask])
  res <- tryCatch(
    icc(mat, model = "twoway", type = "agreement", unit = "single"),
    error = function(e) NULL
  )
  if (is.null(res)) {
    cat(sprintf("  %-25s  ERROR computing ICC\n", name))
  } else {
    flag <- if (res$value >= 0.80) "✓ PASS" else "✗ BELOW THRESHOLD"
    cat(sprintf("  %-25s  ICC = %.3f  [%.3f, %.3f]  F(%d,%d) = %.2f  %s\n",
                name, res$value, res$lbound, res$ubound,
                res$df1, res$df2, res$Fvalue, flag))
  }
}

# ---- 1. Categorical variables (kappa) -----------------------------------
cat("=== CATEGORICAL VARIABLES (Cohen's κ, threshold ≥ 0.70) ===\n")
safe_kappa(dat$coder1_include_flag, dat$coder2_include_flag, "include_flag")
safe_kappa(dat$coder1_icrv,         dat$coder2_icrv,         "icrv")
safe_kappa(dat$coder1_dpl,          dat$coder2_dpl,          "dpl")
cat("\n")

# ---- 2. Continuous variables (ICC) --------------------------------------
cat("=== CONTINUOUS VARIABLES (ICC two-way agreement, threshold ≥ 0.80) ===\n")
safe_icc(dat$coder1_r, dat$coder2_r, "r (effect size)")
safe_icc(dat$coder1_n, dat$coder2_n, "n (sample size)")
cat("\n")

# ---- 3. Agreement rate --------------------------------------------------
if ("agreement_flag" %in% names(dat)) {
  n_agree <- sum(dat$agreement_flag == "Y", na.rm = TRUE)
  n_total <- sum(!is.na(dat$agreement_flag))
  if (n_total > 0) {
    cat(sprintf("Overall agreement (manually coded): %d / %d (%.1f%%)\n\n",
                n_agree, n_total, n_agree / n_total * 100))
  }
}

# ---- 4. Percent agreement by variable -----------------------------------
cat("=== PERCENT AGREEMENT (% exact match) ===\n")
pairs <- list(
  include_flag = c("coder1_include_flag", "coder2_include_flag"),
  icrv         = c("coder1_icrv",         "coder2_icrv"),
  dpl          = c("coder1_dpl",          "coder2_dpl")
)
for (var in names(pairs)) {
  v1 <- dat[[ pairs[[var]][1] ]]
  v2 <- dat[[ pairs[[var]][2] ]]
  mask <- !is.na(v1) & !is.na(v2) & v1 != "" & v2 != ""
  if (sum(mask) == 0) next
  pct <- mean(v1[mask] == v2[mask], na.rm = TRUE) * 100
  cat(sprintf("  %-20s  %.1f%% (%d pairs)\n", var, pct, sum(mask)))
}
cat("\n")

cat("--- Interpretation guide ---\n")
cat("  κ ≥ 0.70 = acceptable for categorical coding (Landis & Koch, 1977)\n")
cat("  ICC ≥ 0.80 = good agreement for continuous coding (Cicchetti, 1994)\n")
cat("  If below threshold: re-calibrate codebook, reconcile, re-code subsample\n")
cat("\n(Only relevant if a second coder joins the formal-search expansion;\n the current single-coder study reports no inter-coder reliability.)\n")
