# Lab 23: FedSpeak 2.0 — NLP Pipeline for Central Bank Communications
**ECON 5200: Causal Machine Learning & Applied Analytics**

## Objective
Build and debug a production-grade NLP pipeline for Federal Reserve meeting minutes, comparing traditional TF-IDF representations against modern sentence-transformer embeddings for predicting monetary policy decisions.

## How to Reproduce
```bash
pip install datasets nltk scikit-learn sentence-transformers
jupyter notebook notebooks/lab_ch23_diagnostic.ipynb
```

## Methodology
- Diagnosed three planted errors in a broken NLP pipeline: naive `split()` tokenizer, Harvard GI sentiment dictionary, and misconfigured TF-IDF parameters
- Fixed preprocessing with `nltk.word_tokenize()` and regex to strip non-alphabetic characters
- Replaced Harvard General Inquirer dictionary with Loughran-McDonald — reduces false positive rate from ~51% to under 10% on financial terminology
- Fixed TF-IDF with `min_df=5`, `max_df=0.85`, `ngram_range=(1,2)` to filter noise and capture bigrams like "interest rate" and "labor market"
- Encoded FOMC documents with sentence-transformers (`all-MiniLM-L6-v2`) and compared against TF-IDF for clustering and prediction
- Evaluated predictive power using TimeSeriesSplit logistic regression for tightening vs easing period classification
- Built reusable `fomc_sentiment.py` module with `preprocess_fomc()`, `compute_lm_sentiment()`, and `build_tfidf_matrix()`

## Key Findings
- Harvard GI flagged 51% of "negative" hits as false positives in the first FOMC document — neutral financial terms like capital, debt, and liability
- TF-IDF and sentence-transformer embeddings achieved comparable AUC (0.60-0.80) for predicting rate decisions
- TF-IDF may edge out embeddings for this task because tightening periods use distinctive vocabulary ("inflation", "restrictive", "overheating") that TF-IDF captures directly
- Embeddings excel when semantic meaning matters more than vocabulary overlap

## Repository Structure
- README.md
- requirements.txt
- notebooks/lab_ch23_diagnostic.ipynb
- src/fomc_sentiment.py
- figures/LINKTOFIGURES.md
