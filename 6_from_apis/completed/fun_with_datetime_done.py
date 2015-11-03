# Date and time follow slightly different conventions in Python then other
# places you've probably used them before.

import datetime

# Get the current date and time and stick it in a variable called 'now.'
now = datetime.datetime.now()

# That object containing year, month, day, hour, minute, second and
# millisecond is now frozen in that variable. Printing it will send a more
# readable string.
now
print now

# We can isolate parts of the datetime object, too.
print now.year
print now.hour
print now.day

# It has a few built-in formats that might look familiar to you.
print now.ctime()
print now.isoformat()

# You can also take the reins and output a string based on how you need it
# to be displayed: https://docs.python.org/2/library/time.html#time.strftime
print now.strftime('%m/%d/%y %I:%M%p')

# We can, of course, also make our own datetime object.
my_datetime = datetime.date(2014, 5, 7)
print my_datetime.isoformat()
print my_datetime.month

# This is especially useful when you're trying to gauge the difference
# between dates, something we frequently have to do in analysis. Let's do
# some simple math to see how may days until January 1, 2018.
diff = datetime.datetime(2018, 1, 1) - now
print diff.days

# What gets returned by that math is a datetime.timedelta, and we can use
# that to add or subtract time, too. What is the date 219 days and two hours
# from now?
the_future = now + datetime.timedelta(days=219, hours=2)
print the_future.ctime()
