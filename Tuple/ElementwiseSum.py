'''
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
'''


def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))


output_tuple = tuple_elementwise_sum((1, 2, 3), (4, 5, 6))
print(output_tuple)
