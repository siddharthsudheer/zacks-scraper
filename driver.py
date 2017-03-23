#!/usr/bin/env python3
from get_fxns import *

def main():
	networkTickers = ['FB', 'YELP', 'TWTR', 'GRPN', 'EBAY', 'V', 'MA', 'PYPL','ETSY', 'WB']
	otherTickers = ['ACGL', 'GALT', 'WMT', 'SPR', 'PXLW', 'PGRE', 'C', 'RIGL', 'CCI', 'QSII', 'MDLZ', 'GIS', 'BAC', 'CSCO', 'SYUT', 'BKS', 'BRKL', 'GPS', 'ANF', 'M', 'KR', 'DPS', 'PEP', 'BID','AEO', 'BEBE', 'RL', 'PVH', 'VFC', 'SWK', 'SNA', 'GE', 'MCD', 'TSLA', 'KO', 'PG', 'JNJ', 'MRK', 'JPM', 'MMM', 'UTX', 'HON', 'XOM', 'PM', 'RAI', 'CVX', 'BP', 'GM', 'COST','NKE', 'DIS', 'INTC', 'HD', 'LOW', 'DRYS']

	testTickers = ['FB']

	get_eps_12months(testTickers)
	# get_consensus_estimates(otherTickers)
	# get_eps_surprise(networkTickers)
	# date = "02/14/2017"
	# newDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%b-%Y')
	# print(newDate)







if __name__ == "__main__":
	main()
