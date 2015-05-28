# Coding for Journalists #
### IRE15, Philadelphia ###
### Thursday, June 4, 2015: 2:30pm to 5:50pm
---

This class is an evolving introduction to coding and the Python programming language for journalists. In addition to a tour of the fundamentals, it spans four basic projects to get you started.

We're working in a PC lab in Philadelphia, so we're going to be using the [Anaconda distribution of Python](http://continuum.io/downloads), which comes with many popular libraries already installed alongside the core program. We'll also be using Windows PowerShell as the command line interface to run our scripts and [iPython](http://ipython.org/) -- a handy interactive interpreter and sandbox for messing around with Python. Beyond that, just a text editor. Everything you'll need is already installed and tested on these machines.

Each task we'll tackle has two files: the one we'll write code in and then a version with '_done' appended to the name that's already been completed. Since there won't be enough time to get through every single one, you can circle back afterward and work through the exercises on your own. 

### [1_start](https://github.com/richardsalex/coding_for_journos/tree/master/1_start)

A whirlwind tour of Python's data types, variables, basic functionality and loops. We'll run a script in the iPython interactive interpreter to load a variety of variables and then start messing with them.

### [2\\_web_scrape](https://github.com/richardsalex/coding_for_journos/tree/master/2_web_scrape)

Fetching data from the web was one of programming's original beachheads in the journalism world. We're going to grab a data table from a website and turn it into a delimited text file to use in a spreadsheet or database manager.

This is a task one could arguably accomplish using Excel's "import from web" feature, so we're going to take it one step further: we'll alter our script to drill into additional detail pages and automatically extract more columns of data for our text file.

### [3\\_parse_addresses](https://github.com/richardsalex/coding_for_journos/tree/master/2_parse_addresses)

Data don't always arrive in a nice, neat table. We have hundreds of addresses to parse into a format that will work in Excel or a database manager, and Python is going to help us make it happen. We'll write a script that dices it all puts everything in its proper place -- one line for one location.

### [4\\_make_function](https://github.com/richardsalex/coding_for_journos/tree/master/4_make_function)

In this quick project, we'll modify the address parsing script we wrote in the previous exercise, turning it into a reusable function that we can apply to future address lists that arrive in the same problematic format.

### [5\_geocode](https://github.com/richardsalex/coding_for_journos/tree/master/5_geocode)

Geocoding is one of those perennial data journalism problems that's gotten easier in some ways over the years, yet harder in others. While having a street address is great, having a latitude and longitude is better. We'll take the poorly-formatted addresses we coaxed into a flat file and march them one at a time through a online geocoding service using a handy Python library called [geopy](https://github.com/geopy/geopy). 