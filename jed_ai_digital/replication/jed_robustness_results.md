# JED paper — robustness, saturation test, margins (computed)

## Robustness: pooled DAI premium under alternative specs

| spec | DAI premium | p | N |
|---|--:|--:|--:|
| baseline (DAI only) | +0.321 | 0.000 | 81377 |
| + TCI | +0.241 | 0.000 | 80900 |
| + size, age, FDI | +0.188 | 0.000 | 79309 |
| domestic-owned only | +0.179 | 0.000 | 74773 |

## Does the digital dividend differ by firm size? (DAI x ln size)

- DAI main = +0.189 (p=0.000)
- DAI x size = -0.024 (p=0.483)  (smaller firms gain more)

## Digital-saturation test (regime adoption vs regime premium, k=6)

- adoption %: [np.float64(69.2), np.float64(50.2), np.float64(53.9), np.float64(48.3), np.float64(40.9), np.float64(41.5)]
- premium  : [np.float64(0.24), np.float64(0.477), np.float64(0.214), np.float64(0.383), np.float64(0.253), np.float64(0.246)]
- Pearson r(adoption, premium) = -0.132 (p=0.803); negative => saturation (higher adoption, smaller marginal premium)

## Web adoption over time (all 50 economies)

| period | adoption % | N |
|---|--:|--:|
| 2003-09 | 32.6 | 5794 |
| 2010-15 | 44.6 | 23753 |
| 2016-25 | 52.3 | 58736 |
