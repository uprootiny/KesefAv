import pandas as pd
import sys
import json
from pathlib import Path
from hashlib import sha256
import pandas as pd
import dumper
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

dmpr = dumper.get_Dumper()

def display_market_data(indicators: pd.DataFrame, company, ticker):
    print(f"Market data for {company} ({ticker}):")
    df_indi: pd.DataFrame = indicators[['Open', 'High', 'Low', 'Close', 'RSI', 'SMA', 'EMA', 'MACD', 'MACD Signal']]
    print(df_indi.tail())
    dmpr.dump_indicators(ticker, df_indi)
    print(f"dumped {ticker}")

def display_sentiment_analysis(news_sentiments, company, ticker):
    article_info = {}
    print(f"Sentiment analysis for {company}: {ticker}")
    for article, info in news_sentiments.items():
        print(f"Article: {article}")
        print(f"Sentiment: {info['sentiment']}")
        print(f"Relevance Score: {info['relevance_score']:.2f}")
        
        article_info = dict()
        article_info['title'] = str(article)
        # article_info['sentiment'] = info['sentiment']
        # article_info['relevance_score'] = info['relevance_score']
        # eprint(json.dumps(article_info))
        sha_id = sha256(article_info['title'].encode('utf-8')).hexdigest()
        article_info['sha_id'] = sha_id
        article_info.update(**info)
        dmpr.dump_article_yaml(article_info)
    print("\n")

def display_data_with_sentiment(indicators, news_sentiments, company, ticker):
    display_market_data(indicators, company, ticker)
    display_sentiment_analysis(news_sentiments, company, ticker)
    print("\n" + "="*50 + "\n")
