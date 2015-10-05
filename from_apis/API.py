#!/usr/bin/env python

# For more information about this particular API, Socrata, the vendor Chicago uses for 
# many of its publicly-facing data sources, has excellent documentation to read:
# http://dev.socrata.com/foundry/#/data.cityofchicago.org/6zsd-86xi


# When were the most recent records added? 

import json
import requests
import sqlite3
from datetime import datetime, date, timedelta

crime_url = 'https://data.cityofchicago.org/resource/6zsd-86xi.json'

# Let's write a function that check the date of the most recent crime in the JSON and
# returns it. We'll have it convert the date it finds into a datetime object Python
# can do some math on.
def date_check():
	r = requests.get(crime_url + '?$limit=1&$order=date DESC')
	most_recent_crime = r.json()
	date_string = most_recent_crime[0]['date'][:10]
	return datetime.strptime(date_string,'%Y-%m-%d')
	
# We're going to have to convert dates back and forth between strings a bit. Better to 
# just go ahead and whip a short function for it.
def date_to_string(dt):
	return dt.date().isoformat()
	
# Let's write another designed to grab the most recent week of crime from Chicago's API.
# We'll set it up so it can take the date from our date_check function.
def crime_week(dt):
	end_date = date_to_string(dt)
	start_date = date_to_string(dt - timedelta(days=6))
	query_url = crime_url + '?$limit=50000&$where=date between \'%sT00:00:00\' and \'%sT23:59:59\'' % (start_date, end_date)
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
# 	lengths.append(len(rec))
# print set(lengths) # set is a data type that only holds uniques

# Let's see what one of these shorter crime records looks like.
# for rec in week:
# 	if len(rec) == 17:
# 		shorter = rec
# 		break

# Open a connection to a SQLite database and create a cursor we'll use to interact with 
# said database.  
db_loc = 'test.db'
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
	
c.execute("CREATE TABLE IF NOT EXISTS newtest (" + ", ".join(fields) + ")")

# So now we have to write a SQL statement that will insert values into the right fields, 
# regardless of how long the field is. To make this happen, we're also going to need to 
# deal with some dict order weirdness.

for rec in week:
	cols = []
	vals = []
	for item in rec:
		if item != 'location':
			cols.append(item)
			vals.append(str(rec[item]))
	c.execute("INSERT INTO newtest (" + ",".join(cols) + ") VALUES ('" + "','".join(vals) + "')")
	
conn.commit()
	
# Some basic queries based on the data.

# Top 10 beats for different crimes
c.execute('''SELECT beat, count(*)
FROM newtest
WHERE primary_type = 'ROBBERY'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 0,5''')
top_rob = c.fetchall()

for item in top_rob:
    print 'Beat %s: %s robberies' % (item[0], item[1])
    
# Communities with the top violent crime rates


# will have to be filled in with req process
# file_loc = '/Users/alexrichards/Desktop/crime.json'
# 
# with open(file_loc, 'rb') as json_file:
#     crime_data = json.load(json_file)
    

