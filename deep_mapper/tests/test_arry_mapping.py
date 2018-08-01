import deep_mapper
from assertpy import assert_that

DATA = {
    "mds": [{"name": "alan"}]
}

def test_arry_mapping():
    MAP_STRUCTURE = {
        "methods": {"path": "/mds",
                    "sub_mapping": {
                        "title": {"path": "/name"}
                    }
        }
    }

    result = deep_mapper.process_mapping(DATA, MAP_STRUCTURE, "/")    
    assert_that(result).contains_key('methods')
    assert_that(result["methods"][0]).contains_entry({"title": "alan"})
