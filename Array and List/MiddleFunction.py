'''
Write a function called middle that takes a list and returns
a new list that contains all but the first and last elements.
'''


def middle(arr) -> list:
    mid_arr = arr[1:-1]
    return mid_arr


print(middle([1, 2, 3, 4]))
