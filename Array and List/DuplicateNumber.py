'''
Write a function to remove the duplicate numbers on given integer array/list.
'''


def remove_duplicates(arr) -> list:
    distNums = list(set(arr))
    return distNums


print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
