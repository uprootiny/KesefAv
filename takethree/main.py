import pandas as pd
import yfinance as yf
import json
from news_analysis import get_news_sentiment

def fetch_market_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

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
            print(f"Market data for {company} ({ticker}):")
            print(market_data.head())
    
            keywords = [company, ticker, category]  # Customize keywords as needed
            news_sentiments = get_news_sentiment(keywords)
            print(f"Sentiment analysis for {company}:")
            for article, sentiment in news_sentiments.items():
                print(f"Article: {article}")
                print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
