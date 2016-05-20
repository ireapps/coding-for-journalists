# FUN WITH BEAUTIFULSOUP
#
# This is a quick primer on BeautifulSoup and some of its key abilities. The
# big advantage is that it's great at parsing different markup languages,
# like HTML. Think of it like a diving rod for text on a web page.
# For more, see the docs:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/

# The library has more than just BeautifulSoup, but let's just import that.

from bs4 import BeautifulSoup

# The sequence of events with BeautifulSoup:

# 1. Open a file. In many cases, you'll be sending the content of a web page
# fetched by the requests library. In this example, we'll just open a file
# like we would any other and read it into a variable.

with open('table_example.html', 'rb') as infile:
    example = infile.read()

# 2. Make a BeautifulSoup object out of HTML file contents. This transforms
# the underlying HTML into something BeautifulSoup can navigate and parse.

soup = BeautifulSoup(example, 'html.parser')

# 2a. Peek at the HTML that BS has gone to work on, if you'd like.

print soup.prettify()

# 3. Isolate the information that you want to collect. This is where BS
# really shines. There are many different ways to dive into the markup
# "tree" outlined in the documentation, but this is an example of ferreting
# out one thing: HTML within <table> tags.

table = soup.find('table')

# 4. Start walking through this isolated information; for a table, the pattern
# generally dives into each row and then each cell. This is just one way to
# do it; we'll use a slightly different construction in our scraping task.

for row in table.find_all('tr'):
    cell_holder = []
    for cell in row.find_all(['th', 'td']):
        cell_holder.append(cell.text)
    print ', '.join(cell_holder)
    
# What's happening in the above example:
# 
# for each row in the table (identified by <tr> tags):
#     make an empty list to hold the text from cells
#     then, for each cell in the row (identified by either <th> or <td> tags):
#         append the text for that cell to the empty list
#     finally, print those list contents on one line, connect them with commas

# This scraped information can then be written to a file or manipulated
# further.
