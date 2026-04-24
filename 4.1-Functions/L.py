def find_mountains(matrix):
    result = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] > max(
                max(matrix[i - 1][j - 1:j + 2]),
                max(matrix[i + 1][j - 1:j + 2]),
                matrix[i][j - 1],
                matrix[i][j + 1]
            ):
                result.append((i + 1, j + 1))
    return tuple(result)