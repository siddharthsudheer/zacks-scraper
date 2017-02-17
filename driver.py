#!/usr/bin/env python3
from get_fxns import *

def main():
	networkTickers = ['FB', 'YELP', 'TWTR', 'GRPN', 'EBAY', 'V', 'MA', 'PYPL','ETSY', 'WB']
	otherTickers = ['MSFT', 'AAPL', 'NFLX', 'TSLA', 'BAC', 'GE', 'PYPL']
	test = ['V', 'MA', 'PYPL','ETSY', 'WB']

	# get_eps_12months(otherTickers)
	# get_consensus_estimates(otherTickers)
	get_eps_surprise(test)
	# date = "02/14/2017"
	# newDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%b-%Y')
	# print(newDate)







if __name__ == "__main__":
	main()
