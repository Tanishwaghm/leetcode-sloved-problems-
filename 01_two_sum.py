"""
LeetCode 1. Two Sum
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

Approach: Hash map storing value -> index. O(n) time, O(n) space.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))  # [0, 1]
