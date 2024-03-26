import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, value=None, results=None, true_branch=None, false_branch=None):
        self.feature = feature  # 当前节点的划分特征
        self.value = value  # 划分特征的取值（仅针对离散特征）
        self.results = results  # 叶节点的结果（类别分布）
        self.true_branch = true_branch  # 左子树
        self.false_branch = false_branch  # 右子树

def entropy(data):
    # 计算数据集的熵
    labels = [label for _, label in data]
    label_counts = Counter(labels)
    probs = [count / len(labels) for count in label_counts.values()]
    return -sum(p * np.log2(p) for p in probs if p != 0)

def split_data(data, feature_index, value):
    # 根据特征和特征值划分数据集
    true_data = [(sample, label) for sample, label in data if sample[feature_index] == value]
    false_data = [(sample, label) for sample, label in data if sample[feature_index] != value]
    return true_data, false_data

def information_gain(data, feature_index, unique_values):
    # 计算信息增益
    entropy_before = entropy(data)
    total_samples = len(data)
    entropy_after = sum(len(true_data) / total_samples * entropy(true_data) +
                        len(false_data) / total_samples * entropy(false_data)
                        for true_data, false_data in [split_data(data, feature_index, value)
                                                      for value in unique_values])
    return entropy_before - entropy_after

def find_best_split(data, available_features):
    # 找到最佳的划分特征
    best_gain = 0
    best_feature = None
    best_value = None
    for feature_index in available_features:
        values = set(sample[feature_index] for sample, _ in data)
        gain = information_gain(data, feature_index, values)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature_index
            best_value = None
    return best_feature, best_value

def build_tree(data, available_features):
    # 递归构建决策树
    if len(set(label for _, label in data)) == 1:
        return Node(results=Counter(label for _, label in data))
    if len(available_features) == 0:
        return Node(results=Counter(label for _, label in data))
    
    best_feature, best_value = find_best_split(data, available_features)
    true_branch_data, false_branch_data = split_data(data, best_feature, best_value)
    true_branch = build_tree(true_branch_data, available_features)
    false_branch = build_tree(false_branch_data, available_features)
    return Node(feature=best_feature, value=best_value, true_branch=true_branch, false_branch=false_branch)

def print_tree(node, indent=''):
    # 打印决策树
    if node.results is not None:
        print(indent + str(node.results))
    else:
        print(indent + 'Feature ' + str(node.feature))
        print(indent + 'Value: ' + str(node.value))
        print_tree(node.true_branch, indent + '  ')
        print_tree(node.false_branch, indent + '  ')

# 示例数据
X_train = np.array([[1, 1], [1, 0], [0, 1], [0, 0], [1, 1], [0, 0]])
y_train = np.array([1, 1, 0, 0, 1, 0])

data = list(zip(X_train, y_train))
num_features = X_train.shape[1]
available_features = set(range(num_features))

# 构建决策树
tree = build_tree(data, available_features)

# 打印决策树
print_tree(tree)