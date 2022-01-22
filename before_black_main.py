import numpy as np
import pandas as pd
import preprocessing as pp
import calculate as calc


def main():
    # Read the data
    climate_precip = pd.read_csv(precip_path)
    climate_temp = pd.read_csv(temp_path)

    # Filter one station
    precip_one_station = climate_precip[
        climate_precip["STATION"] == "GHCND:USW00024215"
    ]

    # Inner join, keys: STATION, STATION_NAME, DATE
    precip_temp_one_station = pd.merge(precip_one_station, climate_temp)

    # Clean NaN for less than 0
    precip_temp_one_station = pp.clean_nan(
        df=precip_temp_one_station,
        columns=["DLY-PRCP-PCTALL-GE001HI", "DLY-SNOW-PCTALL-GE030TI"],
        value=0,
    )

    # Convert int to datetime and extract month from date
    precip_temp_one_station = pp.int_to_datetime(
        df=precip_temp_one_station, date_column="DATE"
    )
    precip_temp_one_station = pp.create_month_column(
        df=precip_temp_one_station, date_column="DATE"
    )

    # Calculate monthly amount of rain/snow
    monthly_precip_snow = precip_temp_one_station.groupby("MONTH")[
        ["DLY-PRCP-PCTALL-GE001HI", "DLY-SNOW-PCTALL-GE030TI"]
    ].agg(sum)
    monthly_precip_snow.rename(columns={
        "DLY-PRCP-PCTALL-GE001HI": "SUM_DLY-PRCP-PCTALL-GE001HI",
        "DLY-SNOW-PCTALL-GE030TI": "SUM_DLY-SNOW-PCTALL-GE030TI"},
        inplace=True)

    # Calculate monthly rain/snow ratio
    monthly_precip_snow["rain_snow_ratio"] = calc.calculate_ratio(
        df=monthly_precip_snow,
        numerator="SUM_DLY-PRCP-PCTALL-GE001HI",
        denominator="SUM_DLY-SNOW-PCTALL-GE030TI",
    )

    # Calculate monthly average heat temperature
    avg_heat_temp = precip_temp_one_station.groupby("MONTH")["DLY-HTDD-NORMAL"].agg(
        np.mean
    )
    avg_heat_temp.rename("MEAN_DLY-HTDD-NORMAL", inplace=True)

    # Merge precipitations and cloud data
    monthly_data = pd.concat([monthly_precip_snow, avg_heat_temp], axis=1)

    # Calculate correlations 
    corrs = calc.calculate_correlations(df=monthly_data, columns=monthly_data.columns)

    # Print correlations and create csv.file
    for key, value in corrs.items():
        print(f"Monthly {key} correlation is {value:.4f}")
    monthly_data.to_csv("Monthly_data.csv")


if __name__ == "__main__":
    precip_path = "data/climate_precip.csv"
    temp_path = "data/climate_temp.csv"
    main()
