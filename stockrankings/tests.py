from django.test import TestCase

# Create your tests here.
import FinanceDatabase as fd
from yfinance.utils import get_json
from yfinance import download

stocks = fd.select_equities(country='United States', industry='Advertising Agencies')

fundamentals = {}
for symbol in stocks :
    fundamentals[symbol] = get_json( "https://finance.yahoo.com/quote/" + symbol)

print(fundamentals)