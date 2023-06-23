'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
'''

import numpy as np


def rotate_matrix(matrix):
    row, col = matrix.shape
    res = matrix.copy()
    element_list = []
    for idx in range(col):
        temp = res[:, idx]
        element_list.append(np.flip(temp))

    rotated = np.array(element_list)
    return rotated


def rotate(matrix):
    rotated = list()
    for i in range(len(matrix)):
        temp = list()
        for j in reversed(range(len(matrix))):
            temp.append(matrix[j][i])
        rotated.append(temp)

    return rotated




#ar = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# abb = arr.T
#print(ar)
print()
# print(abb)

# print(arr[2:, 2:])
# m, n = arr.shape
# print(m, n)
# #arr = np.array([[1, 2],
#                 [3, 4],
#                 [5, 6]])
ar = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ar)
print(rotate(ar))
