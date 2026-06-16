"""
LeetCode 62. Unique Paths
Count the number of unique paths from top-left to bottom-right of an m x n grid.

Approach: Dynamic programming, 1D rolling row. O(m*n) time, O(n) space.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]


if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7))  # 28
