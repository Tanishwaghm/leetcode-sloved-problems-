"""
LeetCode 20. Valid Parentheses
Determine if the input string of brackets is valid.

Approach: Stack-based matching. O(n) time, O(n) space.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return not stack


if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))  # True
