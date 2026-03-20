"""第二个 sklearn 例子：单特征房价预测（KNN 回归）。

流程概览：准备数据 -> 划分训练/测试 -> 训练 KNN 回归 -> 在测试集上评估 -> 预测新样本。
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


def main() -> None:
    # ---------- 1) 准备数据 ----------
    # 只有一个特征：房屋面积 area（单位可理解为 m^2）；目标：房价 price（与 area 同量纲的示例数）
    area = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140], dtype=float)
    price = np.array([100, 118, 135, 150, 170, 188, 210, 225, 245, 265], dtype=float)

    # sklearn 要求特征矩阵 X 形状为 [样本数, 特征数]，不能是一维向量。
    # reshape(-1, 1)：-1 表示自动推断行数，1 表示 1 个特征列 -> 形状 (10, 1)
    X = area.reshape(-1, 1)
    # y：每个样本对应的真实房价，一维即可
    y = price

    # ---------- 2) 划分训练集 / 测试集 ----------
    # 训练集用来 fit；测试集从未参与训练，用来检验泛化能力。
    # test_size=0.2：约 20% 样本作为测试集；random_state：固定随机种子，每次划分结果一致
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print("X_train:", X_train.shape)
    print("y_train:", y_train.shape)
    print("X_test:", X_test.shape)
    print("y_test shape:", y_test.shape)

    # ---------- 3) 训练 KNN 回归模型 ----------
    # KNeighborsRegressor：在特征空间（这里是一维面积）找最近的 k 个训练样本，
    # 用它们的房价取平均，作为新样本的预测值（回归，输出连续数值）。
    # n_neighbors=3：使用 3 个最近邻
    model = KNeighborsRegressor(n_neighbors=3)
    model.fit(X_train, y_train)

    # ---------- 4) 在测试集上评估 ----------
    # 用测试集特征预测，再与测试集真实房价对比
    y_pred = model.predict(X_test)

    # MAE（平均绝对误差）：mean(|y_true - y_pred|)，与房价同单位，越小越好，表示平均偏差多少
    mae = mean_absolute_error(y_test, y_pred)
    # R²（决定系数）：相对“只预测 y 的均值”提升了多少，越接近 1 越好，无量纲
    r2 = r2_score(y_test, y_pred)

    print("n_neighbors:", model.n_neighbors)
    print("test MAE:", round(float(mae), 4))
    print("test R2:", round(float(r2), 4))

    # ---------- 5) 预测新样本 ----------
    # 新房子面积 95，形状必须是 (1, 1)：一行样本、一列特征
    new_area = np.array([[95.0],[105.0]])
    pred_price = model.predict(new_area)
    print("pred price for 95 m^2:", round(float(pred_price[0]), 2))
    print("pred price for 105 m^2:", round(float(pred_price[1]), 2))


if __name__ == "__main__":
    main()
