import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate some synthetic data for clustering
np.random.seed(42)
X_unsupervised, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.60, random_state=42)

# Initialize and train the K-Means model
n_clusters = 3
model_unsupervised = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto') # Added n_init for compatibility
clusters = model_unsupervised.fit_predict(X_unsupervised)

# Get the cluster centers
centers = model_unsupervised.cluster_centers_

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(X_unsupervised[:, 0], X_unsupervised[:, 1], c=clusters, cmap='viridis', label='Data Points')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Cluster Centers')
plt.title(f'Unsupervised Learning: K-Means Clustering (Number of Clusters = {n_clusters})')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()

# Demonstrate model output difference
print("\nUnsupervised Learning (K-Means) - Cluster Assignments for the first 10 data points:")
print(clusters[:10])
print("\nUnsupervised Learning (K-Means) - Cluster Centers:")
print(centers)