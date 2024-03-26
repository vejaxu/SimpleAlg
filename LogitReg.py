import numpy as np

class LogitRegression:
    def __init__(self, lr=0.01, num_iterations=1000):
        self.lr = lr
        self.num_iterations = num_iterations
        self.theta = None
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        n_samples, n_features = X.shape
        X_with_b = np.c_[np.ones((n_samples, 1)), X]

        self.theta = np.zeros(n_features + 1)

        for _ in range(self.num_iterations):
            z = np.dot(X_with_b, self.theta)
            h = self.sigmoid(z)
            gradient = np.dot(X_with_b.T, (h-y)) / n_samples
            self.theta -= self.lr * gradient
        
    
    def predict_proba(self, X):
        X = np.array(X)
        X_with_intercept = np.c_[np.ones((X.shape[0], 1)), X]

        return self.sigmoid(np.dot(X_with_intercept, self.theta))
    
    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)

X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([0, 0, 1, 1, 1])
X_test = np.array([[6], [7]])
lr = LogitRegression()
lr.fit(X_train, y_train)
predictions_proba = lr.predict_proba(X_test)
predictions = lr.predict(X_test)
print("Predictions (probabilities):", predictions_proba)
print("Predictions (binary):", predictions)