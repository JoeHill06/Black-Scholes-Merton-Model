import yfinance as yf

dat = yf.Ticker("MSFT")

print(dat.fast_info)