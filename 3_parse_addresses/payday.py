# PROBLEM: We have a list of addresses with varying lengths tied up in an HTML page, but it's
# not in a table. Luckily they follow a pretty predictable format; we need to parse them into
# different columns and stick them in a delimited file.
# 
# HOW WE'RE GOING TO DEAL WITH IT: 
# 	- Use line breaks to split one big chunk of text into a list of separate addresses
# 	- Use flow control to loop through said list (a 'for' loop)
# 	- Use more flow control in the form of if/elif to send text from each item to the right spots
# 	- Write each list item to a row in a csv after we've tinkered with it
# 	- Mop up some other minor issues along the way


# Let's import the libraries we'll be using for this parsing task: BeautifulSoup from bs4 and
# Python's csv library.


# Open our HTML file in Python, then make a BeautifulSoup object out of it.


# Nothing we need is outside of the HTML <body>, which in this case is essentially formatted text
# without HTML tags and hooks we'd use to parse a table.
# Let's go ahead and pass it to a text variable, that way we can go to work on it with Python's
# string functions.

# There's an ugly horizontal rule and single line break at the very start; we don't want it there.


# Between each address, there are two line break tags. That'll be our split point.

# There's some cruft in our list; let's slice it out. Skip the first two items and the last item.


# Let's go ahead and make a new, empty csv file and get a csv.writer object queued up; it will take
# our work below and write it one row at a time to the file.


# First row in the csv will just be a comma-separated list of field names.


# Let's begin our 'for' loop here. 

	# Just like we used back-to-back <br/> tags to help us split up the text, we can use individual
	# tags to further subdivide the details for each lender. For each lender in the list, we're going
	# to break it apart and turn it into a new list in the details variable.

	# The lender name is always going to be the first thing in this new sub-list. We're also using
	# .strip() to get rid of any leading or trailing whitespace.

	# The number of items in this new sub-list can be three, four or five, with a twist; sometimes
	# it's four items because 'doing-business-as' info exists, sometimes it's because the street
	# address takes up two lines.
	# If there are three items in details, it has to be the name, the street address and the line
	# with city, state and zip info. We can safely pass an empty string to our placeholders for
	# 'doing-business-as' and a second address line.




	# If there are four items and the second starts with 'D/B/A,' parse accordingly. We're converting
	# it to UPPERCASE because this check is case sensitive.


	# If there is no 'D/B/A,' it must be because of a second street address line.




	# Five items in the list? This could also end with 'else,' meaning if it doesn't fit any of the
	# above criteria, just do this instead.




	# So let's deal with the last item in the details sub-list, a line of text that has city, state and 
	# zip separated by a comma and a single space. Regardless of how many lines the lender details is,
	# this will always come at the end, so grab it accordingly.

	# Broken apart, let's pass the pieces to a few variables.



	# Now that we've grabbed the lender name, figured out whether a 'D/B/A' line exists (as well as 
	# a second address line), and broken apart city, state and zip, let's go ahead and write this
	# line to our csv.


# We're done writing stuff to our csv. Let's close it to save all of our work.	


