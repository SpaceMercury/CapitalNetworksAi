import sys
from tickerExtract import tickerListFinder
from dataGen import add_ticker_news
import json
import os
sys.path.append("./src")
from stockFeature import getStockFeature



def main():
    for i in range(0, 10):
        ticker_names = tickerListFinder(f'data/synthetic/user{i}.csv')
        for (ticker,name) in ticker_names:
            # Data to be written to JSON
            print(ticker)
            print(name)
            
            # File path for the new JSON file
            file_path = f'data/{ticker}.json'

            # If file doesn't exist, create it
            if not os.path.exists(file_path):
                open(file_path, 'x')
                with open(f'{file_path}', 'w') as file:
                    file.write('{}')
            
            # Writing data to the JSON file
            ##getStockFeature(ticker)
            add_ticker_news(name, ticker)

        

if __name__ == "__main__":
    main()


