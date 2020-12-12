use warehouse COMPUTE_WH;
use database CITYBIKES;
use schema PUBLIC;

copy into '@%staging/result/'
from
(select MAX(YEAR_VALUE) as LAST_YEAR from "CITYBIKES"."PUBLIC"."TRIPS");

GET @%staging/result/ file:///home/soumya/Documents/citybike/