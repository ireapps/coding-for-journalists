# SCRAPING DATA FROM A WEB PAGE
#
# PROBLEM: We want to scrape the contents of a table on a web page into a
# a delimited text file.
#
# HOW WE'RE GOING TO DEAL WITH IT:
#   - Use the requests library to grab the page source
#   - Use BeautifulSoup to navigate to the table and then loop through its rows
#   - Write it all to a CSV file
#   - Handle some (minor) encoding issues

# Let's import the libraries we'll be using for this parsing task: BeautifulSoup from bs4,
# Python's csv library and requests.





# The data table we want is at
# 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'


# Fetch the page with requests.


# Move the content of the page into a BeautifulSoup object that we can navigate.
# NOTE: BeautifulSoup also decodes the HTML to Unicode, and we'll deal with
# changing it back to a character encoding system below.


# We can check the original encoding of our page, too.


# This page only has one table, so it's not much work to find it.


# Let's make a new, empty CSV file and a csv.writer which will take write our
# table one row at a time to the file.



# The first row written will be our field names.


# We want to loop through all <tr> tags (rows) except for the header.


    # Each <tr> tag also has some <td> tags holding cell contents; these are
    # what we'll move into variables and then write to the CSV file.

    
    # Reactor name, detail page link and docket number are all part of the first cell.
    # Docket has a bunch of whitespace, so we'll .strip() it.




    
    # Two fields in this table (location and owner) have characters outside
    # of our fair ASCII realm; we need to make sure these are encoded into a
    # character system (and one that can handle them) on the way into our CSV.
    # We'll put them in UTF-8, the original encoding of our page.




    # Once everything's collected, write it as a row in the csv.


# Close the file and let us know it's finished.


# We'll also print a brief message to the console to let us know the script
# finished.

