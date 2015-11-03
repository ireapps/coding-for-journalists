#! usr/bin/python




# We're going to be messing with an existing file, so let's clone our Excel
# file just to be on the safe side.



# Load our Excel workbook into memory



# List the sheets we find in the workbook



# Active sheet will default to the first; we can also select it


# We can iterate through rows an do things based on the pattern that
# we find. First, though, we need to decide where to put the data.
# Why not another blank sheet in the same book?



# Right now there's nothing on the sheet; the max row and column would be '1'



# Max_row can help us keep track of where we are as we write to the book.
# Let's start by writing a header for all the information we're going to
# collect.





# This is our first modification to the workbook; let's save our changes.


# We need something outside the loop to hold onto the race name



# Let's walk through each row in our sheet with .rows

    # Headers are duplicated for each race in this sheet; we can grab the
    # race name in the cell directly above and hold onto it IF we encounter
    # that first header item, "Candidate's Name."



    # The other condition to hunt for: Candidate info is spread out over two
    # rows. If there's something in the first and second columns, that means
    # it's a candidate, and we can go to work on that row and the row below it.







        # Let's break apart the combined city, state and zip





        # Let's write the row to Sheet2, which we've already queued up. Watch
        # out for the date, which we'll reformat from a Python date object.





# Save changes to the file.

