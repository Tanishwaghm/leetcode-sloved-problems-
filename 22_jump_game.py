"""
LeetCode 55. Jump Game
Determine if you can reach the last index given max jump lengths at each index.

Approach: Greedy, track furthest reachable index while scanning. O(n) time, O(1) space.
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, num in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + num)
        return True


if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))  # True
    print(Solution().canJump([3, 2, 1, 0, 4]))  # False
