"""
LeetCode 48. Rotate Image
Rotate an n x n matrix 90 degrees clockwise, in place.

Approach: Transpose the matrix, then reverse each row. O(n^2) time, O(1) extra space.
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(m)
    print(m)  # [[7,4,1],[8,5,2],[9,6,3]]
