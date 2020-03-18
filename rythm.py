import pronouncing
import copy
import itertools

print(pronouncing.rhymes("climbing"))


class Rythm(object):
        
    def get_rythm(self, input_words):
        answer = []
        for i in input_words:
            print(i)
            answer.append(pronouncing.rhymes(i))
        return answer
b=["one", "two"]
a=copy.deepcopy(Rythm().get_rythm(b))
print(a)