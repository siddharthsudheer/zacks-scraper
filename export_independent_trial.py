#!/usr/bin/env python3
import datetime, time, os
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell




    

def export(data_collection, table_title):
  workbook = xlsxwriter.Workbook(table_title + " Data.xlsx")
  worksheet = workbook.add_worksheet("RawData")
  resultsSheet = workbook.add_worksheet("Calculations")

  #General
  values_format = workbook.add_format({ 'valign':'vcenter', 'align': 'right'})
  otherHeaders = workbook.add_format({'bold': 1, 'font_size': 14, 'valign':'vcenter', 'align': 'right', 'font_name': 'Myriad Set Pro', 'bottom': 2})
  italic = workbook.add_format({'italic': 1, 'font_name': 'Myriad Set Pro'})
  blank_cell = workbook.add_format({'bg_color': '#f5f5f5'})
  worksheet.hide_gridlines(2)
  worksheet.set_column('A:A', 5)
  worksheet.set_row(0, 28)
  worksheet.set_row(1, 30)
  worksheet.set_column('C:ZZ', 10, values_format)

  resultsSheet.hide_gridlines(2)
  resultsSheet.set_column('A:A', 5)
  resultsSheet.set_row(0, 28)
  resultsSheet.set_row(1, 30)
  resultsSheet.set_column('C:ZZ', 10, values_format)



  #Date Column
  date_col = workbook.add_format({'num_format': 'MMM, YYYY', 'valign':'vcenter', 'align': 'left', 'font_name': 'Myriad Set Pro','right': 2})
  date_col_header = workbook.add_format({'bold': 1, 'font_size': 14, 'valign':'vcenter', 'font_name': 'Myriad Set Pro', 'right': 2, 'bottom': 2})
  worksheet.set_column('B:B', 30)
  worksheet.write('B2', 'Date', date_col_header)
  resultsSheet.set_column('B:B', 30)
  resultsSheet.write('B2', '=RawData!B2', date_col_header)


  #Results Stuff
  results_format = workbook.add_format({'bold': 1, 'italic': 1,'valign':'vcenter', 'align': 'right', 'font_name': 'Myriad Set Pro', 'top': 2})
  results_mid_rows = workbook.add_format({'bold': 1, 'italic': 1,'valign':'vcenter', 'align': 'right', 'font_name': 'Myriad Set Pro', 'num_format': '#.##0'})
  results_last_row = workbook.add_format({'bold': 1, 'italic': 1,'valign':'vcenter', 'align': 'right', 'font_name': 'Myriad Set Pro', 'num_format': '#.##0', 'bottom': 6})
  results_label_top = workbook.add_format({'bold': 1, 'italic': 1,'valign':'vcenter', 'align': 'left', 'font_name': 'Myriad Set Pro', 'top': 2,'right': 2})
  results_label_bottom = workbook.add_format({'bold': 1, 'italic': 1,'valign':'vcenter', 'align': 'left', 'font_name': 'Myriad Set Pro', 'bottom': 6,'right': 2})
  results_label_mid = workbook.add_format({'bold': 1, 'italic': 1,'valign':'vcenter', 'align': 'left', 'font_name': 'Myriad Set Pro','right': 2})
  
  def resultsCalcs(row, col):
      start_cell = xl_rowcol_to_cell(2, col + 2)
      end_cell = xl_rowcol_to_cell(row + 1, col + 2)
      cell_range = '(' + start_cell + ":" + end_cell + ')'

      num_obs_val = '=COUNTA' + cell_range
      num_obs_cell = xl_rowcol_to_cell(row + 2, col + 2)

      mean_val = '=SUM' + cell_range + '/' + num_obs_cell
      mean_cell = xl_rowcol_to_cell(row + 3, col + 2)

      std_dev_val = '=STDEV' + cell_range
      std_dev_cell = xl_rowcol_to_cell(row + 4, col + 2)

      std_err_val = '=' + std_dev_cell + '/SQRT(' +  std_dev_cell + ')'
      std_err_cell = xl_rowcol_to_cell(row + 5, col + 2)

      resultsSheet.write(num_obs_cell, num_obs_val, results_format)
      resultsSheet.write(mean_cell, mean_val, results_mid_rows)
      resultsSheet.write(std_dev_cell, std_dev_val, results_mid_rows)
      resultsSheet.write(std_err_cell, std_err_val, results_last_row)

      if col == 0: 
        resultsSheet.write(row + 2, 1, 'No. of Observations', results_label_top)
        resultsSheet.write(row + 3, 1, 'Mean', results_label_mid)
        resultsSheet.write(row + 4, 1, 'Std. Dev.', results_label_mid)
        resultsSheet.write(row + 5, 1, 'S.E.', results_label_bottom)

  # Keeping track of filled columns, so that,
  # the next ticker's values will be added to the
  # next empty column.
  worksheet_curr_col = 0
  


  for each_company in data_collection:
    company_name, ticker, final_url, data = each_company
    worksheet.write(1, worksheet_curr_col + 2, ticker, otherHeaders)
    cell = xl_rowcol_to_cell(1, worksheet_curr_col + 2)
    resultsSheet.write(1, worksheet_curr_col + 2, '=RawData!' + cell, otherHeaders)

    row = 0
    for date, value in data:
      date = datetime.datetime.strptime(date, "%m/%d/%Y")
      #getting dates only once
      if worksheet_curr_col == 0: 
        worksheet.write(row + 2, worksheet_curr_col + 1, date, date_col)
        cell = xl_rowcol_to_cell(row + 2, worksheet_curr_col + 1)
        resultsSheet.write(row + 2, worksheet_curr_col + 1, '=ABS(RawData!' + cell + ')', date_col)
        
      if value == "N/A": 
        worksheet.write(row + 2, worksheet_curr_col + 2, "", blank_cell)
        resultsSheet.write(row + 2, worksheet_curr_col + 2, "", blank_cell)
      else: 
        worksheet.write(row + 2, worksheet_curr_col + 2, value)
        cell = xl_rowcol_to_cell(row + 2, worksheet_curr_col + 2)
        resultsSheet.write(row + 2, worksheet_curr_col + 2, '=ABS(RawData!' + cell + ')')

      row += 1

    resultsCalcs(row, worksheet_curr_col)
    worksheet_curr_col +=1



    # Writing Meta Data
    # curr_time = time.time()
    # timestamp = datetime.datetime.fromtimestamp(curr_time).strftime('%b %d, %Y')
    # worksheet.write(row + 2, 0, "{}".format(company_name.replace(",", "") + ": " + table_title))
    # worksheet.write(row + 3, 0, final_url,italic)
    # worksheet.write(row + 4, 0, timestamp)

  print("{0}{1:20}{2}".format("==> ", table_title, " : Successfully scraped!\n"))
  workbook.close()


