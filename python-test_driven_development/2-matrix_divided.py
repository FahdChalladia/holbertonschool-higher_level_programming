#!/usr/bin/python3
"""
This module contains the function matrix_divided(matrix, div) that divides
all elements of a matrix by div with validation and rounding.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of int/float,
                   or if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        new_matrix (list of lists of float): The divided matrix.

    Example:
        matrix = [[1, 2, 3], [4, 5, 6]]
        matrix_divided(matrix, 3)
        # returns [[0.33, 0.67, 1.0],
        #          [1.33, 1.67, 2.0]]
    """
    # Validate matrix type and contents
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(not all(isinstance(el, (int, float)) for el in row)
            for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Validate all rows have the same size
    row_length = len(matrix[0]) if matrix else 0
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Compute the new matrix with rounded division
    new_matrix = []
    for row in matrix:
        new_row = [round(el / div, 2) for el in row]
        new_matrix.append(new_row)

    return new_matrix
