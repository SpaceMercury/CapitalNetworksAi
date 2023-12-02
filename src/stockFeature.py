import yfinance as yf 
from utils import isin_to_ticker
from gnews import GNews
from datetime import datetime

def getStockFeature(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        if info:
            return info
        else:
            print("Stock Info not found")
            return None
    except Exception as e:
        print(f"An error occurred while fetching info for {ticker}: {e}")
        return None

def getStockNews(ticker, startDate, endDate):
    news = GNews(start_date=startDate, end_date=endDate)
    return news.get_news(ticker)

def appendStockFeature(row):
    if row['ISIN_CODE'] == "nan":
        print("ISIN not found")
        return None
    ticker = isin_to_ticker(row['ISIN_CODE'])
    if ticker == None:
        print("Ticker not found")
        return None

    print(f"Prev Row : \ {row}")
    #date = row['DATE_TRANSACTION']  # assuming 'StartDate' is a column in your DataFrame
    #startDate = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    stockFeature = getStockFeature(ticker)
    if stockFeature == None:
        return None
    # Add each element of stockFeature and stockNews to the row
    for key, value in stockFeature.items():
        row[f'StockFeature_{key}'] = value
    print(row)
    return row

def main():
    ticker = "AAPL"
    print(getStockNews(ticker, startDate=(2021,3,1), endDate=(2021,3,3)))
    #print(yf.Ticker(ticker).info)

if __name__ == "__main__":
    main()
