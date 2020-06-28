import requests
import json

def check_if_index_is_present(url):
    response = requests.request("GET", url, data="")
    json_data = json.loads(response.text)
    return json_data


if __name__ == "__main__":
    url = "http://localhost:9200/_template/search_engine_template/"
    response = requests.request("GET", url, data="")
    if(len(response.text)>2):
        print("1. Deleted template: search_engine_template")
        response_delete = requests.request("DELETE", url)
    payload = {
  "template": "hacker",
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "sinhalaLyricAnalyzer": {
            "type": "custom",
            "tokenizer": "icu_tokenizer",
            "filter": ["edgeNgram"],
            "char_filter": ["initialFilter"]
          }
        },
        "filter": {
          "edgeNgram": {
            "type": "edge_ngram",
            "min_gram": 2,
            "max_gram": 50,
            "side": "front"
          }
        },
        "char_filter": {
          "initialFilter": {
            "type": "mapping",
            "mappings": ". => \\u0020"
          }
        }
      }
    }
  },
  "mappings": {
    "_source": {
      "enabled": True
    },
    "properties": {
    "artist": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      },
      "analyzer": "sinhalaLyricAnalyzer",
      "search_analyzer": "standard"
    },
    "beat": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      }
    },
    "genre": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      },
      "analyzer": "sinhalaLyricAnalyzer",
      "search_analyzer": "standard"
    },
    "key": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      }
    },
    "lyric": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      },
      "analyzer": "sinhalaLyricAnalyzer",
      "search_analyzer": "standard"
    },
    "lyricWriter": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      },
      "analyzer": "sinhalaLyricAnalyzer",
      "search_analyzer": "standard"
    },
    "musicDirector": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      },
      "analyzer": "sinhalaLyricAnalyzer",
      "search_analyzer": "standard"
    },
    "shares": {
      "type": "long"
    },
    "songName": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      },
      "analyzer": "sinhalaLyricAnalyzer",
      "search_analyzer": "standard"
    },
    "url": {
      "type": "text",
      "fields": {
        "keyword": {
          "type": "keyword",
          "ignore_above": 256
        }
      }
    },
    "views":{
      "type":"integer",
      "fields":{
        "keyword":{
          "type": "keyword",
          "ignore_above":256
        }
      }
    }
  }
  }
}
    payload = json.dumps(payload)
    print(payload)
    headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
        }
    response = requests.request("PUT", url, data=payload, headers=headers)
    if (response.status_code == 200):
        print("2. Created a new template: search_engine_template")
    else:
        print(response.status_code )
    url = "http://localhost:9200/hacker"
    json_data = check_if_index_is_present(url)

    if(not 'error' in json_data):
        print("3. Deleted an index: hacker")
        response = requests.request("DELETE", url)

    response = requests.request("PUT", url)
    if (response.status_code == 200):
        print("4. Created an index: hacker")

    url = "http://localhost:9200/autocomplete/"
    json_data = check_if_index_is_present(url)

    if(not 'error' in json_data):
        print("5. Deleting index: autocomplete")
        response = requests.request("DELETE", url)

    payload = {
        "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "sinhalaAnalyzer": {
            "type": "custom",
            "tokenizer": "icu_tokenizer",
            "filter": [
              "edgeNgram"
            ]
          }
        },
        "filter": {
          "edgeNgram": {
            "type": "edge_ngram",
            "min_gram": 2,
            "max_gram": 50,
            "side": "front"
          }
        }
      }
    }
  },
      "mappings": {
        
          "properties" : {
            "title_suggest" : {
              "type" :     "completion",
              "analyzer" :  "standard",
              "search_analyzer" : "standard",
              "preserve_position_increments": False,
              "preserve_separators": False
            }
          }
        
      }
    }
    payload = json.dumps(payload)
    response = requests.request("PUT", url, data=payload, headers=headers)

    if(response.status_code==200):
        print("6. Created a new index: autocomplete")
    else:
        print(response.status_code)





