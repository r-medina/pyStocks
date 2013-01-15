def make_url(ticker,start_date,end_date,interval):
    """Formats a string to be the proper url for yahoo to return the
    exact data the program is specifying
    """
    url = str()
    url = 'http://ichart.finance.yahoo.com/table.csv?s=' + \
          ticker + '&a=' + repr(start_date.month) + '&b=' + \
          repr(start_date.day) + '&c=' + repr(start_date.year) + \
          '&d=' + repr(end_date.month) + '&e=' + repr(end_date.day) + \
          '&f=' + repr(end_date.year) + '&g=' + interval + \
          '&ignore=.csv'
    return url
