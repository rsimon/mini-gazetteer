import csv
import json

# Global lookup table for GeoNames alternateNames
altNames = {}

# Shorthand to add a single altName to the lookup table
def addAltName(gnId, lang, name):
    altName = { 'label': name }

    if lang:
        altName['lang'] = lang

    if gnId in altNames:
        altNames[gnId].append(altName)
    else:
        altNames[gnId] = [ altName ]

# Load altNames
with open('source-data/alternateNames.txt', 'r') as n:
    print('Parsing GeoNames alternateNames.txt...')

    names = csv.reader(n, delimiter='\t')

    for row in names:
        gnId = row[1]
        lang = row[2]
        altName = row[3]

        if lang != 'link':
            addAltName(gnId, lang, altName)

    n.close()
    print('Done. Got alternate names for ' + str(len(altNames)) + ' GeoNames places.')

# Load quattroshapes GoeJSON dump
with open('source-data/quattroshapes_gazetteer_gn_then_gp.shp.json', 'r') as g, \
     open('output/places.json.txt', 'w') as outfile:

    print('Loading quattroshapes GeoJSON...')
    places = json.load(g)

    ctr = 0

    print('Done. Converting places...')
    for feature in places['features']:

        # Skip places without geometry
        if feature['geometry']:
            ctr += 1

            props = feature['properties']

            place = {
                'type': 'Feature',
                 'id': feature['id'],
                 'geometry': feature['geometry'],
                 'properties': {
                     'country': props['iso']
                 }
            }

            if 'gn_id' in props:
                gnId = props['gn_id']
                place['properties']['geonames_id']= gnId

                if str(gnId) in altNames:
                    place['properties']['names'] = altNames[str(gnId)]

            if 'name_local' in props:
                place['properties']['label'] = props['name_local']
            elif 'name' in props:
                place['properties']['label'] = props['name']
            else:
                print('Warning: unnamed place ' + json.dumps(props))

            if 'gn_pop' in props:
                place['properties']['geonames_population'] = props['gn_pop']

            outfile.write(json.dumps(place) + '\n')

    outfile.close()
    g.close()

print('Done. Wrote ' + str(ctr) + ' GeoJSON features.')
