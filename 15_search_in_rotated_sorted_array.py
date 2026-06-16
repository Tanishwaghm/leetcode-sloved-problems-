"""
LeetCode 33. Search in Rotated Sorted Array
Search for target in a rotated sorted array in O(log n).

Approach: Modified binary search, decide which half is properly sorted.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


if __name__ == "__main__":
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
