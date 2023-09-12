from flask import Flask, render_template, request, redirect, url_for, flash
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from utils import is_valid_amount, get_symbol, is_valid_currency
import logging

app = Flask(__name__)
app.secret_key = '87E3B4188F358A55983A311BF765D'

# Define the string variable
string = "This is a string."

# Get supported currencies
def get_supported_currencies():
    supported_currencies = sorted(CurrencyRates().get_rates('USD').keys())
    print(f"Supported currencies: {supported_currencies}")
    return supported_currencies

# Import the CurrencyRates class

cr = CurrencyRates()

# Setup logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    category = "success"
    result = None
    status_code = 200  # Initialize with default status code

    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        print(f"From Currency: {from_currency}, To Currency: {to_currency}")
        print("Form data received:", request.form)
        amount = request.form.get('amount')

        try:
            amount_float = float(amount)
        except ValueError:
            amount_float = None

        # Immediately check for a negative amount and handle the error
        if amount_float and amount_float < 0:
            flash("Invalid amount. Please enter a positive number.", "error")
            return render_template('index.html', result=result, currencies=get_supported_currencies()), 400

        # Validate the input from the user
        if from_currency is None or from_currency == '' or to_currency is None or to_currency == '':
            message = "Currency fields cannot be empty."
            category = "error"
            status_code = 400  # Update the status code to 400 for bad request

        elif not amount_float:
            message = "Invalid amount. Please enter a positive number."
            category = "error"
            status_code = 400  # Update the status code to 400 for bad request

        # Convert the currency
        if not message:
            try:
                converted = cr.convert(from_currency, to_currency, amount_float)
                symbol = get_symbol(to_currency)
                result = f"{amount} {from_currency} is equal to {symbol} {round(converted, 2)} {to_currency}"
            except RatesNotAvailableError:
                message = "Invalid currency code. Please check and try again."
                category = "error"
                status_code = 500  # This might be a server error (you can decide the right status code)
            except Exception as e:
                message = f"Unexpected error occurred."
                category = "error"
                logger.error(f"Error while converting currency: {e}")
                status_code = 500  # This might be a server error

        # Redirect to the index page with the error message
        if message:
            flash(message, category)
            print("Returning with message:", message)
            return render_template('index.html', result=result, currencies=get_supported_currencies()), status_code

    print("Rendering template")
    return render_template('index.html', result=result, currencies=get_supported_currencies())


if __name__ == '__main__':
    if 'TESTING' not in app.config or not app.config['TESTING']:
        app.run()