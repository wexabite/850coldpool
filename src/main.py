import data_handler as dat
import display
from display import plot_line, plot_series

time_frames_in_season = 91 * 4
years = 24

dataset = dat.open_data()
t850, z850 = dat.extract_data(dataset,850.0)

series = [[]] * years

t850_splits = dat.split_to_years(t850, years, time_frames_in_season)

for i in range(years):
    t = i * time_frames_in_season
    year_series = [0.] * time_frames_in_season
    print(i, f"{t}/{time_frames_in_season*years}")
    for j in range(time_frames_in_season - 1):
        time_frame = dat.get_time(t850_splits[i], j)
        year_series[j] = dat.integrate(time_frame).values
    series[i] = year_series

plot_series(series)