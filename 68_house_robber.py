"""
LeetCode 198. House Robber
Maximize the amount robbed without robbing two adjacent houses.

Approach: DP with two rolling variables (rob vs skip current house). O(n) time, O(1) space.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1


if __name__ == "__main__":
    print(Solution().rob([2, 7, 9, 3, 1]))  # 12
