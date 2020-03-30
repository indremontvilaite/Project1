import random
import sys
from googletrans import Translator
import pronouncing
import itertools
import nltk
import copy
import user_input
import synonims
import rythm

def min_max(w_length):
        if w_length.capitalize() == 'A':
            minimum = 2
            maximum = 7
        elif w_length.capitalize() == 'B':
            minimum = 6
            maximum = 13
        else:
            minimum = 12
            maximum = 99
        return [minimum, maximum]  

def read_dict_file(filename):
    with open(filename, 'r') as r:
        lines = r.read().strip().lower().split('\n')
    return lines

class Startup_name():
    def __init__(self, k_words, w_length, w_style, w_type, k_synonims, min_max):
        self.k_words = k_words
        self.w_length = w_length
        self.w_style = w_style
        self.w_type = w_type
        self.k_synonims = k_synonims
        self.minimum = min_max[0]
        self.maximum = min_max[1]

    def set_length(self, text_list, minimum, maximum):
        double = [x for x in text_list if minimum < len(x) < maximum]
        return double

    def misspell(self):
        answer = []
        for i in self.k_words:
            if len(i) >= 4:
                start = random.randint(1,len(i) - 3)
                stop = start + 2
                f,s = i[start:stop]
                i[start:stop] = s,f
            
            elif len(i) >=5:
                start = random.randint(1,len(i) - 4)
                stop = start + 2
                f,s = i[start:stop]
                i[start:stop] = s,f
            
            answer.append(i)
        return answer

    def give_names(self):
        answer = []
        if self.w_style == 1:
            names = self.set_length(names_db, self.minimum, self.maximum)
            for i in range(self.w_type):
                answer.append(random.choice(names))
        elif self.w_style == 2:
            a = copy.deepcopy(rythm.Rythm().get_rythm(self.k_words))
            b = list(itertools.chain.from_iterable(a))
            answer0 = [
                random.choice(
                    self.set_length(
                        b,
                        self.minimum,
                        self.maximum)) for i in range(
                    self.w_type)]
            if len(answer0)> self.w_type:
                answer = answer0[:self.w_type]
            else:
                answer = answer0
        elif self.w_style == 3:
            synonim = self.set_length(self.k_synonims, self.minimum, self.maximum)
            if len(synonim)< self.w_type:
                words = self.set_length(words_db, self.minimum, self.maximum)
                synonim.append(words[:self.w_type])
            for i in range(self.w_type):
                answer.append(random.choice(synonim))
        elif self.w_style == 4:
            translator = Translator()
            for w in k_words:
                destination = ['lt', 'ja', 'fr', 'eo']
                for d in destination:
                    foreign = translator.translate(w, dest=d, src='en')
                    answer.append(foreign.text)
        elif self.w_style == 5:
            words = self.set_length(words_db, int(
                self.minimum / 2), int(self.maximum / 2))
            for i in range(w_type):
                answer.append(random.choice(words) + random.choice(words))
        elif self.w_style == 6:
            answer0 = self.set_length(self.misspell(),self.minimum, self.maximum)
            if len(answer0) < self.w_type:
                answer = copy.deepcopy(answer0)
                words = self.set_length(words_db,self.minimum, self.maximum)
                for i in range(self.w_type - len(answer0)):
                    answer.append(random.choice(words))
            elif len(answer0) == self.w_type:
                answer = copy.deepcopy(answer0)
            else:
                for i in range(self.w_type):
                    answer.append(random.choice(answer0))
        return answer
    

if __name__ == '__main__':
    print('Welcome! Find the name for your very new Startup\n Have no ideas? Let us help you!')
    print('Choosing a name can be fun and easy!')
    print('Get names ideas regarding your preferences\nLet\'s answer some question\'s')
    k_words=user_input.InputList.get_k_words()
    k_synonims=synonims.Synonims(k_words).get_synonims()
    w_length=user_input.get_length()
    w_style=user_input.get_style()
    w_type=user_input.get_number()
    min_max = min_max(w_length)
    names_db = read_dict_file("first_names.txt")
    words_db = read_dict_file("usa.txt")
    suggestions = Startup_name(k_words, w_length, w_style, w_type, k_synonims, min_max).give_names()
    print('1,2,3 - be ready!')
    print('Your Startup can be named:')
    for name in suggestions:
        print(name.capitalize())
    print('I hope you have find something you like!\nIf not, let`s try again')
