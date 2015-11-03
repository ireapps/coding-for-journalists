#! usr/bin/python

import requests
from bs4 import BeautifulSoup
import re
import time

# We're not always going to be diving into a table or other information tied
# up in HTML. Sometimes our target is a file or set of files; we can write the content
# to outfiles in a directory of our choosing.

# Fetch the page:
# https://portal.chicagopolice.org/portal/page/portal/ClearPath/News/Crime Statistics

url = 'https://portal.chicagopolice.org/portal/page/portal/ClearPath/News/Crime Statistics'
page = requests.get(url)

# Process the HTML with BeautifulSoup

soup = BeautifulSoup(page.text)

# Find all the links on the page (just for practice)
soup.find_all('a')

# The links we want don't have great characteristics to hook onto; let's just
# find everything where the link contains '.pdf'

pdf_links = soup.find_all(href=re.compile('.pdf'))

# Sometimes it's useful to me to count up what I expect to have. We'll take
# a peek here and use the enumerate function to count. When iterating through
# a list it returns a tuple that looks like (<number>, <list item>) instead
# of just <list item>.

for link in enumerate(pdf_links):
    print '{0}: {1}'.format(link[0]+1, link[1].string)

# Make an empty list to hold the URLs we're going to pull out of all these links.

pdf_urls = []

# Loop through and grab the URLs.

for link in pdf_links:
    pdf_urls.append(link['href'])

# Now we have a list of PDF files to grab from the page. We're going to write
# the content in each to a file, and we can use information we've gleaned
# from the file or link to name the files that we're writing to disk.

# Let's use a dict instead; the key will be the link text and the value will
# be the URL.

pdf_urls_dict = {}

for link in pdf_links:
    pdf_urls_dict[link.string] = link['href']

# We can get the original file name out of the URL by splitting URL at '/' and
# grabbing the last item in the list.

name_ex = pdf_urls_dict['District 010'].split('/')[-1]
print name_ex

# Since the original file names don't contain any information about the District
# or Area, let's add that in.

# Also, let's make sure we're not bombarding the site with a ton of requests at
# the same time; we need to briefly pause between downloads.

# We'll pass the URL to a variable, get it with requests, do a little tinkering
# with the PDF name and link name to remove spaces (and the URL equivalent),
# then write them to a directory.

for url in pdf_urls_dict:
    pdf = pdf_urls_dict[url]
    file = requests.get(pdf)
    loc_name = url.replace(' ', '')
    pdf_name = pdf.split('/')[-1].replace('%20', '')
    file_name = '{0}-{1}'.format(loc_name, pdf_name)
    directory = './pdfs/'
    with open(directory+file_name, 'wb') as outfile:
        outfile.write(file.content)
    print 'Grabbed '+loc_name
    time.sleep(1)
