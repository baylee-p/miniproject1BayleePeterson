### INF601 - Advanced Programming in Python
### Baylee Peterson
### Mini Project 1

import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

# Create charts folder if doesn't exist
os.makedirs("charts", exist_ok=True)

# Get today's date and calculate the date 10 business days ago
today = datetime.now()
ten_days_ago = today - timedelta(days=13)

# Program to create graphs of the five stocks
mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Days')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} last 10 closing prices")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")