def main():
  data = [('Facebookkkk, Inc. (FB)', 'FB', 'https://www.zacks.com/stock/chart/FB/eps', [['12/31/2016', 'N/A'], ['09/30/2016', '2.8'], ['06/30/2016', '2.28'], ['03/31/2016', '1.82'], ['12/31/2015', '1.48'], ['09/30/2015', '1.21'], ['06/30/2015', '1.17'], ['03/31/2015', '1.17'], ['12/31/2014', '1.19'], ['09/30/2014', '1.07'], ['06/30/2014', '0.92'], ['03/31/2014', '0.75'], ['12/31/2013', '0.59'], ['09/30/2013', '0.48'], ['06/30/2013', '0.37'], ['03/31/2013', '0.16'], ['12/31/2012', '0.16'], ['09/30/2012', 'N/A'], ['06/30/2012', 'N/A'], ['03/31/2012', 'N/A']]), ('Yelp Inc. (YELP)', 'YELP', 'https://www.zacks.com/stock/chart/YELP/eps', [['12/31/2016', 'N/A'], ['09/30/2016', '-0.44'], ['06/30/2016', '-0.57'], ['03/31/2016', '-0.61'], ['12/31/2015', '-0.43'], ['09/30/2015', '-0.05'], ['06/30/2015', '0.1'], ['03/31/2015', '0.16'], ['12/31/2014', '0.14'], ['09/30/2014', '0.02'], ['06/30/2014', '-0.07'], ['03/31/2014', '-0.12'], ['12/31/2013', '-0.15'], ['09/30/2013', '-0.18'], ['06/30/2013', '-0.17'], ['03/31/2013', '-0.19'], ['12/31/2012', '-0.43'], ['09/30/2012', '-0.93'], ['06/30/2012', '-1.14'], ['03/31/2012', '-1.19']])]
  export(data, "EPS 12 MONTH TRIALS")

if __name__ == "__main__":
  main()
