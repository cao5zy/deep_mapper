**deep_mapper**
# Introduction
could be used to turn one py-object (mash of dicts / lists etc) into another one,
using deep mapping structure and postprocessing through custom functions / builtins

mapping structure example


    {
        'name': {
            'path': '/title'
        },
        'time': {
            'path': '/runtime',
            'postprocess': int
        },
        'restrictions': {
            'path': '/age_restricted'
        },
        'tags': {
            'path': '/tags/tag'
        },
        'image': {
            'path': '/gallery/image/@href'
        },
        'methods': {
            'path': '/mds',
            'sub_mapping': {
                'name': { 'path': '/title'},
                'num': { 'path': '/age'}
            }
        }
    }


all pathes need to be based on XPath rules.   
`sub_mapping` is used to map the object in the list. Please take a look at [test_arry_mapping](deep_mapper/tests/test_arry_mapping.py) for more details.  

# Installation
available from pip (python3):

``pip install deep_mapper``

# Examples
## Convert from a simple dict object
Source Data
```
DATA = {
    "name": "alan",
    "ID": "2q212121"
}
```
Map structure
```
MAP_STRUCTURE = {
    "title": { "path": "/name"},
    "id": { "path": "/id" }
}
```
Do mapping
```
from deep_mapper import process_mapping

result = process_mapping(DATA, MAP_STRUCTURE, "/")
```
Result
```
{
    "title": "alan",
    "id": "2q212121"
}
```

## Convert from a simple dict that contains an array
