import pandas as pd
import sys
import json
from pathlib import Path
from hashlib import sha256


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def dump_to_table():
    engine = create_engine(
    'postgresql+psycopg2://username:password@host:port/database')

    # Drop old table and create new empty table
    df.head(0).to_sql('table_name', engine, if_exists='replace',index=False)

    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, 'table_name', null="") # null values become ''
    conn.commit()
    cur.close()
    conn.close()


def display_market_data(indicators, company, ticker):
    print(f"Market data for {company} ({ticker}):")
    print(indicators[['Open', 'High', 'Low', 'Close', 'RSI', 'SMA', 'EMA', 'MACD', 'MACD Signal']].head())

def display_sentiment_analysis(news_sentiments, company):
    article_info = {}
    print(f"Sentiment analysis for {company}:")
    for article, info in news_sentiments.items():
        print(f"Article: {article}")
        print(f"Sentiment: {info['sentiment']}")
        print(f"Relevance Score: {info['relevance_score']:.2f}")
        
        article_info['content'] = str(article)
        article_info['sentiment'] = info['sentiment']
        article_info['relevance_score'] = info['relevance_score']
        # eprint(json.dumps(article_info))
        sha_id = sha256(article_info['content'].encode('utf-8')).hexdigest()
        
        article_info['sha_id'] = sha_id
        # filename = f"{sha_id}.json"
        filename = "block.json"
        filepath = f"__data/{filename}"
        # Path(filepath).wr(json.dumps(article_info))
        filepath = f"__data/{filename}"
        item =  json.dumps(article_info)
        line_item = f"- {item}\n"
        with open(filepath, "a") as fd:
            fd.write(line_item)

    print("\n")

def display_data_with_sentiment(indicators, news_sentiments, company, ticker):
    display_market_data(indicators, company, ticker)
    display_sentiment_analysis(news_sentiments, company)
    print("\n" + "="*50 + "\n")
