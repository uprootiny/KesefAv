# INSTALL.md

python -m venv kesef-av-env
source kesef-av-env/bin/activate
pip install yfinance ta pandas sentence-transformers beautifulsoup4 requests vaderSentiment

python takethree/main.py


# Expected output:

(kesef-av-env) (kesef-av-env) ➜  KesefAv git:(main*)python takethree/main.py
/Users/other/Projects/KesefAv/kesef-av-env/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Category: Biotech
[*********************100%%**********************]  1 of 1 completed
Market data for Halozyme Therapeutics (HALO):
                 Open       High        Low      Close  ...  VWAP  MACD  MACD Signal  MACD Hist
Date                                                    ...                                    
2023-01-03  56.990002  57.000000  55.110001  55.130001  ...   NaN   NaN          NaN        NaN
2023-01-04  55.130001  55.610001  53.419998  53.900002  ...   NaN   NaN          NaN        NaN
2023-01-05  53.799999  54.680000  53.369999  54.230000  ...   NaN   NaN          NaN        NaN
2023-01-06  54.779999  55.599998  54.009998  55.480000  ...   NaN   NaN          NaN        NaN
2023-01-09  55.709999  56.490002  54.869999  55.040001  ...   NaN   NaN          NaN        NaN

[5 rows x 16 columns]
Sentiment analysis for Halozyme Therapeutics:
Article: Simone Biles credits therapy for her success at the Paris Olympics
Relevance Score: 0.25
Sentiment: {'neg': 0.0, 'neu': 0.592, 'pos': 0.408, 'compound': 0.7351}


Article: Forget Nvidia: Billionaire Ken Griffin Raised His Position in This Rival AI Stock by More Than 500%
Relevance Score: 0.20
Sentiment: {'neg': 0.106, 'neu': 0.894, 'pos': 0.0, 'compound': -0.2263}


Article: Cramer's Lightning Round: Advanced Micro Devices is a buy
Relevance Score: 0.19
Sentiment: {'neg': 0.0, 'neu': 0.8, 'pos': 0.2, 'compound': 0.25}



==================================================

[*********************100%%**********************]  1 of 1 completed
Market data for United Therapeutics (UTHR):
                  Open        High         Low  ...  MACD  MACD Signal  MACD Hist
Date                                            ...                              
2023-01-03  276.260010  277.670013  272.100006  ...   NaN          NaN        NaN
2023-01-04  272.470001  273.890015  270.170013  ...   NaN          NaN        NaN
2023-01-05  274.109985  275.519989  270.600006  ...   NaN          NaN        NaN
2023-01-06  274.950012  279.140015  272.940002  ...   NaN          NaN        NaN
2023-01-09  275.470001  275.970001  263.410004  ...   NaN          NaN        NaN

[5 rows x 16 columns]
Sentiment analysis for United Therapeutics:
Article: Analyst Report: Bread Financial Holdings, Inc.
Relevance Score: 0.21
Sentiment: {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}