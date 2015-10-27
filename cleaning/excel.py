#! usr/bin/python

from openpyxl import load_workbook
import csv

# Load our Excel workbook into memory
loc = '/Users/alexrichards/Downloads/datacleaninginexcel/Candidates.xlsx'
wb = load_workbook(filename = loc)

# List the sheets we find in the workbook
for sheet in wb.sheetnames:
	print sheet

# Active sheet will default to the first; we can also select it
ws = wb.get_sheet_by_name('Sheet1')

# This library can also generate Excel workbooks in memory

# We can iterate through rows an do things based on the pattern that
# we find. 

race_holder = ''

for ws_row in ws.iter_rows():
	if ws_row[0].value == "Candidate's Name":
		cell_above = ws_row[0].column + str(ws_row[0].row - 1)
		race_holder = ws[cell_above].value
	elif ws_row[0].value != None and ws_row[1].value != None:
		row_below = ws_row[0].row + 1
		cand_name = ws_row[0].value
		st_addr = ws_row[1].value
		phone = ws_row[3].value
		filed_date = ws_row[4].value
		city_st_zip = ws['B'+str(row_below)].value
		email = ws['C'+str(row_below)].value
		print ','.join([str(cand_name), str(st_addr), str(city_st_zip), str(phone), str(email), str(filed_date)])
