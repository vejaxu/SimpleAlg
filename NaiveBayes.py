import numpy as np

class NaiveBayes:
    def __init__(self):
        self.classes = None
        self.class_prior = None
        self.feature_likelihoods = None

    def fit(self, X, y):
        self.classes = np.unique(y)
        num_classes = len(self.classes)
        num_features = X.shape[1]

        # 计算先验概率
        self.class_prior = np.zeros(num_classes)
        for i, c in enumerate(self.classes):
            self.class_prior[i] = np.sum(y == c) / len(y)

        # 计算条件概率
        self.feature_likelihoods = np.zeros((num_classes, num_features))
        for i, c in enumerate(self.classes):
            class_samples = X[y == c]
            total_samples = len(class_samples)
            for j in range(num_features):
                feature_counts = np.sum(class_samples[:, j] == 1)
                self.feature_likelihoods[i, j] = (feature_counts + 1) / (total_samples + 2)  # 拉普拉斯平滑

    def predict_proba(self, X):
        num_samples = X.shape[0]
        num_classes = len(self.classes)
        probs = np.zeros((num_samples, num_classes))

        for i in range(num_samples):
            for j in range(num_classes):
                likelihood = np.prod(self.feature_likelihoods[j, :] ** X[i, :] *
                                     (1 - self.feature_likelihoods[j, :]) ** (1 - X[i, :]))
                probs[i, j] = self.class_prior[j] * likelihood

        return probs / np.sum(probs, axis=1, keepdims=True)

    def predict(self, X):
        return np.argmax(self.predict_proba(X), axis=1)

# 示例数据
X_train = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
y_train = np.array([1, 1, 0, 0])

# 创建并训练朴素贝叶斯模型
nb = NaiveBayes()
nb.fit(X_train, y_train)

# 进行预测
predictions_proba = nb.predict_proba(X_train)
predictions = nb.predict(X_train)
print("Predictions (probabilities):", predictions_proba)
print("Predictions:", predictions)