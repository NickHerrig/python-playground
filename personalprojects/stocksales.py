from collections import namedtuple
import time
from pprint import pprint
import concurrent.futures

import yfinance as yf

Stock = namedtuple('Stock', 'name sector high low price book_value pb eps pe discount')

def parse_tickers(ticker_file):
    with open(ticker_file) as f:
        tickers = f.read().splitlines()
    return tickers

def load_stock_data(ticker):
    ticker_object = yf.Ticker(ticker)
    stock_data = ticker_object.info
    return stock_data

def parse_stock_data(stock_data):

    delta  = stock_data['fiftyTwoWeekHigh'] - stock_data['regularMarketPrice']
    discount = 100 * (delta / stock_data['fiftyTwoWeekHigh'])

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
    discount,
    )

def rank_stocks(stock_evaluations, attribute, reverse=False):
    stock_evaluations.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

def main():

    stock_reports = []
    tickers_file = 'tickers.txt'
    tickers = parse_tickers(tickers_file)

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_to_ticker = {executor.submit(load_stock_data, ticker): ticker for ticker in tickers}
        for future in concurrent.futures.as_completed(future_to_ticker):
            ticker = future_to_ticker[future]
            try:
                print("Processing Ticker: ", ticker)
                data = future.result()
                parsed_data = parse_stock_data(data)

            except Exception as exc:
                print('%r generated an exception: %s' % (ticker, exc))

            stock_reports.append(parsed_data)

    rank_stocks(stock_reports, "discount", True)
    pprint(stock_reports(:24)

if __name__=="__main__":
    main()
