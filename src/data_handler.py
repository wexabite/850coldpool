import xarray as xr
import numpy as np
import math

data_source = "../data_source/data.grib"
earth_radius = 6371.2229  #km
absolute_zero = -273.15 #Celsius
nlon_cells = 1440
nlat_cells = 121

def open_data():
    dataset = xr.open_dataset(data_source,
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

def integrate(t850: xr.Dataset):
    t850_C = t850.to_numpy() + absolute_zero
    cosine_latitude = np.cos(np.radians(t850.coords["latitude"]))
    ring_radius = cosine_latitude * earth_radius
    integrated_latitude = t850_C.sum(axis=1) * ring_radius / nlon_cells
    return integrated_latitude.sum() * earth_radius / nlat_cells


