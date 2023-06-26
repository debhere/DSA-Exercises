'''
Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
'''


def get_diagonal(tup):
    return tuple(tup[idx][idx] for idx in range(len(tup)))


inp = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(get_diagonal(inp))
