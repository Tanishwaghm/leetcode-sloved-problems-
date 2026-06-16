"""
LeetCode 3. Longest Substring Without Repeating Characters
Find the length of the longest substring without repeating characters.

Approach: Sliding window with a hash map of last seen index. O(n) time, O(min(n, m)) space.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
