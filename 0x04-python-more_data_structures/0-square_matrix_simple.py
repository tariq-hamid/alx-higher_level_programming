#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Function that computes the square
    value of all integers of a matrix.

    Args:
        matrix: matrix to be used

    Returns:
        New matrix
    """
    new_squared_matrix = list(
        map(lambda el: list(map(lambda i: pow(i, 2), el)), matrix)
    )
    return new_squared_matrix
