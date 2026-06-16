"""
LeetCode 22. Generate Parentheses
Generate all combinations of well-formed parentheses for n pairs.

Approach: Backtracking, tracking open/close counts. O(4^n / sqrt(n)) time (Catalan number).
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path: List[str], open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                backtrack(path, open_count + 1, close_count)
                path.pop()
            if close_count < open_count:
                path.append(")")
                backtrack(path, open_count, close_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return res


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))  # ['((()))','(()())','(())()','()(())','()()()']
