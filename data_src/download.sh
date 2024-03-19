set -- $@ 44123 7790  31367 7868  4923  49908 27529 45667 31688 48549 51459 
# GRIMSBY MOUNTAIN        | 44123 
# PORT WELLER (AUT)       | 7790  
# VINELAND STATION RCS    | 31367 
# BURLINGTON PIERS (AUT)  | 7868  
# GEORGETOWN WWTP         | 4923  
# HAMILTON A              | 49908 
# HAMILTON RBG CS         | 27529 
# OAKVILLE TWN            | 45667 
# TORONTO CITY            | 31688 
# TORONTO CITY CENTRE     | 48549 
# TORONTO INTL A          | 51459 

for station in $@;
do 
	if [ ! -d $station ]; then
	  mkdir -p $station
	  cd $station
	  for year in `seq 2014 2023`;
	  	do for month in `seq 1 1`;
	  		do
	  	  wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=${station}&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" ;
	  	done;
	  done
	  cd ..
	fi
done;

#		wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=51459&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" ; # TORONTO INTL A
#		wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=31688&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" ; # TORONTO CITY
#		wget --content-disposition "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=26953&Year=${year}&Month=${month}&Day=14&timeframe=2&submit= Download+Data" ; # TORONTO NORTH YORK
