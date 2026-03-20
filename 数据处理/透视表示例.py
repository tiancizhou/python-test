"""
透视表示例（初学者）

Pandas 透视表：pd.pivot_table()
把“长表”按 行索引、列、取值 重新排列，并可指定聚合方式（sum、mean 等）。
"""

from pathlib import Path

import pandas as pd


def main() -> None:
    data_dir = Path(__file__).resolve().parent
    df = pd.read_csv(data_dir / "sample_data.csv")
    df["sales"] = df["sales"].fillna(df["sales"].mean())
    df["name"] = df["name"].ffill().bfill()

    print("Original data (long format):")
    print(df)
    print()

    # 1) 基本透视：行=name，列=date，值=sales，聚合=sum
    pt1 = pd.pivot_table(df, index="name", columns="date", values="sales", aggfunc="sum")
    print("pivot_table: index=name, columns=date, values=sales, aggfunc='sum'")
    print(pt1)
    print()

    # 2) 聚合用 mean，并显示行/列小计（margins）
    pt2 = pd.pivot_table(
        df, index="name", columns="date", values="sales", aggfunc="mean", margins=True
    )
    print("Same + margins=True (row/col totals):")
    print(pt2)
    print()

    # 3) 行=date，列=name（行列对调）
    pt3 = pd.pivot_table(df, index="date", columns="name", values="sales", aggfunc="sum")
    print("pivot_table: index=date, columns=name, values=sales, aggfunc='sum'")
    print(pt3)
    print()

    # 4) 多种聚合：aggfunc 传列表
    pt4 = pd.pivot_table(
        df, index="name", columns="date", values="sales", aggfunc=["sum", "mean"]
    )
    print("aggfunc=['sum','mean'] (multi-level columns):")
    print(pt4)


if __name__ == "__main__":
    main()
