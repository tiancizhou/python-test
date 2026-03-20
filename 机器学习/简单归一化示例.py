"""简单归一化示例：Min-Max 归一化 + Z-score 标准化。"""

import numpy as np


def main() -> None:
    # 假设这是“房屋面积”特征
    x = np.array([50, 60, 80, 100, 120], dtype=float)
    print("原始数据:", x)

    # 1) Min-Max 归一化：缩放到 [0, 1]
    x_min = x.min()
    x_max = x.max()
    x_minmax = (x - x_min) / (x_max - x_min)
    print("Min-Max 归一化:", np.round(x_minmax, 4))

    # 2) Z-score 标准化：变成“均值约 0，标准差约 1”
    mu = x.mean()
    sigma = x.std(ddof=0)
    x_zscore = (x - mu) / sigma
    print("Z-score 标准化:", np.round(x_zscore, 4))

    print("标准化后均值:", round(float(x_zscore.mean()), 6))
    print("标准化后标准差:", round(float(x_zscore.std(ddof=0)), 6))


if __name__ == "__main__":
    main()

