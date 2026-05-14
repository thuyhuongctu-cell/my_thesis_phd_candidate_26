# =============================================================================
# Paper 7 – Asian Capstone (49 economies)
# Comprehensive R Analysis: Pooled + Country FE + Moderation
# Script: 06_p7_run_models_R.R
# Author: PhD Dissertation Replication
# Date:   2026-05-14
# R:      4.3.3
# =============================================================================

suppressPackageStartupMessages({
  library(dplyr)
  library(lmtest)
  library(sandwich)
  library(broom)
})

cat("=============================================================\n")
cat("  Paper 7 – Asian Capstone: Comprehensive R Analysis\n")
cat("=============================================================\n\n")

# ---------------------------------------------------------------------------
# 0. Paths
# ---------------------------------------------------------------------------
DATA_PATH    <- "/home/user/PAPERS_IN_PHD_2026/data_wbes/p7/p7_pooled_clean.csv"
RESULTS_DIR  <- "/home/user/PAPERS_IN_PHD_2026/p7/replication/results"
dir.create(RESULTS_DIR, showWarnings = FALSE, recursive = TRUE)

COEF_OUT     <- file.path(RESULTS_DIR, "p7_R_coefs.csv")
TP_OUT       <- file.path(RESULTS_DIR, "p7_R_turning_points.csv")

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
cat("--- 1. Loading data ---\n")
raw <- read.csv(DATA_PATH, stringsAsFactors = FALSE)
cat(sprintf("Raw rows: %d  |  Columns: %d\n", nrow(raw), ncol(raw)))

# Verify required columns
required_cols <- c(
  "country", "year", "icrv_group", "icrv_label",
  "firm_id", "ln_labor_prod", "fsts", "exporter",
  "fsts_pct", "dai_website", "dai_epay", "dai_epay_pct",
  "dai_z", "tci_cert", "tci_foreign_tech", "tci_z",
  "mgr_experience", "mgr_female", "female_owner",
  "foreign_own_pct", "firm_age", "ln_size",
  "isic_sector", "wstrict"
)
missing_cols <- setdiff(required_cols, names(raw))
if (length(missing_cols) > 0) {
  cat("WARNING – Missing columns:", paste(missing_cols, collapse = ", "), "\n")
} else {
  cat("All required columns present.\n")
}

# ---------------------------------------------------------------------------
# 2. Prepare analysis dataset
# ---------------------------------------------------------------------------
cat("\n--- 2. Preparing analysis dataset ---\n")

df <- raw %>%
  filter(!is.na(ln_labor_prod), !is.na(fsts)) %>%
  mutate(
    fsts_mean = mean(fsts, na.rm = TRUE),
    fsts_c    = fsts - mean(fsts, na.rm = TRUE),
    fsts_c2   = fsts_c^2,
    country_f     = factor(country),
    year_f        = factor(year),
    isic_sector_f = factor(isic_sector)
  )

cat(sprintf("Analysis sample (non-missing ln_labor_prod & fsts): %d rows\n", nrow(df)))
cat(sprintf("  Countries:  %d\n", n_distinct(df$country)))
cat(sprintf("  Years:      %d\n", n_distinct(df$year)))
cat(sprintf("  Sectors:    %d\n", n_distinct(df$isic_sector)))
cat(sprintf("  ICRV groups: %d\n", n_distinct(df$icrv_label)))
cat(sprintf("  Mean fsts (grand):  %.4f\n", df$fsts_mean[1]))
cat(sprintf("  SD   fsts:          %.4f\n", sd(df$fsts, na.rm = TRUE)))
cat(sprintf("  Min  fsts:          %.4f\n", min(df$fsts, na.rm = TRUE)))
cat(sprintf("  Max  fsts:          %.4f\n", max(df$fsts, na.rm = TRUE)))

# Complete-controls subset (for M6-M8)
controls_full <- c("ln_size", "firm_age", "foreign_own_pct",
                   "fsts_c", "fsts_c2", "tci_z", "dai_z",
                   "mgr_experience", "mgr_female",
                   "isic_sector", "year", "country")
