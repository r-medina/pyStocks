import urllib

def download_stockdata(ticker,url):
    """Takes the name of the ticker and the url made by make_url and
    downloads a csv with the stock data and returns the name of the csv
    """
    # csv is saved in ../data/
    file_name = str("../data/" + ticker + ".csv")
    urllib.urlretrieve(url, file_name)
    return file_name
