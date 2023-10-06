#!/usr/bin/python3
"""divide a matrix module"""


def matrix_divided(matrix, div):
    """funciton a divide a matrix

    Args:
        matrix: a list of lists
        div(int): what to divide the matrix by
    Returns:
        the divided matrix
    """
    new_matrix = []
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        first_row = len(matrix[0])
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            res = "{:.2f}".format(element/div)
            new_row.append(float(res))
        new_matrix.append(new_row)

    return new_matrix
