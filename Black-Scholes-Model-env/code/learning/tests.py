import yfinance as yf

company_id = "AAPL"
apple = yf.Ticker(company_id)

# Fetch the last price from the 'info' attribute
last_price = apple.info["currentPrice"]
print(f"The last price of Apple was {last_price}")

# Fetch the balance sheet
balance_sheet = apple.balance_sheet
print(balance_sheet)

# Access "Ordinary Shares Number" from the balance sheet
if "Ordinary Shares Number" in balance_sheet.index:
    ordinary_shares = balance_sheet.loc["Ordinary Shares Number"][0]  # Access the most recent value
    total_for_ordinary_shares = float(last_price) * ordinary_shares
    print(f"Total for ordinary shares: {total_for_ordinary_shares}")
else:
    print("Ordinary Shares Number not found in balance sheet.")