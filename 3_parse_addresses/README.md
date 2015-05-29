# 3\_parse_addresses

It would be great if every piece of data you came across was in a format that lent itself to easy capture. In the same vein as the text extraction from reactor detail pages in our last example, we're going to pick apart an HTML file of licensed payday lenders (that's mostly text) and turn it into a flat CSV file where one row is one record.

In this file, addresses can span three, four or five lines. Sometimes it's on four lines because a lender does business in Illinois under another name; in others, it's because the lender operates out of a suite, room or building stored on a line separate from the street address. This means that our script needs to behave four different ways depending on how many lines it encounters for each address, and we'll switch between those behaviors with ```if/elif``` syntax.

We'll again use ```BeautifulSoup```, but primarily to break out the portion of the file we want to capture for the resulting CSV.

This exercise has three files:

- **payday.py**: The file we'll use to write our address parser, following the comments.

- **payday_lenders.html**: A simple HTML file that lists nearly 500 payday lenders licensed to do business in Illinois; their addresses are split across multiple lines.

- **payday_done.py**: A completed and working version of **payday.py**.
