import datetime
import numpy as np
import yfinance as yf
from scipy.stats import norm  # For cumulative distribution function

def get_risk_free_rate_from_etf():
    treasury_etf = yf.Ticker("SHY")  # Short-term bond ETF
    yield_rate = treasury_etf.info.get('yield', 0.0)  # Get the yield
    return yield_rate / 100  # Convert percentage to decimal

class Company(yf.Ticker):
    def __init__(self, ticker, session=None, proxy=None):
        super().__init__(ticker, session, proxy)

    def get_current_stock_price(self):
        price = self.info['currentPrice']
        return price

    def get_expirations(self):
        return self.options

    def chose_expirations(self):
        options = self.get_expirations()
        print("Available Expirations:")
        
        for index in range(len(options)):
            print(f"{index:>2}: {options[index]}")
        
        choice = int(input(f"Enter an option number (0 --> {len(options)-1}): "))
        selected_expiration = options[choice]
        print(f"Selected expiration: {selected_expiration}")
        
        return selected_expiration

    def time_to_expiration(self, input_date):
        input_date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
        current_date = datetime.datetime.today()
        days_difference = (input_date - current_date).days
        years_difference = days_difference / 365.0
        return round(years_difference, 6)

    def get_strike_price(self, expiration_date):
        options = self.option_chain(expiration_date)
        return options.calls

    def chose_strike_price(self, expiration_date):
        strike_prices = self.get_strike_price(expiration_date)
        print("Available Strike Prices:")
        for index, strike in enumerate(strike_prices["strike"]):
            print(f"{index:>2}: {strike}")
        
        choice = int(input(f"Choose an option number (0 --> {len(strike_prices['strike'])-1}): "))
        selected_strike = strike_prices["strike"][choice]
        
        return selected_strike

    def calculate_volatility(self, period="1mo"):
        historical_data = self.history(period=period)
        log_returns = np.log(historical_data['Close'] / historical_data['Close'].shift(1))
        volatility = log_returns.std() * np.sqrt(252)  # Annualize the volatility
        return round(volatility, 6)

    def calculate_option_price(self, S, K, T, r, sigma):
        d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        call_price = (S * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
        return round(call_price, 6)

    def get_market_option_price(self, expiration_date, strike_price):
        options = self.option_chain(expiration_date).calls
        market_price = options.loc[options['strike'] == strike_price, 'lastPrice']
        if not market_price.empty:
            return market_price.values[0]
        else:
            return None


# Example usage
apple = Company("AAPL")

# Get current stock price
current_stock_price = apple.get_current_stock_price()
print(f"Current Stock Price: {current_stock_price}")

# Get expiration date
expiration_date = apple.chose_expirations()

# Calculate time to expiration
time_to_expiration = apple.time_to_expiration(expiration_date)
print(f"Time to Expiration (years): {time_to_expiration}")

# Choose a strike price
strike_price = apple.chose_strike_price(expiration_date)
print(f"Chosen Strike Price: {strike_price}")

# Calculate historical volatility
volatility = apple.calculate_volatility()
print(f"Historical Volatility: {volatility}")

# Get risk-free rate
risk_free_rate = get_risk_free_rate_from_etf()
print(f"Risk-Free Rate: {risk_free_rate}")

# Calculate Black-Scholes option price
calculated_option_price = apple.calculate_option_price(
    S=current_stock_price,
    K=strike_price,
    T=time_to_expiration,
    r=risk_free_rate,
    sigma=volatility
)
print(f"Calculated Option Price: {calculated_option_price}")

# Get market option price for comparison
market_option_price = apple.get_market_option_price(expiration_date, strike_price)
if market_option_price is not None:
    print(f"Market Option Price: {market_option_price}")
else:
    print("Market option price data not available for the selected expiration and strike price.")