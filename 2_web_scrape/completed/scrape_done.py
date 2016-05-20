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
import requests
from bs4 import BeautifulSoup
import csv

# The data table we want is at
# 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'
url = 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'

# Fetch the page with requests.
web_page = requests.get(url)

# Move the content of the page into a BeautifulSoup object that we can navigate.
# NOTE: BeautifulSoup also decodes the HTML to Unicode, and we'll deal with
# changing it back to a character encoding system below.
soup = BeautifulSoup(web_page.content, 'html.parser')

# We can check the original encoding of our page, too.
soup.original_encoding

# This page only has one table, so it's not much work to find it.
reactor_table = soup.find('table')

# Let's make a new, empty CSV file and a csv.writer which will take write our
# table one row at a time to the file.
csv_file = open('reactors.csv', 'wb')
output = csv.writer(csv_file)

# The first row written will be our field names.
output.writerow(['NAME', 'LINK', 'DOCKET', 'TYPE', 'LOCATION', 'OWNER', 'REGION'])

# We want to loop through all <tr> tags (rows) except for the header.
for row in reactor_table.find_all('tr')[1:]:

    # Each <tr> tag also has some <td> tags holding cell contents; these are
    # what we'll move into variables and then write to the CSV file.
    cell = row.find_all('td')
    
    # Reactor name, detail page link and docket number are all part of the first cell.
    # Docket has a bunch of whitespace, so we'll .strip() it.
    name = cell[0].contents[0].text
    link = cell[0].contents[0].get('href')
    docket = cell[0].contents[2].strip()
    type = cell[1].text
    
    # Two fields in this table (location and owner) have characters outside
    # of our fair ASCII realm; we need to make sure these are encoded into a
    # character system (and one that can handle them) on the way into our CSV.
    # We'll put them in UTF-8, the original encoding of our page.
    location = cell[2].text.encode('utf-8')
    owner = cell[3].text.strip().encode('utf-8')
    region = cell[4].text

    # Once everything's collected, write it as a row in the csv.
    output.writerow([name, link, docket, type, location, owner, region])

# Close the file and let us know it's finished.
csv_file.close()

# We'll also print a brief message to the console to let us know the script
# finished.
print 'All done!'
