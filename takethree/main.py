import pandas as pd
import yfinance as yf
import json
from newsrag import get_news_sentiment_and_relevance
from tabular_output import display_data_with_sentiment
from indicators import calculate_indicators

def fetch_market_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching market data for {ticker}: {e}")
        return None

def read_tickers(file_path):
    with open(file_path, 'r') as file:
        stock_list = json.load(file)
    tickers = {category: tickers for category, tickers in stock_list.items()}
    return tickers

def main():
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    tickers = read_tickers('stock_list.json')
    
    for category, stocks in tickers.items():
        print(f"Category: {category}")
        for company, ticker in stocks.items():
            market_data = fetch_market_data(ticker, start_date, end_date)
            if market_data is not None:
                indicators = calculate_indicators(market_data)
                if not indicators.empty:
                    keywords = [company, ticker, category]
                    news_sentiments = get_news_sentiment_and_relevance(keywords)
                    
                    if news_sentiments:
                        display_data_with_sentiment(indicators, news_sentiments, company, ticker)

if __name__ == "__main__":
    from pathlib import Path
    Path("__data").mkdir(exist_ok=True)

    main()
