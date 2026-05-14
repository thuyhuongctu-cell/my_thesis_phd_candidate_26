# P4 Singapore — R replication of 02_run_models.do
# Uses pooled WBES CSV (stata-khong-license alternative)
# Packages: lmtest, sandwich, broom, dplyr, AER (for Heckman-style selection)

suppressPackageStartupMessages({
  library(dplyr)
  library(lmtest)
  library(sandwich)
  library(broom)
  library(AER)
})

DATA_PATH <- file.path("..", "..", "..", "data_wbes", "analysis", "pooled_wbes_6waves.csv")
OUT_DIR   <- file.path("..", "tables")
dir.create(OUT_DIR, showWarnings = FALSE)

# ── Load & filter Singapore 2023 ─────────────────────────────────────────────
raw <- read.csv(DATA_PATH)
sgp <- raw %>%
  filter(dataset == "SGP_2023") %>%
  mutate(
    FSTS    = export_pct / 100,
    FSTSsq  = FSTS^2,
    FSTSc   = FSTS - mean(FSTS, na.rm = TRUE),
    FSTScsq = FSTSc^2,
    lnEmp   = ln_empl,
    lnLP    = ln_labor_prod,
    foreign = as.integer(foreign_own > 0),
    TCI     = TCI_full,
    DAI     = DAI_rich
  ) %>%
  filter(!is.na(lnLP), !is.na(lnEmp), !is.na(firm_age))

cat(sprintf("[INFO] Singapore N (total) = %d\n", nrow(sgp)))

# Exporter subsample (FSTS > 0)
exp_sgp <- sgp %>% filter(FSTS > 0, !is.na(FSTS))
cat(sprintf("[INFO] Exporters N = %d\n", nrow(exp_sgp)))

# ── Helper ────────────────────────────────────────────────────────────────────
rob_tidy <- function(fit, sample, model) {
  ct <- coeftest(fit, vcov = vcovHC(fit, type = "HC1"))
  as.data.frame(ct[, , drop = FALSE]) %>%
    tibble::rownames_to_column("term") %>%
    rename(b = Estimate, se = `Std. Error`, t = `t value`, p = `Pr(>|t|)`) %>%
    mutate(ci_lo = b - 1.96*se, ci_hi = b + 1.96*se,
           n = nobs(fit), r2 = summary(fit)$r.squared,
           sample = sample, model = model)
}

results <- list()
tag_full <- "SGP2023_full"
tag_exp  <- "SGP2023_exp"

# ── PART A: Full sample ───────────────────────────────────────────────────────
results[["full_M0"]] <- rob_tidy(
  lm(lnLP ~ lnEmp + firm_age + foreign, data = sgp), tag_full, "M0")

results[["full_M1"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + lnEmp + firm_age + foreign, data = sgp), tag_full, "M1")

results[["full_M2"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firm_age + foreign, data = sgp), tag_full, "M2")

results[["full_M3"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + lnEmp + firm_age + foreign, data = sgp), tag_full, "M3")

results[["full_M4"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + lnEmp + firm_age + foreign, data = sgp),
  tag_full, "M4")

results[["full_M5"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + FSTScsq:TCI + lnEmp + firm_age + foreign,
     data = sgp), tag_full, "M5")

# ── PART B: Exporters only ────────────────────────────────────────────────────
if (nrow(exp_sgp) >= 30) {
  results[["exp_M0"]] <- rob_tidy(
    lm(lnLP ~ lnEmp + firm_age + foreign, data = exp_sgp), tag_exp, "M0")

  results[["exp_M2"]] <- rob_tidy(
    lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firm_age + foreign, data = exp_sgp),
    tag_exp, "M2")

  results[["exp_M4"]] <- rob_tidy(
    lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + lnEmp + firm_age + foreign,
       data = exp_sgp), tag_exp, "M4")

  results[["exp_M5"]] <- rob_tidy(
    lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + FSTScsq:TCI + lnEmp + firm_age + foreign,
       data = exp_sgp), tag_exp, "M5")
}

# ── PART C: Heckman 2-step selection correction ───────────────────────────────
# Stage 1: probit — exporter status on firm characteristics
sgp_probit <- sgp %>% filter(!is.na(FSTS))
probit_fit  <- glm(exporter ~ lnEmp + firm_age + foreign + website + quality_cert,
                   family = binomial(link = "probit"), data = sgp_probit)
xb_all             <- predict(probit_fit, newdata = sgp_probit)
sgp_probit         <- sgp_probit %>%
  mutate(xb = xb_all, IMR = dnorm(xb) / pmax(pnorm(xb), 1e-10))

# Stage 2: OLS on exporters with IMR
exp_h <- sgp_probit %>% filter(exporter == 1, !is.na(IMR))
if (nrow(exp_h) >= 30) {
  fit_imr <- lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + IMR +
                  lnEmp + firm_age + foreign, data = exp_h)
  results[["exp_Heckman"]] <- rob_tidy(fit_imr, "SGP2023_Heckman", "M_IMR")
  cat(sprintf("[Heckman] IMR coef = %.4f, p = %.4f\n",
              coef(fit_imr)["IMR"],
              coeftest(fit_imr, vcovHC(fit_imr, "HC1"))["IMR", "Pr(>|t|)"]))
}

# ── PART D: Turning point (full M2) ───────────────────────────────────────────
m2_full <- lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firm_age + foreign, data = sgp)
b1 <- coef(m2_full)["FSTSc"]; b2 <- coef(m2_full)["FSTScsq"]
tp_c  <- -b1 / (2 * b2)
tp    <- tp_c + mean(sgp$FSTS, na.rm = TRUE)
cat(sprintf("\n[TURNING POINT full M2]\n  tp = %.4f (%.1f%%)\n", tp, tp*100))

# ── Lind-Mehlum equivalent: check if tp in [min, max] ────────────────────────
fsts_range <- range(sgp$FSTS, na.rm = TRUE)
lm_verdict <- tp >= fsts_range[1] & tp <= fsts_range[2]
cat(sprintf("[Lind-Mehlum] tp in data range [%.3f, %.3f]: %s\n",
            fsts_range[1], fsts_range[2], ifelse(lm_verdict, "YES (U/invU supported)", "NO")))

# ── Export ────────────────────────────────────────────────────────────────────
out <- bind_rows(results)
write.csv(out, file.path(OUT_DIR, "p4_R_coefs.csv"), row.names = FALSE)
cat(sprintf("\n[OUTPUT] Saved %d rows → %s/p4_R_coefs.csv\n", nrow(out), OUT_DIR))

tp_df <- data.frame(
  sample = "SGP2023_full_M2", tp_fsts = tp, tp_pct = tp*100,
  b1_fstsc = b1, b2_fstssq = b2,
  lm_verdict = lm_verdict, fsts_min = fsts_range[1], fsts_max = fsts_range[2]
)
write.csv(tp_df, file.path(OUT_DIR, "p4_R_turning_points.csv"), row.names = FALSE)
cat("[OUTPUT] Turning points saved.\n")
