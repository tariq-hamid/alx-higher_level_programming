#!/usr/bin/python3
""" Module containing a function that multiplies two matrices """


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices

    Args:
        m_a: first matrices
        m_b: second matrices

    Returns:
        multiplication of two m_a and m_b
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list ")
    if type(m_b) != list:
        raise TypeError("m_b must be a list ")
    for element in m_a:
        if type(element) != list:
            raise TypeError("m_a must be a list of lists")
    for element in m_b:
        if type(element) != list:
            raise TypeError("m_b must be a list of lists")
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
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_new = []
    row_new = []
    tmp = 0
    for row in m_a:
        for i in range(len(m_b[0])):
            for j in range(len(row)):
                tmp += row[j] * m_b[j][i]
            row_new.append(tmp)
            tmp = 0
        m_new.append(row_new)
        row_new = []
    return m_new
