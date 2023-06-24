'''
Write a function that takes a tuple and a value,
and returns a new tuple with the value inserted at the beginning of the original tuple.
'''


def insert_value_front(input_tuple, value_to_insert):
    new_tuple = (value_to_insert, )
    new_tuple += input_tuple
    return new_tuple


output_tuple = insert_value_front((2, 3, 4), 1)
print(output_tuple)
