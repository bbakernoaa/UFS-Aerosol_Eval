#!/bin/sh
#SBATCH --account=naqfc
#SBATCH --qos=batch
#SBATCH --partition=hera
#SBATCH --nodes=1
#SBATCH --tasks-per-node=12
#SBATCH -t 00:30:00
#SBATCH -o log
#SBATCH -e err


# Embedded bash script:
binary=nexus

module purge

month=${1}

srun series_stat_P8MERRA2DailyMonth_wk1BCAOD.sh ${month} &
srun series_stat_P8MERRA2DailyMonth_wk1DAOD.sh ${month} &  
srun series_stat_P8MERRA2DailyMonth_wk1OCAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk1SsltAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk1SulAOD.sh ${month} &  
srun series_stat_P8MERRA2DailyMonth_wk1TAOD.sh ${month} & 

srun series_stat_P8MERRA2DailyMonth_wk2BCAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk2DAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk2OCAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk2SsltAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk2SulAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk2TAOD.sh ${month} & 

srun series_stat_P8MERRA2DailyMonth_wk34BCAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk34DAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk34OCAOD.sh ${month} &
srun series_stat_P8MERRA2DailyMonth_wk34SsltAOD.sh ${month} &
srun series_stat_P8MERRA2DailyMonth_wk34SulAOD.sh ${month} & 
srun series_stat_P8MERRA2DailyMonth_wk34TAOD.sh ${month} &
wait 


