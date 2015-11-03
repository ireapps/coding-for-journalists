# Regular expressions are a powerful tool for pattern matching when you
# know the general format of what you're trying to find but want to keep
# it loose in terms of actual content: think finding email addresses or
# phone numbers based on what they have in common with each other. Python
# has a standard library that deals with it.

import re

#

records = [
          'April 13, 2013 Cyberdyne Systems $4,000.00 18144 El Camino '
          'Real, Sunnyvale, CA 94087 (408) 555-1234 info@cyberdyne.com '
          'December 2, 2018 December 14, 2018',

          'May 4, 2013 Sam Fuzz, Inc. $6,850.50 939 Walnut St, San '
          'Carlos, CA 94070 (408) 555-0304 ceo@samfuzz.net January 28'
          ', 2016 February 15, 2016']

# Find the word 'Sunnyvale' in the first record with re.search()


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


# Do the same thing but wrap some parentheses around the month, day and year
# patterns and re.search().group(0) to return the whole date.



# Try 1, 2 and 3 to cycle through month, day and year.




# Grab all the dates in the first record with re.findall().


# Print them out with a for loop



# Pick out and print dollar amounts from the records.
# . matches any character, * matches any number of times




# Try to do the same thing for the phone numbers.




# How would I isolate something like a company name that's totally variable?
# Think about the hooks you have on either side; the pattern you want to
# match here has to do with what's around it.




# We can also substitute based on a pattern. Give everyone an '.info'
# email address via print and re.sub().



# If you have multiple character possibilities that act as delimiters for a
# string you want to break apart, re.split() can come in handy.



