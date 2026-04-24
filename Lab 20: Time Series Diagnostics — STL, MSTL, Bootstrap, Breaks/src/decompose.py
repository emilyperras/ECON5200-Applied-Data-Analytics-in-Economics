"""
decompose.py — Time Series Decomposition & Diagnostics Module

Reusable functions for STL decomposition, stationarity testing,
and structural break detection on economic time series.

Author: Emily Perras
Course: ECON 5200, Lab 20
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL, MSTL
from statsmodels.tsa.stattools import adfuller, kpss
import ruptures as rpt


def run_stl(series, period=12, log_transform=True, robust=True):
    """Apply STL decomposition with optional log-transform.

    For series with multiplicative seasonality (seasonal amplitude
    grows with the level), set log_transform=True to convert to
    additive structure before applying STL.

    Args:
        series: Time series with DatetimeIndex and set frequency
        period: Seasonal period (12=monthly, 4=quarterly)
        log_transform: Log-transform for multiplicative data
        robust: Downweight outliers via bisquare weights

    Returns:
        STL result object with .trend, .seasonal, .resid attributes

    Raises:
        ValueError: if series contains non-positive values with log_transform=True
    """
    if log_transform:
        if (series <= 0).any():
            raise ValueError(
                "Series contains non-positive values. "
                "Cannot log-transform. Set log_transform=False."
            )
        work_series = np.log(series)
    else:
        work_series = series.copy()

    stl = STL(work_series, period=period, robust=robust)
    return stl.fit()


def run_mstl(series, periods):
    """Apply MSTL decomposition for multiple seasonal periods.

    MSTL works by iteratively applying STL for each period,
    removing one seasonal component at a time.

    Args:
        series: Time series with DatetimeIndex and set frequency
        periods: List of seasonal periods e.g. [24, 168] for hourly data

    Returns:
        MSTL result object with .trend, .seasonal, .resid attributes
    """
    mstl = MSTL(series, periods=periods)
    return mstl.fit()


def test_stationarity(series, alpha=0.05):
    """Run ADF + KPSS and return the 2x2 decision table verdict.

    ADF null: unit root (non-stationary)
    KPSS null: stationary

    Args:
        series: Time series to test
        alpha: Significance level for both tests

    Returns:
        dict with 'adf_stat', 'adf_p', 'kpss_stat', 'kpss_p', 'verdict'
        Verdict is one of: 'stationary', 'non-stationary',
        'contradictory', 'inconclusive'
    """
    adf_stat, adf_p, _, _, _, _ = adfuller(series, autolag='AIC', regression='ct')
    kpss_stat, kpss_p, _, _ = kpss(series, regression='ct', nlags='auto')

    adf_rejects = adf_p < alpha
    kpss_rejects = kpss_p < alpha

    if adf_rejects and not kpss_rejects:
        verdict = 'stationary'
    elif not adf_rejects and kpss_rejects:
        verdict = 'non-stationary'
    elif adf_rejects and kpss_rejects:
        verdict = 'contradictory'
    else:
        verdict = 'inconclusive'

    return {
        'adf_stat': adf_stat,
        'adf_p': adf_p,
        'kpss_stat': kpss_stat,
        'kpss_p': kpss_p,
        'verdict': verdict,
    }


def detect_breaks(series, pen=10):
    """Detect structural breaks using the PELT algorithm.

    PELT minimizes a penalized cost function to find changepoints
    in mean and/or variance. Higher penalty = fewer breaks.

    Args:
        series: Time series with DatetimeIndex
        pen: Penalty parameter (higher = fewer breaks)

    Returns:
        List of break dates as pd.Timestamp
    """
    signal = series.values
    algo = rpt.Pelt(model='rbf').fit(signal)
    breakpoints = algo.predict(pen=pen)

    break_dates = [
        series.index[bp - 1]
        for bp in breakpoints
        if bp < len(series)
    ]
    return break_dates


def block_bootstrap_trend(series, n_bootstrap=200, block_size=8, period=4):
    """Generate bootstrap confidence bands for STL trend.

    Block bootstrap preserves autocorrelation by keeping contiguous
    chunks of residuals together instead of shuffling randomly.

    Args:
        series: Log-transformed time series with DatetimeIndex
        n_bootstrap: Number of bootstrap iterations
        block_size: Size of each resampled block
        period: Seasonal period passed to STL

    Returns:
        dict with 'lower', 'upper', 'original_trend' as pd.Series
    """
    np.random.seed(42)
    stl_fit = STL(series, period=period, robust=True).fit()
    original_trend = stl_fit.trend
    original_seasonal = stl_fit.seasonal
    original_resid = stl_fit.resid.values
    n = len(series)

    boot_trends = np.zeros((n_bootstrap, n))

    for b in range(n_bootstrap):
        boot_resid = np.zeros(n)
        idx = 0
        while idx < n:
            start = np.random.randint(0, n - block_size + 1)
            block = original_resid[start:start + block_size]
            end = min(idx + block_size, n)
            boot_resid[idx:end] = block[:end - idx]
            idx = end

        boot_series = pd.Series(
            original_trend.values + original_seasonal.values + boot_resid,
            index=series.index
        )
        boot_series.index.freq = series.index.freq
        boot_stl = STL(boot_series, period=period, robust=True).fit()
        boot_trends[b, :] = boot_stl.trend.values

    return {
        'lower': pd.Series(np.percentile(boot_trends, 5, axis=0), index=series.index),
        'upper': pd.Series(np.percentile(boot_trends, 95, axis=0), index=series.index),
        'original_trend': original_trend
    }


if __name__ == '__main__':
    print('decompose.py loaded successfully.')
    print('Functions: run_stl(), run_mstl(), test_stationarity(), detect_breaks(), block_bootstrap_trend()')
