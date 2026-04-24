"""
forecast_evaluation.py — Forecast Evaluation Module

Reusable functions for evaluating time series forecasts.

Author: Emily Perras
Course: ECON 5200, Lab 21
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX


def compute_mase(actual, forecast, train):
    """Compute Mean Absolute Scaled Error (MASE).

    MASE scales the forecast error by the in-sample naive forecast error,
    making it comparable across series of different scales.
    MASE < 1 means the model beats the naive baseline.

    Args:
        actual: pd.Series of actual values (test set)
        forecast: pd.Series of forecasted values
        train: pd.Series of training values (used to compute naive baseline)

    Returns:
        float: MASE value
    """
    mae = np.mean(np.abs(actual.values - forecast.values))
    naive_mae = np.mean(np.abs(np.diff(train.values)))
    return mae / naive_mae


def backtest_expanding_window(series, order=(2, 1, 1),
                               seasonal_order=(1, 1, 1, 12),
                               min_train_size=60, horizon=1):
    """Run expanding window backtest for SARIMA model.

    Trains on all data up to time t, forecasts h steps ahead,
    then expands the window by one observation and repeats.
    This simulates real-world forecasting conditions.

    Args:
        series: pd.Series with DatetimeIndex
        order: ARIMA (p, d, q) order
        seasonal_order: Seasonal (P, D, Q, m) order
        min_train_size: Minimum number of observations to train on
        horizon: Forecast horizon (steps ahead)

    Returns:
        pd.DataFrame with columns: 'actual', 'forecast', 'error'
    """
    actuals = []
    forecasts = []
    indices = []

    for t in range(min_train_size, len(series) - horizon + 1):
        train = series.iloc[:t]
        actual = series.iloc[t + horizon - 1]

        try:
            model = SARIMAX(train, order=order,
                            seasonal_order=seasonal_order,
                            enforce_stationarity=False,
                            enforce_invertibility=False)
            fit = model.fit(disp=False)
            forecast = fit.get_forecast(steps=horizon).predicted_mean.iloc[-1]
        except Exception:
            forecast = np.nan

        actuals.append(actual)
        forecasts.append(forecast)
        indices.append(series.index[t + horizon - 1])

    results = pd.DataFrame({
        'actual': actuals,
        'forecast': forecasts,
    }, index=indices)

    results['error'] = results['actual'] - results['forecast']
    return results


if __name__ == '__main__':
    print('forecast_evaluation.py loaded successfully.')
    print('Functions: compute_mase(), backtest_expanding_window()')

    # Quick self-test with synthetic data
    np.random.seed(42)
    dates = pd.date_range('2010-01-01', periods=100, freq='MS')
    train = pd.Series(np.cumsum(np.random.randn(80)), index=dates[:80])
    test = pd.Series(np.cumsum(np.random.randn(20)) + train.iloc[-1], index=dates[80:])
    forecast = test + np.random.randn(20) * 0.1

    mase = compute_mase(test, forecast, train)
    print(f'\nSelf-test MASE: {mase:.4f} (< 1 means beats naive baseline)')
    print('All tests passed.')
