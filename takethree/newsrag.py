import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import math
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Fetch news articles from a given URL
def fetch_news_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.select('.article__headline'):
        title = item.get_text().strip()
        articles.append(title)
    
    return articles

# Analyze sentiment of a given text
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

# Calculate TF (Term Frequency)
def compute_tf(text):
    tf_dict = defaultdict(int)
    words = text.split()
    for word in words:
        tf_dict[word] += 1
    total_words = len(words)
    for word in tf_dict:
        tf_dict[word] = tf_dict[word] / total_words
    return tf_dict

# Calculate IDF (Inverse Document Frequency)
def compute_idf(documents):
    N = len(documents)
    idf_dict = defaultdict(int)
    all_words = set(word for doc in documents for word in doc.split())
    for word in all_words:
        idf_dict[word] = math.log(N / sum(word in doc.split() for doc in documents))
    return idf_dict

# Calculate TF-IDF
def compute_tfidf(tf, idf):
    tfidf = defaultdict(float)
    for word, tf_val in tf.items():
        tfidf[word] = tf_val * idf[word]
    return tfidf

# Calculate cosine similarity between two TF-IDF vectors
def cosine_similarity(tfidf1, tfidf2):
    intersection = set(tfidf1.keys()) & set(tfidf2.keys())
    numerator = sum(tfidf1[word] * tfidf2[word] for word in intersection)
    
    sum1 = sum(tfidf1[word] ** 2 for word in tfidf1.keys())
    sum2 = sum(tfidf2[word] ** 2 for word in tfidf2.keys())
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# Filter relevant articles using keyword matching and TF-IDF similarity
def filter_relevant_articles(articles, keywords):
    keyword_text = " ".join(keywords)
    documents = articles + [keyword_text]
    
    tf_docs = [compute_tf(doc) for doc in documents]
    idf = compute_idf(documents)
    tfidf_docs = [compute_tfidf(tf, idf) for tf in tf_docs]
    
    query_tfidf = tfidf_docs[-1]
    scores = [cosine_similarity(query_tfidf, doc_tfidf) for doc_tfidf in tfidf_docs[:-1]]
    
    relevant_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]
    relevant_articles = [(articles[i], scores[i]) for i in relevant_indices]
    
    return relevant_articles

# Get news sentiment and relevant articles
def get_news_sentiment_and_relevance(keywords):
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
    for article, score in relevant_articles:
        sentiment = analyze_sentiment(article)
        sentiments[article] = {
            "sentiment": sentiment,
            "relevance_score": score
        }
    
    return sentiments
