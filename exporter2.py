import datetime, time, os
import re



def export(data_collection, table_title):
	# filename = re.sub(' ', '_', table_title) + '_inserts.sql'
	# outFile = open(filename, 'a')
	# for each_company in data_collection:
	# 	company_name, ticker, final_url, data = each_company
	# 	for date, value in data:
	# 		# value = "NULL" if value == "N/A" else value
	# 		newDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%b-%Y')
	# 		new_val = "NULL" if value == "N/A" else float(re.sub('%', '', value))/100
	# 		insert = "INSERT INTO {} VALUES ('{}', {});\n".format(ticker, newDate, new_val)
	# 		outFile.write(insert)
	# 	print(" ")
	# outFile.close()


	# for each_company in data_collection:
	# 	company_name, ticker, final_url, data = each_company
	# 	filename = re.sub(' ', '_', table_title) + ticker
	# 	outFile = open(filename, 'w')
	# 	for date, value in data:
	# 		newDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%b-%Y')
	# 		new_val = "NULL" if value == "N/A" else float(re.sub('%', '', value))/100
	# 		insert = "{}, {}\n".format(newDate, new_val)
	# 		outFile.write(insert)
	# 	outFile.close()

	for each_company in data_collection:
		company_name, ticker, final_url, data = each_company
		for date, value in data:
			# newDate = datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%b-%Y')
			# new_val = "NULL" if value == "N/A" else float(re.sub('%', '', value))/100
			# insert = "{}, {}\n".format(newDate, new_val)
			print(date, ": ", value)
