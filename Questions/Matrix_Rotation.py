#Matrix Rotation
def rotate_matrix(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
    return matrix

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotated = rotate_matrix(matrix)
for row in rotated:
    print(row)
