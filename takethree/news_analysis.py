import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def fetch_news_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.select('.article__headline'):
        title = item.get_text().strip()
        articles.append(title)
    
    return articles

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

def filter_relevant_articles(articles, keywords):
    relevant_articles = []
    for article in articles:
        if any(keyword.lower() in article.lower() for keyword in keywords):
            relevant_articles.append(article)
    return relevant_articles

def get_news_sentiment(keywords):
    urls = [
        "https://www.marketwatch.com/latest-news",
        # Add more URLs as needed
    ]
    
    all_articles = []
    for url in urls:
        articles = fetch_news_articles(url)
        all_articles.extend(articles)
    
    relevant_articles = filter_relevant_articles(all_articles, keywords)
    
    sentiments = {}
    for article in relevant_articles:
        sentiment = analyze_sentiment(article)
        sentiments[article] = sentiment
    
    return sentiments
