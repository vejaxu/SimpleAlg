import numpy as np

class Perceptron:
    def __init__(self, lr=0.01, num_iterations=1000):
        self.lr = lr
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.num_iterations):
            for i in range(n_samples):
                prediction = self.predict(X[i])
                update = self.lr * (y[i] - prediction)
                self.weights += update * X[i]
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return np.where(linear_output > 0, 1, 0)
    

X_train = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y_train = np.array([1, 1, 0, 0])

# 创建并训练感知机模型
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

X_test = np.array([1, 2])
# 进行预测
predictions = perceptron.predict(X_train)
print("Predictions:", predictions)
predictions2 = perceptron.predict(X_test)
print("Predictions:", predictions2)