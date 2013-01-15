import matplotlib.mlab as mlab

from make_url import *
from download_stockdata import *

def fetch_stock(ticker,start_date,end_date,interval):
    """Takes a ticker, a start date, an end date, and an interval and
    returns a record array ("stock_data") with the stock data specified by
    the arguments
    """
    url = make_url(ticker,start_date,end_date,interval)
    file_name = download_stockdata(ticker,url)
    stock_data = mlab.csv2rec(file_name)
    return stock_data