df_fe <- df %>%
  filter(complete.cases(across(all_of(intersect(controls_full, names(df))))))

cat(sprintf("FE subset (complete controls): %d rows\n", nrow(df_fe)))

# ---------------------------------------------------------------------------
# 3. Helper: coeftest with HC1 robust SEs
# ---------------------------------------------------------------------------
robust_coeftest <- function(model) {
  coeftest(model, vcov = vcovHC(model, type = "HC1"))
}

# Helper: extract tidy table with robust SEs
tidy_robust <- function(model, model_name) {
  ct    <- robust_coeftest(model)
  n_obs <- length(model$residuals)   # nobs() on an lm object
  tidy(ct) %>%
    mutate(
      model = model_name,
      n_obs = n_obs
    )
}

# ---------------------------------------------------------------------------
# 4. Models M0–M5: Pooled (no country FE)
# ---------------------------------------------------------------------------
cat("\n--- 3. Fitting pooled models M0–M5 ---\n")

# Base controls (re-used in all models)
base_rhs <- "ln_size + firm_age + foreign_own_pct + factor(isic_sector) + factor(year)"

cat("  Fitting M0 ...\n")
M0 <- lm(
  as.formula(paste("ln_labor_prod ~", base_rhs)),
  data = df
)

cat("  Fitting M1 ...\n")
M1 <- lm(
  as.formula(paste("ln_labor_prod ~ fsts_c +", base_rhs)),
  data = df
)

cat("  Fitting M2 ...\n")
M2 <- lm(
  as.formula(paste("ln_labor_prod ~ fsts_c + fsts_c2 +", base_rhs)),
  data = df
)

cat("  Fitting M3 ...\n")
M3 <- lm(
  as.formula(paste("ln_labor_prod ~ fsts_c + fsts_c2 + tci_z +", base_rhs)),
  data = df
)

cat("  Fitting M4 ...\n")
M4 <- lm(
  as.formula(paste("ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z +", base_rhs)),
  data = df
)

cat("  Fitting M5 ...\n")
M5 <- lm(
  as.formula(
    paste("ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z",
          "+ mgr_experience + mgr_female +", base_rhs)
  ),
  data = df
)

# ---------------------------------------------------------------------------
# 5. Models M6–M8: With country FE
# ---------------------------------------------------------------------------
cat("\n--- 4. Fitting country-FE models M6–M8 ---\n")

fe_rhs <- paste(base_rhs, "+ factor(country)")

cat("  Fitting M6 ...\n")
M6 <- lm(
  as.formula(paste("ln_labor_prod ~ fsts_c + fsts_c2 +", fe_rhs)),
  data = df_fe
)

cat("  Fitting M7 ...\n")
M7 <- lm(
  as.formula(paste("ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z +", fe_rhs)),
  data = df_fe
)

cat("  Fitting M8 ...\n")
M8 <- lm(
  as.formula(
    paste("ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z",
          "+ mgr_experience + mgr_female +", fe_rhs)
  ),
  data = df_fe
)

