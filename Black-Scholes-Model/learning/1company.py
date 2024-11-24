import yfinance as yf


dat = yf.Ticker("MSFT")

import yfinance as yf

def debreif(Comp):
    # Initialize the Ticker object for Microsoft
    dat = yf.Ticker(Comp)

    # Print general information about the company
    print("Company Info:")
    print(dat.info)

    # Print the calendar of upcoming events
    print("\nCompany Calendar:")
    print(dat.calendar)

    # Print analyst price targets
    print("\nAnalyst Price Targets:")
    print(dat.analyst_price_targets)

    # Print the quarterly income statement
    print("\nQuarterly Income Statement:")
    print(dat.quarterly_income_stmt)

    # Print historical stock prices for the last month: 
    print("\nHistorical Stock Prices (1 Month):")
    print(dat.history(period='1mo'))

    # Get and print call options for the nearest expiration date
    if dat.options:
        nearest_expiration_date = dat.options[0]  # Nearest expiration date
        call_options = dat.option_chain(nearest_expiration_date).calls
        print("\nCall Options for Nearest Expiration Date:")
        print(call_options)
    else:
        print("\nNo options data available for this stock.")