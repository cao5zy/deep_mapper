**deep_mapper**

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
                'name': '/title',
                'num': '/age'
            }
        }
    }


all pathes need to be based on XPath rules.   
`sub_mapping` is used to map the object in the list. Please take a look at [test_arry_mapping](tests/test_arry_mapping.py) for more details.  

available from pip (python3):

``pip install deep_mapper``
