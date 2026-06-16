"""
LeetCode 121. Best Time to Buy and Sell Stock
Maximize profit from a single buy and a single sell.

Approach: Track minimum price seen so far and best profit. O(n) time, O(1) space.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best, price - min_price)
        return best


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5
