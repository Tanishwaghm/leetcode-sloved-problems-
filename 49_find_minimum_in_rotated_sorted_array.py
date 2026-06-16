"""
LeetCode 153. Find Minimum in Rotated Sorted Array
Find the minimum element in a rotated sorted array (no duplicates).

Approach: Binary search comparing mid to right boundary. O(log n) time.
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    print(Solution().findMin([3, 4, 5, 1, 2]))  # 1
