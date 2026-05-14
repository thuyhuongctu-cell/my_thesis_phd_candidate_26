# P5 China — R replication of 04_run_models.do
# Uses pooled WBES CSV (stata-khong-license alternative)
# Packages: lmtest, sandwich, plm (panel FE), dplyr

suppressPackageStartupMessages({
  library(dplyr)
  library(lmtest)
  library(sandwich)
  library(plm)
  library(broom)
})

DATA_PATH <- file.path("..", "..", "..", "data_wbes", "analysis", "pooled_wbes_6waves.csv")
OUT_DIR   <- file.path("..", "results")
dir.create(OUT_DIR, showWarnings = FALSE)

# ── Load & filter China ───────────────────────────────────────────────────────
raw <- read.csv(DATA_PATH)
chn <- raw %>%
  filter(country == "CHN") %>%
  mutate(
    FSTS      = export_pct / 100,
    FSTSsq    = FSTS^2,
    FSTSc     = FSTS - mean(FSTS, na.rm = TRUE),
    FSTScsq   = FSTSc^2,
    lnEmp     = ln_empl,
    lnLP      = ln_labor_prod,
    firmage   = firm_age,
    foreign   = as.integer(foreign_own > 0),
    TCI       = TCI_full,
    DAI       = DAI_thin,
    wave      = as.integer(year == 2024)
  ) %>%
  filter(!is.na(lnLP), !is.na(lnEmp), !is.na(firmage))

chn_2012 <- chn %>% filter(year == 2012)
chn_2024 <- chn %>% filter(year == 2024)
cat(sprintf("[INFO] China 2012 N = %d | 2024 N = %d\n", nrow(chn_2012), nrow(chn_2024)))

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

# ── PART A: 2012 Wave ─────────────────────────────────────────────────────────
d12 <- chn_2012 %>% filter(!is.na(FSTS))
cat(sprintf("[INFO] 2012 analytic N = %d\n", nrow(d12)))

results[["m0_2012"]] <- rob_tidy(
  lm(lnLP ~ lnEmp + firmage + foreign, data = d12), "CHN2012", "M0")
results[["m1_2012"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + lnEmp + firmage + foreign, data = d12), "CHN2012", "M1")
results[["m2_2012"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign, data = d12), "CHN2012", "M2")
results[["m3_2012"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + lnEmp + firmage + foreign, data = d12), "CHN2012", "M3")
results[["m4_2012"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + lnEmp + firmage + foreign, data = d12),
  "CHN2012", "M4")
results[["m5_2012"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + FSTScsq:TCI + lnEmp + firmage + foreign,
     data = d12), "CHN2012", "M5")

# Turning point 2012
m2_12 <- lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign, data = d12)
b1_12 <- coef(m2_12)["FSTSc"]; b2_12 <- coef(m2_12)["FSTScsq"]
tp_12 <- (-b1_12 / (2*b2_12)) + mean(d12$FSTS, na.rm=TRUE)
cat(sprintf("[2012] Turning point FSTS = %.4f (%.1f%%)\n", tp_12, tp_12*100))

# ── PART B: 2024 Wave ─────────────────────────────────────────────────────────
d24 <- chn_2024 %>% filter(!is.na(FSTS))
cat(sprintf("[INFO] 2024 analytic N = %d\n", nrow(d24)))

results[["m0_2024"]] <- rob_tidy(
  lm(lnLP ~ lnEmp + firmage + foreign, data = d24), "CHN2024", "M0")
results[["m1_2024"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + lnEmp + firmage + foreign, data = d24), "CHN2024", "M1")
results[["m2_2024"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign, data = d24), "CHN2024", "M2")
results[["m3_2024"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + lnEmp + firmage + foreign, data = d24), "CHN2024", "M3")
results[["m4_2024"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + lnEmp + firmage + foreign, data = d24),
  "CHN2024", "M4")
results[["m5_2024"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + FSTScsq:TCI + lnEmp + firmage + foreign,
     data = d24), "CHN2024", "M5")

