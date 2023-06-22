'''
Find the maximum product of two integers in an array where all elements are positive.
'''


def max_product(arr) -> int:
    rev_arr = arr.copy()
    rev_arr.sort(reverse=True)
    return rev_arr[0] * rev_arr[1]


print(max_product([1, 2, 3, 4, 5, 6, 9]))
