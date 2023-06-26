'''
Write a function that takes two tuples and returns a tuple containing
the common elements of the input tuples.
'''


def get_common_elements(tuple1, tuple2):
    return tuple(element for element in tuple1 if element in tuple2)


# return tuple(set(tuple1) & set(tuple2))

inp1 = (1, 2, 3, 4, 5)
inp2 = (4, 5, 6, 7, 8)
output_tuple = get_common_elements(inp1, inp2)
print(output_tuple)
