# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from forex_python.converter import CurrencyRates, RatesNotAvailableError, CurrencyCodes
from utils import is_valid_amount, get_symbol, is_valid_currency

app = Flask(__name__)
app.secret_key = 'supersecretkey'

cr = CurrencyRates()
cc = CurrencyCodes()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        amount = request.form.get('amount')

        # Validation
        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            flash("Invalid currency code. Please check and try again.")
            return redirect(url_for('index'))

        if not is_valid_amount(amount):
            flash("Invalid amount. Please enter a valid number.")
            return redirect(url_for('index'))

        try:
            converted = cr.convert(from_currency, to_currency, float(amount))
            symbol = get_symbol(to_currency)
            flash(f"{amount} {from_currency} is equal to {symbol} {round(converted, 2)} {to_currency}")

        except RatesNotAvailableError:
            error = "Sorry, we couldn't fetch the conversion rates at the moment. Please try again later."
            flash(error)

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    if 'TESTING' not in app.config or not app.config['TESTING']:
        app.run(debug=True)
