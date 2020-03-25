from collections import namedtuple
import time
from pprint import pprint
import concurrent.futures

import yfinance as yf

Stock = namedtuple('Stock', 'name sector high price discount ticker')

def parse_tickers(ticker_file):
    with open(ticker_file) as f:
        tickers = f.read().splitlines()
    return tickers

def load_stock_data(ticker):
    ticker_object = yf.Ticker(ticker)
    stock_data = ticker_object.info
    return stock_data

def parse_stock_data(stock_data, ticker):

    delta  = stock_data['fiftyTwoWeekHigh'] - stock_data['regularMarketPrice']
    discount = 100 * (delta / stock_data['fiftyTwoWeekHigh'])

    return Stock(
    stock_data['longName'],
    stock_data['sector'],
    stock_data['fiftyTwoWeekHigh'],
    stock_data['regularMarketPrice'],
    discount,
    ticker
    )

def rank_stocks(stock_evaluations, attribute, reverse=False):
    return sorted(stock_evaluations, key=lambda x: getattr(x, attribute), reverse=reverse)
    #stock_evaluations.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

def main():

    stock_reports = []
    tickers_file = 'tickers.txt'
    tickers = parse_tickers(tickers_file)

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ticker = {executor.submit(load_stock_data, ticker): ticker for ticker in tickers}
        for future in concurrent.futures.as_completed(future_to_ticker):
            ticker = future_to_ticker[future]
            try:
                print("Processing Ticker: ", ticker)
                data = future.result()
                parsed_data = parse_stock_data(data, ticker)
                stock_reports.append(parsed_data)

            except Exception as exc:
                print('%r generated an exception: %s' % (ticker, exc))

    discount_report = rank_stocks(stock_reports, "discount", True)
    pprint(discount_report)

if __name__=="__main__":
    main()
