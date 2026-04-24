# Lab 20: Time Series Diagnostics & Advanced Decomposition
**ECON 5200: Causal Machine Learning & Applied Analytics**

## Objective
Diagnose and correct common time series decomposition pitfalls, implement advanced decomposition techniques, and build a reusable production module for economic time series analysis.

## How to Reproduce
```bash
pip install -r requirements.txt
jupyter notebook notebooks/lab_ch20_diagnostic.ipynb
streamlit run src/app.py
```

## Methodology
- Diagnosed and fixed broken STL decomposition (additive on multiplicative data — required log-transform)
- Fixed misspecified ADF test (wrong regression parameter — changed from `regression='n'` to `regression='ct'`)
- Applied MSTL to simulated hourly electricity demand with daily (24h) and weekly (168h) seasonal cycles
- Implemented moving block bootstrap for GDP trend uncertainty bands (block_size=8, n_bootstrap=200)
- Detected structural breaks with PELT algorithm and ran per-regime ADF/KPSS stationarity tests
- Built reusable `decompose.py` module with `run_stl()`, `test_stationarity()`, `detect_breaks()`, `run_mstl()`, `block_bootstrap_trend()`
- Built interactive Streamlit dashboard with FRED integration, decomposition panels, stationarity tests, and bootstrap CIs

## Key Findings
- GDP is I(1) — non-stationary in levels, stationary after first differencing
- Retail sales require log-transform before STL (multiplicative seasonality — seasonal amplitude grew 2x+ from 2000 to 2023)
- MSTL successfully separates daily and weekly electricity demand cycles (residual std ~15 MW, matching true noise level)
- Block bootstrap confidence bands are wider around recessions (2008, 2020), confirming higher trend uncertainty during volatile periods
- PELT detects structural breaks near 2008 and 2020 — GDP growth is stationary within regimes

## Repository Structure

econ-lab-20-time-series/
├── README.md
├── requirements.txt
├── notebooks/
│   └── lab_ch20_diagnostic.ipynb
├── src/
│   ├── decompose.py
│   └── app.py
├── figures/
│   └── LINKTOFIGURES.md
└── verification-log.md
