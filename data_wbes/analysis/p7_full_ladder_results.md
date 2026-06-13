# P7 full ladder — 50-economy frame (incl. Japan), canonical spec

Analytic frame: 88869 firms, 50 economies. DV lp_z; two-way FE economy+year; CRV1 economy. FSTS mean 9.0%.

| Model | N | b1 (FSTS) | p | b2 (FSTS²) | p | TP % | key moderators |
|---|--:|--:|--:|--:|--:|--:|---|
| M1 linear | 81,022 | +0.219 | 0.002 | — | — | — |  |
| M2 quadratic [anchor] | 81,022 | +1.188 | 0.000 | -1.398 | 0.000 | 51.5 |  |
| M3 +controls | 78,970 | +0.697 | 0.000 | -1.000 | 0.000 | 43.8 |  |
| M4 +TCI+DAI [anchor] | 79,080 | +0.499 | 0.000 | -0.721 | 0.000 | 43.6 | tci_z=+0.108*** dai=+0.219*** |
| M5 +FSTSxTCI | 79,080 | +0.457 | 0.001 | -0.652 | 0.002 | 44.0 | fXt=+0.068 f2Xt=-0.119 tci_z=+0.115*** dai=+0.219*** |
| M6 +FSTSxDAI | 79,080 | +0.704 | 0.000 | -0.924 | 0.000 | 47.1 | fXd=-0.270 f2Xd=+0.252 tci_z=+0.108*** dai=+0.201*** |
| M7 +manager | 75,029 | +0.505 | 0.000 | -0.720 | 0.000 | 44.0 | mgr_exp_z=+0.002 mgr_fem=-0.104*** tci_z=+0.108*** dai=+0.218*** |
| M8 +ICRVmod | 79,080 | +0.806 | 0.053 | -0.624 | 0.216 | 73.6 | grp=+0.930 fXg=-0.086 f2Xg=-0.013 tci_z=+0.107*** dai=+0.220*** |

## Per-ICRV turning points (M4 form: + fdi10+ln_age+tci_z+dai)

| ICRV group | N | b1 | b2 | TP % |
|---|--:|--:|--:|--:|
| Advanced_innovation | 5,581 | +0.707 | -0.504 | 80.0 |
| Advanced_resource | 2,075 | +0.774 | -0.730 | 56.6 |
| Upper_mid | 12,055 | +0.174 | -0.189 | 56.4 |
| Lower_mid_transition | 42,094 | +0.689 | -1.012 | 42.0 |
| Emerging | 15,457 | +0.235 | -0.455 | 36.8 |
| SIDS_small | 1,818 | -0.681 | +0.870 | — |
