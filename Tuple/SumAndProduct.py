'''
Write a function that calculates the sum and product of all elements in a tuple of numbers.
'''


def sum_product(input_tuple):
    tot, product = 0, 1
    for ele in input_tuple:
        tot += ele
        product *= ele

    return tot, product


sum_result, product_result = sum_product((1, 2, 3, 4))
print(sum_result, product_result)
