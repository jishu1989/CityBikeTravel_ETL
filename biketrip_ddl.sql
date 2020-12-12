use warehouse COMPUTE_WH;
use database CITYBIKES;
use schema PUBLIC;

create or replace table trips
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

