import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer, util
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

url_holder = {}
# Fetch news articles from a given URL
def fetch_news_articles(url, selector):
    if url in url_holder:
        return url_holder[url]
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.select(selector):
        title = item.get_text().strip()
        articles.append(title)
    url_holder[url] = articles
    return articles

# Analyze sentiment of a given text
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

# Filter relevant articles using contextual embeddings
def filter_relevant_articles(articles, keywords, model):
    keywords_text = " ".join(keywords)
    articles.append(keywords_text)
    
    embeddings = model.encode(articles, convert_to_tensor=True)
    keyword_embedding = embeddings[-1]
    article_embeddings = embeddings[:-1]
    
    cosine_scores = util.pytorch_cos_sim(keyword_embedding, article_embeddings).flatten()
    srtd = cosine_scores.argsort(descending=True)
    relevant_indices = srtd[:min(12, len(srtd))]  # Top 3 relevant articles
    
    relevant_articles = [(articles[i], cosine_scores[i].item()) for i in relevant_indices]
    
    return relevant_articles

# Get news sentiment and relevant articles
def get_news_sentiment_and_relevance(keywords):
    with open('cfg_news_sources.json', 'r') as file:
        sources = json.load(file)['sources']
    company, ticker, category = keywords
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    
    all_articles = []
    for source in sources:
        print(f"--- processing source {source['url']}")
        try:
            articles = fetch_news_articles(source['url'], source['selector'])
            print(f"--- processing source {source['url']}. fetched {len(articles)}")

            all_articles.extend(articles)
        except Exception as e:
            print(f"Error fetching articles from {source['name']} ({source['url']}): {e}")
    
    relevant_articles = filter_relevant_articles(all_articles, keywords, model)
    
    sentiments = {}
    for article, score in relevant_articles:
        sentiment = analyze_sentiment(article)
        sentiments[article] = {
            "sentiment": sentiment,
            "relevance_score": score,
            "url": source['url'],
            "company": company,
            "ticker": ticker,
            'category': category
        }
    
    return sentiments
