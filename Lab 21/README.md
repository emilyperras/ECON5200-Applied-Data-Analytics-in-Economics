# Lab 21: Time Series Forecasting — ARIMA, GARCH & Bootstrap
**ECON 5200: Causal Machine Learning & Applied Analytics**

## Objective
Diagnose and correct a broken ARIMA forecasting pipeline, model S&P 500 conditional volatility with GARCH(1,1), and build a reusable production module for forecast evaluation.

## How to Reproduce
```bash
pip install fredapi pmdarima prophet arch yfinance statsmodels
jupyter notebook notebooks/lab_ch21_diagnostic.ipynb
```

## Methodology
- Diagnosed three planted errors in a broken ARIMA pipeline: d=0 on non-stationary CPI, missing seasonal terms, and skipped Ljung-Box residual diagnostics
- Corrected pipeline to SARIMA(2,1,1)(1,1,1,12) with proper differencing and seasonal structure, verified via Ljung-Box test
- Log-transformed CPI before modeling to handle multiplicative growth structure
- Fit GARCH(1,1) to S&P 500 daily log returns to model conditional volatility clustering
- Built reusable `forecast_evaluation.py` module with `compute_mase()` and `backtest_expanding_window()`

## Key Findings
- Raw CPI is I(1) — non-stationary in levels, stationary after first differencing (ADF p = 0.026)
- SARIMA captures seasonal CPI patterns that plain ARIMA misses
- S&P 500 GARCH(1,1): alpha + beta ≈ 0.98, confirming high volatility persistence
- Ljung-Box at lag 6 is clean (p = 0.38) — short-run residuals are white noise

## Repository Structure
- README.md
- requirements.txt
- notebooks/lab_ch21_diagnostic.ipynb
- src/forecast_evaluation.py
- figures/LINKTOFIGURES.md
