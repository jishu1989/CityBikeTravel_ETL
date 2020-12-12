use warehouse COMPUTE_WH;
use database CITYBIKES;
use schema PUBLIC;

create or replace table staging
(
Departure_time string,
Return_time string,
Departure_station_id string,
Departure_station_name string,
Return_station_id string,
Return_station_name string,
Covered_distance string,
Duration string,
Year_Month string,
Year_value string
);

put file:///home/soumya/Documents/citybike/landing/2017.csv  @%staging;

list @%staging;

copy into staging
   from @%staging
   file_format = (type = csv FIELD_DELIMITER = ',')
   on_error = 'skip_file';