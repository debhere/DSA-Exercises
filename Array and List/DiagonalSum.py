'''
Given 2D list calculate the sum of diagonal elements.
'''


def diagonal_sum(matrix) -> int:
    total = 0
    for idx in range(len(matrix)):
        total += matrix[idx][idx]
    return total


print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
