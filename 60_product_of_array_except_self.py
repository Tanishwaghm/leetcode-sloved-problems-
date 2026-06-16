"""
LeetCode 238. Product of Array Except Self
Return an array where each element is the product of all other elements, no division.

Approach: Prefix products from the left, then suffix products from the right. O(n) time, O(1) extra space.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
