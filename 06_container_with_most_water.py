"""
LeetCode 11. Container With Most Water
Find two lines that together with the x-axis form a container holding the most water.

Approach: Two pointers from both ends, always move the shorter side. O(n) time, O(1) space.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            h = min(height[left], height[right])
            best = max(best, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
