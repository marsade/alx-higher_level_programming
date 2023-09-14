#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqMatrix = []
    for row in matrix:
        sqRow = [x*x for x in row]
        sqMatrix.append(sqRow)
    return sqMatrix
