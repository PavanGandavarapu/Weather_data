from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import sqlite3

app = Flask(__name__)
api = Api(app, version='1.0', title='Weather Data API',
          description='A simple Weather Data API',
          )

ns = api.namespace('weather', description='Weather operations')

# Define the model for the weather data
weather_model = api.model('WeatherData', {
    'date': fields.String(required=True, description='The date of the weather data'),
    'max_temperature': fields.Float(required=True, description='The maximum temperature'),
    'min_temperature': fields.Float(required=True, description='The minimum temperature'),
    'precipitation': fields.Float(required=True, description='The precipitation'),
    'station_name': fields.String(required=True, description='The name of the station')
})

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('weatherdb.db')
    conn.row_factory = sqlite3.Row
    return conn

@ns.route('/yearly-stats')
class YearlyStats(Resource):
    @api.doc(params={'year': 'The year to filter by', 'station_name': 'The station name to filter by'})
    def get(self):
        """Fetch yearly statistics"""
        conn = get_db_connection()
        year = request.args.get('year')
        station_name = request.args.get('station_name')

        query = """
            SELECT * FROM yearly_weather_data_stats
            WHERE 1=1
        """
        params = []

        if year:
            query += " AND year = ?"
            params.append(year)

        if station_name:
            query += " AND station_name = ?"
            params.append(station_name)

        stats = conn.execute(query, params).fetchall()
        conn.close()

        result = [dict(row) for row in stats]
        return jsonify(result)

@ns.route('/weather-data')
class WeatherData(Resource):
    @api.doc(params={'date': 'The date to filter by', 'station_name': 'The station name to filter by'})
    def get(self):
        """Fetch weather data"""
        conn = get_db_connection()
        date = request.args.get('date')
        station_name = request.args.get('station_name')

        query = """
            SELECT * FROM weather_data
            WHERE 1=1
        """
        params = []

        if date:
            query += " AND date = ?"
            params.append(date)

        if station_name:
            query += " AND station_name = ?"
            params.append(station_name)

        data = conn.execute(query, params).fetchall()
        conn.close()

        result = [dict(row) for row in data]
        return jsonify(result)

# Add the namespace to the API
api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True)
