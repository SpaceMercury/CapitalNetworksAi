import pandas as pd
import requests
import json
import numpy as np

def findStockTickers(data_csv):
    df = pd.read_csv(data_csv)
    df = df[['StockFeature_underlyingSymbol', 'NAME']]
    #get unique elements of df stock tickers
    original_tickers = df['StockFeature_underlyingSymbol'].unique()

    #get unique elements of df stock names from tickers
    original_names = df['NAME'].unique()

    return original_tickers, original_names

def tickerListFinder(csv_path):
    arr = findStockTickers(csv_path)
    tuple_list = []
    for i in range(0, len(arr[0])):
        tuple_list.append((arr[0][i], arr[1][i]))
    return tuple_list


def main():
    ticker_names = tickerListFinder('data/synthetic/user0.csv')


if __name__ == "__main__":
    main()