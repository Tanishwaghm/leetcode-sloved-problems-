"""
LeetCode 322. Coin Change
Find the fewest number of coins needed to make up a given amount.

Approach: Bottom-up DP over amounts 0..target. O(amount * len(coins)) time.
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))  # 3
