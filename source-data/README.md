# Source data

This repository does not include the source data.

Please grab your own copies of the two necessary data files here:

* The __quatroshapes gazetteer file__ (gzipped geojson version, named
  `quattroshapes_gazetteer_gn_then_gp.gz` from
  [here](https://github.com/foursquare/quattroshapes#goodies). Uncompress the file into
  this (`source-data`) folder.
* The GeoNames __alternateNames.zip__ file, available from the
  [Geonames Dump site](http://download.geonames.org/export/dump/). Unzip the file into this
  folder.

That's it. Change to the project root folder and run `python convertSourceData.py`
