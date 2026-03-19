"""
NumPy + Pandas + Matplotlib：三个模块去重版示例（初学者友好）

要点：
- “生成数据”只写一次（避免你在三个版本里重复代码）
- 分别用三个小函数对应：NumPy 生成/制造缺失、Pandas 填充和移动平均、Matplotlib 画图
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

import matplotlib  # pyright: ignore[reportMissingImports]

matplotlib.use("Agg")  # 不弹窗，直接保存图片
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]


def build_data(n: int = 30, seed: int = 0) -> tuple[list[datetime], np.ndarray]:
    """只负责生成“时间序列 + NaN 缺失”，避免重复代码。"""
    dates = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(n)]

    x = np.arange(n)
    rng = np.random.default_rng(seed)

    sales = 10 + 0.4 * x + np.sin(2 * np.pi * x / 10) + rng.normal(0, 1.5, size=n)
    sales = sales.astype(float)

    # 制造缺失值：每隔 7 天缺一次
    sales[::7] = np.nan

    return dates, sales


def numpy_demo(sales: np.ndarray) -> None:
    """NumPy：展示原始销量（包含 NaN）。"""
    print("numpy: sales with NaN (head) ->", sales[:10])


def pandas_process(dates: list[datetime], sales: np.ndarray) -> pd.DataFrame:
    """Pandas：填充缺失值 + 计算 3 天移动平均。"""
    df = pd.DataFrame({"date": dates, "sales": sales})

    df["sales_filled"] = df["sales"].ffill().bfill()
    df["ma3"] = df["sales_filled"].rolling(window=3).mean()

    return df


def matplotlib_demo(df: pd.DataFrame, out_file: Path) -> None:
    """Matplotlib：画图并保存。"""
    plt.figure(figsize=(8, 4))
    plt.plot(df["date"], df["sales_filled"], label="sales_filled")
    plt.plot(df["date"], df["ma3"], label="ma3 (rolling mean)", linewidth=2)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_file, dpi=150)
    plt.close()


if __name__ == "__main__":
    dates, sales = build_data()

    # 1) NumPy 演示：只看原始 sales（含 NaN）
    numpy_demo(sales)

    # 2) Pandas 处理：填充 NaN + 移动平均
    df = pandas_process(dates, sales)
    print("pandas: head ->")
    print(df.head(8))

    # 3) Matplotlib 画图：保存到 PNG
    out_dir = Path(__file__).resolve().parent
    out_file = out_dir / "timeseries_simple_no_dup.png"
    matplotlib_demo(df, out_file)
    print("saved plot to:", out_file)

