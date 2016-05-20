# FUN WITH CSV FILES
#
# A common data format we know and love: delimited text files. Part of the
# standard library in Python deals specifically with CSVs (text files with Comma-Separated Values).
# This is just kind of modern shorthand for files with delimiters, and the
# csv library can deal with more than just commas.

# To gain access to csv, we need to import it for use in our script.



# Let's try writing some stuff to a file first. Open a file and get a
# writer object started that will actually transcribe the data to the file.
# The writer will sit in a variable called output; sometimes characterizing
# files as being read "in" or written "out" can help you keep them straight
# in your head in terms of a naming convention for variables.




# If you give a writer a list, it will turn it into a row in a CSV file for
# you. Let's Make a list with column headers and write it to the file:
#FIRSTNAME, LASTNAME, CITY.




# Based on the headers, write two more rows to the file.




# Close the file, otherwise the data may only be partially recorded. And by
# "otherwise," I mean definitely.



# So another thing we can do as far as opening a file, doing something with
# the contents and then closing it is using a slightly different syntax: with.
# Instead of having discrete steps for opening, reading/writing and closing a
# file like the example above, this automatically closes the file at the end
# of the indented code underneath. Not perfect for every situation, but it
# can be slightly more elegant sometimes.





