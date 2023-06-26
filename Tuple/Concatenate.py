'''
Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
'''


def concatenate_strings(input_tuple):
    concat = ' '.join(input_tuple)
    return concat


output_string = concatenate_strings(('Hello', 'World', 'from', 'Python'))
print(output_string)
