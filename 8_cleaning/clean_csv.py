#!/usr/bin/env python










# ['LASTONLYNAME', 'FIRSTNAME', 'EXPENDEDDATE', 'AMOUNT', 'ADDRESS1',
# 'ADDRESS2', 'CITY', 'STATE', 'ZIP', 'EXPTYPE', 'PURPOSE', 'BENEFICIARY']

# Let's just go ahead and write a function for this.



    # Let's worry about the columns with problems.
    # LASTONLYNAME needs to be uppercase.

    # AMOUNT suffers from whitespace and dollar signs

    # CITY contains some problematic spellings of 'Chicago'
    # and non-breaking spaces for display (&NBSP;)




    # ZIP has leading zeros removed




    # One thing with PURPOSE: there's additional detail after
    # a - or /. We can use regex to specify multiple split criteria.

    # Have to set an if/else up for if it doesn't have one of these.






    # There are also synonymous words present: 'fee,' 'fees,'
    # 'cost,' 'costs,' 'expense.' Replacing this with 'expenses'
    # will go a long way toward cleaner categories.








    # All done; let's return a revised row that contains our fixes and
    # rows we didn't touch.



# Our file is loaded and ready to go. We have a cleaning function. Let's fix the
# headers to match our file changes before we loose the function on the file.








        # Here's where we can weed out non-expenditures from hitting our clean file.





