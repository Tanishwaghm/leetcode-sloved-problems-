"""
LeetCode 84. Largest Rectangle in Histogram
Find the area of the largest rectangle in a bar-height histogram.

Approach: Monotonic increasing stack of indices. O(n) time, O(n) space.
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        return best


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
