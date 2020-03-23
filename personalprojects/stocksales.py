import yfinance as yf
from pprint import pprint

pfg = yf.Ticker("PFG")
pprint(pfg.info)
pprint(pfg.sustainability)
pprint(pfg.recommendations)
