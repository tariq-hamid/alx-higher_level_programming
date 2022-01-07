#!/usr/bin/python3
""" Module containing a function that multiplies two matrices """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices using Numpy

    Args:
        m_a: first matrices
        m_b: second matrices

    Returns:
        multiplication of two m_a and m_b
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for i in row:
            if not (type(i) in [int, float]):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if not (type(i) in [int, float]):
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    return np.matmul(m_a, m_b)
