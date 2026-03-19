"""
NumPy + Pandas + Matplotlib：时间序列数据处理示例

演示内容：
1) 用 NumPy 生成带趋势/季节性/噪声的销量数据
2) 用 Pandas 做缺失值填充和滚动均值（移动平均）
3) 用 Matplotlib 可视化并保存到 PNG 文件
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

# 使用无界面后端，避免在命令行运行时卡住
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def build_demo_df(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    # 60 天数据
    dates = pd.date_range("2026-01-01", periods=60, freq="D")
    regions = ["North", "South", "East"]

    rows: list[dict[str, object]] = []
    for region in regions:
        # 不同区域有不同的基础量和趋势强度
        base = {"North": 120, "South": 90, "East": 100}[region]
        trend = {"North": 0.35, "South": 0.20, "East": 0.28}[region]

        t = np.arange(len(dates))
        # 简单“周周期”季节性 + 随机噪声
        seasonal = 8 * np.sin(2 * np.pi * t / 7)
        noise = rng.normal(loc=0.0, scale=6.0, size=len(dates))

        sales = base + trend * t + seasonal + noise

        # 让销量不出现负数（只是为了示例更合理）
        sales = np.clip(sales, 0, None)

        for d, s in zip(dates, sales):
            rows.append({"date": d, "region": region, "sales": float(s)})

    df = pd.DataFrame(rows)

    # 随机制造缺失值：对每个区域做一点点丢失，方便演示清洗
    missing_mask = rng.random(df.shape[0]) < 0.06
    df.loc[missing_mask, "sales"] = np.nan

    return df


def process_df(df: pd.DataFrame) -> pd.DataFrame:
    # 1) 缺失值填充：用“同区域均值”填
    df = df.copy()
    df["sales_filled"] = df.groupby("region")["sales"].transform(
        lambda s: s.fillna(s.mean())
    )

    # 2) 移动平均：按区域分别滚动计算 7 天移动平均
    df = df.sort_values(["region", "date"])
    df["sales_ma7"] = df.groupby("region")["sales_filled"].transform(
        lambda s: s.rolling(window=7, min_periods=1).mean()
    )

    # 3) 用 NumPy 做一个“数值处理”示例：对所有填充后的 sales 做 z-score 标准化
    values = df["sales_filled"].to_numpy()
    mu = float(np.mean(values))
    sigma = float(np.std(values, ddof=0)) or 1.0
    df["sales_zscore"] = (values - mu) / sigma

    return df


def plot_for_region(df: pd.DataFrame, region: str, out_path: Path) -> None:
    sub = df[df["region"] == region].sort_values("date")

    # 原始 sales（含 NaN）、填充后的 sales、7日移动平均
    plt.figure(figsize=(10, 5))
    plt.plot(sub["date"], sub["sales"], label="sales (raw)", linewidth=1)
    plt.plot(sub["date"], sub["sales_filled"], label="sales (filled)", linewidth=1)
    plt.plot(sub["date"], sub["sales_ma7"], label="sales (MA7)", linewidth=2)

    plt.title(f"Time Series Demo - {region}")
    plt.xlabel("date")
    plt.ylabel("sales")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()


if __name__ == "__main__":
    df0 = build_demo_df()
    df = process_df(df0)

    missing_count = int(df0["sales"].isna().sum())
    print("missing sales count:", missing_count)
    print("df head:")
    print(df.head(8))

    out_dir = Path(__file__).resolve().parent
    out_file = out_dir / "timeseries_demo.png"

    plot_for_region(df, region="North", out_path=out_file)
    print("saved plot to:", out_file)

