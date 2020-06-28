As sinhala stemmer https://github.com/e11379dana/SinhalaStemming.git is used here.

# SinhalaStemming
A simple stemming tool for Sinhalese (සිංහල). 


## How to get started
Steps-
1. Clone the repository using [`git clone  stemmerhttps://github.com/e11379dana/SinhalaStemming.git`]
2. Cut and paste [`suffixes.txt`] to the root of sinhala-songs-search-engine project.
3. Use the stemmer in [`routes/search.py`]




## How to use
### Sinhala Stemmer

In [`routes/search.py`]

```python
from SinhalaStemming import sinhalaStemmer

st = sinhalaStemmer.stemmer()

sentence = '...'  # your sentence

bench_word_list, check_word_list = st.stemminig(tokenizer.tokenize(sentence))
```

Note : The stemmer used is not perfect, so there can be faults in the sinhala bench words selected.
