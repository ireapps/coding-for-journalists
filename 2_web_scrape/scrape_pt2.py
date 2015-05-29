# PROBLEM: We scraped our table, but there's actually information on the detail page
# we want to have in our result.
#
# HOW WE'RE GOING TO DEAL WITH IT:
#   - Do everything we did before: fetch a page, navigate it and output to csv
#   - Refine our script to dip into the detail page for each reactor
#   - Use pattern matching to isolate two additional data points for our csv
#   -

# Let's add Python's regex and time libraries.
import requests
from bs4 import BeautifulSoup
import csv



url = 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'

web_page = requests.get(url)
web_page.encoding = 'UTF-8'
soup = BeautifulSoup(web_page.text)

reactor_table = soup.find('table')

# We'll send stuff to a different file.
csv_file = open('reactors.csv', 'wb')
output = csv.writer(csv_file)
# Add the two new fields we'll grab from the detail page to the header row.
output.writerow(['NAME', 'LINK', 'DOCKET', 'TYPE', 'LOCATION', 'OWNER', 'REGION'])

for row in reactor_table.find_all('tr')[1:]:
    cell = row.find_all('td')
    name = cell[0].contents[0].string
    link = cell[0].contents[0].get('href')
    docket = cell[0].contents[2].strip()
    type = cell[1].string
    location = cell[2].string.encode('utf8')
    owner = cell[3].contents[0].encode('utf8')
    region = cell[4].string

    # Let's get the reactor's detail page and get a quick note about it.



    # Use pattern matching to find the text after 'Licensed MwT:'
    # '(?i)licensed mwt:\s*</strong>(.*)<' decoded:
    # (?i) = ignore case
    # \s* = spaces may exist
    # () = the text we care about
    # .* = all characters, including text, numbers and punctuation

    # Send the match to a variable.


    # Do the same thing for the text after 'Containment Type:'
    # '(?i)containment type:\s*</strong>(.*?)\s*<'



    # Add these two new fields to the csv.writer's output.
    output.writerow([name, link, docket, type, location, owner, region])

    # Let's slow down how quickly we're sending these requests for detail pages.
    time.sleep(2)


csv_file.close()
print 'All done!'
