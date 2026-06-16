"""
LeetCode 5. Longest Palindromic Substring
Return the longest palindromic substring of s.

Approach: Expand around center for every index (odd and even length). O(n^2) time, O(1) space.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        best = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            best = max(best, odd, even, key=len)
        return best


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))  # "bab" or "aba"
