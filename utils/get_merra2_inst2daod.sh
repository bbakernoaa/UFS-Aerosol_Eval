#!/bin/bash


d=${1}

yyyy=$(date -d ${d} +'%Y')
mm=$(date -d ${d} +'%m')
yyyymmdd=$(date -d ${d} +'%Y%m%d')

wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies -r -c -nH -nd -np -A nc4 --content-disposition "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXAER.5.12.4/${yyyy}/${mm}/MERRA2_400.tavg1_2d_aer_Nx.${yyyymmdd}.nc4"
                                                                                                                                       
#                                                                                                                                         https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NXGAS.5.12.4/2011/01/MERRA2_400.inst3_2d_gas_Nx.20110101.nc4
#wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --keep-session-cookies -r -c -nH -nd -np -A nc4 --content-disposition "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVAER.5.12.4/${yyyy}/${mm}/MERRA2_400.inst3_3d_aer_Nv.${yyyymmdd}.nc4"
