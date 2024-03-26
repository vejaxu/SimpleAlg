import numpy as np

class AdaBoost:
    def __init__(self, num_estimators=50):
        self.num_estimators = num_estimators
        self.estimators = []  # 存储每个弱分类器
        self.estimator_weights = []  # 存储每个弱分类器的权重

    def fit(self, X, y):
        n_samples, n_features = X.shape
        sample_weights = np.ones(n_samples) / n_samples  # 初始化样本权重

        for _ in range(self.num_estimators):
            estimator = DecisionStump()  # 使用决策树桩作为弱分类器
            estimator.fit(X, y, sample_weights)
            y_pred = estimator.predict(X)

            error = np.sum(sample_weights * (y_pred != y))  # 计算误差

            if error > 0.5:  # 如果误差大于0.5，则重新随机初始化样本权重并终止
                sample_weights = np.ones(n_samples) / n_samples
                continue

            estimator_weight = 0.5 * np.log((1 - error) / error)  # 计算弱分类器的权重
            self.estimators.append(estimator)
            self.estimator_weights.append(estimator_weight)

            sample_weights *= np.exp(-estimator_weight * y * y_pred)  # 更新样本权重
            sample_weights /= np.sum(sample_weights)  # 归一化样本权重

    def predict(self, X):
        predictions = np.zeros(X.shape[0])
        for estimator, estimator_weight in zip(self.estimators, self.estimator_weights):
            predictions += estimator.predict(X) * estimator_weight
        return np.sign(predictions)

# 弱分类器，使用决策树桩（单层决策树）作为弱分类器
class DecisionStump:
    def __init__(self):
        self.feature_index = None
        self.threshold = None
        self.alpha = None

    def fit(self, X, y, sample_weights):
        n_samples, n_features = X.shape
        min_error = float('inf')

        for feature_index in range(n_features):
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                y_pred = np.ones(n_samples)
                y_pred[X[:, feature_index] < threshold] = -1
                error = np.sum(sample_weights * (y_pred != y))

                if error < min_error:
                    min_error = error
                    self.feature_index = feature_index
                    self.threshold = threshold

        self.alpha = 0.5 * np.log((1 - min_error) / min_error)

    def predict(self, X):
        n_samples = X.shape[0]
        y_pred = np.ones(n_samples)
        y_pred[X[:, self.feature_index] < self.threshold] = -1
        return y_pred

# 示例数据
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y_train = np.array([-1, -1, 1, 1, 1])

# 创建并训练AdaBoost模型
adaboost = AdaBoost(num_estimators=10)
adaboost.fit(X_train, y_train)

# 进行预测
predictions = adaboost.predict(X_train)
print("Predictions:", predictions)
