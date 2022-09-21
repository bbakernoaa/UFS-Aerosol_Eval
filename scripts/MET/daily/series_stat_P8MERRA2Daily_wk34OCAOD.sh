#!/bin/sh -i

module use -a /contrib/anaconda/modulefiles
module load intel/18.0.5.274
module load anaconda/latest
module use -a /contrib/met/modulefiles/
module load met/9.0.2

FCSTDIR=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/20120101
OBSDIR=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2012

mkdir -p output_METseriesDaily_201201
series_analysis \
-fcst $FCSTDIR/20120115.nc4 \
$FCSTDIR/20120116.nc4 \
$FCSTDIR/20120117.nc4 \
$FCSTDIR/20120118.nc4 \
$FCSTDIR/20120119.nc4 \
$FCSTDIR/20120120.nc4 \
$FCSTDIR/20120121.nc4 \
$FCSTDIR/20120122.nc4 \
$FCSTDIR/20120123.nc4 \
$FCSTDIR/20120124.nc4 \
$FCSTDIR/20120125.nc4 \
$FCSTDIR/20120126.nc4 \
$FCSTDIR/20120127.nc4 \
$FCSTDIR/20120128.nc4 \
-obs $OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120115.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120116.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120117.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120118.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120119.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120120.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120121.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120122.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120123.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120124.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120125.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120126.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120127.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120128.nc4 \
-out output_METseriesDaily_201201/series_Dailyavg_20120101_wk34_MERRA2_P8_OCAOD.nc \
-config SeriesAnlConfig_WK34_MERRA2OCAOD_Daily \
-paired \
-v 5
