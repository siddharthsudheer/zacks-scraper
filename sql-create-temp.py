#!/usr/bin/env python3

def main():
	type = ['station_info_', 'station_status_', 'trip_info_']
	dates = ['2014','2015','2016']

	for i in type:
		for d in dates:
			desc = "\d {}{};".format(i,d)
			statement = "SELECT count(*) from {}{};".format(i,d)
			print(desc)
			print(statement)
		print(" ")


if __name__ == "__main__":
	main()
