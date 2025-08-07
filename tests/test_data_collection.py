import unittest
from src.data_collection import collect_health_data

class TestDataCollection(unittest.TestCase):

    def test_collect_health_data(self):
        # Test the data collection function
        data = collect_health_data()
        self.assertIsInstance(data, dict)
        self.assertIn('heart_rate', data)
        self.assertIn('blood_oxygen', data)
        self.assertIn('activity_level', data)

    def test_collect_health_data_values(self):
        # Test the values returned by the data collection function
        data = collect_health_data()
        self.assertGreaterEqual(data['heart_rate'], 60)
        self.assertLessEqual(data['heart_rate'], 100)
        self.assertGreaterEqual(data['blood_oxygen'], 90)
        self.assertLessEqual(data['blood_oxygen'], 100)
        self.assertIn(data['activity_level'], ['low', 'moderate', 'high'])

if __name__ == '__main__':
    unittest.main()