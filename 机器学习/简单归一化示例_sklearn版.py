"""简单归一化示例（sklearn版）：MinMaxScaler + StandardScaler。"""

import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def main() -> None:
    # sklearn 里通常用二维特征矩阵：shape = (样本数, 特征数)
    x = np.array([50, 60, 80, 100, 120], dtype=float).reshape(-1, 1)
    print("原始数据:\n", x.ravel())

    # 1) Min-Max 归一化到 [0, 1]
    mm = MinMaxScaler()
    x_mm = mm.fit_transform(x)
    print("MinMaxScaler:\n", np.round(x_mm.ravel(), 4))

    # 2) 标准化到“均值约 0、标准差约 1”
    ss = StandardScaler()
    x_ss = ss.fit_transform(x)
    print("StandardScaler:\n", np.round(x_ss.ravel(), 4))

    print("标准化后均值:", round(float(x_ss.mean()), 6))
    print("标准化后标准差:", round(float(x_ss.std(ddof=0)), 6))


if __name__ == "__main__":
    main()

