# Date and time follow slightly different conventions in Python then other
# places you've probably used them before.



# Get the current date and time and stick it in a variable called 'now.'


# That object containing year, month, day, hour, minute, second and
# millisecond is now frozen in that variable. Printing it will send a more
# readable string.



# We can isolate parts of the datetime object, too.




# It has a few built-in formats that might look familiar to you.



# You can also take the reins and output a string based on how you need it
# to be displayed: https://docs.python.org/2/library/time.html#time.strftime


# We can, of course, also make our own datetime object.




# This is especially useful when you're trying to gauge the difference
# between dates, something we frequently have to do in analysis. Let's do
# some simple math to see how may days until January 1, 2018.



# What gets returned by that math is a datetime.timedelta, and we can use
# that to add or subtract time, too. What is the date 219 days and two hours
# from now?


