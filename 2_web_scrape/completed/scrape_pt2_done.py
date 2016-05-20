# SCRAPING DATA FROM MORE THAN ONE WEB PAGE
#
# PROBLEM: We scraped our table, but there are a few key pieces of information
# sitting on each reactor's detail page that we want to include in our
# analysis.
#
# HOW WE'RE GOING TO DEAL WITH IT:
#   - Do everything we did before: fetch a page, navigate to the main table
#     and output those details to a CSV
#   - Refine our script so that it dips into the detail page for each reactor
#   - Target the location of these new data with BeautifulSoup
#   - Write a function that will extract them for us.

# Let's add Python's time library, which we can use to slow down the speed of
# our requests to this government website.
import requests
from bs4 import BeautifulSoup
import csv
import time

# We'll write our function here. It will take two arguments: A list and a
# value to find. When it finds a match, it will return the item it matched on.
# We'll also have it only return the part after the colon (:).


def finder(a_list, some_value):
    for item in a_list:
        if some_value.upper() in item.upper():
            return item.split(':')[1].strip()

url = 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'

web_page = requests.get(url)
soup = BeautifulSoup(web_page.content, 'html.parser')

reactor_table = soup.find('table')

# First change: We'll send our results to a different file.
csv_file = open('reactors_more.csv', 'wb')
output = csv.writer(csv_file)

# We'll also Add the two new fields we'll be grabbing from the detail page to
# the header row.
output.writerow(['NAME', 'LINK', 'DOCKET', 'TYPE', 'LOCATION', 'OWNER', 'REGION', 'MWT', 'CONTAINMENT'])

for row in reactor_table.find_all('tr')[1:]:
    cell = row.find_all('td')
    name = cell[0].contents[0].text
    link = cell[0].contents[0].get('href')
    docket = cell[0].contents[2].strip()
    type = cell[1].text
    location = cell[2].text.encode('utf-8')
    owner = cell[3].text.strip().encode('utf-8')
    region = cell[4].text

    # Let's get the reactor's detail page and have a short note printed for us
    # to see about the status.
    print 'Fetching details for {}...'.format(name)
    detail_page = requests.get('http://www.nrc.gov'+link)

    # We'll make a new BeautifulSoup object out of the page, just like we did
    # for the main one.
    detail_soup = BeautifulSoup(detail_page.content, 'html.parser')

    # We need to isolate the section of HTML where our data are. There's one
    # two-cell table in the whole page - the first cell holds a reactor photo,
    # the second holds the details we want to add.
    new_data = detail_soup.find_all('td')[1]

    # We're going to boil this down to just the text and then turn it into a
    # list based on line breaks.
    data_list = new_data.text.split('\n')

    # Let's hop up to the start of our script to write a function that will
    # search this data. We can then call it up to grab the wattage and
    # containment type for these reactors.
    mwt = finder(data_list, 'licensed mwt')
    containment = finder(data_list, 'containment')

    # Add these two new fields to the output written to the CSV file.
    output.writerow([name, link, docket, type, location, owner, region, mwt, containment])

    # Let's slow down how quickly we send requests for detail pages.
    time.sleep(2)

csv_file.close()
print 'All done!'
