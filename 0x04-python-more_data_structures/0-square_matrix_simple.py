#!/urs/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    for i in matrix:
        inner_matrix = []
        for j in i:
            inner_matrix.append(j ** 2)
        new_matrix.append(inner_matrix)

    return new_matrix