# Turning point 2024
m2_24 <- lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign, data = d24)
b1_24 <- coef(m2_24)["FSTSc"]; b2_24 <- coef(m2_24)["FSTScsq"]
tp_24 <- (-b1_24 / (2*b2_24)) + mean(d24$FSTS, na.rm=TRUE)
cat(sprintf("[2024] Turning point FSTS = %.4f (%.1f%%)\n", tp_24, tp_24*100))

# ── PART C: Pooled (OLS with wave FE) ─────────────────────────────────────────
pool <- chn %>% filter(!is.na(FSTS))
cat(sprintf("[INFO] Pooled analytic N = %d\n", nrow(pool)))

results[["m0_pool"]] <- rob_tidy(
  lm(lnLP ~ lnEmp + firmage + foreign + wave, data = pool), "CHN_pooled", "M0")
results[["m2_pool"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign + wave, data = pool),
  "CHN_pooled", "M2")
results[["m3_pool"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + lnEmp + firmage + foreign + wave, data = pool),
  "CHN_pooled", "M3")
results[["m4_pool"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + lnEmp + firmage + foreign + wave, data = pool),
  "CHN_pooled", "M4")
results[["m5_pool"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + FSTScsq:TCI + lnEmp + firmage + foreign + wave,
     data = pool), "CHN_pooled", "M5")

# Turning point pooled
m2_pool <- lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign + wave, data = pool)
b1_p <- coef(m2_pool)["FSTSc"]; b2_p <- coef(m2_pool)["FSTScsq"]
tp_p  <- (-b1_p / (2*b2_p)) + mean(pool$FSTS, na.rm=TRUE)
cat(sprintf("[Pooled] Turning point FSTS = %.4f (%.1f%%)\n", tp_p, tp_p*100))

# ── PART D: Paternoster z-test (2012 vs 2024 quadratic coefficients) ───────────
get_robust <- function(fit, var) {
  ct <- coeftest(fit, vcov = vcovHC(fit, "HC1"))
  c(b = ct[var, "Estimate"], se = ct[var, "Std. Error"])
}

b_lin_12 <- get_robust(m2_12, "FSTSc")
b_lin_24 <- get_robust(m2_24, "FSTSc")
b_sq_12  <- get_robust(m2_12, "FSTScsq")
b_sq_24  <- get_robust(m2_24, "FSTScsq")

z_lin <- (b_lin_12["b"] - b_lin_24["b"]) / sqrt(b_lin_12["se"]^2 + b_lin_24["se"]^2)
z_sq  <- (b_sq_12["b"]  - b_sq_24["b"])  / sqrt(b_sq_12["se"]^2  + b_sq_24["se"]^2)
cat(sprintf("\n[Paternoster 2012 vs 2024]\n"))
cat(sprintf("  FSTSc:   z = %.3f, p = %.4f\n", z_lin, 2*pnorm(-abs(z_lin))))
cat(sprintf("  FSTScsq: z = %.3f, p = %.4f\n", z_sq,  2*pnorm(-abs(z_sq))))

# ── Export ────────────────────────────────────────────────────────────────────
out <- bind_rows(results)
write.csv(out, file.path(OUT_DIR, "p5_R_coefs.csv"), row.names = FALSE)
cat(sprintf("\n[OUTPUT] Saved %d rows → p5_R_coefs.csv\n", nrow(out)))

tp_df <- data.frame(
  sample  = c("CHN2012_M2", "CHN2024_M2", "CHNpooled_M2"),
  tp_fsts = c(tp_12, tp_24, tp_p),
  tp_pct  = c(tp_12*100, tp_24*100, tp_p*100),
  b1      = c(b1_12, b1_24, b1_p),
  b2      = c(b2_12, b2_24, b2_p),
  z_paternoster_lin = c(z_lin, NA, NA),
  p_paternoster_lin = c(2*pnorm(-abs(z_lin)), NA, NA),
  z_paternoster_sq  = c(z_sq,  NA, NA),
  p_paternoster_sq  = c(2*pnorm(-abs(z_sq)),  NA, NA)
)
write.csv(tp_df, file.path(OUT_DIR, "p5_R_turning_points.csv"), row.names = FALSE)
cat("[OUTPUT] Turning points and Paternoster z saved.\n")
