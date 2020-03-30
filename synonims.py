import itertools
import nltk
from nltk.corpus import wordnet

class Synonims:
    def __init__(self, input_list):
        self.input_list = input_list
    def get_synonims(self):
        a = []
        for i in self.input_list:
            for syn in wordnet.synsets(i):
                for l in syn.lemmas():
                    a.append(l.name())
        return a
