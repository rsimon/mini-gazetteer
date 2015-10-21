# Mini-Gazetteer

Scripts for building a minimalistic gazetteer dataset from the following data sources:

* The [quattroshapes](https://github.com/foursquare/quattroshapes) GeoJSON gazetteer dump file is
  used as the 'master file'.
* The [GeoNames alternateNames](http://download.geonames.org/export/dump/) table is used to
  enrich quattroshapes records with additional names (and language codes, where available).

## Output Format

Generated output is a plaintext file that holds __one GeoJSON record per line__. The `id`
field holds the ID assigned in quattroshapes. The `properties` hold the corresponding
GeoNames ID (where included in the quattroshapes data) and an array of names. Names are
JavaScript objects which always contain a `label` field, and optionally a `lang` field.

Output is written to the `output` folder.

## Sample Record

```json
{  
  "type":"Feature",
  "id":"101037",
   "geometry":{  
      "type":"Point",
      "coordinates":[  
         16.37169,
         48.2082
      ]
   },
   "properties":{  
      "geonames_id":2761367,
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
      ],
      "label":"Wien"
   }
}
```
