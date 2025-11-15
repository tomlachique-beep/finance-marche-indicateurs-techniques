import pandas as pd
import numpy as np

def compute_moving_averages(df, window_short=20, window_long=40, price_col="Dernier"):
    df = df.copy()
    df[f"MA_{window_short}"] = df[price_col].rolling(window_short).mean()
    df[f"MA_{window_long}"] = df[price_col].rolling(window_long).mean()
    return df

def compute_rsi(df, window=14, price_col="Dernier"):
    df = df.copy()
    delta = df[price_col].diff()

    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)

    roll_up = pd.Series(gain).rolling(window).mean()
    roll_down = pd.Series(loss).rolling(window).mean()

    rs = roll_up / roll_down
    rsi = 100 - (100 / (1 + rs))

    df["RSI"] = rsi.values
    return df

def compute_stochastic(df, window=14, high_col="Plus Haut", low_col="Plus Bas", close_col="Dernier"):
    df = df.copy()
    low_min = df[low_col].rolling(window).min()
    high_max = df[high_col].rolling(window).max()
    df["Stochastique"] = 100 * (df[close_col] - low_min) / (high_max - low_min)
    df["Stochastique_moyenne"] = df["Stochastique"].rolling(3).mean()
    return df

def compute_bollinger_bands(df, window=20, price_col="Dernier", num_std=2):
    df = df.copy()
    ma = df[price_col].rolling(window).mean()
    std = df[price_col].rolling(window).std()

    df["Bollinger_MA"] = ma
    df["Bollinger_Haut"] = ma + num_std * std
    df["Bollinger_Bas"] = ma - num_std * std

    return df

def load_excel_sheet(path, sheet_name):
    return pd.read_excel(path, sheet_name=sheet_name)

if __name__ == "__main__":
    # Exemple d'utilisation avec la feuille BMW
    path = "data/Finance_de_marche.xlsx"
    df_bmw = load_excel_sheet(path, "BMW")

    df_bmw = compute_moving_averages(df_bmw)
    df_bmw = compute_rsi(df_bmw)
    df_bmw = compute_stochastic(df_bmw)
    df_bmw = compute_bollinger_bands(df_bmw)

    print(df_bmw.head())
