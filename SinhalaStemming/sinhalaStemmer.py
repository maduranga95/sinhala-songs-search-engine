import io


class stemmer():

    def stemminig(self, doc):


        suffFileDirec = "suffixes.txt"
        try:
            suffixFile = io.open(suffFileDirec, "r", encoding='utf-8').read()
        except UnicodeDecodeError:
            suffixFile = io.open(suffFileDirec, "r", encoding='latin-1').read()

        suffixList = suffixFile.split()

        doc.sort()
        wordList = doc
        stemmer_benchwords = []
        stemmer_checkwords =[]
        i = 0
        while (i < len(wordList) - 1):
            j = i + 1

            while (j < len(wordList)):

                benchWord = wordList[i]
                checkWord = wordList[j]
                benchCharList = list(benchWord)
                checkCharList = list(checkWord)

                if (checkWord.startswith(benchWord)):
                    for suffix in suffixList:
                        if checkWord.endswith(suffix):
                            print(benchWord+" = "+checkWord)
                            stemmer_benchwords.append(benchWord)
                            stemmer_checkwords.append(checkWord)
                            wordList[j] = benchWord
                            break
                j += 1
            i += 1
        return stemmer_benchwords, stemmer_checkwords

#st = stemmer()
#bench_word_list, check_word_list = st.stemminig( [" සුදුයන්"," සුදුයන්දේ", "මැණිකයන්දේ", "මැණිකයන්"])
#print(bench_word_list, check_word_list)
