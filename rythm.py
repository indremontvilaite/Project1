import pronouncing

class Rythm(object):
    def get_rythm(self, input_words):
        answer = []
        for i in input_words:
            answer.append(pronouncing.rhymes(i))
        return answer
