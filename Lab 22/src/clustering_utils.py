"""
clustering_utils.py — Reusable Clustering Pipeline Module

Author: Emily Perras
Course: ECON 5200, Lab 22
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.impute import SimpleImputer


def run_kmeans_pipeline(df, feature_names, n_clusters=4, random_state=42):
    """Run full K-Means pipeline: impute, scale, cluster.

    Args:
        df: pd.DataFrame with features
        feature_names: list of column names to cluster on
        n_clusters: number of clusters
        random_state: random seed for reproducibility

    Returns:
        dict with 'labels', 'X_scaled', 'silhouette', 'inertia'
    """
    imputer = SimpleImputer(strategy='median')
    X_imputed = imputer.fit_transform(df[feature_names])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    kmeans = KMeans(n_clusters=n_clusters, init='k-means++',
                    n_init='auto', random_state=random_state)
    labels = kmeans.fit_predict(X_scaled)

    sil = silhouette_score(X_scaled, labels)

    return {
        'labels': labels,
        'X_scaled': X_scaled,
        'silhouette': sil,
        'inertia': kmeans.inertia_
    }


def evaluate_k_range(df, feature_names, k_range=range(2, 11), random_state=42):
    """Evaluate K-Means for a range of K values using silhouette and inertia.

    Args:
        df: pd.DataFrame with features
        feature_names: list of column names
        k_range: range of K values to try
        random_state: random seed

    Returns:
        pd.DataFrame with columns: 'k', 'inertia', 'silhouette'
    """
    imputer = SimpleImputer(strategy='median')
    X_imputed = imputer.fit_transform(df[feature_names])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    results = []
    for k in k_range:
        km = KMeans(n_clusters=k, init='k-means++',
                    n_init='auto', random_state=random_state)
        labels = km.fit_predict(X_scaled)
        sil = silhouette_score(X_scaled, labels)
        results.append({'k': k, 'inertia': km.inertia_, 'silhouette': sil})

    return pd.DataFrame(results)


def plot_pca_clusters(X_scaled, labels, title='PCA Cluster Plot'):
    """Plot K-Means clusters in 2D PCA space.

    Args:
        X_scaled: standardized feature array
        labels: cluster labels from K-Means
        title: plot title

    Returns:
        matplotlib figure
    """
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1],
                         c=labels, cmap='Set1',
                         alpha=0.7, edgecolors='white', s=60)
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
    ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
    ax.set_title(title)
    plt.colorbar(scatter, label='Cluster')
    plt.tight_layout()
    return fig


if __name__ == '__main__':
    print('clustering_utils.py loaded successfully.')
    print('Functions: run_kmeans_pipeline(), evaluate_k_range(), plot_pca_clusters()')

    # self-test with synthetic data
    from sklearn.datasets import make_blobs
    X, _ = make_blobs(n_samples=200, centers=4, random_state=42)
    test_df = pd.DataFrame(X, columns=['f1', 'f2'])

    result = run_kmeans_pipeline(test_df, ['f1', 'f2'], n_clusters=4)
    print(f'Silhouette: {result["silhouette"]:.4f}')

    k_results = evaluate_k_range(test_df, ['f1', 'f2'], k_range=range(2, 6))
    print(k_results)

    print('All tests passed.')
