# Instruction
 
##  Deadline

Project 1: Due March 25, 2024 (The team will select the topic that should differ from last semester.
Project 2: Due April 15, 2024 ( the topic will be one of the talks in data science seminar)

##  Format specification

I need a report consisting of the following.

* Abstract
* Section 1. The introduction will review the existing literature related to the topic.
* Section 2. Review the approaches that you used to deal with the topic (e.g. finance)
* Section 3. You need to select one approach from Section 2 and describe the approach in detail. Write the code in Python with several datasets.
* Section 4. Write your results of the approach of section 3, e.g., tables, graphs, and explanation of the results. Describe the datasets if possible.
* Section 5. Conclusion
* References

Note: try to be generous in writing. Collect related papers from Google Scholar, especially reviews or surveys for your topic. Consider the academic integrity in your writing (do not copy and paste) and write the references especially if you get the code(s) from online.

General Presentation:

* Body text in a minimum 12 pt Times New Roman font
* Single-spaced, with no more than 6 lines of type per inch
* All margins set at a minimum of 3/4" (1.87 cm)
* Min pages 15-20, be generous in writing and explanations whatever it takes
* Share the code when you submit the project to check it.

## Data retrieve

Weather station selecting: 
https://climate-change.canada.ca/climate-data/#/daily-climate-data

Station inventory list:
https://collaboration.cmc.ec.gc.ca/cmc/climate/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv

Historic data downloading:
https://collaboration.cmc.ec.gc.ca/cmc/climate/Get_More_Data_Plus_de_donnees/

`stationselect.py` read the Station inventory list and filtered out ALL operating stations within one grid in GFS model.

| Name                   | Climate ID | Station ID | Latitude | Longitude |
| ---------------------- | ---------- | ---------- | -------- | --------- |
| GRIMSBY MOUNTAIN       | 6133055    | 44123      | 43.18    | -79.56    |
| PORT WELLER (AUT)      | 6136699    | 7790       | 43.25    | -79.22    |
| VINELAND STATION RCS   | 6139148    | 31367      | 43.18    | -79.40    |
| BURLINGTON PIERS (AUT) | 6151061    | 7868       | 43.30    | -79.80    |
| GEORGETOWN WWTP        | 6152695    | 4923       | 43.64    | -79.88    |
| HAMILTON A             | 6153193    | 49908      | 43.17    | -79.94    |
| HAMILTON RBG CS        | 6153301    | 27529      | 43.29    | -79.91    |
| OAKVILLE TWN           | 6155750    | 45667      | 43.51    | -79.69    |
| TORONTO CITY           | 6158355    | 31688      | 43.67    | -79.40    |
| TORONTO CITY CENTRE    | 6158359    | 48549      | 43.63    | -79.40    |
| TORONTO INTL A         | 6158731    | 51459      | 43.68    | -79.63    |

Data format reference: https://climate.weather.gc.ca/doc/Technical_Documentation.pdf


GFS model forcast:
https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast

https://docs.unidata.ucar.edu/ldm/current/basics/source-install-steps.html
