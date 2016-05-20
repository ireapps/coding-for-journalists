# ----------------
# BASIC DATA TYPES
# ----------------

# Print your name in the interpreter.
print 'Jane Smith'

# Print an integer.
print 8

# Print a basic math equation.
print 2 + 2

# Define a string called my_string and wrap it in single quotes.
my_string = 'This is a string.'

# Define another string called my_other_string and wrap it in double quotes.
my_other_string = "This is also a string."

# Define an integer (whole number) and call it my_integer.
my_integer = 14

# Define a float (number that contains a fraction of one) called my_float.
my_float = 5.45

# Define a boolean value (True/False) called my_boolean.
my_boolean = True

# Print my_string.
print my_string

# Print my_string and my_other_string together using a plus (+) to
# concatenate.
print my_string + my_other_string

# Let's get a space in there.
print my_string + ' ' + my_other_string

# Print my_integer divided by 3.
print my_integer / 3

# If we don't define one of these as a float, Python 2.7 lops off extra.
# digits. Try it again with the 3 as a float.
print my_integer / float(3)

# Check the data types of some of what we defined above.
print type(my_integer)
print type(my_string)
print type(my_boolean)

# Print the result of checking whether my_boolean is True and is not True.
print my_boolean is True
print my_boolean is not True


# In iPython, typing the following will load the variables from 'var.py'
# into the interactive interpreter: %run var.py
# We can also type: from var import *

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
new_sentiment = sentiment.upper().replace('MODERATELY', 'EXTREMELY')

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
print ' '.join(['a', 'series', 'of', 'words'])

# Split ugly_string apart again based on spaces, then join back together with
# a single space between the words; call it pretty_string
pretty_string = ' '.join(ugly_string.split())

# Print the string 'apple ' three times
print 'apple ' * 3


# -----
# LISTS
# -----

# Define a list called my_list that contains three strings: Tomato, Celery
# and Carrot
my_list = ['Tomato', 'Celery', 'Carrot']

# Print the list
print my_list

# Print the first item in the list
print my_list[0]

# Print the second item in the list
print my_list[1]

# Add 'Potato' to my_list
my_list.append('Potato')

# Print the contents of my_list again
print my_list

# ------------
# DICTIONARIES
# ------------

# Make a simple dictionary of four items called my_dict:
# class: Python, location: New York, time: 9am, attendance: 20

my_dict = {'class': 'Python', 'location': 'New York', 'time': '9am', 'attendance': 20}

# Print my_dict.
print my_dict

# Print the value for location.
print my_dict['location']

# Print the keys in my_dict.
print my_dict.keys()

# Print the values in my_dict.
print my_dict.values()

# Check to see if a key 'month' exists in my_dict
print 'month' in my_dict


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
# FUN WITH CONTROL FLOW
# ---------------------

# Write a for loop that prints each month in the months list
for month in months:
    print month

# Get a list of the keys from the person_info dictionary
for key in person_info:
    print key

# Write a for loop that prints the key/value pair in our person_info
# dictionary. We can also use commas in a similar fashion as plus above.
for key in person_info:
    print 'The key is', key, 'and the value is', person_info[key]

# A for loop that gives a quick summary of each list in multi_list
for sublist in multi_list:
    print 'This list has', len(sublist), 'items:'
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


def print_beans():
    print 'Beans!'

# Run the PrintBeans() function.
print_beans()

# Define another basic function that multiplies a number by itself


def square(number):
    return number * number

# Find the square of 27.
square(27)

# Put the square of 47 into a new variable.
square_result = square(47)

# Try finding the square of 'apple.'
square('apple')

# Let's turn that list summary for loop from earlier into a function


def list_summary(list):
    for sublist in list:
        print 'This list has', len(sublist), 'items:'
        for item in sublist:
            print item
        print ''

# Append the months list to multi_list; run the ListSummary function on it
multi_list.append(months)
ListSummary(multi_list)
