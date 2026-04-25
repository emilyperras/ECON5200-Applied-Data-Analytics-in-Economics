# Verification Log — Lab 24: Double Machine Learning

## Manual DML Verification on Simulated Data

**Setup:**
- n = 5,000 observations, p = 100 covariates
- True ATE = 5.0 (known by construction)
- Treatment assigned via logistic propensity score on X[:,0:3]
- Outcome: Y = 5.0*D + 2*X0 + 1.5*X1 + 1.0*X2 + noise

**Broken DML result:**
- Broken ATE: 1.09
- Bias: -3.91
- All three bugs active: in-sample prediction, missing treatment residualization, wrong formula

**Fixed DML result:**
- Fixed ATE: within 0.5 of 5.0 ✓
- PASS — Fixed ATE is within 1.0 of the true value ✓
- Cross-fitting confirmed: residuals computed out-of-fold only
- Double residualization confirmed: both Y and D residualized on X
- IV-style formula confirmed: sum(D_tilde * Y_tilde) / sum(D_tilde * D)

## 401(k) DML Results

**ATE Estimate:** $8,755
**95% CI:** [$4,984, $12,526]
**Result:** Statistically significant — 401(k) eligibility increases net financial assets by ~$8,755

**Sensitivity Analysis (cf_y=0.03, cf_d=0.03):**
- Robustness Value (RV): 6.83%
- An unobserved confounder would need to explain at least 6.83% of residual variance in both 401(k) eligibility and net financial assets to reduce the result to non-significance
- Lower bound of bias-adjusted CI: $2,655 — result remains positive even under moderate confounding
- Conclusion: result is moderately robust to unobserved confounding

## What I Verified
- Broken DML bias: -3.91 (far from true ATE) ✓
- Fixed DML recovers true ATE within tolerance ✓
- DoubleML ATE statistically significant ✓
- Sensitivity RV = 6.83% — result survives moderate confounding ✓
- CATE histogram saved to figures/cate_histogram.png ✓
- causal_ml.py self-test passes ✓
