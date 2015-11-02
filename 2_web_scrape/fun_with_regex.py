# Regular expressions are a powerful tool for pattern matching when you
# know the general format of what you're trying to find but want to keep
# it loose in terms of actual content: think finding email addresses or 
# phone numbers based on what they have in common with each other. Python
# has a standard library that deals with it.

import re

#

records = [
          'April 13, 2013 Cyberdyne Systems $4,000.00 18144 El Camino ' \
          'Real, Sunnyvale, CA 94087 (408) 555-1234 info@cyberdyne.com ' \
          'December 2, 2018 December 14, 2018',
          
          'May 4, 2013 Sam Fuzz, Inc. $6,850.50 939 Walnut St, San ' \
          'Carlos, CA 94070 (408) 555-0304 ceo@samfuzz.net January 28' \
          ', 2016 February 15, 2016']

# Find the word 'Sunnyvale' in the first record with re.search()
re.search('Sunnyvale', records[0]).group()

# Find the first date in the first record. Let's pick apart the pattern:
# 1. \w matches upper/lowercase A-Z and digits 0-9, good for text.
# 2. {3,} matches three or more (shortest possible month is May)
# 3. \s matches whitespace, good for spaces and tabs
# 4. {1} matches exactly one
# 5. \d matches 0-9
# 6. {1,2} matches at least one, but no more than 2
# 7. , matches the comma in the date
# 8. \s{1}: again, one space or tab
# 9. \d{4} matches four digits.
re.search('\w{3,}\s{1}\d{1,2},\s{1}\d{4}', records[0]).group()

# Do the same thing but wrap some parentheses around the month, day and year
# patterns and re.search().group(0) to return the whole date.
date_match = re.search('(\w{3,})\s{1}(\d{1,2}),\s{1}(\d{4})', records[0])
date_match.group(0)

# Try 1, 2 and 3 to cycle through month, day and year.
date_match.group(1)
date_match.group(2)
date_match.group(3)

# Grab all the dates in the first record with re.findall().
all_dates = re.findall('\w{3,}\s{1}\d{1,2},\s{1}\d{4}', records[0])

# Print them out with a for loop
for date in all_dates:
	print date
	
# Pick out and print dollar amounts from the records.
# . matches any character, * matches any number of times
for record in records:
	money_match = re.search('\$.*\.\d{2}', record)
	print money_match.group()

# Try to do the same thing for the phone numbers.
for record in records:
	ph_match = re.search('\(\d{3}\)\s\d{3}-\d{4}', record)
	print ph_match.group()

# How would I isolate something like a company name that's totally variable?
# Think about the hooks you have on either side; the pattern you want to
# match here has to do with what's around it.
for record in records:
	company_match = re.search('\d{4}\s(.+)\s\$', record)
	print company_match.group(1)
	
# We can also substitute based on a pattern. Give everyone an '.info'
# email address via print and re.sub().
for record in records:
	print re.sub('\.\w{3}', '.info', record)
	

	