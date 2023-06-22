'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''


def contains_duplicate(nums) -> bool:
    isExist = False
    unique = list(set(nums))
    if len(unique) < len(nums):
        isExist = True
    return isExist


print(contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
