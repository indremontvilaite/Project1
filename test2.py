import random
import sys
from googletrans import Translator

print('Welcome! Find the name for your very new Startup\n Have no ideas? Let us help you!')
print('Choosing a name can be fun and easy!')
print('Get names ideas regarding your preferences\nLet\'s answer some question\'s')

def get_k_words():
    while True:
        k_words = input('Enter key words about your Startup:\n')
        if len(k_words) < 1:
            k_words = input('No entry, please enter some words: ')
        else:
            k_list = k_words.split()
            print('Thanks for the key words')
            break
    return k_list

max_number = 7

def get_length():
    answers = ('A', 'B', 'C', 'D','E')
    n_length = ''
    while True:
        n_length = input('Select a name length by writting a letter:\nA Short names (3-6 letters)\nB Medium names (6-12 letters)\nC Long names (>12 letters)\n')
        if n_length.capitalize() in answers[:3]:
            print('Thanks for the choise')
            break
        else:
            print('Please enter a letter from the list\n',answers[:3])
            True
    return n_length

styles_option = {1:"Person names like Chanel",
                    2:"Rhyming words like SubHub and FireWire",
                    3:"Real words like Apple and Always",
                    4:"Foreign words like Iki and Toyota",
                    5:"Multiple words like Facebook"}

def get_style():
    print('Please select a name style:')
    for i in styles_option:
        print(str(i)+' '+styles_option[i])
    while True:
        try:
            n_style=int(input('Select a name style by writting a number:'))
            if n_style in styles_option.keys():
                print('Thank you for the answer')
                break
        except:
            print('Please enter a number from the list')
            print(range(1, 5))
    return n_style

def get_number():   
    while True:
        try:
            n_number=int(input('How many suggestions you would like to get?\nEnter 1-6\n'))
            if n_number  in range(max_number):
                print('Thank you for the answer')
                break
        except:
            print('Please enter suggestions number from the list:')
            print(range(max_number))
    return n_number

k_words=get_k_words()
w_length=get_length()
w_style=get_style()
w_type=get_number()

def read_dict_file(filename):
    with open(filename, 'r') as r:
        lines = r.read().strip().lower().split('\n')
    return lines

names_db=read_dict_file("first_names.txt")
words_db=read_dict_file("usa.txt")

def set_length(text_list, minimum, maximum):
    double=[x for x in text_list if  minimum < len(x) < maximum ]
    return double

def give_names(k_words, w_length, w_style, w_type):
    answer=[]
    if w_length.capitalize()=='A':
        minimum=2
        maximum=7
    elif w_length.capitalize()=='B':
        minimum=6
        maximum=13
    else:
        minimum=12
        maximum=99
   
    if w_style==1:
        names=set_length(names_db, minimum, maximum)
        for i in range(w_type):
            answer.append(random.choice(names))
    elif w_style==3:
        words=set_length(words_db, minimum, maximum)
        for i in range(w_type):
            answer.append(random.choice(words))
    elif w_style==4:
        translator = Translator()
        for w in k_words:
            destination=['lt', 'ja', 'fr', 'eo']
            for d in destination:
                foreign=translator.translate(w, dest=d, src='en')
                answer.append(foreign.text)
    elif w_style==5:
        words=set_length(words_db, int(minimum/2), int(maximum/2))
        for i in range(w_type):
            answer.append(random.choice(words)+random.choice(words))
    else:
        for i in range(w_type):
            answer.append(random.choice(words_db))
    return answer

suggestions=give_names(k_words, w_length, w_style, w_type)
print('1,2,3 - be ready!')
print('Your Startup can be named:')
for name in suggestions:
    print(name)
print('I hope you have find something you like!\nIf not, let`s try again')
