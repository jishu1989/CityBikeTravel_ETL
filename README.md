# MicroService: HSL CityBike Travel  

### Description:  

City bike stations’ Origin-Destination (OD) data includes all trips made with city bikes of Helsinki and Espoo. The data includes information about trip’s origin and destination stations, start and end times, distance (in metres) as well as duration (in seconds). In this project we design a microservice to scrape data from hsl weblink, a python data pipeline to move the data into landing space, process and archive the data, creating a snowflake pipeline to stage and bulk load the data in the cloud database, thereby automating the incremental load of data. 


### Data Source:

https://www.avoindata.fi/data/en_GB/dataset/helsingin-ja-espoon-kaupunkipyorilla-ajatut-matkat

Monthly data: "dev.hsl.fi/citybikes/od-trips-[year]/[year]-[mm].csv" 

Yearly data: "dev.hsl.fi/citybikes/od-trips-[year]/od-trips-[year].zip" 

### Scraping:  

We start by scraping the yearly data using the link to download yearly data. A zip file gets downloaded, which contains yearly data of city bike travel by month.
Before running the scrapper ```scrapper.py```, we need to run ```yearvalue_download.sql``` script to download the value of latest year present in the database-table: TRIP. ```scrapper.py``` uses this information to scrape data of the following year.

### Processing:  

After the zip file gets downloaded, the zip file is moved to a landing directory(on running the script : ```file_transfer.py```) where we unzip the file. The unzipped folder has monthly csv files which are integrated into => one yearly csv file on running ```file_integration.py```.

### Snowflake Load:  

We create sql script ```biketrip_ddl.sql``` to define table in the database(schema creation).We use the SnowSQL CLI service to bulk load the data in the staging table(```staging.sql```).Once the the data is loaded in the staging table it is pushed to the main table <= from the staging table on running the ```data_integration.sql```. 





