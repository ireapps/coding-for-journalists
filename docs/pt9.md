#### Other scrapes

Scraping can be about more than parsing tables tags in HTML.

The first thing we'll do is collect files from a website with Python.

Then we'll turn out attention to this common problem: ```javascript:__doPostBack()``` isn't a link you can follow with a click in Python, but sometimes the data you need is behind it. 

If we're trying to collect data from a government website using ASP.NET, we can watch the transaction between our browser and the site unfurl using developer tools like the ones built into Chrome. The requests library isn't just good for fetching URLs — it's full service. It can POST information as well with the intention of getting a response from the site. Based on what we see in terms of exhanged headers, we can copy that information and use requests to send it ourselves.

The files we'll be using:

- **other_scrapes.py**: This script will collect a set of PDFs. We'll point BeautifulSoup at the page contents to collect the links and then pipe the contents of those links (the PDFs) to files on our machine.

- **other_scrapes_post.py**: We'll use requests to POST data to the Illinois Elections site, causing its ASP.NET framework to give us a tab-delimited text file that contain's the days political contributions. 