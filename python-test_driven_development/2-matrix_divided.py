#!/usr/bin/python3
'''
This is the "2-matrix_divided" module.
The example module supplies one function, def matrix_divided().
'''

def matrix_divided(matrix, div):
    '''
    Returns new list of lists diveded by div argument
    '''
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    max_len = max(len(item) for item in matrix)
    for sublist in matrix:
        if len(sublist) != max_len:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(sublist[:])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
    return new_matrix
