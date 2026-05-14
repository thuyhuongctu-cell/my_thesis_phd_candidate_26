# P3 Vietnam — R replication of 02_run_models.do
# Uses pooled WBES CSV (stata-khong-license alternative)
# Packages: lmtest, sandwich, broom, dplyr

suppressPackageStartupMessages({
  library(dplyr)
  library(lmtest)
  library(sandwich)
  library(broom)
})

DATA_PATH <- file.path("..", "..", "..", "data_wbes", "analysis", "pooled_wbes_6waves.csv")
OUT_DIR   <- file.path("..", "data")
dir.create(OUT_DIR, showWarnings = FALSE)

# ── Load & filter Vietnam ────────────────────────────────────────────────────
raw <- read.csv(DATA_PATH)
vnm <- raw %>%
  filter(country == "VNM") %>%
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
    yr2015    = as.integer(year == 2015),
    yr2023    = as.integer(year == 2023)
  ) %>%
  filter(!is.na(lnLP), !is.na(lnEmp), !is.na(firmage))

cat(sprintf("[INFO] Vietnam total N = %d\n", nrow(vnm)))
cat(sprintf("[INFO] Exporters (FSTS>0): %d\n", sum(vnm$FSTS > 0, na.rm = TRUE)))

# ── Helper: robust-SE tidy ───────────────────────────────────────────────────
rob_tidy <- function(fit, sample, model) {
  ct <- coeftest(fit, vcov = vcovHC(fit, type = "HC1"))
  as.data.frame(ct[, , drop = FALSE]) %>%
    tibble::rownames_to_column("term") %>%
    rename(b = Estimate, se = `Std. Error`, t = `t value`, p = `Pr(>|t|)`) %>%
    mutate(
      ci_lo  = b - 1.96 * se,
      ci_hi  = b + 1.96 * se,
      n      = nobs(fit),
      r2     = summary(fit)$r.squared,
      sample = sample,
      model  = model
    )
}

results <- list()

# ── PART A: Full sample, pooled years ─────────────────────────────────────────
full <- vnm %>% filter(!is.na(FSTS))
cat(sprintf("[INFO] Full analytic N = %d\n", nrow(full)))

results[["full_M0"]] <- rob_tidy(
  lm(lnLP ~ lnEmp + firmage + foreign + yr2015 + yr2023, data = full),
  "VNM_pooled", "M0")

results[["full_M1"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + lnEmp + firmage + foreign + yr2015 + yr2023, data = full),
  "VNM_pooled", "M1")

results[["full_M2"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign + yr2015 + yr2023, data = full),
  "VNM_pooled", "M2")

results[["full_M3"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + lnEmp + firmage + foreign + yr2015 + yr2023, data = full),
  "VNM_pooled", "M3")

results[["full_M4"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + lnEmp + firmage + foreign + yr2015 + yr2023, data = full),
  "VNM_pooled", "M4")

results[["full_M5"]] <- rob_tidy(
  lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + FSTScsq:TCI + lnEmp + firmage + foreign + yr2015 + yr2023, data = full),
  "VNM_pooled", "M5")

# ── PART B: Exporters only ────────────────────────────────────────────────────
exp_only <- vnm %>% filter(FSTS > 0, !is.na(FSTS))
cat(sprintf("[INFO] Exporters-only N = %d\n", nrow(exp_only)))

for (yr in c(2009, 2015, 2023)) {
  s <- exp_only %>% filter(year == yr)
  tag <- paste0("VNM", yr, "_exp")
  fit_m2 <- lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign, data = s)
  results[[paste0(yr, "_M2_exp")]] <- rob_tidy(fit_m2, tag, "M2")
  fit_m4 <- lm(lnLP ~ FSTSc + FSTScsq + TCI + FSTSc:TCI + lnEmp + firmage + foreign, data = s)
  results[[paste0(yr, "_M4_exp")]] <- rob_tidy(fit_m4, tag, "M4")
}

# ── PART C: Turning-point (on pooled full sample M2) ─────────────────────────
m2 <- lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign + yr2015 + yr2023, data = full)
b1 <- coef(m2)["FSTSc"]; b2 <- coef(m2)["FSTScsq"]
tp_centered <- -b1 / (2 * b2)
tp_fsts     <- tp_centered + mean(full$FSTS, na.rm = TRUE)
cat(sprintf("\n[TURNING POINT M2 pooled]\n  tp_FSTS = %.4f (%.1f%%)\n", tp_fsts, tp_fsts * 100))

# ── PART D: Paternoster z-test 2009 vs 2023 (exporters, M2 FSTS quadratic) ──
est_years <- list()
for (yr in c(2009, 2023)) {
  s   <- exp_only %>% filter(year == yr)
  fit <- lm(lnLP ~ FSTSc + FSTScsq + lnEmp + firmage + foreign, data = s)
  v   <- vcovHC(fit, type = "HC1")
  est_years[[as.character(yr)]] <- list(
    b  = coef(fit)[c("FSTSc", "FSTScsq")],
    se = sqrt(diag(v)[c("FSTSc", "FSTScsq")])
  )
}
z_lin <- (est_years[["2009"]]$b["FSTSc"]   - est_years[["2023"]]$b["FSTSc"]) /
         sqrt(est_years[["2009"]]$se["FSTSc"]^2 + est_years[["2023"]]$se["FSTSc"]^2)
z_sq  <- (est_years[["2009"]]$b["FSTScsq"] - est_years[["2023"]]$b["FSTScsq"]) /
         sqrt(est_years[["2009"]]$se["FSTScsq"]^2 + est_years[["2023"]]$se["FSTScsq"]^2)
cat(sprintf("[Paternoster] FSTSc:  z = %.3f, p = %.3f\n", z_lin, 2*pnorm(-abs(z_lin))))
cat(sprintf("[Paternoster] FSTScsq: z = %.3f, p = %.3f\n", z_sq,  2*pnorm(-abs(z_sq))))

# ── Export ────────────────────────────────────────────────────────────────────
out <- bind_rows(results)
out_path <- file.path(OUT_DIR, "p3_R_coefs.csv")
write.csv(out, out_path, row.names = FALSE)
cat(sprintf("\n[OUTPUT] Saved %d rows → %s\n", nrow(out), out_path))

tp_df <- data.frame(
  sample = "VNM_pooled_M2",
  tp_fsts = tp_fsts,
  tp_pct  = tp_fsts * 100,
  b1_fstsc = b1, b2_fstssq = b2,
  z_paternoster_lin = z_lin, p_paternoster_lin = 2*pnorm(-abs(z_lin)),
  z_paternoster_sq  = z_sq,  p_paternoster_sq  = 2*pnorm(-abs(z_sq))
)
write.csv(tp_df, file.path(OUT_DIR, "p3_R_turning_points.csv"), row.names = FALSE)
cat("[OUTPUT] Turning points and Paternoster z saved.\n")
