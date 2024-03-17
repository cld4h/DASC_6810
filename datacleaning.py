# pandas library is required
# To prepare the environment
# python3 -m venv 6810_temp_venv
# source 6810_temp_venv/bin/activate
# pip install pandas
import pandas as pd

FILE_PREFIX = "data_src/en_climate_daily_ON_6158731_"
NCEP_PREFIX = "data_src/NCEP_temp.csv"
NCEP_df = pd.read_csv(NCEP_PREFIX)
NCEP_df = NCEP_df[["Date","Temperature"]]
final_df = pd.DataFrame()


for year in range(2016, 2024):
    df = pd.read_csv(FILE_PREFIX+str(year)+"_P1D.csv")
    df = df[['Date/Time', 'Mean Temp (°C)', 'Max Temp (°C)', 'Min Temp (°C)', "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)", "Spd of Max Gust (km/h)"]]
    result_df = pd.merge(NCEP_df, df, left_on="Date", right_on="Date/Time", suffixes=(None,"_ws") )
    result_df = result_df[['Date', 'Temperature', 'Mean Temp (°C)', 'Max Temp (°C)', 'Min Temp (°C)', "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)", "Spd of Max Gust (km/h)"]]
    final_df = pd.concat([final_df, result_df], ignore_index=True)

final_df.to_csv("output/data.csv")

