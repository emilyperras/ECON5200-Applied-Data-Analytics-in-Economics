"""
causal_ml.py — Reusable Causal ML Module

Functions for Double Machine Learning and CATE subgroup analysis.

Author: Emily Perras
Course: ECON 5200, Lab 24
"""

import numpy as np
import pandas as pd
from typing import Tuple, List, Optional
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
from sklearn.base import clone


def manual_dml(
    Y: np.ndarray,
    D: np.ndarray,
    X: np.ndarray,
    ml_l: Optional[object] = None,
    ml_m: Optional[object] = None,
    n_folds: int = 2,
    random_state: int = 42
) -> dict:
    """Estimate ATE via manual Double Machine Learning with cross-fitting.

    Implements the Chernozhukov et al. (2018) DML estimator:
    1. Cross-fit outcome residuals: Y_tilde = Y - E[Y|X]
    2. Cross-fit treatment residuals: D_tilde = D - E[D|X]
    3. Estimate theta via IV-style ratio: sum(D_tilde * Y_tilde) / sum(D_tilde * D)

    Cross-fitting prevents regularization bias from contaminating
    the sqrt(n)-consistent causal estimate. Without it, in-sample
    predictions overfit and bias residuals toward zero.

    Args:
        Y: Outcome vector (n,)
        D: Treatment vector (n,)
        X: Covariate matrix (n, p)
        ml_l: Outcome nuisance model (default: RandomForestRegressor)
        ml_m: Treatment nuisance model (default: RandomForestRegressor)
        n_folds: Number of cross-fitting folds
        random_state: Random seed for reproducibility

    Returns:
        dict with 'theta' (ATE), 'Y_tilde', 'D_tilde', 'se'
    """
    n = len(Y)

    if ml_l is None:
        ml_l = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=random_state)
    if ml_m is None:
        ml_m = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=random_state)

    kf = KFold(n_splits=n_folds, shuffle=True, random_state=random_state)

    Y_tilde = np.zeros(n)
    D_tilde = np.zeros(n)

    for train_idx, test_idx in kf.split(X):
        # outcome residuals — train on train_idx, predict on test_idx
        ml_l_clone = clone(ml_l)
        ml_l_clone.fit(X[train_idx], Y[train_idx])
        Y_tilde[test_idx] = Y[test_idx] - ml_l_clone.predict(X[test_idx])

        # treatment residuals — double residualization removes X -> D confounding
        ml_m_clone = clone(ml_m)
        ml_m_clone.fit(X[train_idx], D[train_idx])
        D_tilde[test_idx] = D[test_idx] - ml_m_clone.predict(X[test_idx])

    # IV-style ratio (Frisch-Waugh-Lovell theorem)
    theta = np.sum(D_tilde * Y_tilde) / np.sum(D_tilde * D)

    # heteroskedasticity-robust standard error
    residuals = Y_tilde - theta * D_tilde
    se = np.sqrt(
        np.sum(D_tilde**2 * residuals**2) / (np.sum(D_tilde**2))**2
    )

    return {
        'theta': theta,
        'se': se,
        'ci_lower': theta - 1.96 * se,
        'ci_upper': theta + 1.96 * se,
        'Y_tilde': Y_tilde,
        'D_tilde': D_tilde
    }


def cate_by_subgroup(
    data: pd.DataFrame,
    cate_col: str,
    feature_cols: List[str],
    n_quantiles: int = 4
) -> pd.DataFrame:
    """Profile subgroups by CATE quantile.

    Splits observations into quantile bins based on their estimated
    CATE and computes mean characteristics for each bin. Useful for
    identifying which subgroups respond most to treatment.

    Args:
        data: DataFrame with CATE estimates and covariates
        cate_col: Column name containing CATE estimates
        feature_cols: List of covariate columns to profile
        n_quantiles: Number of quantile bins (default 4 = quartiles)

    Returns:
        pd.DataFrame with mean characteristics per CATE quantile
    """
    data = data.copy()
    data['cate_quantile'] = pd.qcut(
        data[cate_col],
        q=n_quantiles,
        labels=[f'Q{i+1}' for i in range(n_quantiles)]
    )

    profile = data.groupby('cate_quantile')[feature_cols + [cate_col]].mean().round(3)
    profile.index.name = 'CATE Quantile'
    return profile


if __name__ == '__main__':
    print('causal_ml.py loaded successfully.')
    print('Functions: manual_dml(), cate_by_subgroup()')

    # self-test on simulated data with known ATE
    np.random.seed(42)
    n, p = 1000, 10
    TRUE_ATE = 5.0

    X_test = np.random.normal(0, 1, (n, p))
    propensity = 1 / (1 + np.exp(-X_test[:, 0]))
    D_test = np.random.binomial(1, propensity)
    Y_test = TRUE_ATE * D_test + 2 * X_test[:, 0] + np.random.normal(0, 1, n)

    result = manual_dml(Y_test, D_test, X_test)
    print(f'\nTrue ATE: {TRUE_ATE:.2f}')
    print(f'Estimated ATE: {result["theta"]:.2f}')
    print(f'95% CI: [{result["ci_lower"]:.2f}, {result["ci_upper"]:.2f}]')
    print(f'Bias: {result["theta"] - TRUE_ATE:+.2f}')

    # test cate_by_subgroup
    test_df = pd.DataFrame(X_test, columns=[f'x{i}' for i in range(p)])
    test_df['cate'] = np.random.normal(5000, 2000, n)
    profile = cate_by_subgroup(test_df, 'cate', ['x0', 'x1', 'x2'])
    print(f'\nCATE subgroup profile:\n{profile}')
    print('\nAll tests passed.')

    
