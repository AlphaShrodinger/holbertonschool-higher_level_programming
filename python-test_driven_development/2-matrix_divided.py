#!/usr/bin/python3
"""matrix_div
    """


def matrix_divided(matrix, div):
    """divides matrix"""
    e = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(e)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) not in (int, float):
                raise TypeError(e)
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
