#!/bin/sh

start=${1}

end=$(date -d "${start} +35 days" '+%Y-%m-%d')

./get_aeronet_L15_aod.py -s ${start} -e ${end} -f 'D' -sl True
