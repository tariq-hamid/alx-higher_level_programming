#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers.

    Args:
        matrix: matrix to be printed

    Returns:
        Nothing
    """
    if not len(matrix[0]) and len(matrix) == 1:
        print("")
    for row in matrix:
        for element in row:
            if row.index(element) == len(row) - 1:
                print("{:d}".format(element))
                continue
            print("{:d}".format(element), end=" ")
