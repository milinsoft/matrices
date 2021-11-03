asymmetric_matrix = [['1', '2', '0', '_', '_'],
                     ['_', '3', '4', '0', '_'],
                     ['_', '_', '0', '8', '6'],
                     ['7', '_', '_', '-9', '0'],
                     ['5', '-1', '_', '_', '7']]





def fill_asymmetrix_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix)):
            # print(matrix[row][column])
            if matrix[row][column] != matrix[column][row]:
                if matrix[row][column] == "_" and matrix[column][row].lstrip("-").isdigit():
                    matrix[row][column] = matrix[column][row]
                elif matrix[column][row] == "_" and matrix[row][column].lstrip("-"):
                    matrix[column][row] = matrix[row][column]

    return symmetric_matrix


m1 = fill_asymmetrix_matrix(asymmetric_matrix)

print(*m1, sep="\n")
