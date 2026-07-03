import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def get_preview(df):
    return df.head()


def get_statistics(df):
    return df.describe()


def calculate_moving_average(df, column, window=3):
    df = df.copy()
    df["Moving_Average"] = df[column].rolling(window).mean()
    return df


def calculate_percent_change(df, column):
    df = df.copy()
    df["Pct_Change"] = df[column].pct_change() * 100
    return df


def create_line_plot(df, x_col, y_col):
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df[x_col], df[y_col], marker='o')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f"{y_col} vs {x_col}")
    return fig


def create_moving_average_plot(df, x_col, y_col, window=3):
    df = df.copy()
    df["MA"] = df[y_col].rolling(window).mean()

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df[x_col], df[y_col], label="Original")
    ax.plot(df[x_col], df["MA"], label=f"{window}-Period Moving Average")
    ax.legend()
    return fig
