"""
LeetCode 70. Climbing Stairs
Count distinct ways to climb n stairs taking 1 or 2 steps at a time.

Approach: Fibonacci-style DP with two rolling variables. O(n) time, O(1) space.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1


if __name__ == "__main__":
    print(Solution().climbStairs(5))  # 8
