from forex_python.converter import CurrencyRates

def test_live_rates():
    cr = CurrencyRates()
    rates = cr.get_rates('USD')
    print(rates)  # Get the conversion rates for USD to other currencies.
    assert isinstance(rates, dict)
    assert 'EUR' in rates

if __name__ == '__main__':
    test_live_rates()
