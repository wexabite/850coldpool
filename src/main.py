import data_handler as dat
import display
from display import plot_line, plot_series

days_in_year = 92
years = 24

dataset = dat.open_data()
t850, z850 = dat.extract_data(dataset,850.0)

series = [[]] * years

for i in range(years):
    t = i*days_in_year
    year_series = [0.] * days_in_year
    print(t)
    for j in range(days_in_year):
        time_frame = dat.get_time(t850, t+j)
        year_series[j] = dat.integrate(time_frame).values
    series[i] = year_series

plot_series(series)