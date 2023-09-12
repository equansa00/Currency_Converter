import unittest
from app import app
from forex_python.converter import RatesNotAvailableError
from unittest.mock import patch
from flask import session
from flask import get_flashed_messages
import time
from flask import Flask, session, flash


class CurrencyConverterTestCase(unittest.TestCase):
    """Tests for the Currency Converter application."""

    def setUp(self):
        self.main_app = Flask(__name__)
        self.app = app.test_client()
        app.testing = True
        self.main_app = app
        self.client = self.main_app.test_client()
        self.client.testing = True


    @patch('app.cr.convert')
    def test_conversion(self, mock_convert):
        # Mocking the convert method for CurrencyRates
        mock_convert.return_value = 1.12
        response = self.app.post('/', data={'from_currency': 'USD', 'to_currency': 'EUR', 'amount': '1'}, follow_redirects=True)
        self.assertIn(b'1 USD is equal to \xe2\x82\xac 1.12 EUR', response.data)

    def test_convert_same_currency(self):
        response = self.app.post('/', data={'from_currency': 'USD', 'to_currency': 'USD', 'amount': 1}, follow_redirects=True)
        self.assertIn(b'1 USD is equal to $ 1.0 USD', response.data)

    def test_convert_different_currency(self):
        response = self.app.post('/', data={'from_currency': 'USD', 'to_currency': 'EUR', 'amount': '1'}, follow_redirects=True)
        self.assertIn(b'USD is equal to', response.data)

    def test_invalid_amount(self):
        # Define the POST data here
        data = {
            'from_currency': 'USD',
            'to_currency': 'EUR',
            'amount': 'INVALID'
        }

        with app.test_client() as client:
            response = client.post('/', data=data, follow_redirects=True)
            # Access flashed messages directly from the session here
            flashed_messages = [(category, message) for category, message in get_flashed_messages(with_categories=True)]

            self.assertIn(("error", "Invalid amount. Please enter a positive number."), flashed_messages)
            self.assertEqual(response.status_code, 400)

    def test_empty_input_values(self):
        """Test with empty input values."""
        with app.test_client() as client:
            response = client.post('/', data={'from_currency': '', 'to_currency': '', 'amount': ''}, follow_redirects=True)

            flashed_messages = [(category, message) for category, message in get_flashed_messages(with_categories=True)]

            # Optional print for debugging
            print("Flashed messages:", flashed_messages)

            self.assertIn(("error", "Currency fields cannot be empty."), flashed_messages)


    def test_large_amount(self):
        """Test with a large amount."""
        response = self.app.post('/', data={'from_currency': 'USD', 'to_currency': 'EUR', 'amount': '999999999999'})
        assert b'USD is equal to' in response.data

    def test_small_amount(self):
        """Test with a small amount."""
        response = self.app.post('/', data={'from_currency': 'USD', 'to_currency': 'EUR', 'amount': '0.0001'})
        assert b'USD is equal to' in response.data

    def test_get_request(self):
        """Test handling of GET requests."""
        response = self.app.get('/')
        assert response.status_code == 200
        assert b'<form action="/" method="post">' in response.data


if __name__ == '__main__':
    unittest.main()