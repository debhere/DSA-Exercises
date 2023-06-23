'''
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
'''


def merge_dicts(dict1, dict2):
    common_key = {}
    keys = list(dict1.keys()) + list(dict2.keys())

    for key in keys:
        common_key[key] = dict1.get(key, 0) + dict2.get(key, 0)

    return common_key


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))
