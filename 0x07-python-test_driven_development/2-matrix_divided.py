#!/usr/bin/python3
""" Module containing a function that does division on matrix """


def matrix_divided(matrix, div):
    """functions that divides all elements of a matrix

    Arguments:
        matrix: a matrix to be divided
        div: number to divide the matrix by

    Returns:
        a new matrix
    """
    for row in matrix:
        for i in row:
            if not (type(i) in [int, float]):
                raise TypeError("\
matrix must be a matrix (list of lists) of integers/floats")
    n = len(matrix[0])
    for row in matrix:
        if len(row) != n:
            raise TypeError("Each row of the matrix must have the same size")
    if not (type(div) in [int, float]):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")

    new_matrix = [row[:] for row in matrix]
    for row in new_matrix:
        for i in range(n):
            row[i] = round(row[i] / div, 2)

    return new_matrix
