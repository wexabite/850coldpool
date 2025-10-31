from data_handler import open_data, get_time, integrate, get_instantaneous_mean, get_area_factor
import display as dp
import numpy as np

import math

days_in_year = 91
number_of_years = 24

lat_top = 90
lat_bottom = 80

title = "Mean Temperature at 850hPa, 80N - 90N"
xlabel = "Day # in Meteo Autumn"
ylabel = "Mean Temperature, °C"

set_2020_25 = open_data("data")
t850 = set_2020_25["t"].sel(latitude=slice(lat_top, lat_bottom))

set_1940_99 = open_data("data_2")
t850_2 = set_1940_99["t"].sel(latitude=slice(lat_top, lat_bottom))

def get_multi_series(dataset, start, years):
    series = [[]] * years

    for i in range(years):
        year_start = start + i * days_in_year
        year_series = [0.] * days_in_year
        print(i, f"{i*days_in_year}/{days_in_year*years}")

        for j in range(days_in_year):
            time_frame = get_time(dataset, year_start + j)
            year_series[j] = integrate(time_frame)#.values

        series[i] = year_series
    return series

def get_single_series(dataset, start, days):
    series = [0.] * days
    for i in range(days):
        time_frame = get_time(dataset, start + i)
        series[i] = integrate(time_frame)#.values
    return series

series_1940_99 = get_multi_series(t850_2, 0, 59)
series_2000_2020 = get_multi_series(t850, 0, 20)

series_2021_2024 = get_multi_series(t850, 21 * days_in_year, 4)
series_2025 = get_single_series(t850, 25 * days_in_year, 54)

series_1940_2020 = np.stack(series_1940_99, series_2000_2020)

dp.set_title(title)
dp.set_xlabel(xlabel)
dp.set_ylabel(ylabel)

black_color_set = [[0., 0., 0.]] * 59
dp.plot_series(series_1940_99, colors=black_color_set, lw=.5)
dp.plot_series(series_2000_2020, colors=black_color_set, lw=.5)
dp.plot_series(series_2021_2024, lw=1.5)
dp.plot_line(series_2025, color=[0., 1., 0.], lw=1.5)

dp.show()