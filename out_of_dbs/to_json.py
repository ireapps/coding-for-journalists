#! usr/bin/python

# Now that we've processed JSON, moved into into a database an set up some helpful 
# prewritten queries for new records, we're going to talk about the flip side of that: 
# exporting data to JSON for use elsewhere.

import sqlite3
import json
import collections

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
# 		"geometry": {"type": "Point", "coordinates": [<LAT>, <LONG>]},
#         "properties": {"<PROPNAME>": "<PROPVALUE>"}
#         },
# 		{ "type": "Feature",
#         <...>
#         }
#     ]
# }

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
print json.dumps(homicide_json, indent=4)

