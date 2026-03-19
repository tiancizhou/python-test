"""
分组聚合示例（初学者）

步骤：
1) 读取 CSV 并填充缺失值，得到完整表格
2) 按某一列分组（如 name），对数值列做聚合：sum、mean、count
"""

from pathlib import Path

import pandas as pd


def main() -> None:
    data_dir = Path(__file__).resolve().parent
    csv_path = data_dir / "sample_data.csv"

    df = pd.read_csv(csv_path)
    # 先填充缺失值，便于聚合
    df["sales"] = df["sales"].fillna(df["sales"].mean())
    df["name"] = df["name"].ffill().bfill()

    print("Data (after fill):")
    print(df)
    print()

    # 按 name 分组，对 sales 做多种聚合
    grouped = df.groupby("name", as_index=True)
    agg_df = grouped["sales"].agg(["sum", "mean", "count"])
    agg_df.columns = ["sales_sum", "sales_mean", "sales_count"]

    print("GroupBy name -> sales (sum, mean, count):")
    print(agg_df)
    print()

    # 一次对多列指定不同聚合：按 name 分组，date 取个数，sales 取总和与均值
    multi = df.groupby("name").agg(
        date_count=("date", "count"),
        sales_sum=("sales", "sum"),
        sales_mean=("sales", "mean"),
    )
    print("GroupBy name -> multiple aggs:")
    print(multi)


if __name__ == "__main__":
    main()
