#!/usr/bin/python3

def matrix_divided(matrix, div):
    
    if(div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = deepcopy(matrix)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if(new_matrix[i][j]):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            res = round((new_matrix[i][j]/div),2)
            new_matrix[i][j] = res
    return new_matrix
    
    
def deepcopy(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        new_matrix.append(new_row)
    return new_matrix