# ---------------------------------------------------------------------------
# 6. Turning-point calculations and Lind-Mehlum check
# ---------------------------------------------------------------------------
turning_point <- function(model, df_used, model_name) {
  ct      <- robust_coeftest(model)
  coefs   <- ct[, 1]
  ses     <- ct[, 2]
  pvals   <- ct[, 4]

  b1_name <- "fsts_c"
  b2_name <- "fsts_c2"

  if (!(b1_name %in% names(coefs)) || !(b2_name %in% names(coefs))) {
    return(
      data.frame(
        model      = model_name,
        b1         = NA, b2 = NA,
        tp_centered = NA,
        tp_raw     = NA,
        fsts_min   = NA,
        fsts_max   = NA,
        tp_in_range = NA,
        shape      = "no_quadratic",
        stringsAsFactors = FALSE
      )
    )
  }

  b1   <- coefs[b1_name]
  b2   <- coefs[b2_name]
  mean_fsts <- mean(df_used$fsts, na.rm = TRUE)

  tp_centered <- -b1 / (2 * b2)
  tp_raw      <- tp_centered + mean_fsts

  fsts_min <- min(df_used$fsts, na.rm = TRUE)
  fsts_max <- max(df_used$fsts, na.rm = TRUE)
  in_range <- (tp_raw >= fsts_min) & (tp_raw <= fsts_max)

  shape <- if (b2 < 0) "inverted-U" else "U-shaped"

  data.frame(
    model       = model_name,
    b1          = round(b1, 6),
    b2          = round(b2, 6),
    tp_centered = round(tp_centered, 6),
    tp_raw      = round(tp_raw, 6),
    fsts_min    = round(fsts_min, 6),
    fsts_max    = round(fsts_max, 6),
    tp_in_range = in_range,
    shape       = shape,
    stringsAsFactors = FALSE
  )
}

cat("\n--- 5. Turning-point analysis (M2 and M7) ---\n")
tp_m2 <- turning_point(M2, df,    "M2_pooled")
tp_m7 <- turning_point(M7, df_fe, "M7_country_FE")

print_tp <- function(tp) {
  cat(sprintf(
    "  [%s]  b1=%.5f  b2=%.5f  TP(raw)=%.4f  Range=[%.4f, %.4f]  In-range=%s  Shape=%s\n",
    tp$model, tp$b1, tp$b2, tp$tp_raw,
    tp$fsts_min, tp$fsts_max,
    ifelse(tp$tp_in_range, "YES", "NO"),
    tp$shape
  ))
  if (tp$tp_in_range) {
    cat("  --> Lind-Mehlum condition satisfied: TP is inside the data range.\n")
  } else {
    cat("  --> Lind-Mehlum condition NOT satisfied: TP is outside the data range.\n")
  }
}

print_tp(tp_m2)
print_tp(tp_m7)

# ---------------------------------------------------------------------------
# 7. ICRV moderation: M2 by icrv_label group
# ---------------------------------------------------------------------------
cat("\n--- 6. ICRV moderation: M2 by icrv_label ---\n")
icrv_groups <- sort(unique(df$icrv_label[!is.na(df$icrv_label)]))
cat("  ICRV groups found:", paste(icrv_groups, collapse = " | "), "\n\n")

icrv_tp_list <- list()

for (grp in icrv_groups) {
  df_grp <- df %>% filter(icrv_label == grp)
  n_grp  <- nrow(df_grp)

  if (n_grp < 50) {
    cat(sprintf("  [%s]  n=%d – skipping (too few obs)\n", grp, n_grp))
    next
  }

  # Re-center fsts within group
  df_grp <- df_grp %>%
    mutate(
      fsts_c  = fsts - mean(fsts, na.rm = TRUE),
      fsts_c2 = fsts_c^2
    )

  m_grp <- tryCatch(
    lm(
      as.formula(paste("ln_labor_prod ~ fsts_c + fsts_c2 +", base_rhs)),
      data = df_grp
    ),
    error = function(e) NULL
  )

  if (is.null(m_grp)) {
    cat(sprintf("  [%s]  Model failed to converge\n", grp))
    next
  }

  tp_grp <- turning_point(m_grp, df_grp, paste0("ICRV_", grp))
  icrv_tp_list[[grp]] <- tp_grp

  ct_grp <- tryCatch(robust_coeftest(m_grp), error = function(e) NULL)
  b1_p <- if (!is.null(ct_grp) && "fsts_c"  %in% rownames(ct_grp)) ct_grp["fsts_c",  4] else NA
  b2_p <- if (!is.null(ct_grp) && "fsts_c2" %in% rownames(ct_grp)) ct_grp["fsts_c2", 4] else NA

  cat(sprintf(
    "  [%-12s]  n=%6d  b1=%.5f (p=%.3f)  b2=%.5f (p=%.3f)  TP=%.4f  In-range=%s  Shape=%s\n",
    grp, n_grp,
    tp_grp$b1, ifelse(is.na(b1_p), NA, b1_p),
    tp_grp$b2, ifelse(is.na(b2_p), NA, b2_p),
    tp_grp$tp_raw,
    ifelse(tp_grp$tp_in_range, "YES", "NO"),
    tp_grp$shape
  ))
}

