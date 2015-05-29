# PROBLEM: We need coordinates for the addresses we parsed earlier.
#
# HOW WE'RE GOING TO DEAL WITH IT:
#   - Use a library called geopy to run an address through Google's geocoder
#   - Use a sleep function to pause so we don't swamp Google
#   - Keep track of it all with a keyed dictionary (coming in and going out)
#   - Put the original information AND our returned lat/long coordinates into a
#     new csv file

# Import the Google geocoder from geopy as well as Python's csv and time libaries
from geopy.geocoders import GoogleV3
import csv
import time

# Make a geolocator object
geolocator = GoogleV3()

# Open our address file and start a DictReader object that will give each element in
# each row a key/value pair based on the header columns in the file.
address_file = open('payday_lenders.csv', 'rb')
input = csv.DictReader(address_file)

# We'll go ahead and set up a new file for our eventual output.
geocoded_file = open('payday_geocoded.csv', 'wb')
# For the DictWriter, we have to give it a list of fields from the get-go to establish
# the order; we'll go ahead and write a header to the file, too.
output_fields = ['NAME', 'DBA', 'STADDR', 'STADDR2', 'CITY', 'STATE', 'ZIP', 'MATCH_ADDR', 'LAT_Y', 'LONG_X']
output = csv.DictWriter(geocoded_file, output_fields)
output.writeheader()

# Start for loop here
for row in input:
    # We're going to put an if/else here to prevent the whole class from launching a
    # volley of 500 requests at Google. Let's get the first five (row 1 is the header).
    if input.line_num <= 6:
        # Put the address in a Google-recognizable string: ADDRESS, CITY, STATE ZIP
        addr = (row['STADDR']+' '+row['STADDR2']).strip()+', '+row['CITY']+', '+row['STATE']+' '+row['ZIP']
        # Geocode that string
        location = geolocator.geocode(addr)
        # Plug results from the geocoder right back into the same row of data with new key
        # values: the returned latitude, longitude and address Google matched on.
        row['LAT_Y'] = location.latitude
        row['LONG_X'] = location.longitude
        row['MATCH_ADDR'] = location.address
        # Write the modified row to our new csv.
        output.writerow(row)
        # To keep tabs on what's happening, get a printed message with address and line.
        print 'Attempted geocode of '+addr+', row '+str(input.line_num)
        # Before we do all of this with the next row, pause for two seconds.
        time.sleep(2)
    else:
        break

# Alert us with a printed message when this completes and close both files.
print 'All done!'
address_file.close()
geocoded_file.close()
