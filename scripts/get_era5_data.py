# coding: utf-8
import cdsapi

c = cdsapi.Client()

for year in range(2011, 2019):
    for month in range(1, 13):
        c.retrieve(
            "reanalysis-era5-single-levels",
            {
                "product_type": "reanalysis",
                "variable": [
                    "10m_u_component_of_wind",
                    "10m_v_component_of_wind",
                    "friction_velocity",
                    "volumetric_soil_water_layer_1",
                ],
                "year": "{}".format(year),
                "month": ["{}".format(str(month).zfill(2))],
                "day": [
                    "01",
                    "02",
                    "03",
                    "04",
                    "05",
                    "06",
                    "07",
                    "08",
                    "09",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                    "15",
                    "16",
                    "17",
                    "18",
                    "19",
                    "20",
                    "21",
                    "22",
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29",
                    "30",
                    "31",
                ],
                "time": [
                    "00:00",
                    "06:00",
                    "12:00",
                    "18:00",
                ],
                "format": "netcdf",
            },
            "ERA5_ustar_soilmoist_{}{}.nc".format(year, str(month).zfill(2)),
        )
