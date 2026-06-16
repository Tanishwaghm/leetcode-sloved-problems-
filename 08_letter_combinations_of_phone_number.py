"""
LeetCode 17. Letter Combinations of a Phone Number
Return all letter combinations that the number could represent.

Approach: Backtracking over each digit's mapped letters. O(4^n) time worst case.
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        res = []

        def backtrack(index: int, path: List[str]) -> None:
            if index == len(digits):
                res.append("".join(path))
                return
            for ch in mapping[digits[index]]:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))  # ['ad','ae','af','bd','be','bf','cd','ce','cf']
