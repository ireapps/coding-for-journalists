### Scraping the web

Now that we've familiarized ourselves with the ways Python works, we have a little bit of a foundation to build from. Nearly everything else we do today is going to be using the fundamentals from [the intro](pt1.md) to varying degrees and in different combinations to create longer scripts.

So let's scrape a web page. We want to collect all the data from the main table on the U.S. Nuclear Regulatory Commission's [list of domestic power reactor units](http://www.nrc.gov/reactors/operating/list-power-reactor-units.html).

Python comes with a library installed that's designed specifically for reading and writing CSV files ([```csv```](https://docs.python.org/2/library/csv.html)), but we're also going to need to extend Python's functionality a bit by bringing in two other libraries.

One is [```requests```](http://docs.python-requests.org/en/latest/) -- it handles the job of playing a web browser that can fetch a web page and send back the underlying HTML. The other is [```BeautifulSoup```](http://www.crummy.com/software/BeautifulSoup/), which parses the HTML into what amounts to a series of lists that we can then search, navigate and extract data from.

When we get to part two, we'll use the built-in regular expressions library [```re```](https://docs.python.org/2/library/re.html) to isolate some text from the detail pages and [```time```](https://docs.python.org/2/library/time.html) to keep us from swamping a government site with too many requests at once.

A big thank you to [Anthony DeBarros](https://twitter.com/anthonydb) for allowing us to present a modified version of his web scraping example from [python-get-started](https://github.com/anthonydb/python-get-started).

We'll use the following files:

- **scrape.py**: The file we'll use to write our scraping script, following the comments.

- **scrape_pt2.py**: The file we'll use to push our scraping script further; it contains finished code for **scrape.py** and open spots to add code that loops through to detail pages and collects additional information.

- **nrc_backup.html**: A backup version of the main table we want to scrape in case there's a connection problem.

- **table_example.html**: A bare bones HTML table that shows the basic tags and how they're nested, with the flourishes of a modern web page stripped away -- it's ugly.

- **fun_with_bs.py**: A primer for some of BeautifulSoup's most relevant commands for navigating HTML.

- **fun_with_csv.py**: A brief example of how Python uses its standard csv library to read and write delimited-text files.

- **fun_with_regex.py**: A file that covers some regular expresses in Python for finding and isolating text.

Finished versions will appear in the **completed** folder.