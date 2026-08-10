def can_be_rotated(mat, target):

    for _ in range(4):

        if mat == target:
            return True

        n = len(mat)

        # Rotate 90 degrees
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        for row in mat:
            row.reverse()

    return False
