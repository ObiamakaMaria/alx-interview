#!/usr/bin/python3
"""A script containing a function to rotate a 2D
matrix 90 degrees clockwise, in place.
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise,
    in place.
    """
    n = len(matrix)  # Number of rows/columns
    y = n - 1  # Max index value for rows/columns

    # Reverse all columns
    for c in range(n):  # Iterate
        for r in range(int(n / 2)):
            buffer = matrix[r][c]
            matrix[r][c] = matrix[y - r][c]
            matrix[y - r][c] = buffer

    # Transpose the matrix
    for r in range(n):
        for c in range(r + 1, n):
            buffer = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = buffer
