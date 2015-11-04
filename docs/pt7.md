#### Unlocking data from databases

Most of the internet demands data in forms that play nicely with it — especially for visualization. JavaScript libraries that dynamically assemble charts, graphs and maps typically want something that looks a lot more like the JSON we got from the crime API over a CSV file or a database table. And that's OK, because it just gives Python another chance to shine.

We're going to write a few scripts that convert our crime data into [GeoJSON](http://geojson.org/), which is designed specifically to store geographic data like points, lines and polygons, as well as data that may be associated with those shapes.

From there, we're going to layer them on a very basic [Leaflet.js](http://leafletjs.com/) map that was hacked together from a few of their [tutorials](http://leafletjs.com/examples.html). 

Instead of having to load data into a GIS program like Esri's ArcGIS or the open-source QGIS and spend the time manually joining a table from a database to a shapefile and then exporting the whole affair to a web-friendly format, we'll handle it two ways.

First, we'll write a section of script so that Python will generate GeoJSON straight from a database table. We'll use a new data type, [```OrderedDict```](https://docs.python.org/2/library/collections.html#collections.OrderedDict), to store key/value pairs as well as the order in which they are added.

The next section of the Python script will process an existing GeoJSON polygon shapefile. It will check the ID of each polygon against an existing data set; if it finds a match, it will write new data into the shape.

The whole point here is that you can have Python acting as an autonomous data depot, pulling down new data from one side and sending it to update dynamic visualizations from the other.

We'll use the following files for this project:

- **to_json.py**: The script we'll write to make and alter GeoJSON files based on information in our existing crime.db.

- **chicago_crime.html**: An HTML file that contains JavaScript. It uses Leaflet.js to draw a map and other functions that are part of that library to incorporate GeoJSON files as map layers.

- **comm_areas.geojson**: A GeoJSON file that contains all of Chicago's community areas. This originally existed as an Esri shapefile but was converted to this format in QGIS; there are also command line tools available that can do this, like [ogr2ogr](http://www.gdal.org/ogr2ogr.html).

A finished version of the Python script is in **completed**. 