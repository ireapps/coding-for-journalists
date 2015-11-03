#!/usr/bin/env python

import csv
import re

orig_file_name = 'rahm_spending.csv'
read_file = open(orig_file_name, 'rb')
csv_reader = csv.reader(read_file)

headers = csv_reader.next()

# ['LASTONLYNAME', 'FIRSTNAME', 'EXPENDEDDATE', 'AMOUNT', 'ADDRESS1',
# 'ADDRESS2', 'CITY', 'STATE', 'ZIP', 'EXPTYPE', 'PURPOSE', 'BENEFICIARY']

# Let's just go ahead and write a function for this.


def cleaner(row):
    # Let's worry about the columns with problems.
    # LASTONLYNAME needs to be uppercase.
    lastonlyname = row[0].upper()
    # AMOUNT suffers from whitespace and dollar signs
    amount = float(row[3].replace('$', '').strip())
    # CITY contains some problematic spellings of 'Chicago'
    # and non-breaking spaces for display (&NBSP;)
    if row[6] in ['CHGO', 'CHCAGO']:
        city = 'CHICAGO'
    else:
        city = row[6].replace('&NBSP;', ' ')
    # ZIP has leading zeros removed
    if len(row[8]) == 4:
        zip = '0{}'.format(row[8])
    else:
        zip = row[8]
    # One thing with PURPOSE: there's additional detail after
    # a - or /. We can use regex to specify multiple split criteria.
    p_split = re.split('-|/', row[10])
    # Have to set an if/else up for if it doesn't have one of these.
    if len(p_split) > 1:
        main_purpose = p_split[0].strip()
        purpose_extra = p_split[1].strip()
    else:
        main_purpose = row[10]
        purpose_extra = ''
    # There are also synonymous words present: 'fee,' 'fees,'
    # 'cost,' 'costs,' 'expense.' Replacing this with 'expenses'
    # will go a long way toward cleaner categories.
    problem_words = ['FEE', 'FEES', 'COST', 'COSTS', 'EXPENSE']
    purpose_words = main_purpose.split()
    for word in purpose_words:
        if word in problem_words:
            loc = purpose_words.index(word)
            purpose_words.pop(loc)
            purpose_words.insert(loc, 'EXPENSES')
    main_purpose = ' '.join(purpose_words)
    # All done; let's return a revised row that contains our fixes and
    # rows we didn't touch.
    cleaned_row = [lastonlyname, row[1], row[2], amount, row[4], row[5], city, row[7], zip, row[9], main_purpose, purpose_extra, row[11]]
    return cleaned_row

# Our file is loaded and ready to go. We have a cleaning function. Let's fix the
# headers to match our file changes before we loose the function on the file.

headers.insert(headers.index('PURPOSE') + 1, 'DETAIL')

clean_file_name = 'rahm_spending_clean.csv'
with open(clean_file_name, 'wb') as write_file:
    csv_writer = csv.writer(write_file)
    csv_writer.writerow(headers)
    for row in csv_reader:
        # Here's where we can weed out non-expenditures from hitting our clean file.
        if row[9] == 'EXPENDITURE':
            csv_writer.writerow(cleaner(row))

print 'All done!'
read_file.close()
