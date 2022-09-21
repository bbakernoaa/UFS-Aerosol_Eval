# Daily

This is used for individual runs. For example, a sanity check on an individual run.  Can be used later for cycled experiments etc.

# Monthly

This is for more aggregate runs.  In the case of P8 this looks at each month (week1

## Requirements  
- NOAA MACHINE HERA
- METv10.0.0

## MODULES
```bash 
module use -a /contrib/anaconda/modulefiles
module load intel/18.0.5.274
module load anaconda/latest
module use -a /contrib/met/modulefiles/
module load met/10.0.0
```

## METplus-4.0.0
METplus-4.0.0 Installation: `/contrib/METplus/METplus-4.0.0`
METplus-4.0.0 Sample Data: `/scratch1/BMC/dtc/METplus/METplus-4.0_sample_data`

## To use METplus run:
module use /contrib/METplus/modulefiles
module load metplus/4.0.0


