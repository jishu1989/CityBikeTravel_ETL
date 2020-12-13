# HSL CityBike Travel  

### Description:  

City bike stations’ Origin-Destination (OD) data includes all trips made with city bikes of Helsinki and Espoo. The data includes information about trip’s origin and destination stations, start and end times, distance (in metres) as well as duration (in seconds). In this project we design a microservice to scrape data from hsl weblink, process the data, and create a snowflake pipeline to load data in the cloud database. 


### Data Source:

https://www.avoindata.fi/data/en_GB/dataset/helsingin-ja-espoon-kaupunkipyorilla-ajatut-matkat

Monthly data: "dev.hsl.fi/citybikes/od-trips-[year]/[year]-[mm].csv" 

Yearly data: "dev.hsl.fi/citybikes/od-trips-[year]/od-trips-[year].zip" 

### Scraping:  

We start by scraping the yearly data using the link to download yearly data. A zip file gets downloaded, which contains yearly data of city bike travel by month.


### Processing:  

Integrating the monthly datasets, to create a yearly dataset.


### Snowflake Load:  

Create a schema in the database, and staging table for yearly load => pushing data => to the database.




