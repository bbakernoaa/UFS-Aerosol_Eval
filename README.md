# UFS-Aerosol_Eval

A smattering of utilities for evaluating NOAA's UFS-Aerosol model 

## UFS p8 Location 
```
COMROT: /scratch1/NCEPDEV/climate/role.ufscpara/Prototype8/work-P8/COMROOT
HPSS: /NCEPDEV/emc-climate/5year/role.ufscpara/HERA/prototype8
```

## p8 progress document and how to run 

https://docs.google.com/document/d/1io4L9XDk4Iavfca2GM8fduARfkkYW-NJDZpf_V8Ysl0/edit

## Observvations on HERA and HPSS

### MERRA2 Daily Data

Currently there is only one script which was used to download the MERRA2 DIURNAL data for AOD over the p8 time period.

All MERRA2 data has been averaged to daily data for comparisons to P8 and have been stored on HPSS.  To retrieve them

```bash
htar -xvf /NCEPDEV/emc-naqfc/5year/Barry.Baker/MERRA2/MERRA2_DAILY_2019.tar
```

This will download all MERRA2 data for the year 2019.  Each day is approximately 29 mb and is at the 0.5x0.625 resolution.

### MODIS Daily AOD Data

/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/MODIS


### AERONET

In the AERONET/ folder data from AERONET for each of the simulations are stored in netcdf format ready for melodies-monet.

There is also a download script that will prepare the AERONET data using monetio as a preprocessing step.

## utils

### get_merra2_inst2daod.sh

the `utils/get_merra2_inst2daod.sh` will download MERRA2 data with wget

to use: `./get_merra2_inst2daod.sh YYYYMMDD`

This will download all MERRA2 data for the year 2019.  Each day is approximately 29 mb and is at the 0.5x0.625 resolution.


### previous analysis

https://docs.google.com/presentation/d/1YJ6OCCsD-tt6mtZW_TcHV5Jk83drJlK_jSHmIcfAAN4/edit?usp=sharing
