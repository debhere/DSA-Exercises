'''
Find a number in an array
'''

from array import *


def find_number(arr, number) -> None:
    isExists = False
    for num in range(len(arr)):
        if arr[num] == number:
            isExists = True

    if isExists:
        print('{} exists in the array'.format(number))
    else:
        print('{} does not exist in the array'.format(number))


ser = [20, 45, 67, 80, 1, 59, 60, 44]
numberList = array('i', ser)

find_number(numberList, 100)
