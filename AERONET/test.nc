import monetio as mio
import numpy as np
import pandas as pd
import xarray as xr
from melodies_monet.util import write_util
import os

verbose=False
dfp = df.rename({'siteid':'x'},axis=1).set_index(['time','x'])
columns = dfp.columns.to_list()
columns2 = []
remove_columns = []
for i in np.arange(len(columns)):
    columns2.append(columns[i])
    try:
        dfp[columns2].to_xarray()
        if verbose:
            print('COLUMN SUCCESS:',columns[i])
    except:
        if verbose:
            print('COLUMN FAILURE:',columns[i])
        remove_columns.append(columns[i])
        columns2.remove(columns[i])
if verbose:
    print(columns2)
dft = df.drop(remove_columns,axis=1)
dfp = dfp.drop(remove_columns,axis=1).dropna(subset=['latitude','longitude'])
dfx = dfp.to_xarray()

dsets = []
for s in df.siteid.unique():
    dsets.append(dft.loc[df.siteid == s].set_index(['time']).to_xarray())

from numpy import unique
site_variable = ['siteid','latitude','longitude','aeronet_instrument_number','elevation']

def expand_dims(ds, index=0):
    # first set a new index for the siteid
    ds['x'] = index
    ds = ds.expand_dims(['x'])
    ds = ds.set_coords(['x'])
    # now reduce the site variables to single element variables 
    for sv in site_variable:
        tmp = [unique(ds[sv])[0]]
        ds[sv] = (('x',), tmp)
    return ds

# now site_variable are the single element attributes of the individual site so lets simplify this
for index,d in enumerate(dsets):
    dsets[index] = expand_dims(d,index=index)

# now combine all the datasets for each site into a single dataset
ds = xr.concat(dsets,dim='x').set_coords(site_variable)

t = ds.expand_dims('y').transpose('time','y','x')
write_util.write_ncf(t,outname)