#!/usr/bin/env python
import monetio as mio
import numpy as np
import pandas as pd
import xarray as xr
from melodies_monet.util import write_util
import os
import argparse

def get_dates(start,end,freq='H'):
    return pd.date_range(start=start,end=end,freq=freq)

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
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start_date", action="store", required=True, type=str,
                        help="Start downloading data for this year")
    parser.add_argument("-e", "--end_date", action="store", required=True, type=str,
                        help="End downloading data for this year")
    parser.add_argument("-f", "--freq", action="store", required=False, type=str, default='H',
                        help="End downloading data for this year")
    parser.add_argument('-o', '--outname', action='store', required=False, default=None)
    parser.add_argument('-v', '--verbose', action='store', required=False, default=False)
    parser.add_argument('-sl','--slim', action='store', required=False, default=False)
    args = parser.parse_args()
    print(args)

    start = args.start_date
    end = args.end_date
    freq = args.freq
    outname = args.outname
    verbose=args.verbose
    slim=args.slim
    
    dates = get_dates(args.start_date,args.end_date,freq=args.freq)
    if outname == None:
        outname = 'AERONET_L15_{}_{}_{}.nc'.format(start.replace('-',''),end.replace('-',''),args.freq)
    else:
        outname = args.outname


    standard_wavelengths = np.array([0.55])* 1000.
    df = mio.aeronet.add_data(dates, interp_to_aod_values=standard_wavelengths, freq='D')
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

    # now site_variable are the single element attributes of the individual site so lets simplify this
    for index,d in enumerate(dsets):
        dsets[index] = expand_dims(d,index=index)
        
    # now combine all the datasets for each site into a single dataset
    ds = xr.concat(dsets,dim='x').set_coords(site_variable)
    # write the file
    if slim:
        ds = ds[['time','siteid','aeronet_instrument_number','latitude','longitude','x','aod_550nm']]
    t = ds.expand_dims('y').transpose('time','y','x')
    write_util.write_ncf(t,outname)

