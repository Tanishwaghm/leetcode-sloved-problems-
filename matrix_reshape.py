def matrix_reshape(mat, r, c):

    rows = len(mat)
    cols = len(mat[0])

    if rows * cols != r * c:
        return mat

    numbers = []

    for row in mat:
        for num in row:
            numbers.append(num)

    result = []
    index = 0

    for i in range(r):
        row = []

        for j in range(c):
            row.append(numbers[index])
            index += 1

        result.append(row)

    return result
