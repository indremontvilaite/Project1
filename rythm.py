import pronouncing
import copy
import itertools
import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet


print(pronouncing.rhymes("climbing"))


class Rythm(object):
        
    def get_rythm(self, input_words):
        answer = []
        for i in input_words:
            print(i)
            answer.append(pronouncing.rhymes(i))
        return answer
b=["one"]
a=copy.deepcopy(Rythm().get_rythm(b))
#print(a)

syns = wordnet.synsets("dog")
#print(syns)