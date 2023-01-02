import requests
import pandas as pd
import defs

class OandaAPI():

    def __init__(self):
        self.session = requests.Session()

    def fetch_candles(self, pair_name, count, granularity, date_from):
        url = f"{defs.OANDA_URL}/instruments/{pair_name}/candles"
        
        params = dict(
        count = count,
        granularity = granularity,
        )

        params['from'] = date_from

        response = self.session.get(url, params=params, headers=defs.SECURE_HEADER)
        return response.status_code, response.json()

if __name__ == "__main__":
    api = OandaAPI()
    api.save_instruments()