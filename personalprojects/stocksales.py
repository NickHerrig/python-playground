from collections import namedtuple
import time
from pprint import pprint

import yfinance as yf

Stock = namedtuple('Stock', 'name sector high low price book_value pb eps pe discount')

def parse_tickers(ticker_file):

    with open(ticker_file) as f:
        tickers = f.read().splitlines()
    return tickers

def get_stock_data(ticker):
    stock_data = yf.Ticker(ticker).info
    return Stock(
    stock_data['longName'],
    stock_data['sector'],
    stock_data['fiftyTwoWeekHigh'],
    stock_data['fiftyTwoWeekLow'],
    stock_data['regularMarketPrice'],
    stock_data['bookValue'],
    stock_data['priceToBook'],
    stock_data['trailingEps'],
    stock_data['trailingPE'],
    None,
    )

def calculate_discount(stock):
    discount = 100 * ((stock.high - stock.price) / stock.high)
    return stock._replace(discount=discount)

def rank_stocks(stock_evaluations, attribute, reverse=False):
    stock_evaluations.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

def main():

    tickers_file = 'tickers.txt'
    tickers = parse_tickers(tickers_file)

    stock_evaluations = []

    for ticker in tickers:
        try:
            raw_stock_data =  get_stock_data(ticker)

        except KeyError:
            print("Key Error", ticker)
            continue

        except IndexError:
            print("Index Error", ticker)
            continue

        evaluation = calculate_discount(raw_stock_data)
        stock_evaluations.append(evaluation)

    rank_stocks(stock_evaluations, "discount", True)
    pprint(stock_evaluations[0:10])

if __name__=="__main__":
    main()
