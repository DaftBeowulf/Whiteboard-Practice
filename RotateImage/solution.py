# Given an matrix represented by an `NxN` matrix,
# where each pixel in the matrix is an integer from 0 to 9,
# write a function `rotatematrix` that rotates the matrix by 90 degrees
# in the counter-clockwise direction.

# For example:
# ```js
# rotatematrix([
#              [1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9]
#            ]);
# ```
# should return
# ```
# [
#   [3, 6, 9],
#   [2, 5, 8],
#   [1, 4, 7]
# ]
"""
[0,0] [0,1] [0,2]-> [2,0] [1,0] [0,0]
[1,0] [1,1] [1,2]-> [2,1] [1,1] [0,1]
[2,0] [2,1] [2,2]-> [2,2] [1,2] [0,2]
"""


def rotate(matrix):

    for row in matrix:
        row.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
