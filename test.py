import string

with open('test.data.txt') as file:

    names = [_.replace('"', '') for _ in next(file).split(',')]

    sorted_names = sorted(names)

def count_letters_sum(input_string):
    """A function that counts a sum of serial numbers of every letter in an input word"""
    letters_sum = 0

    for char in input_string.lower():

        letters_sum += string.ascii_lowercase.index(char) + 1

    return letters_sum

def count_total(input_list):
    """A function that counts a total sum of all name scores,
     where a name score is a sum of serial numbers of every letter in an input word
     multiplied by the name's positional number in a list"""
    total = 0
    for val in input_list:
        total += (input_list.index(val) + 1) * count_letters_sum(val)

    return total

print(count_total(sorted_names))