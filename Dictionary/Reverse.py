'''
Define a function which takes as a parameter dictionary and
returns a dictionary in which everse the key-value pairs are reversed.
'''


def reverse_dict(my_dict):

    rev = {value: key for key, value in my_dict.items()}
    return rev


print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))
