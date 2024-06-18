CREATE TABLE IF NOT EXISTS yearly_weather_data_stats (
    year TEXT NOT NULL,
    station_name TEXT NOT NULL,
    avg_max_temp REAL,
    avg_min_temp REAL,
    total_precipitation REAL,
    PRIMARY KEY (year, station_name)
)