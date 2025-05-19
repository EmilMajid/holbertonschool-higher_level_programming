#!/usr/bin/python3
'''
This is the "2-matrix_divided" module.
The example module supplies one function, def matrix_divided().
'''

def matrix_divided(matrix, div):
    '''
    Returns new list of lists diveded by div argument
    '''

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    try:
        new_matrix = matrix.copy()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new_matrix[i][j] /= div
    except TypeError:
        print("matrix must be a matrix (list of lists) of integers/floats")
    except ZeroDivissionError:
        print("division by zero")
    return new_matrix, matrix
