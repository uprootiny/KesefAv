
def fetch_market_data(ticker, start_date, end_date):
    import yfinance as yf

    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching market data for {ticker}: {e}")
        return None