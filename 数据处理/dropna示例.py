"""
dropna 用法示例（初学者）

dropna() 用来删除含有缺失值（NaN）的行或列。
常用参数：how, subset, axis
"""

from pathlib import Path

import pandas as pd


def main() -> None:
    data_dir = Path(__file__).resolve().parent
    df = pd.read_csv(data_dir / "sample_data.csv")

    print("Original data (with missing):")
    print(df)
    print("Shape:", df.shape)
    print("Missing per column:")
    print(df.isna().sum())
    print()

    # 1) 默认：删除“任意一列有缺失”的行
    d1 = df.dropna()
    print("dropna()  [drop row if ANY column is NaN]:")
    print(d1)
    print("Shape:", d1.shape)
    print()

    # 2) how='all'：只删除“整行全是缺失”的行
    d2 = df.dropna(how="all")
    print("dropna(how='all')  [drop row only if ALL are NaN]:")
    print(d2)
    print("Shape:", d2.shape)
    print()

    # 3) subset：只根据指定列是否有缺失来决定是否删行
    d3 = df.dropna(subset=["sales"])
    print("dropna(subset=['sales'])  [drop row if sales is NaN]:")
    print(d3)
    print("Shape:", d3.shape)
    print()

    d4 = df.dropna(subset=["name"])
    print("dropna(subset=['name'])  [drop row if name is NaN]:")
    print(d4)
    print("Shape:", d4.shape)
    print()

    # 4) axis=1：按列删，删除“含有缺失”的列
    d5 = df.dropna(axis=1)
    print("dropna(axis=1)  [drop column that has any NaN]:")
    print(d5)
    print("Shape:", d5.shape)


if __name__ == "__main__":
    main()
