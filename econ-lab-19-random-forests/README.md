# Tree-Based Models — Random Forests
### ECON 5200: Causal Machine Learning & Applied Analytics · Lab 19

## Objective
Diagnose evaluation and methodological errors in a tree-ensemble workflow, tune hyperparameters via cross-validated grid search, and build production-grade SHAP explanation tooling for the California Housing dataset.

## How to Reproduce

```bash
# 1. Clone and install
git clone https://github.com/<your-username>/econ-lab-19-random-forests
cd econ-lab-19-random-forests
pip install -r requirements.txt

# 2. Run the notebook
jupyter notebook notebooks/lab_19_random_forests.ipynb

# 3. Run the SHAP utils demo (saves figures to figures/)
python src/shap_utils.py

# 4. Launch the interactive dashboard
streamlit run app.py
```

## Repository Structure

```
econ-lab-19-random-forests/
├── README.md
├── requirements.txt
├── app.py                          ← Streamlit dashboard
├── notebooks/
│   └── lab_19_random_forests.ipynb
├── src/
│   └── shap_utils.py               ← Reusable SHAP module
├── figures/
│   ├── shap_waterfall.png
│   ├── shap_beeswarm.png
│   └── feature_importance.png
└── verification-log.md
```

## Methodology

- Loaded California Housing dataset (20,640 obs, 8 features) from sklearn
- Diagnosed train/test leakage bug in RF evaluation (R² inflated from 0.97 → corrected ~0.81)
- Identified MDI causal overclaiming flaw; replaced with permutation importance + proper framing
- Tuned RF with GridSearchCV (n_estimators, max_depth, max_features; 3-fold CV)
- Compared Ridge, RF (default), RF (tuned), and GradientBoostingRegressor on Test RMSE and R²
- Generated SHAP waterfall plots for 3 observations and beeswarm for the full test set
- Built reusable `src/shap_utils.py` module and interactive Streamlit dashboard

## Key Findings

- **RF (tuned) outperforms Ridge** substantially: Test R² ≈ 0.82 vs Ridge ≈ 0.60
- **GBR competitive with RF**: comparable R² with deterministic boosting
- **MDI vs SHAP diverge**: MDI over-ranks continuous features due to cardinality bias; SHAP confirms MedInc as #1 but rebalances mid-tier features
- **Diminishing returns beyond ~200 trees**: learning curve flattens, supporting default n_estimators=100 for production

> ⚠️ **Causal caveat:** Feature importance (MDI or SHAP) reflects predictive relevance, not causal effect. MedInc is correlated with school quality, safety, and labor market access — confounders that require Double Machine Learning (Ch 24) to isolate.

## Dependencies
See `requirements.txt`. Core: `scikit-learn`, `shap`, `streamlit`, `plotly`, `pandas`, `numpy`.
