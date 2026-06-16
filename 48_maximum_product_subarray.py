"""
LeetCode 152. Maximum Product Subarray
Find the contiguous subarray with the largest product.

Approach: Track running max and min product (since negatives flip order). O(n) time, O(1) space.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = curr_max = curr_min = nums[0]
        for num in nums[1:]:
            candidates = (num, curr_max * num, curr_min * num)
            curr_max, curr_min = max(candidates), min(candidates)
            best = max(best, curr_max)
        return best


if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))  # 6
