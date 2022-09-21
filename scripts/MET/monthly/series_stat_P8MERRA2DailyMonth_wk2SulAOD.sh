#!/bin/sh -i

module use -a /contrib/anaconda/modulefiles
module load intel/18.0.5.274
module load anaconda/latest
module use -a /contrib/met/modulefiles/
module load met/9.0.2
month=${1}
FCSTDIR=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/2012${month}01
FCSTDIR2=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/2013${month}01
FCSTDIR3=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/2014${month}01
FCSTDIR4=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/2015${month}01
FCSTDIR5=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/2016${month}01
FCSTDIR6=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/2017${month}01
FCSTDIR7=/scratch1/NCEPDEV/stmp4/Partha.Bhattacharjee/p8_dailymean/2018${month}01
OBSDIR=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2012
OBSDIR2=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2013
OBSDIR3=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2014
OBSDIR4=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2015
OBSDIR5=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2016
OBSDIR6=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2017
OBSDIR7=/scratch1/NCEPDEV/stmp2/Partha.Bhattacharjee/MERRA2/2018

mkdir -p output_METseriesDaily_2012${month}
series_analysis \
-fcst $FCSTDIR/2012${month}08.nc4 \
$FCSTDIR/2012${month}09.nc4 \
$FCSTDIR/2012${month}10.nc4 \
$FCSTDIR/2012${month}11.nc4 \
$FCSTDIR/2012${month}12.nc4 \
$FCSTDIR/2012${month}13.nc4 \
$FCSTDIR/2012${month}14.nc4 \
$FCSTDIR2/2013${month}08.nc4 \
$FCSTDIR2/2013${month}09.nc4 \
$FCSTDIR2/2013${month}10.nc4 \
$FCSTDIR2/2013${month}11.nc4 \
$FCSTDIR2/2013${month}12.nc4 \
$FCSTDIR2/2013${month}13.nc4 \
$FCSTDIR2/2013${month}14.nc4 \
$FCSTDIR3/2014${month}08.nc4 \
$FCSTDIR3/2014${month}09.nc4 \
$FCSTDIR3/2014${month}10.nc4 \
$FCSTDIR3/2014${month}11.nc4 \
$FCSTDIR3/2014${month}12.nc4 \
$FCSTDIR3/2014${month}13.nc4 \
$FCSTDIR3/2014${month}14.nc4 \
$FCSTDIR4/2015${month}08.nc4 \
$FCSTDIR4/2015${month}09.nc4 \
$FCSTDIR4/2015${month}10.nc4 \
$FCSTDIR4/2015${month}11.nc4 \
$FCSTDIR4/2015${month}12.nc4 \
$FCSTDIR4/2015${month}13.nc4 \
$FCSTDIR4/2015${month}14.nc4 \
$FCSTDIR5/2016${month}08.nc4 \
$FCSTDIR5/2016${month}09.nc4 \
$FCSTDIR5/2016${month}10.nc4 \
$FCSTDIR5/2016${month}11.nc4 \
$FCSTDIR5/2016${month}12.nc4 \
$FCSTDIR5/2016${month}13.nc4 \
$FCSTDIR5/2016${month}14.nc4 \
$FCSTDIR6/2017${month}08.nc4 \
$FCSTDIR6/2017${month}09.nc4 \
$FCSTDIR6/2017${month}10.nc4 \
$FCSTDIR6/2017${month}11.nc4 \
$FCSTDIR6/2017${month}12.nc4 \
$FCSTDIR6/2017${month}13.nc4 \
$FCSTDIR6/2017${month}14.nc4 \
$FCSTDIR7/2018${month}08.nc4 \
$FCSTDIR7/2018${month}09.nc4 \
$FCSTDIR7/2018${month}10.nc4 \
$FCSTDIR7/2018${month}11.nc4 \
$FCSTDIR7/2018${month}12.nc4 \
$FCSTDIR7/2018${month}13.nc4 \
$FCSTDIR7/2018${month}14.nc4 \
-obs $OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.2012${month}08.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.2012${month}09.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.2012${month}10.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.2012${month}11.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.2012${month}12.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.2012${month}13.nc4 \
$OBSDIR/MERRA2_400.daily.tavg1_2d_aer_Nx.2012${month}14.nc4 \
$OBSDIR2/MERRA2_400.daily.tavg1_2d_aer_Nx.2013${month}08.nc4 \
$OBSDIR2/MERRA2_400.daily.tavg1_2d_aer_Nx.2013${month}09.nc4 \
$OBSDIR2/MERRA2_400.daily.tavg1_2d_aer_Nx.2013${month}10.nc4 \
$OBSDIR2/MERRA2_400.daily.tavg1_2d_aer_Nx.2013${month}11.nc4 \
$OBSDIR2/MERRA2_400.daily.tavg1_2d_aer_Nx.2013${month}12.nc4 \
$OBSDIR2/MERRA2_400.daily.tavg1_2d_aer_Nx.2013${month}13.nc4 \
$OBSDIR2/MERRA2_400.daily.tavg1_2d_aer_Nx.2013${month}14.nc4 \
$OBSDIR3/MERRA2_400.daily.tavg1_2d_aer_Nx.2014${month}08.nc4 \
$OBSDIR3/MERRA2_400.daily.tavg1_2d_aer_Nx.2014${month}09.nc4 \
$OBSDIR3/MERRA2_400.daily.tavg1_2d_aer_Nx.2014${month}10.nc4 \
$OBSDIR3/MERRA2_400.daily.tavg1_2d_aer_Nx.2014${month}11.nc4 \
$OBSDIR3/MERRA2_400.daily.tavg1_2d_aer_Nx.2014${month}12.nc4 \
$OBSDIR3/MERRA2_400.daily.tavg1_2d_aer_Nx.2014${month}13.nc4 \
$OBSDIR3/MERRA2_400.daily.tavg1_2d_aer_Nx.2014${month}14.nc4 \
$OBSDIR4/MERRA2_400.daily.tavg1_2d_aer_Nx.2015${month}08.nc4 \
$OBSDIR4/MERRA2_400.daily.tavg1_2d_aer_Nx.2015${month}09.nc4 \
$OBSDIR4/MERRA2_400.daily.tavg1_2d_aer_Nx.2015${month}10.nc4 \
$OBSDIR4/MERRA2_400.daily.tavg1_2d_aer_Nx.2015${month}11.nc4 \
$OBSDIR4/MERRA2_400.daily.tavg1_2d_aer_Nx.2015${month}12.nc4 \
$OBSDIR4/MERRA2_400.daily.tavg1_2d_aer_Nx.2015${month}13.nc4 \
$OBSDIR4/MERRA2_400.daily.tavg1_2d_aer_Nx.2015${month}14.nc4 \
$OBSDIR5/MERRA2_400.daily.tavg1_2d_aer_Nx.2016${month}08.nc4 \
$OBSDIR5/MERRA2_400.daily.tavg1_2d_aer_Nx.2016${month}09.nc4 \
$OBSDIR5/MERRA2_400.daily.tavg1_2d_aer_Nx.2016${month}10.nc4 \
$OBSDIR5/MERRA2_400.daily.tavg1_2d_aer_Nx.2016${month}11.nc4 \
$OBSDIR5/MERRA2_400.daily.tavg1_2d_aer_Nx.2016${month}12.nc4 \
$OBSDIR5/MERRA2_400.daily.tavg1_2d_aer_Nx.2016${month}13.nc4 \
$OBSDIR5/MERRA2_400.daily.tavg1_2d_aer_Nx.2016${month}14.nc4 \
$OBSDIR6/MERRA2_400.daily.tavg1_2d_aer_Nx.2017${month}08.nc4 \
$OBSDIR6/MERRA2_400.daily.tavg1_2d_aer_Nx.2017${month}09.nc4 \
$OBSDIR6/MERRA2_400.daily.tavg1_2d_aer_Nx.2017${month}10.nc4 \
$OBSDIR6/MERRA2_400.daily.tavg1_2d_aer_Nx.2017${month}11.nc4 \
$OBSDIR6/MERRA2_400.daily.tavg1_2d_aer_Nx.2017${month}12.nc4 \
$OBSDIR6/MERRA2_400.daily.tavg1_2d_aer_Nx.2017${month}13.nc4 \
$OBSDIR6/MERRA2_400.daily.tavg1_2d_aer_Nx.2017${month}14.nc4 \
$OBSDIR7/MERRA2_400.daily.tavg1_2d_aer_Nx.2018${month}08.nc4 \
$OBSDIR7/MERRA2_400.daily.tavg1_2d_aer_Nx.2018${month}09.nc4 \
$OBSDIR7/MERRA2_400.daily.tavg1_2d_aer_Nx.2018${month}10.nc4 \
$OBSDIR7/MERRA2_400.daily.tavg1_2d_aer_Nx.2018${month}11.nc4 \
$OBSDIR7/MERRA2_400.daily.tavg1_2d_aer_Nx.2018${month}12.nc4 \
$OBSDIR7/MERRA2_400.daily.tavg1_2d_aer_Nx.2018${month}13.nc4 \
$OBSDIR7/MERRA2_400.daily.tavg1_2d_aer_Nx.2018${month}14.nc4 \
-out output_METseriesDaily_2012${month}/series_Dailyavg_March_wk2_MERRA2_P8_SulAOD.nc \
-config SeriesAnlConfig_WK1_MERRA2SulAOD_DailyMonth \
-paired \
-v 5
