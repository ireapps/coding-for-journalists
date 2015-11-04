# Coding for Journalists

This class is an evolving introduction to coding and the Python programming language for journalists. In addition to a tour of the fundamentals, it spans nine basic projects to get you started.

The [first version](https://github.com/ireapps/coding-for-journalists/tree/ire2015) of this course happened at the [2015 IRE Conference in Philadelphia](https://ire.org/conferences/ire-2015/); the repository and associated tasks have been updated since.

A few things to note before we get rolling:

* This guide and all documentation live at [coding-for-journalists.rtfd.org](http://coding-for-journalists.rtfd.org)
* The GitHub repository that includes all code is available from [github.com/ireapps/coding-for-journalists](https://github.com/ireapps/coding-for-journalists)
* A good place to raise issues with the code or ask specific questions about the code is [also on GitHub](https://github.com/ireapps/coding-for-journalists/issues)
* [Email](mailto:alex@ire.org) IRE Training Director Alex Richards, the primary author of this course, or [contact him on Twitter](http://www.twitter.com/alexrichards)

We have set aside time at the end of the workshop to work through the process of getting your home or work laptop set up with Python and a development environment. If you're looking for [a guide](install.md), we've put one together that covers most of what you'll need for OS X and Windows.

Each task we'll tackle and set of lessons has finished and working versions of the code in the "completed" folder; they typically have "_done" appended to the end of the filename. If there isn't enough time to hit each one during our time together, there's enough commenting in place that you should be able to work through them on your own (and feel free to bug [Alex](mailto:alex@ire.org)).

This is designed for people who have some grounding in data journalism already and experience with spreadsheets and database managers. It's helpful if you understand Excel functions, for example, and some basic SQL. Other important skills include navigation of the computer's command line; we'll bemoving between folders, running scripts and issuing commands to a Python interpreter.

## What the next few days have in store

#### Introduction

A whirlwind tour of Python's data types, variables, basic functionality and loops. We'll write a bunch of them on our own, discuss them, and then run a script in the iPython interactive interpreter to load a variety of variables and then start messing with them.

We'll also talk about how to format strings — which we'll be doing a ton — and how Python deals with whitespace.

#### Scraping data from the web

Fetching data from the web was one of programming's original beachheads in the journalism world. We're going to grab a data table from a website and turn it into a delimited text file to use in a spreadsheet or database manager.

This is a task one could arguably accomplish using Excel's "import from web" feature, so we're going to take it one step further: we'll alter our script to drill into additional detail pages and automatically extract more columns of data for our text file.

We'll also drill into the finer points of using the BeautifulSoup library to parse HTML, reading and writing CSV files, and targeting data with regular expressions.

#### Parsing records that fall across multiple lines

Data don't always arrive in a nice, neat table. We have hundreds of addresses to parse into a format that will work in Excel or a database manager, and Python is going to help us make it happen. We'll write a script that dices it all and puts everything in its proper place -- one line for one location.

#### Making a reusable function

In this quick project, we'll modify the address parsing script we wrote in the previous exercise, turning it into a reusable function that we can apply to future address lists that arrive in the same problematic format.

#### Geocoding with Python

Geocoding is one of those perennial data journalism problems that's gotten easier in some ways over the years, yet harder in others. While having a street address is great, having a latitude and longitude is better. We'll take the poorly formatted addresses we coaxed into a flat file and march them one at a time through an online geocoding service using a handy Python library called [geopy](https://github.com/geopy/geopy).

#### Working with APIs and databases

Application Programming Interfaces have become a common spigot for data on the web. We'll tap into one maintained by the city of Chicago that deals with crime and send it to a table in a SQLite database. From there, we'll write some scripted queries to isolate interesting information.

We'll also dig in on how Python interacts with databases and how it deals with dates and times.

#### Unlocking data stuck in a database 

A database is a great reporting tool, having your data and analysis locked up there don't help your audience much. We're going to work with the same crime data we processed earlier and turn it into a web-friendly format (GeoJSON) for automatic display on a very basic Leaflet.js map. 

#### The wonderful world of data cleaning

Once you figure out what the problems are with a data set, you can outsource the tedious cleaning process to Python. We'll focus on a few different types of cleaning you're likely to encounter in your reporting life, including Excel files where data is scattered around different rows and columns, CSV files with obvious errors that 

#### Other kinds of scrapes

We're not always after web tables; sometimes we're trying to collect a bunch of files scattered around a website or need to POST some data in order to get a response from a dynamic page, like a government site that uses ASP.NET. 

#### The deal with text encoding and debugging your scripts

What's ASCII? Why the hell am I getting ```UnicodeEncodeError```? We'll deal sporadically with text encoding in some of these other lessons, but we'll focus on why it's important and what you can do to stay on top of it. In addition, we'll look through common errors you'll run into, what they mean and how to fix them.