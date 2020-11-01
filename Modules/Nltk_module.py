from nltk.corpus import genesis
import nltk
# nltk.download()

class BigramModule:
    inp=[]
    def __init__(self,words):
        self.inp = words
    
    def FindBigrams(self):
        bigrams=[]
        for text in self.inp:
            tokens = nltk.word_tokenize(text)
            bi=list(nltk.bigrams(tokens))
            bigrams=bigrams + bi
        # eng_bifreq = nltk.FreqDist(bigrams)
        # print(eng_bifreq)
        print(bigrams)
        bifreq = nltk.FreqDist(bigrams)
        print(bifreq.most_common(10))
        return(bifreq.most_common(10))
    
    def FindUnigrams(self):
        unigrams=[]
        for text in self.inp:
            tokens = nltk.word_tokenize(text)
            i=list(nltk.ngrams(tokens, n=1))
            unigrams=unigrams + i
        # eng_bifreq = nltk.FreqDist(bigrams)
        # print(eng_bifreq)
        print(unigrams)
        bifreq = nltk.FreqDist(unigrams)
        print(bifreq.most_common(10))
        return(bifreq.most_common(10))