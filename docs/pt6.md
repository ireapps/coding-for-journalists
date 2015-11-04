#### APIs and databases

Scraping isn't the only method for retrieving data; sometimes data resources on the internet — even one maintained by government agencies — actually want to give it away in a usable format. Web application rogramming interfaces exist to make this happen. More often than not, you pass a query through an API's URL and get a response in [JSON](http://www.json.org/) (JavaScript Object Notation) format, which is highly structured and can look a lot like a Python list or dictionary.

We're going to query a [Socrata](http://www.socrata.com/) API maintained by the city of Chicago. This [particular data source](https://dev.socrata.com/foundry/#/data.cityofchicago.org/ijzp-q8t2/no-redirect) is where crime incidents are reported by the Chicago Police Department; the lag time for reporting is about one week.

Our initial goal is to grab the most recent week of crimes in the system, which means pinging the API to figure out the date of the last crime and then grabbing every reported crime on that day and the previous six. This will involve some work with ```datetime``` and date math in Python. 

We're also going to inspect the incoming stream of JSON from the API to make sure we can tell if any are missing fields. This becomes important because we are going to feed each crime event into an [SQLite](https://docs.python.org/2/library/sqlite3.html) database.

SQLite may not be as robust as some other database managers, but it's part of the standard library in later versions of Python 2.7 and creates lightweight database files that are easy to connect to and query.

We'll write some automated queries for crime trends, including which beats in Chicago had the most reported narcotics crimes during the week and what the violent crime rate was in different communities.

This particular task uses these files:

- **API.py**: The main script that fetches data from the crime API, puts it in a SQLite database and runs queries on the data.

- **crime.db**: A SQLite database that only has a table with population data for Chicago's various community areas. We'll add to it from the crime API.

- **fun_with_datetime.py**: A more focused look at datetime objects and how they work in Python.

- **fun_with_sqlite.py**: The fundamentals of connecting to, modifying and querying a database with Python.

- **crime_backup.json.zip**: Shoddy internet or a downed website won't ruin this exercise; this is compressed JSON that represents a week of Chicago crime.

Finished versions are in the **completed** folder.