#!/usr/bin/env Rscript
# Meta-análisis con metafor. Lee meta_input.csv de la carpeta del proyecto y
# genera forest_plot.png, funnel_plot.png, rob_summary.png + script editable.
#
# Schema esperado de meta_input.csv (rellenar manualmente desde master_corpus):
#   study, year, n_int, mean_int, sd_int, n_ctrl, mean_ctrl, sd_ctrl
#   (o bien: study, year, yi, vi  — si ya tienes effect size y varianza)
#
# Uso: Rscript meta_analysis.R <project_dir>

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 1) {
  stop("Uso: Rscript meta_analysis.R <project_dir>")
}
proj <- args[1]
ma_dir <- file.path(proj, "meta_analysis")
dir.create(ma_dir, recursive = TRUE, showWarnings = FALSE)

input_csv <- file.path(proj, "meta_input.csv")
if (!file.exists(input_csv)) {
  cat(sprintf("[ma] No existe %s. Crea un CSV con columnas:\n", input_csv))
  cat("  Para SMD/MD: study, year, n_int, mean_int, sd_int, n_ctrl, mean_ctrl, sd_ctrl\n")
  cat("  Para OR/RR: study, year, events_int, n_int, events_ctrl, n_ctrl\n")
  cat("  O precomputado: study, year, yi, vi\n")
  quit(status = 2)
}

if (!requireNamespace("metafor", quietly = TRUE)) {
  install.packages("metafor", repos = "https://cloud.r-project.org")
}
suppressPackageStartupMessages(library(metafor))

dat <- read.csv(input_csv, stringsAsFactors = FALSE)

# Decide tipo de effect size
if (all(c("yi", "vi") %in% names(dat))) {
  measure <- "Pre-computed"
  res <- rma(yi = dat$yi, vi = dat$vi, slab = paste(dat$study, dat$year), method = "REML")
} else if (all(c("mean_int", "sd_int", "n_int", "mean_ctrl", "sd_ctrl", "n_ctrl") %in% names(dat))) {
  measure <- "SMD"
  es <- escalc(measure = "SMD",
               m1i = mean_int, sd1i = sd_int, n1i = n_int,
               m2i = mean_ctrl, sd2i = sd_ctrl, n2i = n_ctrl,
               data = dat)
  res <- rma(yi, vi, data = es, slab = paste(es$study, es$year), method = "REML")
} else if (all(c("events_int", "n_int", "events_ctrl", "n_ctrl") %in% names(dat))) {
  measure <- "OR"
  es <- escalc(measure = "OR",
               ai = events_int, n1i = n_int,
               ci = events_ctrl, n2i = n_ctrl,
               data = dat)
  res <- rma(yi, vi, data = es, slab = paste(es$study, es$year), method = "REML")
} else {
  stop("[ma] Schema CSV no reconocido — revisa nombres de columnas.")
}

# Forest plot
png(file.path(ma_dir, "forest_plot.png"), width = 1600, height = 900, res = 160)
forest(res, header = TRUE)
dev.off()

# Funnel plot
png(file.path(ma_dir, "funnel_plot.png"), width = 1200, height = 900, res = 160)
funnel(res, main = "Funnel plot — sesgo de publicación")
dev.off()

# RoB summary placeholder — usuario rellena con datos de rob_assessments.xlsx
png(file.path(ma_dir, "rob_summary.png"), width = 1400, height = 700, res = 160)
plot.new()
title("RoB summary plot — rellenar con rob_assessments.xlsx (e.g. robvis package)")
text(0.5, 0.5, "Genera con paquete robvis:\nrobvis::rob_traffic_light(rob_data, tool='ROB2')",
     cex = 1.4)
dev.off()

# Script editable
script_path <- file.path(ma_dir, "ma_script.R")
writeLines(c(
  "# Script de meta-análisis — generado por systematic-review skill",
  "# Edita y re-ejecuta para tunear",
  "library(metafor)",
  sprintf("dat <- read.csv('%s')", input_csv),
  sprintf("# Effect measure: %s", measure),
  "# res <- rma(...)",
  "# forest(res); funnel(res)"
), script_path)

cat(sprintf("[ma] OK — measure=%s, k=%d, summary effect=%.3f (95%% CI %.3f to %.3f)\n",
            measure, res$k, res$b[1], res$ci.lb, res$ci.ub))
