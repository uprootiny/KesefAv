import pandas as pd

def display_market_data(market_data, company, ticker):
    print(f"Market data for {company} ({ticker}):")
    print(market_data.head())

def display_sentiment_analysis(news_sentiments, company):
    print(f"Sentiment analysis for {company}:")
    for article, info in news_sentiments.items():
        print(f"Article: {article}")
        print(f"Sentiment: {info['sentiment']}")
        print(f"Relevance Score: {info['relevance_score']}")
    print("\n")

def display_data_with_sentiment(market_data, news_sentiments, company, ticker):
    print(f"Market data for {company} ({ticker}):")
    print(market_data.head())
    
    print(f"Sentiment analysis for {company}:")
    for article, details in news_sentiments.items():
        print(f"Article: {article}")
        print(f"Relevance Score: {details['relevance_score']}")
        print(f"Sentiment: {details['sentiment']}")
        print("\n")

    print("\n" + "="*50 + "\n")

