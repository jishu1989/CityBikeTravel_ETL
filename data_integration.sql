use warehouse COMPUTE_WH;
use database CITYBIKES;
use schema PUBLIC;

insert into "CITYBIKES"."PUBLIC"."TRIPS" select * from "CITYBIKES"."PUBLIC"."STAGING";