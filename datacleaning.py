# pandas library is required
# To prepare the environment
# python3 -m venv 6810_temp_venv
# source 6810_temp_venv/bin/activate
# pip install pandas
import pandas as pd

FOLDER = "data_src/"
FILE_PREFIX = "en_climate_daily_ON_"
NCEP_PREFIX = "data_src/NCEP_temp.csv"
NCEP_df = pd.read_csv(NCEP_PREFIX)
NCEP_df = NCEP_df[["Date","Temperature"]]
final_df = pd.DataFrame()

station_lists=[
{"station": "GRIMSBY MOUNTAIN", "cid": "6133055", "sid": "44123"},
{"station": "PORT WELLER (AUT)", "cid": "6136699", "sid": "7790"},
{"station": "VINELAND STATION RCS", "cid": "6139148", "sid": "31367"},
{"station": "BURLINGTON PIERS (AUT)", "cid": "6151061", "sid": "7868"},
{"station": "GEORGETOWN WWTP", "cid": "6152695", "sid": "4923"},
{"station": "HAMILTON A", "cid": "6153193", "sid": "49908"},
{"station": "HAMILTON RBG CS", "cid": "6153301", "sid": "27529"},
{"station": "OAKVILLE TWN", "cid": "6155750", "sid": "45667"},
{"station": "TORONTO CITY", "cid": "6158355", "sid": "31688"},
{"station": "TORONTO CITY CENTRE", "cid": "6158359", "sid": "48549"},
{"station": "TORONTO INTL A", "cid": "6158731", "sid": "51459"}]


for station in station_lists:
    final_df = None
    for year in range(2016, 2024):
        filename = FOLDER+station["sid"]+"/"+FILE_PREFIX+station["cid"]+"_"+str(year)+"_P1D.csv"
        df = pd.read_csv(filename)
        df = df[['Date/Time', 'Mean Temp (°C)', 'Max Temp (°C)', 'Min Temp (°C)', "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)"]]
        # df = df[['Date/Time', 'Mean Temp (°C)', 'Max Temp (°C)', 'Min Temp (°C)', "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)", "Spd of Max Gust (km/h)"]]
        result_df = pd.merge(NCEP_df, df, left_on="Date", right_on="Date/Time", suffixes=(None,"_ws") )
        result_df = result_df[['Date', 'Temperature', 'Mean Temp (°C)', 'Max Temp (°C)', 'Min Temp (°C)', "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)"]]
        # result_df = result_df[['Date', 'Temperature', 'Mean Temp (°C)', 'Max Temp (°C)', 'Min Temp (°C)', "Total Rain (mm)", "Total Snow (cm)", "Total Precip (mm)", "Snow on Grnd (cm)", "Spd of Max Gust (km/h)"]]
        final_df = pd.concat([final_df, result_df], ignore_index=True)

    final_df.to_csv("output/"+station["sid"]+"-"+"data.csv")

