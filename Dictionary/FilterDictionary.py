'''
Define a function that takes a dictionary as a parameter and
returns a dictionary with elements based on a condition.
'''


def filter_dict(my_dict, condition):
    filtered = {k: v for k, v in my_dict.items() if condition(k, v)}
    return filtered


a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(filter_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4}, lambda k, v: v % 2 == 0))
print()
print(filter_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4}, lambda k, v: v % 2 != 0))

