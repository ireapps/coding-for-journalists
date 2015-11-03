# A common data format we know and love: delimited text files. Part of the
# standard library deals with CSVs (text files with Comma-Separated Values).
# This is just kind of modern shorthand for files with delimiters, and the
# csv library can deal with more than just commas.



# Let's try writing some stuff to a file first. Open a file and get a
# writer object started that will actually transcribe the data to the file.




# Make a list with column headers and write it to the file: FIRSTNAME,
# LASTNAME, CITY.




# Based on the headers, write two more rows to the file.




# Close the file, otherwise the data may only be partially recorded. And by
# "otherwise," I mean definitely.



# So another thing we can do as far as opening a file, doing something with
# the contents and then closing it is using a slightly different syntax: with.






# With the file open, do some stuff, and then the file will close
# automatically when the code inside the with statement is concluded. Not
# perfect for every situation, but it can be slightly more elegant sometimes.
