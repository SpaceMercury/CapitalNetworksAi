from gnews import GNews
import json

def getStockNews(ticker):
    news = GNews(language='en', max_results=4)
    return news.get_news(ticker)

def cleanNews(news):
    for article in news:
        article.pop('publisher')
        article.pop('url')      

def add_ticker_news(ticker):

    news = getStockNews(ticker)
    cleanNews(news)

    # Load the existing data
    with open(f'data/{ticker}.json', 'r') as f:
        data = json.load(f)

    # Add the news to the data
    data['news'] = news

    # Write the data back to the file
    with open(f'data/{ticker}.json', 'w') as f:
        json.dump(data, f, indent=4)