"""
LeetCode 279. Perfect Squares
Find the minimum number of perfect square numbers that sum to n.

Approach: DP, dp[i] = 1 + min(dp[i - j*j]) for all valid squares j*j <= i. O(n * sqrt(n)) time.
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [float("inf")] * n
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


if __name__ == "__main__":
    print(Solution().numSquares(12))  # 3 (4+4+4)
