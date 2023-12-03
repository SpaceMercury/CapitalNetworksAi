import pandas as pd
import requests
import json
import numpy as np

def findStockTickers(data_csv):
    df = pd.read_csv(data_csv)
    df = df['ISIN_CODE']
    original_tickers = df.unique()
    return original_tickers


def isin_to_ticker(isin):
    OpenFIGI_APIKEY="d3251d8b-e60a-4668-b071-a38176ce11d8"
    url = 'https://api.openfigi.com/v3/mapping'
    headers = {
        'Content-Type': 'application/json',
        'X-OPENFIGI-APIKEY': OpenFIGI_APIKEY
    }
    data = [
        {
            "idType": "ID_ISIN",
            "idValue": isin
        }
    ]
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        data = json.loads(response.text)
        if data and 'data' in data[0]:
            return data[0]['data'][0]['ticker']
    return None


def tickerListFinder(csv_path):
    isin = findStockTickers(csv_path)
    print(isin)
    arr = []
    for i in isin:
        arr.append(isin_to_ticker(i))
    return arr
    