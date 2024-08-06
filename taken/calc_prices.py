import ta
import pandas as pd

def calculate_indicators(data):
    # Ensure data is a DataFrame and contains necessary columns
    if not isinstance(data, pd.DataFrame) or 'Close' not in data.columns or 'High' not in data.columns or 'Low' not in data.columns or 'Volume' not in data.columns:
        print("Invalid data format")
        return None

    # Calculate Indicators
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=14).rsi()
    data['SMA'] = ta.trend.SMAIndicator(data['Close'], window=20).sma_indicator()
    data['EMA'] = ta.trend.EMAIndicator(data['Close'], window=20).ema_indicator()
    data['Upper Band'] = ta.volatility.BollingerBands(data['Close']).bollinger_hband()
    data['Middle Band'] = ta.volatility.BollingerBands(data['Close']).bollinger_mavg()
    data['Lower Band'] = ta.volatility.BollingerBands(data['Close']).bollinger_lband()
    data['VWAP'] = ta.volume.VolumeWeightedAveragePrice(data['High'], data['Low'], data['Close'], data['Volume']).volume_weighted_average_price()
    data['MACD'] = ta.trend.MACD(data['Close']).macd()
    data['MACD Signal'] = ta.trend.MACD(data['Close']).macd_signal()
    data['MACD Hist'] = ta.trend.MACD(data['Close']).macd_diff()

    # Handle NaNs and infinite values
    data = data.fillna(0)
    data = data.replace([float('inf'), float('-inf')], 0)
    
    return data

def display_market_data(indicators: pd.DataFrame, company, ticker):
    print(f"Market data for {company} ({ticker}):")
    df_indi: pd.DataFrame = indicators[['Open', 'High', 'Low', 'Close', 'RSI', 'SMA', 'EMA', 'MACD', 'MACD Signal']]
    print(df_indi.tail())
    dmpr.dump_indicators(ticker, df_indi)
    print(f"dumped {ticker}")