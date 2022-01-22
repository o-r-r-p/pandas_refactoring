from ctypes import Union
import numpy as np
import pandas as pd
import itertools


def calculate_correlations(df: pd.DataFrame, columns: list) -> dict:
    corrs = dict()
    for pair in itertools.combinations(columns, 2):
        corr = df[[pair[0], pair[1]]].corr().values[0, 1]
        corrs[f"{pair[0]} and {pair[1]}"] = corr
    return corrs


def calculate_ratio(
    df: pd.DataFrame, numerator: Union, denominator: Union
) -> list:
    ratio = []
    for i, row in df[[numerator, denominator]].iterrows():
        try:
            ratio.append(float(row[numerator]) / float(row[denominator]))
        except:
            ratio.append(np.nan)
    return ratio
