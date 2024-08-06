from typing import List, Dict
class FetchNews:
    url_holder = {}
    
    def __init__(self):
        import json
        with open('cfg_news_sources.json', 'r') as file:
            self.sources = json.load(file)['sources']
        
    # Fetch news articles from a given URL
    @classmethod
    def fetch_news_articles(cls, url, selector) -> List[dict]:
        import requests
        from bs4 import BeautifulSoup

        if url in cls.url_holder:
            return cls.url_holder[url]
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        articles = []
        for item in soup.select(selector):
            title = item.get_text().strip()
            tar_item = dict(title=title, url=url)
            print(tar_item)
            articles.append(tar_item)

        cls.url_holder[url] = articles
        return articles


    # Get news sentiment and relevant articles
    def get_all_articles(self) -> List[dict]:
        all_articles: List[dict] = []
        for source in self.sources:
            print(f"--- processing source {source['url']}")
            try:
                articles = FetchNews.fetch_news_articles(source['url'], source['selector'])
                print(f"--- processing source {source['url']}. fetched {len(articles)}")
                all_articles.extend(articles)
            except Exception as e:
                print(f"Error fetching articles from {source['name']} ({source['url']}): {e}")
        
        return all_articles