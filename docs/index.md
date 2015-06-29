#Coding for Journalists

This class is an evolving introduction to coding and the Python programming language for journalists. In addition to a tour of the fundamentals, it spans four basic projects to get you started.

The first version of this course happened at the [2015 IRE Conference in Philadelphia](https://ire.org/conferences/ire-2015/); the repository and associated tasks have been updated throughout the summer.

A few things to note before we get rolling:

* This guide and all documentation live at [coding-for-journalists.rtfd.org](http://coding-for-journalists.rtfd.org)
* The GitHub repository that includes all code is available from [github.com/ireapps/coding-for-journalists](https://github.com/ireapps/coding-for-journalists)
* A good place to raise issues with the code or ask specific questions about the code is [also on GitHub](https://github.com/ireapps/coding-for-journalists/issues)
* [Email](mailto:alex@ire.org) IRE Training Director Alex Richards, the primary author of this course, or [contact him on Twitter](http://www.twitter.com/alexrichards)

Because of the pace of this class and limited amount of time available, we won't be able to easily accommodate attendees who prefer to use their own laptops during the session. 

Each task we'll tackle has (at least) two files: the one for writing code in and a version with "_done" appended to the name that's already been completed. Since there won't be enough time to get through every single one, you can circle back afterward, fetch these files from GitHub and work through the exercises on your own.

### Requirements

This is designed for people who have some grounding in data journalism already and experience with spreadsheets and database managers. It's helpful if you understand Excel functions, for example, and some basic SQL.

You will likely struggle if you don't know how to navigate the computer's command line, too; it involves moving between folders, running scripts and issuing commands to a Python interpreter.



Here's what the next few hours have in store:

### [1_start](https://github.com/richardsalex/coding_for_journos/tree/master/1_start)

A whirlwind tour of Python's data types, variables, basic functionality and loops. We'll run a script in the iPython interactive interpreter to load a variety of variables and then start messing with them.

### [2\_web_scrape](https://github.com/richardsalex/coding_for_journos/tree/master/2_web_scrape)

Fetching data from the web was one of programming's original beachheads in the journalism world. We're going to grab a data table from a website and turn it into a delimited text file to use in a spreadsheet or database manager.

This is a task one could arguably accomplish using Excel's "import from web" feature, so we're going to take it one step further: we'll alter our script to drill into additional detail pages and automatically extract more columns of data for our text file.

### [3\_parse_addresses](https://github.com/richardsalex/coding_for_journos/tree/master/3_parse_addresses)

Data don't always arrive in a nice, neat table. We have hundreds of addresses to parse into a format that will work in Excel or a database manager, and Python is going to help us make it happen. We'll write a script that dices it all and puts everything in its proper place -- one line for one location.

### [4\_make_function](https://github.com/richardsalex/coding_for_journos/tree/master/4_make_function)

In this quick project, we'll modify the address parsing script we wrote in the previous exercise, turning it into a reusable function that we can apply to future address lists that arrive in the same problematic format.

### [5\_geocode](https://github.com/richardsalex/coding_for_journos/tree/master/5_geocode)

Geocoding is one of those perennial data journalism problems that's gotten easier in some ways over the years, yet harder in others. While having a street address is great, having a latitude and longitude is better. We'll take the poorly formatted addresses we coaxed into a flat file and march them one at a time through an online geocoding service using a handy Python library called [geopy](https://github.com/geopy/geopy). 