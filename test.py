import yfinance as yf
import pandas as pd

def get_0050_price(start_date, end_date):
    ticker = "0050.TW"
    data = yf.download(ticker, start=start_date, end=end_date)
    return data["Adj Close"]

start_date = "2022-01-01"
end_date = "2022-02-28"
prices = get_0050_price(start_date, end_date)
print(prices)