# This is a quick primer on BeautifulSoup and some of its key abilites. For
# more, see the docs: http://www.crummy.com/software/BeautifulSoup/bs4/doc/



# The sequence of events with BeautifulSoup:

# 1. Get a file. Maybe you have requests playing web browser and it will hand
#    you the file contents. Here we'll just read a file into a variable.




# 2. Make a BeautifulSoup object out of HTML file contents. This makes the
#    underlying HTML something BeautifulSoup can navigate and parse.



# 2a. Peek at the HTML that BS has gone to work on, if you'd like.



# 3. Isolate the information that you want to collect. This is where BS
#    really shines. This is an example of very simple criteria: HTML
#    within <table> tags.



# 4. Start walking through this isolated information; for a table, the pattern
#    generally dives into each row and then each cell.







# for row in table:
#     make empty list to hold cell text
#     for cell in row:
#         append cell text to list
#     print the list contents joined together by commas

# This scraped information can then be written to a file or manipulated
# further.
