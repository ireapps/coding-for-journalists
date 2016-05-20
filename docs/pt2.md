### Scraping the web

Now that we've familiarized ourselves with the ways Python works, we have a little bit of a foundation to build from. Nearly everything else we do as part of this workshop will use the fundamentals from [the intro](pt1.md) to varying degrees and in different combinations to create longer scripts.

So let's scrape a web page. We want to collect all the data from the main table on the U.S. Nuclear Regulatory Commission's [list of domestic power reactor units](http://www.nrc.gov/reactors/operating/list-power-reactor-units.html).

Python comes with a library installed that's designed specifically for reading and writing CSV files ([**csv**](https://docs.python.org/2/library/csv.html)), but we're also going to need to extend Python's functionality a bit by bringing in two other libraries.

One is [**requests**](http://docs.python-requests.org/en/latest/) — it handles the job of playing a web browser that can fetch a web page and send back the underlying HTML. The other is [**BeautifulSoup**](http://www.crummy.com/software/BeautifulSoup/), which parses the HTML into what amounts to a series of lists that we can then search, navigate and extract data from.

Before we begin, we'll cover some of the key features in **BeautifulSoup** and **csv** by setting them to work on some simple examples.

When we get to part two, we'll take the script we've already written — the one designed to extract all of the table's reactor data — and modify it so that it also steps through a link for each reactor and retrieves a web page that shows additional details. The resulting HTML will be parsed by **BeautifulSoup**, and then we'll write a single, short function to return a couple additional columns to write to our CSV file. We'll also use a library called [**time**](https://docs.python.org/2/library/time.html) to keep the pace of our scraping in check — we don't want to swamp a government site with too many requests at once.

A big thank you to [Anthony DeBarros](https://twitter.com/anthonydb) for allowing us to present a modified version of his web scraping example from [python-get-started](https://github.com/anthonydb/python-get-started).

We'll use the following files:

- **fun_with_bs.py**: A primer for some of BeautifulSoup's most relevant commands for navigating HTML.
<br><br>
- **table_example.html**: A bare bones HTML table that shows the basic row and cell tags and how they're nested, with the flourishes of a modern web page stripped away.
<br><br>
- **fun_with_csv.py**: A brief example of how Python uses its standard csv library to read and write delimited-text files.
<br><br>
- **scrape.py**: The file we'll use to write our scraping script, following the comments.
<br><br>
- **scrape_pt2.py**: The file we'll use to push our scraping script further; it contains finished code for **scrape.py** and open spots to add code that loops through to detail pages and collects additional information.
<br><br>
- **nrc_backup.html**: A backup version of the main table we want to scrape in case there's a connection problem. A folder called **nrc_pages** also holds backup copies of all the reactor detail pages for part two.
<br><br>
Finished versions will appear in the **completed** folder.

!!! note
	It's recommended to read the documentation on each of these libraries for a more complete understanding of what they do and how they work. We'll be using some of their central methods, not delving fully into what they are capable of doing.
	
	- [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
	- [csv](https://docs.python.org/2/library/csv.html)
	- [requests](http://docs.python-requests.org/en/latest/)