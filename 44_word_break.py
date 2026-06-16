"""
LeetCode 139. Word Break
Determine if s can be segmented into a sequence of dictionary words.

Approach: DP where dp[i] = can segment s[:i]. O(n^2) time, O(n) space.
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))  # True
