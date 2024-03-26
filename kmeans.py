import numpy as np


class KMeans:
    def __init__(self, k, max_iter=300):
        self.n_clusters = k
        self.max_iter = max_iter
        self.centrodis = None #质心
    
    def fit(self, X):
        n_samples, n_features = X.shape

        self.centroids = X[np.random.choice(n_samples, self.n_clusters, replace=False)]

        for _ in range(self.max_iter):
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            labels = np.argmin(distances, axis=1)
            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])
            if np.all(self.centroids == new_centroids):
                break
            self.centroids = new_centroids

    def predict(self, X):
        # 预测样本所属的簇
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        labels = np.argmin(distances, axis=1)
        return labels


X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
kmeans = KMeans(k=2)
kmeans.fit(X)

# 预测簇标签
labels = kmeans.predict(X)
print("Cluster labels:", labels)