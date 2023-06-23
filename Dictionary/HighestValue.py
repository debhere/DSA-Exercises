'''
Define a function which takes a dictionary as a parameter and
returns the key with the highest value in a dictionary.
'''


def max_value_key(my_dict):
    max_value = max(my_dict.values())
    max_key = ''
    for key in my_dict.keys():
        if my_dict[key] == max_value:
            max_key = key
            break

    return max_key


def max_key(my_dict):
    return max(my_dict, key=my_dict.get)

dict1 = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(dict1))
print(max_key(dict1))
