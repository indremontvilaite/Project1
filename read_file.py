def min_max(w_length):
    if w_length.capitalize() == "A":
        minimum = 2
        maximum = 7
    elif w_length.capitalize() == "B":
        minimum = 6
        maximum = 13
    else:
        minimum = 12
        maximum = 99
    return [minimum, maximum]


def read_dict_file(filename):
    with open(filename, "r") as r:
        lines = r.read().strip().lower().split("\n")
    return lines
