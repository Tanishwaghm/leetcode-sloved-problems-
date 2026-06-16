"""
LeetCode 53. Maximum Subarray
Find the contiguous subarray with the largest sum.

Approach: Kadane's algorithm. O(n) time, O(1) space.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for num in nums[1:]:
            curr = max(num, curr + num)
            best = max(best, curr)
        return best


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
