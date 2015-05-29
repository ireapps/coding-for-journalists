# PROBLEM: We want to scrape the contents of a table into a delimited file.
#
# HOW WE'RE GOING TO DEAL WITH IT:
#   - Use the requests library to grab the page source
#   - Use BeautifulSoup to navigate to the table and then loop through its rows
#   - Write it all to a csv file
#   - Handle some encoding issues

# Let's import the libraries we'll be using for this parsing task: BeautifulSoup from bs4,
# Python's csv library and requests




# The data table we want is at
# 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'


# Fetch the page with requests, set the page encoding and turn it into a BeautifulSoup
# object.




# This page only has one table, so it's not much work to find it.


# Let's make a new, empty csv file and a csv.writer which will take write our
# table one row at a time to the file.


# The first row written will be our field names.


# We want to loop through all <tr> tags (rows) except for the header.

    # Each <tr> has some <td> (cells) below it; these are what we'll move into variables
    # and then write to the csv.

    # Reactor name, detail page link and docket number are all part of the first cell.
    # Docket has a bunch of whitespace, so we'll .strip() it.




    # Two fields in this table have characters like en dash; we need to make sure these are
    # encoded properly when writing to the csv or it will break our script.




    # Once everything's collected, write it as a row in the csv.


# Close the file and let us know it's finished.
