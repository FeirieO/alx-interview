def rotate_2d_matrix(matrix):
    for i in range(len(matrix)):
        matrix[i].reverse()

    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[i][j], matrix[j][i]