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
-fcst $FCSTDIR/20120101.nc4 \
$FCSTDIR/20120102.nc4 \
$FCSTDIR/20120103.nc4 \
$FCSTDIR/20120104.nc4 \
$FCSTDIR/20120105.nc4 \
$FCSTDIR/20120106.nc4 \
$FCSTDIR/20120107.nc4 \
-obs $OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120101.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120102.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120103.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120104.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120105.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120106.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.20120107.nc4 \
-out output_METseriesDaily_201201/series_Dailyavg_20120101_wk1_MERRA2_P8_BCAOD.nc \
-config SeriesAnlConfig_WK1_MERRA2BCAOD_Daily \
-paired \
-v 5
