import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = []
        for sample in X:
            distances = [np.linalg.norm(sample - x) for x in self.X_train]  # 计算样本与训练集样本的距离
            nearest_indices = np.argsort(distances)[:self.k]  # 找出距离最近的k个样本的索引
            nearest_labels = [self.y_train[i] for i in nearest_indices]  # 获取对应的标签
            most_common_label = Counter(nearest_labels).most_common(1)[0][0]  # 统计最常见的标签
            predictions.append(most_common_label)
        return predictions

# 示例数据
X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 6]])
y_train = np.array(['A', 'A', 'B', 'B'])
X_test = np.array([[4, 5], [1, 1]])

# 创建并训练kNN模型
knn = KNN(k=2)
knn.fit(X_train, y_train)

# 进行预测
predictions = knn.predict(X_test)
print("Predictions:", predictions)
