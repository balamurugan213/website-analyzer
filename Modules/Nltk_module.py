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
        bi=bifreq.most_common(10)
        li_key=[]
        for u in bi:
            a=u[0][0]
            b=u[0][1]
            c=a+b
            li_key.append(c)
        print(li_key)
        return(li_key)
    
    def FindUnigrams(self):
        unigrams=[]
        for text in self.inp:
            tokens = nltk.word_tokenize(text)
            i=list(nltk.ngrams(tokens, n=1))
            unigrams=unigrams + i
        # eng_bifreq = nltk.FreqDist(bigrams)
        # print(eng_bifreq)
        # print(unigrams)
        bifreq = nltk.FreqDist(unigrams)
        un=bifreq.most_common(10)
        li_key=[]
        for u in un:
            a=u[0][0]
            li_key.append(a)
            print('\n')
        return(li_key)