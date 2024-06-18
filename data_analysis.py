import sqlite3

# Connect to the database
conn = sqlite3.connect('weatherdb.db')
cursor = conn.cursor()


# Calculate the average maximum temperature, average minimum temperature, and total precipitation for each year and station
cursor.execute('''
INSERT OR REPLACE INTO yearly_weather_data_stats (year, station_name, avg_max_temp, avg_min_temp, total_precipitation)
SELECT 
    SUBSTR(date, 1, 4) AS year,
    station_name,
    AVG(max_temperature / 10.0) AS avg_max_temp,
    AVG(min_temperature / 10.0) AS avg_min_temp,
    SUM(precipitation / 100.0) AS total_precipitation
FROM weather_data
GROUP BY year, station_name
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Weather data stats loaded into the 'yearly_weather_data_stats' table.")
