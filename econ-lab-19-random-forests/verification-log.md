# Verification Log — Lab 19 AI Expansion
## ECON 5200 · P.R.I.M.E. Audit Trail

---

### P.R.I.M.E. Prompt Used

**[Prep]** Expert Python Data Scientist specializing in SHAP explanations,
interactive visualizations, and scikit-learn production workflows.

**[Request]** Two artifacts:
1. `src/shap_utils.py` — reusable module with `explain_prediction()`,
   `global_importance()`, `compare_importance()`, type hints, docstrings,
   error handling, and a `__main__` demo block.
2. `app.py` — Streamlit dashboard with Plotly panels for model comparison,
   SHAP beeswarm, learning curve, and MDI/SHAP toggle. Sliders for
   `n_estimators` and `max_features`. Waterfall for selected observation.

**[Iterate]** Used `plotly.graph_objects`, `shap.TreeExplainer`, `streamlit`,
`sklearn`. Matched variable names from lab: `X_train`, `X_test`, `y_train`,
`y_test`, `data.feature_names`.

**[Mechanism Check]** Inline comments explain:
- TreeExplainer vs KernelExplainer
- SHAP additivity / Shapley property
- Why we re-fit inside the Streamlit callback (observer pattern)
- MDI cardinality bias

**[Evaluate]** Dashboard reveals:
- n_estimators plateau: Test R² stabilizes around 200 trees
- MDI vs SHAP divergence: MDI over-ranks MedInc; SHAP confirms it's #1 but
  rebalances AveOccup and HouseAge
- Marginal value of additional trees: near-zero beyond ~200

---

### What AI Generated
- Full structure of `shap_utils.py` (three functions + `__main__` block)
- Full structure of `app.py` (all four panels + sidebar controls)
- `requirements.txt`

### What I Changed / Verified
- [ ] Confirmed `shap.Explanation` API matches installed SHAP version (>=0.44)
- [ ] Confirmed `check_additivity=False` prevents slow validation warning
- [ ] Confirmed `@st.cache_resource` used correctly for fitted models (not `@st.cache_data`)
- [ ] Verified `matplotlib.use("Agg")` prevents display errors in Streamlit server context
- [ ] Confirmed waterfall plot renders correctly for boundary indices (idx=0, idx=len-1)
- [ ] Ran `if __name__ == "__main__"` block in shap_utils.py — all three figures saved to figures/
- [ ] Confirmed requirements.txt matches all imports in both files

### Human Judgment Applied
- Added causal warning section in explainer text (AI did not include this by default)
- Added `IndexError` guard in `explain_prediction()` — AI generated bare array access
- Normalized SHAP importance in `compare_importance()` for fair visual comparison with MDI
- Kept GBR hyperparameters fixed (200 trees, lr=0.1) so sliders only affect RF,
  making the comparison cleaner for the lab's purpose
