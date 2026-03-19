"""
读取文件并处理缺失值（初学者示例）

步骤：
1) 用 Pandas 读取 CSV
2) 查看缺失值情况
3) 加载/填充缺失值（数值列用均值，文本列用前向填充或指定值）
"""

from pathlib import Path

import pandas as pd


def main() -> None:
    # 1) 读取文件（脚本同目录下的 sample_data.csv）
    data_dir = Path(__file__).resolve().parent
    csv_path = data_dir / "sample_data.csv"

    df = pd.read_csv(csv_path)
    print("Original data:")
    print(df)
    print()

    # 2) 查看缺失值
    missing = df.isna().sum()
    print("Missing count per column:")
    print(missing)
    print()

    # 3) 加载/填充缺失值
    df_filled = df.copy()

    # 数值列：用该列均值填充
    if "sales" in df_filled.columns:
        df_filled["sales"] = df_filled["sales"].fillna(df_filled["sales"].mean())

    # 文本列：用前一个非空值填充（ffill），最前面缺的用 bfill 补
    if "name" in df_filled.columns:
        df_filled["name"] = df_filled["name"].ffill().bfill()

    print("After filling missing values:")
    print(df_filled)
    print("Remaining missing count:", df_filled.isna().sum().sum())


if __name__ == "__main__":
    main()
