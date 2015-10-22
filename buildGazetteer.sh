echo "Dowloading quattroshape data file..."
wget http://static.quattroshapes.com/quattroshapes_gazetteer_gn_then_gp.gz -P source-data
echo "Dowloading alternate names from GeoNames..."
wget http://download.geonames.org/export/dump/alternateNames.zip -P source-data
echo "Uncompressing..."
gunzip -c source-data/quattroshapes_gazetteer_gn_then_gp.gz > source-data/quattroshapes_gazetteer_gn_then_gp.shp.json
unzip source-data/alternateNames.zip -d source-data
python convertSourceData.py
