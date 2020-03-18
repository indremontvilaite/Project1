import pronouncing
print(pronouncing.rhymes("climbing"))

class Rythm(object):

    def __init__(self, input_words):
        self.input_words=input_words
        
    def get_rythm(self):
        answer = []
        for i in input_words:
           answer.append.pronouncing.rhymes(i)
        return answer
