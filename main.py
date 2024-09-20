### INF601 - Advanced Programming in Python
### Baylee Peterson
### Mini Project 1

import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import copy

# Get today's date and calculate the date 10 business days ago
today = datetime.now()
ten_days_ago = today - timedelta(days=13)



mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mydata = {}

mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        maxlist = copy.copy(last10days)
        maxlist.sort()
        max_price = maxlist[-1]+10
        min_price = maxlist[0]-10
        myarray = np.array(last10days)
        plt.plot(myarray)
        plt.xlabel('Days')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} last 10 closing prices")
        plt.show()
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")

# get historical market data
#hist = msft.history(period="1mo")
#pprint.pprint(mydata)