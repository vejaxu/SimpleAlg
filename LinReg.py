import numpy as np


class LinearRegression:
    def __init__(self):
        self.coef_ = None #系数
        self.intercept_ = None #截距
    
    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        n_samples, n_features = X.shape

        X_with_intercept = np.c_[np.ones((n_samples, 1)), X]

        self.theta_ = np.linalg.inv(X_with_intercept.T @ X_with_intercept) @ X_with_intercept.T @ y
        self.intercept = self.theta_[0]
        self.coef_ = self.theta_[1:]

    def predict(self, X):
        X = np.array(X)
        n_samples, _ = X.shape
        X_with_intercept = np.c_[np.ones((n_samples, 1)), X]
        return X_with_intercept @ self.theta_

X_train = np.array([[1], [2], [3], [4], [5]])
print(X_train.shape)
y_train = np.array([2, 3, 4, 5, 6])
X_test = np.array([[6], [7]])

lr = LinearRegression()
lr.fit(X_train, y_train)

predictions = lr.predict(X_test)
print("predictions:", predictions)