# PROBLEM: We need coordinates for the addresses we parsed earlier.
#
# HOW WE'RE GOING TO DEAL WITH IT:
#   - Use a library called geopy to run an address through Google's geocoder
#   - Use a sleep function to pause so we don't swamp Google
#   - Keep track of it all with a keyed dictionary (coming in and going out)
#   - Put the original information AND our returned lat/long coordinates into a
#     new csv file

# Import the Google geocoder from geopy as well as Python's csv and time libaries


# Make a geolocator object


# Open our address file and start a DictReader object that will give each element in
# each row a key/value pair based on the header columns in the file.


# We'll go ahead and set up a new file for our eventual output.

# For the DictWriter, we have to give it a list of fields from the get-go to establish
# the order; we'll go ahead and write a header to the file, too.



# Start for loop here

    # We're going to put an if/else here to prevent the whole class from launching a
    # volley of 500 requests at Google. Let's get the first five (row 1 is the header).

        # Put the address in a Google-recognizable string: ADDRESS, CITY, STATE ZIP

        # Geocode that string

        # Plug results from the geocoder right back into the same row of data with new key
        # values: the returned latitude, longitude and address Google matched on.



        # Write the modified row to our new csv.

        # To keep tabs on what's happening, get a printed message with address and line.

        # Before we do all of this with the next row, pause for two seconds.




# Alert us with a printed message when this completes and close both files.
