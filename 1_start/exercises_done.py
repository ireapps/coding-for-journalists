# In ipython, typing the following will load the variables from 'var.py'
# into the interactive interpreter: %run var.py

# ----------------
# FUN WITH NUMBERS
# ----------------

# Print the contents of lucky_number
print lucky_number

# Subtract 18 from lucky_number and print it
print lucky_number - 18

# Add six to lucky_number and put it in a variable called unlucky_number
unlucky_number = lucky_number + 6

# Print unlucky_number
print unlucky_number

# Set lucky_number to lucky_number plus one; print lucky_number
lucky_number = lucky_number + 1
print lucky_number

# Check to see if lucky_number and unlucky_number are equal and print the result
print lucky_number == unlucky_number

# Check to see if lucky_number is less than unlucky_number and print the result
print lucky_number < unlucky_number

# Check unlucky_number's type
type(unlucky_number)

# Check the type of unlucky_number added to fuel_2015
type(unlucky_number + fuel_2015)


# ----------------
# FUN WITH STRINGS
# ----------------

# Print the contents of sentiment
print sentiment

# Print the length of sentiment
print len(sentiment)

# Print the length of lucky_number
print len(lucky_number)

# Try printing sentiment as all capital letters
print sentiment.upper()

# In a variable called new_sentiment, put sentiment in all caps again and replace
# 'moderately' with 'extremely'
new_sentiment = sentiment.upper().replace('MODERATELY','EXTREMELY')

# Print the result
print new_sentiment

# Print ugly_string, which has too many spaces
print ugly_string

# Try splitting that string apart (defaults to space)
ugly_string.split()

# Try splitting ugly_string on San
ugly_string.split('San')

# Join a series of words together with a space between each and print the result
print 'a'+' '+'series'+' '+'of'+' '+'words'

# Do the same thing but use Python's join function
print ' '.join(['a','series','of','words'])

# Split ugly_string apart again based on spaces, then join back together with
# a single space between the words; call it pretty_string
pretty_string = ' '.join(ugly_string.split())


# ---------------------------------
# FUN WITH LISTS (AND DICTIONARIES)
# ---------------------------------

# Print months
print months

# Print the length of months
print len(months)

# Add missing month to list of months; print months again
months.append('Dec')
print months

# Print the first item in the months list
print months[0]

# Print the third item in the months list
print months[2]

# Print the last item in the months list
print months[-1]

# Print the third through sixth items; print everything from seven onward
print months[2:6]
print months[6:]

# Print multi_list
print multi_list

# Print the second item in multi_list's last list
print multi_list[-1][1]

# Print person_info
print person_info

# Print the item linked to first_name in person_info
print person_info['first_name']

# Add Pennsylvania with a key of state to person_info; print the result
person_info['state'] = 'Pennsylvania'
print person_info

# Change city in person_info to Scranton; print the result
person_info['city'] = 'Scranton'
print person_info


# ---------------------
# FUN WITH FLOW CONTROL
# ---------------------

# Write a for loop that prints each month in the months list
for month in months:
	print month

# Get a list of the keys from the person_info dictionary
for key in person_info:
	print key

# Write a for loop that prints the key/value pair in our person_info dictionary
for key in person_info:
	print 'The key is '+key+' and the value is '+person_info[key]

# A for loop that gives a quick summary of each list in multi_list
for sublist in multi_list:
	print 'This list has',len(sublist),'items:'
	for item in sublist:
		print item
	print '\n'

# An if/else statement that checks the value in lucky_number
if lucky_number == 7:
	print 'Still seven!'
else:
	print 'Not seven anymore.'


# ------------------
# FUN WITH FUNCTIONS
# ------------------

# Define a basic function that prints the word 'beans'
def PrintBeans():
	print 'Beans'

# Define another basic function that multiplies a number by itself
def Square(number):
	print number * number

# Let's turn that list summary for loop from earlier into a function
def ListSummary(list):
	for sublist in list:
		print 'This list has',len(sublist),'items:'
		for item in sublist:
			print item
		print '\n'

# Append the months list to multi_list; run the ListSummary function on it
multi_list.append(months)
ListSummary(multi_list)