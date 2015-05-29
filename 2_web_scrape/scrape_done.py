# PROBLEM: We want to scrape the contents of a table into a delimited file.
#
# HOW WE'RE GOING TO DEAL WITH IT:
#   - Use the requests library to grab the page source
#   - Use BeautifulSoup to navigate to the table and then loop through its rows
#   - Write it all to a csv file
#   - Handle some encoding issues

# Let's import the libraries we'll be using for this parsing task: BeautifulSoup from bs4,
# Python's csv library and requests
import requests
from bs4 import BeautifulSoup
import csv

# The data table we want is at
# 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'
url = 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'

# Fetch the page with requests, set the page encoding and turn it into a BeautifulSoup
# object.
web_page = requests.get(url)
web_page.encoding = 'UTF-8'
soup = BeautifulSoup(web_page.text)

# This page only has one table, so it's not much work to find it.
reactor_table = soup.find('table')

# Let's make a new, empty csv file and a csv.writer which will take write our
# table one row at a time to the file.
csv_file = open('reactors.csv', 'wb')
output = csv.writer(csv_file)
# The first row written will be our field names.
output.writerow(['NAME', 'LINK', 'DOCKET', 'TYPE', 'LOCATION', 'OWNER', 'REGION'])

# We want to loop through all <tr> tags (rows) except for the header.
for row in reactor_table.find_all('tr')[1:]:
    # Each <tr> has some <td> (cells) below it; these are what we'll move into variables
    # and then write to the csv.
    cell = row.find_all('td')
    # Reactor name, detail page link and docket number are all part of the first cell.
    # Docket has a bunch of whitespace, so we'll .strip() it.
    name = cell[0].contents[0].string
    link = cell[0].contents[0].get('href')
    docket = cell[0].contents[2].strip()
    type = cell[1].string
    # Two fields in this table have characters like en dash; we need to make sure these are
    # encoded properly when writing to the csv or it will break our script.
    location = cell[2].string.encode('utf8')
    owner = cell[3].contents[0].encode('utf8')
    region = cell[4].string

    # Once everything's collected, write it as a row in the csv.
    output.writerow([name, link, docket, type, location, owner, region])

# Close the file and let us know it's finished.
csv_file.close()
print 'All done!'
