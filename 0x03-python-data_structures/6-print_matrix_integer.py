#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers.

    Args:
        matrix: matrix to be printed

    Returns:
        Nothing
    """
    for row in matrix:
        row_str = str(row).replace("[", "").replace("]", "").replace(",", "")
        print(row_str)
