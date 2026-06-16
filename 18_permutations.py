"""
LeetCode 46. Permutations
Return all possible permutations of a distinct integer array.

Approach: Backtracking with a used-boolean array. O(n!) time.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path: List[int]) -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
