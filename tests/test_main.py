import sys

sys.path.append("../work")

from main import *
import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def test_data():
    file_path = "test_data.csv"
    filter_one = pd.DataFrame(
        np.array([[20190722, 2, 3, 4], [20190711, 1, 6, 4], [20190722, 2, 3, 4]]),
        columns=["DATE", "A", "B", "C"],
    )
    precip_df = pd.DataFrame(
        {
            "PREFECTURE": ["saitama", "tokyo", "saitama", "tokyo", "saitama", "tokyo"],
            "PRCP": [4, 3, 5, 2, 3, 3],
            "SNOW": [1, 2, 0.5, 0.1, 0, 0],
            "MONTH": [
                1,
                1,
                2,
                2,
                2,
                2,
            ],
            "DATE": [20110101, 20110101, 20110210, 20110210, 20110211, 20110211],
        }
    )
    temp_df = pd.DataFrame(
        {
            "PREFECTURE": ["saitama", "tokyo", "saitama", "tokyo", "saitama", "tokyo"],
            "TEMP": [11, 10, 8, 8, 9, 10],
            "DATE": [20110101, 20110101, 20110210, 20110210, 20110211, 20110211],
        }
    )
    corr = {"corr": 0.55555}
    yield {
        "file_path": file_path,
        "filter_one": filter_one,
        "precip_df": precip_df,
        "temp_df": temp_df,
        "corr": corr,
    }


def test_read_csv(test_data):
    path = test_data["file_path"]
    df = pd.read_csv(path)
    assert df.shape == (6, 5)
    assert type(df) == pd.DataFrame


def test_filter_one(test_data):
    df_filter = test_data["filter_one"]
    df_filter_one = df_filter[df_filter["DATE"] == 20190722]
    assert df_filter_one.shape == (2, 4)
    assert type(df_filter_one) == pd.DataFrame


def test_merge(test_data):
    df_precip = test_data["precip_df"]
    df_temp = test_data["temp_df"]
    test_merge = pd.merge(df_precip, df_temp)
    assert test_merge.shape == (6, 6)
    assert type(test_merge) == pd.DataFrame


def test_agg_sum(test_data):
    df_agg_sum = test_data["precip_df"]
    monthly_precip_snow = df_agg_sum.groupby("MONTH")[["PRCP", "SNOW"]].agg(sum)
    assert monthly_precip_snow.shape == (2, 2)
    assert type(monthly_precip_snow) == pd.DataFrame
    assert monthly_precip_snow["PRCP"][1] == 7


def test_monthly_avg(test_data):
    df_precip = test_data["precip_df"]
    df_avg_snow = df_precip.groupby("MONTH")["SNOW"].agg(np.mean)
    assert df_avg_snow.shape == (2,)
    assert type(df_avg_snow) == pd.Series
    assert df_avg_snow[1] == 1.5


def test_concat(test_data):
    df_precip = test_data["precip_df"]
    df_temp = test_data["temp_df"]
    df_concat = pd.concat([df_precip, df_temp], axis=1)
    assert df_concat.shape == (6, 8)
    assert type(df_concat) == pd.DataFrame


def test_print_corr(test_data):
    corr = test_data["corr"]
    for key, value in corr.items():
        corr_ = f"Monthly {key} is {value:.4f}"
    assert corr_ == "Monthly corr is 0.5555"
