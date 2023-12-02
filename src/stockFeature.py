import yfinance as yf 
from gnews import GNews

def getStockFeature(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info

def getStockNews(ticker, startDate, endDate):
    news = GNews(start_date=startDate, end_date=endDate)
    return news.get_news(ticker)

def main():
    ticker = "AAPL"
    #print(getStockNews(ticker, startDate=(2021,3,1), endDate=(2021,3,3)))
    print(yf.Ticker(ticker).info)

if __name__ == "__main__":
    main()
