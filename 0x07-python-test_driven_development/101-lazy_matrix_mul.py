#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    if m_b == [] or m_b == [[]]:
        TypeError("m_b cannot be empty")
    if (not isinstance(m_a, list) or m_a == [] or
            not all(isinstance(row, list) for row in m_a) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in m_a for num in row])):
        raise TypeError("m_a must be a list")
    if (not isinstance(m_b, list) or m_b == [] or
            not all(isinstance(row, list) for row in m_b) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in m_b for num in row])):
        raise TypeError("m_b must be a list")
    return (np.matmul(m_a, m_b))
