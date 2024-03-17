
for year in `seq 2014 2023`;
	do for month in `seq 1 1`;
		do 
		wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=51459&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" ;
	done;
done
