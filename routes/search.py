from flask import Blueprint,render_template,request,jsonify
import requests,json
from sinling import SinhalaTokenizer
from SinhalaStemming import sinhalaStemmer

tokenizer = SinhalaTokenizer()
st = sinhalaStemmer.stemmer()

# creating a Blueprint class
search_blueprint = Blueprint('search',__name__,template_folder="templates")
search_term = ""


headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
}

@search_blueprint.route("/",methods=['GET','POST'],endpoint='index')
def index():
    if request.method=='GET':
        res ={
	            'hits': {'total': 0, 'hits': []}
             }
        return render_template("index.html",res=res)
    elif request.method =='POST':
        if request.method == 'POST':
            print("-----------------Calling search Result----------")
            search_term = request.form["input"]
            print("Search Term:", search_term)
            nums = [int(i) for i in search_term.split() if i.isdigit()]
            # Sinhala tokenizer
            tokenized_string = ' '.join([str(word) for word in tokenizer.tokenize(search_term)])
            print(tokenized_string)
            # Manual stemming
            manual_stemmed_list = []
            for w in tokenizer.tokenize(search_term):
                if w[-2:]=="ගේ":
                    w = w[:-2]
                manual_stemmed_list.append(w)

            print(manual_stemmed_list)
            # Sinhala Stemmer
            bench_word_list, check_word_list = st.stemminig(  manual_stemmed_list)
            list_after_stemming = list(set(bench_word_list)- set(check_word_list))
            print(list_after_stemming)
            
            if len(list_after_stemming)>0:
                stemmed_string = ' '.join([str(word) for word in tokenizer.tokenize(search_term).extend(list_after_stemming)])
            else:
                stemmed_string = ' '.join([str(word) for word in manual_stemmed_list])

            modified_search_term = ' '.join([str(elem) for elem in stemmed_string.split('.')]) 
            print(modified_search_term)
            

            if len(nums)>0:
                print("num detected")
                payload = {
                    "query": {
    
                        "query_string": {
                            "analyze_wildcard": True,
                            "query": str(modified_search_term),
                            "fields": ["songName", "artist", "genre", "lyric"]
                        }
                    
                    },
                    "size": 50,
                    "sort": [{
                        "views": {
        "order": "desc"
        

      }

                     } ],
                     
  "aggs": {
    "genres": {
      "terms": {
        "field": "genre.keyword",
        "min_doc_count": 10,
        "order": {
          "_count": "desc"
        }
      }
    },
    "artists":{
      "terms": {
        "field": "artist.keyword",
        "min_doc_count": 10,
        "order": {
          "_count": "desc"
        }
      }
    }
  }
                }
            else:
                payload = {
                    "query": {
                        "query_string": {
                            "analyze_wildcard": True,
                            "query": str(modified_search_term),
                            "fields": ["songName", "artist", "genre", "lyric"]
                        }
                    },
                    "size": 50,
                    "sort": [

                    ],
                    
  "aggs": {
    "genres": {
      "terms": {
        "field": "genre.keyword",
        "min_doc_count": 10,
        "order": {
          "_count": "desc"
        }
      }
    },
    "artists":{
      "terms": {
        "field": "artist.keyword",
        "min_doc_count": 10,
        "order": {
          "_count": "desc"
        }
      }
    }
  }
                }
            payload = json.dumps(payload)
            url = "http://localhost:9200/hacker/_search"
            response = requests.request("GET", url, data=payload, headers=headers)
            response_dict_data = json.loads(str(response.text))
            print(response_dict_data)
            return render_template('index.html', res=response_dict_data)


@search_blueprint.route("/autocomplete",methods=['POST'],endpoint='autocomplete')
def autocomplete():
    if request.method == 'POST':
        search_term = request.form["input"]
        print("POST request called")
        print(search_term)
        payload ={
          "autocomplete" : {
            "text" : str(search_term),
            "completion" : {
              "field" : "title_suggest"
            }
          }
        }
        payload = json.dumps(payload)
        url="http://localhost:9200/autocomplete/_suggest"
        response = requests.request("GET", url, data=payload, headers=headers)
        response_dict_data = json.loads(str(response.text))
        return json.dumps(response_dict_data)




