from data_retrieval import fetch_most_traded_tickers, organize_tickers
from sentiment_analysis import analyze_sentiments  # Ensure this module does not use fetch_most_traded_tickers
from volatility_analysis import analyze_volatility
from alert_system import alert_system

def main():
    tickers = fetch_most_traded_tickers()
    organized_tickers = organize_tickers(tickers)
    sentiment_scores = analyze_sentiments(tickers)
    volatilities = analyze_volatility(tickers)
    alert_system(tickers, volatilities, sentiment_scores)

if __name__ == "__main__":
    main()
