import xarray as xr
import numpy as np
import math

data_source = "../data_source/data.grib"
earth_radius = 6371.2229  #km
absolute_zero = -273.15 #Celsius
nlat_cells = 1440

def open_data():
    dataset = xr.open_dataset(data_source, engine="cfgrib", decode_timedelta=None)
    return dataset

def extract_data(dataset: xr.Dataset, height: float):
    d = dataset.sel(isobaricInhPa=height)
    return d["t"], d["z"]

def get_time(dataset: xr.Dataset, time: int):
    return dataset.isel(time=time)

def integrate_parallel(dataset: xr.Dataset, latitude: float):
    v = math.cos(latitude) * earth_radius / nlat_cells
    parallel = dataset.sel(latitude=latitude)
    return np.sum(parallel) * v

def integrate(dataset: xr.Dataset):
    cosine_latitude = np.cos(np.radians(dataset.coords["latitude"]))
    ring_radius = cosine_latitude * earth_radius
    integrated_latitude = np.sum(dataset.values, axis=0) * ring_radius / nlat_cells
    integrated = np.sum(integrated_latitude) * .25
    return integrated


