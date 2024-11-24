# Black-Scholes-Merton Model

The **Black-Scholes-Merton model** calculates the fair price of **European options** using the underlying asset’s price, strike price, time to expiration, risk-free rate, and volatility. It assumes constant volatility and no arbitrage, providing a widely used formula for pricing and hedging in financial markets.

---

## Brief Explanation

The **Black-Scholes model** is a mathematical formula used to calculate the **fair price of an option**.

![BlackScholesEquation](https://github.com/user-attachments/assets/9fa32f53-38d1-4532-9f6e-cf7357e071ab)

### Where:
- **St**: Current stock price.
- **K**: Strike (exercise) price.
- **N(d1), N(d2)**: Cumulative probability distributions.
- **e^(-rt)**: Discount factor (where `r` is the risk-free interest rate, and `t` is the time to expiration).

### What is an option?
An **option** is a financial contract giving the buyer the right (but not the obligation) to **buy** or **sell** an asset (like a stock) at a fixed price (strike price) before or on a specific date.

---

### What does the model do?

It helps answer: **How much is this option worth today?**

To do this, the model considers:
1. **Stock price**: Current value of the stock.
2. **Strike price**: Price at which the option can be exercised.
3. **Time to expiration**: Remaining time until the option expires.
4. **Risk-free interest rate**: The return from a "risk-free" investment (e.g., government bonds).
5. **Volatility**: Expected price fluctuations of the stock.

---

### Why is it useful?

Traders and investors use it to:
- Determine the **fair price** of an option.
- Assess the **risk** and **reward** of an option.
- Evaluate if an option is **overpriced** or **underpriced** in the market.

---

## Ticker Objects in `yfinance`

In the `yfinance` library, each company is represented by a **Ticker object**. This object provides access to a wide range of financial data about the company.

### **Attributes** (Access Data)
The following are the key attributes available in a Ticker object:

| **Attribute**            | **Description**                                                                 |
|--------------------------|-------------------------------------------------------------------------------|
| `actions`                | Corporate actions like splits and dividends.                                  |
| `analyst_price_targets`  | Analyst price target data (high, low, average).                               |
| `calendar`               | Upcoming company events (e.g., earnings release dates).                      |
| `dividends`              | Historical dividend payments.                                                |
| `earnings`               | Historical and upcoming earnings data.                                       |
| `financials`             | Yearly financial statements.                                                 |
| `quarterly_financials`   | Quarterly financial statements.                                              |
| `history`                | Historical stock price data (open, high, low, close, volume).                |
| `info`                   | General information about the company (sector, market cap, etc.).            |
| `options`                | Available options expiration dates.                                          |
| `recommendations`        | Analyst recommendations (buy, hold, sell).                                   |
| `sustainability`         | ESG (environmental, social, governance) metrics.                             |

---

### **Methods** (Retrieve Data)

| **Method**                       | **Description**                                                                                     |
|----------------------------------|-----------------------------------------------------------------------------------------------------|
| `get_actions()`                  | Retrieves corporate actions.                                                                        |
| `get_analyst_price_targets()`    | Fetches analyst price targets.                                                                      |
| `get_balance_sheet()`            | Retrieves the balance sheet (yearly/quarterly).                                                     |
| `get_cash_flow()`                | Retrieves cash flow data (yearly/quarterly).                                                        |
| `get_dividends()`                | Gets historical dividend data.                                                                      |
| `get_earnings()`                 | Retrieves earnings data (yearly/quarterly).                                                         |
| `get_earnings_dates()`           | Fetches historical and future earnings dates.                                                       |
| `get_financials()`               | Retrieves financial statements.                                                                     |
| `get_history(period='1mo')`      | Retrieves historical price data for the specified period (e.g., 1 month).                           |
| `get_info()`                     | Returns general company info as a dictionary.                                                       |
| `get_options()`                  | Fetches options data (call/put).                                                                    |
| `get_recommendations()`          | Retrieves analyst recommendations.                                                                  |
| `option_chain(date=None)`        | Retrieves the option chain for a specific expiration date (default is the nearest).                 |

---

### Example Usage
Here's an example of how you can use `yfinance` to retrieve and display data:

```python
import yfinance as yf

# Initialize the Ticker object for Microsoft
ticker = yf.Ticker("MSFT")

# Get and print company info
print("Company Info:")
print(ticker.info)

# Get historical price data for the last month
print("\nHistorical Prices (1 month):")
print(ticker.history(period='1mo'))

# Get upcoming earnings calendar
print("\nEarnings Calendar:")
print(ticker.calendar)

# Get call options for the nearest expiration date
if ticker.options:
    nearest_exp = ticker.options[0]
    call_options = ticker.option_chain(nearest_exp).calls
    print("\nCall Options:")
    print(call_options)
else:
    print("\nNo options available.")