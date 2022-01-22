import sys

sys.path.append("../work")

from calculate import *
import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def df():
    df_test = pd.DataFrame(np.array([[1, 2, 3, 4, 5], [4, 0, 0, 6, 5]]))
    yield {"df_test": df_test}


def test_calculate_correlations(df):
    df_test = df["df_test"]
    corr = calculate_correlations(df=df_test, columns=df_test.columns)
    assert len(corr) == 10
    assert type(corr) == dict


def test_calculate_ratio(df):
    df_test = df["df_test"]
    ratio = calculate_ratio(df=df_test, numerator=0, denominator=2)
    assert len(ratio) == 2
    assert type(ratio) == list
