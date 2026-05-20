#!/usr/bin/env python3
"""
38_mara_readiness_check.py
Check current MARA readiness: how many effect sizes are ready_for_r=1,
project k and K after full L2 completion, and output R starter code.
"""

import csv
from datetime import datetime
from pathlib import Path
from collections import Counter

TODAY = datetime.now().strftime("%Y%m%d")

def run():
    # Load tracker v3
    with open('p6/tools/results/fulltext_to_extraction_tracker_v3.csv') as f:
        rows = list(csv.DictReader(f))

    # Existing coded studies (seq <= 435)
    existing = [r for r in rows if int(r.get('seq', 0)) <= 435]
    ex_ready = [r for r in existing if r.get('ready_for_r', '') == '1']
    ex_r     = [r for r in existing if r.get('converted_r', '').strip()]

    # New candidates
    new_all  = [r for r in rows if int(r.get('seq', 0)) > 435]
    new_y    = [r for r in new_all if r['fulltext_screening_decision'] == 'Y']
    new_done = [r for r in new_y if r.get('ready_for_r', '') == '1']
    new_r    = [r for r in new_y if r.get('converted_r', '').strip()]

    print("=" * 60)
    print(f"MARA Readiness Check — {TODAY}")
    print("=" * 60)
    print(f"\nExisting coded studies (k=238 database):")
    print(f"  Total rows in tracker:  {len(existing)}")
    print(f"  ready_for_r=1:          {len(ex_ready)}")
    print(f"  converted_r filled:     {len(ex_r)}")
    print(f"\nNew candidates (post-screening):")
    print(f"  Total new rows:         {len(new_all)}")
    print(f"  Confirmed Y:            {len(new_y)}")
    print(f"  ready_for_r=1 (done):   {len(new_done)}")
    print(f"  converted_r filled:     {len(new_r)}")
    print(f"  Pending extraction:     {len(new_y) - len(new_done)}")

    # ICRV breakdown for Y papers
    icrv_c = Counter(r.get('icrv', '') for r in new_y if r.get('icrv', '').strip())
    print(f"\nICRV breakdown for 538 Y papers (pre-filled):")
    for code, label in [('1','Advanced'),('2','Upper-middle'),('3','Emerging'),
                         ('4','Resource-rich'),('5','SIDS'),('6','Frontier'),('0','Multi-country')]:
        cnt = icrv_c.get(code, 0)
        print(f"  ICRV {code} ({label}): {cnt}")
    print(f"  Unknown/blank:          {icrv_c.get('', sum(1 for r in new_y if not r.get('icrv', '').strip()))}")

    # DPL breakdown
    dpl_c = Counter(r.get('dpl', '') for r in new_y)
    print(f"\nDPL breakdown for 538 Y papers:")
    for code, label in [('1','Pre-digital <2000'),('2','Early digital 2000-09'),('3','Platform era ≥2010')]:
        print(f"  DPL {code} ({label}): {dpl_c.get(code, 0)}")

    # fp_type breakdown
    fp_c = Counter(r.get('fp_type', '') for r in new_y if r.get('fp_type', '').strip())
    print(f"\nfp_type breakdown (pre-filled, 85% coverage):")
    for fp, cnt in fp_c.most_common(8):
        print(f"  {fp}: {cnt}")

    # Projection
    print(f"\n--- MARA PROJECTION ---")
    print(f"Current k (existing coded): ~238 studies")
    print(f"Y candidates from new search: 538")
    print(f"  Conservative (50% pass full L2): +269")
    print(f"  Optimistic (70% pass full L2):   +377")
    print(f"Projected k range: 507–615 studies")
    print(f"Assuming 1.5 effects/study avg: K = 760–920 effect sizes")
    print(f"")
    print(f"This would power: ICRV (6 groups), DPL (3 phases),")
    print(f"  cDAI (continuous), curvilinear subset — all adequately")

    # R starter code
    r_code = '''
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

# ── M0: Three-level baseline ────────────────────────────────────────
m0 <- rma.mv(yi, vi,
             random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
             data = dat, method = "REML")

cat("k =", length(unique(dat$study_id)),
    "| K =", nrow(dat),
    "| r =", round(tanh(coef(m0)), 3), "\\n")

# I² decomposition (Cheung 2014)
W  <- diag(1 / dat$vi)
X  <- model.matrix(m0)
P  <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
I2 <- 100 * sum(m0$sigma2) / (sum(m0$sigma2) + (m0$k - m0$p) / sum(diag(P)))

# ── M1–M4: Moderators ───────────────────────────────────────────────
m1_icrv <- rma.mv(yi, vi, mods = ~ factor(icrv),
                  random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
                  data = dat, method = "REML")

m2_dpl  <- rma.mv(yi, vi, mods = ~ factor(dpl),
                  random = list(~ 1 | study_id, ~ 1 | study_id/es_id),
                  data = dat, method = "REML")

# ── Publication bias ────────────────────────────────────────────────
precision <- 1 / sqrt(dat$vi)
egger     <- lm(dat$yi ~ precision, weights = 1 / dat$vi)
cat("Egger p =", summary(egger)$coefficients[1, 4], "\\n")

# ── Cluster-robust variance estimation ─────────────────────────────
vcov_rve <- vcovCR(m0, cluster = dat$study_id, type = "CR2")
coef_test(m0, vcov = vcov_rve)
'''

    r_path = Path(f'p6/tools/meta_r_scripts/00_mara_starter_{TODAY}.R')
    r_path.parent.mkdir(parents=True, exist_ok=True)
    with open(r_path, 'w') as f:
        f.write(r_code.strip() + '\n')
    print(f"\nR starter script written: {r_path}")

if __name__ == "__main__":
    run()
