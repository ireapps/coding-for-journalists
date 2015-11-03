#!/usr/bin/env python

# For more information about this particular API, Socrata, the vendor Chicago
# uses for many of its publicly-facing data sources, has excellent
# documentation to read:
# http://dev.socrata.com/foundry/#/data.cityofchicago.org/6zsd-86xi







# Let's write a function that check the date of the most recent crime in the JSON and
# returns it. We'll have it convert the date it finds into a datetime object Python
# can do some math on.









# We're going to have to convert dates back and forth between strings a bit. Better to
# just go ahead and whip up a short function for it.





# Let's write another designed to grab the most recent week of crime from Chicago's API.
# We'll set it up so it can take the date from our date_check function.









# With those three functions in place, one short line of code will toss the most recent
# week's worth of crimes into a variable for us.


# Let's do some quick checks in the interpreter to see what our data looks like:
            # return the first record
            # see how many records we received

# Are all the records we're getting back the same length? This will be important when we
# kick the result over to a database.



                      # set is a data type that only holds uniques

# Let's see what one of these shorter crime records looks like.





# Open a connection to a SQLite database and create a cursor we'll use to interact with
# said database. (If one doesn't exist, it'll be created on the spot.)




# We want to make a table, so let's get a list of fields that need to be in there. We
# won't put "location" in, because it's redundant (we already have latitude and longitude,
# not to mention Illinois state plane coordinates in feet).










# Let's write a quick function to figure out if the table already exists in our database
# or not. If we query a table that doesn't exist, we'll get an error; let's use that to
# our advantage.










# Start if


    # So now we have to write a SQL statement that will insert values into the right fields,
    # regardless of how long the field is. To make this happen, we're also going to need to
    # deal with some dict order weirdness by specifying fields for our inserted values.







        # SQL format: INSERT INTO <table> (<col1>, <col2>, ...) VALUES ('<val1>', '<val2>', ...)





# Some basic queries based on the data.

# A function to assess the week's crimes.















# And a function to format the result of high_crime_areas!









# This could be set up to run some quick summaries as soon as the data is processed by
# the script.





# Violent crime rates in each Chicago community for the most recent week of data available






















