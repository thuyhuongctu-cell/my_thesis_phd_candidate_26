# P7 full ladder — 50-economy frame (incl. Japan), canonical spec

Analytic frame: 87987 firms, 48 economies. DV lp_z; two-way FE economy+year; CRV1 economy. FSTS mean 9.0%.

| Model | N | b1 (FSTS) | p | b2 (FSTS²) | p | TP % | key moderators |
|---|--:|--:|--:|--:|--:|--:|---|
| M1 linear | 80,373 | +0.220 | 0.002 | — | — | — |  |
| M2 quadratic [anchor] | 80,373 | +1.193 | 0.000 | -1.404 | 0.000 | 51.5 |  |
| M3 +controls | 78,331 | +0.702 | 0.000 | -1.008 | 0.000 | 43.8 |  |
| M4 +TCI+DAI [anchor] | 78,445 | +0.502 | 0.000 | -0.727 | 0.000 | 43.5 | tci_z=+0.108*** dai=+0.218*** |
| M5 +FSTSxTCI | 78,445 | +0.460 | 0.001 | -0.658 | 0.002 | 43.9 | fXt=+0.066 f2Xt=-0.118 tci_z=+0.115*** dai=+0.219*** |
| M6 +FSTSxDAI | 78,445 | +0.722 | 0.000 | -0.950 | 0.000 | 47.0 | fXd=-0.291 f2Xd=+0.279 tci_z=+0.109*** dai=+0.199*** |
| M7 +manager | 74,507 | +0.509 | 0.000 | -0.727 | 0.000 | 44.0 | mgr_exp_z=+0.002 mgr_fem=-0.103*** tci_z=+0.109*** dai=+0.218*** |
| M8 +ICRVmod | 78,445 | +0.780 | 0.061 | -0.570 | 0.255 | 77.4 | fXg=-0.079 f2Xg=-0.029 tci_z=+0.107*** dai=+0.220*** |

## Per-ICRV turning points (M4 form: + fdi10+ln_age+tci_z+dai)

| ICRV group | N | b1 | b2 | TP % |
|---|--:|--:|--:|--:|
| Advanced_innovation | 5,581 | +0.707 | -0.504 | 80.0 |
| Advanced_resource | 2,075 | +0.774 | -0.730 | 56.6 |
| Upper_mid | 12,055 | +0.174 | -0.189 | 56.4 |
| Lower_mid_transition | 42,094 | +0.689 | -1.012 | 42.0 |
| Emerging | 15,251 | +0.232 | -0.453 | 36.7 |
| SIDS_small | 1,389 | -0.775 | +1.051 | — |
