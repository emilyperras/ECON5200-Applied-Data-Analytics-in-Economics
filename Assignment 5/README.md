# Assignment 5: The Sovereign Risk Engine

## Overview

This project develops a machine learning framework to predict sovereign financial crises using cross-country macroeconomic and institutional data. The goal is to simulate how an organization such as the IMF could use predictive analytics to identify countries at elevated risk and allocate monitoring resources more efficiently.

The project compares traditional linear models with regularized methods and logistic classification models. It also evaluates threshold selection under real-world policy constraints such as limited intervention capacity and the high cost of missing a crisis.

---

## Research Question

Can country-level economic and development indicators be used to predict sovereign crisis risk, and how should policymakers choose a classification threshold when false negatives are much more costly than false positives?

---

## Dataset Summary

- Initial countries: 266  
- Final countries after cleaning: 238  
- Indicators retained: 28  
- Training observations: 166  
- Test observations: 72  

Class balance:

- Non-crisis countries: 200  
- Crisis countries: 38  

This creates an imbalanced classification problem where crisis events are relatively rare.

---

## Methods Used

### Regression Models

- Ordinary Least Squares (OLS)
- Ridge Regression
- Lasso Regression

### Classification Model

- Logistic Regression

### Model Evaluation

- Training R²
- Test R²
- RMSE
- Accuracy
- Recall
- ROC-AUC
- PR-AUC
- Confusion Matrix

### Policy Optimization

- Capacity-constrained threshold selection
- F1-optimal threshold selection
- Cost-sensitive threshold optimization

---

## Key Results

### Forecasting GDP / Continuous Prediction

| Model | Test R² | Test RMSE |
|------|---------|-----------|
| OLS | -0.8864 | 2.9015 |
| Ridge | -0.1042 | 2.2199 |
| Lasso | -0.3602 | 2.4637 |

Ridge performed best out-of-sample, showing the value of regularization.

### Crisis Classification

- ROC-AUC: 0.7401  
- PR-AUC: 0.3472  

At threshold τ = 0.50:

- Accuracy: 76.4%
- Recall: 42.9%

### Threshold Optimization

**Capacity-Constrained (≤5 flags):**

- Threshold: 0.88  
- Recall: 14.3%

**F1-Optimal:**

- Threshold: 0.13  
- Recall: 71.4%

**Cost-Minimizing:**

- Threshold: 0.03  
- Expected Cost: $50.07B

This reflects that missing crises is far more expensive than issuing false alarms.

---

## Important Predictors

Frequently selected variables included:

- Population growth
- Natural resource rents
- Health expenditure
- Unemployment
- Inflation
- Urbanization
- Tariff rates

These variables were consistently associated with crisis risk across resamples.

---

## Files

```text
Assignment 5/
└── Assignment 5: The Sovereign Risk Engine.ipynb
