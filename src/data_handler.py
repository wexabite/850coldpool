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
                              #chunks={"time": 200})
    return dataset

def extract_data(dataset: xr.Dataset, height: float):
    d = dataset.sel(isobaricInhPa=height)
    return d["t"], d["z"]

def get_time(dataset: xr.Dataset, time: int):
    return dataset.isel(time=time)

def integrate(t850: xr.Dataset):
    t850_C = t850 + absolute_zero
    cosine_latitude = np.cos(np.radians(t850_C.coords["latitude"]))
    ring_radius = cosine_latitude * earth_radius
    integrated_latitude = t850_C.sum(dim="longitude") * ring_radius / nlon_cells
    return (integrated_latitude.sum(dim="latitude") * earth_radius / nlat_cells)


