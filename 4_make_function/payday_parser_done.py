from bs4 import BeautifulSoup
import csv

# Let's bundle everything we did previously into a function. Let's call it 'ParseMyAddresses'. We'll pass it one variable,
# the HTML file that we want parsed.


def ParseMyAddresses(html_file):
# Because indentation controls how Python reads our code, we need to tab all the code over one spot under the function def.
    # Instead of explicitly giving Python a file name, we'll have the function pass that information along.
    html = open(html_file, 'rb')
    soup = BeautifulSoup(html)

    block = unicode(soup.body)
    block = block.replace('<hr/><br/>', '')

    list = block.split('<br/><br/>')
    list = list[2:len(list)-1]
    # And instead of specifying a csv file name, we'll make one out of the HTML file, replacing '.html' with '.csv'
    csv_file = open(html_file.replace('.html', '.csv'), 'wb')
    output = csv.writer(csv_file)
    output.writerow(['NAME', 'DBA', 'STADDR', 'STADDR2', 'CITY', 'STATE', 'ZIP'])

    for lender in list:
        details = lender.split('<br/>')
        name = details[0].strip()
        if len(details) == 3:
            dba = ''
            staddr = details[1].strip()
            staddr2 = ''
        elif len(details) == 4 and details[1].upper().startswith('D/B/A'):
            dba = details[1].strip()
            staddr = details[2].strip()
            staddr2 = ''
        elif len(details) == 4 and not details[1].upper().startswith('D/B/A'):
            dba = ''
            staddr = details[1].strip()
            staddr2 = details[2].strip()
        elif len(details) == 5:
            dba = details[1].strip()
            staddr = details[2].strip()
            staddr2 = details[3].strip()
        citystzip = details[len(details)-1].split(', ')
        city = citystzip[0].strip()
        state = citystzip[1].strip()
        zip = citystzip[2].strip()
        output.writerow([name, dba, staddr, staddr2, city, state, zip])

    csv_file.close()
