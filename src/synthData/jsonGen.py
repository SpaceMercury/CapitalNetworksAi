import sys
from tickerExtract import tickerListFinder
from dataGen import add_ticker_news
import json
import os
sys.path.append("..")
from stockFeature import getStockFeature



def main():
    for i in range(0, 10):
        tickers = tickerListFinder(f'data/synthetic/user{i}.csv')
        
        for ticker in tickers:
            # Data to be written to JSON
            print(ticker)
            data = {}
            # File path for the new JSON file
            file_path = f'data/synthetic/{ticker}.json'

            # If file doesn't exist, create it
            if not os.path.exists(file_path):
                open(file_path, 'x')
            # Writing data to the JSON file
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
                add_ticker_news(ticker)

        

if __name__ == "__main__":
    main()


