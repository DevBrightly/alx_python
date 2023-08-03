def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        result_row = [element ** 2 for element in row]
        result_matrix.append(result_row)
    return result_matrix
