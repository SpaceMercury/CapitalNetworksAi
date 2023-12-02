import yfinance as yf
import requests
import json

def ticker_to_isin(ticker):
        return yf.Ticker(ticker).isin

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

def main():
    ticker = "AAPL"
    isin="US17275R1023"
    print(isin_to_ticker(isin))

    print(isin_to_ticker(ticker_to_isin(ticker)))

if __name__ == "__main__":
    main()



