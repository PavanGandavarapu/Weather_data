Weather Data Ingestion and API Project

Overview

This project involves ingesting weather data from raw text files into a SQLite database, processing the data, and providing an API for accessing the processed weather data. The project includes automatic Swagger/OpenAPI documentation for the API.

Requirements
Python 3.x
Flask
Flask-RESTX
Flask-Swagger-UI
Pandas
SQLite

Installation

1. Clone the Repository:

git clone https://github.com/your-username/your-repository.git
cd your-repository

2. Set Up a Virtual Environment:

python -m venv myenv
source myenv\bin\activate

3. Install the Required Packages:

pip install -r requirements.txt

Data Ingestion

The data_ingestion.py script ingests weather data from raw text files into a SQLite database. It handles duplicate entries and logs the ingestion process.

Steps to Run the Data Ingestion Script

1. Prepare the Data Files:

Ensure the raw text files are located in the wx_data folder.

2. Run the Data Ingestion Script:

python data_ingestion.py

3. Check the Logs:

The script logs the start and end times, as well as the number of records ingested, in the data_ingestion.log file.

Data Analysis

The data_analysis.py script processes the ingested weather data to calculate yearly statistics for each weather station.

Steps to Run the Data Analysis Script

1. Run the Data Analysis Script:

python data_analysis.py

2. Output:

The processed statistics are stored in the yearly_weather_data_stats table in the SQLite database.

API

The project includes a Flask-based API with Swagger/OpenAPI documentation. The API provides endpoints to access the ingested weather data and the calculated yearly statistics.

API Endpoints

GET /weather/yearly-stats
Parameters:
year: The year to filter by.
station_name: The station name to filter by.

GET /weather/weather-data
Parameters:
date: The date to filter by.
station_name: The station name to filter by.

Running the API

1. Start the Flask Application:

python app.py

2. Access the API Documentation:

Open your browser and navigate to http://127.0.0.1:5000/ to access the Swagger UI.

Unit Tests

Unit tests for the API are included in the test_app.py file.

Running the Unit Tests

1. Run the Tests:

python test_app.py

Files in the Project
app.py: Flask application with API endpoints.
data_ingestion.py: Script to ingest raw text data into the SQLite database.
data_analysis.py: Script to process ingested data and calculate yearly statistics.
data_downlaod.py: Script to download data files from GitHub.
test_app.py: Unit tests for the API.
requirements.txt: List of required Python packages.
data_ingestion.log: Log file for the data ingestion process.
weatherdb.db: SQLite database containing the ingested and processed weather data.
