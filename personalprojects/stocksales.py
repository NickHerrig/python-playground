from collections import namedtuple
import time
from pprint import pprint

import yfinance as yf

Stock = namedtuple('Stock', 'name sector high low price book_value pb eps pe')

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
    )

def stock_evaluation(stock):
    discount = 100 * ((stock.high - stock.price) / stock.high)
    print(stock.name)
    print("{:.2f}% off!".format(discount))
    print(stock.price, "is the current price")
    print(f"book value: {stock.book_value} price to book: {stock.pb} earnings per share: {stock.eps} price to earnings: {stock.pe}")
    print("\n")

def main():

    tickers_file = 'tickers.txt'
    tickers = parse_tickers(tickers_file)

    stock_evaluations = []

    for ticker in tickers:
        start_time = time.perf_counter()

        try:
            raw_stock_data =  get_stock_data(ticker)

        except KeyError:
            print("KEEYYY ERRORR")
            break

        except IndexError:
            print("INDEXXX ERROR")
            break

        end_time = time.perf_counter()

        evaluation = stock_evaluation(raw_stock_data)
        stock_evaluations.append(evaluation)

    print(f"Downloaded stock data in {end_time - start_time} seconds")

if __name__=="__main__":
    main()
