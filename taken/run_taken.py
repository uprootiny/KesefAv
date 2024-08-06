import fetch_prices
import calc_prices 

import fetch_news
import calc_news

import dump_indi
import conf_tickers

dumper = dump_indi.get_EDumper()


def fetch_and_persit_ticker(ticker, start_date, end_date):
    market_data = fetch_prices.fetch_market_data(ticker, start_date, end_date)
    
    dumper.dump_indicators(".md."+ticker, market_data)
    
    indicators = calc_prices.calculate_indicators(market_data)
    dumper.dump_indicators(ticker, indicators)
    # persistor.persist(indicators)

def fetch_and_persist_news(ticker="", company="", category=""):

    bri = fetch_news.FetchNews()
    all_articles: List[dict] = bri.get_all_articles()
    
    sentiments = calc_news.relevance_and_sentiment(
        all_articles,
        keywords=[company, ticker, category],
            tag_it = {
                "company": company,
                "ticker": ticker,
                'category': category}
        )


    dumper.dump_sentiment_analysis(sentiments,company,category)

def main():
    # print(f"{cf_ticker.tickers_flat}")
    ticker = 'PLTK'
    
    cf_ticker = conf_tickers.ConfTicker()
    company = cf_ticker.tickers_flat[ticker]['company']
    category = cf_ticker.tickers_flat[ticker]['category']

    fetch_and_persist_news(
        ticker=ticker, 
        company=company, 
        category=category)
    # -----
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    fetch_and_persist_news('ticker', start_date, end_date)


if __name__ == "__main__":
    main()