icrv_tp_df <- if (length(icrv_tp_list) > 0) {
  bind_rows(icrv_tp_list)
} else {
  data.frame()
}

# ---------------------------------------------------------------------------
# 8. DAI moderation: joint F-test of interaction terms in M4 spec
# ---------------------------------------------------------------------------
cat("\n--- 7. DAI moderation: joint F-test ---\n")

M4_interact <- lm(
  as.formula(paste(
    "ln_labor_prod ~ fsts_c + fsts_c2 + tci_z + dai_z",
    "+ fsts_c:dai_z + fsts_c2:dai_z +", base_rhs
  )),
  data = df
)

# Waldtest with HC1 for joint test of the two interaction terms
wtest <- waldtest(
  M4, M4_interact,
  vcov = vcovHC(M4_interact, type = "HC1"),
  test = "F"
)

cat("  Restricted model (M4):   no interaction\n")
cat("  Unrestricted model:      + fsts_c:dai_z + fsts_c2:dai_z\n\n")
print(wtest)

joint_F   <- wtest$F[2]
joint_df1 <- wtest$Df[2]
joint_df2 <- wtest$Res.Df[2]
joint_p   <- wtest$`Pr(>F)`[2]

cat(sprintf(
  "\n  Joint F(%d, %d) = %.4f,  p = %.4f  [%s]\n",
  joint_df1, joint_df2, joint_F, joint_p,
  ifelse(joint_p < 0.05, "SIGNIFICANT", "not significant")
))

# Individual interaction coefficients
ct_interact <- robust_coeftest(M4_interact)
cat("\n  Interaction-term coefficients (HC1 robust SEs):\n")
interact_rows <- c("fsts_c:dai_z", "fsts_c2:dai_z")
for (rn in interact_rows) {
  if (rn %in% rownames(ct_interact)) {
    r <- ct_interact[rn, ]
    cat(sprintf("    %-20s  b=%.5f  SE=%.5f  t=%.3f  p=%.4f\n",
                rn, r[1], r[2], r[3], r[4]))
  }
}

# ---------------------------------------------------------------------------
# 9. Collect all model coefficients
# ---------------------------------------------------------------------------
cat("\n--- 8. Collecting coefficients ---\n")

all_models <- list(
  M0 = list(m = M0, d = df),
  M1 = list(m = M1, d = df),
  M2 = list(m = M2, d = df),
  M3 = list(m = M3, d = df),
  M4 = list(m = M4, d = df),
  M5 = list(m = M5, d = df),
  M6 = list(m = M6, d = df_fe),
  M7 = list(m = M7, d = df_fe),
  M8 = list(m = M8, d = df_fe)
)

coef_list <- lapply(names(all_models), function(nm) {
  tidy_robust(all_models[[nm]]$m, nm)
})
coef_df <- bind_rows(coef_list)

# Add R-squared and adjusted R-squared
model_fit <- lapply(names(all_models), function(nm) {
  s <- summary(all_models[[nm]]$m)
  data.frame(
    model     = nm,
    n_obs     = nobs(all_models[[nm]]$m),
    r_sq      = round(s$r.squared, 6),
    adj_r_sq  = round(s$adj.r.squared, 6)
  )
})
model_fit_df <- bind_rows(model_fit)

# ---------------------------------------------------------------------------
# 10. Build turning-points table (all models with quadratic)
# ---------------------------------------------------------------------------
tp_all <- bind_rows(
  turning_point(M2, df,    "M2_pooled"),
  turning_point(M3, df,    "M3_pooled"),
  turning_point(M4, df,    "M4_pooled"),
  turning_point(M5, df,    "M5_pooled"),
  turning_point(M6, df_fe, "M6_country_FE"),
  turning_point(M7, df_fe, "M7_country_FE"),
  turning_point(M8, df_fe, "M8_country_FE")
)

