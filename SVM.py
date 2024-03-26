import numpy as np

class SVM:
    def __init__(self, learning_rate=0.01, regularization_strength=1000, num_iterations=1000):
        self.learning_rate = learning_rate  # 学习率
        self.regularization_strength = regularization_strength  # 正则化强度
        self.num_iterations = num_iterations  # 迭代次数
        self.weights = None  # 权重
        self.bias = None  # 偏置项

    def hinge_loss(self, X, y):
        # 计算Hinge Loss
        distances = 1 - y * (np.dot(X, self.weights) - self.bias)
        return np.maximum(0, distances)

    def gradient(self, X, y):
        # 计算梯度
        if len(y.shape) == 1:
            y = np.expand_dims(y, axis=1)
        distances = 1 - y * (np.dot(X, self.weights) - self.bias)
        grad = np.zeros_like(self.weights)
        for i, d in enumerate(distances):
            if max(0, d) == 0:
                grad += self.weights
            else:
                grad += self.weights - self.regularization_strength * y[i] * X[i]
        return grad

    def fit(self, X, y):
        # 初始化参数
        self.weights = np.zeros(X.shape[1])
        self.bias = 0

        # 使用梯度下降优化参数
        for _ in range(self.num_iterations):
            gradient = self.gradient(X, y)
            self.weights -= self.learning_rate * gradient
            self.bias -= self.learning_rate * np.sum(gradient)

    def predict(self, X):
        # 预测输出
        return np.sign(np.dot(X, self.weights) - self.bias)

# 示例数据
X_train = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y_train = np.array([1, 1, -1, -1])

# 创建并训练SVM模型
svm = SVM()
svm.fit(X_train, y_train)

# 进行预测
predictions = svm.predict(X_train)
print("Predictions:", predictions)
