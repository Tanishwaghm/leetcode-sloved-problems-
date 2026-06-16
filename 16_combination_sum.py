"""
LeetCode 39. Combination Sum
Find all unique combinations of candidates that sum to target (reuse allowed).

Approach: Backtracking with sorted candidates and pruning. O(2^n) worst case.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > remaining:
                    break
                path.append(c)
                backtrack(i, remaining - c, path)
                path.pop()

        backtrack(0, target, [])
        return res


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
