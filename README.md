# HSL CityBike Travel  

### Description:  

City bike stations’ Origin-Destination (OD) data includes all trips made with city bikes of Helsinki and Espoo. The data includes information about trip’s origin and destination stations, start and end times, distance (in metres) as well as duration (in seconds).


### Data Source:

https://www.avoindata.fi/data/en_GB/dataset/helsingin-ja-espoon-kaupunkipyorilla-ajatut-matkat

Monthly data: "dev.hsl.fi/citybikes/od-trips-[year]/[year]-[mm].csv" 

Yearly data: "dev.hsl.fi/citybikes/od-trips-[year]/od-trips-[year].zip" 

### Scraping:  

We start by scraping the yearly data using the link to download yearly data. A zip file gets downloaded, which contains yearly data of city bike travel by month.


### Processing:  

Integrating the monthly datasets, to create a annual dataset.


### Snowflake Load:  

Create a schema in the database, and staging table for yearly load => pushing data => to the database.




