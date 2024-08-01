import pandas as pd
import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Fetch market data
def fetch_market_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Analyze sentiment
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

# Example usage
ticker = 'AAPL'
start_date = '2023-01-01'
end_date = '2024-01-01'
market_data = fetch_market_data(ticker, start_date, end_date)
print(market_data.head())

sample_text = "This is a great day for the market!"
sentiment = analyze_sentiment(sample_text)
print(sentiment)
