import unittest
from app import app

class CurrencyConverterTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_convert_same_currency(self):
        response = self.app.post('/', data={'from_currency': 'USD', 'to_currency': 'USD', 'amount': '1'})
        assert b'1 USD is equal to $ 1.0 USD' in response.data

    # Add more tests, for instance for invalid currency codes and amounts
    
if __name__ == '__main__':
    unittest.main()
