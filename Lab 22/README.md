# Lab 22: Clustering Economies — K-Means, PCA & UMAP
**ECON 5200: Causal Machine Learning & Applied Analytics**

## Objective
Diagnose and correct a broken K-Means clustering pipeline on World Bank development indicators, compare PCA vs UMAP for dimensionality reduction, and build a reusable production clustering module.

## How to Reproduce
```bash
pip install wbgapi scikit-learn matplotlib seaborn umap-learn
jupyter notebook notebooks/lab_ch22_diagnostic.ipynb
```

## Methodology
- Diagnosed four planted errors: missing standardization, wrong parameter name (k= vs n_clusters=), PCA applied before scaling, missing random_state
- Fixed pipeline with StandardScaler + SimpleImputer before K-Means
- Clustered 55+ countries on 9 WDI indicators (GDP, life expectancy, infant mortality, Gini, etc.)
- Applied PCA and UMAP for 2D visualization and compared separation quality
- Built synthetic customer segmentation dataset and compared PCA vs UMAP embeddings
- Built reusable clustering_utils.py with run_kmeans_pipeline(), evaluate_k_range(), plot_pca_clusters()

## Key Findings
- Without standardization GDP per capita dominates all cluster distances by a factor of ~1 million
- Silhouette score on WDI data: ~0.64 — reasonable separation across development levels
- UMAP provides better visual cluster separation than PCA for nonlinear data structures
- Synthetic customer data silhouette: ~0.60-0.70 — high separation from well-defined blobs

## Repository Structure
- README.md
- requirements.txt
- notebooks/lab_ch22_diagnostic.ipynb
- src/clustering_utils.py
- figures/LINKTOFIGURES.md
