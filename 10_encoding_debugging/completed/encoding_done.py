#!/usr/bin/env

# If you're running into problems with encoding, your code probably mixes
# strings, which are stored in bytes, and unicode, which is stored in code
# points.
#
# If you get the dreaded UnicodeDecodeError, follow these steps.
#
# 1. DECODE EARLY
# 2. DO YOUR STUFF
# 3. ENCODE LATE

# Open an file and read the lines into a variable. This file uses Windows
# encoding: cp1252
with open('some_text.txt', 'rb') as infile:
	new_text = infile.readlines()

# Print a unicode string and the lines from the file we read in, which
# will break because we're putting a string from the file with unicode.
# Easy fix: decode each line and print.	
for line in new_text:
	prefix = u"This is a line: "
	print prefix + line.decode('cp1252')

# Save decoded strings to a new list.
decoded_text = []
for line in new_text:
	decoded_text.append(line.decode('cp1252'))

# This will come out as garbage unless we encode.
with open('output_text.txt', 'wb') as outfile:
	for line in decoded_text:
		outfile.write(line.encode('utf8'))
