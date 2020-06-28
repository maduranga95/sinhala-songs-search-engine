As sinhala tokenizer https://github.com/ysenarath/sinling is used here.

# SinLing 
A language processing tool for Sinhalese (සිංහල). 

`Update 2019.07.21: This tool no longer requires java to run sinhala tokenizer. 
All java code is ported to Python implementation for convenience.`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ysenarath/sinling/37fbcbaef51f0ff87ea9dcca4617ff427f7d34ce)


## How to get started
Steps-
1. Create new folder named `bin` in root path
1. Download [`stat.split.pickle`](https://github.com/ysenarath/sinling/releases/download/v0.1-alpha/stat.split.pickle) to the `bin` folder
1. Import required tools from the `sinling` module in your desired project 
(you have to append this project path to your path environment variable. Append the path of the root of sinling project to the PATH variable in System Variables. The way this is done diffres by operating system.)



## How to use
### Sinhala Tokenizer
```python
from sinling import SinhalaTokenizer

tokenizer = SinhalaTokenizer()

sentence = '...'  # your sentence

tokenizer.tokenize(sentence)
```

Sinhala tokenizer also includes `tokenizer.split_sentences(...)` function for splitting sentences.