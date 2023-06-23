'''
Define a function which takes two lists as parameters and
check if two given lists have the same frequency of elements.
'''


def check_same_frequency(list1, list2):
    list1.sort()
    list2.sort()
    return True if sum(map(lambda x, y: list1.count(x) == list2.count(y), list1, list2)) == len(list1) \
        else False


print(check_same_frequency([3, 2, 3, 1, 1], [3, 1, 2, 1, 3]))
