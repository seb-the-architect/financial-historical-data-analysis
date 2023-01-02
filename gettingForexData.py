from oanda_api import OandaAPI
import pandas as pd

api = OandaAPI()

pure_df = pd.read_pickle("pure_data.pkl")

response, data = api.fetch_candles("GBP_USD", 3, "H1", "2008-02-21T10:30:00.00+01:00")

print(data)

candleArray = []

for eachDate in pure_df["RFC3339"]:
    response, data = api.fetch_candles("GBP_USD", 3, "H1", eachDate)
    if(response == 200):
        candleArray.append(data)
    else:
        print("FAILED OH NO")

pure_df["candle_data"] = candleArray

pure_df.to_pickle("pure_data.pkl")

print("success")