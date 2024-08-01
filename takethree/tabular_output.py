import pandas as pd

def display_market_data(indicators, company, ticker):
    print(f"Market data for {company} ({ticker}):")
    print(indicators[['Open', 'High', 'Low', 'Close', 'RSI', 'SMA', 'EMA', 'MACD', 'MACD Signal']].head())

def display_sentiment_analysis(news_sentiments, company):
    print(f"Sentiment analysis for {company}:")
    for article, info in news_sentiments.items():
        print(f"Article: {article}")
        print(f"Sentiment: {info['sentiment']}")
        print(f"Relevance Score: {info['relevance_score']:.2f}")
    print("\n")

def display_data_with_sentiment(indicators, news_sentiments, company, ticker):
    display_market_data(indicators, company, ticker)
    display_sentiment_analysis(news_sentiments, company)
    print("\n" + "="*50 + "\n")
