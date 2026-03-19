"""
NumPy + Pandas + Matplotlib：一个尽量简单的时间序列处理示例。

演示流程：
1) 用 NumPy 生成一条“销量”随时间变化的数据，并制造少量 NaN
2) 用 Pandas 填充缺失值（ffill/bfill）并计算 3 天移动平均
3) 用 Matplotlib 画图并保存为 PNG
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

import matplotlib  # pyright: ignore[reportMissingImports]


matplotlib.use("Agg")  # 不弹窗，直接保存图片
import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]


if __name__ == "__main__":
    # 1) 用 NumPy 生成数据
    n = 30
    dates = pd.date_range("2026-01-01", periods=n, freq="D")

    x = np.arange(n)
    rng = np.random.default_rng(0)
    sales = 10 + 0.4 * x + np.sin(2 * np.pi * x / 10) + rng.normal(0, 1.5, size=n)

    # 制造缺失值：每隔 7 天缺一次
    sales[::7] = np.nan

    df = pd.DataFrame({"date": dates, "sales": sales})

    # 2) 用 Pandas 填充缺失值 + 移动平均
    df["sales_filled"] = df["sales"].ffill().bfill()
    df["ma3"] = df["sales_filled"].rolling(window=3).mean()

    # 3) 可视化
    out_dir = Path(__file__).resolve().parent
    out_file = out_dir / "timeseries_simple.png"

    plt.figure(figsize=(8, 4))
    plt.plot(df["date"], df["sales_filled"], label="sales_filled")
    plt.plot(df["date"], df["ma3"], label="ma3 (rolling mean)", linewidth=2)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_file, dpi=150)
    plt.close()

    print("saved plot to:", out_file)

