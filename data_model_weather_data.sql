CREATE TABLE IF NOT EXISTS weather_data (
    date TEXT NOT NULL,
    max_temperature INTEGER,
    min_temperature INTEGER,
    precipitation INTEGER,
    station_name TEXT NOT NULL,
    PRIMARY KEY (date, station_name)
)