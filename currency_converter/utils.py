# utils.py
from forex_python.converter import CurrencyCodes, CurrencyRates

cr = CurrencyRates()
cc = CurrencyCodes()

def is_valid_currency(currency):
    try:
        cc.get_symbol(currency)
        return True
    except:
        return False

def is_valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False

def get_symbol(currency):
    return cc.get_symbol(currency)
