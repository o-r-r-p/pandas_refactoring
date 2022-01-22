import sys

sys.path.append("../work")

from preprocessing import *
import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def df():
    df_clean_nan = pd.DataFrame(np.array([[-1, 0, 3, 4], [-1, 2, -3, 4], [1, 2, 3, 8]]))
    df_int_to_datetime = pd.DataFrame(
        np.array([[20190722, 2, 3, 4], [20190711, 1, 6, 4], [20190721, 2, 3, 4]]),
        columns=["DATE", "A", "B", "C"],
    )
    df_create_month_column = pd.DataFrame(
        np.array([["20190722", 2, 3, 4], ["20190711", 1, 6, 4], ["20190521", 2, 3, 4]]),
        columns=["DATE", "A", "B", "C"],
    )
    yield {
        "clean_nan": df_clean_nan,
        "int_to_datetime": df_int_to_datetime,
        "create_month_column": df_create_month_column,
    }


def test_clean_nan(df):
    df = df["clean_nan"]
    df_test1 = clean_nan(df=df, columns=df.columns, value=-1)
    assert df_test1[0].isnull().sum() == 0
    assert df_test1[1].isnull().sum() == 0
    assert df_test1[2].isnull().sum() == 1


def test_int_to_datetime(df):
    df = df["int_to_datetime"]
    df_test = int_to_datetime(df=df, date_column="DATE")
    assert df_test["DATE"][0] == pd.to_datetime("20190722")
    assert df_test["DATE"][1] == pd.to_datetime("20190711")
    assert df_test["DATE"][2] == pd.to_datetime("20190721")


def test_create_month_column(df):
    df_test = df["create_month_column"]
    df_test["DATE"] = pd.to_datetime(df_test["DATE"])
    df_test = create_month_column(df=df_test, date_column="DATE")
    assert (df_test["MONTH"][0], df_test["MONTH"][1], df_test["MONTH"][2]) == (7, 7, 5)
    assert df_test.shape == (3, 5)
