# Lab 24: Double Machine Learning — Causal Inference on 401(k) Eligibility
**ECON 5200: Causal Machine Learning & Applied Analytics**

## Objective
Estimate the causal effect of 401(k) eligibility on net financial assets using Double Machine Learning (DML) and Causal Forests, moving from manual cross-fitting implementation to production-grade package-based estimation.

## How to Reproduce
```bash
pip install doubleml econml scikit-learn matplotlib pandas numpy
jupyter notebook notebooks/lab_ch24_diagnostic.ipynb
```

## Methodology
- Diagnosed and fixed three bugs in a manual DML cross-fitting implementation: in-sample prediction instead of out-of-fold, missing treatment residualization, and wrong IV-style formula
- Used DoubleML package to estimate the ATE of 401(k) eligibility (`e401`) on net total financial assets (`net_tfa`) with 5-fold cross-fitting
- Fit CausalForestDML (EconML) to estimate individual-level Conditional Average Treatment Effects (CATEs)
- Compared high vs low CATE subgroups to identify which households benefit most from 401(k) eligibility
- Used RandomForestRegressor for both outcome and treatment nuisance models

## Key Findings
- DML ATE estimate: ~$7,000–$12,000 increase in net financial assets from 401(k) eligibility
- Result is statistically significant (p < 0.05) — eligibility has a meaningful causal effect
- Causal Forest reveals heterogeneity: higher-income and more educated households tend to have larger individual treatment effects
- Manual DML with bugs produces severely biased estimates — cross-fitting and double residualization are both essential

## Repository Structure
- README.md
- requirements.txt
- notebooks/lab_ch24_diagnostic.ipynb
- src/
- figures/cate_histogram.png
