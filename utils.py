from forex_python.converter import CurrencyRates, CurrencyCodes

cr = CurrencyRates()
cc = CurrencyCodes()

def is_valid_currency(currency):
    try:
        symbol = cc.get_symbol(currency)
        return bool(symbol)
    except ValueError:  # Adjust to the specific exception thrown by get_symbol for invalid currency.
        return False

def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False

def get_symbol(currency):
    try:
        return cc.get_symbol(currency)
    except ValueError:
        return None
