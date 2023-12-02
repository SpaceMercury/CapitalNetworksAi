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
    # To print the response
    return response.json()[0]['data'][0]['ticker']

#def main():
#    ticker = "AAPL"
#    print(isin_to_ticker(ticker_to_isin(ticker)))
#
#if __name__ == "__main__":
#    main()



