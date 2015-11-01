# A common 

import csv

outfile = open('my_test.csv', 'wb')
csv_writer = csv.writer(outfile)

headers = ['FIRSTNAME', 'LASTNAME', 'CITY']

csv_writer.writerow(headers)

csv_writer.writerow(['Alex', 'Richards', 'Chicago'])
csv_writer.writerow(['John', 'Smith', 'New York'])

outfile.close()

with open('my_test.csv', 'rb') as infile:
	csv_reader = csv.reader(infile)
	for row in csv_reader:
		print row
		
