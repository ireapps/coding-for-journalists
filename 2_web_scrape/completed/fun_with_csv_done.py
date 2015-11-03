# A common data format we know and love: delimited text files. Part of the
# standard library deals with CSVs (text files with Comma-Separated Values).
# This is just kind of modern shorthand for files with delimiters, and the
# csv library can deal with more than just commas.

import csv

# Let's try writing some stuff to a file first. Open a file and get a
# writer object started that will actually transcribe the data to the file.

outfile = open('my_test.csv', 'wb')
csv_writer = csv.writer(outfile)

# Make a list with column headers and write it to the file: FIRSTNAME,
# LASTNAME, CITY.

headers = ['FIRSTNAME', 'LASTNAME', 'CITY']
csv_writer.writerow(headers)

# Based on the headers, write two more rows to the file.

csv_writer.writerow(['Alex', 'Richards', 'Chicago'])
csv_writer.writerow(['John', 'Smith', 'New York'])

# Close the file, otherwise the data may only be partially recorded. And by
# "otherwise," I mean definitely.

outfile.close()

# So another thing we can do as far as opening a file, doing something with
# the contents and then closing it is using a slightly different syntax: with.

with open('my_test.csv', 'rb') as infile:
    csv_reader = csv.reader(infile)
    for row in csv_reader:
        print row

# With the file open, do some stuff, and then the file will close
# automatically when the code inside the with statement is concluded. Not
# perfect for every situation, but it can be slightly more elegant sometimes.
