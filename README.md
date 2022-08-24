# UFS-Aerosol_Eval

A smattering of utilities for evaluating NOAA's UFS-Aerosol model 

## UFS p8 Location 
```
COMROT: /scratch1/NCEPDEV/climate/role.ufscpara/Prototype8/work-P8/COMROOT
HPSS: /NCEPDEV/emc-climate/5year/role.ufscpara/HERA/prototype8
```



### AERONET

In the AERONET/ folder data from AERONET for each of the simulations are stored in netcdf format ready for melodies-monet.

There is also a download script that will prepare the AERONET data using monetio as a preprocessing step.

### utils

Here are various scripts used to download, process or retrieve other evalations

Currently there is only one script which was used to download the MERRA2 DIURNAL data for AOD over the p8 time period.

All MERRA2 data has been averaged to daily data for comparisons to P8 and have been stored on HPSS.  To retrieve them

```bash
htar -xvf /NCEPDEV/emc-naqfc/5year/Barry.Baker/MERRA2/MERRA2_DAILY_2019.tar
```

This will download all MERRA2 data for the year 2019.  Each day is approximately 29 mb and is at the 0.5x0.625 resolution.

