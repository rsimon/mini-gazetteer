import json

def enc(str):
    return str.encode('utf8').replace('"', '\\"')

with open('output/places.json.txt') as f:
    outfile = open('output/places.pelagios.ttl', 'w')

    outfile.write('@base <http://github.com/rsimon/mini-gazetteer> .\n')
    outfile.write('@prefix : <http://github.com/rsimon/mini-gazetteer> .\n')
    outfile.write('@prefix dcterms: <http://purl.org/dc/terms/> .\n')
    outfile.write('@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n')
    outfile.write('@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .\n')
    outfile.write('@prefix geosparql: <http://www.opengis.net/ont/geosparql#> .\n')
    outfile.write('@prefix lawd: <http://lawd.info/ontology/> .\n')
    outfile.write('@prefix osgeo: <http://data.ordnancesurvey.co.uk/ontology/geometry/> .\n')
    outfile.write('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n')
    outfile.write('@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n')
    outfile.write('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n')

    for line in f.readlines():
        place = json.loads(line)
        props = place['properties']

        if props['label']:
            if 'geonames_id' in props:
                outfile.write('<http://sws.geonames.org/' + str(props['geonames_id']) + '> a lawd:Place ;\n')
            else:
                outfile.write(':' + place['id'] + '> a lawd:Place ;\n')

            # Label
            outfile.write('  rdfs:label "' + enc(props['label']) + '" ;\n')

            # Names
            if 'names' in props:
                for name in props['names']:
                    if 'lang' in name and len(name['lang']) < 4:
                        outfile.write('  lawd:hasName [ lawd:primaryForm "' + enc(name['label']) + '"@' + enc(name['lang']) + ' ] ;\n')
                    else:
                        outfile.write('  lawd:hasName [ lawd:primaryForm "' + enc(name['label']) + '" ] ;\n')

            # Geometry
            outfile.write('  geosparql:hasGeometry [\n')
            outfile.write('    osgeo:asGeoJSON "' + json.dumps(place['geometry']).replace('"', '\\"') + '" ;\n')
            outfile.write('  ] ;\n')

            outfile.write('  .\n\n')

    outfile.close()
