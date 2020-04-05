import random
import sys
from googletrans import Translator
import itertools
import nltk
import copy
import user_input
import synonims
import rythm
import read_file
import os
from airtable import Airtable


class StartupName:
    def __init__(self, k_words, w_length, w_type, k_synonims, min_max):
        self.k_words = k_words
        self.w_length = w_length
        self.w_type = w_type
        self.k_synonims = k_synonims
        self.minimum = min_max[0]
        self.maximum = min_max[1]
        self.answer = []

    def set_length(self, text_list, minimum, maximum):
        double = [x for x in text_list if minimum < len(x) < maximum]
        return double

    def misspell(self):
        answer = []
        for i in self.k_words:
            if len(i) >= 4:
                start = random.randint(1, len(i) - 3)
                stop = start + 2
                f, s = i[start:stop]
                i[start:stop] = s, f

            elif len(i) >= 5:
                start = random.randint(1, len(i) - 4)
                stop = start + 2
                f, s = i[start:stop]
                i[start:stop] = s, f

            answer.append(i)
        return answer

    def style_one(self):
        names = self.set_length(names_db, self.minimum, self.maximum)
        for i in range(self.w_type):
            self.answer.append(random.choice(names))
        return self.answer

    def style_two(self):
        a = copy.deepcopy(rythm.Rythm().get_rythm(self.k_words))
        b = list(itertools.chain.from_iterable(a))
        answer0 = [
            random.choice(self.set_length(b, self.minimum, self.maximum))
            for i in range(self.w_type)
        ]
        if len(answer0) > self.w_type:
            self.answer = answer0[: self.w_type]
        else:
            self.answer = answer0
        return self.answer

    def style_three(self):
        synonim = self.set_length(self.k_synonims, self.minimum, self.maximum)
        if len(synonim) < self.w_type:
            words = self.set_length(words_db, self.minimum, self.maximum)
            synonim.append(words[: self.w_type])
        for i in range(self.w_type):
            self.answer.append(random.choice(synonim))
        return self.answer

    def style_four(self):
        translator = Translator()
        for w in k_words:
            destination = ["lt", "ja", "fr", "eo"]
            for d in destination:
                foreign = translator.translate(w, dest=d, src="en")
                self.answer.append(foreign.text)
        return self.answer

    def style_five(self):
        words = self.set_length(words_db, int(self.minimum / 2), int(self.maximum / 2))
        for i in range(w_type):
            self.answer.append(random.choice(words) + random.choice(words))
        return self.answer

    def style_six(self):
        answer0 = self.set_length(self.misspell(), self.minimum, self.maximum)
        if len(answer0) < self.w_type:
            self.answer = copy.deepcopy(answer0)
            words = self.set_length(words_db, self.minimum, self.maximum)
            for i in range(self.w_type - len(answer0)):
                self.answer.append(random.choice(words))
        elif len(answer0) == self.w_type:
            self.answer = copy.deepcopy(answer0)
        else:
            for i in range(self.w_type):
                self.answer.append(random.choice(answer0))
        return self.answer


if __name__ == "__main__":
    base_key = "appo5iwkTjYewQoES"
    table_name = "Table_1"
    airtable = Airtable(base_key, table_name, api_key="keyVkc0FhNAX0ct8o")
    styles = airtable.get_all(fields="Style", sort="Style")

    print(
        "Welcome! Find the name for your very new Startup\n Have no ideas? Let us help you!"
    )
    print("Choosing a name can be fun and easy!")
    print("Get names ideas regarding your preferences\nLet's answer some question's")

    k_words = user_input.InputList.get_k_words()
    k_synonims = synonims.Synonims(k_words).get_synonims()
    w_length = user_input.get_length()
    w_style = user_input.get_style(styles)
    w_type = user_input.get_number()
    min_max = read_file.min_max(w_length)
    names_db = read_file.read_dict_file("first_names.txt")
    words_db = read_file.read_dict_file("usa.txt")

    startup_name = StartupName(k_words, w_length, w_type, k_synonims, min_max)

    styles_functions = {
        1: startup_name.style_one,
        2: startup_name.style_two,
        3: startup_name.style_three,
        4: startup_name.style_four,
        5: startup_name.style_five,
        6: startup_name.style_six,
    }

    suggestions = styles_functions[w_style]()

    print("1,2,3 - be ready!")
    print("Your Startup can be named:")
    for name in suggestions:
        print(name.capitalize())
    print("I hope you have find something you like!\nIf not, let`s try again")
