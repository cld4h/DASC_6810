import pandas as pd

FILE_PREFIX = "data_src/stations.csv"

STATIONS = pd.read_csv(FILE_PREFIX)

STATIONS.columns

selected = STATIONS[(STATIONS['Latitude (Decimal Degrees)'] >= 43) & (STATIONS['Latitude (Decimal Degrees)'] <= 44) & (STATIONS['Longitude (Decimal Degrees)'] >= -80) & (STATIONS['Longitude (Decimal Degrees)'] <= -79) & (STATIONS['DLY Last Year'] >= 2023) & (STATIONS['DLY First Year'] <= 2016)]

selected.to_csv("output/selectedstations.csv")
