class InputList:
    def __init__(self, k_words):
        self.k_words = k_words
    def get_k_words():
        while True:
            k_words = input("Enter key words about your Startup:\n")
            if len(k_words.split()) < 2:
                k_words = input("Not enough entry, please enter some words: ")
            else:
                k_list = k_words.split()
                print("Thanks for the key words")
                break
        return k_list

max_number = 7

def get_length():
    answers = ("A", "B", "C", "D", "E")
    n_length = ""
    while True:
        n_length = input(
            "Select a name length by writting a letter:\nA Short names (3-6 letters)\nB Medium names (6-12 letters)\nC Long names (>12 letters)\n"
        )
        if n_length.capitalize() in answers[:3]:
            print("Thanks for the choise")
            break
        else:
            print("Please enter a letter from the list\n", answers[:3])
            True
    return n_length

styles_option = {
    1: "Person names like Chanel",
    2: "Rhyming words like SubHub and FireWire",
    3: "Real words like Apple and Always",
    4: "Foreign words like Iki and Toyota",
    5: "Multiple words like Facebook",
    6: "Misspelled words like Lyft",
}

def get_style():
    print("Please select a name style:")
    for i in styles_option:
        print(str(i) + " " + styles_option[i])
    while True:
        try:
            n_style = int(input("Select a name style by writting a number:"))
            if n_style in styles_option.keys():
                print("Thank you for the answer")
                break
        except BaseException:
            print("Please enter a number from the list")
            print(range(1, 5))
    return n_style

def get_number():
    while True:
        try:
            n_number = int(
                input("How many suggestions you would like to get?\nEnter 1-6\n")
            )
            if n_number in range(max_number):
                print("Thank you for the answer")
                break
        except BaseException:
            print("Please enter suggestions number from the list:")
            print(range(max_number))
    return n_number
