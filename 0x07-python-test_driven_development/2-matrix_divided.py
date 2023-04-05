#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all elements of the matrix
    by a given div

    Args:
        matrix: list lists of integers or floats
        div: a divisor type int or float.
    
    Raises:
        TypeError:if matrix is not a list of lists of int or floats and if div is not in int or float.
        ZeroDivisionError:if div is equal to 0

     Returns:
         new matrix

    """
    if not all(isinstance(row, list) and all(isinstance(element,(int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeErrror("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        result_row = []
        for element in row:
            result_row.append(element / div)
            new_matrix.append(result_row)
            for row in new_matrix:
                for element in row:
                    print("{:.2f}".format(element), end=" ")
