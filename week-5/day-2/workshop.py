#Where is this weather station
select country_code from weather_station where id = '724940:23234';

#Show the temperature for June 1st, 2008.
select temperature from raw_weather_data where wsid = '724940:23234' and month = 6 and day = 1 and year = 2008;

# Show the temperatures for June 1st, 2008 from 9AM to 3PM.
 select temperature, hour from raw_weather_data where wsid = '724940:23234' and month = 6 and day = 1 and year = 2008 and hour in (9,10,11,12,13,14,15);
# What is the average elevation of the weather stations in Indiana?
select sum(elevation) from weather_station where state_code = 'IA' allow filtering;
   ## 18761.8
select count(elevation) from weather_station where state_code = 'IA' allow filtering;
  ##62   average is 18761.8 / 62 = 302.6

# What is the latitude of the northest weather station in Texas?
select max(lat) as max_lat from weather_station where state_code = 'TX' allow filtering;
# Insert the current temperature for today.

# Fill the daily_aggregate_temperature table.

