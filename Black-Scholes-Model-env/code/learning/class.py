import yfinance as yf
import pandas as pd
company_id = "MSFT"
Microsoft = yf.Ticker(company_id)


print(Microsoft.recommendations_summary)

# literaly just a testing function to gather basic info on the company. 
def background_info(company):
    
    info = company.get_info()
    data = pd.DataFrame.from_dict(info, orient='index').T

    #print(data)
    #print(data['address1'][0])
    print(f"The company is based in {data["country"][0]}")
#background_info(Microsoft)


class Company(yf.Ticker):
    def __init__(self, ticker, session=None, proxy=None):
        super().__init__(ticker, session, proxy)


Apple = Company("AAPl")
print(Apple.news)