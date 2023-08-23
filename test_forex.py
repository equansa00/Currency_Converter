from forex_python.converter import CurrencyRates

cr = CurrencyRates()
print(cr.get_rates('USD'))  # Get the conversion rates for USD to other currencies.
