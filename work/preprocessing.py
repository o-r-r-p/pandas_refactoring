import numpy as np
import pandas as pd


def clean_nan(df: pd.DataFrame, columns: list, value: float) -> pd.DataFrame:
    for column in columns:
        df.loc[df[column] < value, column] = np.nan
    return df


def int_to_datetime(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    df[date_column] = pd.to_datetime(df[date_column].astype(str))
    return df


def create_month_column(df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    df["MONTH"] = df[date_column].dt.month
    return df
