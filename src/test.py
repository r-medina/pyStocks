ximport numpy as np
import datetime
import stock
import matplotlib.pyplot as plot

tickers =  "AAPL","SBUX","GRPN","EC","T","IBM","INTC","NFLX","GOOG","OSTK","CMG","TWX"
how_long = 90
time_between = "d"

ending = datetime.date.today()
time_span = datetime.timedelta(days=how_long)
starting = ending - time_span

s = ([])
j = 0
for ticker in tickers:
    s.append(stock.stock(ticker,starting,ending,time_between))
    print ticker + "\nNormalized Standard Deviation:\n"  + repr(100*s[j].std_dev/s[j].price_avg) + \
          "\nMaximum Return:\n" + repr(max(s[j].returns)*100) + \
          "\nLinear Deviation:\n" + repr(s[j].r_squared) + \
          "\nInitial Investment:\n" + repr(s[j].price_init) + "\n"
    j += 1

plot.show()

#stdev = list(stdev)
#which =  stdev.index(max(stdev))
#print s[which].ticker
#print stdev[which]
#print s[which].r_squared
#print s[1:2].r_squared
