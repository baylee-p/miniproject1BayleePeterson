### INF601 - Advanced Programming in Python
### Baylee Peterson
### Mini Project 1

import pprint
import yfinance as yf

mytickers = ("MSFT", "AAPL", "NVDA", "GME", "AMC")

mydata = {}

for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                       'dailyHigh': result.info['dayHigh']
                       }

# get historical market data
#hist = msft.history(period="1mo")

pprint.pprint(mydata)