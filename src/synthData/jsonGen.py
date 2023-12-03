import sys
from tickerExtract import tickerListFinder
from dataGen import add_ticker_news
import json
import os
sys.path.append("./src")
from stockFeature import getStockFeature

def add_ticker(ticker):
    # Load the existing data
    with open(f'data/{ticker}.json', 'r') as f:
        data = json.load(f)
    
    # Add the news to the data
    data['TICKER'] = ticker

    # Write the data back to the file
    with open(f'data/{ticker}.json', 'w') as f:
        json.dump(data, f, indent=4)
    
def add_stockFeature(ticker):
    # Load the existing data
    with open(f'data/{ticker}.json', 'r') as f:
        data = json.load(f)
    
    # Add the news to the data
    data['stockFeature'] = getStockFeature(ticker)

    # Write the data back to the file
    with open(f'data/{ticker}.json', 'w') as f:
        json.dump(data, f, indent=4)

def main():
#    for i in range(1, 10):
    ticker_names = tickerListFinder(f'data/extended/JosephExtended1.csv')
    for (ticker,name) in ticker_names:
        # Data to be written to JSON
        
        # File path for the new JSON file
        file_path = f'data/{ticker}.json'

        # If file doesn't exist, create it
        if not os.path.exists(file_path):
            open(file_path, 'x')
            with open(f'{file_path}', 'w') as file:
                file.write('{}')
        
        #print(getStockFeature(ticker))
        # Writing data to the JSON file
        
        add_ticker(ticker)
        add_stockFeature(ticker)
        add_ticker_news(name, ticker)

        

if __name__ == "__main__":
    main()


