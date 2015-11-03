#! usr/bin/python

# Now that we've processed JSON, moved into into a database an set up some helpful 
# prewritten queries for new records, we're going to talk about the flip side of that: 
# exporting data to JSON for use elsewhere.

# PROBLEM: We have some cool crime data and have set up the automated analysis
# of weekly records for interesting trends we may want to keep regular tabs
# on. It all comes with coordinates, though; why don't we use that to our
# advantage and generate some stuff we can actually see?

# HOW WE'RE GOING TO DEAL WITH IT:
#   - Query our database, crawl through the rows of results to make a GeoJSON
#     file of points from scratch for display when connected to a Leaflet map.
#   - Query our database again while going through an existing GeoJSON and
#     adding data to it, that way we can display the result.

import sqlite3
import json
import collections

# Connect to the crime.db we made earlier and grab all the homicide records.
db_loc = '../from_apis/crime.db'
conn = sqlite3.connect(db_loc)
c = conn.cursor()

c.execute('''SELECT *
             FROM week
             WHERE primary_type = "HOMICIDE"''')
             
homicides = c.fetchall()

# The GeoJSON format for points we'll need to write. Don't worry, we'll break it down!
#
# { "type": "FeatureCollection",
# 	"features": [
# 		{ "type": "Feature",
# 		"geometry": {"type": "Point", "coordinates": [<LONG_X>, <LAT_Y>]},
#         "properties": {"<PROPNAME>": "<PROPVALUE>"}
#         },
# 		{ "type": "Feature",
#         <...>
#         }
#     ]
# }

# As we've learned, the dict data type doesn't have an order. Fortunately,
# there's an OrderedDict object we can pull out here to keep our GeoJSON
# structured properly.

homicide_json = collections.OrderedDict()

homicide_json['type'] = 'FeatureCollection'
homicide_json['features'] = []

for h in homicides:
	feat = collections.OrderedDict()
	feat['type'] = 'Feature'
	feat['geometry'] = collections.OrderedDict()
	feat['geometry']['type'] = 'Point'
	feat['geometry']['coordinates'] = [float(h[14]), float(h[12])]
	feat['properties'] = {'block': h[2], 'location': h[13], 'datetime': h[5]}
	homicide_json['features'].append(feat)
	
# Check the format to make sure it's looking like we expect:
# print json.dumps(homicide_json, indent=4)

# Let's open a file and write all of it. Because JavaScript is a weird beast,
# we need to prefix our GeoJSON output with a "var <whatever> ="

with open('homicide.geojson', 'wb') as outfile:
	outfile.write('var homicide_points = ')
	json.dump(homicide_json, outfile)
	

# The next step's a little more complicated; we're going to parse an existing 
# GeoJSON file that shows all of Chicago's communities and add a property 
# to it. 

# First thing to do is load the GeoJSON

geojson_loc = 'comm_areas.geojson'
with open(geojson_loc, 'rb') as geojson_file:
	comm_areas = json.load(geojson_file)
	
# Let's also summon that long query from last time that calculates a violent 
# crime rate from the same data. Slight tweak: we're adding the column with
# community ID numbers.

viol_rate_sql = '''SELECT chicago_areas.comm_id, chicago_areas.comm_name, ROUND((crime_query.violent_crimes*1.0/chicago_areas.pop2010) * 10000,2) as rate
         FROM (
               SELECT community_area, COUNT(*) AS violent_crimes
               FROM week
               WHERE primary_type in ('HOMICIDE', 'CRIM SEXUAL ASSAULT', 'ROBBERY', 'ASSAULT', 'BATTERY')
               GROUP BY 1
               ) as crime_query, chicago_areas
         WHERE crime_query.community_area = chicago_areas.comm_id
         ORDER BY 3 DESC'''
         
c.execute(viol_rate_sql)
viol_rate = c.fetchall()

# Now we need to walk through the list of 'features' in our GeoJSON file, checking
# the community ID number against the community IDs in our violent crime list. If
# they match, we're going to insert a property called 'VC_RATE.'

for shape in comm_areas['features']:
	comm_id = int(shape['properties']['AREA_NUMBE'])
	for loc in viol_rate:
		if loc[0] == comm_id:
			shape['properties']['VC_RATE'] = loc[2]
			
with open('comm_area_plusrate.geojson', 'wb') as outfile:
	outfile.write('var comm = ')
	json.dump(comm_areas, outfile)

# Close the database when we're all done. 	
conn.close()
