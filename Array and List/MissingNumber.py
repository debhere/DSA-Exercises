'''
Write a function to find the missing number in a given integer array of 1 to 100.
'''


def missing_number(arr, n):
    num = -1
    for i in range(1, n + 1):
        if i not in arr:
            num = i
    return num


print(missing_number([1, 2, 3, 4, 5, 7, 8], 8))


def get_missing_number(arr, n):
    total = n * (n + 1) // 2
    sum_arr = sum(arr)
    missing = total - sum_arr
    return missing


print(get_missing_number([1, 2, 3, 4, 5, 7, 8], 8))
