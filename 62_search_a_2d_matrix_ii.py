"""
LeetCode 240. Search a 2D Matrix II
Search for a target in a matrix sorted ascending across rows and columns.

Approach: Start at top-right corner, move left if too big, down if too small. O(m + n) time.
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            if val > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(Solution().searchMatrix(matrix, 5))  # True
