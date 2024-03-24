import pandas as pd
import os

folder_path = "output"

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

dfs = {}

# Loop through each station
for station in station_lists:
    sid = station["sid"]
    file_name = f"{sid}-data.csv"
    file_path = os.path.join(folder_path, file_name)
    
    # Read CSV file into DataFrame
    df = pd.read_csv(file_path)
    # Check for null values
    null_values = df.isnull().sum()
    print(f"Null values for station {sid}:\n{null_values}")
    dfs[sid] = df
    
# Update NULL value:
dfs_nona = {}
for station in station_lists:
    sid = station["sid"]
    file_name = f"{sid}-data.csv"
    file_path = os.path.join(folder_path, file_name)
    # Read CSV file into DataFrame
    df = pd.read_csv(file_path)
    colnames = df.columns
    for i in range(3,10):
        # Traverse ever column from 'Mean Temp (°C)' to 'Spd of Max Gust (km/h)'
        null_indices = df[colnames[i]][df[colnames[i]].isnull()].index
        print("Null indices in station "+sid+" column "+colnames[i])
        print(null_indices)
        for j in null_indices:
            # Calculate the mean using all the valid data in other stations
            print("On indice "+str(j))
            other_stations_data = pd.Series([dfs[key][colnames[i]][j] for key in dfs.keys() if key != sid])
            print(other_stations_data)
            mean_value = other_stations_data.mean()
            print("Mean value is: "+str(mean_value))
            # update the missing value
            df.loc[j,colnames[i]] = mean_value
    # update dfs
    dfs_nona[sid] = df

for station in station_lists:
    sid = station["sid"]
    csv_file_name = f"{sid}-data-nona.csv"
    csv_file_path = os.path.join(folder_path, csv_file_name)
    dfs_nona[sid].to_csv(csv_file_path)
