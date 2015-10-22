# Mini-Gazetteer

Scripts for building a minimalistic gazetteer dataset from the following data sources:

* The [quattroshapes](https://github.com/foursquare/quattroshapes) GeoJSON gazetteer dump file is
  used as the 'master file'.
* The [GeoNames alternateNames](http://download.geonames.org/export/dump/) table is used to
  enrich quattroshapes records with additional names (and language codes, where provided).

If you're on Linux, and have the usual complement of tools and helpers installed (wget, gunzip,
unzip, python) you can try running the `./buildGazetteer` script. This will download the source
data and do the conversion all in one step.

## Output Format

Generated output is a plaintext file that holds __one GeoJSON record per line__. The `id`
field holds the ID assigned in quattroshapes. The `properties` hold:

* a label (the value recorded in quattroshapes as _local name_ or _name_)
* an ISO country code
* the corresponding GeoNames ID (where included in the quattroshapes data)
* the GeoNames population count
* an array of names - names are JSON objects which always contain a `label` field,
  and optionally a `lang` field.

Output is written to the `output` folder.

## Sample Record

```json
{  
  "id":"101037",
  "type":"Feature",
   "geometry":{  
      "type":"Point",
      "coordinates":[  
         16.37169,
         48.2082
      ]
   },
   "properties":{  
      "label":"Wien",
      "country":"AT",
      "geonames_id":2761367,
      "geonames_population":1569316,
      "names":[  
         {  
            "lang":"en",
            "label":"Vienna"
         },
         {  
            "lang":"es",
            "label":"Viena"
         },
         {  
            "lang":"de",
            "label":"Wien"
         },
         {  
            "lang":"fr",
            "label":"Vienne"
         },
         {  
            "lang":"ca",
            "label":"Viena"
         },
         {  
            "lang":"sv",
            "label":"Wien"
         },
         {  
            "lang":"no",
            "label":"Wien"
         },
         {  
            "lang":"pl",
            "label":"Wiede\u0144"
         },
         {  
            "lang":"it",
            "label":"Vienna"
         },
         {  
            "lang":"pt",
            "label":"Viana"
         },
         {  
            "lang":"ru",
            "label":"\u0412\u0435\u043d\u0430"
         },
         {  
            "lang":"cs",
            "label":"V\u00edde\u0148"
         }
      ]
   }
}
```
## Running the Conversion Outside of .buildGazetteer

This repository does not include the source data. (It's big...) If the `./buildGazetteer` script
doesn't work for you, download the data from quattroshapes and GeoNames into the `source-data`
folder yourself first (instructions are [here](https://github.com/rsimon/mini-gazetteer/blob/master/source-data/README.md)).
Uncompress the files and run `python convertSourceData.py`. Done.

## And What Now?

Once you have the data file, one thing you may want to do with it is to set up an HTTP
search endpoint. An ultra-quick solution to achieve this is to download and install the
Open Source search server [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/guide/current/_installing_elasticsearch.html),
and use a nifty command-line utility called [stream2es](https://github.com/elastic/stream2es) to
batch-index the file. If you're on Linux, the command should look something like this:

`cat places.json.txt | stream2es stdin --target http://localhost:9200/gazetteer/place`

Minutes later, you'll have a fully searchable index you can query like so:

[http://localhost:9200/gazetteer/_search?q=label:Wien&sort=geonames_population:desc&pretty](http://localhost:9200/gazetteer/_search?q=label:Wien&sort=geonames_population:desc&pretty)

## License Info

Really not much to license here, except for a few lines of Python code. But consider things
[MIT-licensed](https://raw.githubusercontent.com/rsimon/mini-gazetteer/master/MIT-License.txt).

The source data is licensed separately, but not included in this repository. (For info:
quattroshapes is released by [foursquare](https://github.com/foursquare) under
[CC-BY 2.0](http://creativecommons.org/licenses/by/2.0/) attribution license. GeoNames data
is released under [CC-BY 3.0](http://creativecommons.org/licenses/by/3.0/) attribution license.)
