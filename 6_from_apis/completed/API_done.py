#!/usr/bin/env python

# For more information about this particular API, Socrata, the vendor Chicago
# uses for many of its publicly-facing data sources, has excellent
# documentation to read:
# http://dev.socrata.com/foundry/#/data.cityofchicago.org/6zsd-86xi

import requests
import sqlite3
from datetime import datetime, date, timedelta

crime_url = 'https://data.cityofchicago.org/resource/6zsd-86xi.json'

# Let's write a function that check the date of the most recent crime in the JSON and
# returns it. We'll have it convert the date it finds into a datetime object Python
# can do some math on.


def date_check():
    # URL: https://data.cityofchicago.org/resource/6zsd-86xi.json?$limit=1&$order=date DESC
    r = requests.get('{0}?$limit=1&$order=date DESC'.format(crime_url))
    most_recent_crime = r.json()
    date_string = most_recent_crime[0]['date'][:10]
    return datetime.strptime(date_string, '%Y-%m-%d')

# We're going to have to convert dates back and forth between strings a bit. Better to
# just go ahead and whip up a short function for it.


def date_to_string(dt):
    return dt.date().isoformat()

# Let's write another designed to grab the most recent week of crime from Chicago's API.
# We'll set it up so it can take the date from our date_check function.


def crime_week(dt):
    end_date = date_to_string(dt)
    start_date = date_to_string(dt - timedelta(days=6))
    query_url = '{0}?$limit=50000&$where=date between \'{1}T00:00:00\' and \'{2}T23:59:59\''.format(crime_url, start_date, end_date)
    r = requests.get(query_url)
    return r.json()

# With those three functions in place, one short line of code will toss the most recent
# week's worth of crimes into a variable for us.
week = crime_week(date_check())

# Let's do some quick checks in the interpreter to see what our data looks like:
# week[0] # return the first record
# len(week) # see how many records we received

# Are all the records we're getting back the same length? This will be important when we
# kick the result over to a database.
# lengths = []
# for rec in week:
#     lengths.append(len(rec))
# print set(lengths) # set is a data type that only holds uniques

# Let's see what one of these shorter crime records looks like.
# for rec in week:
#     if len(rec) == 17:
#         shorter = rec
#         break

# Open a connection to a SQLite database and create a cursor we'll use to interact with
# said database. (If one doesn't exist, it'll be created on the spot.)
db_loc = 'crime.db'
conn = sqlite3.connect(db_loc)
c = conn.cursor()

# We want to make a table, so let's get a list of fields that need to be in there. We
# won't put "location" in, because it's redundant (we already have latitude and longitude,
# not to mention Illinois state plane coordinates in feet).
fields = []

for rec in week:
    if len(rec) == 22:
        for item in rec.items():
            fields.append(item[0])
        fields.remove('location')
        fields.sort()
        break

# Let's write a quick function to figure out if the table already exists in our database
# or not. If we query a table that doesn't exist, we'll get an error; let's use that to
# our advantage.


def table_exist(table_name):
    try:
        c.execute("SELECT * FROM {}".format(table_name))
    except sqlite3.OperationalError:
        return False
    else:
        return True

if table_exist('week') is False:
    c.execute("CREATE TABLE week ({})".format(', '.join(fields)))
    # So now we have to write a SQL statement that will insert values into the right fields,
    # regardless of how long the field is. To make this happen, we're also going to need to
    # deal with some dict order weirdness by specifying fields for our inserted values.
    for rec in week:
        cols = []
        vals = []
        for item in rec:
            if item != 'location':
                cols.append(item)
                vals.append(str(rec[item]))
        # SQL format: INSERT INTO <table> (<col1>, <col2>, ...) VALUES ('<val1>', '<val2>', ...)
        c.execute("INSERT INTO week ({0}) VALUES ('{1}')".format(', '.join(cols), "', '".join(vals)))
    conn.commit()
else:
    print 'Table already exists.'

# Some basic queries based on the data.

# A function to assess the week's crimes.


def high_crime_areas(main_type, area, top):
    valid_areas = ['district', 'beat', 'community_area', 'ward']
    if area in valid_areas:
        result = [area, main_type]
        c.execute('''SELECT {0}, count(*)
                     FROM week
                     WHERE primary_type = '{1}'
                     GROUP BY 1
                     ORDER BY 2 DESC
                     LIMIT 0,{2}'''.format(area, main_type, top))
        result.append(c.fetchall())
        return result

# And a function to format the result of high_crime_areas!


def show_crimes(result):
    head_string = '{0} BY {1}'.format(result[1], result[0])
    print head_string.upper().replace('_', ' ')
    print '-' * len(head_string)
    for t in result[2]:
        print '{0}: {1}'.format(t[0], t[1])
    print '\n\n'

# This could be set up to run some quick summaries as soon as the data is processed by
# the script.
show_crimes(high_crime_areas('HOMICIDE', 'district', 100))
show_crimes(high_crime_areas('NARCOTICS', 'beat', 5))
show_crimes(high_crime_areas('ASSAULT', 'ward', 10))
show_crimes(high_crime_areas('THEFT', 'community_area', 10))

# Violent crime rates in each Chicago community for the most recent week of data available

sql = '''SELECT chicago_areas.comm_name, ROUND((crime_query.violent_crimes*1.0/chicago_areas.pop2010) * 10000,2) as rate
         FROM (
               SELECT community_area, COUNT(*) AS violent_crimes
               FROM week
               WHERE primary_type in ('HOMICIDE', 'CRIM SEXUAL ASSAULT', 'ROBBERY', 'ASSAULT', 'BATTERY')
               GROUP BY 1
               ) as crime_query, chicago_areas
         WHERE crime_query.community_area = chicago_areas.comm_id
         ORDER BY 2 DESC'''

c.execute(sql)
results = c.fetchall()
print 'Violent crime rates by community'
print '-' * 32
for row in results:
    offset = ' ' * (25 - len(row[0]))
    print '{0}:{1}{2}'.format(row[0], offset, row[1])
