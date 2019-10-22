

print('Welcome! Find the name for your very new Startup\n Have no ideas? Let us help you!')
print('Choosing a name can be fun and easy!')
print('Get names ideas regarding your preferences\nLet\'s answer some question\'s')

def get_k_words():
    k_words = input('Enter key words about your Startup: ')
    for str(type(k_words)) != 'str':
        k_words = input('Wrong format, please enter words: ')
    k_list = k_words.split()
    return k_list

Answers = ('A', 'B', 'C', 'D','E')
Numbers = range(6)

def get_length():
    answers = ('A', 'B', 'C', 'D','E')
    n_length = ''
    while True:
        n_length = input('Select a name length by writting a letter:\nA Short names (3-6 letters)\nB Medium names (6-12 letters)\nC Long names (>12 letters)\n')
        print(n_length)
        if str(n_length).upper in answers[:3]:
            return n_length
            False
        else:
            print('Please enter a letter from the list\n',answers[:3])
            True

styles_option = {1:"Person names like Chanel",
                    2:"Rhyming words like SubHub and FireWire",
                    3:"Real words like Apple and Always",
                    4:"Foreign words like Iki and Toyota",
                    5:"Multiple words like Facebook"}
def get_style():
    print('Please select a name style:')
    for i in styles_option:
        print(str(i)+' '+styles_option[i])
    #print(styles_option)
    while True:
        n_style=input('Select a name style by writting a number:')
        if n_style in styles_option.keys():
            print('Thank you for the answer')
            break
        else:
            print('Please enter a letter from the list')
            print(str(Numbers[:5]))
    return n_style

def get_number():   
    while True:
        n_number=input('How many suggestions you would like to get?\nEnter 1-6\n')
        if n_number  in Numbers:
            False
            print('Thank you for the answer')
            break
        else:
            print('Please enter suggestions number from the list:')
            print(Numbers)
    return n_number

#get_k_words()
get_length()
get_style()
get_number()
