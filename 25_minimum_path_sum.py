"""
LeetCode 64. Minimum Path Sum
Find the path from top-left to bottom-right minimizing the sum of values.

Approach: DP in place on the grid. O(m*n) time, O(1) extra space.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


if __name__ == "__main__":
    print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # 7
