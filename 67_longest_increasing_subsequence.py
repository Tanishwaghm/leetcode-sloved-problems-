"""
LeetCode 300. Longest Increasing Subsequence
Find the length of the longest strictly increasing subsequence.

Approach: Patience sorting with binary search (tails array). O(n log n) time.
"""
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []
        for num in nums:
            i = bisect.bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
