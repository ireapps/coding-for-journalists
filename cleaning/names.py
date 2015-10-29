#! usr/bin/python

import requests
from bs4 import BeautifulSoup
import csv
import re
import time

main_url = 'https://webapps1.cityofchicago.org/moboco/org/cityofchicago/moboc/controller/view/start.do'

page = requests.get(main_url)

soup = BeautifulSoup(page.content, 'html.parser')

board_links = soup.find_all('a', href=re.compile('cid='))

# Quick check to make sure we're getting all of our links before we move on
for link in board_links:
    print link.text
print 'Total number of boards: '+str(len(board_links))

# Let's look at the URL string
print board_links[0].get('href')
print board_links[1].get('href')

# What we really care about are the numbers at the end of the link; that's
# how the whole setup for the website works. We feed it an ID, it generates
# a page.

board_pages = []

for link in board_links:
    board_name = link.string
    board_url = link.get('href')
    # We only need the number at the end; we can split the URL and grab it
    board_code = board_url.split('?cid=')[1]
    tup = (board_name, board_code)
    board_pages.append(tup)

board_url = 'https://webapps1.cityofchicago.org/moboco/org/cityofchicago/moboc/controller/view/searchBoard.do?cid='

# Just as a test, let's look at the first one to see what we're dealing with.

test_page = requests.get(board_url+board_pages[0][1])
soup = BeautifulSoup(test_page.content, 'html.parser')

# Two tables on each page, both are functionally identical to BeautifulSoup,
# so we just grab both and take the second.

page_tables = soup.find_all('table', {'class': 'resultTable'})
member_table = page_tables[1].find_all('tr')

# The names are coming from a db that's dynamically combining them; we can use that.
# All the components are inside of label tags. If we try to extract the text, we're
# met with a mess of unicode junk (non-breaking spaces, in this case) meant to
# glue the title, first name, middle initial and last name together.

first_row = member_table[1]

# Pull the name and clean it up with split(), which by default will work on
# whitespace. .join and .split together can be handy for cleaning.

name_text = first_row.td.text
clean_name = ' '.join(name_text.split())

# Depending on how we need the name to be parsed, it might be better for us
# to chop it up into components.

name_list = []
for name_part in first_row.td.find_all('label'):
    name_list.append(name_part.text)

# Now that we see how this works, we can write a full run. We'll feed
# requests.get a page, parse it with BeautifulSoup, and write it to CSV.

# We can use the 'with' syntax here to open the file
with open('./boards.csv', 'wb') as csv_outfile:
    writer = csv.writer(csv_outfile)
    writer.writerow(['BOARD', 'FULL_NAME', 'TITLE', 'FIRST_NAME', 'MIDDLE', 'LASTNAME', 'SUFFIX', 'TERM', 'APPOINTER'])
    for board_page in board_pages:
        # We can basically use what we've done above to zero in on the table
        page = requests.get(board_url+board_page[1])
        soup = BeautifulSoup(page.content, 'html.parser')
        page_tables = soup.find_all('table', {'class': 'resultTable'})
        member_table = page_tables[1].find_all('tr')
        # Another for loop to move inside each row (except the header)
        for row in member_table[1:]:
            cells = row.find_all('td')
            name_cell = cells[0]
            term_cell = cells[1]
            appt_cell = cells[2]
            full_name = ' '.join(name_cell.text.split())
            # If it's a vacancy, let's not go through the trouble of splitting.
            if full_name == 'Vacancy':
                title, first_name, mi, last_name, suffix = '', '', '', '', ''
            else:
                # Slot the different components here
                name_parts = []
                for part in name_cell.find_all('label'):
                    name_parts.append(part.text)
                title = name_parts[0]
                first_name = name_parts[1]
                mi = name_parts[2]
                # Last name is currently including suffixes like Jr, Sr, III, etc.
                # We can look for a comma that denotes the suffix.
                if name_parts[3].find(',') == -1:
                    last_name = name_parts[3]
                    suffix = ''
                else:
                    last_split = name_parts[3].split(', ')
                    last_name = last_split[0]
                    suffix = last_split[1]
            term = term_cell.text.strip()
            appt = appt_cell.text.strip()
            writer.writerow([board_page[0], full_name, title, first_name, mi, last_name, suffix, term, appt])
        print 'Fetched and wrote '+board_page[0]
        time.sleep(2)
