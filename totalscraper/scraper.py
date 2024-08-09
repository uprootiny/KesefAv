import requests
import pandas as pd
import json
import os
from bs4 import BeautifulSoup

# Load configuration
def load_config(config_file='config.json'):
    with open(config_file) as f:
        return json.load(f)

# Fetch news data from NewsAPI
def fetch_news(api_key, query='technology', page_size=5):
    url = f'https://newsapi.org/v2/everything?q={query}&pageSize={page_size}&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        news_data = [{'source': article['source']['name'],
                      'author': article['author'],
                      'title': article['title'],
                      'description': article['description'],
                      'url': article['url'],
                      'publishedAt': article['publishedAt']}
                     for article in articles]
        return news_data
    else:
        response.raise_for_status()

# Fetch stock data from Finnhub
def fetch_stock_data(api_key, symbol='AAPL'):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stock_data = {
            'symbol': symbol,
            'current_price': data['c'],
            'high_price': data['h'],
            'low_price': data['l'],
            'open_price': data['o'],
            'previous_close': data['pc']
        }
        return stock_data
    else:
        response.raise_for_status()

# Scrape Market Watch
def scrape_market_watch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

# Save data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")

def main():
    config = load_config()

    news_api_key = config['api_keys']['newsapi']
    finnhub_api_key = config['api_keys']['finnhub']

    # Fetch news data
    news_data = fetch_news(news_api_key)
    save_to_csv(news_data, 'news_data.csv')

    # Fetch stock data
    stock_data = fetch_stock_data(finnhub_api_key)
    save_to_csv([stock_data], 'stock_data.csv')

    # Scrape market data (example URL, adjust as needed)
    market_watch_data = scrape_market_watch("https://www.marketwatch.com/investing/stock/aapl")
    print(market_watch_data.prettify())

if __name__ == '__main__':
    main()
