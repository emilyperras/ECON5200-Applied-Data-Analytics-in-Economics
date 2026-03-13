# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective
Executed a multivariate hedonic pricing model on 2026 California real estate data to decompose property sale prices by their structural determinants, and formally proved the Frisch-Waugh-Lovell (FWL) theorem through manual residual isolation — demonstrating that algorithmic *ceteris paribus* is a mathematically verifiable operation, not merely a conceptual abstraction.

---

## Methodology

- **Data Ingestion:** Loaded a synthetic Zillow dataset (`n = 1,000`) containing `Sale_Price`, `Property_Age`, and `Distance_to_Tech_Hub` for California residential properties (2026).
- **Naive OLS Baseline:** Regressed `Sale_Price` on `Property_Age` alone, yielding a spuriously *positive* coefficient of **+$5,573/year** — a textbook signature of omitted variable bias (OVB).
- **Multivariate OLS:** Introduced `Distance_to_Tech_Hub` as a control, collapsing the age coefficient to **−$2,063/year** and lifting R² from 0.757 → 0.954. The sign reversal confirmed that proximity to tech employment was the true value driver being incorrectly attributed to physical age.
- **FWL Theorem — Manual Proof (3-step residual extraction):**
  1. Regressed `Sale_Price` on `Distance_to_Tech_Hub`; retained residuals (`Price_Residuals`) — the variation in price *unexplained* by distance.
  2. Regressed `Property_Age` on `Distance_to_Tech_Hub`; retained residuals (`Age_Residuals`) — the variation in age *unexplained* by distance.
  3. Regressed `Price_Residuals ~ Age_Residuals` (no intercept), isolating the pure partial effect of age net of all shared covariance with distance.

---

## Key Findings

| Model | Age Coefficient | R² |
|---|---|---|
| Naive OLS (bivariate) | **+$5,573/yr** *(biased)* | 0.757 |
| Multivariate OLS | **−$2,063/yr** | 0.954 |
| FWL Manual Proof | **−$2,063/yr** *(exact match)* | — |

- **Omitted Variable Bias confirmed:** Excluding `Distance_to_Tech_Hub` caused a **~$7,600/year sign-reversing bias** on the age coefficient. Newer homes clustered near tech hubs were expensive *because of location*, not youth — but the naive model assigned that premium entirely to age.
- **FWL theorem verified:** The three-step residual regression produced a coefficient of **−$2,063.13**, matching the multivariate OLS result to six decimal places. This proves that controlling for a covariate is mathematically equivalent to partialling out its shared variance — *ceteris paribus* is not assumed; it is computed.
- **Interpretive implication:** In hedonic pricing models, failure to account for spatial confounders (proximity to employment, amenities, transit) will systematically distort attribute-level valuations, making rigorous covariate selection a prerequisite — not an optional enhancement.

---

## Tech Stack

`Python 3.10+` · `pandas` · `statsmodels.formula.api` · `matplotlib` · `plotly.graph_objects` · `numpy`

---

*Lab 13 | ECON 5200 — Applied Data Analytics in Economics*
