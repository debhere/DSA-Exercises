'''
What is the runtime of the below code?
'''


def foo(array):
    sum = 0  # O(1)
    product = 1  # O(1)

    for i in array: #O(n)
        sum += i # O(1)

    for i in array:
        product += i

    print("Sum = " + str(sum) + "Product = " + str(product))

#

def printPairs(array):
    for i in array:
        for j in array:
            print(str(i) + "," + str(j))
