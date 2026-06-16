"""
LeetCode 338. Counting Bits
For every number from 0 to n, count the number of set bits.

Approach: DP using the relation bits[i] = bits[i >> 1] + (i & 1). O(n) time.
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


if __name__ == "__main__":
    print(Solution().countBits(5))  # [0,1,1,2,1,2]