if (nrow(icrv_tp_df) > 0) {
  tp_all <- bind_rows(tp_all, icrv_tp_df)
}

# ---------------------------------------------------------------------------
# 11. Summary table for focal variables
# ---------------------------------------------------------------------------
cat("\n=============================================================\n")
cat("  SUMMARY: Focal Variables (fsts_c, fsts_c2, tci_z, dai_z)\n")
cat("=============================================================\n")

focal_terms <- c("fsts_c", "fsts_c2", "tci_z", "dai_z",
                 "mgr_experience", "mgr_female")

cat(sprintf("%-20s %8s %10s %10s %10s %10s %10s %10s %10s %10s\n",
            "Term", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", ""))
cat(paste(rep("-", 112), collapse = ""), "\n")

pivot_coef <- coef_df %>%
  filter(term %in% focal_terms) %>%
  select(term, model, estimate, p.value)

for (trm in focal_terms) {
  row_d <- pivot_coef %>% filter(term == trm)
  vals  <- sapply(c("M1","M2","M3","M4","M5","M6","M7","M8"), function(m) {
    r <- row_d %>% filter(model == m)
    if (nrow(r) == 0) return("     ---")
    stars <- ifelse(r$p.value < 0.01, "***",
             ifelse(r$p.value < 0.05, "** ",
             ifelse(r$p.value < 0.10, "*  ", "   ")))
    sprintf("%7.4f%s", r$estimate, stars)
  })
  cat(sprintf("%-20s %s\n", trm, paste(vals, collapse = " ")))
}

cat(paste(rep("-", 112), collapse = ""), "\n")
cat("Significance: *** p<0.01  ** p<0.05  * p<0.10\n\n")

# Model fit
cat("Model fit:\n")
cat(sprintf("%-10s %8s %10s %12s\n", "Model", "N", "R²", "Adj. R²"))
for (i in seq_len(nrow(model_fit_df))) {
  cat(sprintf("%-10s %8d %10.4f %12.4f\n",
              model_fit_df$model[i],
              model_fit_df$n_obs[i],
              model_fit_df$r_sq[i],
              model_fit_df$adj_r_sq[i]))
}

cat("\nTurning Points (fsts_c quadratic):\n")
cat(sprintf("%-22s %8s %8s %10s %10s %10s %10s %12s\n",
            "Model", "b1", "b2", "TP(raw)", "TP(cntrd)",
            "Min(fsts)", "Max(fsts)", "In-Range?"))
for (i in seq_len(nrow(tp_all))) {
  r <- tp_all[i, ]
  cat(sprintf("%-22s %8.5f %8.5f %10.4f %10.4f %10.4f %10.4f %12s\n",
              r$model, r$b1, r$b2, r$tp_raw, r$tp_centered,
              r$fsts_min, r$fsts_max,
              ifelse(r$tp_in_range, "YES", "NO")))
}

# ---------------------------------------------------------------------------
# 12. Export results
# ---------------------------------------------------------------------------
cat("\n--- 9. Exporting results ---\n")

# Add model fit to coef_df
coef_export <- coef_df %>%
  left_join(model_fit_df %>% select(model, r_sq, adj_r_sq), by = "model") %>%
  rename(
    se       = std.error,
    t_stat   = statistic,
    p_val    = p.value
  )

write.csv(coef_export, COEF_OUT, row.names = FALSE)
cat(sprintf("  Coefficients written to: %s  (%d rows)\n", COEF_OUT, nrow(coef_export)))

tp_export <- tp_all
write.csv(tp_export, TP_OUT, row.names = FALSE)
cat(sprintf("  Turning points written to: %s  (%d rows)\n", TP_OUT, nrow(tp_export)))

cat("\n=============================================================\n")
cat("  DONE – Paper 7 R Analysis Complete\n")
cat("=============================================================\n")
