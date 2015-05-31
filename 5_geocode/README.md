# 5_geocode

For any kind of analysis that involves mapping, having coordinates is a must. En masse, though, they aren't always easy to come by.

Open-source geographic information systems like [QGIS](http://www.qgis.org) don't have built-in options to figure out a location's latitude and longitude; [Esri](http://www.esri.com/software/arcgis/arcgisonline/credits) charges for some of its online geocoding services, too.

Enter [geopy](https://github.com/geopy/geopy), a Python library that's designed to interact with a slew of third-party geolocation APIs. As part of a larger script, we can read lines of address data from a CSV file, send each through one of these services and return the results.

In this example, we'll be using Google's geocoding service, which is good at properly interpreting an address string even when it's partially malformed or contains extraneous information. As a free service, however, it will only geocode 2,500 addresses in a 24-hour period.

We'll be using the CSV file we made by parsing payday lender addresses from 3\_parse\_addresses. Our goal at the end is to have a new CSV file with three additional fields of information:

- Google's match for the address
- Latitude in decimal degrees (Y coordinate)
- Longitude in decimal degrees (X coordinate)

Google's free geocoder can only handle five requests per second, so we're going to use Python's time functions to slow our requests down and set up a control flow so that we're all only geocoding the first five addresses -- a condition that can be removed at your discretion if you're working through this task on your own later.

This exercise contains three files:

- **geocode.py**: A script we'll write to pass addresses through Google's geocoding service. It will take the results along with our initial data fields and send them all to a new CSV file.

- **payday_lenders.csv**: Our completed CSV file from 3\_parse\_addresses.

- **geocode_done.py**: A completed and working version of **geocode.py**.