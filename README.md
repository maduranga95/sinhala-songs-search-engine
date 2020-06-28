
# sinhala-songs-search-engine

[![](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/maduranga95/sinhala-songs-search-engine/blob/master/LICENSE)

Search engine to retrieve sinhala songs and metadata of sinhala songs using Elasticsearch, Python and Flask.

## Prerequisites

1. Elasticsearch running locally on http://localhost:9200/ (additionally you may have Kibana running on http://localhost:5601/ )
```
> Check here for additional information on downloading and running above instances. (https://www.elastic.co/downloads/)
```
2. Python 3.x  installed with pip version 3

## Getting Started
1.  Install required python packages by running the following command in the project home directory.
  `pip install -r requirements.txt`
2. Then run `create_new_index.py` ( This will create a template and relevant indexes on Elasticsearch which is already up and running )
3. After that if you are posting the sinhala song data using the json file provided, you can run `es_doc_post.py` to post the documents to the index created.
4. Then run `app.py` to run the Flask app with the front end. 
5. Visit [http://localhost:8005/](http://localhost:8005/) to view the Sinhala Song Search Engine.

## Screenshots

![Screenshot 1](/Screenshots/ss1.jpg?raw=true "Search")

![Screenshot 2](/Screenshots/ss2.jpg?raw=true "Search results")

## Note
**Please go through [SinhalaStemmer.md](https://github.com/maduranga95/sinhala-songs-search-engine/blob/master/SinhalaStemmer.md), [SinhalaTokenizer.md](https://github.com/maduranga95/sinhala-songs-search-engine/blob/master/SinhalaTokenizer.md) and [Scraper.md](https://github.com/maduranga95/sinhala-songs-search-engine/blob/master/Scraper.md) for more details on Stemmer, Tokenizer and Scraper.**