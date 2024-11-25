import yfinance as yf

dat = yf.Ticker("MSFT")

dates = dat.calendar
for date in dates:
    print(date, dates[date])