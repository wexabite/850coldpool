import xarray as xr
import numpy as np
import math

data_path = "../data_source/"
earth_radius = 6371.2229  #km
absolute_zero = -273.15 #Celsius
nlon_cells = 1440
nlat_cells = 121
delta_latitude = .25

def open_data(data_file: str):
    dataset = xr.open_dataset(f"{data_path}{data_file}.grib",
                              engine="cfgrib",
                              decode_timedelta=None,)
                              #backend_kwargs={"indexpath": ""},
    return dataset

def extract_data(dataset: xr.Dataset, height: float):
    d = dataset.sel(isobaricInhPa=height)
    return d["t"], d["z"]

def get_time(dataset: xr.Dataset, time: int):
    return dataset.isel(time=time)

def split_to_years(dataset: xr.Dataset, years: int, frames_in_year: int):
    splits = [None] * years
    for i in range(years):
        split = dataset.isel(time=slice(i * frames_in_year, -1 + (i+1) * frames_in_year))
        splits[i] = split
    return splits

def get_area_factor(dataset: xr.Dataset):
    lat_coords = dataset.coords["latitude"]
    Ulat = np.radians(lat_coords + delta_latitude)
    Llat = np.radians(lat_coords)

    area_factor = (np.sin(Ulat) - np.sin(Llat)) #* 2*math.pi * (earth_radius**2)
    return area_factor, np.sum(area_factor.values)

def integrate(t850: xr.Dataset):
    t850_C = t850.to_numpy() + absolute_zero
    area_factor, total_factor = get_area_factor(t850)
    integrated_latitude = t850_C.mean(axis=1) * area_factor
    return integrated_latitude.sum() / total_factor

def get_instantaneous_mean(t850: xr.Dataset):
    t850_C = t850.to_numpy() + absolute_zero
    instant_mean = np.mean(t850_C)
    return instant_mean
