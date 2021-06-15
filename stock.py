from python_stock_search import stock_scraper
#
# #stock=[]
#update: cnbc has different xpaths (at least for some stocks)
#and i have yet again been ip banned so im going to discontinue this project for now
stock_string=input("enter your stock:")
#
# print(stock_string)
stock=stock_string.split()
# print(stock)
#
# #print(stock_scraper(stock))
# stock = "tsla ba"
#print(stock_string)
print(stock_scraper(stock))

#print(stock)
