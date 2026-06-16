"""
LeetCode 128. Longest Consecutive Sequence
Find the length of the longest run of consecutive integers in an unsorted array.

Approach: Hash set, only start counting from the beginning of a run. O(n) time, O(n) space.
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                curr = num
                while curr + 1 in num_set:
                    curr += 1
                    length += 1
                best = max(best, length)
        return best


if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
