"""第一个 sklearn 例子：鸢尾花分类（初学者版）。"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def main() -> None:
    # 1) 加载数据
    iris = load_iris()
    X = iris.data
    y = iris.target

    # 2) 切分训练集/测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3) 训练模型（KNN）
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    # 4) 预测与评估
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("测试集准确率:", round(acc, 4))
    print("前5个预测值:", y_pred[:5])
    print("前5个真实值:", y_test[:5])


if __name__ == "__main__":
    main()

