"""
LeetCode 31. Next Permutation
Rearrange numbers into the lexicographically next greater permutation, in place.

Approach: Find pivot from right where order breaks, swap with next larger, reverse suffix.
O(n) time, O(1) space.
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


if __name__ == "__main__":
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    print(nums)  # [1, 3, 2]
