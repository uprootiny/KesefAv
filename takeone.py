import pandas as pd
import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def fetch_market_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

def integrate_data(market_data, media_sentiments):
    combined_data = market_data.copy()
    combined_data['sentiment'] = media_sentiments
    return combined_data

ticker = 'AAPL'
start_date = '2023-01-01'
end_date = '2024-01-01'

market_data = fetch_market_data(ticker, start_date, end_date)
media_sentiments = [analyze_sentiment('sample news text') for _ in range(len(market_data))]
combined_data = integrate_data(market_data, media_sentiments)

print(combined_data.head())


def validate_assumptions(data, indicator_column, threshold):
    valid_periods = data[data[indicator_column] > threshold]
    return valid_periods

indicator_column = 'RSI'
threshold = 70

valid_periods = validate_assumptions(combined_data, indicator_column, threshold)
print(f"Valid periods for trading: {len(valid_periods)}")


def trading_strategy(data, buy_threshold, sell_threshold):
    data['position'] = None
    data['position'][data['RSI'] < buy_threshold] = 'buy'
    data['position'][data['RSI'] > sell_threshold] = 'sell'
    return data

buy_threshold = 30
sell_threshold = 70

strategy_data = trading_strategy(combined_data, buy_threshold, sell_threshold)
print(strategy_data[['RSI', 'position']].dropna().head())
