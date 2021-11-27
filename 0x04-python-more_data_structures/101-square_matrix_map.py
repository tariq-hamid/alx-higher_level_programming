#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(
        map(lambda el: list(map(lambda i: pow(i, 2), el)), matrix)
    )
