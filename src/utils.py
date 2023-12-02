import yfinance as yf
import requests

def ticker_to_isin(ticker):
        return yf.Ticker(ticker).isin

def isin_to_ticker(isin):
        OpenFIGI_APIKEY="d3251d8b-e60a-4668-b071-a38176ce11d8"
        url = 'https://api.openfigi.com/v3/mapping'
        headers = {'Content-Type':'application/json', 'X-OPENFIGI-APIKEY': OpenFIGI_APIKEY}
        payload = '[{"idType":"ID_ISIN","idValue":"' + isin + '","exchCode":"US"}]'

        return requests.post(url, headers=headers, data=payload)

def main():
    ticker = "AAPL"
    print(isin_to_ticker(ticker_to_isin(ticker)))
