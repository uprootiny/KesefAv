class ConfTicker:

    def __init__(self, file_path='cfg_stock_list.json'):
        self.cfg_file_path = file_path
        self.tickers_org: dict = {}
        self.tickers_flat: dict = {}
        self.load_tickers_info(self.cfg_file_path)

    def load_tickers_info(self, file_path='cfg_stock_list.json'):
        import json

        with open(file_path, 'r') as file:
            stock_list = json.load(file)
        self.tickers_org = {category: tickers for category, tickers in stock_list.items()}
        
        for category, tickers in stock_list.items():
            for company, ticker_id in tickers.items():
                self.tickers_flat[ticker_id] = {
                    'category': category,
                    'company': company,
                    'ticker_id': ticker_id
                }
        
        return self
