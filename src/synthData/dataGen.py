from gnews import GNews

def getStockNews(ticker):
    news = GNews(language='en', max_results=4)
    return news.get_news(ticker)

def main():
    ticker = "AAPL"
    news = getStockNews(ticker)
    print (news)

if __name__ == "__main__":
    main()