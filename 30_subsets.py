"""
LeetCode 78. Subsets
Return all possible subsets (the power set) of a distinct integer array.

Approach: Backtracking, add path at every recursive call. O(2^n) time.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]) -> None:
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
