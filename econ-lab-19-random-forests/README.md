%%writefile README.md
# Lab 19: Tree-Based Models and Random Forests

## Objective
This project compares Ridge Regression, Random Forest, tuned Random Forest, and Gradient Boosting on the California Housing dataset. It also uses SHAP to interpret model predictions.

## Methods
- Train/test split
- Ridge Regression benchmark
- Random Forest model
- GridSearchCV tuning
- Gradient Boosting comparison
- MDI, permutation importance, and SHAP importance
- Plotly dashboard for model comparison and SHAP explanations

## AI Expansion
The AI expansion creates a Plotly dashboard with SHAP integration. It includes model comparison, global SHAP importance, and a local explanation for one prediction.

## How to Reproduce
1. Open the notebook in Google Colab.
2. Run all cells from top to bottom.
3. Install any missing packages if prompted.
4. Review the model comparison, SHAP plots, and Plotly dashboard outputs.

## Files
- `notebooks/lab_19_random_forests.ipynb`
- `src/shap_utils.py`
- `README.md`
- `requirements.txt`
- `verification-log.md`
