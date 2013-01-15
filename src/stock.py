import numpy as np
from scipy import stats
import matplotlib.pyplot as plot
import matplotlib.ticker as mpl_ticker
import matplotlib.dates as dates

from fetch_stock import *

class stock:
    '''Makes a stock object'''
    def __init__(self,ticker,start_date,end_date,interval):
        self.ticker = ticker
        # Creates a record array with "date, open, high, low, close,
        # volume, adj_close" fields for data that it downloads about
        # the tickers passed
        self.stock_data = fetch_stock(ticker,start_date,end_date,interval)
        self.price = self.stock_data.adj_close
        self.price_init = min(self.price)
        self.price_avg = np.mean(self.price)
        self.returns = (self.price-self.price_init)/self.price_init
        self.std_dev = np.std(self.price)
        ind = np.arange(self.stock_data.date.shape[0])[::-1]
        slope, intercept, r_value, p_value, std_err = \
               stats.linregress(ind,self.price)
        self.r_squared = r_value**2
        
        self.graph = plot.figure()
        stock_graph = self.graph.add_subplot(111)
        stock_graph.plot(self.stock_data.date,self.price)
        
        plot.title(ticker)
        
        stock_graph.xaxis.set_major_locator(dates.MonthLocator())
        stock_graph.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=5))
        
        stock_graph.xaxis.set_major_formatter(mpl_ticker.NullFormatter())
        stock_graph.xaxis.set_minor_formatter(dates.DateFormatter('%b'))

        for tick in stock_graph.xaxis.get_minor_ticks():
            tick.tick1line.set_markersize(0)
            tick.tick2line.set_markersize(0)
            tick.label1.set_horizontalalignment('center')

        # Sets axis for the graphs: x axis = (min(price),max(price)) ...
        plot.axis([min(self.stock_data.date),max(self.stock_data.date),self.price_init,max(self.price)])
        
        imid = len(self.stock_data.date)/2
        stock_graph.set_xlabel(str(self.stock_data.date[imid].year))
                
