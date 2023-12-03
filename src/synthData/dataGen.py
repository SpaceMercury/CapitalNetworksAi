from gnews import GNews
import json

def getStockNews(name):
    news = GNews(language='en', max_results=4)
    return news.get_news(name)

def cleanNews(news):
    for article in news:
        article.pop('publisher')
        article.pop('url')      

def add_ticker_news(name, ticker):

    news = getStockNews(name)
    cleanNews(news)
    print(news)

    # Load the existing data
    with open(f'data/{ticker}.json', 'r') as f:

        data = json.load(f)
    
    # If the data is empty, put nothing in it
    if data == None:
        data = news
    else:
        # Add the news to the data
        data['news'] = news

    # Write the data back to the file
    with open(f'data/{ticker}.json', 'w') as f:
        json.dump(data, f, indent=4)

def main():
    add_ticker_news('DSD')

if __name__ == "__main__":
    main()