# Make sure you have elastic search up and running locally on http://localhost:9200/

from datetime import datetime
from elasticsearch import Elasticsearch
import json
with open('ss.json', encoding='utf-8') as fh:
    data = json.load(fh)

print(type(data))

es = Elasticsearch()

for i in range(len(data)):
    doc = data[i]
    res = es.index(index="hacker", id=i, body=doc)
    print(res['result'])

    res = es.get(index="hacker", id=i)
    print(res['_source'])

    es.indices.refresh(index="hacker")

    res = es.search(index="hacker", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total']['value'])
    for hit in res['hits']['hits']:
        print("%(songName)s %(artist)s: %(views)s" % hit["_source"])
