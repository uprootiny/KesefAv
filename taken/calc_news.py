from typing import List
from sentence_transformers import SentenceTransformer, util

def filter_relevant_articles(articles_ld: List[dict], keywords, model):
    if isinstance(articles_ld[0], str):
        articles = articles_ld
    else:
        assert isinstance(articles_ld[0], dict)
        articles = [a['title'] for a in articles_ld]

    keywords_text = " ".join(keywords)
    articles.append(keywords_text)
    
    embeddings = model.encode(articles, convert_to_tensor=True)
    keyword_embedding = embeddings[-1]
    article_embeddings = embeddings[:-1]
    
    cosine_scores = util.pytorch_cos_sim(keyword_embedding, article_embeddings).flatten()
    srtd = cosine_scores.argsort(descending=True)
    relevant_indices = srtd[:min(5, len(srtd))]  # Top 3 relevant articles
    
    if articles is articles_ld:
        relevant_articles = [(articles[i], cosine_scores[i].item()) for i in relevant_indices]
    else:
        relevant_articles = [dict(relevance_score=cosine_scores[i].item(),**articles_ld[i]) for i in relevant_indices]
    
    return relevant_articles

# Analyze sentiment of a given text
def analyze_sentiment(text):
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    return sentiment

# class RelevanceAndSentiment:

def relevance_and_sentiment(all_articles, keywords, tag_it=None) -> List[dict]:
    the_model =  SentenceTransformer('paraphrase-MiniLM-L6-v2')
    relevant_articles: List[dict] = filter_relevant_articles(all_articles, keywords, the_model)
    sentiments: List[dict] = just_sentiment(relevant_articles)
    if tag_it:
        for sent in sentiments:
            sent.update(**tag_it)

    return sentiments

def just_sentiment(relevant_articles: List[dict]) -> List[dict]:
        for it_info in relevant_articles:
            sentiment = analyze_sentiment(it_info['title'])
            it_info['sentiment'] = sentiment
        return relevant_articles