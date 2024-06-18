import unittest
from app import app

class WeatherDataAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_yearly_stats(self):
        response = self.app.get('/weather/yearly-stats?year=2022')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)

    def test_weather_data(self):
        response = self.app.get('/weather/weather-data?date=2022-01-01')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)

if __name__ == '__main__':
    unittest.main()
